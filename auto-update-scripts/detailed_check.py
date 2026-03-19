#!/usr/bin/env python3
"""详细检查所有攻略页的标题一致性"""

from pathlib import Path
import re

REPO_DIR = Path("/home/openclaw/.openclaw/workspace/my-novel-website")

# 游戏主页映射
GAME_PAGES = {
    "game-guide.html": "game_guide",
    "saint-seiya-guide.html": "saint_seiya",
    "beapro-football-guide.html": "beapro_football",
    "kai-tian-guide.html": "kai_tian"
}

def extract_card_titles(html):
    """从主页提取所有卡片标题"""
    pattern = r'<strong>([^<]+)</strong>'
    titles = re.findall(pattern, html)
    return [t.strip() for t in titles if t.strip()]

def check_consistency(game_page, game_type):
    """检查单个游戏的标题一致性"""
    html = (REPO_DIR / game_page).read_text(encoding='utf-8')
    card_titles = extract_card_titles(html)
    
    print(f"\n{'='*60}")
    print(f"检查: {game_page} ({game_type})")
    print(f"{'='*60}")
    
    issues = []
    
    for card_title in card_titles:
        # 查找对应的详细页（尝试多种可能的文件名）
        possible_files = [
            f"guides/{game_type}/{card_title}.html",
            f"guides/{game_type}/{card_title}-guide.html",
        ]
        
        found_file = None
        for pf in possible_files:
            p = REPO_DIR / pf
            if p.exists():
                found_file = p
                break
        
        if not found_file:
            # 尝试模糊匹配
            guide_files = list((REPO_DIR / "guides" / game_type).glob("*guide.html"))
            for gf in guide_files:
                content = gf.read_text(encoding='utf-8')
                h1_match = re.search(r'<h1>([^<]+)</h1>', content)
                if h1_match:
                    page_title = h1_match.group(1).strip()
                    if card_title in page_title or page_title in card_title:
                        found_file = gf
                        break
        
        if found_file:
            # 检查标题是否完全一致
            content = found_file.read_text(encoding='utf-8')
            h1_match = re.search(r'<h1>([^<]+)</h1>', content)
            if h1_match:
                page_title = h1_match.group(1).strip()
                if page_title == card_title:
                    print(f"  ✅ {card_title} -> {found_file.name}")
                else:
                    print(f"  ❌ {card_title} -> {found_file.name} (标题: '{page_title}')")
                    issues.append((found_file, card_title, page_title))
            else:
                print(f"  ⚠️  {card_title} -> {found_file.name} (无 h1 标题)")
        else:
            print(f"  ❌ {card_title} -> 文件不存在!")
            issues.append((None, card_title, None))
    
    return issues

def main():
    all_issues = []
    
    for page, game_type in GAME_PAGES.items():
        if not (REPO_DIR / page).exists():
            print(f"❌ 跳过: {page} 不存在")
            continue
        issues = check_consistency(page, game_type)
        all_issues.extend([(page, *issue) for issue in issues])
    
    print(f"\n{'='*60}")
    print(f"📊 总结")
    print(f"{'='*60}")
    print(f"总问题数: {len(all_issues)}")
    
    if all_issues:
        print("\n问题详情:")
        for game_page, file, card_title, actual_title in all_issues:
            if file:
                print(f"  [{game_page}] {card_title} -> {file.name} (标题: '{actual_title}')")
            else:
                print(f"  [{game_page}] {card_title} -> 文件不存在!")
    
    return 0

if __name__ == "__main__":
    exit(main())
