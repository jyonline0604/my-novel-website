#!/usr/bin/env python3
"""
修復頁腳縮進格式腳本
確保所有頁面有統一的縮進格式
"""

import os
import re
import sys
from pathlib import Path

# 設定路徑
REPO_PATH = Path(__file__).parent.parent

def fix_indentation_in_page(file_path):
    """修復單個頁面的縮進格式"""
    
    print(f"處理頁面: {file_path}")
    
    if not os.path.exists(file_path):
        print(f"❌ 錯誤: 找不到文件 {file_path}")
        return False
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        # 查找頁腳區域的起始和結束位置
        footer_start = -1
        footer_end = -1
        
        for i, line in enumerate(lines):
            if '<section class="share-section">' in line:
                footer_start = i
            elif '<section class="comment-section">' in line and footer_start != -1:
                # 找到comment-section，然後找到它的結束標籤
                for j in range(i, len(lines)):
                    if '</section>' in lines[j] and '</section>' not in lines[j+1]:
                        footer_end = j + 1
                        break
                break
        
        if footer_start == -1:
            print(f"⚠️  未找到頁腳區域")
            return True  # 不是錯誤，可能頁面結構不同
        
        print(f"✅ 找到頁腳區域: 行 {footer_start+1} 到 {footer_end}")
        
        # 修復縮進：確保頁腳區域有統一的4空格縮進
        fixed_lines = lines.copy()
        
        # 修復頁腳區域的縮進
        for i in range(footer_start, footer_end):
            line = fixed_lines[i]
            
            # 計算應該的縮進級別
            # 基本縮進：4個空格
            # 但有些行可能需要額外縮進
            
            # 修復<section class="share-section">的縮進
            if '<section class="share-section">' in line and not line.startswith('    '):
                fixed_lines[i] = '    ' + line.lstrip()
                print(f"✅ 修復行 {i+1} 的縮進")
            
            # 修復其他頁腳元素的縮進
            elif any(tag in line for tag in ['<h4 class="share-title">', '<div class="share-buttons">', 
                                           '<a href="#"', '<button id="copy-link-btn"',
                                           '<footer class="reader-footer-nav">', '<footer class="main-footer">',
                                           '<section class="comment-section">']):
                
                # 檢查是否需要修復
                if not line.startswith('    '):
                    fixed_lines[i] = '    ' + line.lstrip()
                elif line.startswith('        ') and not line.startswith('            '):
                    # 已經是正確的縮進
                    pass
                else:
                    # 確保有至少4空格縮進
                    current_indent = len(line) - len(line.lstrip())
                    if current_indent < 4:
                        fixed_lines[i] = '    ' + line.lstrip()
        
        # 檢查是否有明顯的縮進不一致
        changes_made = fixed_lines != lines
        
        if changes_made:
            # 保存更新後的文件
            with open(file_path, 'w', encoding='utf-8') as f:
                f.writelines(fixed_lines)
            print(f"✅ 縮進修復完成")
        else:
            print(f"✅ 縮進已正確")
        
        return True
        
    except Exception as e:
        print(f"❌ 修復失敗: {e}")
        import traceback
        traceback.print_exc()
        return False

def main():
    """主函數"""
    
    print("開始修復網站分頁縮進格式...")
    
    # 需要修復的頁面列表
    pages_to_fix = [
        REPO_PATH / "game-guide.html",
        REPO_PATH / "saint-seiya-guide.html",
        REPO_PATH / "beapro-football-guide.html",
        REPO_PATH / "ai-news.html"
    ]
    
    success_count = 0
    fail_count = 0
    
    for page_path in pages_to_fix:
        page_name = page_path.name
        
        print(f"\n--- 修復 {page_name} ---")
        
        success = fix_indentation_in_page(page_path)
        
        if success:
            success_count += 1
        else:
            fail_count += 1
    
    print(f"\n=== 修復完成 ===")
    print(f"✅ 成功: {success_count} 個頁面")
    print(f"❌ 失敗: {fail_count} 個頁面")
    
    if fail_count > 0:
        return 1
    else:
        return 0

if __name__ == "__main__":
    sys.exit(main())