#!/bin/bash
# 檢查小說章節完整性
# 驗證章節列表、導航鏈接和網站結構

set -e

echo "🔍 開始檢查小說章節完整性..."
echo "時間: $(date '+%Y-%m-%d %H:%M:%S')"

cd "$(dirname "$0")"
ERRORS=0
WARNINGS=0

# 1. 獲取最新章節編號
get_latest_chapter() {
    ls -1 chapter-*.html 2>/dev/null | grep -oP 'chapter-\K[0-9]+' | sort -n | tail -1
}

# 2. 檢查章節檔案
check_chapter_files() {
    echo "📄 檢查章節檔案..."
    
    local chapters
    chapters=$(ls -1 chapter-*.html 2>/dev/null | grep -oP 'chapter-\K[0-9]+' | sort -n)
    
    if [ -z "$chapters" ]; then
        echo "❌ 未找到任何章節檔案"
        ((ERRORS++))
        return
    fi
    
    local total=0
    for chapter in $chapters; do
        if [ -f "chapter-${chapter}.html" ]; then
            ((total++))
        else
            echo "❌ 章節檔案缺失: chapter-${chapter}.html"
            ((ERRORS++))
        fi
    done
    
    echo "✅ 找到 $total 個章節檔案"
}

# 3. 檢查最新章節是否在首頁
check_latest_chapter_in_index() {
    echo "🏠 檢查首頁章節列表..."
    
    local latest_chapter
    latest_chapter=$(get_latest_chapter)
    
    if [ -z "$latest_chapter" ]; then
        echo "⚠️ 無法確定最新章節"
        ((WARNINGS++))
        return
    fi
    
    if grep -q "href=\"chapter-${latest_chapter}.html\"" index.html; then
        echo "✅ 最新章節（第${latest_chapter}章）在首頁中"
    else
        echo "❌ 最新章節（第${latest_chapter}章）不在首頁中"
        ((ERRORS++))
    fi
    
    # 檢查是否在最頂部（應該是最新章節）
    local chapter_list_line
    chapter_list_line=$(grep -n "<ul class=\"chapter-list\">" index.html | head -1 | cut -d: -f1)
    if [ -n "$chapter_list_line" ]; then
        local next_line=$((chapter_list_line + 1))
        if sed -n "${next_line}p" index.html | grep -q "chapter-${latest_chapter}.html"; then
            echo "✅ 最新章節在列表頂部"
        else
            echo "⚠️ 最新章節不在列表頂部（應該在最前面）"
            ((WARNINGS++))
        fi
    fi
}

# 4. 檢查章節導航
check_chapter_navigation() {
    echo "🧭 檢查章節導航..."
    
    local chapters
    chapters=$(ls -1 chapter-*.html 2>/dev/null | grep -oP 'chapter-\K[0-9]+' | sort -n)
    local latest_chapter
    latest_chapter=$(get_latest_chapter)
    
    for chapter in $chapters; do
        local file="chapter-${chapter}.html"
        
        if [ ! -f "$file" ]; then
            continue
        fi
        
        # 檢查是否有 footer 導航
        if ! grep -q "<footer class=\"reader-footer-nav\">" "$file"; then
            echo "❌ ${file}: 缺少導航 footer"
            ((ERRORS++))
            continue
        fi
        
        # 檢查按鈕數量
        local button_count
        button_count=$(grep -c "class=\"nav-button\"" "$file" || true)
        
        if [ "$chapter" -eq 1 ]; then
            # 第一章應該只有「下一章」或「返回目錄」
            if [ "$button_count" -lt 1 ]; then
                echo "❌ ${file}: 第一章需要至少1個導航按鈕"
                ((ERRORS++))
            fi
        elif [ "$chapter" -eq "$latest_chapter" ]; then
            # 最新章節應該有「上一章」和「返回目錄」
            if [ "$button_count" -ne 2 ]; then
                echo "⚠️ ${file}: 最新章節應該有2個按鈕（上一章 + 返回目錄）"
                ((WARNINGS++))
            fi
            
            # 檢查是否包含「返回目錄」
            if ! grep -q "href=\"index.html\".*返回目錄" "$file"; then
                echo "❌ ${file}: 最新章節缺少「返回目錄」按鈕"
                ((ERRORS++))
            fi
        else
            # 中間章節應該有「上一章」和「下一章」
            if [ "$button_count" -ne 2 ]; then
                echo "⚠️ ${file}: 第${chapter}章應該有2個按鈕（上一章 + 下一章）"
                ((WARNINGS++))
            fi
            
            # 檢查下一章鏈接是否正確
            local next_chapter=$((chapter + 1))
            if ! grep -q "href=\"chapter-${next_chapter}.html\".*下一章" "$file"; then
                echo "❌ ${file}: 缺少或錯誤的「下一章」鏈接（應該指向第${next_chapter}章）"
                ((ERRORS++))
            fi
        fi
    done
}

# 5. 檢查首頁更新日期
check_update_date() {
    echo "📅 檢查更新日期..."
    
    local current_year
    current_year=$(date +%Y)
    
    if grep -q "最後更新：.*${current_year}" index.html; then
        echo "✅ 最後更新日期包含今年"
    else
        echo "⚠️ 最後更新日期可能過時"
        ((WARNINGS++))
    fi
}

# 6. 檢查所有鏈接是否有效
check_all_links() {
    echo "🔗 檢查鏈接有效性..."
    
    # 檢查首頁中的所有章節鏈接
    grep -o 'href="chapter-[0-9]*\.html"' index.html | sort -u | while read -r link; do
        local filename
        filename=$(echo "$link" | sed 's/href="//' | sed 's/"//')
        
        if [ ! -f "$filename" ]; then
            echo "❌ 鏈接指向不存在的檔案: $filename"
            ((ERRORS++))
        fi
    done
}

# 7. 檢查 GitHub 狀態
check_git_status() {
    echo "🐙 檢查 Git 狀態..."
    
    if command -v git >/dev/null 2>&1; then
        if git status --porcelain | grep -q "^ M"; then
            echo "⚠️ 有未提交的修改"
            ((WARNINGS++))
        fi
        
        local ahead
        ahead=$(git status --porcelain -b | grep -o 'ahead [0-9]*' | grep -o '[0-9]*' || echo "0")
        if [ "$ahead" -gt 0 ]; then
            echo "⚠️ 有 $ahead 個未推送的提交"
            ((WARNINGS++))
        fi
    else
        echo "ℹ️ Git 命令不可用"
    fi
}

# 執行所有檢查
check_chapter_files
check_latest_chapter_in_index
check_chapter_navigation
check_update_date
check_all_links
check_git_status

# 輸出總結
echo ""
echo "=== 檢查總結 ==="
echo "時間: $(date '+%Y-%m-%d %H:%M:%S')"
echo "✅ 檢查完成"
echo "錯誤: $ERRORS"
echo "警告: $WARNINGS"

if [ $ERRORS -gt 0 ]; then
    echo "❌ 發現 $ERRORS 個錯誤，需要修復"
    exit 1
elif [ $WARNINGS -gt 0 ]; then
    echo "⚠️ 發現 $WARNINGS 個警告，建議檢查"
    exit 0
else
    echo "🎉 所有檢查通過，章節完整性良好"
    exit 0
fi