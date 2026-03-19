#!/usr/bin/env python3
import re
import sys

def fix_guide(file_path):
    print(f"🔧 處理: {file_path}")
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 查找更新日誌部分
        # 通常在class為update-log或changelog的div中
        patterns = [
            r'(<div class="update-log"[^>]*>.*?</div>)',
            r'(<div class="changelog"[^>]*>.*?</div>)',
            r'(<section class="updates"[^>]*>.*?</section>)',
        ]
        
        update_log = None
        for pattern in patterns:
            match = re.search(pattern, content, re.DOTALL)
            if match:
                update_log = match.group(1)
                break
        
        if update_log:
            print(f"  ✅ 找到更新日誌")
            
            # 從原位置移除
            content = content.replace(update_log, '')
            
            # 在標題後面插入
            # 查找第一個<h1>後面或<header>後面
            insert_patterns = [
                (r'(</h1>)', r'\1\n    <!-- 當日更新 -->\n    ' + update_log),
                (r'(</header>)', r'\1\n    <!-- 當日更新 -->\n    ' + update_log),
            ]
            
            inserted = False
            for pattern, replacement in insert_patterns:
                if re.search(pattern, content):
                    content = re.sub(pattern, replacement, content, count=1)
                    inserted = True
                    break
            
            if inserted:
                print(f"  ✅ 已將更新日誌移到頂部")
                
                # 保存
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                print(f"  ✅ 文件已保存")
            else:
                print(f"  ⚠️  未找到插入位置")
        else:
            print(f"  ℹ️  未找到更新日誌標記")
            
    except FileNotFoundError:
        print(f"  ❌ 文件不存在")
    except Exception as e:
        print(f"  ❌ 錯誤: {e}")

if __name__ == '__main__':
    guides = [
        'beapro-football-guide.html',
        'saint-seiya-guide.html', 
        'kai-tian-guide.html',
        'ai-news.html'
    ]
    
    for guide in guides:
        fix_guide(guide)
        print()
    
    print("🎯 修復完成！")
