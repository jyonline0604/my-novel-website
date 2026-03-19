#!/usr/bin/env python3
# 專門修復第30章的格式問題

import re

def fix_chapter_30():
    with open('chapter-30.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 找到第一個section（空標題）
    # 匹配模式：<div class="section">後跟空標題和《科技修真傳》第30章
    pattern = r'(\s*<div class="section">\s*<h3 class="section-title">一、</h3>\s*<p>《科技修真傳》第30章</p>\s*</div>\s*)'
    
    # 刪除第一個空section
    new_content = re.sub(pattern, '', content, count=1)
    
    # 現在需要重新編號剩下的sections
    # 將「二、」改為「一、」，「三、」改為「二、」，「四、」改為「三、」
    new_content = new_content.replace('二、', '一、', 1)
    new_content = new_content.replace('三、', '二、', 1)
    new_content = new_content.replace('四、', '三、', 1)
    
    # 寫回文件
    with open('chapter-30.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print("✅ 第30章修復完成")

if __name__ == '__main__':
    fix_chapter_30()