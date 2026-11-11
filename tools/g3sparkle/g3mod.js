/* ══════════════════════════════════════════════════════════════
   G3 ELA ADDITIONS (Nov 2026): Opti's Story Map
   Everything here is driven by the lesson's own DATA. Nothing below
   names a lesson, a book or a chapter.
     DATA.glossary  = [ {w, m, key} ]      dotted words, 🔊 on key words
     DATA.sayWords  = [ 'word', … ]          🔊 on the vocab cards (says just the word)
     DATA.cards     = [ {id, kind, tab, after, title, sub, look, todo, …} ]
     DATA.wordgame  = {type:'tower'|'wagon', …}  Up the North Tower / Fill the Wagon
   The rules for 8-year-olds: every module opens with a "What to do:"
   line Opti reads, shows one step at a time, and every picture opens
   on notice/wonder before it says what it is.
   ══════════════════════════════════════════════════════════════ */
function g3slug(w) { return String(w).toLowerCase().replace(/[’']/g, '').replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, ''); }
function wordSrc(w) { return MEDIA.audioBase + 'words/g3ela-word-' + g3slug(w) + '.mp3'; }

/* a small 🔊 that says just the word; hidden until the file is really there */
function sayBtn(w) {
  var b = document.createElement('button');
  b.type = 'button'; b.className = 'g3-say'; b.hidden = true;
  b.setAttribute('aria-label', 'Hear the word ' + w); b.title = 'Hear the word';
  b.textContent = '🔊';
  var a = new Audio(); a.preload = 'metadata'; a.src = wordSrc(w);
  a.addEventListener('loadedmetadata', function () { b.hidden = false; });
  a.addEventListener('error', function () { b.remove(); });
  b.addEventListener('click', function (e) {
    e.stopPropagation(); e.preventDefault();
    audioStopAll(a); _nowPlaying = a; try { a.currentTime = 0; } catch (x) {} a.play().catch(function () {});
  });
  return b;
}

/* "What to do:", the opening of every module. Pilot feedback (Nov 10
   2026): the "👀 What am I looking at?" box was one more thing to read
   before the work, so modules open on "What to do:" alone (Opti reads
   it). A card's `look` text now lives behind a picture's notice/wonder. */
function lookCard(look, todo) {
  return todo ? '<p class="g3-todo"><b>What to do:</b> ' + todo + '</p>' : '';
}

/* Notice first, reveal after. Under a picture: look, notice, wonder,
   then one tap tells you what it is. */
function noticeCard(about, btn) {
  btn = btn || 'Tap to learn about this picture';
  if (!about) return '';
  return '<div class="g3-notice"><div class="g3-notice-h">👀 Look closely.</div>' +
    '<p class="g3-notice-q">What do you <b>notice</b>? What do you <b>wonder</b>? Say it out loud.</p>' +
    '<button type="button" class="g3-notice-btn" aria-expanded="false" data-label="' + esc(btn) + '">' + esc(btn) + '</button>' +
    '<p class="g3-notice-a" hidden>' + about + '</p></div>';
}
document.addEventListener('click', function (e) {
  var b = e.target && e.target.closest && e.target.closest('.g3-notice-btn'); if (!b) return;
  var a = b.nextElementSibling; if (!a) return;
  a.hidden = !a.hidden; b.setAttribute('aria-expanded', String(!a.hidden));
  b.textContent = a.hidden ? (b.getAttribute('data-label') || 'Tap to learn about this picture') : 'Hide the answer';
  markTaps(b.parentNode);
});

/* A new tab starts at the top of the lesson (pilot feedback, Nov 10
   2026). G4 holds the scroll across a switch; G3 does not: an
   8-year-old who taps Reading should land on Reading's first line. The
   lesson's own switchTab already scrolls to #pageTop; G4's
   hookTabScroll is left out of the G3 build (port.py), and this also
   asks Canvas to scroll its page up, since the lesson sits in an
   iframe there. */
function g3TabTop() {
  if (typeof window.switchTab !== 'function' || window.switchTab._g3top) return;
  var inner = window.switchTab;
  var f = function () {
    var r = inner.apply(this, arguments);
    var top = document.getElementById('pageTop');
    try { if (top) top.scrollIntoView({ block: 'start' }); else window.scrollTo(0, 0); } catch (e) { window.scrollTo(0, 0); }
    try {
      if (window.parent && window.parent !== window) {
        window.parent.postMessage(JSON.stringify({ subject: 'lti.scrollToTop' }), '*');
        window.parent.postMessage({ subject: 'lti.scrollToTop' }, '*');
      }
    } catch (e) {}
    return r;
  };
  f._g3top = true; window.switchTab = f;
}

/* What is a button and what is not (pilot feedback, Nov 10 2026).
   One rule across the page: if you can tap it, it shows 👆 and lifts
   like a key. Boxes you only read stay flat. A key line under the
   header says so once. */
var G3_TAP_BTN = 'button.dol-check-btn, button.fillin-check-btn, button.tab-next-btn, button.spk-mini-btn, ' +
  'button.spk-dol-swap, button.g3-opt-btn, button.g3-tw-chip, button.g3-notice-btn, button.spk-btn, button.gathered-btn';
function markTaps(root) {
  (root || document).querySelectorAll(G3_TAP_BTN).forEach(function (b) {
    if (b.querySelector('.g3-hand')) return;
    /* one icon per button: a leading emoji gives way to the hand */
    var t = b.firstChild;
    if (t && t.nodeType === 3) t.nodeValue = t.nodeValue.replace(/^\s*(?:\p{Extended_Pictographic}\uFE0F?\s*)+/u, '');
    var h = document.createElement('span'); h.className = 'g3-hand'; h.setAttribute('aria-hidden', 'true'); h.textContent = '👆';
    b.insertBefore(h, b.firstChild);
  });
  (root || document).querySelectorAll('.fc-tap').forEach(function (t) {
    if (!/👆/.test(t.textContent)) t.textContent = '👆 ' + t.textContent;
  });
}
function buildTapKey() {
  if (document.querySelector('.g3-tapkey')) return;
  var hdr = document.querySelector('.spk-hd, .header'); if (!hdr) return;
  var k = document.createElement('div'); k.className = 'g3-tapkey';
  k.innerHTML = '<span><b>👆</b> You can tap it.</span><span><b>🔊</b> You can listen.</span><span><b class="g3-dot">dotted word</b> Tap it to see what it means.</span>';
  hdr.parentNode.insertBefore(k, hdr.nextSibling);
}
function buildTaps() {
  markTaps(); buildTapKey(); g3TabTop();
  if (window.MutationObserver) {
    var t = null;
    new MutationObserver(function () { clearTimeout(t); t = setTimeout(function () { markTaps(); }, 60); })
      .observe(document.body, { childList: true, subtree: true });
  }
}

/* ── glossary: dotted words with a tooltip; key words get a 🔊 ─────── */
var G3_SKIP = '[class*="match"], .flip-card, .fillin-game, .fillin-item, [class*="sort"], [class*="spotter"], ' +
              '[class*="dice"], input, textarea, button, select, script, style, a, .spk-card, .g3-card, .g3-tip, ' +
              '.header, .q-text, .textbox-prompt, [class*="reveal"], [class*="answer"], .decode-sentence, h1, h2, h3, ' +
              '.activity-title, .tab-btn, .footer';
function buildGlossary() {
  var G = DATA.glossary; if (!G || !G.length) return;
  var panels = document.querySelectorAll('.tab-panel');
  panels.forEach(function (panel) {
    G.forEach(function (g) {
      /* plurals count (conjunction / conjunctions); cs:true matches case exactly,
         so "whipping boy" is glossed but the book title "The Whipping Boy" is not */
      var re = new RegExp('\\b(' + g.w.replace(/[.*+?^${}()|[\]\\]/g, '\\$&') + '(?:e?s)?)\\b', g.cs ? '' : 'i');
      var walker = document.createTreeWalker(panel, NodeFilter.SHOW_TEXT, {
        acceptNode: function (n) {
          if (!n.nodeValue || !re.test(n.nodeValue)) return NodeFilter.FILTER_REJECT;
          var p = n.parentElement; if (!p || p.closest(G3_SKIP) || p.closest('.g3-gl')) return NodeFilter.FILTER_REJECT;
          return NodeFilter.FILTER_ACCEPT;
        }
      });
      var node = walker.nextNode(); if (!node) return;           /* first use on each tab only */
      var m = re.exec(node.nodeValue);
      var after = node.splitText(m.index); after.nodeValue = after.nodeValue.slice(m[1].length);
      var span = document.createElement('span');
      span.className = 'g3-gl'; span.tabIndex = 0;
      span.setAttribute('aria-label', m[1] + ': ' + g.m);
      var word = document.createElement('span'); word.className = 'g3-gl-w'; word.textContent = m[1];
      span.appendChild(word);
      var tip = document.createElement('span');
      tip.className = 'g3-tip'; tip.setAttribute('role', 'tooltip');
      var b = document.createElement('b'); b.textContent = g.w; tip.appendChild(b);
      if (g.key) tip.appendChild(sayBtn(g.w));
      var t = document.createElement('span'); t.className = 'g3-tip-m'; t.textContent = g.m; tip.appendChild(t);
      span.appendChild(tip);
      span.addEventListener('click', function (e) { if (e.target.closest('.g3-say')) return; span.classList.toggle('open'); });
      span.addEventListener('keydown', function (e) {
        if (e.key === 'Escape') span.classList.remove('open');
        if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); span.classList.toggle('open'); }
      });
      node.parentNode.insertBefore(span, after);
    });
  });
  document.addEventListener('click', function (e) {
    document.querySelectorAll('.g3-gl.open').forEach(function (s) { if (!s.contains(e.target)) s.classList.remove('open'); });
  });
}

/* ── 🔊 on the vocabulary: a row of the day's words at the head of the
   Vocabulary activity. Each says just the word, never the meaning; a
   word whose recording is not there yet does not show, and the row
   shows only once one of them does. ───────────────────────────────── */
function buildSayWords() {
  var W = DATA.sayWords; if (!W || !W.length) return;
  var titles = document.querySelectorAll('#tab-words .activity-title'), act = null;
  for (var i = 0; i < titles.length; i++) if (/vocabular/i.test(titles[i].textContent || '')) { act = titles[i].closest('.activity'); break; }
  if (!act || act.querySelector('.g3-sayrow')) return;
  var head = act.querySelector('.activity-head');
  var row = document.createElement('div'); row.className = 'g3-sayrow'; row.hidden = true;
  row.innerHTML = '<span class="g3-sayrow-l">🔊 Hear this week’s words:</span>';
  W.forEach(function (w) {
    var chip = document.createElement('span'); chip.className = 'g3-saychip'; chip.hidden = true;
    var b = sayBtn(w);
    b.textContent = w + ' 🔊'; b.className = 'g3-say g3-say-chip';
    chip.appendChild(b); row.appendChild(chip);
    if (window.MutationObserver) {
      var ob = new MutationObserver(function () { if (!b.hidden) { chip.hidden = false; row.hidden = false; ob.disconnect(); } });
      ob.observe(b, { attributes: true, attributeFilter: ['hidden'] });
    }
  });
  if (head && head.parentNode === act) act.insertBefore(row, head.nextSibling); else act.insertBefore(row, act.firstChild);
}

/* ── where a card goes ──────────────────────────────────────────── */
function g3Anchor(c) {
  var panel = document.getElementById('tab-' + (c.tab || 'reading')); if (!panel) return null;
  if (c.after === 'top') return { host: panel, before: panel.firstChild };
  if (c.after && c.after !== 'end') {               /* an activity title, matched loosely */
    var re = new RegExp(c.after, 'i');
    var acts = panel.querySelectorAll('.activity');
    for (var i = 0; i < acts.length; i++) {
      var t = acts[i].querySelector('.activity-title');
      if (t && re.test(t.textContent || '')) {
        return c.before ? { host: acts[i].parentNode, before: acts[i] }
                        : { host: acts[i].parentNode, before: acts[i].nextSibling };
      }
    }
  }
  var nx = panel.querySelector('.tab-next-wrap');
  return { host: nx ? nx.parentNode : panel, before: nx };
}
function cardShell(c, icon) {
  var card = document.createElement('section');
  card.className = 'spk-card g3-card g3-' + c.kind; card.id = 'g3card-' + c.id;
  card.innerHTML =
    '<div class="spk-card-head"><div class="spk-card-num">' + (icon || '✦') + '</div><div>' +
    '<div class="spk-card-title">' + esc(c.title || '') + '</div>' +
    (c.sub ? '<div class="spk-card-sub">' + esc(c.sub) + '</div>' : '') +
    '</div></div><div class="spk-card-body"></div>';
  return card;
}
/* Opti's clip for a card, if one has been recorded: guide/opti/g3ela-w-d-card-<id>.mp3 */
function cardVoice(id, body) {
  var src = MEDIA.audioBase + 'guide/opti/g3ela-' + LESSON.week + '-' + dayNum(LESSON.day) + '-card-' + id + '.mp3';
  var ac = audioControl('Listen to Opti', src); if (!ac) return;
  var words = (DATA.transcripts || {})['card-' + id];
  if (ac._audio && words) spotlight('card-' + id, words, ac._audio);
  var row = document.createElement('div'); row.className = 'g3-opti-row'; row.hidden = true;
  row.innerHTML = '<span class="g3-opti-face" aria-hidden="true">' + owlSVG('opti', 46) + '</span>';
  row.appendChild(ac);
  if (words) {
    var ra = document.createElement('details'); ra.className = 'spk-note spk-readalong';
    var sm = document.createElement('summary'); sm.textContent = '📄 Read Opti’s words instead'; ra.appendChild(sm);
    var bd = document.createElement('div'); bd.className = 'spk-note-body'; bd.textContent = words; ra.appendChild(bd);
    row.appendChild(ra);
  }
  if (window.MutationObserver) {
    var ob = new MutationObserver(function () { if (!ac.hidden) { row.hidden = false; ob.disconnect(); } });
    ob.observe(ac, { attributes: true, attributeFilter: ['hidden'] });
  }
  body.insertBefore(row, body.firstChild);
}
function stepHead(i, n, title) {
  return '<div class="g3-step-h">Step ' + i + ' of ' + n + ' · ' + esc(title) + '</div>';
}
function artFig(a, cls) {
  if (!a || !a.file) return '';
  return '<figure class="g3-art ' + (cls || '') + '"><img src="' + artURL(a.file) + '" alt="' + esc(a.alt || a.title || '') +
    '" loading="lazy" onerror="this.parentNode.remove()"><figcaption>' + esc(a.title || '') +
    (a.creator ? ', ' + esc(a.creator) : '') + (a.date ? ' (' + esc(a.date) + ')' : '') +
    (a.license ? ' · ' + esc(a.license) : '') + '</figcaption></figure>';
}

/* card kind 'info': art + what it is + a few plain sentences */
function cardInfo(c, body) {
  var h = lookCard(null, c.todo) + artFig(c.art) + (c.art ? noticeCard(c.look, c.lookBtn) : '');
  (c.text || []).forEach(function (p) { h += '<p class="g3-p">' + p + '</p>'; });
  body.insertAdjacentHTML('beforeend', h);
}

/* card kind 'tapwords': one phrase at a time. Tap the phrase and its
   everyday words open right underneath it; "Next" moves on. Phrases
   already done stay stacked above, each with its meaning under it. */
function cardTapwords(c, body) {
  var items = c.items || []; if (!items.length) return;
  var KEY = 'oao.g3ela.card.' + LID + '.' + c.id;
  var done = Math.min(items.length, Sparkle.get(KEY, 0) || 0);
  body.insertAdjacentHTML('beforeend', lookCard(c.look, c.todo) + '<div class="g3-done-list"></div><div class="g3-steps"></div>');
  var steps = body.querySelector('.g3-steps'), list = body.querySelector('.g3-done-list');
  function pair(it) {
    return '<div class="g3-tw-said">“' + esc(it.said) + '”</div>' +
           '<div class="g3-tw-means"><span class="g3-tw-tag">Everyday words</span>' + esc(it.means) + '</div>';
  }
  function show() {
    list.innerHTML = '';
    for (var k = 0; k < done; k++) { var d = document.createElement('div'); d.className = 'g3-tw-done'; d.innerHTML = pair(items[k]); list.appendChild(d); }
    if (done >= items.length) {
      steps.innerHTML = '<div class="g3-finish">✓ ' + esc(c.finish || 'All done!') + '</div>' +
        '<button type="button" class="spk-mini-btn g3-again">Start again</button>';
      steps.querySelector('.g3-again').onclick = function () { done = 0; Sparkle.set(KEY, 0); show(); };
      return;
    }
    var it = items[done];
    steps.innerHTML = stepHead(done + 1, items.length, it.title || 'Tap the words') +
      '<p class="g3-step-p">' + esc(it.context || '') + '</p>' +
      '<div class="g3-tw-live"><button type="button" class="g3-tw-chip" aria-expanded="false">“' + esc(it.said) + '” <span class="g3-tw-tap" aria-hidden="true">👆 tap</span></button>' +
      '<div class="g3-tw-reveal" hidden><div class="g3-tw-means"><span class="g3-tw-tag">Everyday words</span>' + esc(it.means) + '</div>' +
      '<button type="button" class="spk-mini-btn g3-tw-next">' + (done + 1 < items.length ? 'Next words →' : 'Finish ✓') + '</button></div></div>';
    var chip = steps.querySelector('.g3-tw-chip'), rev = steps.querySelector('.g3-tw-reveal');
    chip.onclick = function () {
      if (!rev.hidden) return;
      rev.hidden = false; chip.setAttribute('aria-expanded', 'true'); chip.classList.add('open'); wgSfx('chime');
      steps.querySelector('.g3-tw-next').focus({ preventScroll: true });
    };
    steps.querySelector('.g3-tw-next').onclick = function () { done++; Sparkle.set(KEY, done); show(); };
  }
  show();
}

/* card kind 'crest': hold the lantern to the saddle (reveal), then design your own */
var CREST_SYMBOLS = {
  crown: '<path d="M-22 10 L-26 -14 L-12 -2 L0 -20 L12 -2 L26 -14 L22 10 Z" fill="#E9C46A" stroke="#7A5A10" stroke-width="2"/><circle cx="0" cy="-20" r="3" fill="#C0392B"/>',
  owl: '<ellipse cx="0" cy="2" rx="18" ry="22" fill="#B87333" stroke="#5E3A14" stroke-width="2"/><circle cx="-7" cy="-4" r="6" fill="#FFF8E9"/><circle cx="7" cy="-4" r="6" fill="#FFF8E9"/><circle cx="-7" cy="-4" r="2.6" fill="#0E1C42"/><circle cx="7" cy="-4" r="2.6" fill="#0E1C42"/><path d="M-3 3 L0 8 L3 3 Z" fill="#E9C46A"/><path d="M-16 -18 L-10 -24 L-8 -15 Z M16 -18 L10 -24 L8 -15 Z" fill="#5E3A14"/>',
  book: '<path d="M-22 -14 Q-11 -18 0 -12 Q11 -18 22 -14 L22 14 Q11 10 0 16 Q-11 10 -22 14 Z" fill="#FFF8E9" stroke="#3B2A14" stroke-width="2"/><path d="M0 -12 V16" stroke="#3B2A14" stroke-width="2"/>',
  key: '<circle cx="-12" cy="0" r="9" fill="none" stroke="#E9C46A" stroke-width="5"/><path d="M-3 0 H22 M14 0 V8 M20 0 V6" stroke="#E9C46A" stroke-width="5" stroke-linecap="round"/>',
  tower: '<path d="M-14 22 V-10 H-18 V-20 H-11 V-14 H-4 V-20 H4 V-14 H11 V-20 H18 V-10 H14 V22 Z" fill="#D2C9B1" stroke="#5E5340" stroke-width="2"/><path d="M-4 22 V8 Q0 2 4 8 V22 Z" fill="#5E5340"/>',
  star: '<path d="M0 -22 L6 -7 L22 -7 L9 3 L14 19 L0 9 L-14 19 L-9 3 L-22 -7 L-6 -7 Z" fill="#E9C46A" stroke="#7A5A10" stroke-width="2"/>',
  horse: '<path d="M-14 20 L-10 0 Q-14 -10 -6 -18 L2 -24 L4 -16 Q14 -12 16 -2 L10 0 Q4 -4 2 2 L6 20 Z" fill="#F6E9CE" stroke="#3B2A14" stroke-width="2"/>',
  heart: '<path d="M0 18 C-26 0 -18 -20 0 -8 C18 -20 26 0 0 18 Z" fill="#C0392B" stroke="#7A1E14" stroke-width="2"/>'
};
var CREST_COLORS = { 'Royal blue': '#2A3A8C', 'Ruby red': '#A32020', 'Forest green': '#2F6B3B', 'Royal purple': '#5B2C83', 'Sky blue': '#4A86C5', 'Night black': '#222831' };
function crestSVG(o, size) {
  var col = CREST_COLORS[o.color] || '#2A3A8C', sym = CREST_SYMBOLS[o.symbol] || CREST_SYMBOLS.crown;
  var motto = esc((o.motto || '').toUpperCase().slice(0, 14));
  return '<svg viewBox="0 0 200 240" width="' + (size || 200) + '" class="g3-crest-svg" role="img" aria-label="Your crest">' +
    '<path d="M30 14 H170 V104 Q170 172 100 204 Q30 172 30 104 Z" fill="' + col + '" stroke="#C7922C" stroke-width="8"/>' +
    (o.split ? '<path d="M100 18 V200" stroke="#C7922C" stroke-width="4"/><path d="M34 94 H166" stroke="#C7922C" stroke-width="4"/>' : '') +
    '<g transform="translate(100 96) scale(2)">' + sym + '</g>' +
    (motto ? '<path d="M14 196 Q100 226 186 196 L180 222 Q100 250 20 222 Z" fill="#FFF8E9" stroke="#C7922C" stroke-width="3"/>' +
      '<text x="100" y="224" text-anchor="middle" font-family="Lora,Georgia,serif" font-weight="700" font-size="15" fill="#3B2A14">' + motto + '</text>' : '') +
    '</svg>';
}
function cardCrest(c, body) {
  var KEY = 'oao.g3ela.card.' + LID + '.' + c.id;
  var st = Sparkle.get(KEY, null) || { step: 0, mine: { color: 'Royal blue', symbol: 'owl', motto: '', split: false } };
  if (!CREST_COLORS[st.mine.color]) st.mine.color = 'Royal blue';
  body.insertAdjacentHTML('beforeend', lookCard(c.look, c.todo) + '<div class="g3-steps"></div>');
  var steps = body.querySelector('.g3-steps');
  function save() { Sparkle.set(KEY, st); }
  function reveal() {
    return artFig(c.art, 'g3-crest-real') + (c.revealText || []).map(function (p) { return '<p class="g3-p">' + p + '</p>'; }).join('');
  }
  function paint() {
    if (st.step === 0) {
      steps.innerHTML = stepHead(1, 2, c.step1 || 'Look at the saddle') +
        '<p class="g3-step-p">' + esc(c.step1p || '') + '</p>' +
        '<div class="g3-saddle"><svg viewBox="0 0 320 150" width="100%" style="max-width:360px" aria-hidden="true">' +
          '<rect x="0" y="0" width="320" height="150" rx="10" fill="#1E2433"/>' +
          '<path d="M0 150 Q80 120 160 132 Q240 120 320 150 Z" fill="#2B3247"/>' +
          '<path d="M64 110 Q72 64 128 66 Q166 44 206 66 Q258 64 262 110 Z" fill="#6B3E1E" stroke="#3B220E" stroke-width="3"/>' +
          '<path d="M60 112 H266" stroke="#3B220E" stroke-width="7" stroke-linecap="round"/>' +
          '<path d="M128 112 V140 M200 112 V140" stroke="#3B220E" stroke-width="4"/>' +
          '<circle cx="164" cy="88" r="14" fill="#4E2C12" stroke="#8C6A2E" stroke-width="2"/>' +
        '</svg></div>' +
        '<button type="button" class="spk-btn g3-lantern">🏮 Hold up the lantern</button>';
      steps.querySelector('.g3-lantern').onclick = function () { st.step = 1; save(); wgSfx('chime'); paint(); };
    } else if (st.step === 1) {
      steps.innerHTML = stepHead(1, 2, c.step1 || 'Look at the saddle') + reveal() +
        '<button type="button" class="spk-btn g3-next">Next: design your own crest →</button>' +
        '<p class="g3-opt">Step 2 is just for fun. You can skip it.</p>';
      steps.querySelector('.g3-next').onclick = function () { st.step = 2; save(); paint(); };
    } else {
      var m = st.mine;
      var colors = Object.keys(CREST_COLORS).map(function (k) {
        return '<button type="button" class="g3-sw' + (m.color === k ? ' sel' : '') + '" data-c="' + k + '" style="background:' + CREST_COLORS[k] + '" aria-label="' + k + '" title="' + k + '"></button>';
      }).join('');
      var syms = Object.keys(CREST_SYMBOLS).map(function (k) {
        return '<button type="button" class="g3-sym' + (m.symbol === k ? ' sel' : '') + '" data-s="' + k + '"><svg viewBox="-30 -30 60 60" width="40" aria-hidden="true">' + CREST_SYMBOLS[k] + '</svg><span>' + k + '</span></button>';
      }).join('');
      steps.innerHTML = '<details class="g3-redo"><summary>See the king’s crest again</summary>' + reveal() + '</details>' +
        stepHead(2, 2, c.step2 || 'Design your own crest') +
        '<p class="g3-step-p">' + esc(c.step2p || '') + '</p>' +
        '<div class="g3-crest-wrap"><div class="g3-crest-live">' + crestSVG(m, 200) + '</div><div class="g3-crest-tools">' +
          '<div class="g3-tl">1. Tap a color</div><div class="g3-row">' + colors + '</div>' +
          '<div class="g3-tl">2. Tap a picture</div><div class="g3-row g3-syms">' + syms + '</div>' +
          '<label class="g3-tl g3-chk"><input type="checkbox" class="g3-split"' + (m.split ? ' checked' : '') + '> Add gold lines across the shield</label>' +
          '<div class="g3-tl">3. Type one word for your banner</div>' +
          '<input class="g3-motto" maxlength="14" placeholder="Brave" value="' + esc(m.motto || '') + '"><div class="g3-warn" hidden></div>' +
          '<button type="button" class="spk-btn g3-dl">⬇ Save my crest as a picture</button>' +
        '</div></div>';
      var live = function () { steps.querySelector('.g3-crest-live').innerHTML = crestSVG(m, 200); save(); };
      steps.querySelectorAll('.g3-sw').forEach(function (b) { b.onclick = function () { m.color = b.getAttribute('data-c'); steps.querySelectorAll('.g3-sw').forEach(function (x) { x.classList.toggle('sel', x === b); }); live(); }; });
      steps.querySelectorAll('.g3-sym').forEach(function (b) { b.onclick = function () { m.symbol = b.getAttribute('data-s'); steps.querySelectorAll('.g3-sym').forEach(function (x) { x.classList.toggle('sel', x === b); }); live(); }; });
      steps.querySelector('.g3-split').onchange = function (e) { m.split = e.target.checked; live(); };
      var mi = steps.querySelector('.g3-motto'), warn = steps.querySelector('.g3-warn');
      mi.oninput = function () {
        var v = mi.value.replace(/[^A-Za-z \-']/g, '');
        if (v && nameProblem(v) === 'block') { warn.hidden = false; warn.textContent = 'Pick a kind word for your crest.'; return; }
        warn.hidden = true; m.motto = v; live();
      };
      steps.querySelector('.g3-dl').onclick = function () {
        var svg = crestSVG(m, 400).replace('<svg ', '<svg xmlns="http://www.w3.org/2000/svg" ');
        var img = new Image();
        img.onload = function () {
          var cv = document.createElement('canvas'); cv.width = 400; cv.height = 480;
          var cx = cv.getContext('2d'); cx.fillStyle = '#FFFDF4'; cx.fillRect(0, 0, 400, 480); cx.drawImage(img, 0, 0, 400, 480);
          var a = document.createElement('a'); a.download = 'my-crest.png'; a.href = cv.toDataURL('image/png');
          document.body.appendChild(a); a.click(); a.remove();
        };
        img.src = 'data:image/svg+xml;charset=utf-8,' + encodeURIComponent(svg);
      };
    }
  }
  paint();
}

function buildCards() {
  var C = DATA.cards; if (!C || !C.length) return;
  var ICON = { info: '👀', tapwords: '💬', crest: '🛡️', backward: '🔄' };
  /* reversed, so two cards anchored to the same activity keep DATA order */
  C.slice().reverse().forEach(function (c) {
    if (document.getElementById('g3card-' + c.id)) return;
    var at = g3Anchor(c); if (!at) return;
    var card = cardShell(c, c.icon || ICON[c.kind]);
    var body = card.querySelector('.spk-card-body');
    if (c.kind === 'info') cardInfo(c, body);
    else if (c.kind === 'tapwords') cardTapwords(c, body);
    else if (c.kind === 'crest') cardCrest(c, body);
    else if (c.kind === 'backward') cardBackward(c, body);
    else return;
    cardVoice(c.id, body);
    at.host.insertBefore(card, at.before || null);
  });
}

/* ── Opti beside every guide clip: he is the one talking ────────── */
function optiFaces() {
  document.querySelectorAll('.spk-guide-wrap, .spk-audio.spk-guide, #spkGreet .spk-audio').forEach(function (w) {
    var outer = w.parentElement && w.parentElement.closest('.spk-guide-wrap');
    if (outer) return;
    if (w.querySelector(':scope > .g3-opti-face')) return;
    var f = document.createElement('span'); f.className = 'g3-opti-face'; f.setAttribute('aria-hidden', 'true');
    f.innerHTML = owlSVG('opti', 46);
    w.classList.add('g3-opti-wrap'); w.insertBefore(f, w.firstChild);
    /* Opti shows only once one of his recordings is really there */
    var media = [].slice.call(w.querySelectorAll('.spk-audio, .spk-video'));
    if (w.matches('.spk-audio, .spk-video')) media.push(w);
    var shown = function () { return media.some(function (m) { return !m.hidden && m.isConnected; }); };
    f.hidden = !shown();
    if (f.hidden && window.MutationObserver) {
      var ob = new MutationObserver(function () { if (shown()) { f.hidden = false; ob.disconnect(); } });
      media.forEach(function (m) { ob.observe(m, { attributes: true, attributeFilter: ['hidden'] }); });
    }
  });
}

/* ── Up the North Tower: one round a day ────────────────────────────
   DATA.wordgame = { type:'tower', title, sub, look, todo, win, winWeek,
     items:[ {title, q, opts:[…], a:n, why, miss:{n:'…'}} ] }
   Day d starts with days 1…d-1's steps already lit, so the week climbs
   one tower and day 4 reaches Jemmy's chamber at the top. The game is
   practice beside the strand's own activity; it never replaces or
   fills a graded box. */
WORDGAME.tower = function (cfg) {
  var items = cfg.items || []; if (!items.length) return;
  var panel = document.getElementById('tab-words'); if (!panel) return;
  var anchor = panel.querySelector('.tab-next-wrap');
  var day = dayNum(LESSON.day), PER = items.length, TOTAL = PER * 4;
  var KEY = 'oao.g3ela.wg.' + LID;
  var st = Sparkle.get(KEY, null) || { i: 0, misses: 0 };
  if (st.i > PER) st.i = PER;
  var card = cardShell({ id: 'tower', kind: 'tower', title: cfg.title || 'Up the North Tower', sub: cfg.sub || '' }, '🏰');
  var body = card.querySelector('.spk-card-body');
  body.insertAdjacentHTML('beforeend', lookCard(cfg.look, cfg.todo) +
    '<div class="g3-tw-grid"><div class="g3-tower" aria-hidden="true"></div><div class="g3-tw-play" aria-live="polite"></div></div>');
  var towerEl = body.querySelector('.g3-tower'), play = body.querySelector('.g3-tw-play');
  function pos(k) {
    var row = Math.floor(k / 4), col = k % 4, dir = row % 2 === 0 ? 1 : -1;
    return { x: dir > 0 ? 58 + col * 26 : 136 - col * 26, y: 372 - k * 7.4 };
  }
  function towerSVG(lit) {
    var s = '<svg viewBox="0 0 220 420" width="100%" style="max-width:230px">' +
      '<defs><linearGradient id="g3TwSky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#1B2547"/><stop offset="1" stop-color="#4A5580"/></linearGradient></defs>' +
      '<rect width="220" height="420" fill="url(#g3TwSky)" rx="12"/>' +
      '<circle cx="182" cy="38" r="15" fill="#F4E7B8" opacity=".9"/>' +
      '<circle cx="30" cy="30" r="1.4" fill="#fff"/><circle cx="60" cy="58" r="1.1" fill="#fff"/><circle cx="196" cy="88" r="1.2" fill="#fff"/>' +
      '<path d="M48 392 V96 H38 V70 H56 V84 H74 V70 H92 V84 H110 V70 H128 V84 H146 V70 H164 V84 H182 V96 H172 V392 Z" fill="#9C927C" stroke="#5E5340" stroke-width="2"/>' +
      '<rect x="0" y="390" width="220" height="30" fill="#3E5A34"/>';
    for (var y = 112; y < 390; y += 20) s += '<path d="M48 ' + y + ' H172" stroke="#857B66" stroke-width="1"/>';
    var top = lit >= TOTAL;
    s += '<path d="M98 140 V114 Q110 98 122 114 V140 Z" fill="' + (top ? '#FFD86B' : '#2A2E3E') + '" stroke="#5E5340" stroke-width="2"/>';
    if (top) s += '<circle cx="110" cy="124" r="28" fill="#FFD86B" opacity=".25"/>';
    for (var k = 0; k < TOTAL; k++) {
      var p = pos(k), on = k < lit, today = k >= (day - 1) * PER && k < day * PER;
      s += '<rect x="' + p.x + '" y="' + p.y.toFixed(1) + '" width="24" height="6" rx="1.5" fill="' + (on ? '#F2C14E' : (today ? '#D9D1BB' : '#7E7563')) +
           '" stroke="' + (on ? '#B5841C' : '#5E5340') + '" stroke-width="1"/>';
    }
    var c = pos(Math.max(0, Math.min(lit, TOTAL) - 1));
    if (lit === 0) c = { x: 58, y: 384 };
    s += '<g transform="translate(' + (c.x + 12) + ' ' + (c.y - 9).toFixed(1) + ')"><circle r="10" fill="#FFD86B" opacity=".35"/>' +
         '<rect x="-3.5" y="-5" width="7" height="9" rx="1.5" fill="#FFD86B" stroke="#7A5A10"/><path d="M-2 -5 Q0 -9 2 -5" stroke="#7A5A10" fill="none"/></g>';
    return s + '</svg>';
  }
  function lit() { return (day - 1) * PER + st.i; }
  function paint(msg, ok, tried) {
    towerEl.innerHTML = towerSVG(lit());
    if (st.i >= PER) {
      play.innerHTML = '<div class="g3-finish">✓ ' + esc(day === 4 ? (cfg.winWeek || cfg.win || '') : (cfg.win || '')) + '</div>' +
        '<button type="button" class="spk-mini-btn g3-again">Play today’s round again</button>';
      play.querySelector('.g3-again').onclick = function () { st = { i: 0, misses: 0 }; Sparkle.set(KEY, st); paint(); };
      return;
    }
    var it = items[st.i];
    var h = stepHead(st.i + 1, PER, it.title || 'Climb one step') + '<p class="g3-tw-q">' + it.q + '</p><div class="g3-opts">';
    it.opts.forEach(function (o, n) { h += '<button type="button" class="g3-opt-btn' + (tried && tried.indexOf(n) >= 0 ? ' tried' : '') + '" data-n="' + n + '">' + esc(o) + '</button>'; });
    h += '</div>';
    if (msg) h += '<div class="g3-fb ' + (ok ? 'ok' : 'no') + '">' + msg + '</div>';
    play.innerHTML = h;
    play.querySelectorAll('.g3-opt-btn').forEach(function (b) {
      b.onclick = function () {
        var n = +b.getAttribute('data-n');
        if (n === it.a) {
          st.i++; Sparkle.set(KEY, st); wgSfx(st.i >= PER ? 'win' : 'chime');
          if (st.i >= PER) { paint(); return; }
          paint('✓ ' + (it.why || 'That’s the one.'), true);
        } else {
          st.misses++; Sparkle.set(KEY, st); wgSfx('bonk');
          var t = (tried || []).concat([n]);
          paint((it.miss || {})[n] || 'Not that one. Read it again, then try another.', false, t);
        }
      };
    });
  }
  paint();
  if (anchor) anchor.parentNode.insertBefore(card, anchor); else panel.appendChild(card);
};

/* ── Fill the Wagon: one round a day ────────────────────────────────
   DATA.wordgame = { type:'wagon', title, sub, look, todo, win, winWeek,
     bins:[ {id, label} ], items:[ {t, bin, why, miss:{binId:'…'}} ] }
   One thing to sort at a time: read it, tap the sack it belongs in. Each
   right answer drops a coin (every fourth one a jewel) into the outlaws'
   wagon. Day d starts with days 1…d-1's coins already in, so the week
   fills one wagon. Practice only; never fills a graded box. */
function wagonSVG(have, day, per) {
  var total = per * 4;
  var s = '<svg viewBox="0 0 240 190" width="100%" style="max-width:250px" role="img" aria-label="The wagon has ' + have + ' of ' + total + ' coins and jewels">' +
    '<rect width="240" height="190" rx="12" fill="#EAF1E4"/>' +
    '<path d="M0 160 Q120 150 240 160 V190 H0 Z" fill="#B9CFA4"/>' +
    '<path d="M186 120 L232 104" stroke="#6B4423" stroke-width="5" stroke-linecap="round"/>';
  /* the pile, drawn before the front board so it sits inside the wagon bed */
  for (var k = 0; k < total; k++) {
    var row = Math.floor(k / 8), col = k % 8;
    var x = 44 + col * 19 + (row % 2 ? 9 : 0), y = 99 - row * 12;
    var today = k >= (day - 1) * per && k < day * per;
    if (k < have) {
      if (k % 4 === 3) {
        var jc = ['#C0392B', '#2E6FB5', '#2F8F4E', '#8E44AD'][(k >> 2) % 4];
        s += '<path d="M' + x + ' ' + (y - 8) + ' l7 7 l-7 8 l-7 -8 Z" fill="' + jc + '" stroke="#3B2A14" stroke-width="1.2"/>' +
             '<path d="M' + (x - 3) + ' ' + (y - 3) + ' l3 -3" stroke="#fff" stroke-width="1.2" opacity=".7"/>';
      } else {
        s += '<ellipse cx="' + x + '" cy="' + y + '" rx="8" ry="6" fill="#F2C14E" stroke="#9A6B12" stroke-width="1.4"/>' +
             '<ellipse cx="' + x + '" cy="' + (y - 1) + '" rx="4" ry="2.6" fill="none" stroke="#C8901E" stroke-width="1"/>';
      }
    } else if (today && row < 3) {
      s += '<ellipse cx="' + x + '" cy="' + y + '" rx="8" ry="6" fill="none" stroke="#9A8A6A" stroke-width="1" stroke-dasharray="2 2" opacity=".6"/>';
    }
  }
  s += '<path d="M30 104 H196 L186 136 H40 Z" fill="#8A5A2B" stroke="#4E3016" stroke-width="2.5"/>' +
       '<path d="M34 114 H192 M37 125 H189" stroke="#6B4423" stroke-width="1.5"/>';
  [[62, 146], [166, 146]].forEach(function (w) {
    s += '<circle cx="' + w[0] + '" cy="' + w[1] + '" r="17" fill="#5E3A1A" stroke="#3B220E" stroke-width="3"/>' +
         '<circle cx="' + w[0] + '" cy="' + w[1] + '" r="4" fill="#C7922C"/>';
    for (var a = 0; a < 6; a++) {
      var r = a * Math.PI / 3;
      s += '<path d="M' + w[0] + ' ' + w[1] + ' L' + (w[0] + 15 * Math.cos(r)).toFixed(1) + ' ' + (w[1] + 15 * Math.sin(r)).toFixed(1) + '" stroke="#C9A46A" stroke-width="2"/>';
    }
  });
  if (have >= total) s += '<text x="120" y="24" text-anchor="middle" font-family="Nunito,sans-serif" font-weight="800" font-size="15" fill="#2F6B3B">A wagonload!</text>';
  return s + '</svg>';
}
WORDGAME.wagon = function (cfg) {
  var items = cfg.items || [], bins = cfg.bins || []; if (!items.length || bins.length < 2) return;
  var panel = document.getElementById('tab-words'); if (!panel) return;
  var anchor = panel.querySelector('.tab-next-wrap');
  var day = dayNum(LESSON.day), PER = items.length;
  var KEY = 'oao.g3ela.wg.' + LID;
  var st = Sparkle.get(KEY, null) || { i: 0, misses: 0 };
  if (st.i > PER) st.i = PER;
  var card = cardShell({ id: 'wagon', kind: 'wagon', title: cfg.title || 'Fill the Wagon', sub: cfg.sub || '' }, '💰');
  var body = card.querySelector('.spk-card-body');
  body.insertAdjacentHTML('beforeend', lookCard(cfg.look, cfg.todo) +
    '<div class="g3-tw-grid"><div class="g3-wagon"></div><div class="g3-tw-play" aria-live="polite"></div></div>');
  var wagonEl = body.querySelector('.g3-wagon'), play = body.querySelector('.g3-tw-play');
  function have() { return (day - 1) * PER + st.i; }
  function paint(msg, ok, tried) {
    wagonEl.innerHTML = wagonSVG(have(), day, PER);
    if (st.i >= PER) {
      play.innerHTML = '<div class="g3-finish">✓ ' + esc(day === 4 ? (cfg.winWeek || cfg.win || '') : (cfg.win || '')) + '</div>' +
        '<button type="button" class="spk-mini-btn g3-again">Play today’s round again</button>';
      play.querySelector('.g3-again').onclick = function () { st = { i: 0, misses: 0 }; Sparkle.set(KEY, st); paint(); };
      return;
    }
    var it = items[st.i];
    var h = stepHead(st.i + 1, PER, cfg.stepTitle || 'Which sack?') +
      '<div class="g3-wg-item">' + it.t + '</div><div class="g3-sacks">';
    bins.forEach(function (b) {
      h += '<button type="button" class="g3-sack' + (tried && tried.indexOf(b.id) >= 0 ? ' tried' : '') + '" data-b="' + esc(b.id) + '">' +
           '<span class="g3-sack-ic" aria-hidden="true">💰</span><span>' + esc(b.label) + '</span></button>';
    });
    h += '</div>';
    if (msg) h += '<div class="g3-fb ' + (ok ? 'ok' : 'no') + '">' + msg + '</div>';
    play.innerHTML = h;
    play.querySelectorAll('.g3-sack').forEach(function (b) {
      b.onclick = function () {
        var id = b.getAttribute('data-b');
        if (id === it.bin) {
          st.i++; Sparkle.set(KEY, st); wgSfx(st.i >= PER ? 'win' : 'chime');
          if (st.i >= PER) { paint(); return; }
          paint('✓ ' + (it.why || 'Into the wagon it goes.'), true);
          var pile = wagonEl.querySelector('svg'); if (pile) { pile.classList.remove('g3-clink'); void pile.getBoundingClientRect(); pile.classList.add('g3-clink'); }
        } else {
          st.misses++; Sparkle.set(KEY, st); wgSfx('bonk');
          paint((it.miss || {})[id] || 'Not that sack. Read it again, then try another.', false, (tried || []).concat([id]));
        }
      };
    });
  }
  paint();
  if (anchor) anchor.parentNode.insertBefore(card, anchor); else panel.appendChild(card);
};

/* card kind 'backward': read a note from the last word to the first (Billy's test),
   then rebuild it the right way round by tapping the words in order. Last step: why. */
function cardBackward(c, body) {
  var notes = c.notes || [], q = c.q; if (!notes.length) return;
  var N = notes.length + (q ? 1 : 0);
  var KEY = 'oao.g3ela.card.' + LID + '.' + c.id;
  var st = Sparkle.get(KEY, null) || { step: 0 };
  if (st.step > N) st.step = N;
  body.insertAdjacentHTML('beforeend', lookCard(c.look, c.todo) + '<div class="g3-steps" aria-live="polite"></div>');
  var steps = body.querySelector('.g3-steps');
  function save() { Sparkle.set(KEY, st); }
  function finish() {
    steps.innerHTML = (q && q.why ? '<div class="g3-fb ok">' + esc(q.why) + '</div>' : '') +
      '<div class="g3-finish">✓ ' + esc(c.finish || 'All done!') + '</div>' +
      '<button type="button" class="spk-mini-btn g3-again">Start again</button>';
    steps.querySelector('.g3-again').onclick = function () { st = { step: 0 }; save(); paint(); };
  }
  function noteStep(n) {
    var back = notes[n].back, fwd = back.slice().reverse(), got = 0;
    steps.innerHTML = stepHead(n + 1, N, notes[n].title || 'Turn the note around') +
      '<p class="g3-step-p">' + esc(c.stepText || 'Read the note out loud from the last word to the first. Then tap the words in the right order.') + '</p>' +
      '<div class="g3-bk-note"><span class="g3-bk-tag">The note, read backward</span>' + back.map(esc).join(' ') + '</div>' +
      '<div class="g3-bk-line" aria-label="Your note the right way round"><span class="g3-bk-tag">The right way round</span><span class="g3-bk-built"></span></div>' +
      '<div class="g3-bk-chips"></div><div class="g3-bk-fb"></div>';
    var chips = steps.querySelector('.g3-bk-chips'), built = steps.querySelector('.g3-bk-built'), fb = steps.querySelector('.g3-bk-fb');
    back.forEach(function (w, k) {
      var b = document.createElement('button'); b.type = 'button'; b.className = 'g3-bk-chip'; b.textContent = w;
      b.onclick = function () {
        if (b.disabled) return;
        if (w === fwd[got]) {
          b.disabled = true; b.classList.add('used'); got++;
          built.textContent = fwd.slice(0, got).join(' '); fb.innerHTML = '';
          if (got === fwd.length) {
            wgSfx('chime');
            fb.innerHTML = '<div class="g3-fb ok">✓ ' + esc(notes[n].done || 'You turned it around.') + '</div>' +
              '<button type="button" class="spk-btn g3-next">' + (n + 1 < N ? 'Next →' : 'Finish ✓') + '</button>';
            fb.querySelector('.g3-next').onclick = function () { st.step = n + 1; save(); paint(); };
          }
        } else {
          wgSfx('bonk'); b.classList.remove('g3-shake'); void b.offsetWidth; b.classList.add('g3-shake');
          fb.innerHTML = '<div class="g3-fb no">' + esc(got === 0 ? (c.missFirst || 'Not that one yet. The note starts with the last word you see.') : (c.missNext || 'Not that one yet. Look for the word just before the ones you used.')) + '</div>';
        }
      };
      chips.appendChild(b);
    });
  }
  function qStep(msg, ok, tried) {
    var h = stepHead(N, N, q.title || 'Why read it backward?') + '<p class="g3-tw-q">' + q.text + '</p><div class="g3-opts">';
    q.opts.forEach(function (o, n) { h += '<button type="button" class="g3-opt-btn' + (tried && tried.indexOf(n) >= 0 ? ' tried' : '') + '" data-n="' + n + '">' + esc(o) + '</button>'; });
    h += '</div>';
    if (msg) h += '<div class="g3-fb ' + (ok ? 'ok' : 'no') + '">' + msg + '</div>';
    steps.innerHTML = h;
    steps.querySelectorAll('.g3-opt-btn').forEach(function (b) {
      b.onclick = function () {
        var n = +b.getAttribute('data-n');
        if (n === q.a) {
          wgSfx('win'); st.step = N; save(); finish();
        } else {
          wgSfx('bonk'); qStep(esc((q.miss || {})[n] || 'Not that one. Read the choices again.'), false, (tried || []).concat([n]));
        }
      };
    });
  }
  function paint() {
    if (st.step >= N) { finish(); return; }
    if (st.step < notes.length) noteStep(st.step); else qStep();
  }
  paint();
}

/* ── tooltips never get cut off ─────────────────────────────────────
   The tip is placed with position:fixed against the viewport, so a
   card with overflow:hidden or the edge of the screen can't clip it.
   It sits above the word, or below when there isn't room, and the
   little arrow still points at the word. */
function placeTip(span) {
  var tip = span.querySelector('.g3-tip'); if (!tip) return;
  tip.classList.add('g3-tip-fixed');
  var r = span.querySelector('.g3-gl-w').getBoundingClientRect();
  var vw = document.documentElement.clientWidth, vh = window.innerHeight, pad = 8;
  tip.style.left = '0px'; tip.style.top = '0px'; tip.style.maxWidth = Math.min(300, vw - pad * 2) + 'px';
  var tw = tip.offsetWidth, th = tip.offsetHeight;
  var cx = r.left + r.width / 2;
  var left = Math.max(pad, Math.min(vw - pad - tw, cx - tw / 2));
  var above = r.top - th - 10 >= pad || r.bottom + th + 10 > vh;
  var top = above ? r.top - th - 10 : r.bottom + 10;
  tip.style.left = left + 'px'; tip.style.top = Math.max(pad, top) + 'px';
  tip.style.setProperty('--g3-arrow', Math.max(14, Math.min(tw - 14, cx - left)) + 'px');
  tip.classList.toggle('g3-tip-below', !above);
}
function hookTips() {
  document.querySelectorAll('.g3-gl').forEach(function (s) {
    if (s._g3tip) return; s._g3tip = true;
    ['mouseenter', 'focus', 'click'].forEach(function (ev) { s.addEventListener(ev, function () { placeTip(s); }); });
  });
  window.addEventListener('scroll', function () { document.querySelectorAll('.g3-gl.open, .g3-gl:hover, .g3-gl:focus-within').forEach(placeTip); }, { passive: true });
  window.addEventListener('resize', function () { document.querySelectorAll('.g3-gl.open').forEach(placeTip); });
}

/* ── the open book flips to today's page ────────────────────────────
   Every time the book comes into view (opening the Reading tab, or
   scrolling back to it), a few printed pages turn from right to left
   and the book settles on the page that is open now. The turning
   pages carry faint lines of print, a running head and a page number,
   so they read as pages of a book, never as blank sheets. Off with
   reduced motion. */
function bookLeafSide(back, n) {
  var h = '<div class="g3-leaf-side ' + (back ? 'g3-leaf-back' : 'g3-leaf-front') + '">' +
          '<div class="g3-leaf-head"></div>';
  var widths = [96, 100, 92, 100, 98, 88, 100, 95, 100, 70];
  for (var i = 0; i < widths.length; i++) {
    var w = widths[(i + n * 3) % widths.length];
    if (i === 4 || i === 9) w = 40 + ((n * 17 + i * 7) % 40);   /* paragraph ends */
    h += '<i style="width:' + w + '%"></i>';
  }
  return h + '<div class="g3-leaf-num">' + (back ? (n * 2) : (n * 2 + 1)) + '</div></div>';
}
function buildBookFlip() {
  var book = document.querySelector('.open-book'); if (!book || book.querySelector('.g3-flip')) return;
  var right = book.querySelector('.open-book-right'), left = book.querySelector('.open-book-left');
  if (!right || !left) return;
  var flip = document.createElement('div'); flip.className = 'g3-flip'; flip.setAttribute('aria-hidden', 'true');
  var N = 5, base = 3 + ((LESSON.week || 1) * 7) % 40;
  for (var k = 0; k < N; k++) {
    var leaf = document.createElement('div'); leaf.className = 'g3-leaf';
    leaf.style.setProperty('--d', (k * 0.16) + 's');
    leaf.style.zIndex = String(20 + N - k);
    leaf.innerHTML = bookLeafSide(false, base + k) + bookLeafSide(true, base + k + 1);
    flip.appendChild(leaf);
  }
  book.appendChild(flip);
  var playing = false;
  function play() {
    if (playing) return;
    var rm = false; try { rm = window.matchMedia('(prefers-reduced-motion: reduce)').matches; } catch (e) {}
    if (rm || document.documentElement.classList.contains('spk-motion-off')) return;
    playing = true;
    book.classList.remove('g3-flipping'); void book.offsetWidth;
    book.classList.add('g3-flipping');
    var total = (N - 1) * 160 + 900 + 150;
    setTimeout(function () { book.classList.remove('g3-flipping'); playing = false; }, total);
  }
  if ('IntersectionObserver' in window) {
    var seen = false;
    new IntersectionObserver(function (es) {
      es.forEach(function (e) {
        if (e.isIntersecting && e.intersectionRatio >= 0.5) { if (!seen) { seen = true; play(); } }
        else if (!e.isIntersecting) seen = false;           /* left the screen or the tab closed: play again next time */
      });
    }, { threshold: [0, 0.5] }).observe(book);
  }
}


/* ── read along with Opti ───────────────────────────────────────────
   Like G3 social studies: under each clip, "📄 Read along with Opti"
   opens Opti's words, and while the clip plays each word lights up as
   he says it (words already said go soft, the one he is on glows gold).
   Timing is shared out by word length, with a little extra for the
   pause after a comma or a full stop. */
function readAlongify(ra) {
  if (ra._g3ra) return; ra._g3ra = true;
  if (ra.classList.contains('g3-fold')) return;   // audit Nov 10: a folded card is not a clip's words (it showed a second "Read along with Opti")
  var wrap = ra.parentNode, au = wrap && wrap.querySelector('.spk-audio');
  var a = au && au._spkAudio; if (!a) return;
  var bodyEl = ra.querySelector('.spk-note-body'), sum = ra.querySelector('summary');
  var text = bodyEl.textContent, toks = text.split(/(\s+)/), html = '', weights = [], wi = 0;
  toks.forEach(function (w) {
    if (!w) return;
    if (/^\s+$/.test(w)) { html += /\n\s*\n/.test(w) ? '<br><br>' : ' '; return; }
    var wt = w.replace(/[^\w']/g, '').length + 2;
    if (/[.!?…]["”’)]*$/.test(w)) wt += 6; else if (/[,;:—–]["”’)]*$/.test(w)) wt += 3;
    weights.push(wt);
    html += '<span class="g3-w" data-w="' + (wi++) + '">' + esc(w) + '</span>';
  });
  bodyEl.innerHTML = html; bodyEl.classList.add('g3-ra-text');
  var ws = bodyEl.querySelectorAll('.g3-w'), cum = [], tot = 0;
  weights.forEach(function (x) { cum.push(tot); tot += x; });
  sum.textContent = '📄 Read along with Opti';
  ra.classList.add('g3-ra');
  var last = -2, raf = 0;
  function setWord(k) {
    if (k === last) return; last = k;
    for (var i = 0; i < ws.length; i++) { ws[i].classList.toggle('said', i < k); ws[i].classList.toggle('now', i === k); }
  }
  function frame() {
    if (a.duration) {
      var lead = 0.25, f = Math.min(1, Math.max(0, (a.currentTime - lead) / Math.max(0.5, a.duration - lead * 2))) * tot, k = 0;
      while (k + 1 < cum.length && cum[k + 1] <= f) k++;
      setWord(k);
    }
    if (!a.paused) raf = requestAnimationFrame(frame);
  }
  a.addEventListener('play', function () { ra.classList.add('g3-ra-live'); cancelAnimationFrame(raf); raf = requestAnimationFrame(frame); });
  a.addEventListener('pause', function () { cancelAnimationFrame(raf); });
  a.addEventListener('ended', function () { cancelAnimationFrame(raf); setWord(ws.length); ra.classList.remove('g3-ra-live'); });
  a.addEventListener('seeked', function () { if (a.currentTime < 0.1) setWord(-1); });
  /* tap a word to hear Opti from there */
  bodyEl.addEventListener('click', function (e) {
    var w = e.target.closest && e.target.closest('.g3-w'); if (!w || !a.duration) return;
    var k = +w.getAttribute('data-w'); a.currentTime = 0.25 + cum[k] / tot * Math.max(0.5, a.duration - 0.5);
    if (a.paused) au.querySelector('.spk-audio-btn').click();
  });
}
function buildReadAlong() {
  function scan() { document.querySelectorAll('.spk-readalong').forEach(readAlongify); }
  scan();
  if (window.MutationObserver) new MutationObserver(scan).observe(document.body, { childList: true, subtree: true });
}

/* ── the Character Spotlight block gets a stage ─────────────────── */
function buildSpotlight() {
  document.querySelectorAll('.activity').forEach(function (b) {
    var t = b.querySelector('.activity-title');
    if (!t || !/^Character Spotlight/i.test(t.textContent) || b.classList.contains('g3-spot')) return;
    b.classList.add('g3-spot');
    var head = b.querySelector('.activity-head');
    if (head) head.insertAdjacentHTML('afterbegin',
      '<svg class="g3-spot-beam" viewBox="0 0 400 120" preserveAspectRatio="none" aria-hidden="true"><defs><linearGradient id="g3beam" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFF1C4" stop-opacity=".75"/><stop offset="1" stop-color="#FFE9A8" stop-opacity="0"/></linearGradient></defs><path d="M338 0 L352 0 L420 120 L230 120 Z" fill="url(#g3beam)"/><ellipse cx="325" cy="118" rx="95" ry="10" fill="#FFE9A8" opacity=".22"/></svg>' +
      '<div class="g3-spot-lamp" aria-hidden="true"></div>');
  });
}

/* ── Opti reads the directions ──────────────────────────────────────
   Every "What to do:" line carries data-say="<slug>". A 🔊 in front of
   it plays Opti saying exactly those words:
   assets/audio/guide/opti/g3ela-how-<slug>.mp3 (shared by every lesson
   that uses the same words). The button stays hidden until the file is
   really there, so a line without a recording just reads as text. */
var SAY_FOR_CARD = { 'spk-copia-card': 'copia', 'g3card-tower': 'tower', 'g3card-wagon': 'wagon', 'g3card-backward': 'backward' };
function buildSayDo() {
  document.querySelectorAll('.g3-todo:not([data-say])').forEach(function (p) {
    for (var k in SAY_FOR_CARD) {
      if (p.closest('.' + k) || p.closest('#' + k)) { p.setAttribute('data-say', SAY_FOR_CARD[k]); break; }
    }
  });
  document.querySelectorAll('[data-say]').forEach(function (p) {
    if (p._g3say) return; p._g3say = true;
    var b = document.createElement('button');
    b.type = 'button'; b.className = 'g3-say'; b.hidden = true;
    b.setAttribute('aria-label', 'Hear Opti read the directions');
    b.innerHTML = '<span aria-hidden="true">🔊</span>';
    var a = new Audio(); a.preload = 'metadata';
    a.addEventListener('loadedmetadata', function () { b.hidden = false; });
    a.addEventListener('play', function () { b.classList.add('on'); });
    a.addEventListener('pause', function () { b.classList.remove('on'); });
    a.addEventListener('ended', function () { b.classList.remove('on'); });
    a.src = MEDIA.audioBase + 'guide/opti/g3ela-how-' + p.getAttribute('data-say') + '.mp3';
    b.onclick = function () {
      if (!a.paused) { a.pause(); return; }
      if (typeof audioStopAll === 'function') audioStopAll(a);
      _nowPlaying = a; a.currentTime = 0; a.play().catch(function () {});
    };
    p.insertBefore(b, p.firstChild);
  });
}

/* ══════════════════════════════════════════════════════════════
   OPTI TEACHES (pilot feedback, Nov 10 2026): fewer words on the page,
   more said out loud. Opti acts as the teacher: before each activity he
   gives the context and the instruction, then the student does it. The
   boxes he has explained fold away behind "📄 Read it instead".
     DATA.teach = {
       mods:  [ {id, find:'title regex' | sel:'css', script, fold:['css', …]} ],
       cards: { 'word': 'Opti reads the book sentence + meaning', … },
       dropTurnNotes: true      // the 3 "Opti · before …" tab notes go
     }
   Clip files: guide/opti/g3ela-W-D-teach-<id>.mp3 and -say-<word>.mp3.
   A clip that is not recorded yet keeps its row hidden, like every other
   slot (window.G3_PILOT_TTS lets a preview stand in a computer voice).
   ══════════════════════════════════════════════════════════════ */
function teachSrc(kind, id) {
  return MEDIA.audioBase + 'guide/opti/g3ela-' + LESSON.week + '-' + dayNum(LESSON.day) + '-' + kind + '-' + g3slug(id) + '.mp3';
}
function plainScript(t) { return String(t || '').replace(/\[[^\]]*\]\s*/g, '').trim(); }
var _ttsBtn = null;
function ttsSay(text, btn) {
  if (!window.speechSynthesis) return;
  speechSynthesis.cancel();
  if (_ttsBtn) _ttsBtn.classList.remove('on');
  if (_ttsBtn === btn) { _ttsBtn = null; return; }
  var u = new SpeechSynthesisUtterance(text), v = speechSynthesis.getVoices();
  u.voice = v.filter(function (x) { return /en[-_]US/i.test(x.lang) && /natural|aria|jenny|guy|google us/i.test(x.name); })[0] ||
            v.filter(function (x) { return /^en/i.test(x.lang); })[0] || null;
  u.rate = 0.95; u.pitch = 1.05;
  u.onend = function () { btn.classList.remove('on'); if (_ttsBtn === btn) _ttsBtn = null; };
  audioStopAll(); btn.classList.add('on'); _ttsBtn = btn; speechSynthesis.speak(u);
}
/* the player: Opti + one big button, real clip if it is there */
function teachPlayer(label, src, text, cls) {
  /* One button. It plays Opti's recorded clip when the file is there;
     until it is, the browser reads Opti's words aloud instead, so the
     live lesson works the same today as it will once the clips exist. */
  var row = document.createElement('div'); row.className = 'g3-teach ' + (cls || '');
  var secs = Math.max(5, Math.round(plainScript(text).length / 15));
  row.innerHTML = '<span class="g3-teach-face" aria-hidden="true">' + owlSVG('opti', 44) + '</span>';
  var b = document.createElement('button'); b.type = 'button'; b.className = 'g3-teach-btn';
  b.innerHTML = '<span class="g3-teach-ico">▶</span> ' + esc(label) + ' <span class="g3-teach-t">' + Math.floor(secs / 60) + ':' + ('0' + secs % 60).slice(-2) + '</span>';
  var a = null, real = false;
  if (!window.G3_PILOT_TTS) {
    a = new Audio(); a.preload = 'metadata';
    a.addEventListener('loadedmetadata', function () { real = true; });
    a.addEventListener('ended', function () { b.classList.remove('on'); });
    a.addEventListener('pause', function () { b.classList.remove('on'); });
    a.src = src;
  }
  b.onclick = function () {
    if (real && a) {
      if (!a.paused) { a.pause(); return; }
      if (window.speechSynthesis) speechSynthesis.cancel();
      audioStopAll(a); _nowPlaying = a; try { a.currentTime = 0; } catch (e) {}
      b.classList.add('on'); a.play().catch(function () { b.classList.remove('on'); });
    } else ttsSay(plainScript(text), b);
  };
  row.appendChild(b);
  return row;
}
function findMod(m) {
  if (m.sel) return document.querySelector(m.sel);
  var re = new RegExp(m.find, 'i'), t = document.querySelectorAll('.activity-title, .spk-card-title');
  for (var i = 0; i < t.length; i++) if (re.test(t[i].textContent || '')) return t[i].closest('.activity, .spk-card');
  return null;
}
/* Opti-teaches mode is on for every lesson whose DATA has `teach`
   (Bethany, Nov 10 2026: the live lesson IS the pilot). Each button
   plays the recorded clip when it exists, else the browser voice.
   ?pilot=1 / G3_PILOT_TTS forces the browser voice (previews). */
if (/[?&]pilot=1(&|$)/.test(location.search)) window.G3_PILOT_TTS = true;
function buildTeach() {
  var T = DATA.teach;
  if (!T) { if (DATA.howto) { try { buildHowTo(); } catch (e) {} } return; }
  if (document.querySelector('.g3-teach')) return;
  applyTeach(T);
}
function applyTeach(T) {
  if (document.body.classList.contains('g3-teaching')) return;
  document.body.classList.add('g3-teaching');
  /* One step at a time (Nov 11 2026): same onestep.js as G4/G5 plus the G3 rules; ?steps=0 turns it off */
  try { if (!/[?&]steps=0/.test(location.search) && !document.querySelector('script[src="onestep.js"]')) {
    var osl = document.createElement('link'); osl.rel = 'stylesheet'; osl.href = 'onestep.css'; document.head.appendChild(osl);
    var oss = document.createElement('script'); oss.src = 'onestep.js'; document.body.appendChild(oss); } } catch (e) {}
  /* the greeting rebuilds media after a name is typed, so hide by class */
  if (T.dropTurnNotes) document.body.classList.add('g3-no-turnnotes');
  (T.mods || []).forEach(function (m) {
    var mod = findMod(m); if (!mod) return;
    var body = mod.querySelector('.activity-body, .spk-card-body') || mod;
    var row = m.script ? teachPlayer(m.label || 'Opti teaches this', teachSrc('teach', m.id), m.script) : null;
    var folds = [];
    (m.fold || []).forEach(function (s) { body.querySelectorAll(s).forEach(function (e) { if (folds.indexOf(e) < 0) folds.push(e); }); });
    (m.foldText || []).forEach(function (rx) {
      var re = new RegExp(rx, 'i');
      [].forEach.call(body.children, function (e) { if (re.test(e.textContent || '') && folds.indexOf(e) < 0) folds.push(e); });
    });
    if (row) body.insertBefore(row, body.firstChild);
    if (row || folds.length) {
      var d = document.createElement('details'); d.className = 'spk-note spk-readalong g3-fold';
      d.innerHTML = '<summary>' + (m.script ? '📄 Read Opti’s words' : '📖 Read more about this') + '</summary>';
      var inner = document.createElement('div'); inner.className = 'spk-note-body';
      if (m.script) { var p = document.createElement('p'); p.className = 'g3-fold-words'; p.textContent = plainScript(m.script); inner.appendChild(p); }
      folds.forEach(function (e) { inner.appendChild(e); });
      d.appendChild(inner);
      var prev = row || body.querySelector(':scope > .g3-opti-row');
      body.insertBefore(d, prev ? prev.nextSibling : body.firstChild);
      /* Opti's teaching ends on the instruction, so the What to do line
         keeps its words but loses its own 🔊 */
      if (row) body.querySelectorAll('.g3-do .g3-say, .g3-todo .g3-say, .g3-do .g3-saydo, .g3-todo .g3-saydo').forEach(function (x) { x.remove(); });
      /* a shorter What to do: Opti has already explained the rest */
      var td = m.todo && body.querySelector('.g3-do, .g3-todo');
      if (td) td.innerHTML = '<b>What to do:</b> ' + m.todo;
    }
  });
  /* every vocabulary card: Opti reads the book's sentence and the meaning */
  var C = T.cards || {};
  if (Object.keys(C).length) document.body.classList.add('g3-cards-said');
  document.querySelectorAll('.vocab-decode-item').forEach(function (it) {
    var w = ((it.querySelector('.fc-word') || {}).textContent || '').trim(), s = C[w] || C[w.toLowerCase()];
    if (!s || it.querySelector('.g3-teach')) return;
    var r = teachPlayer('Opti reads it', teachSrc('say', w), s, 'g3-teach-sm');
    if (r) it.insertBefore(r, it.firstChild);
  });
  try { buildHowTo(); } catch (e) {}
}

/* ── How to use your lesson (pilot feedback, Nov 10 2026): Opti's
   1-minute tour, one video for the whole course, in a "Start here"
   drawer at the very top of the lesson, under the key line. Always shown (one course-wide
   file, committed with the layer), with a poster so the card is never
   blank before the video loads. ── */
function buildHowTo() {
  if (document.querySelector('.g3-start') || !(document.body.classList.contains('g3-teaching') || DATA.howto)) return;
  var src = window.G3_HOWTO_SRC || 'assets/video/g3ela-howto.mp4';
  var poster = window.G3_HOWTO_POSTER || 'assets/video/g3ela-howto.jpg';
  var card = document.createElement('details'); card.className = 'g3-start';
  card.innerHTML = '<summary class="g3-start-bar"><span class="g3-start-play" aria-hidden="true">▶</span>' +
    '<span class="g3-start-txt"><span class="g3-start-k">Start here</span>' +
    '<span class="g3-start-t">Watch how to use your lesson · 1 minute</span></span>' +
    '<span class="g3-start-face" aria-hidden="true">' + owlSVG('opti', 46) + '</span>' +
    '<span class="g3-start-chev" aria-hidden="true">▾</span></summary>' +
    '<div class="g3-howto"><video class="g3-howto-v" controls preload="metadata" playsinline></video></div>';
  var v = card.querySelector('video');
  v.poster = poster;
  v.addEventListener('play', function () { audioStopAll(); });
  v.src = src;
  card.addEventListener('toggle', function () { if (!card.open) { try { v.pause(); } catch (e) {} } });
  var key = document.querySelector('.g3-tapkey') || document.querySelector('.spk-hd, .header');
  if (key && key.parentNode) key.parentNode.insertBefore(card, key.nextSibling);
  else document.body.insertBefore(card, document.body.firstChild);
}
