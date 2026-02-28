#!/bin/bash
# 更新章節導航和首頁列表
# 用法：./update_chapter_nav.sh <新章節編號> <新章節標題>

set -e

if [ $# -lt 2 ]; then
    echo "用法: $0 <章節編號> <章節標題>"
    exit 1
fi

NEXT_CHAPTER="$1"
CHAPTER_TITLE="$2"
PREV_CHAPTER=$((NEXT_CHAPTER - 1))

echo "🔧 更新章節導航：第${NEXT_CHAPTER}章（${CHAPTER_TITLE}）"

# 1. 更新 index.html：在章節列表頂部添加新章節
echo "📝 更新首頁章節列表..."
python3 << PYEOF
import re
import sys

index_file = 'index.html'
next_chapter = int('${NEXT_CHAPTER}')
chapter_title = '${CHAPTER_TITLE}'
date_str = '$(date "+%Y-%m-%d")'

# 讀取 index.html
with open(index_file, 'r', encoding='utf-8') as f:
    content = f.read()

# 構建新章節項目
new_chapter_item = f'''                <li class="chapter-item">
                    <a href="chapter-{next_chapter}.html" class="chapter-link">
                        <span class="chapter-title">第{next_chapter}章：{chapter_title}</span>
                        <span class="chapter-date">{date_str}</span>
                    </a>
                </li>'''

# 找到章節列表位置並插入
# 尋找 <ul class="chapter-list"> 後的空白行，然後第一個 <li>
pattern = r'(<ul class="chapter-list">\s*\n)(\s*<li class="chapter-item">)'
replacement = r'\1' + new_chapter_item + r'\n\2'

new_content = re.sub(pattern, replacement, content, count=1, flags=re.DOTALL)

if new_content == content:
    # 如果替換失敗，嘗試另一種模式
    pattern2 = r'(<ul class="chapter-list">\s*\n\s*)'
    replacement2 = r'\1' + new_chapter_item + r'\n'
    new_content = re.sub(pattern2, replacement2, content, count=1, flags=re.DOTALL)

# 寫回文件
with open(index_file, 'w', encoding='utf-8') as f:
    f.write(new_content)

print(f"✅ 已添加第{next_chapter}章到首頁")
PYEOF

# 2. 更新前一章節的footer：將「返回目錄」改為「下一章」
if [ $PREV_CHAPTER -ge 1 ]; then
    echo "🔄 更新第${PREV_CHAPTER}章導航..."
    PREV_FILE="chapter-${PREV_CHAPTER}.html"
    
    if [ -f "$PREV_FILE" ]; then
        python3 << PYEOF
import re

prev_file = '${PREV_FILE}'
next_chapter = int('${NEXT_CHAPTER}')

# 讀取前一章節文件
with open(prev_file, 'r', encoding='utf-8') as f:
    content = f.read()

# 尋找 footer 中的「返回目錄」按鈕並改為「下一章」
pattern = r'(<footer class="reader-footer-nav">\s*<a href="chapter-[0-9]+\.html" class="nav-button">« 上一章</a>\s*)<a href="index\.html" class="nav-button">返回目錄</a>'
replacement = r'\1<a href="chapter-' + str(next_chapter) + '.html" class="nav-button">下一章 »</a>'

new_content = re.sub(pattern, replacement, content, count=1, flags=re.DOTALL)

if new_content != content:
    # 寫回文件
    with open(prev_file, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"✅ 已更新第{prev_file}的導航：返回目錄 → 下一章")
else:
    # 嘗試另一種模式：可能已經是「下一章」了
    pattern2 = r'(<footer class="reader-footer-nav">\s*<a href="chapter-[0-9]+\.html" class="nav-button">« 上一章</a>\s*)<a href="[^"]*" class="nav-button">[^<]*</a>'
    match = re.search(pattern2, content)
    if match:
        print(f"ℹ️ 第{prev_file}的導航可能已正確設置")
    else:
        print(f"⚠️ 無法更新第{prev_file}的導航，可能需要手動檢查")
PYEOF
    else
        echo "⚠️ 前一章節文件不存在：$PREV_FILE"
    fi
else
    echo "ℹ️ 這是第一章，無需更新前一章節導航"
fi

# 3. 更新網站最後更新日期
echo "📅 更新最後更新日期..."
DATE_STR="$(date "+%Y年%m月%d日")"
sed -i "s/最後更新：.*/最後更新：${DATE_STR}/g" index.html 2>/dev/null || true

echo "✅ 章節導航更新完成"