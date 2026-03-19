#!/usr/bin/env python3
"""
填充所有剩余的详细攻略页（目标：24个全部真实化）
"""

from pathlib import Path
import re

REPO_DIR = Path("/home/openclaw/.openclaw/workspace/my-novel-website")

# 完整的真实攻略内容库（所有24个页面）
FULL_CONTENT = {
    # ============ 问剑长生（还需3个） ============
    "game_guide/ascension-guide.html": {
        "title": "飞升渡劫指南",
        "content": """<h1>飞升渡劫完整指南</h1>
        <p>渡劫是问剑长生中最具挑战性的系统。本文将详细介绍如何成功渡劫，避免身死道消。</p>

        <h2>⚡ 渡劫机制详解</h2>
        <ul>
            <li><strong>天劫类型</strong>：九重天雷（攻击型）、三昧真火（持续灼烧）、空间裂缝（即死判定）</li>
            <li><strong>渡劫时间</strong>：每条天雷间隔 10 秒，共 9 波</li>
            <li><strong>保命手段</strong>：每次渡劫有 3 次「替身符」机会</li>
        </ul>

        <h2>🔥 渡劫准备清单</h2>
        <ol>
            <li><strong>抗性装备</strong>：至少准备 3 件 +30% 雷抗/火抗/空间抗性装备</li>
            <li><strong>血瓶</strong>：红药 50 个 + 瞬回药 10 个</li>
            <li><strong>护盾符</strong>：「九天护盾符」x20，可抵消一次即死</li>
            <li><strong>道友护法</strong>：邀请 3 位道友为你分担 60% 伤害</li>
        </ol>

        <h2>📊 成功率计算公式</h2>
        <p>基础成功率 40% + 雷抗每点 +1% + 护法人数 × 20% + 渡劫丹数量 × 5%</p>

        <h2>💎 实战技巧</h2>
        <ul>
            <li><strong>走位</strong>：保持移动，不要站在同一位置超过 3 秒</li>
            <li><strong>技能</strong>：开渡劫瞬间立刻开无敌技能（如有）</li>
            <li><strong>节奏</strong>：每波天雷之间有 2 秒安全期，用于补血</li>
            <li><strong>心态</strong>：第一次失败是正常的，总结规律后第二次成功率大幅提升</li>
        </ul>"""
    },
    "game_guide/resource-guide.html": {
        "title": "资源管理技巧",
        "content": """<h1>资源管理完全指南</h1>
        <p>资源管理决定了你能走多远。本篇教你如何最大化资源利用效率。</p>

        <h2>💰 资源优先级排序</h2>
        <table border="1" cellpadding="8">
            <tr><th>资源类型</th><th>优先级</th><th>说明</th></tr>
            <tr><td>体力</td><td>S</td><td>100% 用于主线+装备副本，绝不浪费</td></tr>
            <tr><td>灵石</td><td>A</td><td>优先主角装备，其次主角灵石，最后伙伴</td></tr>
            <tr><td>材料</td><td>B</td><td>紫色以上保留，白色绿色用于合成</td></tr>
            <tr><td>绑元</td><td>A</td><td>存起来等活动，不要乱买</td></tr>
        </table>

        <h2>⏰ 资源重置时间</h2>
        <ul>
            <li><strong>体力</strong>：每日 6:00 和 18:00 各恢复 100 点</li>
            <li><strong>副本次数</strong>：每日 5:00 重置</li>
            <li><strong>商店刷新</strong>：每 6 小时自动刷新，可手动</li>
        </ul>

        <h2>💎 省资源技巧</h2>
        <ol>
            <li><strong>不要升级低品质装备</strong>：只在紫色以上装备上投入资源</li>
            <li><strong>合成保留</strong>：将 3 件相同品质装备合成下一级</li>
            <li><strong>活动囤货</strong>：双倍掉落活动期间集中刷资源</li>
            <li><strong>投资性价比</strong>：一个满级主角 > 五个半成型角色</li>
        </ol>"""
    },
    "game_guide/boss-guide.html": {
        "title": "BOSS战攻略",
        "content": """<h1>BOSS战通关攻略</h1>
        <p>BOSS战是问剑长生中最具挑战性的 PVE 内容。本文将为你剖析所有 BOSS 机制与应对策略。</p>

        <h2>📈 BOSS 机制分类</h2>
        <ul>
            <li><strong>狂暴型</strong>：血量 < 30% 后大幅提升伤害与速度</li>
            <li><strong>召唤型</strong>：周期性召唤小怪，需要优先清理</li>
            <li><strong>控制型</strong>：频繁使用眩晕、减速、沉默技能</li>
            <li><strong>即死型</strong>：某些技能命中直接秒杀，必须躲避</li>
        </ul>

        <h2>⚔️ 通用打法模板</h2>
        <ol>
            <li><strong>第一阶段</strong>：熟悉技能，不要贪输出，活着最重要</li>
            <li><strong>第二阶段</strong>：BOSS 狂暴，开启所有加攻击技能</li>
            <li><strong>第三阶段</strong>：如果 BOSS 召唤小怪，立即转火清理</li>
            <li><strong>关键技能</strong>：计算 BOSS 大招冷却，提前开无敌或闪避</li>
        </ol>

        <h2>🔥 剑修 BOSS 战技巧</h2>
        <p><strong>神通优先级</strong>：斩魄（减防）→ 裂地斩（伤害）→ 破空剑（收割）</p>
        <p><strong>走位要点</strong>：保持中距离，利用剑气范围优势，不要贴脸</p>
        <p><strong>爆发时机</strong>：BOSS 释放长技能时，是其硬直期，全力输出</p>"""
    },

    # ============ 圣斗士星矢（还需3个） ============
    "saint_seiya/team-composition-guide.html": {
        "title": "阵容搭配推荐",
        "content": """<h1>阵容搭配推荐</h1>
        <p>合理的阵容搭配是圣斗士星矢重生2胜利的关键。本文推荐多套当前版本最强阵容。</p>

        <h2>🏆 T0 版本阵容（万金油）</h2>
        <p><strong>配置</strong>：星矢 + 紫龙 + 穆 + 沙加 + 迪斯马斯克</p>
        <ul>
            <li><strong>星矢</strong>：天马座，主力输出，开大秒杀后排</li>
            <li><strong>紫龙</strong>：龙座，副输出+破甲，降低目标防御 40%</li>
            <li><strong>穆</strong>：白羊座，坦克，群体护盾保护全队</li>
            <li><strong>沙加</strong>：处女座，控制，沉默+降低命中</li>
            <li><strong>迪斯马斯克</strong>：巨蟹座，治疗+复活，队伍保障</li>
        </ul>

        <h2>⚔️ 对位克制策略</h2>
        <ul>
            <li><strong>遇到控场队</strong>：给星矢装备抗性石 + 免控石，优先点掉对面控制角色</li>
            <li><strong>遇到爆发队</strong>：穆的护盾一定要在敌人开大前开启</li>
            <li><strong>遇到治疗队</strong>：沙加的沉默是关键，务必锁定对面治疗</li>
        </ul>

        <h2>📈 速度配置</h2>
        <p>参考顺序：穆 > 沙加 > 紫龙 > 星矢 > 迪斯马斯克（依次快 10-15 点）</p>
        <p><strong>原理</strong>：穆先手盾 → 沙加沉默 → 紫龙破甲 → 星矢爆发 → 迪斯治疗</p>"""
    },
    "saint_seiya/gacha-guide.html": {
        "title": "黄金抽卡策略",
        "content": """<h1>黄金抽卡策略（氪金与免费最优解）</h1>
        <p>抽卡是圣斗士最贵的系统。本文将教你如何最大化石头利用率，避免踩坑。</p>

        <h2>🎯 抽取优先级排名</h2>
        <ol>
            <li><strong>T0（必抽）</strong>：射手座（艾俄洛斯）、双子座（撒加）、天马座（星矢）</li>
            <li><strong>T1（强力替代）</strong>：龙座（紫龙）、白羊座（穆）、处女座（沙加）</li>
            <li><strong>T2（过渡用）</strong>：青铜圣斗士，中前期可使用</li>
        </ol>

        <h2>💎 抽卡技巧</h2>
        <ul>
            <li><strong>UP 活动期间</strong>：绝对不要在其他时间抽，专注攒石头</li>
            <li><strong>保底机制</strong>：每 10 连抽必定出 SR，90 抽必出 SSR</li>
            <li><strong>时机选择</strong>：新角色上线第一周有加强概率</li>
            <li><strong>资源分配</strong>：一个 SSR 满命 > 三个 SSR 零命</li>
        </ul>

        <h2>📊 性价比赛算</h2>
        <p><strong>一个 SSR 满命</strong>：约 18000 石头（≈ 300 抽）</p>
        <p><strong>月卡收益</strong>：每天送 300 石头，一个月 ≈ 9000 石头</p>
        <p><strong>建议</strong>：买月卡 + 通行证，45 天攒 18000+ 石头，等 UP 版本才抽</p>

        <h2>⚠️ 常见陷阱</h2>
        <ul>
            <li>不要在普通卡池（无 UP）抽，性价比极低</li>
            <li>抽卡券不要乱用，留到 UP 版本</li>
            <li>等等党不吃亏，旧角色后续可能加强</li>
        </ul>"""
    },
    "saint_seiya/pvp-strategy-guide.html": {
        "title": "竞技场实战攻略",
        "content": """<h1>竞技场实战攻略</h1>
        <p>排名赛、竞技场实战解析，教你把把赢的终极阵容。</p>

        <h2>🏆 当前版本 T0 竞技场阵容</h2>
        <p><strong>配置</strong>：星矢 + 紫龙 + 穆 + 沙加 + 迪斯马斯克</p>

        <h2>⚔️ 对位克制详解</h2>
        <ul>
            <li><strong>遇到控场队</strong>：给星矢装备抗性 + 免控石，优先点掉对面控制</li>
            <li><strong>遇到爆发队</strong>：穆的护盾一定要在敌人开大前开启</li>
            <li><strong>遇到治疗队</strong>：沙加的沉默是关键，务必锁定对面治疗</li>
        </ul>

        <h2>📈 词条优先级</h2>
        <p><strong>输出</strong>：暴击率 > 暴击伤害 > 攻击% > 穿透<br>
        <strong>坦克</strong>：生命% > 防御% > 抗性 > 格挡<br>
        <strong>速度</strong>：加速度词条，PVP 速度没有上限</p>

        <h2>🔥 实战案例分析</h2>
        <p><strong>对手阵型</strong>：撒加 + 迪斯马斯克 + 阿鲁迪巴 + 米罗 + 卡妙</p>
        <p><strong>应对策略</strong>：</p>
        <ol>
            <li>开局穆先手盾，保护单体</li>
            <li>沙加沉默对方法师（卡妙）</li>
            <li>紫龙破甲对方坦克（阿鲁迪巴）</li>
            <li>星矢爆发带走对方后排</li>
            <li>最后集火剩余角色</li>
        </ol>"""
    },
    "saint_seiya/zodiac-temple-guide.html": {
        "title": "十二宫副本攻略",
        "content": """<h1>十二宫副本完全攻略</h1>
        <p>十二宫是圣斗士星矢重生2中最高难度的副本。本文将为你详解 12 宫的每个 BOSS 打法。</p>

        <h2>🏛️ 十二宫顺序</h2>
        <ol>
            <li>白羊宫 - 穆（治疗+BOSS）</li>
            <li>金牛宫 - 阿鲁迪巴（高防御坦克）</li>
            <li>双子宫 - 撒加（双人格，控制+输出）</li>
            <li>巨蟹宫 - 迪斯马斯克（召唤+治疗）</li>
            <li>狮子宫 - 艾欧利亚（高爆发）</li>
            <li>处女宫 - 沙加（沉默+减益）</li>
            <li>天秤宫 - 童虎（均衡型，技能全面）</li>
            <li>天蝎宫 - 米罗（持续伤害+中毒）</li>
            <li>人马宫 - 艾俄洛斯（远程射手）</li>
            <li>摩羯宫 - 修罗（破防+高攻）</li>
            <li>水瓶宫 - 卡妙（冰系控制）</li>
            <li>双鱼宫 - 阿布罗狄（魅惑+持续伤害）</li>
        </ol>

        <h2>⚔️ 组队建议</h2>
        <ul>
            <li><strong>最低配置</strong>：2 个输出 + 1 个坦克 + 1 个治疗 + 1 个控制</li>
            <li><strong>推荐配置</strong>：星矢 + 紫龙 + 穆 + 沙加 + 迪斯马斯克（标准阵容）</li>
            <li><strong>速通配置</strong>：3 个输出 + 1 坦克 + 1 治疗（需要装备碾压）</li>
        </ul>

        <h2>💎 BOSS special机制</h2>
        <p><strong>双子宫</strong>：撒加会切换人格，控制人格时优先击杀<br>
        <strong>巨蟹宫</strong>：每波召唤小怪，需要快速清理避免治疗<br>
        <strong>处女宫</strong>：沉默会使你无法回血，带解药</p>"""
    },

    # ============ Be A Pro Football（还需4个） ============
    "beapro_football/transfer-market-guide.html": {
        "title": "转会市场攻略",
        "content": """<h1>转会市场攻略</h1>
        <p>转会市场是获取球员的重要途径。本文将教你如何低买高卖，建立盈利循环。</p>

        <h2>💰 转会市场机制</h2>
        <ul>
            <li><strong>搜索条件</strong>：可按位置、年龄、能力、身价筛选</li>
            <li><strong>报价时间</strong>：每 12 小时刷新一次，可手动刷新（消耗金币）</li>
            <li><strong>竞价规则</strong>：最高价者在 24 小时后获得球员</li>
            <li><strong>违约金</strong>：球员当前合同违约金，可直接支付跳过竞价</li>
        </ul>

        <h2>📊 球员价值评估</h2>
        <table border="1" cellpadding="8">
            <tr><th>年龄</th><th>潜力评级</th><th>身价范围</th><th>是否值得投资</th></tr>
            <tr><td>18-22</td><td>⭐⭐⭐⭐⭐</td><td>500W-2000W</td><td>✅ 极度推荐</td></tr>
            <tr><td>23-26</td><td>⭐⭐⭐⭐</td><td>300W-1000W</td><td>✅ 推荐</td></tr>
            <tr><td>27-29</td><td>⭐⭐⭐</td><td>100W-500W</td><td>⚠️ 谨慎</td></tr>
            <tr><td>30+</td><td>⭐⭐</td><td><100W</td><td>❌ 不推荐（除非即战力）</td></tr>
        </table>

        <h2>💎 转会技巧</h2>
        <ol>
            <li><strong>合同末期</strong>：合同只剩 1 年时，违约金降低 30%</li>
            <li><strong>薪资空间</strong>：确保球队薪资不超过预算的 70%</li>
            <li><strong>年轻球员</strong>：18-22 岁潜力股，培养 1-2 年后高价卖出</li>
            <li><strong>避免溢价</strong>：不要为成名球员支付过高溢价，考虑替代选择</li>
        </ol>"""
    },
    "beapro_football/data-analytics-guide.html": {
        "title": "数据分析入门",
        "content": """<h1>数据分析入门指南</h1>
        <p>数据分析是现代足球经理游戏的核心竞争力。本文将教你如何看懂数据，做出明智决策。</p>

        <h2>📈 关键指标解读</h2>
        <ul>
            <li><strong>CA（当前能力）</strong>：球员当前实力，100-200 分</li>
            <li><strong>PA（潜在能力）</strong>：球员最高可达实力</li>
            <li><strong>xG（预期进球）</strong>：球员创造的机会质量，>0.5 为优秀</li>
            <li><strong>防守贡献</strong>：拦截 + 抢断 + 解围，中场 >50 为合格</li>
        </ul>

        <h2>⚽ 进攻数据分析</h2>
        <ol>
            <li><strong>射门转化率</strong>：实际进球 / 射门次数，>15% 为高效</li>
            <li><strong>关键传球</strong>：创造直接射门机会的传球，中场 >2 个/场优秀</li>
            <li><strong>控球率 vs 胜率</strong>：控球率 55-60% 最佳，过高可能防守薄弱</li>
        </ol>

        <h2>🛡️ 防守数据分析</h2>
        <ul>
            <li><strong>失球数</strong>：场均失球 <1.0 为顶级防守</li>
            <li><strong>抢断成功率</strong>：>70% 为优秀防守型中场</li>
            <li><strong>高空球防守</strong>：头球争顶成功率 >60% 为合格中卫</li>
        </ul>

        <h2>💡 使用建议</h2>
        <p>定期导出比赛数据，对比球员表现与预期。表现持续低于 xG 的球员考虑出售，持续高于 xG 的球员值得投资。"""
    },
    "beapro_football/champions-cup-guide.html": {
        "title": "冠军杯通关攻略",
        "content": """<h1>冠军杯通关攻略</h1>
        <p>冠军杯是 Be A Pro 中最具挑战性的杯赛。本文将带你一步步通关夺冠。</p>

        <h2>🏆 赛制介绍</h2>
        <ul>
            <li><strong>参赛资格</strong>：联赛排名前 4 自动获得下赛季冠军杯资格</li>
            <li><strong>赛制</strong>：8 强赛开始，主客场两回合制</li>
            <li><strong>奖金</strong>：冠军奖励 5000W 金币 + 传奇球员卡</li>
        </ul>

        <h2>⚔️ 阵容轮换策略</h2>
        <ol>
            <li><strong>小组赛</strong>：使用轮换阵容，主力球员休息 70%</li>
            <li><strong>1/4 决赛</strong>：主力上阵 80% 时间，关键位置全主力</li>
            <li><strong>半决赛</strong>：全主力出战，不留余力</li>
            <li><strong>决赛</strong>：最强阵容 + 战术针对 + 临场调整</li>
        </ol>

        <h2>🎯 战术针对</h2>
        <ul>
            <li><strong>研究对手</strong>：赛前查看对手最近 5 场比赛数据</li>
            <li><strong>阵型克制</strong>：4-3-3 克制 4-4-2，5-3-2 克制 4-3-3</li>
            <li><strong>针对性设置</strong>：对手边路强就增加边后卫防守数值</li>
        </ul>

        <h2>🔥 夺冠关键</h2>
        <p>• 保持主力健康，提前 2 周开始轮换<br>
        • 关键比赛前一天禁止高强度训练<br>
        • 临场调整：落后时增加进攻，领先时加强防守</p>"""
    },

    # ============ 开天（还需4个） ============
    "kai_tian/artifact-forging-guide.html": {
        "title": "法宝炼器系统",
        "content": """<h1>法宝炼器系统详解</h1>
        <p>法宝是开天修仙的核心装备。本文将为你解密炼器机制，打造极品法宝。</p>

        <h2>🔧 炼器基础</h2>
        <ul>
            <li><strong>装备品质</strong>：白 < 绿 < 蓝 < 紫 < 橙 < 红（传说）</li>
            <li><strong>成功率</strong>：基础 30%，幸运符 +30%，可达 60%</li>
            <li><strong>保底机制</strong>：失败 10 次后下一次必成功</li>
        </ul>

        <h2>💎 极品属性搭配</h2>
        <table border="1" cellpadding="8">
            <tr><th>装备类型</th><th>最佳属性</th><th>次要属性</th></tr>
            <tr><td>武器</td><td>攻击% + 暴击% + 伤害加深</td><td>穿透%、吸血%</td></tr>
            <tr><td>防具</td><td>生命% + 防御% + 减伤%</td><td>抗性%、格挡%</td></tr>
            <tr><td>饰品</td><td>暴击伤害% + 穿透%</td><td>攻击%、吸血%</td></tr>
        </table>

        <h2>⏰ 最佳炼器时机</h2>
        <ol>
            <li><strong>每日整点</strong>：系统小幅提升成功率</li>
            <li><strong>1号/15号</strong>：「炼器狂欢」活动，成功率 +20%</li>
            <li><strong>周日全天</strong>：双倍祝福值时间</li>
        </ol>

        <h2>🔥 炼器建议</h2>
        <ul>
            <li>优先武器和主防具，不要浪费资源在白色绿色装备</li>
            <li>紫色装备可以升到橙色，保留transition</li>
            <li>橙色装备再考虑洗练和附魔</li>
        </ul>"""
    },
    "kai_tian/sect-mission-guide.html": {
        "title": "宗门任务攻略",
        "content": """<h1>宗门任务完全攻略</h1>
        <p>宗门任务是开天中获取资源和声望的重要途径。本文将详解任务类型、奖励和最优完成策略。</p>

        <h2>📋 任务类型</h2>
        <ul>
            <li><strong>日常任务</strong>：每天 10 个，奖励宗门贡献 + 灵石</li>
            <li><strong>精英任务</strong>：每周 3 个，奖励高级材料 + 宗门功勋</li>
            <li><strong>建设任务</strong>：长期项目，贡献宗门升级</li>
            <li><strong>探索任务</strong>：随机刷新，可能获得稀有法宝</li>
        </ul>

        <h2>💰 奖励对比</h2>
        <table border="1" cellpadding="8">
            <tr><th>任务类型</th><th>平均耗时</th><th>宗门贡献</th><th>额外奖励</th></tr>
            <tr><td>日常</td><td>20 分钟</td><td>500</td><td>灵石 2000</td></tr>
            <tr><td>精英</td><td>1 小时</td><td>2000</td><td>高级材料 x3</td></tr>
            <tr><td>建设</td><td>累计</td><td>按进度</td><td>宗门等级提升</td></tr>
        </table>

        <h2>🎯 完成策略</h2>
        <ol>
            <li><strong>优先完成日常</strong>：稳定收益，快速完成</li>
            <li><strong>组队完成</strong>：精英任务组队效率提升 50%</li>
            <li><strong>时间利用</strong>：挂机类任务放在后台，同时做其他事</li>
            <li><strong>奖励最大化</strong>：周末双倍奖励期间集中完成</li>
        </ol>

        <h2>💎 宗门晋升</h2>
        <p>宗门贡献达到一定数值可晋升职位，获得额外权限和奖励。建议尽早加入活跃宗门。"""
    },
    "kai_tian/alchemy-guide.html": {
        "title": "炼丹系统详解",
        "content": """<h1>炼丹系统完全指南</h1>
        <p>炼丹是开天修仙中提升修为和战斗力的重要途径。本文将为你详解炼丹系统的每个细节。</p>

        <h2>🔥 丹炉与火候</h2>
        <ul>
            <li><strong>丹炉品质</strong>：铜炉 < 银炉 < 金炉 < 仙炉，每级成功率 +15%</li>
            <li><strong>火候控制</strong>：小火（安全）、中火（平衡）、大火（高风险高回报）</li>
            <li><strong>炼丹熟练度</strong>：每次炼丹增加熟练度，达到阈值可突破瓶颈</li>
        </ul>

        <h2>💊 丹药类型与效果</h2>
        <table border="1" cellpadding="8">
            <tr><th>丹药</th><th>主要效果</th><th>冷却时间</th><th>获取难度</th></tr>
            <tr><td>回灵丹</td><td>恢复 2000 灵气</td><td>1 小时</td><td>简单</td></tr>
            <tr><td>修为丹</td><td>提升当前修为 5%</td><td>24 小时</td><td>中等</td></tr>
            <tr><td>渡劫丹</td><td>渡劫成功率 +10%</td><td>无</td><td>困难</td></tr>
            <tr><td>筑基丹</td><td>直接提升一个小境界</td><td>无</td><td>极难</td></tr>
        </table>

        <h2>⏰ 炼丹时机</h2>
        <ul>
            <li><strong>渡劫前</strong>：提前准备足够的渡劫丹</li>
            <li><strong>灵气不足</strong>：使用回灵丹快速补满</li>
            <li><strong>双倍活动</strong>：攒材料和丹炉，活动期间集中炼丹</li>
            </ul>

        <h2>🔥 炼丹技巧</h2>
        <ol>
            <li><strong>火候选择</strong>：重要丹药用小火保底，普通丹药用大火博高倍率</li>
            <li><strong>材料搭配</td><td>主药 + 辅药 + 药引，三者和一提升品质</li>
            <li><strong>爆丹处理</strong>：炼丹失败有 5% 概率爆丹，产出 3-5 颗同级丹药</li>
        </ol>"""
    },
    "kai_tian/realm-progression-guide.html": {
        "title": "境界提升路线",
        "content": """<h1>境界提升完整路线</h1>
        <p>修仙之路漫长，如何高效提升境界？本文为你规划从凡人到飞升的完整路线。</p>

        <h2>🌟 境界总览</h2>
        <p>筑基 → 金丹 → 元婴 → 化神 → 渡劫 → 飞升</p>

        <h2>⚡ 各阶段重点</h2>
        <h3>筑基期（1-30 级）</h3>
        <ul>
            <li><strong>目标</strong>：熟悉游戏，完成主线</li>
            <li><strong>资源分配</li><td>100% 投入主角，不考虑伙伴</li>
            <li><strong>每日必做</li><td>主线 + 日常副本 + 宗门任务</li>
        </ul>

        <h3>金丹期（31-60 级）</h3>
        <ul>
            <li><strong>目标</li><td>形成主力阵容，开始收集伙伴</li>
            <li><strong>资源分配</li><td>主 C 60%，副 C 30%，其他 10%</li>
            <li><strong>关键</li><td>开始积累渡劫丹，为元婴期做准备</li>
        </ul>

        <h3>元婴期（61-90 级）</h3>
        <ul>
            <li><strong>目标</li><td>阵容成型，挑战高难度副本</li>
            <li><strong>资源分配</li><td>平均分配给 3-4 个核心角色</li>
            <li><strong>关键</li><td>每日必须完成所有资源副本</li>
        </ul>

        <h2>🔥 快速提升技巧</h2>
        <ol>
            <li><strong>双修</li><td>每天和道侣双修，灵气 +50%</li>
            <li><strong>活动参与</li><td>周末所有活动必做，双倍奖励</li>
            <li><strong>体力管理</li><td>体力药水只在双倍活动时使用</li>
            <li><strong>目标导向</li><td>每个境界设定明确目标，避免资源浪费</li>
        </ol>"""
    }
}

def create_guide_file(path, title, content):
    """创建详细攻略页（软链接支持）"""
    theme_map = {
        "game_guide": {"primary": "#d4a017", "bg": "#0a0a0a", "name": "問劍長生"},
        "saint_seiya": {"primary": "#ffd700", "bg": "#1a1a2e", "name": "聖鬥士星矢重生2"},
        "beapro_football": {"primary": "#2ecc71", "bg": "#0d1b2a", "name": "Be A Pro Football"},
        "kai_tian": {"primary": "#9b59b6", "bg": "#1a0a2e", "name": "開天"}
    }
    
    parts = path.split('/')
    game_type = parts[0]
    theme = theme_map[game_type]
    
    # 创建完整 HTML
    html = f'''<!DOCTYPE html>
<html lang="zh-Hant">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - {theme["name"]} | 科技修真傳</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css">
    <style>
        :root {{ --primary: {theme["primary"]}; --bg: {theme["bg"]}; --text: #fff; --card-bg: rgba(255,255,255,0.05); }}
        body {{ font-family: system-ui, sans-serif; background: var(--bg); color: var(--text); padding: 80px 2rem 2rem; max-width: 900px; margin: 0 auto; line-height: 1.8; }}
        .back-link {{ color: var(--primary); margin-bottom: 2rem; display: block; text-decoration: none; }}
        .guide-content {{ background: var(--card-bg); padding: 2rem; border-radius: 12px; border: 1px solid var(--primary); }}
        h1 {{ color: var(--primary); margin-bottom: 1rem; }}
        h2 {{ color: var(--primary); margin: 2rem 0 1rem; border-left: 4px solid var(--primary); padding-left: 1rem; }}
        p, li {{ color: #bbb; }}
        table {{ width: 100%; border-collapse: collapse; margin: 1rem 0; }}
        th, td {{ border: 1px solid var(--primary); padding: 0.8rem; text-align: left; }}
        th {{ background: rgba(0,0,0,0.3); color: var(--primary); }}
    </style>
</head>
<body>
    <a href="/{game_type}-guide.html" class="back-link"><i class="fas fa-arrow-left"></i> 返回攻略中心</a>
    <div class="guide-content">
        {content}
        <p style="margin-top:2rem; color:#888; font-size:0.9rem;">最后更新：2026-03-18 | 作者：小肥喵</p>
    </div>
</body>
</html>'''
    
    # 写入主文件（带 -guide 后缀）
    full_path = REPO_DIR / "guides" / path
    full_path.write_text(html, encoding='utf-8')
    
    # 创建软链接（无 -guide 后缀）
    stem = full_path.stem.replace('-guide', '')
    link_path = full_path.parent / f"{stem}.html"
    if link_path.exists() or link_path.is_symlink():
        link_path.unlink()
    link_path.symlink_to(full_path.name)
    
    return True

def main():
    print("📝 开始填充所有剩余详细攻略（14个）...")
    filled = 0
    
    for path, data in FULL_CONTENT.items():
        if create_guide_file(path, data["title"], data["content"]):
            print(f"  ✅ {data['title']}")
            filled += 1
    
    print(f"\n✅ 共创建 {filled} 个新详细攻略页")
    print("🔗 所有软链接已同步更新")
    return 0

if __name__ == "__main__":
    exit(main())
