(function () {
  var root = document.querySelector(".home-page");
  if (!root) return;

  function all(selector, context) {
    return Array.prototype.slice.call((context || document).querySelectorAll(selector));
  }

  function setButtonCopied(button) {
    var original = button.textContent;
    button.textContent = "Copied";
    button.classList.add("copied");
    window.setTimeout(function () {
      button.textContent = original;
      button.classList.remove("copied");
    }, 1600);
  }

  function copyText(text, button) {
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(text).then(function () {
        setButtonCopied(button);
      });
      return;
    }

    var textarea = document.createElement("textarea");
    textarea.value = text;
    textarea.setAttribute("readonly", "");
    textarea.style.position = "fixed";
    textarea.style.top = "-999px";
    document.body.appendChild(textarea);
    textarea.select();
    document.execCommand("copy");
    document.body.removeChild(textarea);
    setButtonCopied(button);
  }

  function closeOpenPanels(exceptPanel) {
    all(".cite-panel.open", root).forEach(function (panel) {
      if (panel === exceptPanel) return;
      panel.classList.remove("open");
      var id = panel.id.replace("panel-", "");
      var button = root.querySelector('[data-cite-toggle="' + id + '"]');
      if (button) {
        button.classList.remove("active");
        button.innerHTML = '<i class="fas fa-quote-right" aria-hidden="true"></i> Cite';
      }
    });
  }

  root.addEventListener("click", function (event) {
    var citeButton = event.target.closest("[data-cite-toggle]");
    if (citeButton) {
      var citeId = citeButton.getAttribute("data-cite-toggle");
      var panel = document.getElementById("panel-" + citeId);
      if (!panel) return;

      var shouldOpen = !panel.classList.contains("open");
      closeOpenPanels(panel);
      panel.classList.toggle("open", shouldOpen);
      citeButton.classList.toggle("active", shouldOpen);
      citeButton.innerHTML = shouldOpen
        ? '<i class="fas fa-times" aria-hidden="true"></i> Close'
        : '<i class="fas fa-quote-right" aria-hidden="true"></i> Cite';
      return;
    }

    var copyButton = event.target.closest("[data-copy-target]");
    if (copyButton) {
      var target = document.getElementById(copyButton.getAttribute("data-copy-target"));
      if (target) copyText(target.textContent.trim(), copyButton);
    }
  });

  function animateCounter(counter) {
    if (counter.dataset.animated) return;
    counter.dataset.animated = "true";

    var target = parseInt(counter.getAttribute("data-target"), 10);
    if (!target && target !== 0) return;

    var start = performance.now();
    var duration = 900;

    function step(now) {
      var progress = Math.min((now - start) / duration, 1);
      var eased = 1 - Math.pow(1 - progress, 3);
      counter.textContent = Math.round(eased * target);
      if (progress < 1) requestAnimationFrame(step);
    }

    requestAnimationFrame(step);
  }

  function reveal(element) {
    if (element.dataset.revealed) return;
    element.dataset.revealed = "true";
    element.classList.add("visible");

    if (element.id === "stats-row") {
      all(".stat-num[data-target]", element).forEach(animateCounter);
    }
  }

  var revealItems = all(".reveal", root);
  revealItems.forEach(function (item) {
    item.classList.add("will-anim");
  });

  if (!("IntersectionObserver" in window) || window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
    revealItems.forEach(reveal);
    return;
  }

  var observer = new IntersectionObserver(function (entries) {
    entries.forEach(function (entry) {
      if (!entry.isIntersecting) return;
      reveal(entry.target);
      observer.unobserve(entry.target);
    });
  }, {
    rootMargin: "0px 0px -8% 0px",
    threshold: 0.08
  });

  revealItems.forEach(function (item) {
    observer.observe(item);
  });
})();
