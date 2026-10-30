/* 121 Scan help: message search, language memory, print. No libraries. */
(function () {
  "use strict";

  // Make text comparable: lower case, no accents or Arabic vowel marks,
  // one form of alef/yeh/teh marbuta, plain apostrophes.
  function norm(s) {
    return String(s || "").toLowerCase().normalize("NFKD")
      .replace(/[\u0300-\u036f\u064B-\u065F\u0670\u0640]/g, "")
      .replace(/[أإآٱ]/g, "ا").replace(/ى/g, "ي").replace(/ة/g, "ه")
      .replace(/[’‘`]/g, "'").replace(/\s+/g, " ").trim();
  }

  function setupFilter(root, query) {
    var input = root.querySelector("[data-filter]");
    if (!input) return;
    var items = Array.prototype.slice.call(root.querySelectorAll(".msg"));
    var groups = Array.prototype.slice.call(root.querySelectorAll("[data-group]"));
    var count = root.querySelector("[data-count]");
    var empty = root.querySelector("[data-empty]");
    items.forEach(function (m) { m._s = norm(m.getAttribute("data-search")); });

    function apply() {
      var words = norm(input.value).split(" ").filter(Boolean);
      var shown = 0;
      items.forEach(function (m) {
        var hit = words.every(function (w) { return m._s.indexOf(w) !== -1; });
        m.hidden = !hit;
        if (hit) shown++;
      });
      groups.forEach(function (g) { g.hidden = !g.querySelector(".msg:not([hidden])"); });
      if (count) count.textContent = (shown === 1 && count.getAttribute("data-template-one")) || count.getAttribute("data-template").replace("{n}", shown);
      if (empty) empty.hidden = shown !== 0;
    }
    input.addEventListener("input", apply);
    if (query) input.value = query;
    apply();
  }

  function init(root, query) {
    root = root || document;
    if (query == null) {
      try { query = new URLSearchParams(location.search).get("q") || ""; } catch (e) { query = ""; }
    }
    setupFilter(root, query);
    Array.prototype.forEach.call(root.querySelectorAll("[data-lang]"), function (a) {
      a.addEventListener("click", function () {
        try { localStorage.setItem("guide-lang", a.getAttribute("data-lang")); } catch (e) {}
      });
    });
    Array.prototype.forEach.call(root.querySelectorAll("[data-print]"), function (b) {
      b.addEventListener("click", function () { window.print(); });
    });
  }

  window.Guide = { init: init };
  if (!window.GUIDE_PREVIEW) {
    if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", function () { init(); });
    else init();
  }
})();
