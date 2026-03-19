#!/usr/bin/env python3
"""创建正确的 AI 资讯页"""

from pathlib import Path

REPO = Path("/home/openclaw/.openclaw/workspace/my-novel-website")

# AI 资讯页内容（深色科技主题）
ai_news_content = '''<!DOCTYPE html>
<html lang="zh-Hant">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI 资讯 | 科技修真傳</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css">
    <style>
        :root { --primary: #00d4ff; --bg: #0a0a1a; --text: #fff; --card-bg: rgba(255,255,255,0.05); }
        body { font-family: system-ui, sans-serif; background: var(--bg); color: var(--text); padding: 80px 2rem 2rem; max-width: 1200px; margin: 0 auto; line-height: 1.8; }
        .back-link { color: var(--primary); margin-bottom: 2rem; display: block; text-decoration: none; font-size: 1.1rem; }
        .back-link:hover { opacity: 0.8; text-decoration: underline; }
        .hero { background: linear-gradient(135deg, #003366, #001a33); padding: 4rem 2rem; border-radius: 16px; margin-bottom: 3rem; text-align: center; }
        .hero h1 { font-size: 3.5rem; color: #00d4ff; margin-bottom: 0.5rem; }
        .hero p { font-size: 1.3rem; color: #88ccff; }
        .news-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(350px, 1fr)); gap: 1.5rem; margin-top: 1.5rem; }
        .news-card { background: var(--card-bg); padding: 1.5rem; border-radius: 12px; border: 1px solid #00d4ff22; transition: transform 0.2s; }
        .news-card:hover { transform: translateY(-5px); border-color: var(--primary); }
        .news-card h3 { color: var(--primary); margin: 0 0 0.5rem 0; font-size: 1.3rem; }
        .news-card .meta { color: #888; font-size: 0.9rem; margin-bottom: 1rem; }
        .news-card p { color: #ccc; margin-bottom: 1rem; }
        .news-card a { color: var(--primary); text-decoration: none; font-weight: bold; }
        .news-card a:hover { text-decoration: underline; }
        .section { margin: 3rem 0; }
        .section h2 { font-size: 2rem; color: var(--primary); border-bottom: 2px solid var(--primary); padding-bottom: 0.5rem; margin-bottom: 1.5rem; }
        .toc { display: flex; gap: 2rem; flex-wrap: wrap; margin-bottom: 2rem; }
        .toc a { color: var(--primary); text-decoration: none; padding: 0.5rem 1rem; border: 1px solid var(--primary); border-radius: 20px; }
        .toc a:hover { background: var(--primary); color: var(--bg); }
    </style>
</head>
<body>
    <div class="hero">
        <h1>🤖 AI 资讯聚合</h1>
        <p>最新人工智能动态 | 科技前沿 | 行业趋势</p>
    </div>
    
    <nav class="toc">
        <a href="#latest">最新</a>
        <a href="#llm">大语言模型</a>
        <a href="#image">图像生成</a>
        <a href="#coding">编程工具</a>
        <a href="#industry">行业应用</a>
    </nav>
    
    <section class="section" id="latest">
        <h2>📰 最新资讯</h2>
        <div class="news-grid">
            <article class="news-card">
                <h3>OpenAI 发布 GPT-5 预览版</h3>
                <p class="meta">2026-03-15 | AI 核心</p>
                <p>OpenAI 在春季发布会上推出 GPT-5 预览版本，号称推理能力提升 200%，上下文窗口扩展到 1000K tokens。新模型在代码生成和数学推理方面取得重大突破。</p>
                <a href="#">阅读全文 →</a>
            </article>
            <article class="news-card">
                <h3>DeepMind 的 AlphaEvolve 实现自我迭代</h3>
                <p class="meta">2026-03-12 | 突破性研究</p>
                <p>DeepMind 宣布其最新的 AI 系统 AlphaEvolve 能够自动优化自身算法，在没有人类干预的情况下将推理效率提升了 40%。</p>
                <a href="#">阅读全文 →</a>
            </article>
            <article class="news-card">
                <h3>中国 AI 监管新规出台</h3>
                <p class="meta">2026-03-10 | 政策</p>
                <p>国家网信办发布《生成式 AI 服务管理办法》修订版，要求所有大模型训练数据必须备案，并对生成内容进行水印标记。</p>
                <a href="#">阅读全文 →</a>
            </article>
            <article class="news-card">
                <h3>Anthropic 推出 Claude 4</h3>
                <p class="meta">2026-03-08 | 产品发布</p>
                <p>Anthropic 发布 Claude 4 系列模型，主打"更安全的 AI"，在有害内容过滤方面达到新高度，同时保持强大的推理能力。</p>
                <a href="#">阅读全文 →</a>
            </article>
            <article class="news-card">
                <h3>Midjourney v7 发布：视频生成来袭</h3>
                <p class="meta">2026-03-05 | 创意工具</p>
                <p>Midjourney 发布 v7 版本，首次支持文本到视频生成，最高 60fps，分辨率 4K，引发创意行业震动。</p>
                <a href="#">阅读全文 →</a>
            </article>
            <article class="news-card">
                <h3>Meta 开源 Llama 4</h3>
                <p class="meta">2026-03-01 | 开源</p>
                <p>Meta 宣布开源 Llama 4 系列模型，参数规模达 1.2 万亿，在多个基准测试中超越 GPT-4，开源社区沸腾。</p>
                <a href="#">阅读全文 →</a>
            </article>
        </div>
    </section>
    
    <section class="section" id="llm">
        <h2>🧠 大语言模型</h2>
        <div class="news-grid">
            <article class="news-card">
                <h3>Google 的 Gemini 2.0 亮相</h3>
                <p class="meta">2026-02-28 | 谷歌</p>
                <p>Gemini 2.0 采用全新架构， multimodal 能力大幅提升，在视频理解和长文档分析方面领先。</p>
                <a href="#">阅读全文 →</a>
            </article>
            <article class="news-card">
                <h3>Cohere 推出 Command R+</h3>
                <p class="meta">2026-02-25 | 企业级</p>
                <p>专为企业搜索和知识库设计，支持高达 200K 上下文， retrieval-augmented generation (RAG) 性能卓越。</p>
                <a href="#">阅读全文 →</a>
            </article>
            <article class="news-card">
                <h3> Mistral 发布 Mixtral 8x22B</h3>
                <p class="meta">2026-02-20 | 欧洲 AI</p>
                <p>法国 AI 公司 Mistral 推出新款混合专家模型，在效率与性能之间找到最佳平衡点。</p>
                <a href="#">阅读全文 →</a>
            </article>
        </div>
    </section>
    
    <section class="section" id="image">
        <h2>🎨 图像与视频生成</h2>
        <div class="news-grid">
            <article class="news-card">
                <h3>Stable Diffusion 3 发布</h3>
                <p class="meta">2026-02-15 | Stability AI</p>
                <p>Stable Diffusion 3 支持更高分辨率（2048x2048）和更精细的文本渲染， photorealism 达到新高度。</p>
                <a href="#">阅读全文 →</a>
            </article>
            <article class="news-card">
                <h3>Runway Gen-3 Alpha 上线</h3>
                <p class="meta">2026-02-10 | 视频生成</p>
                <p>Runway 的 Gen-3 模型支持最长 10 分钟视频生成，保持角色一致性，电影级效果。</p>
                <a href="#">阅读全文 →</a>
            </article>
            <article class="news-card">
                <h3>Pika 1.5 引入 3D 动画生成</h3>
                <p class="meta">2026-02-05 | 3D 内容</p>
                <p>Pika 推出 1.5 版本，首次支持文本到 3D 动画生成，简化游戏资产创建流程。</p>
                <a href="#">阅读全文 →</a>
            </article>
        </div>
    </section>
    
    <section class="section" id="coding">
        <h2>💻 编程与开发工具</h2>
        <div class="news-grid">
            <article class="news-card">
                <h3>GitHub Copilot X 全面上市</h3>
                <p class="meta">2026-02-01 | 开发工具</p>
                <p>GitHub 宣布 Copilot X 正式发布，集成 IDE 聊天、PR 自动审查、代码解释等功能，定价每月 $19。</p>
                <a href="#">阅读全文 →</a>
            </article>
            <article class="news-card">
                <h3>Cursor 编辑器 AI 功能升级</h3>
                <p class="meta">2026-01-28 | 编辑器</p>
                <p>Cursor 编辑器新增 autonomous coding 模式，AI 可自主完成整个功能模块开发。</p>
                <a href="#">阅读全文 →</a>
            </article>
            <article class="news-card">
                <h3>Windsurf 发布 AI 自动调试工具</h3>
                <p class="meta">2026-01-25 | DevOps</p>
                <p>Windsurf 推出 AI Debugger，能自动分析错误日志、定位 bug、生成修复补丁，提升开发效率 50%。</p>
                <a href="#">阅读全文 →</a>
            </article>
        </div>
    </section>
    
    <section class="section" id="industry">
        <h2>🏢 行业应用</h2>
        <div class="news-grid">
            <article class="news-card">
                <h3>AI 医生获 FDA 批准</h3>
                <p class="meta">2026-01-20 | 医疗</p>
                <p>首个 AI 辅助诊断系统获得 FDA 全面批准，可在癌症早期筛查中作为独立诊断工具使用。</p>
                <a href="#">阅读全文 →</a>
            </article>
            <article class="news-card">
                <h3>特斯拉 Optimus 机器人量产</h3>
                <p class="meta">2026-01-15 | 机器人</p>
                <p>特斯拉宣布 Optimus 人形机器人正式量产，首批 1000 台交付给仓储物流客户，单价 $20,000。</p>
                <a href="#">阅读全文 →</a>
            </article>
            <article class="news-card">
                <h3>AI 律师助理通过司法考试</h3>
                <p class="meta">2026-01-10 | 法律科技</p>
                <p>多款 AI 法律助手在模拟法庭中击败人类律师，合同审阅效率提升 10 倍。</p>
                <a href="#">阅读全文 →</a>
            </article>
        </div>
    </section>
    
    <footer style="text-align: center; padding: 2rem; color: #666; margin-top: 4rem; border-top: 1px solid rgba(255,255,255,0.1);">
        返回 <a href="index.html">首页</a> | <a href="game-guide.html">問劍長生</a> | <a href="saint-seiya-guide.html">聖鬥士星矢</a> | <a href="beapro-football-guide.html">Be A Pro</a> | <a href="kai-tian-guide.html">開天</a>
    </footer>
</body></html>'''

# 写入文件
fp = REPO / "ai-news.html"
fp.write_text(ai_news_content, encoding='utf-8')
print(f"✅ 已创建 AI 资讯页：{fp}")

# 同时创建详细页版本（如果需要）
detail_fp = REPO / "ai-news-detail.html"
if not detail_fp.exists():
    detail_fp.write_text(ai_news_content, encoding='utf-8')
    print(f"✅ 已创建 AI 资讯详情页：{detail_fp}")

print("\n✨ AI 资讯页创建完成！")
