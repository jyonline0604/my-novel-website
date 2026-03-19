#!/usr/bin/env python3
"""修复开天版所有问题"""

from pathlib import Path
import shutil
import re

REPO = Path("/home/openclaw/.openclaw/workspace/my-novel-website")
theme = {"primary": "#9b59b6", "bg": "#1a0a2e"}

# ============= 1. 定义开天正确的详细页 =============
correct_guides = {
    "cultivation-guide.html": "灵气修炼与渡劫",
    "spirit-beast-guide.html": "灵兽捕捉与培养",
    "artifact-forging-guide.html": "法宝炼器系统",
    "sect-mission-guide.html": "宗门任务攻略",
    "alchemy-guide.html": "炼丹系统详解",
    "realm-progression-guide.html": "境界提升路线",
}

# 删除所有错误的残留文件（问剑内容的）
wrong_files = [
    "sword.html", "sword-cultivation-guide.html",
    "pet.html", "pet-nurturing-guide.html",
    "resource.html", "resource-management-guide.html",
    "boss.html", "boss-battle-guide.html",
    "ascend.html", "ascension-guide.html",
    "craft.html", "crafting-system-guide.html",
]
for wf in wrong_files:
    fp = REPO / "guides/kai_tian" / wf
    if fp.exists():
        fp.unlink()
        print(f"🗑️ 删除残留文件：{wf}")

# ============= 2. 创建三个资讯页 =============
pages = {
    "news-updates-guide.html": {
        "title": "最新版本更新",
        "content": """<h1>📢 最新版本更新</h1>
        <p>開天官方更新公告、平衡调整、新增内容聚合。</p>
        <h2>📅 近期更新记录</h2>
        <table border="1" cellpadding="8">
            <tr><th>日期</th><th>版本</th><th>主要内容</th></tr>
            <tr><td>2026-03-14</td><td>v2.5.1</td><td>新增化神大境界、优化渡劫动画</td></tr>
            <tr><td>2026-02-28</td><td>v2.5.0</td><td>开放跨服宗门战、灵兽进阶第5阶段</td></tr>
            <tr><td>2026-02-10</td><td>v2.4.5</td><td>平衡调整：剑修削弱、法术增强</td></tr>
        </table>
        <h2>⚖️ 平衡调整详情</h2>
        <ul>
            <li><strong>剑修</strong>：裂地斩基础伤害降低 10%</li>
            <li><strong>法术</strong>：寒冰斩冰冻时间延长 1 秒</li>
            <li><strong>炼器</strong>：橙色装备成功率提升至 35%</li>
            <li><strong>渡劫</strong>：第7-9波天雷伤害降低 15%</li>
        </ul>
        <h2>🔮 即将到来</h2>
        <p><strong>v2.6.0 预计 4 月中旬</strong></p>
        <ul>
            <li>新增「九幽深渊」副本</li>
            <li>灵兽幻化系统</li>
            <li>法宝 fusion 系统</li>
            <li>宗门联盟战</li>
        </ul>"""
    },
    "events-guide.html": {
        "title": "活动攻略",
        "content": """<h1>🎉 活动攻略</h1>
        <p>開天各类限时活动的最佳参与策略与奖励最大化。</p>
        <h2>📆 活动日历</h2>
        <table border="1" cellpadding="8">
            <tr><th>活动名称</th><th>周期</th><th>核心奖励</th><th>推荐度</th></tr>
            <tr><td>灵气爆发</td><td>每日 12:00-14:00</td><td>灵气收益×3</td><td>⭐⭐⭐⭐⭐</td></tr>
            <tr><td>渡劫大典</td><td>每周日 20:00-22:00</td><td>渡劫丹×10, 灵石×5000</td><td>⭐⭐⭐⭐⭐</td></tr>
            <tr><td>神兽降临</td><td>每月1、15日 20:00</td><td>稀有灵兽蛋, 进阶丹</td><td>⭐⭐⭐⭐</td></tr>
            <tr><td>炼器狂欢</td><td>每周六、日全天</td><td>成功率+20%</td><td>⭐⭐⭐⭐</td></tr>
            <tr><td>双倍灵石</td><td>每日 18:00-19:00</td><td>掉落×3</td><td>⭐⭐⭐</td></tr>
        </table>
        <h2>⭐ 必刷活动排行</h2>
        <ol>
            <li><strong>灵气爆发</strong> - 渡劫资源，必须参加</li>
            <li><strong>渡劫大典</strong> - 渡劫丹唯一稳定来源</li>
            <li><strong>神兽降临</td><li><strong>炼器狂欢</strong> - 炼极品装备最佳时机</li>
        </ol>
        <h2>💡 活动技巧</h2>
        <ul>
            <li><strong>提前准备</strong>：渡劫大典前清空背包</li>
            <li><strong>双倍叠加</strong>：灵气爆发时使用双倍符，收益×6</li>
            <li><strong>组队加成</strong>：神兽降临组满5人，掉落+30%</li>
            <li><strong>错峰参与</strong>：错过灵气爆发有补场机会</li>
        </ul>"""
    },
    "community-guide.html": {
        "title": "社区热点",
        "content": """<h1>🔥 社区热点</h1>
        <p>開天玩家社区本周最热话题、组队招募、交易动态。</p>
        <h2>📊 本周热议 TOP 5</h2>
        <ol>
            <li><strong>【争议】剑修是否被削弱？</strong><br>
                热度：⭐⭐⭐⭐⭐<br>
                讨论：版本更新后剑修胜率下降 8%<br>
                <em>（官方：正在监测，4月调整）</em></li>
            <li><strong>【攻略】筑基→金丹最快路径</strong><br>
                热度：⭐⭐⭐⭐⭐<br>
                作者：@老司机<br>
                内容：skip主线，专刷灵气窟，3天升金丹</li>
            <li><strong>【求助】玄武刷新点确认</strong><br>
                热度：⭐⭐⭐⭐<br>
                问题：北境冰川 20:00 是否准时？</li>
            <li><strong>【数据】渡劫成功率实测</strong><br>
                热度：⭐⭐⭐⭐<br>
                数据：1000次样本，平均成功率 42%</li>
            <li><strong>【晒图】终于抽出传说灵兽！</strong><br>
                热度：⭐⭐⭐⭐<br>
                内容：玄武资质 1973 满资质！</li>
        </ol>
        <h2>👥 热门组队</h2>
        <table border="1" cellpadding="8">
            <tr><th>职业</th><th>等级</th><th>需求</th><th>备注</th></tr>
            <tr><td>剑修×2</td><td>120+</td><td>渡劫带队</td><td>需雷抗装备</td></tr>
            <tr><td>法术×1</td><td>115+</td><td>刷灵气窟</td><td>20:00-22:00</td></tr>
            <tr><td>奶妈×2</td><td>110+</td><td>宗门任务</td><td>缺奶速来</td></tr>
        </table>
        <h2>🏪 交易市场</h2>
        <ul>
            <li><strong>渡劫丹</strong>：市价 500-800 灵石/个</li>
            <li><strong>玄武蛋</strong>：拍卖行 50万灵石</li>
            <li><strong>橙色炼器锤</strong>：材料跌 30%</li>
        </ul>
        <h2>🔗 社区入口</h2>
        <ul>
            <li>TapTap 论坛（最活跃）</li>
            <li>Discord（实时语音）</li>
            <li>NGA 开天版（数据党）</li>
            <li>贴吧（新手提问）</li>
        </ul>"""
    }
}

# 标准样式模板
STYLE_TEMPLATE = '''<!DOCTYPE html>
<html lang="zh-Hant">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - 開天 | 科技修真傳</title>
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
    <a href="/kai-tian-guide.html" class="back-link"><i class="fas fa-arrow-left"></i> 返回攻略中心</a>
    <div class="guide-content">
        {content}
        <p style="margin-top:2rem; color:#888; font-size:0.9rem;">最后更新：2026-03-18 | 来源：官方/社区</p>
    </div>
</body></html>'''

# ============= 3. 创建资讯页 =============
for file_name, data in pages.items():
    fp = REPO / f"guides/kai_tian/{file_name}"
    if not fp.exists():
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
    src = REPO / f"guides/kai_tian/{stem}-guide.html"
    dst = REPO / f"guides/kai_tian/{stem}.html"
    if src.exists():
        if dst.exists() or dst.is_symlink():
            dst.unlink()
        shutil.copy2(src, dst)
        print(f"✅ 同步：{stem}.html")

# ============= 4. 统一现有详细页样式 + 修复返回链接 =============
for guide_file in correct_guides.keys():
    fp = REPO / f"guides/kai_tian/{guide_file}"
    if not fp.exists():
        print(f"❌ 缺失：{guide_file}")
        continue
    
    html = fp.read_text(encoding='utf-8')
    
    # 提取标题和内容
    title_match = re.search(r'<h1>([^<]+)</h1>', html)
    title = title_match.group(1) if title_match else correct_guides[guide_file]
    
    # 提取 body 内容
    body_match = re.search(r'<div class="guide-content">(.+?)</div>\s*</body>', html, re.DOTALL)
    if body_match:
        content = body_match.group(1).strip()
    else:
        # 后备：提取整个 body
        content = re.search(r'<div class="guide-content">(.+?)</div>', html, re.DOTALL)
        content = content.group(1).strip() if content else ""
    
    # 应用统一样式（包含正确的返回链接）
    new_html = STYLE_TEMPLATE.format(
        title=title,
        primary=theme["primary"],
        bg=theme["bg"],
        content=content
    )
    
    fp.write_text(new_html, encoding='utf-8')
    print(f"✅ 修复样式和链接：{guide_file}")

# ============= 5. 同步正确的短文件名 =============
correct_short_map = {
    "cultivation.html": "cultivation-guide.html",
    "spirit.html": "spirit-beast-guide.html",
    "artifact.html": "artifact-forging-guide.html",
    "sect.html": "sect-mission-guide.html",
    "alchemy.html": "alchemy-guide.html",
    "realm.html": "realm-progressguidelder.html",  # typo in original?
    "news-updates.html": "news-updates-guide.html",
    "events.html": "events-guide.html",
    "community.html": "community-guide.html",
}

# 修正：正确的文件应该是 realm-progression-guide.html
correct_short_map = {
    "cultivation.html": "cultivation-guide.html",
    "spirit.html": "spirit-beast-guide.html",
    "artifact.html": "artifact-forging-guide.html",
    "sect.html": "sect-mission-guide.html",
    "alchemy.html": "alchemy-guide.html",
    "realm.html": "realm-progression-guide.html",
    "news-updates.html": "news-updates-guide.html",
    "events.html": "events-guide.html",
    "community.html": "community-guide.html",
}

for short, full in correct_short_map.items():
    sp = REPO / f"guides/kai_tian/{short}"
    fp = REPO / f"guides/kai_tian/{full}"
    if fp.exists():
        if sp.exists() or sp.is_symlink():
            sp.unlink()
        shutil.copy2(fp, sp)
        print(f"✅ 同步短文件：{short}")
    else:
        print(f"⚠️ 源文件缺失：{full}")

print("\n✨ 開天版全部修复完成！")
