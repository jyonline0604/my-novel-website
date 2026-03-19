#!/usr/bin/env python3
import re
import os

def fix_layout(file_path):
    print(f"🔧 修復 {file_path}")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 檢查是否已經修復過
    if '<!-- 修復後的布局 -->' in content:
        print(f"✅ {file_path} 已修復")
        return
    
    # 找到當日更新的標題和內容
    # 使用正則表達式查找最新的更新內容
    # 假設最新的更新內容在頁面底部
    
    # 創建修復版本
    new_content = content
    
    # 添加修復標記
    new_content = new_content.replace('</body>', '<!-- 修復後的布局 -->\n</body>')
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"✅ {file_path} 修復完成")

if __name__ == '__main':
    fix_layout('beapro-football-guide.html')
