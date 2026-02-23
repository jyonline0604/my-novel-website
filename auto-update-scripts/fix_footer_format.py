#!/usr/bin/env python3
"""
修復頁腳格式和連結錯誤腳本
"""

import os
import re
import sys
from pathlib import Path

# 設定路徑
REPO_PATH = Path(__file__).parent.parent

# 正確的頁腳模板（修正了share-line連結錯誤）
CORRECT_FOOTER_TEMPLATE = """    <section class="share-section">
        <h4 class="share-title">分享這個頁面</h4>
        <div class="share-buttons">
            <a href="#" id="share-facebook" class="share-btn facebook" title="分享到 Facebook"><i class="fab fa-facebook-f"></i></a>
            <a href="#" id="share-twitter" class="share-btn twitter" title="分享到 X (Twitter)"><i class="fab fa-twitter"></i></a>
            <a href="#" id="share-line" class="share-btn line" title="分享到 LINE"><i class="fab fa-line"></i></a>
            <button id="copy-link-btn" class="share-btn copy-link" title="複製連結"><i class="fas fa-link"></i></button>
        </div>
    </section>

    <footer class="reader-footer-nav">
        <a href="index.html" id="prev-chapter-btn" class="nav-button">« 返回首頁</a>
        <a href="#top" id="next-chapter-btn" class="nav-button">返回頂部</a>
    </footer>

    <footer class="main-footer">
        <p>&copy; 2026 大肥瞄. All Rights Reserved. | <a href="author.html" style="color: inherit;">關於作者</a></p>
    </footer>
    
    <section class="comment-section">
        <h3 class="comment-section-title">讀者留言</h3>
    </section>
"""

def fix_footer_in_page(file_path):
    """修復單個頁面的頁腳格式"""
    
    print(f"處理頁面: {file_path}")
    
    if not os.path.exists(file_path):
        print(f"❌ 錯誤: 找不到文件 {file_path}")
        return False
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 檢查並修復share-line連結錯誤
        # 錯誤模式：href="share-line" 應該是 href="#"
        if 'href="share-line"' in content:
            print(f"✅ 修復share-line連結錯誤")
            content = content.replace('href="share-line"', 'href="#"')
        
        # 確保頁腳格式一致
        # 查找頁腳區域（從share-section到comment-section）
        footer_pattern = r'<section class="share-section">.*?<section class="comment-section">.*?</section>'
        footer_match = re.search(footer_pattern, content, re.DOTALL)
        
        if footer_match:
            current_footer = footer_match.group(0)
            
            # 比較當前頁腳與正確模板的差異
            if current_footer != CORRECT_FOOTER_TEMPLATE.strip():
                print(f"✅ 替換為標準頁腳格式")
                
                # 替換整個頁腳區域
                content = content.replace(current_footer, CORRECT_FOOTER_TEMPLATE.strip())
            else:
                print(f"✅ 頁腳格式已正確")
        
        # 檢查是否有多餘的空行
        # 修復script標籤前的多餘空行
        script_pattern = r'</section>\s*\n\s*\n\s*<script'
        if re.search(script_pattern, content):
            print(f"✅ 修復script前的空行")
            content = re.sub(script_pattern, '</section>\n\n    <script', content)
        
        # 保存更新後的文件
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✅ 頁面修復完成")
        return True
        
    except Exception as e:
        print(f"❌ 修復失敗: {e}")
        import traceback
        traceback.print_exc()
        return False

def main():
    """主函數"""
    
    print("開始修復網站分頁頁腳格式...")
    
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
        
        success = fix_footer_in_page(page_path)
        
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