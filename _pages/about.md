---
permalink: /
title: "Hi, I'm Yiyu Wang (王一宇) 👋"
excerpt: "Joint Ph.D. Student at HKUST(GZ) & SJTU · Streaming Video Understanding"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

<style>
/* ===== Homepage Optimization v6 ===== */

/* --- Base --- */
.glass-card {
  background: rgba(255,255,255,0.65);
  backdrop-filter: blur(20px) saturate(1.3);
  -webkit-backdrop-filter: blur(20px) saturate(1.3);
  border: 1px solid rgba(255,255,255,0.55);
}

/* --- Hero --- */
.hero {
  position: relative; overflow: hidden;
  border-radius: 18px;
  padding: 50px 40px 42px;
  margin-bottom: 30px;
  background: rgba(255,255,255,0.65);
  backdrop-filter: blur(20px) saturate(1.3);
  -webkit-backdrop-filter: blur(20px) saturate(1.3);
  border: 1px solid rgba(255,255,255,0.55);
  border-left: 5px solid;
  border-image: linear-gradient(180deg, #1a3a5c 0%, #3a7bc8 100%) 1;
  box-shadow: 0 4px 30px rgba(26,58,92,0.07), 0 1px 3px rgba(0,0,0,0.03);
}
.hero::before {
  content: ''; position: absolute; top: -100px; right: -100px;
  width: 280px; height: 280px;
  background: radial-gradient(circle, rgba(26,58,92,0.05) 0%, transparent 70%);
  border-radius: 50%; pointer-events: none;
}
.hero::after {
  content: ''; position: absolute; bottom: -80px; left: -60px;
  width: 220px; height: 220px;
  background: radial-gradient(circle, rgba(46,125,50,0.03) 0%, transparent 70%);
  border-radius: 50%; pointer-events: none;
}
.hero-name {
  font-size: 2.4em; font-weight: 900; color: #1a3a5c;
  letter-spacing: -0.03em; line-height: 1.15; margin: 0 0 8px;
  position: relative; z-index: 1;
}
.hero-tagline {
  font-size: 1.1em; color: #3a7bc8; font-weight: 600;
  margin: 0 0 16px; position: relative; z-index: 1;
}
.hero-bio {
  font-size: 0.95em; color: #374151; line-height: 1.85;
  max-width: 720px; position: relative; z-index: 1;
}
.hero-bio a {
  color: #1a3a5c; text-decoration: none; font-weight: 500;
  background-image: linear-gradient(transparent 85%, rgba(26,58,92,0.12) 85%);
  background-repeat: no-repeat; background-size: 100% 100%;
  transition: background-size 0.3s, color 0.2s;
}
.hero-bio a:hover { color: #2c6faa; background-image: linear-gradient(transparent 82%, rgba(44,111,170,0.18) 82%); }

/* Hero Pills */
.hero-pills {
  display: flex; flex-wrap: wrap; gap: 8px;
  margin-top: 18px; position: relative; z-index: 1;
}
.hero-pill {
  display: inline-flex; align-items: center; gap: 5px;
  padding: 5px 14px; border-radius: 20px;
  font-size: 0.8em; font-weight: 600; color: #fff;
  background: linear-gradient(135deg, #1a3a5c, #3a7bc8);
  box-shadow: 0 3px 10px rgba(26,58,92,0.2);
  transition: transform 0.2s, box-shadow 0.2s;
}
.hero-pill:hover {
  transform: translateY(-2px);
  box-shadow: 0 5px 15px rgba(26,58,92,0.3);
}
.hero-pill.hp-sjtu { background: linear-gradient(135deg, #0056a3, #1976d2); }
.hero-pill.hp-tencent { background: linear-gradient(135deg, #00a4ef, #0288d1); }
.hero-pill.hp-streaming { background: linear-gradient(135deg, #c62828, #ef5350); }
.hero-pill.hp-efficiency { background: linear-gradient(135deg, #2e7d32, #43a047); }

/* --- Research Highlights --- */
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

.rh-streaming { border-color: rgba(198,40,40,0.1); background: rgba(198,40,40,0.04); }
.rh-streaming .rh-icon { background: rgba(198,40,40,0.08); color: #c62828; }
.rh-streaming:hover { box-shadow: 0 8px 30px rgba(198,40,40,0.1); }

.rh-compression { border-color: rgba(21,101,192,0.1); background: rgba(21,101,192,0.04); }
.rh-compression .rh-icon { background: rgba(21,101,192,0.08); color: #1565c0; }
.rh-compression:hover { box-shadow: 0 8px 30px rgba(21,101,192,0.1); }

.rh-datacentric { border-color: rgba(46,125,50,0.1); background: rgba(46,125,50,0.04); }
.rh-datacentric .rh-icon { background: rgba(46,125,50,0.08); color: #2e7d32; }
.rh-datacentric:hover { box-shadow: 0 8px 30px rgba(46,125,50,0.1); }

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
  content: ''; position: absolute;
  top: 0; left: 50%; transform: translateX(-50%);
  width: 40px; height: 3px; border-radius: 0 0 3px 3px;
  opacity: 0.5; transition: width 0.3s, opacity 0.3s;
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

.stats-icon {
  font-size: 1.5em; margin-bottom: 6px; display: block;
}
.stats-item:nth-child(1) .stats-icon { filter: drop-shadow(0 2px 4px rgba(26,58,92,0.2)); }
.stats-item:nth-child(2) .stats-icon { filter: drop-shadow(0 2px 4px rgba(46,125,50,0.2)); }
.stats-item:nth-child(3) .stats-icon { filter: drop-shadow(0 2px 4px rgba(239,108,0,0.2)); }

.stats-num {
  font-size: 2.6em; font-weight: 900; color: #1a3a5c;
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
  display: inline-flex; align-items: center; justify-content: center;
  width: 36px; height: 36px; border-radius: 10px;
  background: linear-gradient(135deg, rgba(26,58,92,0.06), rgba(26,58,92,0.02));
}
.section-title::after {
  content: ''; flex: 1; height: 2px;
  background: linear-gradient(90deg, rgba(26,58,92,0.12) 0%, transparent 100%);
  border-radius: 1px;
}

/* --- Divider --- */
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
.news-timeline li.visible::before {
  animation: dotGlow 0.8s ease-out;
}
@keyframes dotGlow {
  0% { box-shadow: 0 0 0 0px rgba(58,123,200,0.4); }
  100% { box-shadow: 0 0 0 10px rgba(58,123,200,0); }
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

/* First Author Highlight */
.paper-card.first-author {
  border-left-color: #f59e0b;
}
.paper-card.first-author::after {
  content: '⭐ First Author';
  position: absolute;
  top: 14px; right: 16px;
  font-size: 0.64em;
  font-weight: 700;
  color: #f59e0b;
  background: rgba(245,158,11,0.1);
  padding: 3px 10px;
  border-radius: 6px;
  letter-spacing: 0.04em;
}
.paper-card.first-author:hover {
  box-shadow: 0 12px 48px rgba(245,158,11,0.12);
}

.paper-card.accent-red { border-left-color: #c62828; }
.paper-card.accent-red:hover { box-shadow: 0 12px 48px rgba(198,40,40,0.1); }
.paper-card.first-author.accent-red:hover { box-shadow: 0 12px 48px rgba(245,158,11,0.15); }
.paper-card.accent-blue { border-left-color: #1565c0; }
.paper-card.accent-blue:hover { box-shadow: 0 12px 48px rgba(21,101,192,0.1); }
.paper-card.accent-purple { border-left-color: #6a1b9a; }
.paper-card.accent-purple:hover { box-shadow: 0 12px 48px rgba(106,27,154,0.1); }
.paper-card.accent-green { border-left-color: #2e7d32; }
.paper-card.accent-green:hover { box-shadow: 0 12px 48px rgba(46,125,50,0.1); }
.paper-card.accent-orange { border-left-color: #e65100; }
.paper-card.accent-orange:hover { box-shadow: 0 12px 48px rgba(230,81,0,0.1); }
.paper-card.first-author.accent-orange:hover { box-shadow: 0 12px 48px rgba(245,158,11,0.15); }
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

.paper-links { display: flex; flex-wrap: wrap; gap: 8px; align-items: center; }
.paper-links a { text-decoration: none; margin-right: 0; border-bottom: none; display: inline-block; }
.paper-links img {
  height: 24px; border-radius: 5px;
  transition: transform 0.3s cubic-bezier(0.34,1.56,0.64,1), box-shadow 0.2s;
}
.paper-links img:hover { transform: translateY(-3px) scale(1.05); box-shadow: 0 6px 16px rgba(0,0,0,0.15); }

/* Cite Toggle */
.cite-toggle {
  display: inline-flex; align-items: center; gap: 4px;
  padding: 5px 12px; border-radius: 6px;
  font-size: 0.78em; font-weight: 600;
  color: #1a3a5c; background: rgba(26,58,92,0.06);
  border: 1px solid rgba(26,58,92,0.1);
  cursor: pointer; transition: all 0.2s;
  margin-left: 4px;
}
.cite-toggle:hover {
  background: #1a3a5c; color: #fff;
  border-color: #1a3a5c;
}
.cite-toggle.active {
  background: #1a3a5c; color: #fff;
}

/* Cite Panel (collapsible) */
.cite-panel {
  max-height: 0; overflow: hidden; opacity: 0;
  transition: max-height 0.4s ease, opacity 0.3s ease, margin 0.3s ease;
  margin-top: 0;
}
.cite-panel.open {
  max-height: 500px; opacity: 1; margin-top: 14px;
}
.cite-panel-inner {
  background: rgba(26,58,92,0.03);
  border-radius: 12px;
  padding: 14px 18px;
}
.cite-row {
  margin-bottom: 12px;
}
.cite-row:last-child { margin-bottom: 0; }
.cite-row-label {
  font-size: 0.7em; font-weight: 700; color: #1a3a5c;
  text-transform: uppercase; letter-spacing: 0.08em;
  margin-bottom: 6px; display: flex; align-items: center; gap: 6px;
  justify-content: space-between;
}
.cite-row-label button {
  background: rgba(255,255,255,0.8);
  border: 1px solid rgba(26,58,92,0.1);
  border-radius: 5px; padding: 3px 10px;
  font-size: 0.85em; font-weight: 600; color: #1a3a5c;
  cursor: pointer; transition: all 0.2s;
}
.cite-row-label button:hover { background: #1a3a5c; color: #fff; }
.cite-row-label button.copied { background: #2e7d32; color: #fff; border-color: #2e7d32; }
.cite-text {
  font-family: 'JetBrains Mono', 'Fira Code', monospace;
  font-size: 0.78em; line-height: 1.5; color: #4a5568;
}
.cite-pre {
  font-family: 'JetBrains Mono', 'Fira Code', monospace;
  font-size: 0.76em; line-height: 1.5;
  color: #4a5568; white-space: pre-wrap; word-break: break-word;
  margin: 0;
}

.note-text { font-size: 0.82em; color: #a0aec0; margin-bottom: 18px; font-style: italic; }

/* View All Button */
.view-all-box {
  text-align: center; margin: 28px 0 8px;
}
.view-all-btn {
  display: inline-flex; align-items: center; gap: 8px;
  padding: 12px 28px; border-radius: 14px;
  font-size: 0.95em; font-weight: 700;
  color: #1a3a5c; background: rgba(255,255,255,0.65);
  backdrop-filter: blur(20px);
  border: 1px solid rgba(26,58,92,0.15);
  box-shadow: 0 4px 20px rgba(26,58,92,0.08);
  text-decoration: none; transition: all 0.35s cubic-bezier(0.34,1.56,0.64,1);
}
.view-all-btn:hover {
  transform: translateY(-4px);
  box-shadow: 0 12px 40px rgba(26,58,92,0.15);
  background: #1a3a5c; color: #fff;
  border-color: #1a3a5c;
}

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
  opacity: 1; transform: translateY(0);
}
.reveal.will-animate {
  opacity: 0; transform: translateY(24px);
  transition: opacity 0.8s cubic-bezier(0.16,1,0.3,1), transform 0.8s cubic-bezier(0.16,1,0.3,1);
}
.reveal.will-animate.visible { opacity: 1; transform: translateY(0); }

/* --- Responsive --- */
@media (max-width: 768px) {
  .stats-bar { gap: 10px; }
  .stats-item { padding: 18px 10px; }
  .stats-num { font-size: 1.8em; }
  .research-viz { gap: 10px; }
  .rh-pill { padding: 12px 16px; min-width: 150px; }
  .news-timeline { padding-left: 28px; }
  .paper-card { padding: 20px 22px; }
  .hero { padding: 32px 24px 28px; }
  .hero-name { font-size: 1.8em; }
  .paper-card.first-author::after { display: none; }
}
@media (max-width: 480px) {
  .research-viz { flex-direction: column; }
  .rh-pill { min-width: 100%; }
}
</style>

<!-- ===== Hero ===== -->
<div class="hero reveal">
  <div class="hero-name">Hi, I'm Yiyu Wang (王一宇) 👋</div>
  <div class="hero-tagline">Joint Ph.D. @ HKUST(GZ) &amp; SJTU · Streaming Video Understanding</div>
  <div class="hero-bio">
    I am a <strong>joint Ph.D. student</strong> at <a href="https://www.hkust-gz.edu.cn/">HKUST(GZ)</a> and <a href="https://www.sjtu.edu.cn/">Shanghai Jiao Tong University (SJTU)</a>, advised by <strong><a href="https://xuminghu.github.io/">Prof. Xuming Hu</a></strong> and <strong><a href="https://linfeng-zhang.github.io/">Prof. Linfeng Zhang</a></strong>. I am currently a <strong>Research Intern at <a href="https://www.tencent.com/">Tencent</a></strong>.
    <br><br>
    My research focuses on <strong>Streaming Video Understanding</strong> — building systems that perceive, reason, and act under real-time constraints with tight token budgets and precise temporal grounding. I am also interested in <strong>efficient VideoLLMs</strong> via token compression and data-centric AI.
  </div>
  <div class="hero-pills">
    <span class="hero-pill">🏫 HKUST(GZ)</span>
    <span class="hero-pill hp-sjtu">🏫 SJTU</span>
    <span class="hero-pill hp-tencent">💼 Tencent Intern</span>
    <span class="hero-pill hp-streaming">🎥 Streaming Video</span>
    <span class="hero-pill hp-efficiency">⚡ Efficient VideoLLM</span>
  </div>
</div>

<!-- ===== Research Highlights ===== -->
<div class="research-viz reveal">
  <div class="rh-pill rh-streaming">
    <div class="rh-icon">📡</div>
    <div class="rh-text">
      <strong>Streaming Video</strong>
      <span>Real-time perception &amp; reasoning</span>
    </div>
  </div>
  <div class="rh-pill rh-compression">
    <div class="rh-icon">⚡</div>
    <div class="rh-text">
      <strong>Token Compression</strong>
      <span>Efficient visual encoding</span>
    </div>
  </div>
  <div class="rh-pill rh-datacentric">
    <div class="rh-icon">📊</div>
    <div class="rh-text">
      <strong>Data-Centric AI</strong>
      <span>Quality over quantity</span>
    </div>
  </div>
</div>

<!-- ===== Stats ===== -->
<div class="stats-bar reveal" id="stats-bar">
  <div class="stats-item">
    <span class="stats-icon">📄</span>
    <span class="stats-num" data-target="8">8</span>
    <span class="stats-label">Papers</span>
  </div>
  <div class="stats-item">
    <span class="stats-icon">✅</span>
    <span class="stats-num" data-target="3">3</span>
    <span class="stats-label">Accepted</span>
  </div>
  <div class="stats-item">
    <span class="stats-icon">📝</span>
    <span class="stats-num" data-target="4">4</span>
    <span class="stats-label">Under Review</span>
  </div>
</div>

<hr class="section-divider">

<!-- ===== News ===== -->
<h2 class="section-title reveal"><span class="title-icon">🔥</span> News &amp; Updates</h2>

<ul class="news-timeline">
  <li class="reveal">
    <span class="news-badge badge-acl">ACL 2026</span>
    📝 <strong>Under Review</strong> — <em>"VTC-Bench: Are We Using the Right Benchmark? An Evaluation Framework for Visual Token Compression Methods"</em> submitted to <strong>ACL 2026</strong>.
  </li>
  <li class="reveal">
    <span class="news-badge badge-eccv">ECCV 2026</span>
    📝 <strong>Under Review</strong> — <em>"V-CAST: Video Curvature-Aware Spatio-Temporal Pruning"</em> submitted to <strong>ECCV 2026</strong>.
  </li>
  <li class="reveal accepted">
    <span class="news-badge badge-cvpr">CVPR 2026</span>
    🏆 <strong>Paper Accepted!</strong> <em>"Accelerating Streaming Video Large Language Models via Hierarchical Token Compression"</em> (<strong>STC</strong>) accepted to <strong>CVPR 2026</strong>.
  </li>
  <li class="reveal accepted">
    <span class="news-badge badge-emnlp">EMNLP 2025</span>
    🏆 <strong>Paper Accepted!</strong> <em>"Video Compression Commander"</em> (<strong>VidCom²</strong>) accepted to <strong>EMNLP 2025 Main Conference</strong>.
  </li>
</ul>

<hr class="section-divider">

<!-- ===== Publications ===== -->
<h2 class="section-title reveal"><span class="title-icon">📝</span> Publications</h2>

<p class="note-text">* denotes equal contribution, † denotes corresponding author. <a href="/publications/" style="color:#3a7bc8;font-weight:600;">View full list →</a></p>

<h3 class="sub-heading reveal"><span class="dot" style="background:#2e7d32; color:#2e7d32;"></span> Accepted <span class="count-badge" style="background: linear-gradient(135deg, #2e7d32, #43a047);">3</span></h3>

<!-- STC -->
<div class="paper-card accent-red first-author reveal">
  <h4><a href="https://arxiv.org/abs/2512.00891">Accelerating Streaming Video Large Language Models via Hierarchical Token Compression</a></h4>
  <div class="paper-authors"><strong>Yiyu Wang</strong>, Xuyang Liu, Xiyan Gui, Xinying Lin, Boxue Yang, Chenfei Liao, Tailai Chen, and Linfeng Zhang.</div>
  <div class="paper-venue-chip" style="color:#c62828; background: rgba(198,40,40,0.08);">CVPR 2026</div>
  <div class="paper-desc">We propose <strong>Streaming Token Compression (STC)</strong>, the first plug-and-play hierarchical token compression framework for streaming VideoLLMs. STC introduces two token-level accelerators: <strong>STC-Cacher</strong> and <strong>STC-Pruner</strong>. Retains up to <strong>99%</strong> of accuracy while reducing ViT encoding latency and LLM pre-filling latency by <strong>24.5%</strong> and <strong>45.3%</strong>.</div>
  <div class="paper-links">
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
<div class="paper-card accent-red reveal">
  <h4><a href="https://arxiv.org/abs/2509.01552">Variation-aware Vision Token Dropping for Faster Large Vision-Language Models</a></h4>
  <div class="paper-authors">Junjie Chen, Xuyang Liu, Zichen Wen, <strong>Yiyu Wang</strong>, Siteng Huang, and Honggang Chen.</div>
  <div class="paper-venue-chip" style="color:#c62828; background: rgba(198,40,40,0.08);">CVPR 2026</div>
  <div class="paper-desc">We propose <strong>V2Drop</strong>, which progressively removes visual tokens with minimal variation during LVLM inference, maintaining <strong>94.0%</strong> and <strong>98.6%</strong> of the original performance for image and video understanding tasks respectively, while reducing LLM generation latency by <strong>31.5%</strong> and <strong>74.2%</strong>.</div>
  <div class="paper-links">
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
<div class="paper-card accent-orange first-author reveal">
  <h4><a href="https://arxiv.org/abs/2505.14454">Video Compression Commander: Plug-and-Play Inference Acceleration for Video Large Language Models</a></h4>
  <div class="paper-authors">Xuyang Liu*, <strong>Yiyu Wang*</strong>, Junpeng Ma, and Linfeng Zhang.</div>
  <div class="paper-venue-chip" style="color:#e65100; background: rgba(230,81,0,0.08);">EMNLP 2025 Main</div>
  <div class="paper-desc">We propose <strong>VidCom²</strong>, a plug-and-play inference acceleration framework for VideoLLMs that adaptively adjusts compression intensity across frames. Achieved <strong>99.6%</strong> performance retention with only <strong>25% tokens</strong> and <strong>70.8%</strong> latency reduction.</div>
  <div class="paper-links">
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

<h3 class="sub-heading reveal"><span class="dot" style="background:#ef6c00; color:#ef6c00;"></span> Under Review <span class="count-badge" style="background: linear-gradient(135deg, #ef6c00, #ffa726);">4</span></h3>

<!-- VTC-Bench -->
<div class="paper-card accent-green reveal">
  <h4><a href="https://arxiv.org/abs/2510.07143">VTC-Bench: Are We Using the Right Benchmark? An Evaluation Framework for Visual Token Compression Methods</a></h4>
  <div class="paper-authors">Chenfei Liao, Wensong Wang, Zichen Wen, Xu Zheng, <strong>Yiyu Wang</strong>, Haocong He, Yuanhuiyi Lyu, Lutao Jiang, Xin Zou, Yuqian Fu, Bin Ren, Linfeng Zhang, and Xuming Hu.</div>
  <div class="paper-venue-chip" style="color:#2e7d32; background: rgba(46,125,50,0.08);">ACL 2026 (Under Review)</div>
  <div class="paper-desc">We propose <strong>VTC-Bench</strong>, the first comprehensive evaluation framework for visual token compression methods across image and video understanding tasks, revealing critical insights about current benchmarks.</div>
  <div class="paper-links">
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

<script>
function toggleCite(id, btn) {
  var panel = document.getElementById('panel-' + id);
  if (panel.classList.contains('open')) {
    panel.classList.remove('open');
    btn.classList.remove('active');
    btn.innerHTML = '📋 Cite';
  } else {
    // close others
    document.querySelectorAll('.cite-panel.open').forEach(function(p) {
      p.classList.remove('open');
    });
    document.querySelectorAll('.cite-toggle.active').forEach(function(b) {
      b.classList.remove('active');
      b.innerHTML = '📋 Cite';
    });
    panel.classList.add('open');
    btn.classList.add('active');
    btn.innerHTML = '📋 Close';
  }
}
function copyCite(id, btn) {
  var text = document.getElementById(id).textContent;
  navigator.clipboard.writeText(text).then(function() {
    btn.textContent = '✓ Copied';
    btn.classList.add('copied');
    setTimeout(function() { btn.textContent = 'Copy'; btn.classList.remove('copied'); }, 2000);
  });
}
function copyBib(id, btn) {
  var text = document.getElementById(id).textContent;
  navigator.clipboard.writeText(text).then(function() {
    btn.textContent = '✓ Copied';
    btn.classList.add('copied');
    setTimeout(function() { btn.textContent = 'Copy'; btn.classList.remove('copied'); }, 2000);
  });
}

document.addEventListener('DOMContentLoaded', function() {
  // Scroll reveal with stagger
  var reveals = document.querySelectorAll('.reveal');
  reveals.forEach(function(el) { el.classList.add('will-animate'); });
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
  reveals.forEach(function(el) { observer.observe(el); });

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
});
</script>
