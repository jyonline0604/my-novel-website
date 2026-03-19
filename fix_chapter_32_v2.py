#!/usr/bin/env python3
# 專門修復第32章的格式問題 - 改進版本

import re
import os
import sys
from pathlib import Path

def extract_chapter_info(html_content):
    """從HTML中提取章節信息"""
    
    # 從<title>標籤提取章節標題
    title_match = re.search(r'<title>第(\d+)章：([^<]+?)(?:\s*-\s*科技修真傳)?</title>', html_content)
    if title_match:
        chapter_num = title_match.group(1)
        chapter_title = title_match.group(2).strip()
    else:
        # 嘗試從h1標籤提取
        h1_match = re.search(r'<h1>第(\d+)章：([^<]+)</h1>', html_content)
        if h1_match:
            chapter_num = h1_match.group(1)
            chapter_title = h1_match.group(2).strip()
        else:
            raise ValueError("無法提取章節標題")
    
    # 提取章節主要內容
    # 先嘗試提取<div class="chapter">內容
    chapter_match = re.search(r'<div class="chapter">(.*?)</div>', html_content, re.DOTALL)
    if chapter_match:
        content = chapter_match.group(1).strip()
    else:
        # 嘗試提取<article>內容
        article_match = re.search(r'<article[^>]*>(.*?)</article>', html_content, re.DOTALL)
        if article_match:
            content = article_match.group(1).strip()
        else:
            # 作為最後手段，提取<body>中的主要內容
            body_match = re.search(r'<main[^>]*>(.*?)</main>', html_content, re.DOTALL)
            if body_match:
                content = body_match.group(1).strip()
            else:
                raise ValueError("無法提取章節內容")
    
    return {
        'chapter_num': chapter_num,
        'chapter_title': chapter_title,
        'content': content
    }

def parse_sections_from_content(content):
    """從內容中解析各個小節"""
    
    # 清理內容
    content = content.strip()
    
    # 移除重複的章節標題
    content = re.sub(r'<h3 class="section-title">#\s*第[^<]+</h3>', '', content)  # 移除錯誤的h3標題
    content = re.sub(r'<h2[^>]*>第\d+章[^<]*</h2>', '', content)  # 移除重複的h2標題
    
    # 將內容按段落分割
    lines = content.split('\n')
    
    sections = []
    current_section = {'title': '', 'paragraphs': []}
    in_section = False
    
    section_num_chinese = ['一', '二', '三', '四', '五', '六', '七', '八', '九', '十']
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        # 檢測是否為小節標題
        section_match = re.match(r'<p>##\s*(第[一二三四五六七八九十\d]+節|[^<]+)</p>', line)
        if section_match:
            # 保存上一個小節
            if in_section and current_section['paragraphs']:
                sections.append(current_section.copy())
            
            # 開始新小節
            title = section_match.group(1).strip()
            # 移除"第X節："前綴
            title = re.sub(r'^第[一二三四五六七八九十\d]+節：\s*', '', title)
            current_section = {'title': title, 'paragraphs': []}
            in_section = True
            
        # 檢測是否為markdown格式的標題（沒有<p>包圍）
        elif line.startswith('## '):
            # 保存上一個小節
            if in_section and current_section['paragraphs']:
                sections.append(current_section.copy())
            
            # 開始新小節
            title = line[3:].strip()
            title = re.sub(r'^第[一二三四五六七八九十\d]+節：\s*', '', title)
            current_section = {'title': title, 'paragraphs': []}
            in_section = True
            
        # 檢測是否為markdown分隔符
        elif line.startswith('---'):
            # 保存上一個小節
            if in_section and current_section['paragraphs']:
                sections.append(current_section.copy())
            
            # 創建一個新小節（用於分隔符後的內容）
            current_section = {'title': '', 'paragraphs': []}
            in_section = True
            
        # 檢測是否為段落
        elif line.startswith('<p>'):
            # 清理段落內容
            paragraph = line[3:-4] if line.endswith('</p>') else line[3:]
            
            # 移除段落中的markdown標題標記
            paragraph = re.sub(r'^#+\s*', '', paragraph)
            
            if paragraph.strip():
                current_section['paragraphs'].append(paragraph.strip())
            in_section = True
            
        # 處理沒有標記的文本
        elif not line.startswith('<') and line:
            if in_section:
                current_section['paragraphs'].append(line.strip())
    
    # 添加最後一個小節
    if in_section and current_section['paragraphs']:
        sections.append(current_section)
    
    # 如果沒有找到小節，將整個內容作為一個小節
    if not sections:
        # 將內容分割成段落
        paragraphs = []
        for line in content.split('\n'):
            line = line.strip()
            if line.startswith('<p>'):
                para = line[3:-4] if line.endswith('</p>') else line[3:]
                paragraphs.append(para.strip())
            elif line and not line.startswith('<'):
                paragraphs.append(line.strip())
        
        if paragraphs:
            sections.append({
                'title': '章節內容',
                'paragraphs': paragraphs
            })
    
    return sections

def generate_correct_html(chapter_num, chapter_title, sections):
    """生成正確的HTML格式"""
    
    # 生成section HTML
    sections_html = []
    section_num_chinese = ['一', '二', '三', '四', '五', '六', '七', '八', '九', '十']
    
    for i, section in enumerate(sections):
        if i < len(section_num_chinese):
            section_num = section_num_chinese[i]
        else:
            section_num = str(i + 1)
        
        # 生成段落HTML
        paragraphs_html = '\n'.join([f'        <p>{para}</p>' for para in section['paragraphs'] if para.strip()])
        
        section_html = f'''    <div class="section">
        <h3 class="section-title">{section_num}、{section['title']}</h3>
{paragraphs_html}
    </div>'''
        sections_html.append(section_html)
    
    sections_str = '\n'.join(sections_html)
    
    # 計算上一章和下一章
    prev_chapter = int(chapter_num) - 1
    next_chapter = int(chapter_num) + 1
    
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
        <a href="chapter-{prev_chapter}.html" id="prev-chapter-btn" class="nav-button">« 上一章</a>
        <a href="chapter-{next_chapter}.html" id="next-chapter-btn" class="nav-button">下一章 »</a>
    </footer>

    <section class="comment-section">
        <h3 class="comment-section-title">讀者留言</h3>
    </section>

    <script src="main.js"></script>

</body>
</html>'''
    
    return html_template

def fix_chapter_32():
    """修復第32章格式"""
    
    chapter_path = 'chapter-32.html'
    print(f"正在處理: {chapter_path}")
    
    # 讀取HTML文件
    with open(chapter_path, 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    try:
        # 提取章節信息
        chapter_info = extract_chapter_info(html_content)
        chapter_num = chapter_info['chapter_num']
        chapter_title = chapter_info['chapter_title']
        content = chapter_info['content']
        
        print(f"  章節: 第{chapter_num}章 - {chapter_title}")
        print(f"  內容長度: {len(content)} 字符")
        
        # 解析小節
        sections = parse_sections_from_content(content)
        print(f"  找到 {len(sections)} 個小節")
        for i, section in enumerate(sections):
            print(f"    小節 {i+1}: {section['title']} ({len(section['paragraphs'])} 段落)")
        
        # 生成正確的HTML
        corrected_html = generate_correct_html(chapter_num, chapter_title, sections)
        
        # 保存修正後的文件
        with open(chapter_path, 'w', encoding='utf-8') as f:
            f.write(corrected_html)
        
        print(f"  ✅ 修正完成")
        return True
        
    except Exception as e:
        print(f"  ❌ 處理失敗: {str(e)}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == '__main__':
    fix_chapter_32()