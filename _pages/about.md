---
permalink: /
title: "Yiyu Wang (王一宇)"
excerpt: "Joint Ph.D. Student at HKUST(GZ) & SJTU · Streaming Video Understanding"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

<style>
/* ===== Refined Glassmorphism Design System v4 ===== */

:root {
  --p1: #6366f1;   --p2: #818cf8;
  --a1: #8b5cf6;   --a2: #a78bfa;
  --h1: #ec4899;   --h2: #f472b6;
  --bg: #f8fafc;
  --card: rgba(255,255,255,0.75);
  --card-b: rgba(255,255,255,0.55);
  --text: #0f172a;
  --text2: #475569;
  --muted: #94a3b8;
  --shadow: 0 8px 32px rgba(99,102,241,0.07);
  --shadow-h: 0 20px 60px rgba(99,102,241,0.14);
  --radius: 20px;
  --grad: linear-gradient(135deg, var(--p1), var(--a1), var(--h1));
  --grad-soft: linear-gradient(135deg, rgba(99,102,241,0.08), rgba(139,92,246,0.06), rgba(236,72,153,0.04));
}

/* --- Hero --- */
.hero {
  position: relative; overflow: hidden;
  border-radius: var(--radius);
  padding: 56px 44px 48px;
  margin-bottom: 36px;
  background: var(--grad-soft);
  border: 1px solid var(--card-b);
}
.hero::before {
  content: ''; position: absolute;
  top: -50%; right: -30%; width: 500px; height: 500px;
  background: radial-gradient(circle, rgba(99,102,241,0.12), transparent 70%);
  border-radius: 50%; pointer-events: none;
  animation: heroGlow 8s ease-in-out infinite alternate;
}
.hero::after {
  content: ''; position: absolute;
  bottom: -40%; left: -20%; width: 400px; height: 400px;
  background: radial-gradient(circle, rgba(236,72,153,0.08), transparent 70%);
  border-radius: 50%; pointer-events: none;
  animation: heroGlow2 10s ease-in-out infinite alternate;
}
@keyframes heroGlow {
  0% { transform: translate(0,0) scale(1); opacity: 0.6; }
  100% { transform: translate(-30px,20px) scale(1.1); opacity: 1; }
}
@keyframes heroGlow2 {
  0% { transform: translate(0,0) scale(1); opacity: 0.5; }
  100% { transform: translate(20px,-20px) scale(1.15); opacity: 0.9; }
}
.hero-name {
  font-size: 2.6em; font-weight: 900; letter-spacing: -0.03em;
  line-height: 1.15; margin: 0 0 8px;
  background: var(--grad); -webkit-background-clip: text;
  -webkit-text-fill-color: transparent; background-clip: text;
  position: relative; z-index: 1;
}
.hero-tagline {
  font-size: 1.15em; color: var(--text2); font-weight: 500;
  margin: 0 0 16px; position: relative; z-index: 1;
}
.hero-bio {
  font-size: 0.95em; color: var(--text2); line-height: 1.85;
  max-width: 720px; position: relative; z-index: 1;
}
.hero-bio a {
  color: var(--p1); text-decoration: none; font-weight: 600;
  border-bottom: 1.5px solid rgba(99,102,241,0.25);
  transition: border-color 0.25s, color 0.25s;
}
.hero-bio a:hover { border-color: var(--p1); color: var(--a1); }
.hero-badges {
  margin-top: 20px; display: flex; flex-wrap: wrap; gap: 8px;
  position: relative; z-index: 1;
}
.hero-badges a img {
  height: 24px; border-radius: 6px;
  transition: transform 0.3s cubic-bezier(.34,1.56,.64,1), box-shadow 0.2s;
}
.hero-badges a img:hover {
  transform: translateY(-3px) scale(1.06);
  box-shadow: 0 6px 18px rgba(99,102,241,0.2);
}

/* --- Research Pills --- */
.research-row {
  display: flex; flex-wrap: wrap; gap: 14px;
  margin-bottom: 36px;
}
.r-pill {
  flex: 1; min-width: 180px;
  display: flex; align-items: center; gap: 14px;
  padding: 18px 22px; border-radius: var(--radius);
  background: var(--card);
  backdrop-filter: blur(20px) saturate(1.3);
  -webkit-backdrop-filter: blur(20px) saturate(1.3);
  border: 1px solid var(--card-b);
  box-shadow: var(--shadow);
  transition: all 0.4s cubic-bezier(.34,1.56,.64,1);
  cursor: default; position: relative; overflow: hidden;
}
.r-pill::before {
  content: ''; position: absolute; inset: 0;
  background: var(--grad-soft); opacity: 0;
  transition: opacity 0.4s;
}
.r-pill:hover {
  transform: translateY(-5px) scale(1.02);
  box-shadow: var(--shadow-h);
}
.r-pill:hover::before { opacity: 1; }
.r-pill .r-icon {
  width: 44px; height: 44px; border-radius: 14px;
  display: flex; align-items: center; justify-content: center;
  font-size: 1.3em; flex-shrink: 0; position: relative; z-index: 1;
  background: var(--grad); color: #fff;
  box-shadow: 0 6px 16px rgba(99,102,241,0.3);
  transition: transform 0.3s;
}
.r-pill:hover .r-icon { transform: scale(1.15) rotate(-6deg); }
.r-pill .r-text { flex: 1; position: relative; z-index: 1; }
.r-pill .r-text strong { display: block; font-size: 0.96em; margin-bottom: 3px; color: var(--text); }
.r-pill .r-text span { font-size: 0.78em; color: var(--text2); font-weight: 400; }

/* --- Stats --- */
.stats-row {
  display: grid; grid-template-columns: repeat(3, 1fr);
  gap: 20px; margin-bottom: 40px;
}
.stat-box {
  text-align: center; padding: 32px 20px 26px;
  background: var(--card);
  backdrop-filter: blur(20px) saturate(1.3);
  -webkit-backdrop-filter: blur(20px) saturate(1.3);
  border: 1px solid var(--card-b);
  border-radius: var(--radius);
  box-shadow: var(--shadow);
  transition: all 0.4s cubic-bezier(.34,1.56,.64,1);
  position: relative; overflow: hidden;
}
.stat-box::after {
  content: ''; position: absolute; bottom: 0; left: 0; right: 0;
  height: 3px; background: var(--grad);
  opacity: 0.5; transition: height 0.3s, opacity 0.3s;
}
.stat-box:hover {
  transform: translateY(-6px);
  box-shadow: var(--shadow-h);
}
.stat-box:hover::after { height: 5px; opacity: 1; }
.stat-num {
  font-size: 3em; font-weight: 900; letter-spacing: -0.04em;
  line-height: 1; display: block;
  background: var(--grad); -webkit-background-clip: text;
  -webkit-text-fill-color: transparent; background-clip: text;
  font-family: 'JetBrains Mono', 'Fira Code', monospace;
}
.stat-label {
  font-size: 0.72em; color: var(--muted); text-transform: uppercase;
  letter-spacing: 0.16em; font-weight: 700; margin-top: 12px; display: block;
}

/* --- Section Title --- */
.sec-title {
  font-size: 1.35em; font-weight: 800; color: var(--text);
  padding-bottom: 14px; margin-top: 40px; margin-bottom: 24px;
  letter-spacing: -0.02em;
  display: flex; align-items: center; gap: 14px;
}
.sec-title .s-icon {
  width: 38px; height: 38px; border-radius: 12px;
  background: var(--grad); color: #fff;
  display: inline-flex; align-items: center; justify-content: center;
  font-size: 1em; box-shadow: 0 6px 16px rgba(99,102,241,0.25);
}
.sec-title::after {
  content: ''; flex: 1; height: 2px;
  background: linear-gradient(90deg, rgba(99,102,241,0.15), transparent);
  border-radius: 1px;
}

/* --- Divider --- */
.divider {
  height: 1px; border: none; margin: 44px 0;
  background: linear-gradient(90deg, transparent, rgba(99,102,241,0.1) 20%, rgba(99,102,241,0.1) 80%, transparent);
  position: relative;
}
.divider::before, .divider::after {
  content: ''; position: absolute; top: -3px;
  width: 7px; height: 7px; border-radius: 50%;
  background: var(--grad);
}
.divider::before { left: calc(50% - 14px); opacity: 0.5; }
.divider::after { left: calc(50% + 7px); opacity: 0.25; }

/* --- News Timeline --- */
.timeline {
  position: relative; padding-left: 36px; list-style: none; margin: 0;
}
.timeline::before {
  content: ''; position: absolute;
  top: 6px; bottom: 6px; left: 10px; width: 2.5px;
  background: linear-gradient(180deg, var(--p1) 0%, var(--a1) 50%, rgba(99,102,241,0.08) 100%);
  border-radius: 2px;
}
.timeline li {
  position: relative;
  padding: 14px 18px 14px 14px;
  margin-bottom: 10px; border-radius: 14px;
  font-size: 0.9em; color: var(--text2);
  line-height: 1.7; transition: all 0.35s cubic-bezier(.34,1.56,.64,1);
}
.timeline li:hover {
  background: rgba(99,102,241,0.03);
  transform: translateX(8px);
  box-shadow: 0 4px 16px rgba(99,102,241,0.06);
}
.timeline li::before {
  content: ''; position: absolute;
  left: -31px; top: 21px;
  width: 14px; height: 14px; border-radius: 50%;
  background: #fff; border: 2.5px solid var(--p1);
  box-shadow: 0 0 0 5px rgba(99,102,241,0.08);
  z-index: 1; transition: all 0.3s cubic-bezier(.34,1.56,.64,1);
}
.timeline li:hover::before {
  background: var(--p1); border-color: var(--p1);
  box-shadow: 0 0 0 7px rgba(99,102,241,0.15);
  transform: scale(1.3);
}
.timeline li.done::before { border-color: #10b981; background: #ecfdf5; }
.timeline li.done:hover::before { background: #10b981; border-color: #10b981; box-shadow: 0 0 0 7px rgba(16,185,129,0.15); }
.timeline li em { color: var(--text); font-style: normal; font-weight: 600; }
.timeline li strong { color: var(--text); }

.t-badge {
  display: inline-block; padding: 4px 12px; border-radius: 8px;
  font-weight: 700; font-size: 0.72em; color: #fff;
  margin-right: 8px; vertical-align: middle; letter-spacing: 0.04em;
  background: var(--grad);
  box-shadow: 0 3px 10px rgba(99,102,241,0.25);
  position: relative; overflow: hidden;
}
.t-badge::after {
  content: ''; position: absolute; top: 0; left: -100%;
  width: 100%; height: 100%;
  background: linear-gradient(90deg, transparent, rgba(255,255,255,0.25), transparent);
  animation: shimmer 3.5s ease-in-out infinite;
}
@keyframes shimmer { 0% { left: -100%; } 100% { left: 200%; } }

/* --- Sub Heading --- */
.sub-h {
  font-size: 1.05em; font-weight: 700; color: var(--text);
  margin: 32px 0 18px; display: flex; align-items: center; gap: 12px;
}
.sub-h .dot {
  width: 10px; height: 10px; border-radius: 50%;
  flex-shrink: 0; position: relative;
}
.sub-h .dot::after {
  content: ''; position: absolute; inset: -5px;
  border-radius: 50%; border: 1.5px solid currentColor;
  opacity: 0.3; animation: pulseRing 2.5s ease-in-out infinite;
}
@keyframes pulseRing {
  0%,100% { transform: scale(1); opacity: 0.3; }
  50% { transform: scale(1.5); opacity: 0; }
}
.sub-h .count {
  font-size: 0.72em; font-weight: 700; color: #fff;
  padding: 3px 10px; border-radius: 10px;
  font-family: 'JetBrains Mono', 'Fira Code', monospace;
  letter-spacing: 0.03em; background: var(--grad);
}

/* --- Paper Card --- */
.p-card {
  background: var(--card);
  backdrop-filter: blur(20px) saturate(1.3);
  -webkit-backdrop-filter: blur(20px) saturate(1.3);
  border: 1px solid var(--card-b);
  border-radius: var(--radius);
  padding: 28px 32px;
  margin-bottom: 18px;
  box-shadow: var(--shadow);
  border-left: 4px solid var(--p1);
  transition: all 0.4s cubic-bezier(.34,1.56,.64,1);
  position: relative; overflow: hidden;
}
.p-card::before {
  content: ''; position: absolute;
  top: 0; right: 0; width: 60px; height: 60px;
  background: linear-gradient(225deg, rgba(99,102,241,0.06) 50%, transparent 50%);
  pointer-events: none; transition: width 0.3s, height 0.3s;
}
.p-card:hover::before { width: 80px; height: 80px; }
.p-card:hover {
  box-shadow: var(--shadow-h);
  transform: translateY(-5px);
  border-left-width: 6px;
}
.p-card h4 { margin: 0 0 10px; font-size: 1.05em; line-height: 1.5; font-weight: 700; }
.p-card h4 a { color: var(--text); text-decoration: none; border-bottom: none; transition: color 0.2s; }
.p-card h4 a:hover { color: var(--p1); }

.p-authors { font-size: 0.84em; color: var(--text2); margin-bottom: 8px; line-height: 1.6; }
.p-authors strong { color: var(--text); font-weight: 600; }
.p-chip {
  display: inline-block; padding: 4px 14px;
  border-radius: 8px; font-weight: 700;
  font-size: 0.74em; letter-spacing: 0.03em;
  margin-bottom: 12px; color: var(--p1);
  background: rgba(99,102,241,0.08);
}
.p-desc { font-size: 0.87em; color: var(--text2); line-height: 1.7; margin-bottom: 16px; }
.p-desc strong { color: var(--text); font-weight: 600; }

.p-links { display: flex; flex-wrap: wrap; gap: 8px; }
.p-links a { text-decoration: none; margin-right: 0; border-bottom: none; display: inline-block; }
.p-links img {
  height: 24px; border-radius: 5px;
  transition: transform 0.3s cubic-bezier(.34,1.56,.64,1), box-shadow 0.2s;
}
.p-links img:hover { transform: translateY(-3px) scale(1.05); box-shadow: 0 6px 16px rgba(99,102,241,0.2); }

.note { font-size: 0.82em; color: var(--muted); margin-bottom: 18px; font-style: italic; }

/* --- Project Grid --- */
.proj-grid {
  display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 20px; margin-top: 10px;
}
.proj-card {
  background: var(--card);
  backdrop-filter: blur(20px) saturate(1.3);
  -webkit-backdrop-filter: blur(20px) saturate(1.3);
  border: 1px solid var(--card-b);
  border-radius: var(--radius);
  padding: 28px 28px;
  box-shadow: var(--shadow);
  transition: all 0.4s cubic-bezier(.34,1.56,.64,1);
  display: flex; flex-direction: column;
  position: relative; overflow: hidden;
}
.proj-card::before {
  content: ''; position: absolute;
  top: 0; left: 0; right: 0; height: 3px;
  background: var(--grad); opacity: 0;
  transition: opacity 0.3s, height 0.3s;
}
.proj-card:hover {
  box-shadow: var(--shadow-h);
  transform: translateY(-7px);
}
.proj-card:hover::before { opacity: 1; height: 4px; }

.proj-tag {
  display: inline-block; font-size: 0.68em;
  padding: 5px 12px; border-radius: 10px;
  font-weight: 700; color: #fff;
  margin-bottom: 16px; width: fit-content;
  letter-spacing: 0.05em;
  background: var(--grad);
  box-shadow: 0 3px 10px rgba(99,102,241,0.25);
}
.proj-card h4 {
  margin: 0 0 10px; font-size: 1.15em; font-weight: 700;
  color: var(--text); letter-spacing: -0.01em;
}
.proj-card p {
  font-size: 0.85em; color: var(--text2);
  margin-bottom: 18px; line-height: 1.65; flex: 1;
}
.proj-card a.plink {
  font-size: 0.84em; color: var(--p1); font-weight: 600;
  text-decoration: none; display: inline-flex;
  align-items: center; gap: 6px;
  transition: gap 0.3s cubic-bezier(.34,1.56,.64,1); border-bottom: none;
  padding: 6px 0;
}
.proj-card a.plink:hover { gap: 12px; text-decoration: none; }

/* --- Service Card --- */
.svc-card {
  padding: 24px 28px; border-radius: var(--radius);
  background: var(--card);
  backdrop-filter: blur(20px) saturate(1.3);
  -webkit-backdrop-filter: blur(20px) saturate(1.3);
  border: 1px solid var(--card-b);
  box-shadow: var(--shadow);
  font-size: 0.93em; color: var(--text2); line-height: 1.7;
  display: flex; align-items: center; gap: 18px;
  transition: all 0.35s ease;
}
.svc-card:hover {
  transform: translateY(-3px);
  box-shadow: var(--shadow-h);
}
.svc-card .svc-icon {
  width: 48px; height: 48px; border-radius: 14px;
  background: var(--grad);
  display: flex; align-items: center; justify-content: center;
  font-size: 1.3em; flex-shrink: 0;
  box-shadow: 0 6px 18px rgba(99,102,241,0.3);
  color: #fff;
}
.svc-card strong { color: var(--text); }
.v-tags { display: flex; flex-wrap: wrap; gap: 6px; margin-top: 10px; }
.v-tag {
  font-size: 0.74em; padding: 3px 12px; border-radius: 6px;
  font-weight: 600; letter-spacing: 0.03em;
  background: rgba(99,102,241,0.07); color: var(--p1);
  transition: all 0.25s;
}
.v-tag:hover { background: var(--p1); color: #fff; }

/* --- Scroll Reveal --- */
.reveal {
  opacity: 1; transform: translateY(0);
}
.reveal.will-anim {
  opacity: 0; transform: translateY(30px) scale(0.98);
  transition: opacity 0.9s cubic-bezier(.16,1,.3,1), transform 0.9s cubic-bezier(.16,1,.3,1);
}
.reveal.will-anim.visible { opacity: 1; transform: translateY(0) scale(1); }

/* --- Responsive --- */
@media (max-width: 768px) {
  .hero { padding: 36px 24px 32px; }
  .hero-name { font-size: 2em; }
  .stats-row { gap: 12px; }
  .stat-box { padding: 24px 14px 20px; }
  .stat-num { font-size: 2.2em; }
  .proj-grid { grid-template-columns: 1fr; }
  .research-row { gap: 10px; }
  .r-pill { padding: 14px 16px; min-width: 140px; }
  .timeline { padding-left: 30px; }
  .p-card { padding: 22px 24px; }
}
@media (max-width: 480px) {
  .research-row { flex-direction: column; }
  .r-pill { min-width: 100%; }
  .stats-row { grid-template-columns: 1fr; }
}
</style>

<!-- ===== Hero ===== -->
<div class="hero reveal">
  <div class="hero-name">Yiyu Wang</div>
  <div class="hero-tagline">王一宇 · Joint Ph.D. @ HKUST(GZ) &amp; SJTU</div>
  <div class="hero-bio">
    I am a <strong>joint Ph.D. student</strong> at <a href="https://www.hkust-gz.edu.cn/">HKUST(GZ)</a> and <a href="https://www.sjtu.edu.cn/">Shanghai Jiao Tong University</a>, advised by <a href="https://xuminghu.github.io/">Prof. Xuming Hu</a> and <a href="https://linfeng-zhang.github.io/">Prof. Linfeng Zhang</a>. Currently a <strong>Research Intern at Tencent</strong>.<br><br>
    My research focuses on <strong>Streaming Video Understanding</strong> — building systems that perceive, reason, and act under real-time constraints with tight token budgets and precise temporal grounding. I am also interested in <strong>efficient VideoLLMs</strong> via token compression and data-centric AI.
  </div>
  <div class="hero-badges">
    <a href="#"><img src="https://img.shields.io/badge/HKUST(GZ)-6366f1?style=flat-square&logo=google-scholar&logoColor=white" alt="HKUST(GZ)"></a>
    <a href="#"><img src="https://img.shields.io/badge/SJTU-0056a3?style=flat-square" alt="SJTU"></a>
    <a href="#"><img src="https://img.shields.io/badge/Tencent_Intern-00a4ef?style=flat-square&logo=tencent-qq&logoColor=white" alt="Tencent"></a>
    <a href="#"><img src="https://img.shields.io/badge/Streaming_Video-ec4899?style=flat-square" alt="Streaming Video"></a>
    <a href="#"><img src="https://img.shields.io/badge/Efficient_VideoLLM-8b5cf6?style=flat-square" alt="Efficiency"></a>
  </div>
</div>

<!-- ===== Research Highlights ===== -->
<div class="research-row reveal">
  <div class="r-pill">
    <div class="r-icon">📡</div>
    <div class="r-text">
      <strong>Streaming Video</strong>
      <span>Real-time perception &amp; reasoning</span>
    </div>
  </div>
  <div class="r-pill">
    <div class="r-icon">⚡</div>
    <div class="r-text">
      <strong>Token Compression</strong>
      <span>Efficient visual encoding</span>
    </div>
  </div>
  <div class="r-pill">
    <div class="r-icon">📊</div>
    <div class="r-text">
      <strong>Data-Centric AI</strong>
      <span>Quality over quantity</span>
    </div>
  </div>
</div>

<!-- ===== Stats ===== -->
<div class="stats-row reveal" id="stats-row">
  <div class="stat-box">
    <span class="stat-num" data-target="8">0</span>
    <span class="stat-label">Papers</span>
  </div>
  <div class="stat-box">
    <span class="stat-num" data-target="3">0</span>
    <span class="stat-label">Accepted</span>
  </div>
  <div class="stat-box">
    <span class="stat-num" data-target="4">0</span>
    <span class="stat-label">Under Review</span>
  </div>
</div>

<div class="divider"></div>

<!-- ===== News ===== -->
<h2 class="sec-title reveal"><span class="s-icon">🔥</span> News &amp; Updates</h2>

<ul class="timeline">
  <li class="reveal">
    <span class="t-badge">ACL 2026</span>
    📝 <strong>Under Review</strong> — <em>"Are We Using the Right Benchmark: An Evaluation Framework for Visual Token Compression Methods"</em> submitted to <strong>ACL 2026</strong>.
  </li>
  <li class="reveal">
    <span class="t-badge">ECCV 2026</span>
    📝 <strong>Under Review</strong> — <em>"V-CAST: Video Curvature-Aware Spatio-Temporal Pruning"</em> submitted to <strong>ECCV 2026</strong>.
  </li>
  <li class="reveal">
    <span class="t-badge">ECCV 2026</span>
    📝 <strong>Under Review</strong> — <em>"Bridging Visual Representation and Reinforcement Learning from Verifiable Rewards in LVLMs"</em> submitted to <strong>ECCV 2026</strong>.
  </li>
  <li class="reveal">
    <span class="t-badge">ICML 2026</span>
    📝 <strong>Under Review</strong> — <em>"Position: Shifting AI Efficiency from Model-Centric to Data-Centric Compression"</em> submitted to <strong>ICML 2026 Position Track</strong>.
  </li>
  <li class="reveal done">
    <span class="t-badge">CVPR 2026</span>
    🏆 <strong>Paper Accepted!</strong> <em>"Accelerating Streaming Video Understanding via Hierarchical Token Compression"</em> (<strong>STC</strong>) accepted to <strong>CVPR 2026</strong>.
  </li>
  <li class="reveal done">
    <span class="t-badge">CVPR 2026</span>
    🏆 <strong>Paper Accepted!</strong> <em>"Variation-aware Vision Token Dropping for Faster LVLMs"</em> (<strong>V2Drop</strong>) accepted to <strong>CVPR 2026</strong>.
  </li>
  <li class="reveal done">
    <span class="t-badge">EMNLP 2025</span>
    🏆 <strong>Paper Accepted!</strong> <em>"Video Compression Commander"</em> (<strong>VidCom²</strong>) accepted to <strong>EMNLP 2025 Main Conference</strong>.
  </li>
  <li class="reveal">
    <span class="t-badge">arXiv 2025</span>
    📄 <strong>Tech Report</strong> — <em>"AI for Service: Proactive Assistance with AI Glasses"</em> (<strong>Alpha-Service</strong>) released on <strong>arXiv</strong>.
  </li>
</ul>

<div class="divider"></div>

<!-- ===== Publications ===== -->
<h2 class="sec-title reveal"><span class="s-icon">📝</span> Publications</h2>

<p class="note">* denotes equal contribution, † denotes corresponding author.</p>

<h3 class="sub-h reveal"><span class="dot" style="background:#10b981; color:#10b981;"></span> Accepted <span class="count">3</span></h3>

<div class="p-card reveal">
  <h4><a href="#">Accelerating Streaming Video Understanding via Hierarchical Token Compression</a></h4>
  <div class="p-authors"><strong>Yiyu Wang*</strong>, Xuyang Liu*†, Xiyan Gui, Xinying Lin, Boxue Yang, Chenfei Liao, Tailai Chen, Linfeng Zhang.</div>
  <div class="p-chip">CVPR 2026</div>
  <div class="p-desc">Proposed <strong>STC-Cacher</strong> and <strong>STC-Pruner</strong>, the first plug-and-play token compression framework specifically designed for real-time streaming video understanding, enabling efficient infinite-length video stream processing.</div>
  <div class="p-links">
    <a href="#"><img src="https://img.shields.io/badge/Paper-Coming_Soon-B31B1B?style=flat&logo=arxiv" alt="Paper"></a>
    <a href="#"><img src="https://img.shields.io/badge/Code-Coming_Soon-181717?style=flat&logo=github" alt="Code"></a>
  </div>
</div>

<div class="p-card reveal">
  <h4><a href="https://arxiv.org/abs/2509.01552">Variation-aware Vision Token Dropping for Faster Large Vision-Language Models</a></h4>
  <div class="p-authors">Junjie Chen, Xuyang Liu, Zichen Wen, <strong>Yiyu Wang</strong>, Siteng Huang, Honggang Chen.</div>
  <div class="p-chip">CVPR 2026</div>
  <div class="p-desc">Leveraged variation-aware token dropping to exploit inherent visual sparsity, accelerating large vision-language models with minimal quality degradation.</div>
  <div class="p-links">
    <a href="https://arxiv.org/abs/2509.01552"><img src="https://img.shields.io/badge/Paper-arXiv-B31B1B?style=flat&logo=arxiv" alt="Paper"></a>
    <a href="https://github.com/xuyang-liu16/V2Drop"><img src="https://img.shields.io/badge/Code-GitHub-181717?style=flat&logo=github" alt="Code"></a>
  </div>
</div>

<div class="p-card reveal">
  <h4><a href="https://aclanthology.org/2025.emnlp-main.98/">Video Compression Commander: Plug-and-Play Inference Acceleration for Video Large Language Models</a></h4>
  <div class="p-authors">Xuyang Liu*, <strong>Yiyu Wang*</strong>, Junpeng Ma, Linfeng Zhang.</div>
  <div class="p-chip">EMNLP 2025 Main</div>
  <div class="p-desc">Proposed <strong>VidCom²</strong>, a training-free framework that adaptively compresses video tokens based on frame uniqueness. Achieved <strong>99.6%</strong> performance retention with only <strong>25% tokens</strong> and <strong>70.8%</strong> latency reduction.</div>
  <div class="p-links">
    <a href="https://aclanthology.org/2025.emnlp-main.98/"><img src="https://img.shields.io/badge/Paper-EMNLP'25-db545a?style=flat&logo=semanticscholar" alt="Paper"></a>
    <a href="https://github.com/xuyang-liu16/VidCom2"><img src="https://img.shields.io/badge/Code-GitHub-181717?style=flat&logo=github" alt="Code"></a>
  </div>
</div>

<h3 class="sub-h reveal"><span class="dot" style="background:#f59e0b; color:#f59e0b;"></span> Under Review <span class="count">4</span></h3>

<div class="p-card reveal">
  <h4><a href="#">Are We Using the Right Benchmark: An Evaluation Framework for Visual Token Compression Methods</a></h4>
  <div class="p-authors">Chenfei Liao, Wensong Wang, Zichen Wen, Xu Zheng, <strong>Yiyu Wang</strong>, Haocong He, Yuanhuiyi Lyu, Lutao Jiang, Xin Zou, Yuqian Fu, Bin Ren, Linfeng Zhang, Xuming Hu.</div>
  <div class="p-chip">ACL 2026 (Under Review)</div>
  <div class="p-desc">Built a more revealing evaluation framework for visual token compression methods and investigated whether current benchmarks truly measure the efficiency-quality trade-off.</div>
  <div class="p-links"><a href="#"><img src="https://img.shields.io/badge/Paper-Coming_Soon-B31B1B?style=flat&logo=arxiv" alt="Paper"></a></div>
</div>

<div class="p-card reveal">
  <h4><a href="#">V-CAST: Video Curvature-Aware Spatio-Temporal Pruning for Efficient Video Large Language Models</a></h4>
  <div class="p-authors">Xinying Lin, Xuyang Liu, <strong>Yiyu Wang</strong>, Teng Ma, Wenqi Ren.</div>
  <div class="p-chip">ECCV 2026 (Under Review)</div>
  <div class="p-desc">Proposed curvature-aware spatio-temporal pruning for efficient video LLMs, exploiting geometric curvature signals to selectively prune redundant video tokens in both spatial and temporal dimensions.</div>
  <div class="p-links"><a href="#"><img src="https://img.shields.io/badge/Paper-Coming_Soon-B31B1B?style=flat&logo=arxiv" alt="Paper"></a></div>
</div>

<div class="p-card reveal">
  <h4><a href="#">Bridging Visual Representation and Reinforcement Learning from Verifiable Rewards in Large Vision-Language Models</a></h4>
  <div class="p-authors">Yuhang Han, Yuyang Wu, Zhengbo Jiao, <strong>Yiyu Wang</strong>, Xuyang Liu, Shaobo Wang, Hanlin Xu, Xuming Hu, Linfeng Zhang.</div>
  <div class="p-chip">ECCV 2026 (Under Review)</div>
  <div class="p-desc">Bridged visual representation learning with reinforcement learning from verifiable rewards (RLVR) in large vision-language models, enabling more grounded visual understanding through reward-driven optimization.</div>
  <div class="p-links"><a href="#"><img src="https://img.shields.io/badge/Paper-Coming_Soon-B31B1B?style=flat&logo=arxiv" alt="Paper"></a></div>
</div>

<div class="p-card reveal">
  <h4><a href="https://arxiv.org/abs/2505.19147">Position: Shifting AI Efficiency from Model-Centric to Data-Centric Compression</a></h4>
  <div class="p-authors">Xuyang Liu, Zichen Wen, Shaobo Wang, Junjie Chen, Zhishan Tao, Yubo Wang, Tailai Chen, Xiangqi Jin, Chang Zou, <strong>Yiyu Wang</strong>, Chenfei Liao, Xu Zheng, Honggang Chen, Weijia Li, Xuming Hu, Conghui He, Linfeng Zhang.</div>
  <div class="p-chip">ICML 2026 Position Track (Under Review)</div>
  <div class="p-desc">A position paper arguing that AI efficiency research should shift focus from model-centric compression to data-centric compression, establishing a unified framework for existing efficiency strategies.</div>
  <div class="p-links"><a href="https://arxiv.org/abs/2505.19147"><img src="https://img.shields.io/badge/Paper-arXiv-B31B1B?style=flat&logo=arxiv" alt="Paper"></a></div>
</div>

<h3 class="sub-h reveal"><span class="dot" style="background:#ef4444; color:#ef4444;"></span> Technical Report <span class="count">1</span></h3>

<div class="p-card reveal">
  <h4><a href="https://arxiv.org/abs/2510.14359">AI for Service: Proactive Assistance with AI Glasses</a></h4>
  <div class="p-authors">Zichen Wen, <strong>Yiyu Wang</strong>, Chenfei Liao, Boxue Yang, Junxian Li, Weifeng Liu, Haocong He, Bolong Feng, Xuyang Liu, Yuanhuiyi Lyu, Xu Zheng, Xuming Hu, Linfeng Zhang.</div>
  <div class="p-chip">arXiv 2025 (Tech Report)</div>
  <div class="p-desc">Proposed <strong>Alpha-Service</strong>, a unified framework for proactive AI assistance via AI glasses. Inspired by von Neumann architecture, it addresses "when to help" and "how to help" through five functional units — perception, scheduling, tool utilization, long-term memory, and natural interaction.</div>
  <div class="p-links"><a href="https://arxiv.org/abs/2510.14359"><img src="https://img.shields.io/badge/Paper-arXiv-B31B1B?style=flat&logo=arxiv" alt="Paper"></a></div>
</div>

<div class="divider"></div>

<!-- ===== Projects ===== -->
<h2 class="sec-title reveal"><span class="s-icon">💻</span> Selected Projects</h2>

<div class="proj-grid">
  <div class="proj-card reveal">
    <span class="proj-tag">CVPR 2026</span>
    <h4>STC</h4>
    <p>A streaming-first token compression framework with caching and pruning for real-time video understanding.</p>
    <a href="#" class="plink">Code Coming Soon <span class="arrow">&rarr;</span></a>
  </div>
  <div class="proj-card reveal">
    <span class="proj-tag">EMNLP 2025</span>
    <h4>VidCom²</h4>
    <p>Plug-and-play inference acceleration for VideoLLMs via adaptive frame-uniqueness-based token compression.</p>
    <a href="https://github.com/xuyang-liu16/VidCom2" class="plink">Open Project <span class="arrow">&rarr;</span></a>
  </div>
</div>

<div class="divider"></div>

<!-- ===== Academic Service ===== -->
<h2 class="sec-title reveal"><span class="s-icon">🎓</span> Academic Service</h2>

<div class="svc-card reveal">
  <div class="svc-icon">✍️</div>
  <div>
    <strong>Conference Reviewer</strong>
    <div class="v-tags">
      <span class="v-tag">CVPR</span>
      <span class="v-tag">ECCV</span>
      <span class="v-tag">ACM MM</span>
      <span class="v-tag">EMNLP</span>
    </div>
  </div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  // Scroll reveal
  var reveals = document.querySelectorAll('.reveal');
  reveals.forEach(function(el) { el.classList.add('will-anim'); });
  var observer = new IntersectionObserver(function(entries) {
    entries.forEach(function(entry) {
      if (entry.isIntersecting) {
        var siblings = entry.target.parentElement.querySelectorAll('.reveal');
        var idx = Array.from(siblings).indexOf(entry.target);
        entry.target.style.transitionDelay = Math.min(idx * 0.08, 0.4) + 's';
        entry.target.classList.add('visible');
      }
    });
  }, { threshold: 0.06, rootMargin: '0px 0px -20px 0px' });
  reveals.forEach(function(el) { observer.observe(el); });

  // Counter animation
  var statsRow = document.getElementById('stats-row');
  if (statsRow) {
    var co = new IntersectionObserver(function(entries) {
      entries.forEach(function(entry) {
        if (entry.isIntersecting) {
          var counters = entry.target.querySelectorAll('.stat-num[data-target]');
          counters.forEach(function(el) {
            if (el.dataset.animated) return;
            el.dataset.animated = 'true';
            var target = parseInt(el.dataset.target);
            var duration = 1600;
            var start = performance.now();
            function step(now) {
              var progress = Math.min((now - start) / duration, 1);
              var eased = 1 - Math.pow(1 - progress, 4);
              el.textContent = Math.round(eased * target);
              if (progress < 1) requestAnimationFrame(step);
            }
            requestAnimationFrame(step);
          });
        }
      });
    }, { threshold: 0.3 });
    co.observe(statsRow);
  }
});
</script>
