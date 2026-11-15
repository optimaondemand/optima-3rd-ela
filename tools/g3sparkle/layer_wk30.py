"""Layer change for week 30: Statues Come Alive word game (type 'statues'), added by hand to the built layer
(g3-sparkle.js/.css) AND the sources (tools/g3sparkle/g3mod.js, g3.css), plus the dispatch line in port.py and
SAY_FOR_CARD. port.py is not run (see skill notes). Run once from the repo root: python tools/g3sparkle/layer_wk30.py"""
import io
JS = r"""/* ── Statues Come Alive: one round a day (week 30, LWW Ch. 16-17; year-end review) ──
   DATA.wordgame = { type:'statues', title, sub, look, todo, stepTitle, win, winWeek,
     bins:[ {id, label, ic} ] (2-4), items:[ {t, bin, why, miss:{binId:'…'}, bins:[…] optional per-item choices} ] }
   The Witch's courtyard in Ch. 16, full of stone statues. Read the word on the
   statue (in the play area, never on the picture), tap the right answer. Each
   right answer is Aslan's breath on one statue: it turns from gray stone to
   full color. Day d starts with days 1…d-1's statues already alive, so by Day 4
   the courtyard "looked more like a zoo" (4 rows of 8). Practice only. */
var STATUE_COL = ['#A0522D', '#3F51B5', '#E0A21B', '#C0392B', '#2F8F4E', '#D2691E', '#8E44AD', '#1F8A9E'];
function statueFig(x, y, k, alive, today) {
  var c = alive ? STATUE_COL[k % 8] : '#B9BCC2', e = alive ? '#4A3A2A' : '#8E9299';
  var s = '<rect x="' + (x - 9) + '" y="' + (y + 9) + '" width="18" height="5" rx="1" fill="' + (alive ? '#C9B79C' : '#9EA2A8') + '"/>';
  var t = k % 3;
  if (t === 0) s += '<ellipse cx="' + x + '" cy="' + (y + 3) + '" rx="8" ry="6" fill="' + c + '" stroke="' + e + '" stroke-width=".8"/><circle cx="' + (x + 6) + '" cy="' + (y - 3) + '" r="4.5" fill="' + c + '" stroke="' + e + '" stroke-width=".8"/>';
  else if (t === 1) s += '<rect x="' + (x - 4) + '" y="' + (y - 2) + '" width="8" height="11" rx="3" fill="' + c + '" stroke="' + e + '" stroke-width=".8"/><circle cx="' + x + '" cy="' + (y - 6) + '" r="4" fill="' + (alive ? '#F1C7A0' : c) + '" stroke="' + e + '" stroke-width=".8"/>' + (alive ? '<path d="M' + (x - 4) + ' ' + (y - 8) + ' l4 -5 l4 5 Z" fill="#C0392B"/>' : '');
  else s += '<ellipse cx="' + x + '" cy="' + (y + 4) + '" rx="7" ry="5" fill="' + c + '" stroke="' + e + '" stroke-width=".8"/><ellipse cx="' + (x - 3) + '" cy="' + (y - 4) + '" rx="2" ry="6" fill="' + c + '" stroke="' + e + '" stroke-width=".8"/><ellipse cx="' + (x + 3) + '" cy="' + (y - 4) + '" rx="2" ry="6" fill="' + c + '" stroke="' + e + '" stroke-width=".8"/>';
  if (today && !alive) s += '<ellipse cx="' + x + '" cy="' + (y + 3) + '" rx="12" ry="12" fill="none" stroke="#D4AF37" stroke-width="1" stroke-dasharray="2 2"/>';
  return s;
}
function statuesSVG(have, day, per) {
  var total = per * 4, W = 320, H = 210, f = Math.min(have, total) / total;
  var s = '<svg viewBox="0 0 ' + W + ' ' + H + '" width="100%" style="max-width:360px" role="img" aria-label="' +
    Math.min(have, total) + ' of ' + total + ' statues have come alive">' +
    '<rect width="' + W + '" height="' + H + '" rx="12" fill="' + (f >= 0.5 ? '#BFE0F2' : '#D7DCE3') + '"/>' +
    /* the castle wall behind the courtyard, with an open gap once half the statues are alive */
    '<rect x="0" y="16" width="' + W + '" height="34" fill="#9AA0A8"/>';
  for (var b = 0; b < 16; b++) s += '<rect x="' + (b * 20 + 2) + '" y="8" width="12" height="10" fill="#9AA0A8"/>';
  if (f >= 0.5) s += '<rect x="138" y="16" width="44" height="34" fill="#7FB069"/><circle cx="160" cy="26" r="6" fill="#4E8A45"/>';
  s += '<rect x="0" y="50" width="' + W + '" height="' + (H - 50) + '" fill="' + (f >= 0.5 ? '#E8E1CF' : '#CDD1D6') + '"/>';
  var y0 = 70, rh = 36, x0 = 24, cw = 38;
  for (var k = 0; k < total; k++) {
    var row = Math.floor(k / 8), col = k % 8;
    var x = x0 + col * cw + (row % 2 ? 10 : 0), y = y0 + row * rh;
    var today = k >= (day - 1) * per && k < day * per;
    s += statueFig(x, y, k, k < have, today);
  }
  if (have >= total) s += '<rect x="86" y="182" width="148" height="20" rx="10" fill="#2F8F4E"/><text x="160" y="196" text-anchor="middle" font-family="Nunito,sans-serif" font-weight="800" font-size="12" fill="#fff">More like a zoo!</text>';
  return s + '</svg>';
}
WORDGAME.statues = function (cfg) {
  var items = cfg.items || [], bins = cfg.bins || []; if (!items.length) return;
  var panel = document.getElementById('tab-words'); if (!panel) return;
  var anchor = panel.querySelector('.tab-next-wrap');
  var day = dayNum(LESSON.day), PER = items.length;
  var KEY = 'oao.g3ela.wg.' + LID;
  var st = Sparkle.get(KEY, null) || { i: 0, misses: 0 };
  if (st.i > PER) st.i = PER;
  var card = cardShell({ id: 'statues', kind: 'statues', title: cfg.title || 'Statues Come Alive', sub: cfg.sub || '' }, '🗿');
  var body = card.querySelector('.spk-card-body');
  body.insertAdjacentHTML('beforeend', lookCard(cfg.look, cfg.todo) +
    '<div class="g3-tw-grid"><div class="g3-statues"></div><div class="g3-tw-play" aria-live="polite"></div></div>');
  var bx = body.querySelector('.g3-statues'), play = body.querySelector('.g3-tw-play');
  function have() { return (day - 1) * PER + st.i; }
  function paint(msg, ok, tried) {
    bx.innerHTML = statuesSVG(have(), day, PER);
    if (st.i >= PER) {
      play.innerHTML = '<div class="g3-finish">✓ ' + esc(day === 4 ? (cfg.winWeek || cfg.win || '') : (cfg.win || '')) + '</div>' +
        '<button type="button" class="spk-mini-btn g3-again">Play today’s round again</button>';
      play.querySelector('.g3-again').onclick = function () { st = { i: 0, misses: 0 }; Sparkle.set(KEY, st); paint(); };
      return;
    }
    var it = items[st.i];
    var h = stepHead(st.i + 1, PER, cfg.stepTitle || 'Which one is right?') +
      '<div class="g3-mk-basket"><span class="g3-mk-ic" aria-hidden="true">🗿</span><span>' + it.t + '</span></div><div class="g3-stalls">';
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
          paint('✓ ' + esc(it.why || 'Right! The statue comes alive.'), true);
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
CSS = ".g3-statues { flex:1 1 300px; max-width:360px; margin:0 auto; }\n.g3-statues svg.g3-clink { animation:g3clink .45s ease-out; }\n"
HEAD = "/* ── Skipping Stones: one round a day (week 29, LWW Ch. 13-15; ject = throw) ──"
DISP_A = "cfg.type === 'thaw' || cfg.type === 'skip')"
DISP_B = "cfg.type === 'thaw' || cfg.type === 'skip' || cfg.type === 'statues')"
SAY_A = "'g3card-skip': 'skip',"
SAY_B = "'g3card-skip': 'skip', 'g3card-statues': 'statues',"
DOC_A = "'thaw'|'skip', "
DOC_B = "'thaw'|'skip'|'statues', "
CSS_A = ".g3-skip svg.g3-clink { animation:g3clink .45s ease-out; }\n"
def edit(p, pairs):
    s = io.open(p, encoding='utf-8', newline='').read()
    assert 'WORDGAME.statues' not in s and '.g3-statues' not in s, p
    for a, b in pairs:
        assert s.count(a) == 1, (p, a[:60], s.count(a)); s = s.replace(a, b)
    io.open(p, 'w', encoding='utf-8', newline='').write(s); print('ok', p)
edit('g3-sparkle.js', [(HEAD, JS + HEAD), (SAY_A, SAY_B), (DISP_A, DISP_B)])
edit('tools/g3sparkle/g3mod.js', [(HEAD, JS + HEAD), (SAY_A, SAY_B), (DOC_A, DOC_B)])
edit('tools/g3sparkle/port.py', [(DISP_A, DISP_B)])
for p in ('g3-sparkle.css', 'tools/g3sparkle/g3.css'):
    edit(p, [(CSS_A, CSS_A + CSS)])
