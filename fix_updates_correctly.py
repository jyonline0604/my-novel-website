#!/usr/bin/env python3
import re
import sys

def fix_updates_correctly(file_path):
    print(f"🔧 正確修復 {file_path}")
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 1. 找到真正的更新日誌部分
        # 模式：包含log-date的更新記錄
        log_entry_pattern = r'(<div class="log-entry">\s*<div class="log-date">(.*?)</div>\s*<div class="log-content">.*?)</div>\s*</div>\s*</div>'
        
        # 2. 找到所有更新記錄
        log_entries = []
        for match in re.finditer(log_entry_pattern, content, re.DOTALL):
            log_entries.append(match.group(1))
        
        # 3. 從原位置移除所有更新記錄
        content_without_logs = re.sub(log_entry_pattern, '', content, flags=re.DOTALL)
        
        # 4. 重新排列更新記錄（最新的在最上面）
        # 因為HTML中是從舊到新排列的，所以我們需要反轉
        log_entries.reverse()
        
        # 5. 創建新的更新日誌部分
        new_log_section = '<section class="content-card">\n'
        new_log_section += '    <h2 class="section-title">📝 更新日誌</h2>\n'
        new_log_section += '    <div class="section-content">'
        
        for entry in log_entries:
            new_log_section += '\n        ' + entry + '</div>'
        
        new_log_section += '\n    </div>\n</section>'
        
        # 6. 找到插入位置（在header後面）
        # 查找第一個<main>或<header>後面
        insert_after = None
        for tag in ['</header>', '<main class="container">', '<main>']:
            if tag in content_without_logs:
                insert_after = tag
                break
        
        if insert_after:
            # 在header後插入新的更新日誌
            content_without_logs = content_without_logs.replace(insert_after, insert_after + '\n\n    <!-- 當日更新 -->\n    ' + new_log_section, 1)
            print(f"  ✅ 已將更新日誌移到頂部")
        else:
            print(f"  ⚠️  未找到插入位置")
        
        # 7. 移除錯誤的「當日更新」標記
        content_without_logs = content_without_logs.replace('<!-- 當日更新 -->', '')
        
        # 8. 保存
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content_without_logs)
        
        print(f"  ✅ 檔案已保存")
        
    except Exception as e:
        print(f"  ❌ 錯誤: {e}")

if __name__ == '__main__':
    fix_updates_correctly('beapro-football-guide.html')
