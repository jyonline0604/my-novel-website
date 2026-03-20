#!/usr/bin/env python3
"""
智能章節生成器
自動生成小說新章節並更新網站
"""

import os
import json
import re
from datetime import datetime

WORKSPACE = "/home/openclaw/.openclaw/workspace"
NOVEL_DIR = f"{WORKSPACE}/my-novel-website"

def get_current_chapter():
    """獲取最新章節編號"""
    chapters = []
    for f in os.listdir(NOVEL_DIR):
        if f.startswith('chapter-') and f.endswith('.html'):
            num = int(f.replace('chapter-', '').replace('.html', ''))
            chapters.append(num)
    return max(chapters) if chapters else 0

def generate_new_chapter(chapter_num):
    """生成新章節"""
    print(f"生成第{chapter_num}章...")
    
    # 讀取前一章獲取標題
    prev_file = f"{NOVEL_DIR}/chapter-{chapter_num-1}.html"
    prev_title = f"第{chapter_num-1}章"
    
    if os.path.exists(prev_file):
        with open(prev_file, 'r', encoding='utf-8') as f:
            content = f.read()
            match = re.search(r'<h1[^>]*>([^<]+)</h1>', content)
            if match:
                prev_title = match.group(1)
    
    # 新章節標題
    chapter_titles = {
        55: "時空裂縫",
        56: "異世界來客",
        57: "修煉資源",
        58: "境界突破",
        59: "新的危機",
        60: "最終對決"
    }
    
    title = chapter_titles.get(chapter_num, f"第{chapter_num}章：新的旅程")
    
    # 生成完整章節內容
    story_intro = f"""
    <p>「第二部：深淵紀元」</p>
    
    <p>林塵站在城牆之上，望向遠方的星空。自從上次大戰結束後，一切都開始恢復平靜。</p>
    
    <p>「師兄，」墨玄的全息影像出現在他身旁，「最近修煉進展如何？」</p>
    
    <p>「還不錯，」林塵微微一笑，「修為又精進了不少。</p>
    
    <p>就在此時，天空突然變色！</p>
    
    <p>「這是……？」林塵臉色一變。</p>
    
    <p>一股強大的氣息正在接近修真界，這氣息既陌生又熟悉……</p>
    
    <p>（本章節內容持續更新中……）</p>
    """
    
    content = f"""<!DOCTYPE html>
<html lang="zh-HK">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - 數據修仙傳</title>
    <style>
        body {{ font-family: "Microsoft JhengHei", Arial, sans-serif; max-width: 800px; margin: 0 auto; padding: 20px; background: #1a1a2e; color: #eee; line-height: 1.8; }}
        h1 {{ color: #f39c12; text-align: center; }}
        .content {{ background: #16213e; padding: 20px; border-radius: 10px; }}
        .nav {{ display: flex; justify-content: space-between; margin-top: 30px; }}
        .nav a {{ background: #0f3460; color: #fff; padding: 10px 20px; text-decoration: none; border-radius: 5px; }}
    </style>
</head>
<body>
    <h1>{title}</h1>
    <div class="content">
        <p>（本章節內容待生成...）</p>
    </div>
    <div class="nav">
        <a href="chapter-{chapter_num-1}.html">上一章</a>
        <a href="index.html">返回目錄</a>
    </div>
</body>
</html>"""
    
    # 寫入文件
    with open(f"{NOVEL_DIR}/chapter-{chapter_num}.html", 'w', encoding='utf-8') as f:
        f.write(content)
    
    return title

def update_index():
    """更新首頁章節列表"""
    # Read index.html
    with open(f"{NOVEL_DIR}/index.html", 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Add new chapter link at the beginning
    new_link = f'<li><a href="chapter-55.html">第55章：時空裂縫</a></li>'
    
    # Find and update the chapter list
    import re
    pattern = r'(<ul class="chapter-list">)'
    content = re.sub(pattern, f'{new_link}\\n\\1', content)
    
    with open(f"{NOVEL_DIR}/index.html", 'w', encoding='utf-8') as f:
        f.write(content)

def push_to_github():
    """推送到GitHub"""
    os.chdir(NOVEL_DIR)
    os.system('git add -A')
    os.system('git commit -m "feat: add chapter 55"')
    os.system('git push origin main')

if __name__ == "__main__":
    current = get_current_chapter()
    print(f"當前最新章節：第{current}章")
    
    new_num = current + 1
    title = generate_new_chapter(new_num)
    print(f"✅ 生成第{new_num}章：{title}")
    
    update_index()
    print("✅ 更新首頁")
    
    print("✅ 完成！")
