#!/bin/bash
# Be A Pro Football 攻略更新腳本
# 每天 18:00 自動執行
# 排版：直接使用 <h2> 和 <h3>

set -e

REPO_DIR="/home/openclaw/.openclaw/workspace/my-novel-website"
DEEPSEEK_API_KEY="sk-8741c7fb7d304634833c5eab93ee6b16"
MODEL="deepseek-chat"

cd "$REPO_DIR"

PROMPT="繼續撰寫《Be A Pro Football》足球遊戲攻略的一部分（1個小節標題+3-4段內容，繁體中文，專業足球遊戲攻略風格）"

RESPONSE=$(curl -s https://api.deepseek.com/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer ${DEEPSEEK_API_KEY}" \
  -d "{
    \"model\": \"${MODEL}\",
    \"messages\": [
      {\"role\": \"system\", \"content\": \"你是專業足球遊戲攻略作家\"},
      {"role": "user", "content": "${PROMPT}"}
    ],
    "stream": false
  }")

NEW_CONTENT=$(echo "$RESPONSE" | grep -oP '"content":\s*"\K[^"]+' | head -1 | sed 's/\\n/\n/g')

if [ -z "$NEW_CONTENT" ]; then
    echo "Error generating content"
    exit 1
fi

# Be A Pro 格式
HTML_CONTENT=$(echo "$NEW_CONTENT" | awk '
BEGIN { 
    print "<h2>⚽ 攻略更新</h2>"
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
')

python3 << EOF
with open('beapro-football-guide.html', 'r', encoding='utf-8') as f:
    content = f.read()

insert_pos = content.find('</main>')
if insert_pos != -1:
    new_content = '''$HTML_CONTENT'''
    content = content[:insert_pos] + new_content + content[insert_pos:]
    
    with open('beapro-football-guide.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Content inserted")
else:
    print("</main> not found")
EOF

git add beapro-football-guide.html
git commit -m "Be A Pro Football：更新遊戲攻略"
git push

echo "✅ Be A Pro Football 已更新"
