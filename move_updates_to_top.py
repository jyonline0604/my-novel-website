#!/usr/bin/env python3
import re

def move_updates_to_top(file_path):
    print(f"🔧 處理: {file_path}")
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 查找更新日誌部分
        # 模式：找到包含"更新日誌"的section
        pattern = r'(<section class="content-card">\s*<h2 class="section-title">.*更新日誌.*</h2>.*?)</section>'
        
        match = re.search(pattern, content, re.DOTALL)
        
        if match:
            update_section = match.group(1) + '</section>'
            print(f"  ✅ 找到更新日誌部分")
            
            # 從原位置移除
            content = content.replace(update_section, '')
            
            # 找到第一個<main>或<header>後面插入
            insert_after = None
            for tag in ['</header>', '<main class="container">', '<main>']:
                if tag in content:
                    insert_after = tag
                    break
            
            if insert_after:
                content = content.replace(insert_after, insert_after + '\n\n    <!-- 當日更新 -->\n    ' + update_section, 1)
                print(f"  ✅ 已將更新日誌移到頂部")
                
                # 保存
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"  ✅ 文件已保存")
            else:
                print(f"  ⚠️  未找到插入位置")
        else:
            print(f"  ℹ️  未找到更新日誌部分")
            
    except Exception as e:
        print(f"  ❌ 錯誤: {e}")

if __name__ == '__main__':
    move_updates_to_top('beapro-football-guide.html')
