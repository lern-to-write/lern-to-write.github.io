---
permalink: /games/
title: "Games"
author_profile: true
---

<div class="lab-page games-page" data-games-page>
  <section class="lab-hero p-card">
    <p class="lab-kicker">Game Lab</p>
    <h2>Snake, plus one doorway to a text cultivation game.</h2>
    <p>A small in-page game for quick breaks, with a link to the xiuxian text world.</p>
  </section>

  <div class="games-grid">
    <section class="game-panel active p-card" data-game-panel="snake" aria-label="Snake">
      <div class="game-heading">
        <div>
          <p class="lab-kicker">Playable here</p>
          <h3>Snake</h3>
        </div>
        <div class="score-stack" aria-label="Snake score">
          <span>Score <strong data-snake-score>0</strong></span>
          <span>Best <strong data-snake-best>0</strong></span>
        </div>
      </div>
      <div class="game-actions">
        <button type="button" class="game-button primary" data-snake-start>Start</button>
        <button type="button" class="game-button" data-snake-dir="up">Up</button>
        <button type="button" class="game-button" data-snake-dir="left">Left</button>
        <button type="button" class="game-button" data-snake-dir="right">Right</button>
        <button type="button" class="game-button" data-snake-dir="down">Down</button>
      </div>
      <p class="game-status" data-snake-status>Ready.</p>
      <canvas class="snake-canvas" width="480" height="384" data-snake-canvas aria-label="Snake game canvas"></canvas>
    </section>

    <a class="game-link-card p-card" href="https://xiuxian.wenzi.games/#/home" target="_blank" rel="noopener noreferrer">
      <span class="home-lab-mark" aria-hidden="true">道</span>
      <span class="home-lab-kicker">External game</span>
      <strong>文字修仙</strong>
      <p>一个中文文字修仙游戏入口。打开新页面后从主页进入即可。</p>
      <span class="game-link-cta">Open Xiuxian</span>
    </a>
  </div>
</div>
