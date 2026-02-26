#!/bin/bash
# 自動化生成小說新章節腳本
# 每天早上 10:00 自動執行

set -e

REPO_DIR="/home/openclaw/.openclaw/workspace/my-novel-website"
DEEPSEEK_API_KEY="sk-8741c7fb7d304634833c5eab93ee6b16"
MODEL="deepseek-chat"

cd "$REPO_DIR"

# 更新網站更新日期
DATE=$(date "+%Y年%m月%d日")
sed -i "s/最後更新：.*/最後更新：${DATE}/g" index.html

# 獲取最新章節編號
LAST_CHAPTER=$(ls -1 chapter-*.html 2>/dev/null | grep -oP 'chapter-\K[0-9]+' | sort -n | tail -1)
NEXT_CHAPTER=$((LAST_CHAPTER + 1))
PREV_CHAPTER=$((NEXT_CHAPTER - 1))
echo "最新章節: 第${LAST_CHAPTER}章 -> 將生成第${NEXT_CHAPTER}章"

# 調用 DeepSeek API（使用 jq 構建 JSON 以確保正確轉義）
PROMPT="延續《科技修真傳》上一章的劇情，撰寫第${NEXT_CHAPTER}章（至少3小節，每小節3-4段，繁體中文，主角是林塵，修真科幻風格）"
JSON_DATA=$(jq -n \
  --arg model "$MODEL" \
  --arg system "你是專業中文小說作家" \
  --arg prompt "$PROMPT" \
  '{
    model: $model,
    messages: [
      {role: "system", content: $system},
      {role: "user", content: $prompt}
    ],
    stream: false
  }')

echo "發送請求到 DeepSeek API..."
RESPONSE=$(curl -s https://api.deepseek.com/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer ${DEEPSEEK_API_KEY}" \
  -d "$JSON_DATA")

# 檢查回應是否有效
if echo "$RESPONSE" | grep -q '"error"'; then
    ERROR_MSG=$(echo "$RESPONSE" | jq -r '.error.message // "Unknown error"' 2>/dev/null || echo "$RESPONSE")
    echo "API 錯誤: $ERROR_MSG"
    exit 1
fi

# 使用 jq 提取內容（更可靠）
NEW_CONTENT=$(echo "$RESPONSE" | jq -r '.choices[0].message.content // empty' 2>/dev/null)
if [ -z "$NEW_CONTENT" ]; then
    echo "錯誤：無法從回應中提取內容"
    echo "回應：$RESPONSE"
    exit 1
fi

if [ -z "$NEW_CONTENT" ]; then
    echo "Error: Failed to generate content"
    exit 1
fi

# 獲取標題
CHAPTER_TITLE=$(echo "$NEW_CONTENT" | head -3 | grep -oP '第[0-9]+章：\K[^　\n]+' | head -1)
[ -z "$CHAPTER_TITLE" ] && CHAPTER_TITLE="修煉之路"

echo "章節標題: ${CHAPTER_TITLE}"

# 使用 Python 生成 HTML
python3 << PYEOF
content = """$NEW_CONTENT""".strip()
title = "$CHAPTER_TITLE"
num = int("$NEXT_CHAPTER")
prev = num - 1

# 轉換內容為 HTML
html_lines = []
in_section = False
for line in content.split('\n'):
    line = line.strip()
    if not line:
        continue
    if '章：' in line and ('第' in line[:5]):
        if in_section:
            html_lines.append('</div>')
        html_lines.append(f'<div class="section">')
        html_lines.append(f'<h3 class="section-title">{line}</h3>')
        in_section = True
    else:
        html_lines.append(f'<p>{line}</p>')

if in_section:
    html_lines.append('</div>')

html_content = '\n'.join(html_lines)

html_template = f'''<!DOCTYPE html>
<html lang="zh-Hant">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>第{num}章：{title} - 科技修真傳</title>
    <meta name="description" content="《科技修真傳》第{num}章：{title}">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Lato:wght@300;400;700&family=Noto+Serif+TC:wght@400;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css">
    <link rel="stylesheet" href="style.css">
</head>
<body class="light-mode">
    <header class="reader-header">
        <a href="index.html" class="header-nav-link"><i class="fas fa-arrow-left"></i> 返回目錄</a>
        <h2 class="reader-chapter-title">第{num}章：{title}</h2>
    </header>
    <main class="reader-content-area">
        <article class="reader-article">
            <div class="content">
                <h1>第{num}章：{title}</h1>
                <div class="chapter">
{html_content}
                </div>
            </div>
        </article>
    </main>
    <footer class="reader-footer-nav">
        <a href="chapter-{prev}.html" class="nav-button">« 上一章</a>
        <a href="index.html" class="nav-button">返回目錄</a>
    </footer>
    <script src="main.js"></script>
</body>
</html>'''

with open(f'chapter-{num}.html', 'w', encoding='utf-8') as f:
    f.write(html_template)

print(f"第{num}章已生成")
PYEOF

# 提交並推送
git add "chapter-${NEXT_CHAPTER}.html"
git commit -m "新增第${NEXT_CHAPTER}章：${CHAPTER_TITLE}"
git push

echo "✅ 已推送到 GitHub"
