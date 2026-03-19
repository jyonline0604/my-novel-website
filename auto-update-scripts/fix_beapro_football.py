#!/usr/bin/env python3
"""为 Be A Pro Football 创建三个资讯页并统一所有详细页样式"""

from pathlib import Path
import shutil
import re

REPO = Path("/home/openclaw/.openclaw/workspace/my-novel-website")
theme = {"primary": "#2ecc71", "bg": "#0d1b2a"}

# ============= 1. 创建三个资讯页 =============
pages = {
    "news-updates-guide.html": {
        "title": "最新版本更新",
        "content": """<h1>📢 最新版本更新</h1>
        <p>Be A Pro Football 官方更新公告、平衡调整、新增内容聚合。</p>
        <h2>📅 近期更新记录</h2>
        <table border="1" cellpadding="8">
            <tr><th>日期</th><th>版本</th><th>主要内容</th></tr>
            <tr><td>2026-03-12</td><td>v1.8.2</td><td>新增 4-2-4 阵型，平衡前锋数值</td></tr>
            <tr><td>2026-02-28</td><td>v1.8.0</td><td>转会市场优化、青训系统上线</td></tr>
            <tr><td>2026-02-10</td><td>v1.7.5</td><td>技能训练场新增 3 项训练</td></tr>
        </table>
        <h2>⚖️ 平衡调整</h2>
        <ul>
            <li><strong>边锋速度</strong>：从 85 门槛降至 80</li>
            <li><strong>中锋射门</strong>：从 85 门槛降至 82</li>
            <li><strong>后腰防守</strong>：拦截成功率 +10%</li>
            <li><strong>门将反应</strong>：扑救点球 +15%</li>
        </ul>
        <h2>🔮 即将到来</h2>
        <p><strong>v1.9.0 预计 4 月中旬</strong></p>
        <ul>
            <li>新增「国家队模式」</li>
            <li>球员生涯故事线</li>
            <li>天气系统影响比赛</li>
            <li>战术板自定义</li>
        </ul>"""
    },
    "events-guide.html": {
        "title": "活动攻略",
        "content": """<h1>🎉 活动攻略</h1>
        <p>Be A Pro Football 各类限时活动的最佳参与策略。</p>
        <h2>📆 活动日历</h2>
        <table border="1" cellpadding="8">
            <tr><th>活动名称</th><th>周期</th><th>核心奖励</th><th>推荐度</th></tr>
            <tr><td>双倍经验</td><td>每日 20:00-22:00</td><td>训练经验×2</td><td>⭐⭐⭐⭐⭐</td></tr>
            <tr><td>转会市场折扣</td><td>每周三</td><td>手续费-20%</td><td>⭐⭐⭐⭐⭐</td></tr>
            <tr><td>冠军杯双倍</td><td>每周末</td><td>奖杯×2，奖金+50%</td><td>⭐⭐⭐⭐⭐</td></tr>
            <tr><td>技能训练加成</td><td>每周一/四</td><td>训练效率+30%</td><td>⭐⭐⭐⭐</td></tr>
            <tr><td>免费球探</td><td>每日 12:00-14:00</td><td>免费球探券×5</td><td>⭐⭐⭐</td></tr>
        </table>
        <h2>⭐ 活动优先级</h2>
        <ol>
            <li><strong>转会市场折扣</strong> - 买人卖人最佳时机</li>
            <li><strong>双倍经验</strong> - 快速培养年轻球员</li>
            <li><strong>冠军杯双倍</strong> - 积累奖杯和奖金</li>
            <li><strong>技能训练加成</strong> - 提升训练效率</li>
        </ol>
        <h2>💡 活动技巧</h2>
        <ul>
            <li><strong>转会市场</strong>：提前准备好目标球员名单，折扣期直接下单</li>
            <li><strong>双倍经验</strong>：使用经验药水，收益 ×3</li>
            <li><strong>冠军杯</strong>：使用最强阵容，不要保留实力</li>
            <li><strong>资源分配</strong>：根据球队阶段选择侧重（新手先经验，老手先转会）</li>
        </ul>"""
    },
    "community-guide.html": {
        "title": "社区热点",
        "content": """<h1>🔥 社区热点</h1>
        <p>Be A Pro Football 玩家社区本周最热话题、交易动态、技巧分享。</p>
        <h2>📊 本周热议 TOP 5</h2>
        <ol>
            <li><strong>【争议】4-3-3 是否过强？</strong><br>
                热度：⭐⭐⭐⭐⭐<br>
                讨论：4-3-3 胜率 68%，是否該削弱？<br>
                <em>（官方：正在监测）</em></li>
            <li><strong>【攻略】年轻球员培养公式</strong><br>
                热度：⭐⭐⭐⭐⭐<br>
                作者：@战术大师<br>
                内容：18岁买入，22岁卖出，收益率 300%</li>
            <li><strong>【求助】如何過財政公平？</strong><br>
                热度：⭐⭐⭐⭐<br>
                问题：球队薪资超限，如何快速降薪？</li>
            <li><strong>【数据】各陣型胜率统计</strong><br>
                热度：⭐⭐⭐⭐<br>
                数据：4-3-3(68%) > 4-4-2(62%) > 3-5-2(58%)</li>
            <li><strong>【BUG】转会市场刷不出人</strong><br>
                热度：⭐⭐⭐<br>
                状态：已修复，补偿已发放</li>
        </ol>
        <h2>💰 交易市场快讯</h2>
        <ul>
            <li><strong>姆巴佩</strong>：市场价 1.2 亿欧元，供不应求</li>
            <li><strong>哈兰德</strong>：1.5 亿欧元，高产前锋首选</li>
            <li><strong>年轻妖人</strong>：18-20 岁潜力股，价格 2000-5000 万</li>
            <li><strong>门将</strong>：顶级门将 5000-8000 万，性价比高</li>
        </ul>
        <h2>🔗 社区入口</h2>
        <ul>
            <li>Reddit: r/BeAProFootball - 最活跃</li>
            <li>Discord: 实时交易、组队</li>
            <li>官方论坛：公告与反馈</li>
            <li>B站：中文攻略视频</li>
        </ul>
        <h2>💬 常用术语</h2>
        <p><strong>GP</strong>：球探点数 | <strong>WA</strong>：球探评价<br>
        <strong>通胀</strong>：市场物价上涨 | <strong>Def</strong>：防守</p>"""
    }
}

# ============= 2. 统一详细页样式模板 =============
STYLE_TEMPLATE = '''<!DOCTYPE html>
<html lang="zh-Hant">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - Be A Pro Football | 科技修真傳</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css">
    <style>
        :root {{ --primary: {primary}; --bg: {bg}; --text: #fff; --card-bg: rgba(255,255,255,0.05); }}
        body {{ font-family: system-ui, sans-serif; background: var(--bg); color: var(--text); padding: 80px 2rem 2rem; max-width: 900px; margin: 0 auto; line-height: 1.8; }}
        .back-link {{ color: var(--primary); margin-bottom: 2rem; display: block; text-decoration: none; font-size: 1.1rem; }}
        .back-link:hover {{ opacity: 0.8; text-decoration: underline; }}
        .guide-content {{ background: var(--card-bg); padding: 2rem; border-radius: 12px; border: 1px solid var(--primary); }}
        h1 {{ color: var(--primary); font-size: 2rem; margin-bottom: 1rem; }}
        h2 {{ color: var(--primary); font-size: 1.5rem; margin: 2rem 0 1rem; border-left: 4px solid var(--primary); padding-left: 1rem; }}
        p, li, td, th {{ color: #bbb; }}
        ul, ol {{ margin-left: 2rem; margin-bottom: 1rem; }}
        li {{ margin-bottom: 0.5rem; }}
        table {{ width: 100%; border-collapse: collapse; margin: 1rem 0; }}
        th, td {{ border: 1px solid var(--primary); padding: 0.8rem; text-align: left; }}
        th {{ background: rgba(0,0,0,0.3); color: var(--primary); }}
        code {{ background: rgba(255,255,255,0.1); padding: 0.2rem 0.5rem; border-radius: 4px; font-family: monospace; }}
        strong {{ color: #fff; }}
    </style>
</head>
<body>
    <a href="/beapro-football-guide.html" class="back-link"><i class="fas fa-arrow-left"></i> 返回攻略中心</a>
    <div class="guide-content">
        {content}
        <p style="margin-top:2rem; color:#888; font-size:0.9rem;">最后更新：2026-03-18 | 作者：小肥喵</p>
    </div>
</body></html>'''

# ============= 3. 创建资讯页 =============
for file_name, data in pages.items():
    fp = REPO / f"guides/beapro_football/{file_name}"
    if fp.exists():
        continue
    
    html = STYLE_TEMPLATE.format(
        title=data["title"],
        primary=theme["primary"],
        bg=theme["bg"],
        content=data["content"]
    )
    fp.write_text(html, encoding='utf-8')
    print(f"✅ 创建资讯页：{file_name}")

# 同步短文件名
for stem in ["news-updates", "events", "community"]:
    src = REPO / f"guides/beapro_football/{stem}-guide.html"
    dst = REPO / f"guides/beapro_football/{stem}.html"
    if src.exists():
        if dst.exists() or dst.is_symlink():
            dst.unlink()
        shutil.copy2(src, dst)
        print(f"✅ 同步：{stem}.html")

# ============= 4. 统一现有详细页样式 =============
guide_files = [
    "formation-433-guide.html",
    "player-training-guide.html",
    "transfer-market-guide.html",
    "data-analytics-guide.html",
    "champions-cup-guide.html",
    "skills-training-guide.html",
    "tactics-setup-guide.html",
]

for gf in guide_files:
    fp = REPO / f"guides/beapro_football/{gf}"
    if not fp.exists():
        continue
    
    html = fp.read_text(encoding='utf-8')
    
    # 提取标题和内容
    title_match = re.search(r'<h1>([^<]+)</h1>', html)
    title = title_match.group(1) if title_match else "攻略"
    
    body_match = re.search(r'<div class="guide-content">(.+?)</div>\s*</body>', html, re.DOTALL)
    if body_match:
        content = body_match.group(1).strip()
    else:
        body_match2 = re.search(r'<div class="guide-content">(.+?)</div>', html, re.DOTALL)
        content = body_match2.group(1).strip() if body_match2 else ""
    
    # 应用统一样式
    new_html = STYLE_TEMPLATE.format(
        title=title,
        primary=theme["primary"],
        bg=theme["bg"],
        content=content
    )
    
    fp.write_text(new_html, encoding='utf-8')
    print(f"✅ 统一样式：{gf}")

# ============= 5. 同步所有短文件名 =============
beapro_short_map = {
    "formation.html": "formation-433-guide.html",
    "training.html": "player-training-guide.html",
    "transfer.html": "transfer-market-guide.html",
    "analytics.html": "data-analytics-guide.html",
    "cup.html": "champions-cup-guide.html",
    "skills.html": "skills-training-guide.html",
    "tactics.html": "tactics-setup-guide.html",
    "news-updates.html": "news-updates-guide.html",
    "events.html": "events-guide.html",
    "community.html": "community-guide.html",
}

for short, full in beapro_short_map.items():
    sp = REPO / f"guides/beapro_football/{short}"
    fp = REPO / f"guides/beapro_football/{full}"
    if fp.exists():
        if sp.exists() or sp.is_symlink():
            sp.unlink()
        shutil.copy2(fp, sp)
        print(f"✅ 同步短文件：{short}")

print("\n✨ Be A Pro Football 版全部修复完成！")
