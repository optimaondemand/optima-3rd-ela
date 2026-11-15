"""Layer change for week 29: Skipping Stones word game (type 'skip'), added by hand to the built layer
(g3-sparkle.js/.css) AND the sources (tools/g3sparkle/g3mod.js, g3.css), plus the dispatch line in port.py
and SAY_FOR_CARD. port.py is not run (see skill notes). Run once from the repo root: python tools/g3sparkle/layer_wk29.py"""
import io
SKIP_JS = r"""/* ── Skipping Stones: one round a day (week 29, LWW Ch. 13-15; ject = throw) ──
   DATA.wordgame = { type:'skip', title, sub, look, todo, stepTitle, win, winWeek,
     bins:[ {id, label, ic} ] (2-4), items:[ {t, bin, why, miss:{binId:'…'}, bins:[…] optional per-item choices} ] }
   The Fords of Beruna, where the river is broad and shallow. Read the word
   on the stone (in the play area, never on the picture), tap the right
   answer. Each right answer throws a stone that skips and settles in the
   river; day d starts with days 1…d-1's stones, so the week lays a path of
   stepping stones across (4 rows of 8). Nothing from later chapters is
   drawn. Practice only; never fills a graded box. */
function skipSVG(have, day, per) {
  var total = per * 4, W = 320, H = 210;
  var s = '<svg viewBox="0 0 ' + W + ' ' + H + '" width="100%" style="max-width:360px" role="img" aria-label="' +
    Math.min(have, total) + ' of ' + total + ' stepping stones are in the river">' +
    '<rect width="' + W + '" height="' + H + '" rx="12" fill="#CFE6F2"/>' +
    /* far bank with a few trees standing on it */
    '<path d="M0 34 Q160 26 320 34 V64 Q160 58 0 64 Z" fill="#9CC48A"/>';
  [[26, 40, 22], [58, 42, 18], [262, 40, 22], [296, 42, 18]].forEach(function (t) {
    s += '<rect x="' + (t[0] - 2) + '" y="' + (t[1] - 4) + '" width="4" height="8" fill="#5A3E2B"/>' +
      '<circle cx="' + t[0] + '" cy="' + (t[1] - 10) + '" r="' + (t[2] / 2) + '" fill="#3F7A3A"/>';
  });
  /* the river: broad and shallow, with soft current lines */
  s += '<path d="M0 64 Q160 58 320 64 V178 Q160 184 0 178 Z" fill="#7FB8D8"/>';
  for (var c = 0; c < 4; c++) s += '<path d="M' + (20 + c * 80) + ' ' + (82 + (c % 2) * 50) + ' q14 -4 28 0" stroke="#B9DCEF" stroke-width="1.5" fill="none"/>';
  /* near bank, where the reader stands */
  s += '<path d="M0 178 Q160 184 320 178 V210 H0 Z" fill="#B8D4A0"/>';
  var y0 = 160, rh = -26, x0 = 30, cw = 37;
  for (var k = 0; k < total; k++) {
    var row = Math.floor(k / 8), col = k % 8;
    var x = x0 + col * cw + (row % 2 ? 9 : 0), y = y0 + row * rh;
    var today = k >= (day - 1) * per && k < day * per;
    if (k < have) {
      s += '<ellipse cx="' + x + '" cy="' + (y + 2) + '" rx="13" ry="5" fill="#5F8FA8" opacity=".55"/>' +
        '<ellipse cx="' + x + '" cy="' + y + '" rx="11" ry="5.5" fill="#9A9A92" stroke="#6E6E66" stroke-width="1"/>' +
        '<ellipse cx="' + (x - 3) + '" cy="' + (y - 1.5) + '" rx="4" ry="1.6" fill="#C4C4BC"/>';
      if (k === have - 1) s += '<ellipse cx="' + x + '" cy="' + (y + 1) + '" rx="17" ry="7" fill="none" stroke="#FFFFFF" stroke-width="1.2" opacity=".8"/>';
    } else if (today) {
      s += '<ellipse cx="' + x + '" cy="' + y + '" rx="11" ry="5" fill="none" stroke="#E8F4FA" stroke-width="1" stroke-dasharray="2 2"/>';
    }
  }
  if (have >= total) s += '<rect x="86" y="8" width="148" height="20" rx="10" fill="#2E5E7A"/><text x="160" y="22" text-anchor="middle" font-family="Nunito,sans-serif" font-weight="800" font-size="12" fill="#fff">A path across the river!</text>';
  return s + '</svg>';
}
WORDGAME.skip = function (cfg) {
  var items = cfg.items || [], bins = cfg.bins || []; if (!items.length) return;
  var panel = document.getElementById('tab-words'); if (!panel) return;
  var anchor = panel.querySelector('.tab-next-wrap');
  var day = dayNum(LESSON.day), PER = items.length;
  var KEY = 'oao.g3ela.wg.' + LID;
  var st = Sparkle.get(KEY, null) || { i: 0, misses: 0 };
  if (st.i > PER) st.i = PER;
  var card = cardShell({ id: 'skip', kind: 'skip', title: cfg.title || 'Skipping Stones', sub: cfg.sub || '' }, '🪨');
  var body = card.querySelector('.spk-card-body');
  body.insertAdjacentHTML('beforeend', lookCard(cfg.look, cfg.todo) +
    '<div class="g3-tw-grid"><div class="g3-skip"></div><div class="g3-tw-play" aria-live="polite"></div></div>');
  var bx = body.querySelector('.g3-skip'), play = body.querySelector('.g3-tw-play');
  function have() { return (day - 1) * PER + st.i; }
  function paint(msg, ok, tried) {
    bx.innerHTML = skipSVG(have(), day, PER);
    if (st.i >= PER) {
      play.innerHTML = '<div class="g3-finish">✓ ' + esc(day === 4 ? (cfg.winWeek || cfg.win || '') : (cfg.win || '')) + '</div>' +
        '<button type="button" class="spk-mini-btn g3-again">Play today’s round again</button>';
      play.querySelector('.g3-again').onclick = function () { st = { i: 0, misses: 0 }; Sparkle.set(KEY, st); paint(); };
      return;
    }
    var it = items[st.i];
    var h = stepHead(st.i + 1, PER, cfg.stepTitle || 'Which one is right?') +
      '<div class="g3-mk-basket"><span class="g3-mk-ic" aria-hidden="true">🪨</span><span>' + it.t + '</span></div><div class="g3-stalls">';
    (it.bins || bins).forEach(function (b) {
      h += '<button type="button" class="g3-stall' + (tried && tried.indexOf(b.id) >= 0 ? ' tried' : '') + '" data-b="' + esc(b.id) + '">' +
           '<span class="g3-sack-ic" aria-hidden="true">' + esc(b.ic || '👆') + '</span><span>' + esc(b.label) + '</span></button>';
    });
    h += '</div>';
    if (msg) h += '<div class="g3-fb ' + (ok ? 'ok' : 'no') + '">' + msg + '</div>';
    play.innerHTML = h;
    play.querySelectorAll('.g3-stall').forEach(function (b) {
      b.onclick = function () {
        var id = b.getAttribute('data-b');
        if (id === it.bin) {
          st.i++; Sparkle.set(KEY, st); wgSfx(st.i >= PER ? 'win' : 'chime');
          if (st.i >= PER) { paint(); return; }
          paint('✓ ' + esc(it.why || 'Right! The stone skips and lands in the river.'), true);
          var sv = bx.querySelector('svg'); if (sv) { sv.classList.remove('g3-clink'); void sv.getBoundingClientRect(); sv.classList.add('g3-clink'); }
        } else {
          st.misses++; Sparkle.set(KEY, st); wgSfx('bonk');
          paint(esc((it.miss || {})[id] || 'Not that one. Read it again, then try another.'), false, (tried || []).concat([id]));
        }
      };
    });
  }
  paint();
  if (anchor) anchor.parentNode.insertBefore(card, anchor); else panel.appendChild(card);
};

"""
CSS = ".g3-skip { flex:1 1 300px; max-width:360px; margin:0 auto; }\n.g3-skip svg.g3-clink { animation:g3clink .45s ease-out; }\n"
THAW_HEAD = "/* ── The Great Thaw: one round a day (week 28, LWW Ch. 10-12) ──"
DISP_A = "cfg.type === 'icehole' || cfg.type === 'thaw')"
DISP_B = "cfg.type === 'icehole' || cfg.type === 'thaw' || cfg.type === 'skip')"
SAY_A = "'g3card-thaw': 'thaw',"
SAY_B = "'g3card-thaw': 'thaw', 'g3card-skip': 'skip',"
DOC_A = "'icehole'|'thaw', "
DOC_B = "'icehole'|'thaw'|'skip', "
CSS_A = ".g3-thaw svg.g3-clink { animation:g3clink .45s ease-out; }\n"
def edit(p, pairs):
    s = io.open(p, encoding='utf-8', newline='').read()
    assert 'WORDGAME.skip' not in s and '.g3-skip' not in s, p
    for a, b in pairs:
        assert s.count(a) == 1, (p, a[:60], s.count(a)); s = s.replace(a, b)
    io.open(p, 'w', encoding='utf-8', newline='').write(s); print('ok', p)
for p in ('g3-sparkle.js', 'tools/g3sparkle/g3mod.js'):
    pairs = [(THAW_HEAD, SKIP_JS + THAW_HEAD), (SAY_A, SAY_B)]
    if p == 'g3-sparkle.js': pairs.append((DISP_A, DISP_B))
    else: pairs.append((DOC_A, DOC_B))
    edit(p, pairs)
edit('tools/g3sparkle/port.py', [(DISP_A, DISP_B)])
for p in ('g3-sparkle.css', 'tools/g3sparkle/g3.css'):
    edit(p, [(CSS_A, CSS_A + CSS)])
