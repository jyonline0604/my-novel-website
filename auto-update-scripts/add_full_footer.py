#!/usr/bin/env python3
"""
為網站分頁添加完整頁腳結構腳本
將簡單的footer替換為完整的頁腳結構（分享區塊、導航、評論區）
"""

import os
import re
import sys
from pathlib import Path

# 設定路徑
REPO_PATH = Path(__file__).parent.parent

# 完整頁腳模板（來自chapter-24.html）
FULL_FOOTER_TEMPLATE = """    <section class="share-section">
        <h4 class="share-title">分享這個頁面</h4>
        <div class="share-buttons">
            <a href="#" id="share-facebook" class="share-btn facebook" title="分享到 Facebook"><i class="fab fa-facebook-f"></i></a>
            <a href="#" id="share-twitter" class="share-btn twitter" title="分享到 X (Twitter)"><i class="fab fa-twitter"></i></a>
            <a href="share-line" id="share-line" class="share-btn line" title="分享到 LINE"><i class="fab fa-line"></i></a>
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

def add_full_footer_to_page(file_path, page_type="game"):
    """為單個頁面添加完整頁腳結構"""
    
    print(f"處理頁面: {file_path}")
    
    if not os.path.exists(file_path):
        print(f"❌ 錯誤: 找不到文件 {file_path}")
        return False
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 查找當前的footer位置
        # 先檢查是否已有完整的頁腳結構
        if 'share-section' in content and 'reader-footer-nav' in content:
            print(f"✅ 頁面已有完整頁腳結構")
            return True
        
        # 查找簡單的footer並替換
        simple_footer_pattern = r'<footer class="main-footer">.*?</footer>'
        simple_footer_match = re.search(simple_footer_pattern, content, re.DOTALL)
        
        if simple_footer_match:
            print(f"✅ 找到簡單footer，進行替換")
            
            # 替換簡單footer為完整頁腳
            new_content = content.replace(
                simple_footer_match.group(0),
                FULL_FOOTER_TEMPLATE
            )
        else:
            # 如果找不到簡單footer，嘗試在</main>後插入
            print(f"⚠️  未找到簡單footer，嘗試在</main>後插入")
            
            # 查找</main>位置
            if '</main>' in content:
                new_content = content.replace(
                    '</main>',
                    f'</main>\n\n{FULL_FOOTER_TEMPLATE}'
                )
            else:
                # 嘗試在</body>前插入
                print(f"⚠️  未找到</main>，嘗試在</body>前插入")
                if '</body>' in content:
                    new_content = content.replace(
                        '</body>',
                        f'\n{FULL_FOOTER_TEMPLATE}\n</body>'
                    )
                else:
                    print(f"❌ 無法找到合適的插入位置")
                    return False
        
        # 保存更新後的文件
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f"✅ 頁面更新完成")
        return True
        
    except Exception as e:
        print(f"❌ 更新失敗: {e}")
        import traceback
        traceback.print_exc()
        return False

def main():
    """主函數"""
    
    print("開始為網站分頁添加完整頁腳結構...")
    
    # 需要更新的頁面列表
    pages_to_update = [
        {
            "path": REPO_PATH / "game-guide.html",
            "name": "問劍長生攻略"
        },
        {
            "path": REPO_PATH / "saint-seiya-guide.html",
            "name": "聖鬥士星矢攻略"
        },
        {
            "path": REPO_PATH / "beapro-football-guide.html",
            "name": "Be A Pro Football攻略"
        },
        {
            "path": REPO_PATH / "ai-news.html",
            "name": "AI資訊頁面"
        }
    ]
    
    success_count = 0
    fail_count = 0
    
    for page_info in pages_to_update:
        page_path = page_info["path"]
        page_name = page_info["name"]
        
        print(f"\n--- 更新 {page_name} ---")
        
        success = add_full_footer_to_page(page_path)
        
        if success:
            success_count += 1
        else:
            fail_count += 1
    
    print(f"\n=== 更新完成 ===")
    print(f"✅ 成功: {success_count} 個頁面")
    print(f"❌ 失敗: {fail_count} 個頁面")
    
    if fail_count > 0:
        return 1
    else:
        return 0

if __name__ == "__main__":
    sys.exit(main())