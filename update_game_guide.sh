#!/bin/bash
# 問劍長生 遊戲攻略更新腳本
# 每天 08:00 自動執行
# 排版：<div class="section"><h3> 在 main 區塊內

set -e

REPO_DIR="/home/openclaw/.openclaw/workspace/my-novel-website"
DEEPSEEK_API_KEY="sk-8741c7fb7d304634833c5eab93ee6b16"
MODEL="deepseek-chat"

cd "$REPO_DIR"

# 更新日期
DATE=$(date "+%Y年%m月%d日")
sed -i "s/最後更新：.*/最後更新：${DATE}/g" game-guide.html

PROMPT="繼續撰寫《問劍長生》遊戲攻略的一部分（1個小節標題+3-4段內容，繁體中文，專業遊戲攻略風格）"

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

# 問劍長生格式
HTML_CONTENT=$(echo "$NEW_CONTENT" | awk '
BEGIN { 
    print "<div class=\"section\">"
}
{
    gsub(/^[[:space:]]+|[[:space:]]+$/, "")
    if (match($0, /^## /)) {
        gsub(/^## /, "", $0)
        print "<h3>🔥 " $0 "</h3>"
    } else if (length($0) > 0) {
        print "<p>" $0 "</p>"
    }
}
END { print "</div>" }
')

python3 << EOF
with open('game-guide.html', 'r', encoding='utf-8') as f:
    content = f.read()

insert_pos = content.find('</main>')
if insert_pos != -1:
    new_content = '''$HTML_CONTENT'''
    content = content[:insert_pos] + new_content + content[insert_pos:]
    
    with open('game-guide.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Content inserted")
else:
    print("</main> not found")
EOF

git add game-guide.html
git commit -m "問劍長生：更新遊戲攻略"
git push

echo "✅ 問劍長生 已更新"
