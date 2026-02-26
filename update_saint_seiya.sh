#!/bin/bash
# 聖鬥士星矢重生2 攻略更新腳本
# 每天 12:00 自動執行
# 排版：<div class="guide-section"><h2 class="section-title"> 和 <div class="content-card">

set -e

REPO_DIR="/home/openclaw/.openclaw/workspace/my-novel-website"
DEEPSEEK_API_KEY="sk-8741c7fb7d304634833c5eab93ee6b16"
MODEL="deepseek-chat"

cd "$REPO_DIR"

PROMPT="繼續撰寫《聖鬥士星矢：重生2》遊戲攻略的一部分（1個小節標題+3-4段內容，繁體中文，專業遊戲攻略風格）"

RESPONSE=$(curl -s https://api.deepseek.com/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer ${DEEPSEEK_API_KEY}" \
  -d "{
    \"model\": \"${MODEL}\",
    \"messages\": [
      {\"role\": \"system\", \"content\": \"你是專業手遊攻略作家\"},
      {\"role\": \"user\", \"content\": \"${PROMPT}\"}
    ],
    \"stream\": false
  }")

NEW_CONTENT=$(echo "$RESPONSE" | grep -oP '"content":\s*"\K[^"]+' | head -1 | sed 's/\\n/\n/g')

if [ -z "$NEW_CONTENT" ]; then
    echo "Error generating content"
    exit 1
fi

# 聖鬥士星矢格式：guide-section > content-card
HTML_CONTENT=$(echo "$NEW_CONTENT" | awk '
BEGIN { 
    print "<div class=\"guide-section\">"
    print "<h2 class=\"section-title\"><i class=\"fas fa-star\"></i> 攻略更新</h2>"
    print "<div class=\"content-card\">"
}
{
    gsub(/^[[:space:]]+|[[:space:]]+$/, "")
    if (match($0, /^## /)) {
        gsub(/^## /, "", $0)
        print "<h3>" $0 "</h3>"
    } else if (length($0) > 0) {
        print "<p>" $0 "</p>"
    }
}
END { 
    print "</div>"
    print "</div>" 
}
')

# 使用 Python 來插入內容
python3 << EOF
import re

with open('saint-seiya-guide.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 在 </main> 之前插入新內容
insert_pos = content.find('</main>')
if insert_pos != -1:
    new_content = '''$HTML_CONTENT'''
    content = content[:insert_pos] + new_content + content[insert_pos:]
    
    with open('saint-seiya-guide.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Content inserted successfully")
else:
    print("</main> not found")
EOF

git add saint-seiya-guide.html
git commit -m "聖鬥士星矢：更新遊戲攻略"
git push

echo "✅ 聖鬥士星矢重生2 已更新"
