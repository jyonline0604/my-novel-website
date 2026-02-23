#!/usr/bin/env python3
"""
備用章節生成腳本（當主腳本失敗時使用）
"""

import os
import re
import subprocess
from datetime import datetime
from pathlib import Path

REPO_PATH = Path(__file__).parent

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

def create_backup_chapter(new_chapter_num):
    """創建備用章節"""
    title = f"第{new_chapter_num}章：備用章節"
    
    content = f"""
    <div class="section">
        <h3 class="section-title">備用章節</h3>
        
        <p>這是由備用系統生成的章節內容。</p>
        
        <p>由於主要AI生成系統暫時不可用，本章節使用預設內容。</p>
        
        <p>趙衍和葉清涵在崑崙山谷中繼續修煉，恢復傷勢。</p>
    </div>
    
    <div class="section">
        <h3 class="section-title">修煉進展</h3>
        
        <p>「雲遊子前輩既指導真係高明。」趙衍感受住體內既靈力流動。</p>
        
        <p>「崑崙派既功法果然與眾不同。」葉清涵點頭贊同。</p>
        
        <p>兩人既實力正喺穩步恢復中。</p>
    </div>
    
    <div class="section">
        <h3 class="section-title">準備離開</h3>
        
        <p>幾日之後，雲遊子召集兩人。</p>
        
        <p>「你哋既傷勢已經恢復得七七八八，係時候離開呢度啦。」</p>
        
        <p>「但係深淵惡魔……」趙衍面露憂色。</p>
        
        <p>「老朽會教你哋一個隱匿氣息既陣法，應該可以暫時避開佢既追蹤。」</p>
    </div>
    """
    
    # 創建章節文件
    template = """<!DOCTYPE html>
<html lang="zh-Hant">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
    <title>{title} - 科技修真傳</title>
    <meta name="description" content="《科技修真傳》{title}。">
    <meta name="keywords" content="{title}, 科技修真傳, 科技修仙, 賽博龐克, 數據修仙">
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
        <h2 class="reader-chapter-title">{title}</h2>
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
            <h1>{title}</h1>
            {content}
        </article>
    </main>

    <script src="main.js"></script>
</body>
</html>"""
    
    file_path = REPO_PATH / f"chapter-{new_chapter_num}.html"
    html_content = template.format(title=title, content=content)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"已創裝備用章節文件: {file_path}")
    return file_path, title

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
    pattern = r'(<ul class="chapter-list">\s*)(<li class="chapter-item">)'
    replacement = r'\1' + new_item + r'<li class="chapter-item">'
    
    new_content = re.sub(pattern, replacement, content, count=1)
    
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"已更新首頁章節列表: {title}")
    return True

def main():
    """主函數"""
    print("備用章節生成系統啟動...")
    
    # 1. 獲取最新章節編號
    latest_num = get_latest_chapter_number()
    if latest_num == 0:
        print("錯誤: 找不到章節文件")
        return
    
    print(f"最新章節編號: {latest_num}")
    
    # 2. 計算新章節編號
    new_chapter_num = latest_num + 1
    print(f"新章節編號: {new_chapter_num}")
    
    # 3. 創建備用章節
    print("創建備用章節...")
    file_path, title = create_backup_chapter(new_chapter_num)
    
    # 4. 更新首頁
    print("更新首頁...")
    update_index_html(new_chapter_num, title)
    
    print("✅ 備用章節生成完成！")

if __name__ == "__main__":
    main()