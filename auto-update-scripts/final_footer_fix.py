#!/usr/bin/env python3
"""
最終頁腳格式修復腳本
確保所有頁面有完全一致的頁腳格式和縮進
"""

import os
import re
import sys
from pathlib import Path

# 設定路徑
REPO_PATH = Path(__file__).parent.parent

# 標準頁腳模板（完全正確的格式）
STANDARD_FOOTER = """    <section class="share-section">
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

def standardize_footer_in_page(file_path):
    """標準化單個頁面的頁腳格式"""
    
    print(f"處理頁面: {file_path}")
    
    if not os.path.exists(file_path):
        print(f"❌ 錯誤: 找不到文件 {file_path}")
        return False
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 1. 確保</main>有正確的縮進
        if '</main>' in content:
            # 查找</main>並確保它有4空格縮進
            lines = content.split('\n')
            for i in range(len(lines)):
                if '</main>' in lines[i]:
                    # 去除多餘空白，確保4空格縮進
                    stripped = lines[i].strip()
                    if stripped == '</main>':
                        lines[i] = '    </main>'
                    elif stripped.startswith('</main>'):
                        lines[i] = '    ' + stripped
                    else:
                        # 已經是正確格式
                        pass
            content = '\n'.join(lines)
            print(f"✅ 修復</main>縮進")
        
        # 2. 標準化整個頁腳區域
        # 查找頁腳區域（從<section class="share-section">到</section>前一個）
        footer_pattern = r'<section class="share-section">.*?<section class="comment-section">.*?</section>'
        footer_match = re.search(footer_pattern, content, re.DOTALL)
        
        if footer_match:
            current_footer = footer_match.group(0)
            
            # 比較當前頁腳與標準模板
            if current_footer.strip() != STANDARD_FOOTER.strip():
                print(f"✅ 替換為標準頁腳格式")
                
                # 替換整個頁腳區域
                content = content.replace(current_footer, STANDARD_FOOTER)
            else:
                print(f"✅ 頁腳格式已標準化")
        else:
            print(f"❌ 找不到頁腳區域")
            return False
        
        # 3. 確保頁腳前有正確的間隔
        # 查找</main>和頁腳之間的部分
        main_footer_pattern = r'</main>\s*\n\s*<section class="share-section">'
        if re.search(main_footer_pattern, content):
            # 確保</main>後有兩個換行，然後是4空格縮進的頁腳
            content = re.sub(main_footer_pattern, '</main>\n\n    <section class="share-section">', content)
            print(f"✅ 修復</main>與頁腳之間的間隔")
        
        # 4. 修復share-line連結（再次確認）
        if 'href="share-line"' in content:
            content = content.replace('href="share-line"', 'href="#"')
            print(f"✅ 修復share-line連結")
        
        # 保存更新後的文件
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✅ 頁面標準化完成")
        return True
        
    except Exception as e:
        print(f"❌ 標準化失敗: {e}")
        import traceback
        traceback.print_exc()
        return False

def main():
    """主函數"""
    
    print("開始標準化網站分頁頁腳格式...")
    
    # 需要標準化的頁面列表
    pages_to_standardize = [
        REPO_PATH / "game-guide.html",
        REPO_PATH / "saint-seiya-guide.html",
        REPO_PATH / "beapro-football-guide.html",
        REPO_PATH / "ai-news.html"
    ]
    
    success_count = 0
    fail_count = 0
    
    for page_path in pages_to_standardize:
        page_name = page_path.name
        
        print(f"\n--- 標準化 {page_name} ---")
        
        success = standardize_footer_in_page(page_path)
        
        if success:
            success_count += 1
        else:
            fail_count += 1
    
    print(f"\n=== 標準化完成 ===")
    print(f"✅ 成功: {success_count} 個頁面")
    print(f"❌ 失敗: {fail_count} 個頁面")
    
    if fail_count > 0:
        return 1
    else:
        return 0

if __name__ == "__main__":
    sys.exit(main())