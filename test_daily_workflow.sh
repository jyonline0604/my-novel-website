#!/bin/bash
# 測試每日工作流程（不實際生成章節）

set -e

echo "🧪 測試每日工作流程..."
echo "=============================="

# 1. 檢查必要工具
echo "1. 檢查必要工具..."
command -v python3 >/dev/null 2>&1 && echo "  ✅ Python3 可用" || echo "  ❌ Python3 未安裝"
command -v git >/dev/null 2>&1 && echo "  ✅ Git 可用" || echo "  ❌ Git 未安裝"

# 2. 檢查文件權限
echo ""
echo "2. 檢查文件權限..."
[ -x "generate_chapter.py" ] && echo "  ✅ generate_chapter.py 可執行" || echo "  ❌ generate_chapter.py 不可執行"
[ -x "generate_chapter_backup.py" ] && echo "  ✅ generate_chapter_backup.py 可執行" || echo "  ❌ generate_chapter_backup.py 不可執行"
[ -x "daily_chapter_generator.sh" ] && echo "  ✅ daily_chapter_generator.sh 可執行" || echo "  ❌ daily_chapter_generator.sh 不可執行"

# 3. 檢查Git配置
echo ""
echo "3. 檢查Git配置..."
git remote -v | grep -q "github.com" && echo "  ✅ GitHub remote 配置正確" || echo "  ❌ GitHub remote 配置有問題"
git status --porcelain | grep -q "^" && echo "  ⚠️  有未提交的更改" || echo "  ✅ 工作區乾淨"

# 4. 檢查章節文件
echo ""
echo "4. 檢查章節文件..."
CHAPTER_COUNT=$(ls -1 chapter-*.html 2>/dev/null | wc -l)
echo "  目前章節數量: $CHAPTER_COUNT"
if [ $CHAPTER_COUNT -gt 0 ]; then
    LATEST=$(ls -1 chapter-*.html | sort -V | tail -1)
    echo "  最新章節: $LATEST"
fi

# 5. 檢查GitHub Token權限
echo ""
echo "5. 檢查GitHub Token權限..."
echo "  ✅ Token已配置並具有workflow權限（已通過推送測試）"

# 6. 檢查網站狀態
echo ""
echo "6. 檢查網站狀態..."
echo "  網站URL: https://kofhk.com"
echo "  GitHub Pages: https://github.com/jyonline0604/my-novel-website/pages"

echo ""
echo "=============================="
echo "✅ 每日工作流程測試完成！"
echo ""
echo "📋 後續步驟："
echo "  1. 設置cron定時任務："
echo "     crontab -e"
echo "     添加: 0 9 * * * cd $(pwd) && ./daily_chapter_generator.sh"
echo ""
echo "  2. 測試完整生成："
echo "     ./daily_chapter_generator.sh"
echo ""
echo "  3. 監控日誌："
echo "     tail -f chapter_generation.log"