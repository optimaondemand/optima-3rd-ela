"""G3 ELA: every Next / tab click lands at the top of the new tab, just under the
sticky tab bar (same rule as G4 sparkle.js goTabTop, Nov 20 2026).
Run from the optima-3rd-ela repo root. Safe to re-run (it checks before editing)."""
import glob, sys

def edit(f, old, new, count=1):
    s = open(f, encoding='utf8', newline='').read()
    if new in s: return False
    n = s.count(old)
    if n != count: sys.exit(f'{f}: expected {count}, found {n}: {old[:70]!r}')
    open(f, 'w', encoding='utf8', newline='').write(s.replace(old, new)); return True

GOTOP = """
/* Every tab change lands at the top of the new tab (Bethany, Nov 20 2026, matching G4):
   the new panel's first line sits just under the sticky progress bar and tab bar, not at
   the very top of the page. Placed twice, because the intro collapsing can still move the
   panel a frame or two later. Skipped while the page restores the last-used tab on load. */
function oaoGoTabTop(tabId) {
  if (window.__oaoRestoringTab) return;
  var last = -1;
  function place() {
    var panel = document.getElementById('tab-' + tabId) || document.querySelector('.tab-panel.active');
    if (!panel) { window.scrollTo(0, 0); return; }
    var off = 8, bar = document.querySelector('.tab-bar');
    if (bar) { var cs = getComputedStyle(bar); off += (parseFloat(cs.top) || 0) + bar.offsetHeight; }
    var y = panel.getBoundingClientRect().top + (window.pageYOffset || 0) - off;
    window.scrollTo(0, Math.max(0, Math.round(y)));
    last = Math.round(window.pageYOffset || 0);
  }
  function again() { if (Math.abs((window.pageYOffset || 0) - last) <= 2) place(); }
  place(); requestAnimationFrame(again); setTimeout(again, 380);
  try {
    if (window.parent && window.parent !== window) {
      window.parent.postMessage(JSON.stringify({ subject: 'lti.scrollToTop' }), '*');
      window.parent.postMessage({ subject: 'lti.scrollToTop' }, '*');
    }
  } catch (e) {}
}
"""

# 1. The sparkle layer (weeks 18-32): both tab wrappers place the new tab instead of the page top,
#    and the restore-on-load flags itself so it does not jump.
j = 'g3-sparkle.js'
OLD_WRAP = """    var r = inner.apply(this, arguments);
    var top = document.getElementById('pageTop');
    try { if (top) top.scrollIntoView({ block: 'start' }); else window.scrollTo(0, 0); } catch (e) { window.scrollTo(0, 0); }
    try {
      if (window.parent && window.parent !== window) {
        window.parent.postMessage(JSON.stringify({ subject: 'lti.scrollToTop' }), '*');
        window.parent.postMessage({ subject: 'lti.scrollToTop' }, '*');
      }
    } catch (e) {}
    return r;"""
NEW_WRAP = """    var r = inner.apply(this, arguments);
    try { oaoGoTabTop(arguments[0]); } catch (e) { window.scrollTo(0, 0); }
    return r;"""
edit(j, OLD_WRAP, NEW_WRAP, 2)
edit(j, "function g3TabTop() {", GOTOP.strip('\n') + "\n\nfunction g3TabTop() {")
edit(j, """      if (pt) pt.scrollIntoView = function () {};   /* no jump on restore */
      try { orig(last); } catch (e) {}
      if (pt) pt.scrollIntoView = keep;""",
     """      if (pt) pt.scrollIntoView = function () {};   /* no jump on restore */
      window.__oaoRestoringTab = true;
      try { orig(last); } catch (e) {}
      window.__oaoRestoringTab = false;
      if (pt) pt.scrollIntoView = keep;""")
print('fixed', j)

# 2. Lessons without the layer (weeks 1-16 and the two project pages): their own switchTab.
LONG = "  document.getElementById('pageTop').scrollIntoView({ behavior: 'smooth', block: 'start' });\n}"
MINI = 'document.getElementById("pageTop").scrollIntoView({behavior:"smooth",block:"start"})}'
n = 0
for f in sorted(glob.glob('lesson-*.html')):
    s = open(f, encoding='utf8').read()
    if 'g3-sparkle.js' in s or 'function switchTab' not in s or 'function oaoGoTabTop' in s: continue
    if LONG in s:
        edit(f, LONG, "  oaoGoTabTop(tabId);\n}\n" + GOTOP)
    elif MINI in s:
        edit(f, MINI, 'oaoGoTabTop(tabId)}\n' + GOTOP)
    else:
        sys.exit(f'{f}: switchTab without a known page-top line')
    n += 1
print('fixed', n, 'lessons')
