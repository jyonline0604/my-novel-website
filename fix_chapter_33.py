#!/usr/bin/env python3
# 專門修復第33章的格式問題

import re

def fix_chapter_33():
    # 讀取原始文件
    with open('chapter-33.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    print("正在解析第33章...")
    
    # 提取章節標題
    # 從<title>中提取
    title_match = re.search(r'<title>第33章：([^<]+)</title>', content)
    if title_match:
        chapter_title = title_match.group(1).strip()
    else:
        chapter_title = "修煉之路"
    
    print(f"章節標題: {chapter_title}")
    
    # 提取主要內容
    # 查找<div class="chapter">中的內容
    chapter_match = re.search(r'<div class="chapter">(.*?)</div>', content, re.DOTALL)
    if chapter_match:
        chapter_content = chapter_match.group(1).strip()
    else:
        print("錯誤: 找不到章節內容")
        return False
    
    print(f"原始內容長度: {len(chapter_content)} 字符")
    
    # 解析小節
    sections = []
    lines = chapter_content.split('\n')
    
    current_section = {'title': '', 'paragraphs': []}
    in_section = False
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
        
        # 檢查是否為小節標題
        section_match = re.match(r'<p>##\s*(第[一二三四五六七八九十\d]+節|[^<]+)</p>', line)
        if section_match:
            # 如果已經在處理一個小節，先保存它
            if in_section and current_section['paragraphs']:
                sections.append(current_section.copy())
            
            # 開始新小節
            title = section_match.group(1).strip()
            # 移除"第X節："前綴，但保留冒號後面的內容
            title = re.sub(r'^第[一二三四五六七八九十\d]+節：\s*', '', title)
            current_section = {'title': title, 'paragraphs': []}
            in_section = True
            continue
        
        # 檢查是否為段落
        if line.startswith('<p>'):
            # 移除<p>和</p>標籤
            paragraph = line[3:-4] if line.endswith('</p>') else line[3:]
            
            # 如果是章節標題行（#開頭），跳過它
            if paragraph.startswith('#《科技修真傳》'):
                continue
            
            # 移除段落中的markdown標記
            paragraph = re.sub(r'^#+\s*', '', paragraph)
            
            if paragraph.strip():
                current_section['paragraphs'].append(paragraph.strip())
            in_section = True
    
    # 添加最後一個小節
    if in_section and current_section['paragraphs']:
        sections.append(current_section)
    
    print(f"找到 {len(sections)} 個小節")
    for i, section in enumerate(sections):
        print(f"  小節 {i+1}: {section['title']} ({len(section['paragraphs'])} 段落)")
    
    # 如果沒有找到小節，將整個內容作為一個小節
    if not sections:
        # 將內容分割成段落
        paragraphs = []
        for line in chapter_content.split('\n'):
            line = line.strip()
            if line.startswith('<p>') and not line.startswith('<p>#'):
                para = line[3:-4] if line.endswith('</p>') else line[3:]
                paragraphs.append(para.strip())
        
        if paragraphs:
            sections.append({
                'title': '章節內容',
                'paragraphs': paragraphs
            })
    
    # 生成修正後的HTML
    # 生成小節HTML
    sections_html = []
    section_num_chinese = ['一', '二', '三', '四', '五']
    
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
    
    # 生成完整的HTML（基於第28章模板）
    corrected_html = f'''<!DOCTYPE html>
<html lang="zh-Hant">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
    <title>第33章：{chapter_title} - 科技修真傳</title>
    <meta name="description" content="《科技修真傳》第33章：{chapter_title}。">
    <meta name="keywords" content="第33章, {chapter_title}, 科技修真傳, 科技修仙, 賽博龐克, 數據修仙">
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
        <h2 class="reader-chapter-title">第33章：{chapter_title}</h2>
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
        <h1>第33章：{chapter_title}</h1>
<div class="chapter">
    <h2 class="chapter-title">第33章：{chapter_title}</h2>

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
        <a href="chapter-32.html" id="prev-chapter-btn" class="nav-button">« 上一章</a>
        <a href="chapter-34.html" id="next-chapter-btn" class="nav-button">下一章 »</a>
    </footer>

    <section class="comment-section">
        <h3 class="comment-section-title">讀者留言</h3>
    </section>

    <script src="main.js"></script>

</body>
</html>'''
    
    # 寫回文件
    with open('chapter-33.html', 'w', encoding='utf-8') as f:
        f.write(corrected_html)
    
    print("✅ 第33章修復完成")
    return True

if __name__ == '__main__':
    fix_chapter_33()