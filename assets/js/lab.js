(function () {
  var root = document.querySelector("[data-games-page]");
  if (!root) return;

  function initSnake() {
    var canvas = root.querySelector("[data-snake-canvas]");
    var scoreEl = root.querySelector("[data-snake-score]");
    var bestEl = root.querySelector("[data-snake-best]");
    var statusEl = root.querySelector("[data-snake-status]");
    var startButton = root.querySelector("[data-snake-start]");
    if (!canvas || !scoreEl || !bestEl || !statusEl || !startButton) return;

    var ctx = canvas.getContext("2d");
    var size = 24;
    var cols = Math.floor(canvas.width / size);
    var rows = Math.floor(canvas.height / size);
    var snake;
    var food;
    var direction;
    var nextDirection;
    var score;
    var best = Number(window.localStorage.getItem("homepage-snake-best") || 0);
    var timer = null;
    var running = false;

    bestEl.textContent = String(best);

    function sameCell(a, b) {
      return a.x === b.x && a.y === b.y;
    }

    function placeFood() {
      var next;
      do {
        next = {
          x: Math.floor(Math.random() * cols),
          y: Math.floor(Math.random() * rows)
        };
      } while (snake.some(function (cell) { return sameCell(cell, next); }));
      food = next;
    }

    function reset(message) {
      snake = [
        { x: 7, y: 8 },
        { x: 6, y: 8 },
        { x: 5, y: 8 }
      ];
      direction = { x: 1, y: 0 };
      nextDirection = direction;
      score = 0;
      scoreEl.textContent = "0";
      statusEl.textContent = message || "Press Start, then use arrows or WASD.";
      placeFood();
      draw();
    }

    function setDirection(x, y) {
      if (direction.x + x === 0 && direction.y + y === 0) return;
      nextDirection = { x: x, y: y };
    }

    function update() {
      direction = nextDirection;
      var head = snake[0];
      var next = {
        x: head.x + direction.x,
        y: head.y + direction.y
      };

      var hitWall = next.x < 0 || next.x >= cols || next.y < 0 || next.y >= rows;
      var hitSelf = snake.some(function (cell) { return sameCell(cell, next); });
      if (hitWall || hitSelf) {
        stop("Game over. Press Restart.");
        return;
      }

      snake.unshift(next);
      if (sameCell(next, food)) {
        score += 1;
        scoreEl.textContent = String(score);
        if (score > best) {
          best = score;
          bestEl.textContent = String(best);
          window.localStorage.setItem("homepage-snake-best", String(best));
        }
        placeFood();
      } else {
        snake.pop();
      }

      draw();
    }

    function stop(message) {
      window.clearInterval(timer);
      timer = null;
      running = false;
      startButton.textContent = "Restart";
      statusEl.textContent = message;
    }

    function start() {
      reset("Playing.");
      running = true;
      startButton.textContent = "Restart";
      window.clearInterval(timer);
      timer = window.setInterval(update, 120);
    }

    function drawCell(x, y, color, inset) {
      var pad = inset || 2;
      ctx.fillStyle = color;
      ctx.fillRect(x * size + pad, y * size + pad, size - pad * 2, size - pad * 2);
    }

    function draw() {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      ctx.fillStyle = "#f7efe3";
      ctx.fillRect(0, 0, canvas.width, canvas.height);

      ctx.strokeStyle = "rgba(70, 50, 35, 0.07)";
      ctx.lineWidth = 1;
      for (var x = 0; x <= cols; x += 1) {
        ctx.beginPath();
        ctx.moveTo(x * size, 0);
        ctx.lineTo(x * size, rows * size);
        ctx.stroke();
      }
      for (var y = 0; y <= rows; y += 1) {
        ctx.beginPath();
        ctx.moveTo(0, y * size);
        ctx.lineTo(cols * size, y * size);
        ctx.stroke();
      }

      drawCell(food.x, food.y, "#b85f3f", 4);
      snake.forEach(function (cell, index) {
        drawCell(cell.x, cell.y, index === 0 ? "#24382f" : "#2f7a50", 2);
      });
    }

    startButton.addEventListener("click", start);

    root.querySelectorAll("[data-snake-dir]").forEach(function (button) {
      button.addEventListener("click", function () {
        var value = button.getAttribute("data-snake-dir");
        if (!running) start();
        if (value === "up") setDirection(0, -1);
        if (value === "down") setDirection(0, 1);
        if (value === "left") setDirection(-1, 0);
        if (value === "right") setDirection(1, 0);
      });
    });

    window.addEventListener("keydown", function (event) {
      var key = event.key.length === 1 ? event.key.toLowerCase() : event.key;
      var handled = true;
      if (key === "ArrowUp" || key === "w") setDirection(0, -1);
      else if (key === "ArrowDown" || key === "s") setDirection(0, 1);
      else if (key === "ArrowLeft" || key === "a") setDirection(-1, 0);
      else if (key === "ArrowRight" || key === "d") setDirection(1, 0);
      else if (key === " " || key === "Enter") {
        if (!running) start();
      } else {
        handled = false;
      }

      if (handled) event.preventDefault();
    });

    reset();
  }

  initSnake();
})();
