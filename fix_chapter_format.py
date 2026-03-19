#!/usr/bin/env python3
# 修正小說章節格式腳本
# 將第29章及之後的錯誤格式修正為與第28章一致的格式

import re
import os
import sys
from pathlib import Path

def extract_content_from_html(html_content):
    """從HTML中提取章節標題和內容"""
    
    # 提取章節標題
    title_match = re.search(r'<title>第(\d+)章：([^<]+)', html_content)
    if title_match:
        chapter_num = title_match.group(1)
        chapter_title = title_match.group(2).strip()
    else:
        # 嘗試從h1標籤中提取
        h1_match = re.search(r'<h1>第(\d+)章：([^<]+)', html_content)
        if h1_match:
            chapter_num = h1_match.group(1)
            chapter_title = h1_match.group(2).strip()
        else:
            raise ValueError("無法提取章節標題")
    
    # 提取章節內容（在<div class="chapter">中）
    chapter_match = re.search(r'<div class="chapter">(.*?)</div>', html_content, re.DOTALL)
    if not chapter_match:
        # 嘗試其他可能的容器
        chapter_match = re.search(r'<div class="chapter"\s*>(.*?)</div>', html_content, re.DOTALL)
    
    if chapter_match:
        raw_content = chapter_match.group(1).strip()
    else:
        # 如果找不到chapter div，嘗試直接提取article內容
        article_match = re.search(r'<article[^>]*>(.*?)</article>', html_content, re.DOTALL)
        if article_match:
            raw_content = article_match.group(1).strip()
        else:
            raise ValueError("無法提取章節內容")
    
    return {
        'chapter_num': chapter_num,
        'chapter_title': chapter_title,
        'raw_content': raw_content
    }

def convert_markdown_to_html_sections(raw_content):
    """將markdown格式的內容轉換為HTML section結構"""
    
    # 清理內容
    content = raw_content.strip()
    
    # 替換各種markdown標題格式
    content = re.sub(r'<h3 class="section-title">#\s*第[^<]+</h3>', '', content)  # 移除錯誤的h3標題
    
    # 將 ## 標題轉換為 section
    lines = content.split('\n')
    sections = []
    current_section = []
    current_title = None
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        # 檢測 ## 標題
        if line.startswith('## '):
            # 保存上一個section
            if current_title is not None and current_section:
                sections.append({
                    'title': current_title,
                    'content': '\n'.join(current_section)
                })
            
            # 開始新section
            current_title = line[3:].strip()  # 移除 "## "
            current_section = []
        elif line.startswith('### '):
            # 三級標題，暫時作為段落處理
            if current_section:
                current_section.append(f'<p><strong>{line[4:]}</strong></p>')
            else:
                current_section.append(f'<p><strong>{line[4:]}</strong></p>')
        elif line.startswith('<p>#'):
            # 處理 <p># 開頭的行
            clean_line = re.sub(r'^<p>#+\s*', '<p><strong>', line)
            clean_line = re.sub(r'</p>$', '</strong></p>', clean_line)
            current_section.append(clean_line)
        elif line.startswith('<p>'):
            # 普通段落
            current_section.append(line)
        else:
            # 沒有標記的文本，包裝為段落
            if line and not line.startswith('<'):
                current_section.append(f'<p>{line}</p>')
            else:
                current_section.append(line)
    
    # 添加最後一個section
    if current_title is not None and current_section:
        sections.append({
            'title': current_title,
            'content': '\n'.join(current_section)
        })
    
    # 如果沒有找到section，將整個內容作為一個section
    if not sections:
        sections.append({
            'title': '章節內容',
            'content': content
        })
    
    return sections

def generate_correct_html(chapter_num, chapter_title, sections):
    """生成正確的HTML格式"""
    
    # 生成section HTML
    sections_html = []
    for i, section in enumerate(sections):
        section_num = ['一', '二', '三', '四', '五', '六', '七', '八', '九', '十'][i] if i < 10 else str(i+1)
        sections_html.append(f'''
    <div class="section">
        <h3 class="section-title">{section_num}、{section['title']}</h3>
        {section['content']}
    </div>''')
    
    sections_str = '\n'.join(sections_html)
    
    # 正確的HTML模板（基於第28章）
    html_template = f'''<!DOCTYPE html>
<html lang="zh-Hant">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
    <title>第{chapter_num}章：{chapter_title} - 科技修真傳</title>
    <meta name="description" content="《科技修真傳》第{chapter_num}章：{chapter_title}。">
    <meta name="keywords" content="第{chapter_num}章, {chapter_title}, 科技修真傳, 科技修仙, 賽博龐克, 數據修仙">
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
        <h2 class="reader-chapter-title">第{chapter_num}章：{chapter_title}</h2>
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

    <div class="content">
        <h1>第{chapter_num}章：{chapter_title}</h1>
<div class="chapter">
    <h2 class="chapter-title">第{chapter_num}章：{chapter_title}</h2>

{sections_str}
</div>
    </div>

        </article>
    </main>

    <section class="share-section">
        <h4 class="share-title">分享這個章節</h4>
        <div class="share-buttons">
            <a href="#" id="share-facebook" class="share-btn facebook" title="分享到 Facebook"><i class="fab fa-facebook-f"></i></a>
            <a href="#" id="share-twitter" class="share-btn twitter" title="分享到 X (Twitter)"><i class="fab fa-twitter"></i></a>
            <a href="#" id="share-line" class="share-btn line" title="分享到 LINE"><i class="fab fa-line"></i></a>
            <button id="copy-link-btn" class="share-btn copy-link" title="複製連結"><i class="fas fa-link"></i></button>
        </div>
    </section>

    <footer class="reader-footer-nav">
        <a href="chapter-{int(chapter_num)-1}.html" id="prev-chapter-btn" class="nav-button">« 上一章</a>
        <a href="chapter-{int(chapter_num)+1}.html" id="next-chapter-btn" class="nav-button">下一章 »</a>
    </footer>

    <section class="comment-section">
        <h3 class="comment-section-title">讀者留言</h3>
    </section>

    <script src="main.js"></script>

</body>
</html>'''
    
    return html_template

def fix_chapter_file(chapter_path):
    """修正單個章節文件"""
    
    print(f"正在處理: {chapter_path}")
    
    # 讀取HTML文件
    with open(chapter_path, 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    try:
        # 提取內容
        extracted = extract_content_from_html(html_content)
        chapter_num = extracted['chapter_num']
        chapter_title = extracted['chapter_title']
        raw_content = extracted['raw_content']
        
        print(f"  章節: 第{chapter_num}章 - {chapter_title}")
        
        # 轉換內容格式
        sections = convert_markdown_to_html_sections(raw_content)
        print(f"  找到 {len(sections)} 個小節")
        
        # 生成正確的HTML
        corrected_html = generate_correct_html(chapter_num, chapter_title, sections)
        
        # 保存修正後的文件
        with open(chapter_path, 'w', encoding='utf-8') as f:
            f.write(corrected_html)
        
        print(f"  ✅ 修正完成")
        return True
        
    except Exception as e:
        print(f"  ❌ 處理失敗: {e}")
        return False

def main():
    """主函數"""
    
    # 要修正的章節文件
    chapters_to_fix = ['chapter-29.html', 'chapter-30.html', 'chapter-31.html']
    
    print("開始修正小說章節格式...")
    print("=" * 50)
    
    success_count = 0
    for chapter_file in chapters_to_fix:
        chapter_path = Path(chapter_file)
        if chapter_path.exists():
            if fix_chapter_file(chapter_path):
                success_count += 1
        else:
            print(f"❌ 文件不存在: {chapter_file}")
    
    print("=" * 50)
    print(f"修正完成: {success_count}/{len(chapters_to_fix)} 個文件成功修正")
    
    if success_count == len(chapters_to_fix):
        print("✅ 所有章節格式修正完成！")
    else:
        print("⚠️  部分章節修正失敗，請檢查錯誤信息")

if __name__ == '__main__':
    main()