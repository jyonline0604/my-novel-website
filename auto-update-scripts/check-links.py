#!/usr/bin/env python3
"""
攻略网站链接完整性检测器
 - 扫描所有攻略主页，检查所有导航链接和攻略卡片链接
 - 验证目标文件是否存在
 - 输出缺失链接报告
"""

import re
import sys
from pathlib import Path

REPO_DIR = Path("/home/openclaw/.openclaw/workspace/my-novel-website")
GUIDE_PAGES = ["game-guide.html", "saint-seiya-guide.html", "beapro-football-guide.html", "kai-tian-guide.html"]

def check_file_exists(path):
    """检查文件是否存在（支持软链接）"""
    full_path = REPO_DIR / Path(path.lstrip('/'))
    return full_path.exists() or full_path.is_symlink()

def extract_links(html_content):
    """提取所有内部链接"""
    # 匹配 href="/..." 的内部链接
    pattern = r'href="(/[^"]+)"'
    return re.findall(pattern, html_content)

def scan_guide_page(page_file):
    """扫描单个攻略页的所有链接"""
    html = (REPO_DIR / page_file).read_text(encoding='utf-8')
    links = extract_links(html)
    
    broken = []
    for link in set(links):  # 去重
        if link.startswith('/guides/'):
            if not check_file_exists(link):
                broken.append(link)
    
    return broken

def main():
    print("🔍 开始检测攻略网站链接完整性...")
    total_broken = 0
    
    for page in GUIDE_PAGES:
        page_path = REPO_DIR / page
        if not page_path.exists():
            print(f"❌ 主页不存在: {page}")
            continue
            
        broken = scan_guide_page(page)
        if broken:
            print(f"\n⚠️  {page} 发现 {len(broken)} 个失效链接:")
            for link in broken:
                print(f"   - {link}")
            total_broken += len(broken)
        else:
            print(f"✅ {page} 所有链接正常")
    
    print(f"\n📊 总计: {total_broken} 个失效链接")
    
    if total_broken > 0:
        print("\n💡 建议: 运行 fix-missing-guides.py 自动创建缺失文件")
        return 1
    return 0

if __name__ == "__main__":
    sys.exit(main())
