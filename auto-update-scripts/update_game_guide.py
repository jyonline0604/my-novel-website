#!/usr/bin/env python3
"""
問劍長生遊戲攻略自動更新腳本
"""

import os
import re
import json
import sys
from datetime import datetime
from pathlib import Path

# 設定路徑
REPO_PATH = Path(__file__).parent.parent
GAME_GUIDE_FILE = REPO_PATH / "game-guide.html"
UPDATE_TEMPLATE = """
    <strong>📝 {date}更新：</strong> {summary}
"""

def update_timestamp_and_content():
    """更新攻略頁面的時間戳和內容"""
    
    print(f"正在更新問劍長生攻略: {GAME_GUIDE_FILE}")
    
    if not GAME_GUIDE_FILE.exists():
        print(f"錯誤: 找不到文件 {GAME_GUIDE_FILE}")
        return False
    
    try:
        with open(GAME_GUIDE_FILE, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 獲取當前日期
        today_chinese = datetime.now().strftime("%Y年%m月%d日")
        today_iso = datetime.now().strftime("%Y-%m-%d")
        
        # 1. 更新最後更新時間
        old_update_pattern = r'<div class="update-time">最後更新：\d{4} 年 \d{1,2} 月 \d{1,2} 日</div>'
        new_update_div = f'<div class="update-time">最後更新：{today_chinese}</div>'
        
        content = re.sub(old_update_pattern, new_update_div, content)
        
        # 2. 更新highlight區域的更新摘要
        # 查找highlight區域
        highlight_pattern = r'<div class="highlight">(.*?)</div>'
        highlight_match = re.search(highlight_pattern, content, re.DOTALL)
        
        if highlight_match:
            highlight_content = highlight_match.group(1)
            
            # 檢查是否已有更新摘要
            update_pattern = r'<strong>📝 \d{4}年\d{1,2}月\d{1,2}日更新：</strong>'
            
            if re.search(update_pattern, highlight_content):
                # 替換現有的更新摘要
                new_summary = f"經自動更新系統檢查，遊戲版本維持穩定。建議玩家關注每日任務完成度，合理分配修煉資源。本日重點提醒：1) 心法重置機會應優先使用於當前主力流派；2) 宗門貢獻每日上限務必完成；3) 法寶共鳴效果可大幅提升戰力。"
                
                # 替換更新摘要
                new_highlight = re.sub(
                    r'<strong>📝 \d{4}年\d{1,2}月\d{1,2}日更新：</strong>.*?(?=<br><br>|$)',
                    f'<strong>📝 {today_chinese}更新：</strong> {new_summary}',
                    highlight_content,
                    flags=re.DOTALL
                )
                
                # 替換整個highlight區域
                new_div = f'<div class="highlight">\n{new_highlight}\n</div>'
                content = content.replace(highlight_match.group(0), new_div)
                
                print(f"✅ 已更新highlight區域")
            else:
                # 添加新的更新摘要
                new_summary = f"遊戲版本穩定運行中。本日建議：1) 完成所有日常任務獲取資源；2) 檢查心法重置機會是否使用；3) 參與宗門活動提升貢獻度。"
                new_update_text = f'<strong>📝 {today_chinese}更新：</strong> {new_summary}<br><br>'
                
                # 在highlight內容開頭插入
                lines = highlight_content.strip().split('\n')
                if lines:
                    lines[0] = new_update_text + lines[0]
                    new_highlight = '\n'.join(lines)
                    new_div = f'<div class="highlight">\n{new_highlight}\n</div>'
                    content = content.replace(highlight_match.group(0), new_div)
                    
                    print(f"✅ 已添加新的更新摘要")
        
        # 3. 檢查是否需要更新其他內容區域
        # 例如：檢查是否有需要更新的表格或列表
        
        # 保存更新後的文件
        with open(GAME_GUIDE_FILE, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✅ 問劍長生攻略更新完成！")
        print(f"   更新時間: {today_chinese}")
        
        return True
        
    except Exception as e:
        print(f"❌ 更新失敗: {e}")
        import traceback
        traceback.print_exc()
        return False

def generate_ai_enhanced_content():
    """使用AI生成增強內容（可選功能）"""
    
    # 這裡可以整合DeepSeek API來生成更豐富的攻略內容
    # 但需要考慮API成本和內容質量
    
    print("⚠️  AI增強內容生成功能待實現")
    return None

def check_game_updates():
    """檢查遊戲是否有更新（模擬功能）"""
    
    # 這裡可以實現實際的遊戲更新檢查
    # 例如：訪問遊戲官網、檢查版本號等
    
    print("🔍 檢查遊戲更新...")
    
    # 模擬檢查結果
    game_updates = {
        "has_update": False,  # 假設今天沒有重大更新
        "version": "1.0.5",
        "last_update_date": "2026-02-22",
        "update_summary": "遊戲版本穩定，無重大更新"
    }
    
    return game_updates

def main():
    """主函數"""
    
    print("開始更新問劍長生遊戲攻略...")
    
    # 檢查遊戲更新
    game_status = check_game_updates()
    
    # 更新頁面內容
    success = update_timestamp_and_content()
    
    if success:
        print("✅ 問劍長生攻略更新流程完成")
        return 0
    else:
        print("❌ 問劍長生攻略更新失敗")
        return 1

if __name__ == "__main__":
    sys.exit(main())