"""Layer change for week 32 (Year-End Culmination: The 7 Pillars of Virtue), Bethany Nov 16 2026
("err on the fun side ... more fun interactives and reflection"):
  * word game type 'pillars' (Raise the 7 Pillars): each right answer raises a temple pillar; Day 4 the roof goes on.
  * card kinds 'awards' (Bookshelf Awards), 'lookback' (Reading Road look-back) and 'cert' (year-end certificate).
Added by hand to the built layer (g3-sparkle.js/.css) AND the sources (g3mod.js, g3.css), plus the port.py dispatch line
and SAY_FOR_CARD (port.py is not run; see skill notes). Run once from the repo root: python tools/g3sparkle/layer_wk32.py"""
import io
JS = r"""/* ── Raise the 7 Pillars: one round a day (week 32, year-end) ──
   DATA.wordgame = { type:'pillars', title, sub, todo, stepTitle, win, winWeek, names:[7 pillar names],
     bins:[ {id, label, ic} ], items:[ {t, bin, why, miss:{binId:'…'}, bins:[…] optional} ] }
   A temple with seven pillars. Each right answer raises the pillars a little more; Day d starts
   where days 1…d-1 left them, and on Day 4 the last pillar stands and the roof goes on.
   The pillar names show under the picture (never on it) once the temple is finished. */
function pillarsSVG(have, day, per) {
  var total = per * 4, W = 320, H = 210, f = Math.min(have, total) / total, done = have >= total;
  var s = '<svg viewBox="0 0 ' + W + ' ' + H + '" width="100%" style="max-width:360px" role="img" aria-label="' +
    (done ? 'All seven pillars stand and the roof is on' : 'The temple is ' + Math.round(f * 100) + ' percent built') + '">' +
    '<defs><linearGradient id="g3pSky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="' + (done ? '#FFE9B0' : '#CFE3F5') + '"/><stop offset="1" stop-color="#F7F1E3"/></linearGradient></defs>' +
    '<rect width="' + W + '" height="' + H + '" rx="12" fill="url(#g3pSky)"/>' +
    '<path d="M0 176 Q80 160 160 170 T320 166 V' + H + ' H0 Z" fill="#9DBF7A"/>' +
    '<rect x="34" y="172" width="252" height="10" fill="#D9D2C2" stroke="#9A917F" stroke-width="1"/>' +
    '<rect x="42" y="164" width="236" height="9" fill="#E6E0D2" stroke="#9A917F" stroke-width="1"/>' +
    '<rect x="50" y="157" width="220" height="8" fill="#EFEADF" stroke="#9A917F" stroke-width="1"/>';
  var top = 66, base = 157, full = base - top, gap = 220 / 7;
  for (var k = 0; k < 7; k++) {
    var x = 50 + gap * k + gap / 2, part = Math.max(0, Math.min(1, f * 7 - k)), h = full * part;
    s += '<rect x="' + (x - 9).toFixed(1) + '" y="' + (base - 3) + '" width="18" height="3" fill="#CFC7B4"/>';
    if (h > 0) {
      s += '<rect x="' + (x - 7).toFixed(1) + '" y="' + (base - h).toFixed(1) + '" width="14" height="' + h.toFixed(1) + '" fill="#F4F0E6" stroke="#9A917F" stroke-width="1"/>';
      if (h > 6) s += '<line x1="' + (x - 2).toFixed(1) + '" y1="' + (base - h + 3).toFixed(1) + '" x2="' + (x - 2).toFixed(1) + '" y2="' + (base - 2) + '" stroke="#DDD5C3" stroke-width="1"/>' +
        '<line x1="' + (x + 3).toFixed(1) + '" y1="' + (base - h + 3).toFixed(1) + '" x2="' + (x + 3).toFixed(1) + '" y2="' + (base - 2) + '" stroke="#DDD5C3" stroke-width="1"/>';
      if (part >= 1) s += '<rect x="' + (x - 9).toFixed(1) + '" y="' + (top - 4) + '" width="18" height="5" fill="#E6E0D2" stroke="#9A917F" stroke-width="1"/>';
    }
  }
  if (!done) {
    var a = 50 + 220 * (day - 1) / 4, b = 50 + 220 * day / 4;
    s += '<line x1="' + a.toFixed(1) + '" y1="161" x2="' + b.toFixed(1) + '" y2="161" stroke="#D4AF37" stroke-width="2" stroke-dasharray="3 3"/>';
  } else {
    s += '<rect x="44" y="52" width="232" height="11" fill="#EFEADF" stroke="#9A917F" stroke-width="1"/>' +
      '<polygon points="40,52 160,18 280,52" fill="#F4F0E6" stroke="#9A917F" stroke-width="1.2"/>' +
      '<polygon points="70,48 160,25 250,48" fill="none" stroke="#D4AF37" stroke-width="1.5"/>' +
      '<circle cx="160" cy="38" r="6" fill="#D4AF37"/>';
    for (var g = 0; g < 7; g++) s += '<circle cx="' + (50 + gap * g + gap / 2).toFixed(1) + '" cy="192" r="4" fill="#D4AF37"/>';
  }
  return s + '</svg>';
}
WORDGAME.pillars = function (cfg) {
  var items = cfg.items || [], bins = cfg.bins || []; if (!items.length) return;
  var panel = document.getElementById('tab-words'); if (!panel) return;
  var anchor = panel.querySelector('.tab-next-wrap');
  var day = dayNum(LESSON.day), PER = items.length;
  var KEY = 'oao.g3ela.wg.' + LID;
  var st = Sparkle.get(KEY, null) || { i: 0, misses: 0 };
  if (st.i > PER) st.i = PER;
  var card = cardShell({ id: 'pillars', kind: 'pillars', title: cfg.title || 'Raise the 7 Pillars', sub: cfg.sub || '' }, '🏛️');
  var body = card.querySelector('.spk-card-body');
  body.insertAdjacentHTML('beforeend', lookCard(cfg.look, cfg.todo) +
    '<div class="g3-tw-grid"><div class="g3-pillgame"><div class="g3-pill-pic"></div><div class="g3-pill-names" hidden></div></div><div class="g3-tw-play" aria-live="polite"></div></div>');
  var bx = body.querySelector('.g3-pill-pic'), nm = body.querySelector('.g3-pill-names'), play = body.querySelector('.g3-tw-play');
  function have() { return (day - 1) * PER + st.i; }
  function paint(msg, ok, tried) {
    bx.innerHTML = pillarsSVG(have(), day, PER);
    var fin = have() >= PER * 4;
    nm.hidden = !fin;
    if (fin) nm.innerHTML = (cfg.names || []).map(function (n) { return '<span>' + esc(n) + '</span>'; }).join('');
    if (st.i >= PER) {
      play.innerHTML = '<div class="g3-finish">✓ ' + esc(day === 4 ? (cfg.winWeek || cfg.win || '') : (cfg.win || '')) + '</div>' +
        '<button type="button" class="spk-mini-btn g3-again">👆 Play today’s round again</button>';
      play.querySelector('.g3-again').onclick = function () { st = { i: 0, misses: 0 }; Sparkle.set(KEY, st); paint(); };
      return;
    }
    var it = items[st.i];
    var h = stepHead(st.i + 1, PER, cfg.stepTitle || 'Which one is right?') +
      '<div class="g3-mk-basket"><span class="g3-mk-ic" aria-hidden="true">🏛️</span><span>' + it.t + '</span></div><div class="g3-stalls">';
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
          paint('✓ ' + esc(it.why || 'Right! The pillars rise.'), true);
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

/* ── Year-end cards (week 32). Taps go into My Work through one gatherAnswers wrapper per card. */
function g3AddToWork(label, fn) {
  var _orig = window.gatherAnswers;
  if (typeof _orig !== 'function') return;
  window.gatherAnswers = function () {
    var r = _orig.apply(this, arguments), out = document.getElementById('gatheredOutput');
    if (out) { var t = fn(); if (t) out.value += '\n' + label + '\n────────────────\n' + t; }
    return r;
  };
}
/* card kind 'awards': Bookshelf Awards. c.ribbons = [{id, name, ic, q, opts:[{who, book, moment}]}].
   One ribbon at a time: tap the character who wins it; the real book moment shows. Any pick is fine. */
function cardAwards(c, body) {
  var R = c.ribbons || []; if (!R.length) return;
  var KEY = 'oao.g3ela.awards', st = Sparkle.get(KEY, null) || { i: 0, picks: {} };
  if (st.i > R.length) st.i = R.length;
  body.insertAdjacentHTML('beforeend', lookCard(null, c.todo) + '<div class="g3-aw"></div>');
  var box = body.querySelector('.g3-aw');
  function save() { Sparkle.set(KEY, st); if (window.gatherAnswers) try { window.gatherAnswers(); } catch (e) {} }
  function shelf() {
    return '<div class="g3-aw-shelf">' + R.map(function (r) {
      var p = st.picks[r.id];
      return '<div class="g3-aw-won"><span class="g3-aw-rib" aria-hidden="true">' + esc(r.ic || '🏅') + '</span><b>' + esc(r.name) + '</b><span>' +
        (p ? esc(p.who) + ' <i>(' + esc(p.book) + ')</i>' : '…') + '</span></div>';
    }).join('') + '</div>';
  }
  function paint(shown) {
    if (st.i >= R.length) {
      box.innerHTML = '<div class="g3-finish">✓ ' + esc(c.win || 'Every ribbon has a winner!') + '</div>' + shelf() +
        '<button type="button" class="spk-mini-btn g3-again">👆 Give the ribbons again</button>';
      box.querySelector('.g3-again').onclick = function () { st = { i: 0, picks: {} }; save(); paint(); };
      return;
    }
    var r = R[st.i], h = stepHead(st.i + 1, R.length, 'Give the ' + r.name + ' ribbon') +
      '<div class="g3-aw-now"><span class="g3-aw-rib big" aria-hidden="true">' + esc(r.ic || '🏅') + '</span><span>' + esc(r.q || ('Who gets the ' + r.name + ' ribbon?')) + '</span></div><div class="g3-stalls">';
    r.opts.forEach(function (o, j) {
      h += '<button type="button" class="g3-stall' + (shown === j ? ' sel' : '') + '" data-j="' + j + '"><span class="g3-sack-ic" aria-hidden="true">👆</span><span>' +
        esc(o.who) + ' <i>(' + esc(o.book) + ')</i></span></button>';
    });
    h += '</div>';
    if (shown !== undefined) {
      var o = r.opts[shown];
      h += '<div class="g3-fb ok">🏅 ' + esc(o.who) + ' wins! ' + o.moment + '</div>' +
        '<button type="button" class="spk-btn g3-aw-next">👆 ' + (st.i + 1 < R.length ? 'Next ribbon' : 'See all the winners') + '</button>';
    }
    box.innerHTML = h;
    box.querySelectorAll('.g3-stall').forEach(function (b) {
      b.onclick = function () { var j = +b.getAttribute('data-j'); st.picks[r.id] = { who: r.opts[j].who, book: r.opts[j].book }; save(); wgSfx('chime'); paint(j); };
    });
    var nx = box.querySelector('.g3-aw-next');
    if (nx) nx.onclick = function () { st.i++; save(); paint(); };
  }
  paint();
  g3AddToWork('🏅 BOOKSHELF AWARDS', function () {
    return R.map(function (r) { var p = st.picks[r.id]; return p ? r.name + ': ' + p.who + ' (' + p.book + ')' : ''; }).filter(Boolean).join('\n');
  });
}
/* card kind 'lookback': the Reading Road, looked back on. c.stops = [{book, ic, color, learned}].
   Tap each stop: Opti walks there and one thing you learned shows. Then tap your favorite book. */
function cardLookback(c, body) {
  var S = c.stops || []; if (S.length < 2) return;
  var KEY = 'oao.g3ela.lookback', st = Sparkle.get(KEY, null) || { seen: [], at: -1, fav: null };
  body.insertAdjacentHTML('beforeend', lookCard(null, c.todo) + '<div class="g3-lb"><div class="g3-lb-road"></div><div class="g3-lb-play" aria-live="polite"></div></div>');
  var road = body.querySelector('.g3-lb-road'), play = body.querySelector('.g3-lb-play');
  var W = 320, H = 120, X = S.map(function (s, i) { return 34 + i * (W - 68) / (S.length - 1); }), Y = S.map(function (s, i) { return i % 2 ? 46 : 80; });
  function save() { Sparkle.set(KEY, st); if (window.gatherAnswers) try { window.gatherAnswers(); } catch (e) {} }
  function svg() {
    var p = 'M' + X[0] + ' ' + Y[0]; for (var i = 1; i < S.length; i++) p += ' Q' + ((X[i - 1] + X[i]) / 2) + ' ' + ((Y[i - 1] + Y[i]) / 2 + (i % 2 ? -14 : 14)) + ' ' + X[i] + ' ' + Y[i];
    var s = '<svg viewBox="0 0 ' + W + ' ' + H + '" width="100%" style="max-width:420px" role="img" aria-label="The Reading Road with ' + S.length + ' book stops">' +
      '<rect width="' + W + '" height="' + H + '" rx="12" fill="#F3EEDD"/>' +
      '<path d="' + p + '" fill="none" stroke="#C9B48A" stroke-width="12" stroke-linecap="round"/>' +
      '<path d="' + p + '" fill="none" stroke="#FFF8E6" stroke-width="2" stroke-dasharray="5 6"/>';
    S.forEach(function (o, i) {
      var seen = st.seen.indexOf(i) >= 0;
      s += '<circle cx="' + X[i] + '" cy="' + Y[i] + '" r="15" fill="' + (seen ? '#FFF6D8' : '#FFFFFF') + '" stroke="' + (o.color || '#1B7A4E') + '" stroke-width="' + (seen ? 4 : 2) + '"/>' +
        '<text x="' + X[i] + '" y="' + (Y[i] + 5) + '" text-anchor="middle" font-size="15">' + esc(o.ic || '📖') + '</text>';
      if (st.fav === i) s += '<text x="' + X[i] + '" y="' + (Y[i] - 20) + '" text-anchor="middle" font-size="14">⭐</text>';
    });
    if (st.at >= 0) s += '<g transform="translate(' + (X[st.at] + 10) + ',' + (Y[st.at] - 2) + ')">' + owlSVG('opti', 26).replace('<svg ', '<svg x="0" y="0" ') + '</g>';
    return s + '</svg>';
  }
  function paint() {
    road.innerHTML = svg();
    var allSeen = st.seen.length >= S.length;
    var h = stepHead(allSeen ? 2 : 1, 2, allSeen ? 'Tap your favorite book' : 'Tap each stop on the road') + '<div class="g3-stalls g3-lb-btns">';
    S.forEach(function (o, i) {
      h += '<button type="button" class="g3-stall' + (st.seen.indexOf(i) >= 0 ? ' seen' : '') + (st.fav === i ? ' sel' : '') + '" data-i="' + i + '"><span class="g3-sack-ic" aria-hidden="true">' +
        (allSeen ? '⭐' : '👆') + '</span><span>' + esc(o.book) + '</span></button>';
    });
    h += '</div>';
    if (st.fav !== null) h += '<div class="g3-finish">⭐ ' + esc(S[st.fav].book) + ' is your favorite. ' + esc(c.win || 'What a year of reading!') + '</div>';
    else if (st.at >= 0) h += '<div class="g3-fb ok">' + esc(S[st.at].book) + ': ' + S[st.at].learned + '</div>';
    play.innerHTML = h;
    play.querySelectorAll('.g3-stall').forEach(function (b) {
      b.onclick = function () {
        var i = +b.getAttribute('data-i');
        if (st.seen.length >= S.length) { st.fav = i; st.at = i; wgSfx('win'); }
        else { if (st.seen.indexOf(i) < 0) st.seen.push(i); st.at = i; wgSfx('chime'); }
        save(); paint();
      };
    });
  }
  paint();
  g3AddToWork('🗺️ MY READING ROAD', function () { return st.fav !== null ? 'My favorite book this year: ' + S[st.fav].book : ''; });
}
/* card kind 'cert': a year-end certificate. Name from the profile (or typed), one pillar tapped,
   saved as a picture. c.pillars = [names], c.head, c.line. */
function certSVG(name, pillar, c, w) {
  var e2 = function (t) { return String(t || '').replace(/&/g, '&amp;').replace(/</g, '&lt;'); };
  return '<svg viewBox="0 0 400 280" width="' + w + '" role="img" aria-label="Certificate">' +
    '<rect x="4" y="4" width="392" height="272" rx="14" fill="#FFFBEE" stroke="#0E1C42" stroke-width="4"/>' +
    '<rect x="14" y="14" width="372" height="252" rx="10" fill="none" stroke="#D4AF37" stroke-width="2" stroke-dasharray="6 4"/>' +
    '<text x="200" y="50" text-anchor="middle" font-family="Georgia,serif" font-size="22" font-weight="700" fill="#0E1C42">' + e2(c.head || 'Story Map Explorer') + '</text>' +
    '<text x="200" y="74" text-anchor="middle" font-family="Nunito,sans-serif" font-size="12" fill="#3A4A6B">This certificate is for</text>' +
    '<text x="200" y="108" text-anchor="middle" font-family="Georgia,serif" font-size="26" font-style="italic" fill="#1B7A4E">' + e2(name || 'A 3rd Grade Reader') + '</text>' +
    '<line x1="90" y1="116" x2="310" y2="116" stroke="#C9B48A" stroke-width="1"/>' +
    '<text x="200" y="140" text-anchor="middle" font-family="Nunito,sans-serif" font-size="12" fill="#3A4A6B">' + e2(c.line || 'who walked the whole Reading Road this year.') + '</text>' +
    '<text x="200" y="172" text-anchor="middle" font-family="Nunito,sans-serif" font-size="12" fill="#3A4A6B">The pillar I am taking to 4th grade:</text>' +
    '<text x="200" y="198" text-anchor="middle" font-family="Georgia,serif" font-size="20" font-weight="700" fill="#C7922C">' + e2(pillar || '…') + '</text>' +
    '<text x="300" y="248" text-anchor="middle" font-family="Georgia,serif" font-size="14" font-style="italic" fill="#0E1C42">Opti</text>' +
    '<line x1="250" y1="234" x2="350" y2="234" stroke="#C9B48A" stroke-width="1"/>' +
    '<g transform="translate(40,206)">' + owlSVG('opti', 54).replace('<svg ', '<svg x="0" y="0" ') + '</g></svg>';
}
function cardCert(c, body) {
  var P = c.pillars || []; if (!P.length) return;
  var KEY = 'oao.g3ela.cert', st = Sparkle.get(KEY, null) || { name: '', pillar: '' };
  var pr = profile(); if (!st.name && pr && pr.name) st.name = pr.name;
  body.insertAdjacentHTML('beforeend', lookCard(null, c.todo) + '<div class="g3-cert"></div>');
  var box = body.querySelector('.g3-cert');
  function save() { Sparkle.set(KEY, st); }
  function paint() {
    box.innerHTML = stepHead(st.pillar ? 2 : 1, 2, st.pillar ? 'Check your name, then save your certificate' : 'Tap the pillar you will take to 4th grade') +
      '<div class="g3-stalls g3-cert-p">' + P.map(function (p) {
        return '<button type="button" class="g3-stall' + (st.pillar === p ? ' sel' : '') + '" data-p="' + esc(p) + '"><span class="g3-sack-ic" aria-hidden="true">👆</span><span>' + esc(p) + '</span></button>';
      }).join('') + '</div>' +
      (st.pillar ? '<label class="g3-tl">Your first name: <input class="g3-motto g3-cert-name" maxlength="16" value="' + esc(st.name) + '"></label><div class="g3-warn" hidden></div>' +
        '<div class="g3-cert-live">' + certSVG(st.name, st.pillar, c, '100%') + '</div>' +
        '<button type="button" class="spk-btn g3-dl">👆 Save my certificate as a picture</button>' : '');
    box.querySelectorAll('.g3-cert-p .g3-stall').forEach(function (b) { b.onclick = function () { st.pillar = b.getAttribute('data-p'); save(); wgSfx('win'); paint(); }; });
    var ni = box.querySelector('.g3-cert-name'), warn = box.querySelector('.g3-warn');
    if (ni) ni.oninput = function () {
      var v = ni.value.replace(/[^A-Za-z \-']/g, '');
      if (v && nameProblem(v) === 'block') { warn.hidden = false; warn.textContent = 'Please type your real first name.'; return; }
      warn.hidden = true; st.name = v; save(); box.querySelector('.g3-cert-live').innerHTML = certSVG(st.name, st.pillar, c, '100%');
    };
    var dl = box.querySelector('.g3-dl');
    if (dl) dl.onclick = function () {
      var svg = certSVG(st.name, st.pillar, c, 800).replace('<svg ', '<svg xmlns="http://www.w3.org/2000/svg" ');
      var img = new Image();
      img.onload = function () {
        var cv = document.createElement('canvas'); cv.width = 800; cv.height = 560;
        var cx = cv.getContext('2d'); cx.fillStyle = '#FFFBEE'; cx.fillRect(0, 0, 800, 560); cx.drawImage(img, 0, 0, 800, 560);
        var a = document.createElement('a'); a.download = 'my-3rd-grade-certificate.png'; a.href = cv.toDataURL('image/png');
        document.body.appendChild(a); a.click(); a.remove();
      };
      img.src = 'data:image/svg+xml;charset=utf-8,' + encodeURIComponent(svg);
    };
  }
  paint();
}

"""
CSS = """.g3-pillgame { flex:1 1 300px; max-width:360px; margin:0 auto; }
.g3-pillgame svg.g3-clink { animation:g3clink .45s ease-out; }
.g3-pill-names { display:flex; flex-wrap:wrap; gap:4px 6px; justify-content:center; margin-top:6px; }
.g3-pill-names span { font:800 12px Nunito,sans-serif; color:#8B6914; background:#FFF6D8; border:1px solid #E8D28A; border-radius:999px; padding:2px 8px; }
.g3-aw-now { display:flex; align-items:center; gap:10px; font:800 16px Nunito,sans-serif; color:#0E1C42; margin:6px 0 10px; }
.g3-aw-rib { font-size:22px; } .g3-aw-rib.big { font-size:34px; }
.g3-aw-next { margin-top:10px; }
.g3-aw-shelf { display:grid; grid-template-columns:repeat(auto-fit,minmax(170px,1fr)); gap:8px; margin:10px 0; }
.g3-aw-won { background:#FFFBEE; border:2px solid #E8D28A; border-radius:12px; padding:8px 10px; display:flex; flex-direction:column; gap:2px; font:14px Nunito,sans-serif; color:#3A4A6B; }
.g3-aw-won b { color:#0E1C42; }
.g3-aw .g3-stall.sel, .g3-lb .g3-stall.sel, .g3-cert .g3-stall.sel { border-color:#1B7A4E; background:#EAF6EE; }
.g3-lb-road { max-width:420px; margin:0 auto 8px; }
.g3-cert-p { margin-bottom:8px; }
.g3-cert-live { max-width:440px; margin:10px auto; }
.g3-cert-name { margin-left:6px; }
"""
HEAD = "/* ── Row to the Wreck: one round a day (week 31, Paired Texts: The Courage to Act) ──"
DISP_A = "cfg.type === 'statues' || cfg.type === 'row')"
DISP_B = "cfg.type === 'statues' || cfg.type === 'row' || cfg.type === 'pillars')"
SAY_A = "'g3card-row': 'row',"
SAY_B = "'g3card-row': 'row', 'g3card-pillars': 'pillars', 'g3card-awards': 'awards', 'g3card-lookback': 'lookback', 'g3card-cert': 'cert',"
DOC_A = "'thaw'|'skip'|'statues'|'row', "
DOC_B = "'thaw'|'skip'|'statues'|'row'|'pillars', "
ICON_A = "var ICON = { info: '👀', tapwords: '💬', crest: '🛡️', backward: '🔄' };"
ICON_B = "var ICON = { info: '👀', tapwords: '💬', crest: '🛡️', backward: '🔄', awards: '🏅', lookback: '🗺️', cert: '📜' };"
KIND_A = "else if (c.kind === 'backward') cardBackward(c, body);"
KIND_B = (KIND_A + "\n    else if (c.kind === 'awards') cardAwards(c, body);\n    else if (c.kind === 'lookback') cardLookback(c, body);"
          "\n    else if (c.kind === 'cert') cardCert(c, body);")
CSS_A = ".g3-rowgame svg.g3-clink { animation:g3clink .45s ease-out; }\n"
def edit(p, pairs):
    s = io.open(p, encoding='utf-8', newline='').read()
    assert 'WORDGAME.pillars' not in s and '.g3-pillgame' not in s, p
    for a, b in pairs:
        assert s.count(a) == 1, (p, a[:60], s.count(a)); s = s.replace(a, b)
    io.open(p, 'w', encoding='utf-8', newline='').write(s); print('ok', p)
if __name__ == '__main__':
    edit('g3-sparkle.js', [(HEAD, JS + HEAD), (SAY_A, SAY_B), (DISP_A, DISP_B), (ICON_A, ICON_B), (KIND_A, KIND_B)])
    edit('tools/g3sparkle/g3mod.js', [(HEAD, JS + HEAD), (SAY_A, SAY_B), (DOC_A, DOC_B), (ICON_A, ICON_B), (KIND_A, KIND_B)])
    edit('tools/g3sparkle/port.py', [(DISP_A, DISP_B)])
    for p in ('g3-sparkle.css', 'tools/g3sparkle/g3.css'):
        edit(p, [(CSS_A, CSS_A + CSS)])
