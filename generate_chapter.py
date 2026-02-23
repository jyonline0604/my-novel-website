#!/usr/bin/env python3
"""
自動生成《科技修真傳》新章節腳本
"""

import os
import re
import json
import subprocess
import sys
from datetime import datetime
from pathlib import Path

# 設定路徑
REPO_PATH = Path(__file__).parent
CHAPTER_TEMPLATE = """<!DOCTYPE html>
<html lang="zh-Hant">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
    <title>{chapter_title} - 科技修真傳</title>
    <meta name="description" content="《科技修真傳》{chapter_title}。">
    <meta name="keywords" content="{chapter_title}, 科技修真傳, 科技修仙, 賽博龐克, 數據修仙">
    <meta name="author" content="大肥瞄">
    
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Lato:wght@300;400;700&family=Noto+Serif+TC:wght@400;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css">

    <link rel="stylesheet" href="style.css">
</head>
<body class="light-mode">

    <header class="reader-header">
        <a href="index.html" class="header-nav-link"><i class="fas fa-arrow-left"></i> 返回目錄</a>
        <h2 class="reader-chapter-title">{chapter_title}</h2>
        <div class="header-controls">
            <button id="settings-btn" class="control-btn" aria-label="閱讀設定"><i class="fas fa-cog"></i></button>
        </div>
    </header>

    <div id="settings-panel" class="settings-panel">
        <div class="setting-group">
            <h4>字體大小</h4>
            <div id="font-size-options" class="setting-options">
                <button data-size="small">小</button>
                <button data-size="medium">中</button>
                <button data-size="large">大</button>
            </div>
        </div>
        <div class="setting-group">
            <h4>背景主題</h4>
            <div id="theme-options" class="setting-options">
                <button data-theme="light-mode">明亮</button>
                <button data-theme="sepia-mode">米黃</button>
                <button data-theme="dark-mode">夜間</button>
                <button data-theme="sky-blue-mode">天空藍</button>
                <button data-theme="light-green-mode">淺綠色</button>
            </div>
        </div>
    </div>

    <main class="reader-content-area">
        <article id="reader-article" class="reader-article font-size-medium">
            <h1>{chapter_title}</h1>
            {chapter_content}
        </article>
    </main>

    <script src="main.js"></script>
</body>
</html>"""

def get_latest_chapter_number():
    """獲取最新的章節編號"""
    chapter_files = list(REPO_PATH.glob("chapter-*.html"))
    if not chapter_files:
        return 0
    
    numbers = []
    for file in chapter_files:
        match = re.search(r'chapter-(\d+)\.html', file.name)
        if match:
            numbers.append(int(match.group(1)))
    
    return max(numbers) if numbers else 0

def read_chapter_content(chapter_num):
    """讀取指定章節的內容"""
    file_path = REPO_PATH / f"chapter-{chapter_num}.html"
    if not file_path.exists():
        return None
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 提取文章內容（在 <article> 標籤內）
    article_match = re.search(r'<article[^>]*>(.*?)</article>', content, re.DOTALL)
    if article_match:
        article_content = article_match.group(1)
        # 移除標題
        article_content = re.sub(r'<h1[^>]*>.*?</h1>', '', article_content, flags=re.DOTALL)
        return article_content.strip()
    
    return None

def extract_story_context(latest_chapter_num, num_chapters=3):
    """提取最近幾章的故事情境"""
    context = ""
    
    for i in range(max(1, latest_chapter_num - num_chapters + 1), latest_chapter_num + 1):
        content = read_chapter_content(i)
        if content:
            context += f"=== 第{i}章 ===\n{content}\n\n"
    
    return context

def get_deepseek_api_key():
    """從 auth-profiles.json 獲取 DeepSeek API Key"""
    try:
        auth_file = Path("/home/openclaw/.openclaw/agents/main/agent/auth-profiles.json")
        with open(auth_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        return data['profiles']['deepseek:default']['key']
    except Exception as e:
        print(f"警告: 無法讀取 DeepSeek API Key: {e}")
        return None

def generate_new_chapter_with_ai(context, new_chapter_num):
    """使用 DeepSeek API 生成新章節內容"""
    
    # 從 auth-profiles.json 獲取 API Key
    api_key = get_deepseek_api_key()
    if not api_key:
        print("警告: 使用測試內容（API Key 不可用）")
        return get_test_content(new_chapter_num)
    
    # 構建提示詞
    prompt = f"""你是一位專業的粵語小說作家，正在續寫《科技修真傳》這部賽博龐克修仙小說。

## 故事背景
這是一部結合科技與修真的賽博龐克小說。主角趙衍擁有科技裝備（靈能步槍、納米戰甲、智能手環等），在一個靈氣復甦的未來世界冒險。

## 當前情節（最近3章摘要）
{context}

## 角色設定
- 趙衍：主角，擁有科技裝備，正在學習修真
- 葉清涵：趙衍的同伴，修真者
- 雲遊子：崑崙派第十七代長老，正在幫助趙衍和葉清涵
- 白衣惡魔/深淵惡魔：反派，正在追殺主角們

## 寫作要求
1. **語言風格**：使用粵語口語寫作（例如：既=的、咗=了、喺=在、咩=什麼、冇=沒有、嘅=的、係=是）
2. **章節結構**：分為3-4個小節，每個小節用 <div class="section"> 包裹，標題用 <h3 class="section-title">
3. **內容要求**：情節要連貫，基於前文發展。可以包含對話、動作描寫、修煉場景等。
4. **長度**：約1500-2000字，足夠一個完整章節。
5. **章節標題**：請為新章節創作一個合適的標題，格式為「第{new_chapter_num}章：XXXX」

## 輸出格式
請直接輸出完整的章節內容，包含標題和分節，使用以下HTML格式：
<h1>第{new_chapter_num}章：你的章節標題</h1>
<div class="section">
    <h3 class="section-title">第一小節標題</h3>
    <p>段落內容...</p>
</div>
<div class="section">
    <h3 class="section-title">第二小節標題</h3>
    <p>段落內容...</p>
</div>

請開始生成第{new_chapter_num}章內容："""

    try:
        import requests
        
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        
        data = {
            "model": "deepseek-chat",
            "messages": [
                {"role": "system", "content": "你是一位專業的粵語小說作家，擅長創作賽博龐克修仙題材的小說。"},
                {"role": "user", "content": prompt}
            ],
            "temperature": 0.7,
            "max_tokens": 4000
        }
        
        print("正在調用 DeepSeek API 生成章節內容...")
        response = requests.post(
            "https://api.deepseek.com/chat/completions",
            headers=headers,
            json=data,
            timeout=60
        )
        
        if response.status_code == 200:
            result = response.json()
            ai_content = result['choices'][0]['message']['content']
            
            # 從 AI 回應中提取標題和內容
            lines = ai_content.strip().split('\n')
            title = None
            content_lines = []
            
            for line in lines:
                if line.startswith('<h1>') and '</h1>' in line:
                    # 提取標題，移除 HTML 標籤
                    title = line.replace('<h1>', '').replace('</h1>', '').strip()
                else:
                    content_lines.append(line)
            
            content = '\n'.join(content_lines).strip()
            
            if not title:
                # 如果 AI 沒有提供標題，使用默認標題
                title = f"第{new_chapter_num}章：AI 生成章節"
            
            print(f"AI 生成成功: {title}")
            return title, content
            
        else:
            print(f"DeepSeek API 錯誤: {response.status_code}")
            print(f"錯誤訊息: {response.text}")
            return get_test_content(new_chapter_num)
            
    except Exception as e:
        print(f"API 調用失敗: {e}")
        return get_test_content(new_chapter_num)

def get_test_content(new_chapter_num):
    """返回測試內容（備用）"""
    title = f"第{new_chapter_num}章：AI 生成章節測試"
    
    content = f"""
    <div class="section">
        <h3 class="section-title">AI 生成測試</h3>
        
        <p>這是由 AI 自動生成的章節內容。</p>
        
        <p>基於前文的情節發展，趙衍和葉清涵在崑崙長老雲遊子的幫助下恢復傷勢。</p>
        
        <p>他們開始學習崑崙派的秘傳功法，實力逐漸恢復。</p>
    </div>
    
    <div class="section">
        <h3 class="section-title">情節延續</h3>
        
        <p>在崑崙山谷中，趙衍發現這裡的修煉方式與外界完全不同。</p>
        
        <p>「呢度既修煉方法……竟然係結合咗古老既陣法同現代既量子理論？」趙衍驚訝地發現。</p>
        
        <p>葉清涵點頭：「崑崙派係修真界最古老既門派之一，佢哋既傳承唔同於一般既修煉方法。」</p>
    </div>
    
    <div class="section">
        <h3 class="section-title">新的危機</h3>
        
        <p>正當兩人專心修煉時，山谷外突然傳來警報聲。</p>
        
        <p>「唔好！深淵惡魔追到來啦！」雲遊子面色大變。</p>
        
        <p>趙衍和葉清涵對視一眼，知道新一輪的戰鬥即將開始……</p>
    </div>
    """
    
    return title, content

def create_new_chapter_file(chapter_num, title, content):
    """創建新章節 HTML 文件"""
    file_path = REPO_PATH / f"chapter-{chapter_num}.html"
    
    html_content = CHAPTER_TEMPLATE.format(
        chapter_title=title,
        chapter_content=content
    )
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"已創建章節文件: {file_path}")
    return file_path

def update_index_html(chapter_num, title):
    """更新首頁的章節列表"""
    index_path = REPO_PATH / "index.html"
    if not index_path.exists():
        print("錯誤: index.html 不存在")
        return False
    
    with open(index_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 創建新的章節列表項目
    today = datetime.now().strftime("%Y-%m-%d")
    new_item = f'''<li class="chapter-item">
                    <a href="chapter-{chapter_num}.html" class="chapter-link">
                        <span class="chapter-title">{title}</span>
                        <span class="chapter-date">{today}</span>
                    </a>
                </li>
                '''
    
    # 找到章節列表區域並插入新項目
    # 尋找 <ul class="chapter-list"> 後的第一個 <li>
    pattern = r'(<ul class="chapter-list">\s*)(<li class="chapter-item">)'
    replacement = r'\1' + new_item + r'<li class="chapter-item">'
    
    new_content = re.sub(pattern, replacement, content, count=1)
    
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"已更新首頁章節列表: {title}")
    return True

def git_commit_and_push(chapter_num):
    """提交並推送到 GitHub"""
    try:
        # 添加文件
        subprocess.run(
            ["git", "add", f"chapter-{chapter_num}.html", "index.html"],
            cwd=REPO_PATH,
            check=True,
            capture_output=True
        )
        
        # 提交
        commit_msg = f"新增第{chapter_num}章：自動生成章節"
        subprocess.run(
            ["git", "commit", "-m", commit_msg],
            cwd=REPO_PATH,
            check=True,
            capture_output=True
        )
        
        # 推送
        result = subprocess.run(
            ["git", "push", "origin", "main"],
            cwd=REPO_PATH,
            capture_output=True,
            text=True
        )
        
        if result.returncode == 0:
            print("成功推送到 GitHub")
            return True
        else:
            print(f"推送失敗: {result.stderr}")
            return False
            
    except subprocess.CalledProcessError as e:
        print(f"Git 操作失敗: {e}")
        return False

def main():
    """主函數"""
    print("開始自動生成新章節...")
    
    # 1. 獲取最新章節編號
    latest_num = get_latest_chapter_number()
    if latest_num == 0:
        print("錯誤: 找不到章節文件")
        return
    
    print(f"最新章節編號: {latest_num}")
    
    # 2. 計算新章節編號
    new_chapter_num = latest_num + 1
    print(f"新章節編號: {new_chapter_num}")
    
    # 3. 提取故事情境
    print("提取故事情境...")
    context = extract_story_context(latest_num)
    
    # 4. 生成新章節內容
    print("生成新章節內容...")
    title, content = generate_new_chapter_with_ai(context, new_chapter_num)
    
    # 5. 創建新章節文件
    print("創建新章節文件...")
    create_new_chapter_file(new_chapter_num, title, content)
    
    # 6. 更新首頁
    print("更新首頁...")
    update_index_html(new_chapter_num, title)
    
    # 7. 提交並推送
    print("提交並推送到 GitHub...")
    if git_commit_and_push(new_chapter_num):
        print("✅ 新章節生成並推送完成！")
    else:
        print("⚠️  章節已生成，但推送失敗")

if __name__ == "__main__":
    main()