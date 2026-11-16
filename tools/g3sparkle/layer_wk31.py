"""(Applied Nov 16 2026; the game box class is .g3-rowgame because .g3-row already exists in the layer CSS.)
Layer change for week 31: Row to the Wreck word game (type 'row'), added by hand to the built layer
(g3-sparkle.js/.css) AND the sources (tools/g3sparkle/g3mod.js, g3.css), plus the dispatch line in port.py and
SAY_FOR_CARD. port.py is not run (see skill notes). Run once from the repo root: python tools/g3sparkle/layer_wk31.py"""
import io
JS = r"""/* ── Row to the Wreck: one round a day (week 31, Paired Texts: The Courage to Act) ──
   DATA.wordgame = { type:'row', title, sub, look, todo, stepTitle, win, winWeek,
     bins:[ {id, label, ic} ] (2-4), items:[ {t, bin, why, miss:{binId:'…'}, bins:[…] optional per-item choices} ] }
   Grace Darling's real rescue (Sept. 7, 1838): she and her father row the lighthouse
   boat out to the wrecked ship. Read the word on the boat (in the play area, never on
   the picture), tap the right answer. Each right answer is one pull on the oars: the
   boat moves across the storm toward the wreck. Day d starts where days 1…d-1 left
   the boat; the storm calms as the boat gets closer, and on Day 4 it reaches the wreck
   (nine people saved). Practice only. */
function rowSVG(have, day, per) {
  var total = per * 4, W = 320, H = 200, f = Math.min(have, total) / total;
  var sky = f < 0.34 ? '#3D4A63' : f < 0.67 ? '#6F86A6' : '#A9C6E3', sea = f < 0.34 ? '#26425E' : f < 0.67 ? '#2F5E86' : '#3D78A8';
  var s = '<svg viewBox="0 0 ' + W + ' ' + H + '" width="100%" style="max-width:360px" role="img" aria-label="The rowing boat is ' +
    Math.round(f * 100) + ' percent of the way to the wreck">' +
    '<rect width="' + W + '" height="' + H + '" rx="12" fill="' + sky + '"/>';
  if (f < 0.67) for (var r = 0; r < 14; r++) s += '<line x1="' + (r * 23 + 6) + '" y1="' + (8 + (r % 3) * 9) + '" x2="' + (r * 23 + 1) + '" y2="' + (22 + (r % 3) * 9) + '" stroke="#C9D4E2" stroke-width="1" opacity="' + (f < 0.34 ? 0.7 : 0.35) + '"/>';
  else s += '<circle cx="270" cy="34" r="14" fill="#FFE7A3"/>';
  /* the sea */
  s += '<rect x="0" y="112" width="' + W + '" height="' + (H - 112) + '" fill="' + sea + '"/>';
  var amp = f < 0.34 ? 7 : f < 0.67 ? 4 : 2;
  for (var w = 0; w < 4; w++) {
    var y = 122 + w * 18, p = 'M0 ' + y;
    for (var x = 0; x <= W; x += 20) p += ' Q' + (x + 10) + ' ' + (y - amp) + ' ' + (x + 20) + ' ' + y;
    s += '<path d="' + p + '" fill="none" stroke="#E6F0F8" stroke-width="1.4" opacity=".55"/>';
  }
  /* the lighthouse on its rock (left) */
  s += '<path d="M6 124 Q26 104 52 112 L58 124 Z" fill="#5A5148"/>' +
    '<polygon points="22,112 38,112 35,58 25,58" fill="#F2EEE6" stroke="#8A8378" stroke-width="1"/>' +
    '<rect x="25" y="74" width="10" height="5" fill="#B5473A"/><rect x="25" y="92" width="10" height="5" fill="#B5473A"/>' +
    '<rect x="24" y="48" width="12" height="10" fill="#FFD86B" stroke="#3B3B3B" stroke-width="1"/><polygon points="22,48 38,48 30,40" fill="#3B3B3B"/>';
  if (f < 0.67) s += '<polygon points="36,51 120,40 120,62" fill="#FFE9A0" opacity=".28"/>';
  /* the wreck on its rock (right): half a ship, people waiting until the boat arrives */
  s += '<path d="M252 126 Q276 104 316 116 L318 126 Z" fill="#4A4239"/>' +
    '<polygon points="262,112 300,104 306,118 266,122" fill="#5C3B22" stroke="#3A2414" stroke-width="1"/>' +
    '<line x1="284" y1="108" x2="280" y2="70" stroke="#3A2414" stroke-width="3"/><line x1="268" y1="82" x2="292" y2="80" stroke="#3A2414" stroke-width="2"/>';
  if (have < total) for (var m = 0; m < 5; m++) s += '<circle cx="' + (270 + m * 6) + '" cy="' + (104 - (m % 2) * 3) + '" r="2.4" fill="#F1D3B3" stroke="#3A2414" stroke-width=".6"/>';
  /* the boat: rows from x 62 (the lighthouse) to x 236 (beside the wreck) */
  var bx = 62 + f * 174, by = 128 + (have < total ? (have % 2 ? -2 : 2) : 0);
  s += '<g transform="translate(' + bx.toFixed(1) + ',' + by + ')">' +
    '<path d="M-16 0 L16 0 L11 8 L-11 8 Z" fill="#7A4A22" stroke="#3A2414" stroke-width="1"/>' +
    '<circle cx="-5" cy="-6" r="3.2" fill="#F1D3B3"/><rect x="-8" y="-3" width="6" height="4" rx="1" fill="#2B4C7E"/>' +
    '<circle cx="6" cy="-6" r="3.2" fill="#F1D3B3"/><path d="M3 -3 h6 v4 h-6 Z" fill="#7B2E3B"/>' +
    '<line x1="-6" y1="0" x2="-20" y2="9" stroke="#C9A36A" stroke-width="1.6"/><line x1="7" y1="0" x2="21" y2="9" stroke="#C9A36A" stroke-width="1.6"/>';
  if (have >= total) for (var q = 0; q < 5; q++) s += '<circle cx="' + (-12 + q * 6) + '" cy="-11" r="2.2" fill="#F1D3B3" stroke="#3A2414" stroke-width=".5"/>';
  s += '</g>';
  /* today's stretch of water, marked with a dotted line */
  var a = 62 + (day - 1) / 4 * 174, b = 62 + day / 4 * 174;
  if (have < total) s += '<line x1="' + a.toFixed(1) + '" y1="146" x2="' + b.toFixed(1) + '" y2="146" stroke="#D4AF37" stroke-width="1.6" stroke-dasharray="3 3"/>';
  if (have >= total) s += '<rect x="96" y="172" width="128" height="20" rx="10" fill="#2F8F4E"/><text x="160" y="186" text-anchor="middle" font-family="Nunito,sans-serif" font-weight="800" font-size="12" fill="#fff">Nine people saved!</text>';
  return s + '</svg>';
}
WORDGAME.row = function (cfg) {
  var items = cfg.items || [], bins = cfg.bins || []; if (!items.length) return;
  var panel = document.getElementById('tab-words'); if (!panel) return;
  var anchor = panel.querySelector('.tab-next-wrap');
  var day = dayNum(LESSON.day), PER = items.length;
  var KEY = 'oao.g3ela.wg.' + LID;
  var st = Sparkle.get(KEY, null) || { i: 0, misses: 0 };
  if (st.i > PER) st.i = PER;
  var card = cardShell({ id: 'row', kind: 'row', title: cfg.title || 'Row to the Wreck', sub: cfg.sub || '' }, '🚣');
  var body = card.querySelector('.spk-card-body');
  body.insertAdjacentHTML('beforeend', lookCard(cfg.look, cfg.todo) +
    '<div class="g3-tw-grid"><div class="g3-rowgame"></div><div class="g3-tw-play" aria-live="polite"></div></div>');
  var bx = body.querySelector('.g3-rowgame'), play = body.querySelector('.g3-tw-play');
  function have() { return (day - 1) * PER + st.i; }
  function paint(msg, ok, tried) {
    bx.innerHTML = rowSVG(have(), day, PER);
    if (st.i >= PER) {
      play.innerHTML = '<div class="g3-finish">✓ ' + esc(day === 4 ? (cfg.winWeek || cfg.win || '') : (cfg.win || '')) + '</div>' +
        '<button type="button" class="spk-mini-btn g3-again">Play today’s round again</button>';
      play.querySelector('.g3-again').onclick = function () { st = { i: 0, misses: 0 }; Sparkle.set(KEY, st); paint(); };
      return;
    }
    var it = items[st.i];
    var h = stepHead(st.i + 1, PER, cfg.stepTitle || 'Which one is right?') +
      '<div class="g3-mk-basket"><span class="g3-mk-ic" aria-hidden="true">🚣</span><span>' + it.t + '</span></div><div class="g3-stalls">';
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
          paint('✓ ' + esc(it.why || 'Right! One more pull on the oars.'), true);
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
CSS = ".g3-rowgame { flex:1 1 300px; max-width:360px; margin:0 auto; }\n.g3-rowgame svg.g3-clink { animation:g3clink .45s ease-out; }\n"
HEAD = "/* ── Statues Come Alive: one round a day (week 30, LWW Ch. 16-17; year-end review) ──"
DISP_A = "cfg.type === 'skip' || cfg.type === 'statues')"
DISP_B = "cfg.type === 'skip' || cfg.type === 'statues' || cfg.type === 'row')"
SAY_A = "'g3card-statues': 'statues',"
SAY_B = "'g3card-statues': 'statues', 'g3card-row': 'row',"
DOC_A = "'thaw'|'skip'|'statues', "
DOC_B = "'thaw'|'skip'|'statues'|'row', "
CSS_A = ".g3-statues svg.g3-clink { animation:g3clink .45s ease-out; }\n"
def edit(p, pairs):
    s = io.open(p, encoding='utf-8', newline='').read()
    assert 'WORDGAME.row ' not in s and '.g3-rowgame' not in s, p
    for a, b in pairs:
        assert s.count(a) == 1, (p, a[:60], s.count(a)); s = s.replace(a, b)
    io.open(p, 'w', encoding='utf-8', newline='').write(s); print('ok', p)
edit('g3-sparkle.js', [(HEAD, JS + HEAD), (SAY_A, SAY_B), (DISP_A, DISP_B)])
edit('tools/g3sparkle/g3mod.js', [(HEAD, JS + HEAD), (SAY_A, SAY_B), (DOC_A, DOC_B)])
edit('tools/g3sparkle/port.py', [(DISP_A, DISP_B)])
for p in ('g3-sparkle.css', 'tools/g3sparkle/g3.css'):
    edit(p, [(CSS_A, CSS_A + CSS)])
