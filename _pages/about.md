---
permalink: /
title: "Hi, I'm Yiyu Wang (王一宇) 👋"
excerpt: "Joint Ph.D. Student at HKUST(GZ) & SJTU · Streaming Video Understanding "
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

<style>
/* ===== Enhanced Academic Design System v3 ===== */

/* --- Glass Effect --- */
.glass-card {
  background: rgba(255,255,255,0.65);
  backdrop-filter: blur(20px) saturate(1.3);
  -webkit-backdrop-filter: blur(20px) saturate(1.3);
  border: 1px solid rgba(255,255,255,0.55);
}

/* --- Bio Card --- */
.bio-card {
  background: rgba(255,255,255,0.65);
  backdrop-filter: blur(20px) saturate(1.3);
  -webkit-backdrop-filter: blur(20px) saturate(1.3);
  border: 1px solid rgba(255,255,255,0.55);
  border-radius: 18px;
  padding: 30px 34px;
  border-left: 5px solid;
  border-image: linear-gradient(180deg, #1a3a5c 0%, #3a7bc8 100%) 1;
  margin-bottom: 28px;
  box-shadow: 0 4px 30px rgba(26,58,92,0.07), 0 1px 3px rgba(0,0,0,0.03);
  position: relative;
  overflow: hidden;
}
.bio-card::before {
  content: '';
  position: absolute; top: -100px; right: -100px;
  width: 250px; height: 250px;
  background: radial-gradient(circle, rgba(26,58,92,0.04) 0%, transparent 70%);
  border-radius: 50%; pointer-events: none;
}
.bio-card::after {
  content: '';
  position: absolute; bottom: -80px; left: -60px;
  width: 200px; height: 200px;
  background: radial-gradient(circle, rgba(46,125,50,0.03) 0%, transparent 70%);
  border-radius: 50%; pointer-events: none;
}
.bio-card h3 {
  margin-top: 0; margin-bottom: 14px;
  color: #1a3a5c; font-size: 1.15em; font-weight: 700;
  position: relative; z-index: 1;
}
.bio-card p {
  font-size: 0.95em; line-height: 1.8; color: #374151; margin-bottom: 10px;
  position: relative; z-index: 1;
}
.bio-card .bio-detail {
  font-size: 0.9em; color: #555e6e; line-height: 1.75;
}
.bio-card a {
  color: #1a3a5c; text-decoration: none; font-weight: 500;
  background-image: linear-gradient(transparent 85%, rgba(26,58,92,0.12) 85%);
  background-repeat: no-repeat;
  background-size: 100% 100%;
  transition: background-size 0.3s, color 0.2s;
}
.bio-card a:hover { color: #2c6faa; background-image: linear-gradient(transparent 82%, rgba(44,111,170,0.18) 82%); }

/* --- Badge Row --- */
.badge-row { margin-top: 20px; display: flex; flex-wrap: wrap; gap: 6px; position: relative; z-index: 1; }
.badge-row img {
  height: 22px; border-radius: 4px;
  transition: transform 0.3s cubic-bezier(0.34,1.56,0.64,1), box-shadow 0.2s;
}
.badge-row img:hover {
  transform: translateY(-3px) scale(1.08);
  box-shadow: 0 6px 16px rgba(0,0,0,0.15);
}

/* --- Research Highlights with Progress Bars --- */
.research-viz {
  display: flex; flex-wrap: wrap; gap: 14px;
  margin-bottom: 32px;
}
.rh-pill {
  flex: 1; min-width: 180px;
  display: inline-flex; align-items: center; gap: 12px;
  padding: 16px 20px; border-radius: 14px;
  font-size: 0.84em; font-weight: 600;
  color: #1a3a5c; transition: all 0.35s cubic-bezier(0.34,1.56,0.64,1);
  cursor: default;
  background: rgba(255,255,255,0.65);
  backdrop-filter: blur(20px) saturate(1.3);
  -webkit-backdrop-filter: blur(20px) saturate(1.3);
  border: 1px solid rgba(255,255,255,0.55);
  position: relative; overflow: hidden;
}
.rh-pill:hover { transform: translateY(-4px) scale(1.01); }
.rh-pill .rh-icon {
  width: 40px; height: 40px; border-radius: 12px;
  display: flex; align-items: center; justify-content: center;
  font-size: 1.2em; flex-shrink: 0;
  transition: transform 0.3s;
}
.rh-pill:hover .rh-icon { transform: scale(1.15) rotate(-5deg); }
.rh-pill .rh-text { flex: 1; }
.rh-pill .rh-text strong { display: block; font-size: 0.95em; margin-bottom: 2px; }
.rh-pill .rh-text span { font-size: 0.78em; font-weight: 400; opacity: 0.65; }
.rh-pill .rh-bar {
  position: absolute; bottom: 0; left: 0; height: 3px;
  border-radius: 0 0 14px 14px;
  transition: width 1.2s cubic-bezier(0.22,1,0.36,1);
  width: 0;
}
.rh-pill.animated .rh-bar { width: var(--bar-width, 60%); }

.rh-streaming { border-color: rgba(198,40,40,0.1); background: rgba(198,40,40,0.04); }
.rh-streaming .rh-icon { background: rgba(198,40,40,0.08); color: #c62828; }
.rh-streaming:hover { box-shadow: 0 8px 30px rgba(198,40,40,0.1); }
.rh-streaming .rh-bar { background: linear-gradient(90deg, #c62828, #ef5350); }

.rh-compression { border-color: rgba(21,101,192,0.1); background: rgba(21,101,192,0.04); }
.rh-compression .rh-icon { background: rgba(21,101,192,0.08); color: #1565c0; }
.rh-compression:hover { box-shadow: 0 8px 30px rgba(21,101,192,0.1); }
.rh-compression .rh-bar { background: linear-gradient(90deg, #1565c0, #42a5f5); }

.rh-datacentric { border-color: rgba(46,125,50,0.1); background: rgba(46,125,50,0.04); }
.rh-datacentric .rh-icon { background: rgba(46,125,50,0.08); color: #2e7d32; }
.rh-datacentric:hover { box-shadow: 0 8px 30px rgba(46,125,50,0.1); }
.rh-datacentric .rh-bar { background: linear-gradient(90deg, #2e7d32, #66bb6a); }

/* --- Stats Bar --- */
.stats-bar {
  display: grid; grid-template-columns: repeat(3, 1fr);
  gap: 16px; margin: 0 0 28px;
}
.stats-item {
  text-align: center; padding: 24px 16px 20px;
  background: rgba(255,255,255,0.65);
  backdrop-filter: blur(20px) saturate(1.3);
  -webkit-backdrop-filter: blur(20px) saturate(1.3);
  border: 1px solid rgba(255,255,255,0.55);
  border-radius: 16px;
  box-shadow: 0 4px 24px rgba(26,58,92,0.06), 0 1px 2px rgba(0,0,0,0.03);
  transition: all 0.35s cubic-bezier(0.34,1.56,0.64,1);
  position: relative; overflow: hidden;
}
.stats-item::before {
  content: '';
  position: absolute;
  top: 0; left: 50%; transform: translateX(-50%);
  width: 40px; height: 3px;
  border-radius: 0 0 3px 3px;
  opacity: 0.5;
  transition: width 0.3s, opacity 0.3s;
}
.stats-item:hover::before { width: 70%; opacity: 1; }
.stats-item::after {
  content: ''; position: absolute;
  bottom: 0; left: 0; right: 0;
  height: 3px; border-radius: 0 0 16px 16px;
  transition: height 0.3s;
}
.stats-item:hover {
  transform: translateY(-5px);
  box-shadow: 0 12px 40px rgba(26,58,92,0.12);
}
.stats-item:hover::after { height: 4px; }
.stats-item:nth-child(1)::after, .stats-item:nth-child(1)::before { background: linear-gradient(90deg, #1a3a5c, #2c6faa); }
.stats-item:nth-child(2)::after, .stats-item:nth-child(2)::before { background: linear-gradient(90deg, #2e7d32, #43a047); }
.stats-item:nth-child(3)::after, .stats-item:nth-child(3)::before { background: linear-gradient(90deg, #ef6c00, #ffa726); }

.stats-num {
  font-size: 2.4em; font-weight: 900; color: #1a3a5c;
  display: block; letter-spacing: -0.04em; line-height: 1.1;
  font-family: 'JetBrains Mono', 'Fira Code', monospace;
}
.stats-label {
  font-size: 0.68em; color: #a0aec0; text-transform: uppercase;
  letter-spacing: 0.14em; font-weight: 600; margin-top: 8px; display: block;
}

/* --- Section Title --- */
.section-title {
  font-size: 1.4em; font-weight: 800; color: #1a3a5c;
  padding-bottom: 14px; margin-top: 32px; margin-bottom: 24px;
  letter-spacing: -0.02em;
  display: flex; align-items: center; gap: 14px;
  border-bottom: none;
}
.section-title .title-icon {
  font-size: 1em;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 36px; height: 36px;
  border-radius: 10px;
  background: linear-gradient(135deg, rgba(26,58,92,0.06), rgba(26,58,92,0.02));
}
.section-title::after {
  content: ''; flex: 1; height: 2px;
  background: linear-gradient(90deg, rgba(26,58,92,0.12) 0%, transparent 100%);
  border-radius: 1px;
}

/* --- Section Divider --- */
.section-divider {
  height: 1px; border: none; margin: 44px 0;
  background: linear-gradient(90deg, transparent, rgba(26,58,92,0.08) 20%, rgba(26,58,92,0.08) 80%, transparent);
  position: relative;
}
.section-divider::before {
  content: '';
  position: absolute;
  top: -2px; left: calc(50% - 16px);
  width: 5px; height: 5px; border-radius: 50%;
  background: #cbd5e0;
}
.section-divider::after {
  content: '';
  position: absolute;
  top: -2px; left: calc(50% + 10px);
  width: 5px; height: 5px; border-radius: 50%;
  background: #e2e8f0;
}

/* --- Timeline News --- */
.news-timeline {
  position: relative; padding-left: 32px; list-style: none; margin: 0;
}
.news-timeline::before {
  content: ''; position: absolute;
  top: 4px; bottom: 4px; left: 9px;
  width: 2.5px;
  background: linear-gradient(180deg, #1a3a5c 0%, #3a7bc8 40%, rgba(26,58,92,0.08) 100%);
  border-radius: 2px;
}
.news-timeline li {
  position: relative;
  padding: 14px 18px 14px 12px;
  margin-bottom: 8px;
  border-radius: 12px; border-bottom: none;
  font-size: 0.9em; color: #4a5568;
  line-height: 1.65;
  transition: all 0.3s cubic-bezier(0.34,1.56,0.64,1);
}
.news-timeline li:hover {
  background: rgba(26,58,92,0.025);
  transform: translateX(6px);
  box-shadow: 0 2px 12px rgba(26,58,92,0.04);
}
.news-timeline li:last-child { border-bottom: none; }
.news-timeline li::before {
  content: ''; position: absolute;
  left: -27px; top: 20px;
  width: 12px; height: 12px; border-radius: 50%;
  background: #fff; border: 2.5px solid #3a7bc8;
  box-shadow: 0 0 0 4px rgba(26,58,92,0.06);
  z-index: 1; transition: all 0.3s cubic-bezier(0.34,1.56,0.64,1);
}
.news-timeline li:hover::before {
  background: #1a3a5c; border-color: #1a3a5c;
  box-shadow: 0 0 0 6px rgba(26,58,92,0.12);
  transform: scale(1.3);
}
.news-timeline li.accepted::before { border-color: #2e7d32; background: #e8f5e9; }
.news-timeline li.accepted:hover::before { background: #2e7d32; border-color: #2e7d32; box-shadow: 0 0 0 6px rgba(46,125,50,0.15); }
.news-timeline li em { color: #2d3748; font-style: normal; font-weight: 500; }
.news-timeline li strong { color: #1a3a5c; }

.news-badge {
  display: inline-block; padding: 3px 11px; border-radius: 6px;
  font-weight: 700; font-size: 0.73em; color: #fff;
  margin-right: 8px; vertical-align: middle;
  letter-spacing: 0.05em;
  box-shadow: 0 2px 8px rgba(0,0,0,0.15);
  position: relative; overflow: hidden;
}
.news-badge::after {
  content: '';
  position: absolute; top: 0; left: -100%;
  width: 100%; height: 100%;
  background: linear-gradient(90deg, transparent, rgba(255,255,255,0.2), transparent);
  animation: badge-shimmer 3s ease-in-out infinite;
}
@keyframes badge-shimmer { 0% { left: -100%; } 100% { left: 200%; } }
.badge-cvpr { background: linear-gradient(135deg, #c62828, #ef5350); }
.badge-emnlp { background: linear-gradient(135deg, #c2185b, #e91e63); }
.badge-eccv { background: linear-gradient(135deg, #1565c0, #42a5f5); }
.badge-icml { background: linear-gradient(135deg, #6a1b9a, #ab47bc); }
.badge-acl { background: linear-gradient(135deg, #2e7d32, #66bb6a); }
.badge-arxiv { background: linear-gradient(135deg, #bf360c, #ff6e40); }

/* --- Sub Heading --- */
.sub-heading {
  font-size: 1.08em; font-weight: 700; color: #1a3a5c;
  margin: 32px 0 18px; display: flex; align-items: center; gap: 12px;
}
.sub-heading .dot {
  width: 10px; height: 10px; border-radius: 50%;
  flex-shrink: 0; display: inline-block; position: relative;
}
.sub-heading .dot::after {
  content: '';
  position: absolute; inset: -4px;
  border-radius: 50%;
  border: 1.5px solid currentColor;
  opacity: 0.3;
  animation: dot-ring-pulse 2.5s ease-in-out infinite;
}
@keyframes dot-ring-pulse {
  0%, 100% { transform: scale(1); opacity: 0.3; }
  50% { transform: scale(1.4); opacity: 0; }
}
.sub-heading .count-badge {
  font-size: 0.72em; font-weight: 600; color: #fff;
  padding: 2px 10px; border-radius: 10px;
  font-family: 'JetBrains Mono', 'Fira Code', monospace;
  letter-spacing: 0.03em;
}

/* --- Paper Card --- */
.paper-card {
  background: rgba(255,255,255,0.65);
  backdrop-filter: blur(20px) saturate(1.3);
  -webkit-backdrop-filter: blur(20px) saturate(1.3);
  border: 1px solid rgba(255,255,255,0.55);
  border-radius: 16px;
  padding: 26px 30px;
  margin-bottom: 16px;
  box-shadow: 0 4px 24px rgba(26,58,92,0.05), 0 1px 2px rgba(0,0,0,0.02);
  border-left: 5px solid #1a3a5c;
  transition: all 0.35s cubic-bezier(0.34,1.56,0.64,1);
  position: relative; overflow: hidden;
}
.paper-card::before {
  content: ''; position: absolute;
  top: 0; right: 0; width: 40px; height: 40px;
  background: linear-gradient(225deg, rgba(26,58,92,0.04) 50%, transparent 50%);
  pointer-events: none;
  transition: width 0.3s, height 0.3s;
}
.paper-card:hover::before { width: 50px; height: 50px; }
.paper-card:hover {
  box-shadow: 0 12px 48px rgba(26,58,92,0.1), 0 2px 4px rgba(0,0,0,0.03);
  transform: translateY(-4px);
  border-left-width: 6px;
}
.paper-card.accent-red { border-left-color: #c62828; }
.paper-card.accent-red:hover { box-shadow: 0 12px 48px rgba(198,40,40,0.1); }
.paper-card.accent-blue { border-left-color: #1565c0; }
.paper-card.accent-blue:hover { box-shadow: 0 12px 48px rgba(21,101,192,0.1); }
.paper-card.accent-purple { border-left-color: #6a1b9a; }
.paper-card.accent-purple:hover { box-shadow: 0 12px 48px rgba(106,27,154,0.1); }
.paper-card.accent-green { border-left-color: #2e7d32; }
.paper-card.accent-green:hover { box-shadow: 0 12px 48px rgba(46,125,50,0.1); }
.paper-card.accent-orange { border-left-color: #e65100; }
.paper-card.accent-orange:hover { box-shadow: 0 12px 48px rgba(230,81,0,0.1); }
.paper-card.accent-deeporange { border-left-color: #bf360c; }
.paper-card.accent-deeporange:hover { box-shadow: 0 12px 48px rgba(191,54,12,0.1); }

.paper-venue-chip {
  display: inline-block; padding: 3px 12px;
  border-radius: 6px; font-weight: 700;
  font-size: 0.76em; letter-spacing: 0.04em;
  margin-bottom: 10px;
}
.paper-card h4 { margin: 0 0 10px; font-size: 1.02em; line-height: 1.5; font-weight: 700; }
.paper-card h4 a { color: #1e293b; text-decoration: none; border-bottom: none; transition: color 0.2s; }
.paper-card h4 a:hover { color: #1a3a5c; }

.paper-authors { font-size: 0.84em; color: #64748b; margin-bottom: 8px; line-height: 1.6; }
.paper-authors strong { color: #1a3a5c; font-weight: 600; }
.paper-desc { font-size: 0.87em; color: #64748b; line-height: 1.7; margin-bottom: 14px; }
.paper-desc strong { color: #374151; font-weight: 600; }

.paper-links { display: flex; flex-wrap: wrap; gap: 8px; }
.paper-links a { text-decoration: none; margin-right: 0; border-bottom: none; display: inline-block; }
.paper-links img {
  height: 24px; border-radius: 5px;
  transition: transform 0.3s cubic-bezier(0.34,1.56,0.64,1), box-shadow 0.2s;
}
.paper-links img:hover { transform: translateY(-3px) scale(1.05); box-shadow: 0 6px 16px rgba(0,0,0,0.15); }

.note-text { font-size: 0.82em; color: #a0aec0; margin-bottom: 18px; font-style: italic; }

/* --- Project Grid --- */
.project-grid {
  display: grid; grid-template-columns: repeat(auto-fill, minmax(270px, 1fr));
  gap: 18px; margin-top: 10px;
}
.project-card {
  background: rgba(255,255,255,0.65);
  backdrop-filter: blur(20px) saturate(1.3);
  -webkit-backdrop-filter: blur(20px) saturate(1.3);
  border: 1px solid rgba(255,255,255,0.55);
  border-radius: 16px;
  padding: 26px 28px;
  box-shadow: 0 4px 24px rgba(26,58,92,0.05), 0 1px 2px rgba(0,0,0,0.02);
  transition: all 0.35s cubic-bezier(0.34,1.56,0.64,1);
  display: flex; flex-direction: column;
  position: relative; overflow: hidden;
}
.project-card::before {
  content: ''; position: absolute;
  top: 0; left: 0; right: 0; height: 3px;
  background: linear-gradient(90deg, var(--accent, #1a3a5c), transparent);
  opacity: 0; transition: opacity 0.3s, height 0.3s;
}
.project-card:hover {
  box-shadow: 0 12px 48px rgba(26,58,92,0.1);
  transform: translateY(-6px);
}
.project-card:hover::before { opacity: 1; height: 4px; }

.project-tag {
  display: inline-block; font-size: 0.68em;
  padding: 4px 12px; border-radius: 8px;
  font-weight: 700; color: #fff;
  margin-bottom: 14px; width: fit-content;
  letter-spacing: 0.05em;
  box-shadow: 0 3px 10px rgba(0,0,0,0.15);
}
.project-card h4 {
  margin: 0 0 10px; font-size: 1.12em; font-weight: 700;
  color: #1a3a5c; letter-spacing: -0.01em;
}
.project-card p {
  font-size: 0.85em; color: #64748b;
  margin-bottom: 18px; line-height: 1.65; flex: 1;
}
.project-card a.project-link {
  font-size: 0.84em; color: #1a3a5c; font-weight: 600;
  text-decoration: none; display: inline-flex;
  align-items: center; gap: 6px;
  transition: gap 0.3s cubic-bezier(0.34,1.56,0.64,1); border-bottom: none;
  padding: 6px 0;
}
.project-card a.project-link:hover { gap: 12px; text-decoration: none; }

/* --- Service Card --- */
.service-card {
  padding: 22px 26px; border-radius: 16px;
  background: rgba(255,255,255,0.65);
  backdrop-filter: blur(20px) saturate(1.3);
  -webkit-backdrop-filter: blur(20px) saturate(1.3);
  border: 1px solid rgba(255,255,255,0.55);
  box-shadow: 0 4px 24px rgba(26,58,92,0.05), 0 1px 2px rgba(0,0,0,0.02);
  font-size: 0.93em; color: #4a5568; line-height: 1.7;
  display: flex; align-items: center; gap: 16px;
  transition: all 0.3s ease;
}
.service-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 32px rgba(26,58,92,0.08);
}
.service-card .service-icon {
  width: 44px; height: 44px; border-radius: 12px;
  background: linear-gradient(135deg, #1a3a5c, #2c6faa);
  display: flex; align-items: center; justify-content: center;
  font-size: 1.2em; flex-shrink: 0;
  box-shadow: 0 6px 16px rgba(26,58,92,0.25);
}
.service-card strong { color: #1a3a5c; }
.venue-tags { display: flex; flex-wrap: wrap; gap: 5px; margin-top: 10px; }
.venue-tag {
  font-size: 0.72em; padding: 2px 10px; border-radius: 5px;
  font-weight: 600; letter-spacing: 0.03em;
  background: rgba(26,58,92,0.06); color: #1a3a5c;
  transition: all 0.2s;
}
.venue-tag:hover { background: #1a3a5c; color: #fff; }

/* --- Scroll Reveal --- */
.reveal {
  opacity: 0; transform: translateY(24px);
  transition: opacity 0.8s cubic-bezier(0.16,1,0.3,1), transform 0.8s cubic-bezier(0.16,1,0.3,1);
}
.reveal.visible { opacity: 1; transform: translateY(0); }

/* --- Responsive --- */
@media (max-width: 768px) {
  .stats-bar { gap: 10px; }
  .stats-item { padding: 18px 10px; }
  .stats-num { font-size: 1.8em; }
  .project-grid { grid-template-columns: 1fr; }
  .research-viz { gap: 10px; }
  .rh-pill { padding: 12px 16px; min-width: 150px; }
  .news-timeline { padding-left: 28px; }
  .bio-card { padding: 22px 22px; }
  .paper-card { padding: 20px 22px; }
}
@media (max-width: 480px) {
  .research-viz { flex-direction: column; }
  .rh-pill { min-width: 100%; }
}
</style>

<!-- ===== Bio Card ===== -->
<div class="bio-card reveal">
  <h3>🎯 Building Real-Time Video Intelligence</h3>
  <p>
    I am a <strong>joint Ph.D. student</strong> at <a href="https://www.hkust-gz.edu.cn/">HKUST(GZ)</a> and <a href="https://www.sjtu.edu.cn/">Shanghai Jiao Tong University (SJTU)</a>, advised by <strong><a href="https://xuminghu.github.io/">Prof. Xuming Hu</a></strong> and <strong><a href="https://linfeng-zhang.github.io/">Prof. Linfeng Zhang</a></strong>. I am currently a <strong>Research Intern at <a href="https://www.tencent.com/">Tencent</a></strong>.
  </p>
  <p class="bio-detail">
    My research focuses on <strong>Streaming Video Understanding</strong> — building systems that perceive, reason, and act under real-time constraints with tight token budgets, precise temporal grounding, and reliable interactive behavior. I am also interested in <strong>efficient VideoLLMs</strong> via token compression and data-centric AI.
  </p>
  <div class="badge-row">
    <img src="https://img.shields.io/badge/HKUST(GZ)-1a3a5c?style=flat-square&logo=google-scholar&logoColor=white" alt="HKUST(GZ)">
    <img src="https://img.shields.io/badge/SJTU-0056a3?style=flat-square" alt="SJTU">
    <img src="https://img.shields.io/badge/Tencent_Intern-00a4ef?style=flat-square&logo=tencent-qq&logoColor=white" alt="Tencent">
    <img src="https://img.shields.io/badge/Streaming_Video-c62828?style=flat-square" alt="Streaming Video">
    <img src="https://img.shields.io/badge/Efficient_VideoLLM-2e7d32?style=flat-square" alt="Efficiency">
  </div>
</div>

<!-- ===== Research Highlights ===== -->
<div class="research-viz reveal">
  <div class="rh-pill rh-streaming" style="--bar-width: 85%;">
    <div class="rh-icon">📡</div>
    <div class="rh-text">
      <strong>Streaming Video</strong>
      <span>Real-time perception & reasoning</span>
    </div>
    <div class="rh-bar"></div>
  </div>
  <div class="rh-pill rh-compression" style="--bar-width: 70%;">
    <div class="rh-icon">⚡</div>
    <div class="rh-text">
      <strong>Token Compression</strong>
      <span>Efficient visual encoding</span>
    </div>
    <div class="rh-bar"></div>
  </div>
  <div class="rh-pill rh-datacentric" style="--bar-width: 55%;">
    <div class="rh-icon">📊</div>
    <div class="rh-text">
      <strong>Data-Centric AI</strong>
      <span>Quality over quantity</span>
    </div>
    <div class="rh-bar"></div>
  </div>
</div>

<!-- ===== Stats ===== -->
<div class="stats-bar reveal" id="stats-bar">
  <div class="stats-item">
    <span class="stats-num" data-target="8">8</span>
    <span class="stats-label">Papers</span>
  </div>
  <div class="stats-item">
    <span class="stats-num" data-target="3">3</span>
    <span class="stats-label">Accepted</span>
  </div>
  <div class="stats-item">
    <span class="stats-num" data-target="4">4</span>
    <span class="stats-label">Under Review</span>
  </div>
</div>

<hr class="section-divider">

<!-- ===== News ===== -->
<h2 class="section-title reveal"><span class="title-icon">🔥</span> News & Updates</h2>

<ul class="news-timeline">
  <li class="reveal">
    <span class="news-badge badge-acl">ACL 2026</span>
    📝 <strong>Under Review</strong> — <em>"Are We Using the Right Benchmark: An Evaluation Framework for Visual Token Compression Methods"</em> submitted to <strong>ACL 2026</strong>.
  </li>
  <li class="reveal">
    <span class="news-badge badge-eccv">ECCV 2026</span>
    📝 <strong>Under Review</strong> — Collaborated work <em>"V-CAST: Video Curvature-Aware Spatio-Temporal Pruning"</em> submitted to <strong>ECCV 2026</strong>.
  </li>
  <li class="reveal">
    <span class="news-badge badge-eccv">ECCV 2026</span>
    📝 <strong>Under Review</strong> — Collaborated work <em>"Bridging Visual Representation and Reinforcement Learning from Verifiable Rewards in LVLMs"</em> submitted to <strong>ECCV 2026</strong>.
  </li>
  <li class="reveal">
    <span class="news-badge badge-icml">ICML 2026</span>
    📝 <strong>Under Review</strong> — Collaborated work <em>"Position: Shifting AI Efficiency from Model-Centric to Data-Centric Compression"</em> submitted to <strong>ICML 2026 Position Track</strong>.
  </li>
  <li class="reveal accepted">
    <span class="news-badge badge-cvpr">CVPR 2026</span>
    🏆 <strong>Paper Accepted!</strong> Our work <em>"Accelerating Streaming Video Understanding via Hierarchical Token Compression"</em> (<strong>STC</strong>) is accepted to <strong>CVPR 2026</strong>.
  </li>
  <li class="reveal accepted">
    <span class="news-badge badge-cvpr">CVPR 2026</span>
    🏆 <strong>Paper Accepted!</strong> Collaborated work <em>"Variation-aware Vision Token Dropping for Faster LVLMs"</em> (<strong>V2Drop</strong>) is accepted to <strong>CVPR 2026</strong>.
  </li>
  <li class="reveal accepted">
    <span class="news-badge badge-emnlp">EMNLP 2025</span>
    🏆 <strong>Paper Accepted!</strong> Our work <em>"Video Compression Commander"</em> (<strong>VidCom²</strong>) is accepted to <strong>EMNLP 2025 Main Conference</strong>.
  </li>
  <li class="reveal">
    <span class="news-badge badge-arxiv">arXiv 2025</span>
    📄 <strong>Tech Report</strong> — <em>"AI for Service: Proactive Assistance with AI Glasses"</em> (<strong>Alpha-Service</strong>) released on <strong>arXiv</strong>.
  </li>
</ul>

<hr class="section-divider">

<!-- ===== Publications ===== -->
<h2 class="section-title reveal"><span class="title-icon">📝</span> Publications</h2>

<p class="note-text">* denotes equal contribution, † denotes corresponding author.</p>

<h3 class="sub-heading reveal"><span class="dot" style="background:#2e7d32; color:#2e7d32;"></span> Accepted <span class="count-badge" style="background: linear-gradient(135deg, #2e7d32, #43a047);">3</span></h3>

<div class="paper-card accent-red reveal">
  <h4><a href="#">Accelerating Streaming Video Understanding via Hierarchical Token Compression</a></h4>
  <div class="paper-authors"><strong>Yiyu Wang*</strong>, Xuyang Liu*†, Xiyan Gui, Xinying Lin, Boxue Yang, Chenfei Liao, Tailai Chen, Linfeng Zhang.</div>
  <div class="paper-venue-chip" style="color:#c62828; background: rgba(198,40,40,0.08);">CVPR 2026</div>
  <div class="paper-desc">Proposed <strong>STC-Cacher</strong> and <strong>STC-Pruner</strong>, the first plug-and-play token compression framework specifically designed for real-time streaming video understanding, enabling efficient infinite-length video stream processing.</div>
  <div class="paper-links">
    <a href="#"><img src="https://img.shields.io/badge/Paper-Coming_Soon-B31B1B?style=flat&logo=arxiv" alt="Paper"></a>
    <a href="#"><img src="https://img.shields.io/badge/Code-Coming_Soon-181717?style=flat&logo=github" alt="Code"></a>
  </div>
</div>

<div class="paper-card accent-red reveal">
  <h4><a href="https://arxiv.org/abs/2509.01552">Variation-aware Vision Token Dropping for Faster Large Vision-Language Models</a></h4>
  <div class="paper-authors">Junjie Chen, Xuyang Liu, Zichen Wen, <strong>Yiyu Wang</strong>, Siteng Huang, Honggang Chen.</div>
  <div class="paper-venue-chip" style="color:#c62828; background: rgba(198,40,40,0.08);">CVPR 2026</div>
  <div class="paper-desc">Leveraged variation-aware token dropping to exploit inherent visual sparsity, accelerating large vision-language models with minimal quality degradation.</div>
  <div class="paper-links">
    <a href="https://arxiv.org/abs/2509.01552"><img src="https://img.shields.io/badge/Paper-arXiv-B31B1B?style=flat&logo=arxiv" alt="Paper"></a>
    <a href="https://github.com/xuyang-liu16/V2Drop"><img src="https://img.shields.io/badge/Code-GitHub-181717?style=flat&logo=github" alt="Code"></a>
  </div>
</div>

<div class="paper-card accent-orange reveal">
  <h4><a href="https://aclanthology.org/2025.emnlp-main.98/">Video Compression Commander: Plug-and-Play Inference Acceleration for Video Large Language Models</a></h4>
  <div class="paper-authors">Xuyang Liu*, <strong>Yiyu Wang*</strong>, Junpeng Ma, Linfeng Zhang.</div>
  <div class="paper-venue-chip" style="color:#e65100; background: rgba(230,81,0,0.08);">EMNLP 2025 Main</div>
  <div class="paper-desc">Proposed <strong>VidCom²</strong>, a training-free framework that adaptively compresses video tokens based on frame uniqueness. Achieved <strong>99.6%</strong> performance retention with only <strong>25% tokens</strong> and <strong>70.8%</strong> latency reduction.</div>
  <div class="paper-links">
    <a href="https://aclanthology.org/2025.emnlp-main.98/"><img src="https://img.shields.io/badge/Paper-EMNLP'25-db545a?style=flat&logo=semanticscholar" alt="Paper"></a>
    <a href="https://github.com/xuyang-liu16/VidCom2"><img src="https://img.shields.io/badge/Code-GitHub-181717?style=flat&logo=github" alt="Code"></a>
  </div>
</div>

<h3 class="sub-heading reveal"><span class="dot" style="background:#ef6c00; color:#ef6c00;"></span> Under Review <span class="count-badge" style="background: linear-gradient(135deg, #ef6c00, #ffa726);">4</span></h3>

<div class="paper-card accent-green reveal">
  <h4><a href="#">Are We Using the Right Benchmark: An Evaluation Framework for Visual Token Compression Methods</a></h4>
  <div class="paper-authors">Chenfei Liao, Wensong Wang, Zichen Wen, Xu Zheng, <strong>Yiyu Wang</strong>, Haocong He, Yuanhuiyi Lyu, Lutao Jiang, Xin Zou, Yuqian Fu, Bin Ren, Linfeng Zhang, Xuming Hu.</div>
  <div class="paper-venue-chip" style="color:#2e7d32; background: rgba(46,125,50,0.08);">ACL 2026 (Under Review)</div>
  <div class="paper-desc">Built a more revealing evaluation framework for visual token compression methods and investigated whether current benchmarks truly measure the efficiency-quality trade-off.</div>
  <div class="paper-links"><a href="#"><img src="https://img.shields.io/badge/Paper-Coming_Soon-B31B1B?style=flat&logo=arxiv" alt="Paper"></a></div>
</div>

<div class="paper-card accent-blue reveal">
  <h4><a href="#">V-CAST: Video Curvature-Aware Spatio-Temporal Pruning for Efficient Video Large Language Models</a></h4>
  <div class="paper-authors">Xinying Lin, Xuyang Liu, <strong>Yiyu Wang</strong>, Teng Ma, Wenqi Ren.</div>
  <div class="paper-venue-chip" style="color:#1565c0; background: rgba(21,101,192,0.08);">ECCV 2026 (Under Review)</div>
  <div class="paper-desc">Proposed curvature-aware spatio-temporal pruning for efficient video LLMs, exploiting geometric curvature signals to selectively prune redundant video tokens in both spatial and temporal dimensions.</div>
  <div class="paper-links"><a href="#"><img src="https://img.shields.io/badge/Paper-Coming_Soon-B31B1B?style=flat&logo=arxiv" alt="Paper"></a></div>
</div>

<div class="paper-card accent-blue reveal">
  <h4><a href="#">Bridging Visual Representation and Reinforcement Learning from Verifiable Rewards in Large Vision-Language Models</a></h4>
  <div class="paper-authors">Yuhang Han, Yuyang Wu, Zhengbo Jiao, <strong>Yiyu Wang</strong>, Xuyang Liu, Shaobo Wang, Hanlin Xu, Xuming Hu, Linfeng Zhang.</div>
  <div class="paper-venue-chip" style="color:#1565c0; background: rgba(21,101,192,0.08);">ECCV 2026 (Under Review)</div>
  <div class="paper-desc">Bridged visual representation learning with reinforcement learning from verifiable rewards (RLVR) in large vision-language models, enabling more grounded visual understanding through reward-driven optimization.</div>
  <div class="paper-links"><a href="#"><img src="https://img.shields.io/badge/Paper-Coming_Soon-B31B1B?style=flat&logo=arxiv" alt="Paper"></a></div>
</div>

<div class="paper-card accent-purple reveal">
  <h4><a href="https://arxiv.org/abs/2505.19147">Position: Shifting AI Efficiency from Model-Centric to Data-Centric Compression</a></h4>
  <div class="paper-authors">Xuyang Liu, Zichen Wen, Shaobo Wang, Junjie Chen, Zhishan Tao, Yubo Wang, Tailai Chen, Xiangqi Jin, Chang Zou, <strong>Yiyu Wang</strong>, Chenfei Liao, Xu Zheng, Honggang Chen, Weijia Li, Xuming Hu, Conghui He, Linfeng Zhang.</div>
  <div class="paper-venue-chip" style="color:#6a1b9a; background: rgba(106,27,154,0.08);">ICML 2026 Position Track (Under Review)</div>
  <div class="paper-desc">A position paper arguing that AI efficiency research should shift focus from model-centric compression to data-centric compression, establishing a unified framework for existing efficiency strategies.</div>
  <div class="paper-links"><a href="https://arxiv.org/abs/2505.19147"><img src="https://img.shields.io/badge/Paper-arXiv-B31B1B?style=flat&logo=arxiv" alt="Paper"></a></div>
</div>

<h3 class="sub-heading reveal"><span class="dot" style="background:#bf360c; color:#bf360c;"></span> Technical Report <span class="count-badge" style="background: linear-gradient(135deg, #bf360c, #ff6e40);">1</span></h3>

<div class="paper-card accent-deeporange reveal">
  <h4><a href="https://arxiv.org/abs/2510.14359">AI for Service: Proactive Assistance with AI Glasses</a></h4>
  <div class="paper-authors">Zichen Wen, <strong>Yiyu Wang</strong>, Chenfei Liao, Boxue Yang, Junxian Li, Weifeng Liu, Haocong He, Bolong Feng, Xuyang Liu, Yuanhuiyi Lyu, Xu Zheng, Xuming Hu, Linfeng Zhang.</div>
  <div class="paper-venue-chip" style="color:#bf360c; background: rgba(191,54,12,0.08);">arXiv 2025 (Tech Report)</div>
  <div class="paper-desc">Proposed <strong>Alpha-Service</strong>, a unified framework for proactive AI assistance via AI glasses. Inspired by von Neumann architecture, it addresses "when to help" and "how to help" through five functional units — perception, scheduling, tool utilization, long-term memory, and natural interaction — demonstrated in real-time blackjack advising, museum guiding, and shopping try-on.</div>
  <div class="paper-links"><a href="https://arxiv.org/abs/2510.14359"><img src="https://img.shields.io/badge/Paper-arXiv-B31B1B?style=flat&logo=arxiv" alt="Paper"></a></div>
</div>

<hr class="section-divider">

<!-- ===== Projects ===== -->
<h2 class="section-title reveal"><span class="title-icon">💻</span> Selected Projects</h2>

<div class="project-grid">
  <div class="project-card reveal" style="--accent: #c62828;">
    <span class="project-tag" style="background: linear-gradient(135deg, #c62828, #ef5350);">CVPR 2026</span>
    <h4>STC</h4>
    <p>A streaming-first token compression framework with caching and pruning for real-time video understanding.</p>
    <a href="#" class="project-link">Code Coming Soon <span class="arrow">&rarr;</span></a>
  </div>
  <div class="project-card reveal" style="--accent: #e65100;">
    <span class="project-tag" style="background: linear-gradient(135deg, #e65100, #ff8f00);">EMNLP 2025</span>
    <h4>VidCom²</h4>
    <p>Plug-and-play inference acceleration for VideoLLMs via adaptive frame-uniqueness-based token compression.</p>
    <a href="https://github.com/xuyang-liu16/VidCom2" class="project-link">Open Project <span class="arrow">&rarr;</span></a>
  </div>

</div>

<hr class="section-divider">

<!-- ===== Academic Service ===== -->
<h2 class="section-title reveal"><span class="title-icon">🎓</span> Academic Service</h2>

<div class="service-card reveal">
  <div class="service-icon">✍️</div>
  <div>
    <strong>Conference Reviewer</strong>
    <div class="venue-tags">
      <span class="venue-tag">CVPR</span>
      <span class="venue-tag">ECCV</span>
      <span class="venue-tag">ACM MM</span>
      <span class="venue-tag">EMNLP</span>
    </div>
  </div>
</div>

<!-- Scripts -->
<script>
document.addEventListener('DOMContentLoaded', function() {
  // Scroll reveal with stagger
  var observer = new IntersectionObserver(function(entries) {
    entries.forEach(function(entry) {
      if (entry.isIntersecting) {
        var siblings = entry.target.parentElement.querySelectorAll('.reveal');
        var idx = Array.from(siblings).indexOf(entry.target);
        entry.target.style.transitionDelay = Math.min(idx * 0.07, 0.35) + 's';
        entry.target.classList.add('visible');
      }
    });
  }, { threshold: 0.06, rootMargin: '0px 0px -20px 0px' });
  document.querySelectorAll('.reveal').forEach(function(el) { observer.observe(el); });

  // Counter animation for stats
  var statsBar = document.getElementById('stats-bar');
  if (statsBar) {
    var counterObserver = new IntersectionObserver(function(entries) {
      entries.forEach(function(entry) {
        if (entry.isIntersecting) {
          var counters = entry.target.querySelectorAll('.stats-num[data-target]');
          counters.forEach(function(el) {
            if (el.dataset.animated) return;
            el.dataset.animated = 'true';
            var target = parseInt(el.dataset.target);
            var duration = 1400;
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
    counterObserver.observe(statsBar);
  }

  // Research pills bar animation
  var pillObserver = new IntersectionObserver(function(entries) {
    entries.forEach(function(entry) {
      if (entry.isIntersecting) {
        var pills = entry.target.querySelectorAll('.rh-pill');
        pills.forEach(function(pill, i) {
          setTimeout(function() { pill.classList.add('animated'); }, i * 200);
        });
      }
    });
  }, { threshold: 0.3 });
  document.querySelectorAll('.research-viz').forEach(function(el) { pillObserver.observe(el); });
});
</script>
