#!/bin/bash
# AI 資訊 更新腳本
# 每天 20:00 自動執行
# 排版：<article class="news-item"><h3>

set -e

REPO_DIR="/home/openclaw/.openclaw/workspace/my-novel-website"
DEEPSEEK_API_KEY="sk-8741c7fb7d304634833c5eab93ee6b16"
MODEL="deepseek-chat"

cd "$REPO_DIR"

PROMPT="撰寫一篇最新的 AI 資訊/新聞（1個新聞標題+3-4段內容，繁體中文，專業科技新聞風格，關於最新 AI 技術發展）"

RESPONSE=$(curl -s https://api.deepseek.com/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer ${DEEPSEEK_API_KEY}" \
  -d "{
    \"model\": \"${MODEL}\",
    \"messages\": [
      {\"role\": \"system\", \"content\": \"你是專業科技新聞作家\"},
      {\"role\": \"user\", \"content\": \"${PROMPT}\"}
    ],
    \"stream\": false
  }")

NEW_CONTENT=$(echo "$RESPONSE" | grep -oP '"content":\s*"\K[^"]+' | head -1 | sed 's/\\n/\n/g')

if [ -z "$NEW_CONTENT" ]; then
    echo "Error generating content"
    exit 1
fi

# AI 資訊格式
DATE=$(date "+%Y年%m月%d日")
HTML_CONTENT=$(echo "$NEW_CONTENT" | awk -v date="$DATE" '
BEGIN { 
    print "<article class=\"news-item\">"
}
{
    gsub(/^[[:space:]]+|[[:space:]]+$/, "")
    if (match($0, /^## /)) {
        gsub(/^## /, "", $0)
        print "<h3>⚡ " $0 "</h3>"
    } else if (match($0, /^# /)) {
        gsub(/^# /, "", $0)
        print "<h3>" $0 "</h3>"
    } else if (length($0) > 0) {
        print "<p>" $0 "</p>"
    }
}
END { 
    print "<p class=\"news-date\">更新日期：" date "</p>"
    print "</article>"
}
')

python3 << EOF
with open('ai-news.html', 'r', encoding='utf-8') as f:
    content = f.read()

insert_pos = content.find('</main>')
if insert_pos != -1:
    new_content = '''$HTML_CONTENT'''
    content = content[:insert_pos] + new_content + content[insert_pos:]
    
    with open('ai-news.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Content inserted")
else:
    print("</main> not found")
EOF

git add ai-news.html
git commit -m "AI 資訊：更新最新 AI 新聞"
git push

echo "✅ AI 資訊 已更新"
