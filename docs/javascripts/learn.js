/* WireFrame docs — small behaviours for the learning paths.
 * 1. A link to a heading inside a content tab (learn/#design-with-ai) opens
 *    that tab; Material only scrolls to the hidden heading.
 * 2. Checklists inside .wf-path can be ticked, and remember it per browser.
 * Runs on every page change (navigation.instant), via Material's document$. */
(function () {
  function openTabFor(hash) {
    if (!hash) return;
    var target = document.getElementById(decodeURIComponent(hash.slice(1)));
    if (!target) return;
    var block = target.closest(".tabbed-block");
    if (!block) return;
    var set = block.closest(".tabbed-set");
    var blocks = Array.prototype.slice.call(block.parentElement.children);
    var inputs = set.querySelectorAll(":scope > input");
    var i = blocks.indexOf(block);
    if (inputs[i]) {
      inputs[i].checked = true;
      setTimeout(function () { set.scrollIntoView({ block: "start" }); }, 0);
    }
  }

  function key() { return "wf-learn:" + location.pathname; }

  function wireChecklists() {
    var boxes = document.querySelectorAll(".wf-path input[type=checkbox]");
    if (!boxes.length) return;
    var saved = {};
    try { saved = JSON.parse(localStorage.getItem(key()) || "{}"); } catch (e) { saved = {}; }
    boxes.forEach(function (box, i) {
      box.disabled = false;
      box.checked = !!saved[i];
      box.closest("li").classList.toggle("wf-done", box.checked);
      box.addEventListener("change", function () {
        saved[i] = box.checked;
        box.closest("li").classList.toggle("wf-done", box.checked);
        try { localStorage.setItem(key(), JSON.stringify(saved)); } catch (e) { /* private mode */ }
      });
    });
  }

  function init() { openTabFor(location.hash); wireChecklists(); }

  if (window.document$) document$.subscribe(init);
  else document.addEventListener("DOMContentLoaded", init);
  window.addEventListener("hashchange", function () { openTabFor(location.hash); });
})();
