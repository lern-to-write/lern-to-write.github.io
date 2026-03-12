---
permalink: /
title: "Hi, I'm Yiyu Wang (王一宇) 👋"
excerpt: "Joint Ph.D. Student at HKUST(GZ) & SJTU · Streaming Video Understanding & Game Agent"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

<style>
/* ===== Global Refined Styles ===== */
.bio-card {
  background: linear-gradient(135deg, #f8fafd 0%, #eef2f7 100%);
  border-radius: 12px;
  padding: 28px 30px;
  border-left: 5px solid #1a3a5c;
  margin-bottom: 30px;
  box-shadow: 0 2px 12px rgba(0,0,0,0.06);
}
.bio-card h3 {
  margin-top: 0;
  color: #1a3a5c;
  font-size: 1.25em;
  letter-spacing: 0.3px;
}
.bio-card p {
  font-size: 1.05em;
  line-height: 1.75;
  color: #333;
  margin-bottom: 8px;
}
.bio-card .bio-detail {
  font-size: 0.98em;
  color: #555;
  line-height: 1.7;
}
.badge-row {
  margin-top: 16px;
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
}
.stats-bar {
  display: flex;
  gap: 16px;
  flex-wrap: wrap;
  margin: 20px 0 28px 0;
  padding: 16px 20px;
  background: #fff;
  border-radius: 10px;
  box-shadow: 0 1px 8px rgba(0,0,0,0.06);
  border: 1px solid #e8ecf1;
}
.stats-item {
  text-align: center;
  flex: 1;
  min-width: 80px;
}
.stats-num {
  font-size: 1.6em;
  font-weight: 700;
  color: #1a3a5c;
  display: block;
}
.stats-label {
  font-size: 0.78em;
  color: #888;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}
.section-title {
  font-size: 1.35em;
  color: #1a3a5c;
  border-bottom: 2.5px solid #e8ecf1;
  padding-bottom: 10px;
  margin-top: 32px;
  margin-bottom: 18px;
}
.news-list {
  list-style: none;
  padding: 0;
  margin: 0;
}
.news-list li {
  padding: 10px 0;
  border-bottom: 1px solid #f0f2f5;
  line-height: 1.65;
  font-size: 0.95em;
}
.news-list li:last-child {
  border-bottom: none;
}
.news-badge {
  display: inline-block;
  padding: 2px 10px;
  border-radius: 4px;
  font-weight: 600;
  font-size: 0.82em;
  color: white;
  margin-right: 6px;
  vertical-align: middle;
}
.badge-cvpr { background-color: #c62828; }
.badge-emnlp { background-color: #db545a; }
.badge-eccv { background-color: #1565c0; }
.badge-icml { background-color: #6a1b9a; }
.badge-acl { background-color: #2e7d32; }
.badge-under-review { background-color: #ef6c00; }

/* Paper Card */
.paper-card {
  background: #fff;
  border-radius: 10px;
  padding: 22px 24px;
  margin-bottom: 18px;
  box-shadow: 0 2px 10px rgba(0,0,0,0.06);
  border-left: 4.5px solid #1a3a5c;
  transition: box-shadow 0.25s ease, transform 0.2s ease;
}
.paper-card:hover {
  box-shadow: 0 6px 20px rgba(0,0,0,0.1);
  transform: translateY(-2px);
}
.paper-card.accent-red { border-left-color: #c62828; }
.paper-card.accent-blue { border-left-color: #1565c0; }
.paper-card.accent-purple { border-left-color: #6a1b9a; }
.paper-card.accent-green { border-left-color: #2e7d32; }
.paper-card.accent-orange { border-left-color: #e65100; }

.paper-card h4 {
  margin: 0 0 8px 0;
  font-size: 1.05em;
  line-height: 1.4;
}
.paper-card h4 a {
  text-decoration: none;
  color: #222;
}
.paper-card h4 a:hover {
  color: #1a3a5c;
}
.paper-authors {
  font-size: 0.9em;
  color: #555;
  margin-bottom: 6px;
  line-height: 1.5;
}
.paper-venue {
  font-weight: 700;
  font-size: 0.88em;
  margin-bottom: 8px;
}
.paper-desc {
  font-size: 0.9em;
  color: #666;
  line-height: 1.6;
  margin-bottom: 10px;
}
.paper-links a {
  text-decoration: none;
  margin-right: 6px;
}

/* Project cards */
.project-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 16px;
  margin-top: 12px;
}
.project-card {
  background: #fff;
  border-radius: 10px;
  padding: 18px 20px;
  box-shadow: 0 1px 8px rgba(0,0,0,0.06);
  border: 1px solid #e8ecf1;
  transition: box-shadow 0.25s ease, transform 0.2s ease;
}
.project-card:hover {
  box-shadow: 0 4px 16px rgba(0,0,0,0.1);
  transform: translateY(-2px);
}
.project-card h4 {
  margin: 0 0 6px 0;
  font-size: 1em;
  color: #1a3a5c;
}
.project-card .project-tag {
  display: inline-block;
  font-size: 0.75em;
  padding: 1px 8px;
  border-radius: 3px;
  font-weight: 600;
  color: #fff;
  margin-bottom: 8px;
}
.project-card p {
  font-size: 0.88em;
  color: #666;
  margin-bottom: 10px;
  line-height: 1.55;
}
.project-card a.project-link {
  font-size: 0.85em;
  color: #1a3a5c;
  text-decoration: none;
  font-weight: 600;
}
.project-card a.project-link:hover {
  text-decoration: underline;
}

/* Venue tag inline */
.venue-tag {
  display: inline-block;
  padding: 1px 8px;
  border-radius: 3px;
  font-weight: 700;
  font-size: 0.82em;
  color: #fff;
  margin-right: 4px;
  vertical-align: middle;
}
</style>

<!-- ===== Bio Card ===== -->
<div class="bio-card">
  <h3>🎯 Building Real-Time Video Intelligence & Game Agents</h3>
  <p>
    I am a <strong>joint Ph.D. student</strong> at <a href="https://www.hkust-gz.edu.cn/" style="color:#1a3a5c;">HKUST(GZ)</a> and <a href="https://www.sjtu.edu.cn/" style="color:#1a3a5c;">Shanghai Jiao Tong University (SJTU)</a>, advised by <strong><a href="https://xuminghu.github.io/" style="color:#1a3a5c;">Prof. Xuming Hu</a></strong> and <strong><a href="https://linfeng-zhang.github.io/" style="color:#1a3a5c;">Prof. Linfeng Zhang</a></strong>. I am currently a <strong>Research Intern at <a href="https://www.tencent.com/" style="color:#1a3a5c;">Tencent</a></strong>.
  </p>
  <p class="bio-detail">
    My research focuses on <strong>Streaming Video Understanding</strong> and <strong>Game Agents</strong> — building systems that perceive, reason, and act under real-time constraints with tight token budgets, precise temporal grounding, and reliable interactive behavior. I am also interested in <strong>efficient VideoLLMs</strong> via token compression and data-centric AI.
  </p>
  <div class="badge-row">
    <img src="https://img.shields.io/badge/HKUST(GZ)-1a3a5c?style=flat-square&logo=google-scholar&logoColor=white" alt="HKUST(GZ)">
    <img src="https://img.shields.io/badge/SJTU-0056a3?style=flat-square" alt="SJTU">
    <img src="https://img.shields.io/badge/Tencent_Intern-00a4ef?style=flat-square&logo=tencent-qq&logoColor=white" alt="Tencent">
    <img src="https://img.shields.io/badge/Streaming_Video-c62828?style=flat-square" alt="Streaming Video">
    <img src="https://img.shields.io/badge/Game_Agent-6a1b9a?style=flat-square" alt="Game Agent">
    <img src="https://img.shields.io/badge/Efficient_VideoLLM-2e7d32?style=flat-square" alt="Efficiency">
  </div>
</div>

<!-- ===== Research Overview Stats ===== -->
<div class="stats-bar">
  <div class="stats-item">
    <span class="stats-num">7</span>
    <span class="stats-label">Papers</span>
  </div>
  <div class="stats-item">
    <span class="stats-num">3</span>
    <span class="stats-label">Accepted</span>
  </div>
  <div class="stats-item">
    <span class="stats-num">4</span>
    <span class="stats-label">Under Review</span>
  </div>
</div>

---

<!-- ===== News ===== -->
<h2 class="section-title">🔥 News & Updates</h2>

<ul class="news-list">
  <li>
    <span class="news-badge badge-acl">ACL 2026</span>
    📝 <strong>Under Review</strong> — <em>"Are We Using the Right Benchmark: An Evaluation Framework for Visual Token Compression Methods"</em> submitted to <strong>ACL 2026</strong>.
  </li>
  <li>
    <span class="news-badge badge-eccv">ECCV 2026</span>
    📝 <strong>Under Review</strong> — Collaborated work <em>"V-CAST: Video Curvature-Aware Spatio-Temporal Pruning"</em> submitted to <strong>ECCV 2026</strong>.
  </li>
  <li>
    <span class="news-badge badge-eccv">ECCV 2026</span>
    📝 <strong>Under Review</strong> — Collaborated work <em>"Bridging Visual Representation and Reinforcement Learning from Verifiable Rewards in LVLMs"</em> submitted to <strong>ECCV 2026</strong>.
  </li>
  <li>
    <span class="news-badge badge-icml">ICML 2026</span>
    📝 <strong>Under Review</strong> — Collaborated work <em>"Position: Shifting AI Efficiency from Model-Centric to Data-Centric Compression"</em> submitted to <strong>ICML 2026 Position Track</strong>.
  </li>
  <li>
    <span class="news-badge badge-cvpr">CVPR 2026</span>
    🏆 <strong>Paper Accepted!</strong> Our work <em>"Accelerating Streaming Video Understanding via Hierarchical Token Compression"</em> (<strong>STC</strong>) is accepted to <strong>CVPR 2026</strong>.
  </li>
  <li>
    <span class="news-badge badge-cvpr">CVPR 2026</span>
    🏆 <strong>Paper Accepted!</strong> Collaborated work <em>"Variation-aware Vision Token Dropping for Faster LVLMs"</em> (<strong>V2Drop</strong>) is accepted to <strong>CVPR 2026</strong>.
  </li>
  <li>
    <span class="news-badge badge-emnlp">EMNLP 2025</span>
    🏆 <strong>Paper Accepted!</strong> Our work <em>"Video Compression Commander"</em> (<strong>VidCom²</strong>) is accepted to <strong>EMNLP 2025 Main Conference</strong>.
  </li>
</ul>

---

<!-- ===== Selected Publications ===== -->
<h2 class="section-title">📝 Publications</h2>

<p style="font-size:0.88em; color:#888; margin-bottom:18px;">* denotes equal contribution, † denotes corresponding author.</p>

<!-- ===== Accepted Papers ===== -->
<h3 style="color:#1a3a5c; font-size:1.1em; margin-top:24px; margin-bottom:14px;">✅ Accepted</h3>

<!-- STC - CVPR 2026 -->
<div class="paper-card accent-red">
  <h4><a href="#">Accelerating Streaming Video Understanding via Hierarchical Token Compression</a></h4>
  <div class="paper-authors">
    <strong>Yiyu Wang*</strong>, Xuyang Liu*†, Xiyan Gui, Xinying Lin, Boxue Yang, Chenfei Liao, Tailai Chen, Linfeng Zhang.
  </div>
  <div class="paper-venue" style="color:#c62828;">CVPR 2026</div>
  <div class="paper-desc">
    Proposed <strong>STC-Cacher</strong> and <strong>STC-Pruner</strong>, the first plug-and-play token compression framework specifically designed for real-time streaming video understanding, enabling efficient infinite-length video stream processing.
  </div>
  <div class="paper-links">
    <a href="#"><img src="https://img.shields.io/badge/Paper-Coming_Soon-B31B1B?style=flat&logo=arxiv" alt="Paper"></a>
    <a href="#"><img src="https://img.shields.io/badge/Code-Coming_Soon-181717?style=flat&logo=github" alt="Code"></a>
  </div>
</div>

<!-- V2Drop - CVPR 2026 -->
<div class="paper-card accent-red">
  <h4><a href="https://arxiv.org/abs/2509.01552">Variation-aware Vision Token Dropping for Faster Large Vision-Language Models</a></h4>
  <div class="paper-authors">
    Junjie Chen, Xuyang Liu, Zichen Wen, <strong>Yiyu Wang</strong>, Siteng Huang, Honggang Chen.
  </div>
  <div class="paper-venue" style="color:#c62828;">CVPR 2026</div>
  <div class="paper-desc">
    Leveraged variation-aware token dropping to exploit inherent visual sparsity, accelerating large vision-language models with minimal quality degradation.
  </div>
  <div class="paper-links">
    <a href="https://arxiv.org/abs/2509.01552"><img src="https://img.shields.io/badge/Paper-arXiv-B31B1B?style=flat&logo=arxiv" alt="Paper"></a>
    <a href="https://github.com/xuyang-liu16/V2Drop"><img src="https://img.shields.io/badge/Code-GitHub-181717?style=flat&logo=github" alt="Code"></a>
  </div>
</div>

<!-- VidCom2 - EMNLP 2025 -->
<div class="paper-card accent-orange">
  <h4><a href="https://aclanthology.org/2025.emnlp-main.98/">Video Compression Commander: Plug-and-Play Inference Acceleration for Video Large Language Models</a></h4>
  <div class="paper-authors">
    Xuyang Liu*, <strong>Yiyu Wang*</strong>, Junpeng Ma, Linfeng Zhang.
  </div>
  <div class="paper-venue" style="color:#e65100;">EMNLP 2025 Main Conference</div>
  <div class="paper-desc">
    Proposed <strong>VidCom²</strong>, a training-free framework that adaptively compresses video tokens based on frame uniqueness. Achieved <strong>99.6%</strong> performance retention with only <strong>25% tokens</strong> and <strong>70.8%</strong> latency reduction.
  </div>
  <div class="paper-links">
    <a href="https://aclanthology.org/2025.emnlp-main.98/"><img src="https://img.shields.io/badge/Paper-EMNLP'25-db545a?style=flat&logo=semanticscholar" alt="Paper"></a>
    <a href="https://github.com/xuyang-liu16/VidCom2"><img src="https://img.shields.io/badge/Code-GitHub-181717?style=flat&logo=github" alt="Code"></a>
  </div>
</div>

<!-- ===== Under Review ===== -->
<h3 style="color:#1a3a5c; font-size:1.1em; margin-top:32px; margin-bottom:14px;">📋 Under Review</h3>

<!-- Benchmark - ACL 2026 -->
<div class="paper-card accent-green">
  <h4><a href="#">Are We Using the Right Benchmark: An Evaluation Framework for Visual Token Compression Methods</a></h4>
  <div class="paper-authors">
    Chenfei Liao, Wensong Wang, Zichen Wen, Xu Zheng, <strong>Yiyu Wang</strong>, Haocong He, Yuanhuiyi Lyu, Lutao Jiang, Xin Zou, Yuqian Fu, Bin Ren, Linfeng Zhang, Xuming Hu.
  </div>
  <div class="paper-venue" style="color:#2e7d32;">ACL 2026 (Under Review)</div>
  <div class="paper-desc">
    Built a more revealing evaluation framework for visual token compression methods and investigated whether current benchmarks truly measure the efficiency-quality trade-off.
  </div>
  <div class="paper-links">
    <a href="#"><img src="https://img.shields.io/badge/Paper-Coming_Soon-B31B1B?style=flat&logo=arxiv" alt="Paper"></a>
  </div>
</div>

<!-- V-CAST - ECCV 2026 -->
<div class="paper-card accent-blue">
  <h4><a href="#">V-CAST: Video Curvature-Aware Spatio-Temporal Pruning for Efficient Video Large Language Models</a></h4>
  <div class="paper-authors">
    Xinying Lin, Xuyang Liu, <strong>Yiyu Wang</strong>, Teng Ma, Wenqi Ren.
  </div>
  <div class="paper-venue" style="color:#1565c0;">ECCV 2026 (Under Review)</div>
  <div class="paper-desc">
    Proposed curvature-aware spatio-temporal pruning for efficient video LLMs, exploiting geometric curvature signals to selectively prune redundant video tokens in both spatial and temporal dimensions.
  </div>
  <div class="paper-links">
    <a href="#"><img src="https://img.shields.io/badge/Paper-Coming_Soon-B31B1B?style=flat&logo=arxiv" alt="Paper"></a>
  </div>
</div>

<!-- Bridging Visual Representation and RL - ECCV 2026 -->
<div class="paper-card accent-blue">
  <h4><a href="#">Bridging Visual Representation and Reinforcement Learning from Verifiable Rewards in Large Vision-Language Models</a></h4>
  <div class="paper-authors">
    Yuhang Han, Yuyang Wu, Zhengbo Jiao, <strong>Yiyu Wang</strong>, Xuyang Liu, Shaobo Wang, Hanlin Xu, Xuming Hu, Linfeng Zhang.
  </div>
  <div class="paper-venue" style="color:#1565c0;">ECCV 2026 (Under Review)</div>
  <div class="paper-desc">
    Bridged visual representation learning with reinforcement learning from verifiable rewards (RLVR) in large vision-language models, enabling more grounded visual understanding through reward-driven optimization.
  </div>
  <div class="paper-links">
    <a href="#"><img src="https://img.shields.io/badge/Paper-Coming_Soon-B31B1B?style=flat&logo=arxiv" alt="Paper"></a>
  </div>
</div>

<!-- Position Paper - ICML 2026 -->
<div class="paper-card accent-purple">
  <h4><a href="https://arxiv.org/abs/2505.19147">Position: Shifting AI Efficiency from Model-Centric to Data-Centric Compression</a></h4>
  <div class="paper-authors">
    Xuyang Liu, Zichen Wen, Shaobo Wang, Junjie Chen, Zhishan Tao, Yubo Wang, Tailai Chen, Xiangqi Jin, Chang Zou, <strong>Yiyu Wang</strong>, Chenfei Liao, Xu Zheng, Honggang Chen, Weijia Li, Xuming Hu, Conghui He, Linfeng Zhang.
  </div>
  <div class="paper-venue" style="color:#6a1b9a;">ICML 2026 Position Paper Track (Under Review)</div>
  <div class="paper-desc">
    A position paper arguing that AI efficiency research should shift focus from model-centric compression to data-centric compression, establishing a unified framework for existing efficiency strategies.
  </div>
  <div class="paper-links">
    <a href="https://arxiv.org/abs/2505.19147"><img src="https://img.shields.io/badge/Paper-arXiv-B31B1B?style=flat&logo=arxiv" alt="Paper"></a>
  </div>
</div>

---

<!-- ===== Selected Projects ===== -->
<h2 class="section-title">💻 Selected Projects</h2>

<div class="project-grid">
  <div class="project-card">
    <span class="project-tag" style="background:#c62828;">CVPR 2026</span>
    <h4>STC</h4>
    <p>A streaming-first token compression framework with caching and pruning for real-time video understanding.</p>
    <a href="#" class="project-link">Code Coming Soon →</a>
  </div>
  <div class="project-card">
    <span class="project-tag" style="background:#e65100;">EMNLP 2025</span>
    <h4>VidCom²</h4>
    <p>Plug-and-play inference acceleration for VideoLLMs via adaptive frame-uniqueness-based token compression.</p>
    <a href="https://github.com/xuyang-liu16/VidCom2" class="project-link">Open Project →</a>
  </div>
  <div class="project-card">
    <span class="project-tag" style="background:#c62828;">CVPR 2026</span>
    <h4>V2Drop</h4>
    <p>Variation-aware visual token dropping that exploits inherent sparsity signals for faster LVLMs.</p>
    <a href="https://github.com/xuyang-liu16/V2Drop" class="project-link">View Code →</a>
  </div>
</div>

---

<!-- ===== Academic Service ===== -->
<h2 class="section-title">🎓 Academic Service</h2>

**Reviewer** for CVPR, ECCV, ACM MM, EMNLP, and other top-tier venues.
