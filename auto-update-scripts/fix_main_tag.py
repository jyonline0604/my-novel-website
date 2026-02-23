#!/usr/bin/env python3
"""
修復缺失的</main>標籤腳本
"""

import os
import re
import sys
from pathlib import Path

# 設定路徑
REPO_PATH = Path(__file__).parent.parent

def fix_main_tag_in_page(file_path):
    """修復單個頁面的<main>標籤"""
    
    print(f"處理頁面: {file_path}")
    
    if not os.path.exists(file_path):
        print(f"❌ 錯誤: 找不到文件 {file_path}")
        return False
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 檢查是否有開始的<main>標籤但沒有結束的</main>標籤
        has_opening_main = '<main ' in content or '<main>' in content
        has_closing_main = '</main>' in content
        
        print(f"  有開頭<main>: {has_opening_main}, 有結尾</main>: {has_closing_main}")
        
        if has_opening_main and not has_closing_main:
            print(f"✅ 發現缺失的</main>標籤，正在修復...")
            
            # 找到<main>標籤
            main_opening_pattern = r'<main[^>]*>'
            main_match = re.search(main_opening_pattern, content)
            
            if main_match:
                # 在頁腳開始前插入</main>
                # 頁腳從<section class="share-section">開始
                footer_start = content.find('<section class="share-section">')
                
                if footer_start != -1:
                    # 在footer開始前插入</main>，並確保有適當的換行
                    before_footer = content[:footer_start].rstrip()
                    after_footer = content[footer_start:]
                    
                    # 確保在</main>前有適當的換行
                    if not before_footer.endswith('\n\n'):
                        if before_footer.endswith('\n'):
                            new_content = before_footer + '\n    </main>\n\n' + after_footer
                        else:
                            new_content = before_footer + '\n    </main>\n\n' + after_footer
                    else:
                        new_content = before_footer.rstrip() + '\n    </main>\n\n' + after_footer
                    
                    content = new_content
                    print(f"✅ 已添加</main>標籤")
                else:
                    print(f"❌ 找不到頁腳開始位置")
                    return False
            else:
                print(f"❌ 找不到<main>標籤")
                return False
        elif not has_opening_main:
            print(f"⚠️  頁面沒有<main>標籤，跳過")
            return True
        else:
            print(f"✅ </main>標籤已存在")
        
        # 保存更新後的文件
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return True
        
    except Exception as e:
        print(f"❌ 修復失敗: {e}")
        import traceback
        traceback.print_exc()
        return False

def fix_main_indentation(file_path):
    """修復</main>標籤前的縮進"""
    
    print(f"修復縮進: {file_path}")
    
    if not os.path.exists(file_path):
        print(f"❌ 錯誤: 找不到文件 {file_path}")
        return False
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        # 查找</main>位置
        for i, line in enumerate(lines):
            if '</main>' in line:
                # 檢查縮進
                if not line.startswith('    '):
                    print(f"✅ 修復</main>縮進 (行 {i+1})")
                    lines[i] = '    ' + line.lstrip()
                break
        
        # 保存更新後的文件
        with open(file_path, 'w', encoding='utf-8') as f:
            f.writelines(lines)
        
        return True
        
    except Exception as e:
        print(f"❌ 縮進修復失敗: {e}")
        return False

def main():
    """主函數"""
    
    print("開始修復網站分頁<main>標籤...")
    
    # 需要修復的頁面列表
    pages_to_fix = [
        REPO_PATH / "beapro-football-guide.html",
        REPO_PATH / "ai-news.html"
    ]
    
    success_count = 0
    fail_count = 0
    
    for page_path in pages_to_fix:
        page_name = page_path.name
        
        print(f"\n--- 修復 {page_name} ---")
        
        # 修復缺失的</main>標籤
        success = fix_main_tag_in_page(page_path)
        
        if success:
            # 修復縮進
            fix_main_indentation(page_path)
            success_count += 1
        else:
            fail_count += 1
    
    print(f"\n=== 修復完成 ===")
    print(f"✅ 成功: {success_count} 個頁面")
    print(f"❌ 失敗: {fail_count} 個頁面")
    
    # 也修復已有</main>但縮進不正確的頁面
    print(f"\n--- 檢查其他頁面的縮進 ---")
    other_pages = [
        REPO_PATH / "game-guide.html",
        REPO_PATH / "saint-seiya-guide.html"
    ]
    
    for page_path in other_pages:
        page_name = page_path.name
        print(f"檢查 {page_name}...")
        fix_main_indentation(page_path)
    
    if fail_count > 0:
        return 1
    else:
        return 0

if __name__ == "__main__":
    sys.exit(main())