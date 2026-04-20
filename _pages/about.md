---
permalink: /
title: "Yiyu Wang"
excerpt: "Joint Ph.D. Student at HKUST(GZ) & SJTU · Streaming Video Understanding"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

<style>
/* ===== Premium Academic Design v7 ===== */

/* Hide duplicate Jekyll page title */
.page__title { display: none !important; }

/* Premium page background */
#main {
  background: linear-gradient(180deg, #eef1f5 0%, #f5f7fa 25%, #f8f9fb 75%, #eef1f5 100%) !important;
}

/* --- Base Card (Apple-style multi-layer shadow) --- */
.p-card {
  background: #ffffff;
  border-radius: 20px;
  border: 1px solid rgba(0,0,0,0.04);
  box-shadow:
    0 0 0 1px rgba(0,0,0,0.02),
    0 1px 3px rgba(0,0,0,0.04),
    0 4px 12px rgba(0,0,0,0.03),
    0 12px 32px rgba(0,0,0,0.02);
  transition: all 0.5s cubic-bezier(0.16, 1, 0.3, 1);
  position: relative;
  overflow: hidden;
}
.p-card:hover {
  box-shadow:
    0 0 0 1px rgba(0,0,0,0.03),
    0 2px 8px rgba(0,0,0,0.05),
    0 8px 24px rgba(0,0,0,0.04),
    0 24px 48px rgba(0,0,0,0.03);
  transform: translateY(-6px);
}

/* --- Hero --- */
.hero-card {
  padding: 48px 44px 42px;
  margin-bottom: 32px;
  background: linear-gradient(135deg, #ffffff 0%, #fafbfc 100%);
}
.hero-card::before {
  content: ''; position: absolute; top: 0; left: 0; right: 0; height: 5px;
  background: linear-gradient(90deg, #1a3a5c, #3a7bc8, #60a5fa);
  border-radius: 20px 20px 0 0;
}
.hero-card::after {
  content: ''; position: absolute; top: -60px; right: -60px;
  width: 200px; height: 200px;
  background: radial-gradient(circle, rgba(58,123,200,0.06) 0%, transparent 70%);
  border-radius: 50%; pointer-events: none;
}
.hero-name {
  font-size: 2.8em; font-weight: 900; color: #0f172a;
  letter-spacing: -0.04em; line-height: 1.1; margin: 0 0 10px;
  position: relative; z-index: 1;
}
.hero-name .wave { font-size: 0.7em; margin-left: 4px; }
.hero-tagline {
  font-size: 1.15em; color: #3a7bc8; font-weight: 600;
  margin: 0 0 18px; position: relative; z-index: 1;
  letter-spacing: -0.01em;
}
.hero-bio {
  font-size: 0.96em; color: #475569; line-height: 1.85;
  max-width: 700px; position: relative; z-index: 1;
}
.hero-bio a {
  color: #1a3a5c; text-decoration: none; font-weight: 600;
  background-image: linear-gradient(transparent 85%, rgba(26,58,92,0.15) 85%);
  background-repeat: no-repeat; background-size: 100% 100%;
  transition: background-size 0.3s, color 0.2s;
}
.hero-bio a:hover { color: #2563eb; background-image: linear-gradient(transparent 82%, rgba(37,99,235,0.2) 82%); }

.hero-pills {
  display: flex; flex-wrap: wrap; gap: 8px;
  margin-top: 20px; position: relative; z-index: 1;
}
.hero-pill {
  display: inline-flex; align-items: center; gap: 5px;
  padding: 6px 16px; border-radius: 100px;
  font-size: 0.8em; font-weight: 600; color: #fff;
  background: linear-gradient(135deg, #1a3a5c, #3a7bc8);
  box-shadow: 0 3px 10px rgba(26,58,92,0.2);
  transition: all 0.3s cubic-bezier(0.34,1.56,0.64,1);
}
.hero-pill:hover {
  transform: translateY(-3px) scale(1.05);
  box-shadow: 0 6px 18px rgba(26,58,92,0.3);
}
.hero-pill.hp-sjtu { background: linear-gradient(135deg, #0056a3, #1976d2); }
.hero-pill.hp-tencent { background: linear-gradient(135deg, #00a4ef, #0288d1); }
.hero-pill.hp-streaming { background: linear-gradient(135deg, #c62828, #ef5350); }
.hero-pill.hp-efficiency { background: linear-gradient(135deg, #2e7d32, #43a047); }

/* --- Research Pills --- */
.research-row {
  display: flex; flex-wrap: wrap; gap: 16px;
  margin-bottom: 32px;
}
.r-pill {
  flex: 1; min-width: 190px;
  display: flex; align-items: center; gap: 16px;
  padding: 22px 24px; border-radius: 18px;
  cursor: default;
}
.r-pill .r-icon-wrap {
  width: 52px; height: 52px; border-radius: 16px;
  display: flex; align-items: center; justify-content: center;
  font-size: 1.5em; flex-shrink: 0;
  transition: transform 0.4s cubic-bezier(0.34,1.56,0.64,1);
}
.r-pill:hover .r-icon-wrap { transform: scale(1.15) rotate(-6deg); }
.r-pill .r-text { flex: 1; }
.r-pill .r-text strong { display: block; font-size: 0.98em; margin-bottom: 3px; color: #0f172a; }
.r-pill .r-text span { font-size: 0.8em; color: #64748b; font-weight: 400; }

.rp-streaming .r-icon-wrap { background: linear-gradient(135deg, #fee2e2, #fecaca); color: #dc2626; }
.rp-compression .r-icon-wrap { background: linear-gradient(135deg, #dbeafe, #bfdbfe); color: #2563eb; }
.rp-datacentric .r-icon-wrap { background: linear-gradient(135deg, #dcfce7, #bbf7d0); color: #16a34a; }

/* --- Stats --- */
.stats-row {
  display: grid; grid-template-columns: repeat(3, 1fr);
  gap: 18px; margin-bottom: 32px;
}
.stat-card {
  text-align: center; padding: 32px 20px 28px;
}
.stat-card .stat-icon-wrap {
  width: 56px; height: 56px; border-radius: 16px;
  display: flex; align-items: center; justify-content: center;
  margin: 0 auto 14px;
  font-size: 1.5em;
  box-shadow: 0 4px 12px rgba(0,0,0,0.08);
}
.stat-card:nth-child(1) .stat-icon-wrap { background: linear-gradient(135deg, #dbeafe, #bfdbfe); }
.stat-card:nth-child(2) .stat-icon-wrap { background: linear-gradient(135deg, #dcfce7, #bbf7d0); }
.stat-card:nth-child(3) .stat-icon-wrap { background: linear-gradient(135deg, #ffedd5, #fed7aa); }

.stat-num {
  font-size: 2.8em; font-weight: 900; color: #0f172a;
  display: block; letter-spacing: -0.04em; line-height: 1;
  font-family: 'JetBrains Mono', 'Fira Code', monospace;
}
.stat-label {
  font-size: 0.72em; color: #94a3b8; text-transform: uppercase;
  letter-spacing: 0.18em; font-weight: 700; margin-top: 10px; display: block;
}

/* --- Section Title --- */
.sec-title {
  font-size: 1.5em; font-weight: 800; color: #0f172a;
  margin: 40px 0 24px;
  letter-spacing: -0.03em;
  display: flex; align-items: center; gap: 12px;
}
.sec-title .sec-icon {
  width: 40px; height: 40px; border-radius: 12px;
  background: linear-gradient(135deg, #1a3a5c, #3a7bc8);
  color: #fff;
  display: inline-flex; align-items: center; justify-content: center;
  font-size: 1.1em;
  box-shadow: 0 4px 14px rgba(26,58,92,0.25);
}
.sec-title::after {
  content: ''; flex: 1; height: 2px;
  background: linear-gradient(90deg, rgba(26,58,92,0.1) 0%, transparent 100%);
  border-radius: 1px;
}

/* --- Divider --- */
.divider {
  height: 1px; border: none; margin: 40px 0;
  background: linear-gradient(90deg, transparent, rgba(0,0,0,0.06) 20%, rgba(0,0,0,0.06) 80%, transparent);
}

/* --- Timeline News --- */
.timeline-wrap {
  position: relative; padding-left: 36px;
}
.timeline-wrap::before {
  content: ''; position: absolute;
  top: 8px; bottom: 8px; left: 11px;
  width: 3px;
  background: linear-gradient(180deg, #1a3a5c 0%, #3a7bc8 50%, rgba(26,58,92,0.08) 100%);
  border-radius: 3px;
}
.tl-item {
  position: relative;
  padding: 16px 20px;
  margin-bottom: 12px;
  font-size: 0.9em; color: #475569;
  line-height: 1.65;
  transition: all 0.35s cubic-bezier(0.34,1.56,0.64,1);
}
.tl-item:hover {
  transform: translateX(8px);
  box-shadow:
    0 0 0 1px rgba(0,0,0,0.03),
    0 4px 16px rgba(0,0,0,0.06);
}
.tl-item::before {
  content: ''; position: absolute;
  left: -32px; top: 22px;
  width: 14px; height: 14px; border-radius: 50%;
  background: #fff; border: 3px solid #3a7bc8;
  box-shadow: 0 0 0 5px rgba(58,123,200,0.1);
  z-index: 1; transition: all 0.3s cubic-bezier(0.34,1.56,0.64,1);
}
.tl-item:hover::before {
  background: #1a3a5c; border-color: #1a3a5c;
  box-shadow: 0 0 0 8px rgba(26,58,92,0.12);
  transform: scale(1.3);
}
.tl-item.accepted::before { border-color: #16a34a; background: #f0fdf4; }
.tl-item.accepted:hover::before { background: #16a34a; border-color: #16a34a; box-shadow: 0 0 0 8px rgba(22,163,74,0.15); }
.tl-item em { color: #334155; font-style: normal; font-weight: 500; }
.tl-item strong { color: #0f172a; }

.tl-badge {
  display: inline-block; padding: 4px 12px; border-radius: 100px;
  font-weight: 700; font-size: 0.72em; color: #fff;
  margin-right: 8px; vertical-align: middle;
  letter-spacing: 0.04em;
  box-shadow: 0 2px 8px rgba(0,0,0,0.12);
}
.tl-cvpr { background: linear-gradient(135deg, #dc2626, #ef4444); }
.tl-emnlp { background: linear-gradient(135deg, #be185d, #ec4899); }
.tl-eccv { background: linear-gradient(135deg, #1d4ed8, #3b82f6); }
.tl-icml { background: linear-gradient(135deg, #7c3aed, #a855f7); }
.tl-acl { background: linear-gradient(135deg, #15803d, #22c55e); }
.tl-arxiv { background: linear-gradient(135deg, #c2410c, #f97316); }

/* --- Sub Heading --- */
.sub-h {
  font-size: 1.1em; font-weight: 700; color: #0f172a;
  margin: 28px 0 18px; display: flex; align-items: center; gap: 10px;
}
.sub-h .dot {
  width: 10px; height: 10px; border-radius: 50%;
  flex-shrink: 0; position: relative;
}
.sub-h .dot::after {
  content: ''; position: absolute; inset: -4px;
  border-radius: 50%; border: 1.5px solid currentColor;
  opacity: 0.25;
  animation: dotPulse 2.5s ease-in-out infinite;
}
@keyframes dotPulse {
  0%,100% { transform: scale(1); opacity: 0.25; }
  50% { transform: scale(1.5); opacity: 0; }
}
.sub-h .count {
  font-size: 0.72em; font-weight: 700; color: #fff;
  padding: 3px 10px; border-radius: 100px;
  font-family: 'JetBrains Mono', 'Fira Code', monospace;
  letter-spacing: 0.03em;
}

/* --- Paper Card --- */
.paper-card {
  padding: 28px 32px;
  margin-bottom: 18px;
}
.paper-card::before {
  content: ''; position: absolute;
  top: 0; left: 0; right: 0; height: 4px;
  background: var(--accent, #1a3a5c);
  border-radius: 20px 20px 0 0;
}
.paper-card h4 { margin: 0 0 10px; font-size: 1.08em; line-height: 1.45; font-weight: 700; color: #0f172a; }
.paper-card h4 a { color: inherit; text-decoration: none; border-bottom: none; transition: color 0.2s; }
.paper-card h4 a:hover { color: #2563eb; }

.p-authors { font-size: 0.85em; color: #64748b; margin-bottom: 10px; line-height: 1.6; }
.p-authors strong { color: #334155; font-weight: 600; }

.v-badge {
  display: inline-flex; align-items: center; gap: 5px;
  padding: 5px 14px; border-radius: 100px;
  font-weight: 700; font-size: 0.74em; letter-spacing: 0.03em;
  margin-bottom: 12px;
  color: var(--accent, #1a3a5c);
  background: var(--accent-bg, rgba(26,58,92,0.05));
  border: 1px solid var(--accent-border, rgba(26,58,92,0.1));
}

.p-desc { font-size: 0.88em; color: #64748b; line-height: 1.75; margin-bottom: 16px; }
.p-desc strong { color: #334155; font-weight: 600; }

.p-links { display: flex; flex-wrap: wrap; gap: 8px; align-items: center; }
.p-links a { text-decoration: none; margin-right: 0; border-bottom: none; display: inline-block; }
.p-links img {
  height: 24px; border-radius: 5px;
  transition: transform 0.3s cubic-bezier(0.34,1.56,0.64,1), box-shadow 0.2s;
}
.p-links img:hover { transform: translateY(-3px) scale(1.05); box-shadow: 0 6px 16px rgba(0,0,0,0.12); }

/* First Author */
.fa-corner {
  position: absolute; top: 16px; right: 16px;
  display: inline-flex; align-items: center; gap: 4px;
  padding: 4px 12px; border-radius: 100px;
  font-size: 0.68em; font-weight: 700;
  color: #b45309;
  background: linear-gradient(135deg, #fef3c7, #fde68a);
  border: 1px solid #fcd34d;
  box-shadow: 0 2px 8px rgba(217,119,6,0.12);
  z-index: 2;
}

/* Cite Toggle */
.cite-toggle {
  display: inline-flex; align-items: center; gap: 4px;
  padding: 5px 14px; border-radius: 8px;
  font-size: 0.8em; font-weight: 600;
  color: #475569; background: rgba(0,0,0,0.03);
  border: 1px solid rgba(0,0,0,0.06);
  cursor: pointer; transition: all 0.2s;
  margin-left: 2px;
}
.cite-toggle:hover {
  background: #0f172a; color: #fff;
  border-color: #0f172a;
}
.cite-toggle.active {
  background: #0f172a; color: #fff;
}

/* Cite Panel */
.cite-panel {
  max-height: 0; overflow: hidden; opacity: 0;
  transition: max-height 0.5s cubic-bezier(0.16,1,0.3,1), opacity 0.35s ease, margin 0.35s ease;
  margin-top: 0;
}
.cite-panel.open {
  max-height: 600px; opacity: 1; margin-top: 16px;
}
.cite-panel-inner {
  background: #f8fafc;
  border-radius: 14px;
  padding: 16px 20px;
  border: 1px solid rgba(0,0,0,0.04);
}
.cite-row { margin-bottom: 14px; }
.cite-row:last-child { margin-bottom: 0; }
.cite-row-label {
  font-size: 0.7em; font-weight: 700; color: #0f172a;
  text-transform: uppercase; letter-spacing: 0.1em;
  margin-bottom: 8px; display: flex; align-items: center; gap: 6px;
  justify-content: space-between;
}
.cite-row-label button {
  background: #fff;
  border: 1px solid rgba(0,0,0,0.08);
  border-radius: 6px; padding: 4px 12px;
  font-size: 0.85em; font-weight: 600; color: #334155;
  cursor: pointer; transition: all 0.2s;
}
.cite-row-label button:hover { background: #0f172a; color: #fff; }
.cite-row-label button.copied { background: #16a34a; color: #fff; border-color: #16a34a; }
.cite-text, .cite-pre {
  font-family: 'JetBrains Mono', 'Fira Code', monospace;
  font-size: 0.78em; line-height: 1.6; color: #475569;
}
.cite-pre { margin: 0; white-space: pre-wrap; word-break: break-word; }

.note-text { font-size: 0.84em; color: #94a3b8; margin-bottom: 18px; font-style: italic; }
.note-text a { color: #3a7bc8; font-weight: 600; text-decoration: none; }
.note-text a:hover { text-decoration: underline; }

/* View All Button */
.view-all-box { text-align: center; margin: 28px 0 8px; }
.view-all-btn {
  display: inline-flex; align-items: center; gap: 10px;
  padding: 14px 32px; border-radius: 16px;
  font-size: 0.95em; font-weight: 700;
  color: #0f172a; background: #ffffff;
  border: 1px solid rgba(0,0,0,0.06);
  box-shadow:
    0 0 0 1px rgba(0,0,0,0.02),
    0 2px 8px rgba(0,0,0,0.04),
    0 8px 24px rgba(0,0,0,0.03);
  text-decoration: none; transition: all 0.4s cubic-bezier(0.16,1,0.3,1);
}
.view-all-btn:hover {
  transform: translateY(-4px);
  box-shadow:
    0 0 0 1px rgba(0,0,0,0.03),
    0 4px 12px rgba(0,0,0,0.06),
    0 16px 40px rgba(0,0,0,0.05);
  background: #0f172a; color: #fff;
}

/* --- Service Card --- */
.svc-card {
  padding: 24px 28px;
  display: flex; align-items: center; gap: 18px;
  font-size: 0.94em; color: #475569; line-height: 1.7;
}
.svc-card .svc-icon {
  width: 48px; height: 48px; border-radius: 14px;
  background: linear-gradient(135deg, #1a3a5c, #3a7bc8);
  display: flex; align-items: center; justify-content: center;
  font-size: 1.3em; flex-shrink: 0;
  box-shadow: 0 6px 18px rgba(26,58,92,0.25);
  color: #fff;
}
.svc-card strong { color: #0f172a; }
.v-tags { display: flex; flex-wrap: wrap; gap: 6px; margin-top: 10px; }
.v-tag {
  font-size: 0.74em; padding: 3px 12px; border-radius: 6px;
  font-weight: 600; letter-spacing: 0.03em;
  background: rgba(26,58,92,0.05); color: #334155;
  transition: all 0.25s;
}
.v-tag:hover { background: #0f172a; color: #fff; }

/* --- Scroll Reveal --- */
.reveal {
  opacity: 1; transform: translateY(0) scale(1);
}
.reveal.will-anim {
  opacity: 0; transform: translateY(40px) scale(0.97);
  transition: opacity 1s cubic-bezier(0.16,1,0.3,1), transform 1s cubic-bezier(0.16,1,0.3,1);
}
.reveal.will-anim.visible { opacity: 1; transform: translateY(0) scale(1); }

/* --- Responsive --- */
@media (max-width: 768px) {
  .hero-card { padding: 32px 24px 28px; }
  .hero-name { font-size: 2em; }
  .stats-row { gap: 12px; }
  .stat-card { padding: 24px 14px 20px; }
  .stat-num { font-size: 2.2em; }
  .research-row { gap: 12px; }
  .r-pill { padding: 16px 18px; min-width: 150px; }
  .timeline-wrap { padding-left: 30px; }
  .paper-card { padding: 22px 24px; }
  .fa-corner { display: none; }
}
@media (max-width: 480px) {
  .research-row { flex-direction: column; }
  .r-pill { min-width: 100%; }
  .stats-row { grid-template-columns: 1fr; }
}
</style>

<!-- ===== Hero ===== -->
<div class="hero-card p-card reveal">
  <div class="hero-name">Yiyu Wang <span class="wave">👋</span></div>
  <div class="hero-tagline">王一宇 · Joint Ph.D. @ HKUST(GZ) &amp; SJTU</div>
  <div class="hero-bio">
    I am a <strong>joint Ph.D. student</strong> at <a href="https://www.hkust-gz.edu.cn/">HKUST(GZ)</a> and <a href="https://www.sjtu.edu.cn/">SJTU</a>, advised by <a href="https://xuminghu.github.io/">Prof. Xuming Hu</a> and <a href="https://linfeng-zhang.github.io/">Prof. Linfeng Zhang</a>. Currently a <strong>Research Intern at <a href="https://www.tencent.com/">Tencent</a></strong>.
    <br><br>
    My research focuses on <strong>Streaming Video Understanding</strong> — building systems that perceive, reason, and act under real-time constraints with tight token budgets and precise temporal grounding.
  </div>
  <div class="hero-pills">
    <span class="hero-pill">🏫 HKUST(GZ)</span>
    <span class="hero-pill hp-sjtu">🏫 SJTU</span>
    <span class="hero-pill hp-tencent">💼 Tencent</span>
    <span class="hero-pill hp-streaming">🎥 Streaming</span>
    <span class="hero-pill hp-efficiency">⚡ Efficient VideoLLM</span>
  </div>
</div>

<!-- ===== Research Highlights ===== -->
<div class="research-row reveal">
  <div class="r-pill rp-streaming p-card">
    <div class="r-icon-wrap">📡</div>
    <div class="r-text">
      <strong>Streaming Video</strong>
      <span>Real-time perception &amp; reasoning</span>
    </div>
  </div>
  <div class="r-pill rp-compression p-card">
    <div class="r-icon-wrap">⚡</div>
    <div class="r-text">
      <strong>Token Compression</strong>
      <span>Efficient visual encoding</span>
    </div>
  </div>
  <div class="r-pill rp-datacentric p-card">
    <div class="r-icon-wrap">📊</div>
    <div class="r-text">
      <strong>Data-Centric AI</strong>
      <span>Quality over quantity</span>
    </div>
  </div>
</div>

<!-- ===== Stats ===== -->
<div class="stats-row reveal" id="stats-row">
  <div class="stat-card p-card">
    <div class="stat-icon-wrap">📄</div>
    <span class="stat-num" data-target="8">0</span>
    <span class="stat-label">Papers</span>
  </div>
  <div class="stat-card p-card">
    <div class="stat-icon-wrap">✅</div>
    <span class="stat-num" data-target="3">0</span>
    <span class="stat-label">Accepted</span>
  </div>
  <div class="stat-card p-card">
    <div class="stat-icon-wrap">📝</div>
    <span class="stat-num" data-target="4">0</span>
    <span class="stat-label">Under Review</span>
  </div>
</div>

<div class="divider"></div>

<!-- ===== News ===== -->
<h2 class="sec-title reveal"><span class="sec-icon">🔥</span> News &amp; Updates</h2>

<div class="timeline-wrap reveal">
  <div class="tl-item p-card">
    <span class="tl-badge tl-acl">ACL 2026</span>
    📝 <strong>Under Review</strong> — <em>VTC-Bench</em> submitted to <strong>ACL 2026</strong>.
  </div>
  <div class="tl-item p-card">
    <span class="tl-badge tl-eccv">ECCV 2026</span>
    📝 <strong>Under Review</strong> — <em>V-CAST</em> submitted to <strong>ECCV 2026</strong>.
  </div>
  <div class="tl-item p-card accepted">
    <span class="tl-badge tl-cvpr">CVPR 2026</span>
    🏆 <strong>Accepted</strong> — <em>STC</em> accepted to <strong>CVPR 2026</strong>.
  </div>
  <div class="tl-item p-card accepted">
    <span class="tl-badge tl-emnlp">EMNLP 2025</span>
    🏆 <strong>Accepted</strong> — <em>VidCom²</em> accepted to <strong>EMNLP 2025</strong>.
  </div>
</div>

<div class="divider"></div>

<!-- ===== Publications ===== -->
<h2 class="sec-title reveal"><span class="sec-icon">📝</span> Publications</h2>

<p class="note-text">* denotes equal contribution, † denotes corresponding author. <a href="/publications/">View full list →</a></p>

<h3 class="sub-h reveal"><span class="dot" style="background:#16a34a; color:#16a34a;"></span> Accepted <span class="count" style="background: linear-gradient(135deg, #16a34a, #22c55e);">3</span></h3>

<!-- STC -->
<div class="paper-card p-card reveal" style="--accent: #dc2626; --accent-bg: rgba(220,38,38,0.06); --accent-border: rgba(220,38,38,0.12);">
  <span class="fa-corner">⭐ First Author</span>
  <h4><a href="https://arxiv.org/abs/2512.00891">Accelerating Streaming Video Large Language Models via Hierarchical Token Compression</a></h4>
  <div class="p-authors"><strong>Yiyu Wang</strong>, Xuyang Liu, Xiyan Gui, Xinying Lin, Boxue Yang, Chenfei Liao, Tailai Chen, and Linfeng Zhang.</div>
  <div class="v-badge">CVPR 2026</div>
  <div class="p-desc">We propose <strong>Streaming Token Compression (STC)</strong>, the first plug-and-play hierarchical token compression framework for streaming VideoLLMs. Introduces <strong>STC-Cacher</strong> and <strong>STC-Pruner</strong>. Retains up to <strong>99%</strong> accuracy while reducing ViT encoding latency and LLM pre-filling latency by <strong>24.5%</strong> and <strong>45.3%</strong>.</div>
  <div class="p-links">
    <a href="https://arxiv.org/abs/2512.00891"><img src="https://img.shields.io/badge/Paper-arXiv-B31B1B?style=flat&logo=arxiv" alt="Paper"></a>
    <a href="https://github.com/lern-to-write/STC"><img src="https://img.shields.io/badge/Code-GitHub-181717?style=flat&logo=github" alt="Code"></a>
    <button class="cite-toggle" onclick="toggleCite('cite-stc',this)">📋 Cite</button>
  </div>
  <div class="cite-panel" id="panel-cite-stc">
    <div class="cite-panel-inner">
      <div class="cite-row">
        <div class="cite-row-label">📋 Citation <button onclick="copyCite('cite-stc',this)">Copy</button></div>
        <span id="cite-stc" class="cite-text">Yiyu Wang, Xuyang Liu, Xiyan Gui, Xinying Lin, Boxue Yang, Chenfei Liao, Tailai Chen, and Linfeng Zhang. (2026). "Accelerating Streaming Video Large Language Models via Hierarchical Token Compression." Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR).</span>
      </div>
      <div class="cite-row">
        <div class="cite-row-label">📝 BibTeX <button onclick="copyBib('bib-stc',this)">Copy</button></div>
        <pre id="bib-stc" class="cite-pre">@inproceedings{wang2026stc,
  title={Accelerating Streaming Video Large Language Models via Hierarchical Token Compression},
  author={Wang, Yiyu and Liu, Xuyang and Gui, Xiyan and Lin, Xinying and Yang, Boxue and Liao, Chenfei and Chen, Tailai and Zhang, Linfeng},
  booktitle={Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition},
  year={2026}
}</pre>
      </div>
    </div>
  </div>
</div>

<!-- V2Drop -->
<div class="paper-card p-card reveal" style="--accent: #dc2626; --accent-bg: rgba(220,38,38,0.06); --accent-border: rgba(220,38,38,0.12);">
  <h4><a href="https://arxiv.org/abs/2509.01552">Variation-aware Vision Token Dropping for Faster Large Vision-Language Models</a></h4>
  <div class="p-authors">Junjie Chen, Xuyang Liu, Zichen Wen, <strong>Yiyu Wang</strong>, Siteng Huang, and Honggang Chen.</div>
  <div class="v-badge">CVPR 2026</div>
  <div class="p-desc">We propose <strong>V2Drop</strong>, which progressively removes visual tokens with minimal variation during LVLM inference, maintaining <strong>94.0%</strong> and <strong>98.6%</strong> of original performance for image and video tasks respectively, while reducing LLM generation latency by <strong>31.5%</strong> and <strong>74.2%</strong>.</div>
  <div class="p-links">
    <a href="https://arxiv.org/abs/2509.01552"><img src="https://img.shields.io/badge/Paper-arXiv-B31B1B?style=flat&logo=arxiv" alt="Paper"></a>
    <a href="https://github.com/xuyang-liu16/V2Drop"><img src="https://img.shields.io/badge/Code-GitHub-181717?style=flat&logo=github" alt="Code"></a>
    <button class="cite-toggle" onclick="toggleCite('cite-v2drop',this)">📋 Cite</button>
  </div>
  <div class="cite-panel" id="panel-cite-v2drop">
    <div class="cite-panel-inner">
      <div class="cite-row">
        <div class="cite-row-label">📋 Citation <button onclick="copyCite('cite-v2drop',this)">Copy</button></div>
        <span id="cite-v2drop" class="cite-text">Junjie Chen, Xuyang Liu, Zichen Wen, Yiyu Wang, Siteng Huang, and Honggang Chen. (2026). "Variation-aware Vision Token Dropping for Faster Large Vision-Language Models." Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR).</span>
      </div>
      <div class="cite-row">
        <div class="cite-row-label">📝 BibTeX <button onclick="copyBib('bib-v2drop',this)">Copy</button></div>
        <pre id="bib-v2drop" class="cite-pre">@inproceedings{chen2026v2drop,
  title={Variation-aware Vision Token Dropping for Faster Large Vision-Language Models},
  author={Chen, Junjie and Liu, Xuyang and Wen, Zichen and Wang, Yiyu and Huang, Siteng and Chen, Honggang},
  booktitle={Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition},
  year={2026}
}</pre>
      </div>
    </div>
  </div>
</div>

<!-- VidCom2 -->
<div class="paper-card p-card reveal" style="--accent: #ea580c; --accent-bg: rgba(234,88,12,0.06); --accent-border: rgba(234,88,12,0.12);">
  <span class="fa-corner">⭐ First Author</span>
  <h4><a href="https://arxiv.org/abs/2505.14454">Video Compression Commander: Plug-and-Play Inference Acceleration for Video Large Language Models</a></h4>
  <div class="p-authors">Xuyang Liu*, <strong>Yiyu Wang*</strong>, Junpeng Ma, and Linfeng Zhang.</div>
  <div class="v-badge">EMNLP 2025 Main</div>
  <div class="p-desc">We propose <strong>VidCom²</strong>, a plug-and-play inference acceleration framework for VideoLLMs that adaptively adjusts compression intensity across frames. Achieved <strong>99.6%</strong> performance retention with only <strong>25% tokens</strong> and <strong>70.8%</strong> latency reduction.</div>
  <div class="p-links">
    <a href="https://arxiv.org/abs/2505.14454"><img src="https://img.shields.io/badge/Paper-arXiv-B31B1B?style=flat&logo=arxiv" alt="Paper"></a>
    <a href="https://github.com/xuyang-liu16/VidCom2"><img src="https://img.shields.io/badge/Code-GitHub-181717?style=flat&logo=github" alt="Code"></a>
    <button class="cite-toggle" onclick="toggleCite('cite-vidcom2',this)">📋 Cite</button>
  </div>
  <div class="cite-panel" id="panel-cite-vidcom2">
    <div class="cite-panel-inner">
      <div class="cite-row">
        <div class="cite-row-label">📋 Citation <button onclick="copyCite('cite-vidcom2',this)">Copy</button></div>
        <span id="cite-vidcom2" class="cite-text">Xuyang Liu, Yiyu Wang, Junpeng Ma, and Linfeng Zhang. (2025). "Video Compression Commander: Plug-and-Play Inference Acceleration for Video Large Language Models." Proceedings of the Conference on Empirical Methods in Natural Language Processing (EMNLP).</span>
      </div>
      <div class="cite-row">
        <div class="cite-row-label">📝 BibTeX <button onclick="copyBib('bib-vidcom2',this)">Copy</button></div>
        <pre id="bib-vidcom2" class="cite-pre">@inproceedings{liu2025vidcom2,
  title={Video Compression Commander: Plug-and-Play Inference Acceleration for Video Large Language Models},
  author={Liu, Xuyang and Wang, Yiyu and Ma, Junpeng and Zhang, Linfeng},
  booktitle={Proceedings of the Conference on Empirical Methods in Natural Language Processing},
  year={2025}
}</pre>
      </div>
    </div>
  </div>
</div>

<h3 class="sub-h reveal"><span class="dot" style="background:#f59e0b; color:#f59e0b;"></span> Under Review <span class="count" style="background: linear-gradient(135deg, #f59e0b, #fbbf24);">4</span></h3>

<!-- VTC-Bench -->
<div class="paper-card p-card reveal" style="--accent: #16a34a; --accent-bg: rgba(22,163,74,0.06); --accent-border: rgba(22,163,74,0.12);">
  <h4><a href="https://arxiv.org/abs/2510.07143">VTC-Bench: Are We Using the Right Benchmark? An Evaluation Framework for Visual Token Compression Methods</a></h4>
  <div class="p-authors">Chenfei Liao, Wensong Wang, Zichen Wen, Xu Zheng, <strong>Yiyu Wang</strong>, Haocong He, Yuanhuiyi Lyu, Lutao Jiang, Xin Zou, Yuqian Fu, Bin Ren, Linfeng Zhang, and Xuming Hu.</div>
  <div class="v-badge">ACL 2026 (Under Review)</div>
  <div class="p-desc">We propose <strong>VTC-Bench</strong>, the first comprehensive evaluation framework for visual token compression methods across image and video understanding tasks, revealing critical insights about current benchmarks.</div>
  <div class="p-links">
    <a href="https://arxiv.org/abs/2510.07143"><img src="https://img.shields.io/badge/Paper-arXiv-B31B1B?style=flat&logo=arxiv" alt="Paper"></a>
    <a href="https://github.com/Chenfei-Liao/VTC-Bench"><img src="https://img.shields.io/badge/Code-GitHub-181717?style=flat&logo=github" alt="Code"></a>
    <button class="cite-toggle" onclick="toggleCite('cite-vtc',this)">📋 Cite</button>
  </div>
  <div class="cite-panel" id="panel-cite-vtc">
    <div class="cite-panel-inner">
      <div class="cite-row">
        <div class="cite-row-label">📋 Citation <button onclick="copyCite('cite-vtc',this)">Copy</button></div>
        <span id="cite-vtc" class="cite-text">Chenfei Liao, Wensong Wang, Zichen Wen, Xu Zheng, Yiyu Wang, Haocong He, Yuanhuiyi Lyu, Lutao Jiang, Xin Zou, Yuqian Fu, Bin Ren, Linfeng Zhang, and Xuming Hu. (2026). "Are We Using the Right Benchmark: An Evaluation Framework for Visual Token Compression Methods." Proceedings of the Annual Meeting of the Association for Computational Linguistics (ACL).</span>
      </div>
      <div class="cite-row">
        <div class="cite-row-label">📝 BibTeX <button onclick="copyBib('bib-vtc',this)">Copy</button></div>
        <pre id="bib-vtc" class="cite-pre">@inproceedings{liao2026vtc,
  title={Are We Using the Right Benchmark: An Evaluation Framework for Visual Token Compression Methods},
  author={Liao, Chenfei and Wang, Wensong and Wen, Zichen and Zheng, Xu and Wang, Yiyu and He, Haocong and Lyu, Yuanhuiyi and Jiang, Lutao and Zou, Xin and Fu, Yuqian and Ren, Bin and Zhang, Linfeng and Hu, Xuming},
  booktitle={Proceedings of the Annual Meeting of the Association for Computational Linguistics},
  year={2026}
}</pre>
      </div>
    </div>
  </div>
</div>

<div class="view-all-box reveal">
  <a href="/publications/" class="view-all-btn">📚 View All 8 Publications <span style="font-size:1.2em;">→</span></a>
</div>

<div class="divider"></div>

<!-- ===== Academic Service ===== -->
<h2 class="sec-title reveal"><span class="sec-icon">🎓</span> Academic Service</h2>

<div class="svc-card p-card reveal">
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
function toggleCite(id, btn) {
  var panel = document.getElementById('panel-' + id);
  if (panel.classList.contains('open')) {
    panel.classList.remove('open');
    btn.classList.remove('active');
    btn.innerHTML = '📋 Cite';
  } else {
    document.querySelectorAll('.cite-panel.open').forEach(function(p) { p.classList.remove('open'); });
    document.querySelectorAll('.cite-toggle.active').forEach(function(b) { b.classList.remove('active'); b.innerHTML = '📋 Cite'; });
    panel.classList.add('open');
    btn.classList.add('active');
    btn.innerHTML = '📋 Close';
  }
}
function copyCite(id, btn) {
  var text = document.getElementById(id).textContent;
  navigator.clipboard.writeText(text).then(function() {
    btn.textContent = '✓ Copied'; btn.classList.add('copied');
    setTimeout(function() { btn.textContent = 'Copy'; btn.classList.remove('copied'); }, 2000);
  });
}
function copyBib(id, btn) {
  var text = document.getElementById(id).textContent;
  navigator.clipboard.writeText(text).then(function() {
    btn.textContent = '✓ Copied'; btn.classList.add('copied');
    setTimeout(function() { btn.textContent = 'Copy'; btn.classList.remove('copied'); }, 2000);
  });
}

document.addEventListener('DOMContentLoaded', function() {
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
            var duration = 1600, start = performance.now();
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
