/* ══════════════════════════════════════════════════════════════
   G3 ELA ADDITIONS (Nov 2026): Opti's Story Map
   Everything here is driven by the lesson's own DATA. Nothing below
   names a lesson, a book or a chapter.
     DATA.glossary  = [ {w, m, key} ]      dotted words, 🔊 on key words
     DATA.sayWords  = [ 'word', … ]          🔊 on the vocab cards (says just the word)
     DATA.cards     = [ {id, kind, tab, after, title, sub, look, todo, …} ]
     DATA.wordgame  = {type:'tower'|'wagon'|'chase'|'sewer'|'castle'|'illuminate'|'market'|'wardrobe'|'delight', …}  Up the North Tower / Fill the Wagon / The Chase / Out of the Sewer / Build the Castle / Illuminate the Page  / Market Day / Through the Wardrobe
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

/* ── The Chase: one round a day (week 20, Ch. 13) ───────────────────
   DATA.wordgame = { type:'chase', title, sub, look, todo, win, winWeek,
     items:[ {title, q, opts:[…], a:n, why, miss:{n:'…'}} ] }
   Same play as Up the North Tower (one question at a time). Each right
   answer moves Jemmy one stone along the forest path, with Cutwater
   three stones behind. Day d starts with days 1…d-1's stones done, so
   the week is one chase and day 4 reaches the hollow tree. Practice
   only; never fills a graded box. */
function chaseSVG(lit, day, per) {
  var total = per * 4;
  function pos(k) {
    var row = k < total / 2 ? 0 : 1, c = row ? k - total / 2 : k, n = total / 2;
    var x = row ? 286 - c * (240 / (n - 1)) : 34 + c * (240 / (n - 1));
    return { x: x, y: row ? 132 + Math.sin(c * 0.9) * 3 : 66 + Math.sin(c * 0.9) * 3 };
  }
  var s = '<svg viewBox="0 0 320 180" width="100%" style="max-width:340px" role="img" aria-label="Jemmy has run ' + Math.min(lit, total) + ' of ' + total + ' steps toward the hollow tree">' +
    '<rect width="320" height="180" rx="12" fill="#DCE8CF"/>' +
    '<path d="M24 66 H296 Q312 66 312 99 Q312 132 296 132 H24" fill="none" stroke="#C9B48A" stroke-width="16" stroke-linecap="round"/>';
  [[18, 30], [62, 24], [110, 32], [158, 22], [206, 30], [252, 24], [298, 30], [60, 102], [120, 96], [180, 104], [240, 98], [90, 168], [150, 172], [210, 166], [270, 170]].forEach(function (t, i) {
    var h = 22 + (i % 3) * 4;
    s += '<rect x="' + (t[0] - 2) + '" y="' + (t[1] + h * 0.35) + '" width="4" height="7" fill="#6B4423"/>' +
         '<path d="M' + t[0] + ' ' + (t[1] - h * 0.65) + ' L' + (t[0] + 10) + ' ' + (t[1] + h * 0.35) + ' L' + (t[0] - 10) + ' ' + (t[1] + h * 0.35) + ' Z" fill="' + (i % 2 ? '#3E6B3A' : '#4F7D45') + '"/>';
  });
  /* the hollow tree at the end of the path */
  var done = lit >= total;
  s += '<g transform="translate(14 112)"><rect x="-2" y="0" width="22" height="34" rx="6" fill="#8A6A44" stroke="#5A4128" stroke-width="2"/>' +
       '<ellipse cx="9" cy="20" rx="6" ry="9" fill="' + (done ? '#FFD86B' : '#3A2A18') + '"/>' +
       '<path d="M-4 34 Q-10 40 -12 44 M20 34 Q26 40 30 44" stroke="#5A4128" stroke-width="3" fill="none"/></g>';
  if (done) s += '<circle cx="23" cy="132" r="22" fill="#FFD86B" opacity=".28"/>';
  for (var k = 0; k < total; k++) {
    var p = pos(k), on = k < lit, today = k >= (day - 1) * per && k < day * per;
    s += '<ellipse cx="' + p.x.toFixed(1) + '" cy="' + p.y.toFixed(1) + '" rx="6" ry="3.6" fill="' + (on ? '#F2C14E' : (today ? '#EFE6CC' : '#A89C80')) +
         '" stroke="' + (on ? '#B5841C' : '#7E7258') + '" stroke-width="1"/>';
  }
  function person(x, y, col, tall) {
    var t = tall ? 1.25 : 1;
    return '<g transform="translate(' + x.toFixed(1) + ' ' + y.toFixed(1) + ') scale(' + t + ')">' +
      '<path d="M-3 0 L-4 -10 M3 0 L4 -10" stroke="#3B2A14" stroke-width="2"/>' +
      '<rect x="-5" y="-21" width="10" height="12" rx="3" fill="' + col + '"/>' +
      '<circle cy="-25" r="4" fill="#E8C9A4" stroke="#3B2A14" stroke-width=".8"/></g>';
  }
  if (!done) {
    var j = pos(Math.max(0, Math.min(lit, total) - 1)); if (lit === 0) j = { x: 34, y: 66 };
    if (lit >= 3) { var c = pos(lit - 3); s += person(c.x, c.y - 2, '#6E6A63', true); }
    s += person(j.x, j.y - 2, '#2E6FB5', false);
  } else {
    s += '<text x="170" y="104" text-anchor="middle" font-family="Nunito,sans-serif" font-weight="800" font-size="15" fill="#2F6B3B">Safe in the hollow tree!</text>';
  }
  return s + '</svg>';
}
WORDGAME.chase = function (cfg) {
  var items = cfg.items || []; if (!items.length) return;
  var panel = document.getElementById('tab-words'); if (!panel) return;
  var anchor = panel.querySelector('.tab-next-wrap');
  var day = dayNum(LESSON.day), PER = items.length;
  var KEY = 'oao.g3ela.wg.' + LID;
  var st = Sparkle.get(KEY, null) || { i: 0, misses: 0 };
  if (st.i > PER) st.i = PER;
  var card = cardShell({ id: 'chase', kind: 'chase', title: cfg.title || 'The Chase', sub: cfg.sub || '' }, '🌲');
  var body = card.querySelector('.spk-card-body');
  body.insertAdjacentHTML('beforeend', lookCard(cfg.look, cfg.todo) +
    '<div class="g3-tw-grid"><div class="g3-chase"></div><div class="g3-tw-play" aria-live="polite"></div></div>');
  var pathEl = body.querySelector('.g3-chase'), play = body.querySelector('.g3-tw-play');
  function lit() { return (day - 1) * PER + st.i; }
  function paint(msg, ok, tried) {
    pathEl.innerHTML = chaseSVG(lit(), day, PER);
    if (st.i >= PER) {
      play.innerHTML = '<div class="g3-finish">✓ ' + esc(day === 4 ? (cfg.winWeek || cfg.win || '') : (cfg.win || '')) + '</div>' +
        '<button type="button" class="spk-mini-btn g3-again">Play today’s round again</button>';
      play.querySelector('.g3-again').onclick = function () { st = { i: 0, misses: 0 }; Sparkle.set(KEY, st); paint(); };
      return;
    }
    var it = items[st.i];
    var h = stepHead(st.i + 1, PER, it.title || 'Run one step') + '<p class="g3-tw-q">' + it.q + '</p><div class="g3-opts">';
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

/* ── Out of the Sewer: one round a day (week 21, Ch. 19) ────────────
   DATA.wordgame = { type:'sewer', title, sub, look, todo, win, winWeek,
     items:[ {title, q, opts:[left, right], a:0|1, why, miss:{n:'…'}} ] }
   Each question is a fork with two tunnels. The right tunnel moves Jemmy
   and the prince one lamp closer to daylight; the wrong one gets a squeak
   from the brewery rats. Day d starts with days 1…d-1's lamps lit, so the
   week is one escape and day 4 reaches the river. Practice only; never
   fills a graded box. */
function sewerSVG(lit, day, per) {
  var total = per * 4, n = total / 2;
  function pos(k) {
    var row = k < n ? 0 : 1, c = row ? k - n : k;
    var x = row ? 278 - c * (232 / (n - 1)) : 46 + c * (232 / (n - 1));
    return { x: x, y: row ? 136 : 62 };
  }
  var s = '<svg viewBox="0 0 320 180" width="100%" style="max-width:340px" role="img" aria-label="Jemmy and the prince have passed ' + Math.min(lit, total) + ' of ' + total + ' lamps on the way out of the sewer">' +
    '<rect width="320" height="180" rx="12" fill="#3A3330"/>';
  /* brick courses */
  for (var r = 0; r < 9; r++) for (var b = 0; b < 9; b++) {
    s += '<rect x="' + (b * 38 - (r % 2 ? 19 : 0) + 2) + '" y="' + (r * 20 + 2) + '" width="34" height="16" rx="2" fill="' + ((r + b) % 3 ? '#4A403B' : '#544843') + '"/>';
  }
  /* the tunnel: two arched passages joined by a bend */
  s += '<path d="M30 62 H290 Q308 62 308 99 Q308 136 290 136 H30" fill="none" stroke="#1E1A18" stroke-width="34" stroke-linecap="round"/>' +
       '<path d="M30 70 H290 Q300 70 300 99 Q300 128 290 128" fill="none" stroke="#2F4A52" stroke-width="6" opacity=".9"/>' +
       '<path d="M290 136 H30" fill="none" stroke="#2F4A52" stroke-width="6" transform="translate(0 8)" opacity=".9"/>';
  /* side tunnels toward the brewery (where the rats are) */
  [[96, 40], [196, 40], [140, 158], [240, 158]].forEach(function (t) {
    s += '<path d="M' + (t[0] - 9) + ' ' + (t[1] + (t[1] < 99 ? 8 : -8)) + ' a9 9 0 0 1 18 0" fill="#141110" stroke="#1E1A18" stroke-width="2" transform="' + (t[1] > 99 ? 'rotate(180 ' + t[0] + ' ' + t[1] + ')' : '') + '"/>';
  });
  /* daylight at the river mouth (end of the bottom passage) */
  var done = lit >= total;
  s += '<circle cx="24" cy="136" r="' + (done ? 26 : 15) + '" fill="#FFE9A8" opacity="' + (done ? '.95' : (0.25 + 0.6 * Math.min(lit, total) / total).toFixed(2)) + '"/>' +
       '<path d="M8 150 Q24 144 40 150" stroke="#6FA8C8" stroke-width="3" fill="none"/>';
  for (var k = 0; k < total; k++) {
    var p = pos(k), on = k < lit, today = k >= (day - 1) * per && k < day * per;
    s += '<g transform="translate(' + p.x.toFixed(1) + ' ' + (p.y - 15) + ')">' +
         (on ? '<circle r="7" fill="#FFD86B" opacity=".35"/>' : '') +
         '<rect x="-2.5" y="-3" width="5" height="6" rx="1.5" fill="' + (on ? '#FFD86B' : (today ? '#8C8070' : '#5E5650')) + '" stroke="#211C19" stroke-width=".8"/></g>';
  }
  function person(x, y, col) {
    return '<g transform="translate(' + x.toFixed(1) + ' ' + y.toFixed(1) + ')">' +
      '<path d="M-3 0 L-4 -10 M3 0 L4 -10" stroke="#E8DCC8" stroke-width="2"/>' +
      '<rect x="-5" y="-21" width="10" height="12" rx="3" fill="' + col + '"/>' +
      '<circle cy="-25" r="4" fill="#E8C9A4" stroke="#211C19" stroke-width=".8"/></g>';
  }
  if (!done) {
    var j = lit === 0 ? { x: 46, y: 62 } : pos(Math.min(lit, total) - 1);
    var dir = (lit <= n) ? -1 : 1;
    s += person(j.x + dir * 9, j.y + 10, '#B5473A') + person(j.x, j.y + 10, '#2E6FB5') +
         '<path d="M' + (j.x + dir * 4).toFixed(1) + ' ' + (j.y - 4) + ' h' + (dir * 1) + '" stroke="#E8C9A4" stroke-width="2"/>';
  } else {
    s += person(30, 160, '#2E6FB5') + person(44, 160, '#B5473A') +
         '<text x="176" y="104" text-anchor="middle" font-family="Nunito,sans-serif" font-weight="800" font-size="15" fill="#FFE9A8">Out into the sunshine!</text>';
  }
  return s + '</svg>';
}
WORDGAME.sewer = function (cfg) {
  var items = cfg.items || []; if (!items.length) return;
  var panel = document.getElementById('tab-words'); if (!panel) return;
  var anchor = panel.querySelector('.tab-next-wrap');
  var day = dayNum(LESSON.day), PER = items.length;
  var KEY = 'oao.g3ela.wg.' + LID;
  var st = Sparkle.get(KEY, null) || { i: 0, misses: 0 };
  if (st.i > PER) st.i = PER;
  var card = cardShell({ id: 'sewer', kind: 'sewer', title: cfg.title || 'Out of the Sewer', sub: cfg.sub || '' }, '🕯️');
  var body = card.querySelector('.spk-card-body');
  body.insertAdjacentHTML('beforeend', lookCard(cfg.look, cfg.todo) +
    '<div class="g3-tw-grid"><div class="g3-sewer"></div><div class="g3-tw-play" aria-live="polite"></div></div>');
  var mapEl = body.querySelector('.g3-sewer'), play = body.querySelector('.g3-tw-play');
  function lit() { return (day - 1) * PER + st.i; }
  function paint(msg, ok, tried) {
    mapEl.innerHTML = sewerSVG(lit(), day, PER);
    if (st.i >= PER) {
      play.innerHTML = '<div class="g3-finish">✓ ' + esc(day === 4 ? (cfg.winWeek || cfg.win || '') : (cfg.win || '')) + '</div>' +
        '<button type="button" class="spk-mini-btn g3-again">Play today’s round again</button>';
      play.querySelector('.g3-again').onclick = function () { st = { i: 0, misses: 0 }; Sparkle.set(KEY, st); paint(); };
      return;
    }
    var it = items[st.i], side = ['Left tunnel', 'Right tunnel'];
    var h = stepHead(st.i + 1, PER, it.title || 'Pick a tunnel') + '<p class="g3-tw-q">' + it.q + '</p><div class="g3-opts g3-tunnels">';
    it.opts.forEach(function (o, n) {
      h += '<button type="button" class="g3-opt-btn g3-tunnel' + (tried && tried.indexOf(n) >= 0 ? ' tried' : '') + '" data-n="' + n + '">' +
        '<span class="g3-tunnel-tag">' + side[n] + '</span><span class="g3-tunnel-txt">' + esc(o) + '</span></button>';
    });
    h += '</div>';
    if (msg) h += '<div class="g3-fb ' + (ok ? 'ok' : 'no') + '">' + msg + '</div>';
    play.innerHTML = h;
    play.querySelectorAll('.g3-opt-btn').forEach(function (b) {
      b.onclick = function () {
        var n = +b.getAttribute('data-n');
        if (n === it.a) {
          st.i++; Sparkle.set(KEY, st); wgSfx(st.i >= PER ? 'win' : 'chime');
          if (st.i >= PER) { paint(); return; }
          paint('✓ ' + (it.why || 'That’s the way out.'), true);
        } else {
          st.misses++; Sparkle.set(KEY, st); wgSfx('bonk');
          var t = (tried || []).concat([n]);
          paint('🐀 Squeak! ' + ((it.miss || {})[n] || 'Rats down that way. Read it again, then try the other tunnel.'), false, t);
        }
      };
    });
  }
  paint();
  if (anchor) anchor.parentNode.insertBefore(card, anchor); else panel.appendChild(card);
};

/* ── Build the Castle: one round a day (week 22, struct = build) ────
   DATA.wordgame = { type:'castle', title, sub, look, todo, win, winWeek,
     items:[ {title, q, opts:[…2 or 3], a, why, miss:{n:'…'}} ] }
   Each right answer lays one stone in the castle wall, bottom row first,
   so every stone sits on the row below it. Day d starts with days
   1…d-1's stones laid, so the week builds one castle; day 4 adds the
   towers, the gate and the flag. Practice only; never fills a graded box. */
function castleSVG(laid, day, per) {
  var total = per * 4, cols = 8, W = 27, H = 17, x0 = 52, g = 148;
  var s = '<svg viewBox="0 0 320 180" width="100%" style="max-width:340px" role="img" aria-label="' + Math.min(laid, total) + ' of ' + total + ' stones are laid in the castle wall">' +
    '<rect width="320" height="180" rx="12" fill="#DCEBF5"/>' +
    '<path d="M0 ' + g + ' H320 V180 H0 Z" fill="#9DBF7E"/><path d="M0 ' + g + ' H320" stroke="#6E9254" stroke-width="2"/>';
  var done = laid >= total;
  /* towers: a dashed builder's plan until the wall is finished */
  [[20, 32], [268, 32]].forEach(function (t) {
    if (done) {
      s += '<rect x="' + t[0] + '" y="52" width="' + t[1] + '" height="' + (g - 52) + '" fill="#B9AE9C" stroke="#6B6152" stroke-width="1.5"/>';
      for (var yy = 60; yy < g; yy += 14) s += '<path d="M' + t[0] + ' ' + yy + ' h' + t[1] + '" stroke="#8D8272" stroke-width="1"/>';
      for (var c = 0; c < 4; c++) s += '<rect x="' + (t[0] + c * 8.7) + '" y="44" width="5.5" height="9" fill="#B9AE9C" stroke="#6B6152" stroke-width="1.2"/>';
      s += '<rect x="' + (t[0] + 12) + '" y="74" width="8" height="12" rx="4" fill="#3B3328"/>';
    } else {
      s += '<rect x="' + t[0] + '" y="52" width="' + t[1] + '" height="' + (g - 52) + '" fill="none" stroke="#7F93A6" stroke-width="1.2" stroke-dasharray="4 3"/>';
    }
  });
  for (var k = 0; k < total; k++) {
    var r = Math.floor(k / cols), c2 = k % cols;
    var x = x0 + c2 * W, y = g - (r + 1) * H;
    var today = k >= (day - 1) * per && k < day * per;
    if (k < laid) {
      var shade = ['#C8BDA9', '#BDB29E', '#D1C7B4'][(k * 7) % 3];
      s += '<rect x="' + (x + 0.8) + '" y="' + (y + 0.8) + '" width="' + (W - 1.6) + '" height="' + (H - 1.6) + '" rx="2" fill="' + shade + '" stroke="#6B6152" stroke-width="1.2"/>';
    } else {
      s += '<rect x="' + (x + 0.8) + '" y="' + (y + 0.8) + '" width="' + (W - 1.6) + '" height="' + (H - 1.6) + '" rx="2" fill="none" stroke="' + (today ? '#8A6212' : '#9FB0C0') + '" stroke-width="1" stroke-dasharray="3 2" opacity="' + (today ? '.9' : '.5') + '"/>';
    }
  }
  if (done) {
    var top = g - 4 * H;
    for (var b = 0; b < cols; b += 2) s += '<rect x="' + (x0 + b * W + 4) + '" y="' + (top - 9) + '" width="' + (W - 8) + '" height="9" fill="#C8BDA9" stroke="#6B6152" stroke-width="1.2"/>';
    s += '<path d="M146 ' + g + ' V' + (g - 22) + ' a14 14 0 0 1 28 0 V' + g + ' Z" fill="#7A4E26" stroke="#4E3016" stroke-width="1.5"/>' +
         '<path d="M160 ' + (g - 36) + ' V' + g + '" stroke="#4E3016" stroke-width="1"/>' +
         '<path d="M284 44 V16" stroke="#4E3016" stroke-width="1.6"/><path d="M284 16 l16 5 l-16 5 Z" fill="#B5473A"/>' +
         '<text x="160" y="30" text-anchor="middle" font-family="Nunito,sans-serif" font-weight="800" font-size="15" fill="#2E4A66">The castle is built!</text>';
  }
  return s + '</svg>';
}
WORDGAME.castle = function (cfg) {
  var items = cfg.items || []; if (!items.length) return;
  var panel = document.getElementById('tab-words'); if (!panel) return;
  var anchor = panel.querySelector('.tab-next-wrap');
  var day = dayNum(LESSON.day), PER = items.length;
  var KEY = 'oao.g3ela.wg.' + LID;
  var st = Sparkle.get(KEY, null) || { i: 0, misses: 0 };
  if (st.i > PER) st.i = PER;
  var card = cardShell({ id: 'castle', kind: 'castle', title: cfg.title || 'Build the Castle', sub: cfg.sub || '' }, '🏰');
  var body = card.querySelector('.spk-card-body');
  body.insertAdjacentHTML('beforeend', lookCard(cfg.look, cfg.todo) +
    '<div class="g3-tw-grid"><div class="g3-castle"></div><div class="g3-tw-play" aria-live="polite"></div></div>');
  var mapEl = body.querySelector('.g3-castle'), play = body.querySelector('.g3-tw-play');
  function laid() { return (day - 1) * PER + st.i; }
  function paint(msg, ok, tried) {
    mapEl.innerHTML = castleSVG(laid(), day, PER);
    if (st.i >= PER) {
      play.innerHTML = '<div class="g3-finish">✓ ' + esc(day === 4 ? (cfg.winWeek || cfg.win || '') : (cfg.win || '')) + '</div>' +
        '<button type="button" class="spk-mini-btn g3-again">Play today’s round again</button>';
      play.querySelector('.g3-again').onclick = function () { st = { i: 0, misses: 0 }; Sparkle.set(KEY, st); paint(); };
      return;
    }
    var it = items[st.i];
    var h = stepHead(st.i + 1, PER, it.title || 'Lay a stone') + '<p class="g3-tw-q">' + it.q + '</p><div class="g3-opts">';
    it.opts.forEach(function (o, n) {
      h += '<button type="button" class="g3-opt-btn' + (tried && tried.indexOf(n) >= 0 ? ' tried' : '') + '" data-n="' + n + '">' + esc(o) + '</button>';
    });
    h += '</div>';
    if (msg) h += '<div class="g3-fb ' + (ok ? 'ok' : 'no') + '">' + msg + '</div>';
    play.innerHTML = h;
    play.querySelectorAll('.g3-opt-btn').forEach(function (b) {
      b.onclick = function () {
        var n = +b.getAttribute('data-n');
        if (n === it.a) {
          st.i++; Sparkle.set(KEY, st); wgSfx(st.i >= PER ? 'win' : 'chime');
          if (st.i >= PER) { paint(); return; }
          paint('✓ ' + (it.why || 'The stone fits.'), true);
        } else {
          st.misses++; Sparkle.set(KEY, st); wgSfx('bonk');
          var t = (tried || []).concat([n]);
          paint('🧱 That stone won’t fit. ' + ((it.miss || {})[n] || 'Read it again, then try another answer.'), false, t);
        }
      };
    });
  }
  paint();
  if (anchor) anchor.parentNode.insertBefore(card, anchor); else panel.appendChild(card);
};

/* ── Illuminate the Page: one round a day (week 23, medieval nonfiction) ──
   DATA.wordgame = { type:'illuminate', title, sub, look, todo, win, winWeek,
     items:[ {title, q, opts:[…2 or 3], a, why, miss:{n:'…'}} ] }
   A medieval book page lies on a wooden desk, drawn in pencil. Each right
   answer paints one part: day 1 the big gold capital, day 2 the border,
   day 3 the little castle picture, day 4 the lines of writing. Day d starts
   with days 1…d-1 painted, so the week finishes one page. Practice only;
   never fills a graded box. */
function illumPieces() {
  function R(x, y, w, h, f) { return { t: 'rect', a: 'x="' + x + '" y="' + y + '" width="' + w + '" height="' + h + '"', f: f }; }
  function P(d, f) { return { t: 'path', a: 'd="' + d + '"', f: f }; }
  function G(pts, f) { return { t: 'polygon', a: 'points="' + pts + '"', f: f }; }
  function C(x, y, r, f) { return { t: 'circle', a: 'cx="' + x + '" cy="' + y + '" r="' + r + '"', f: f }; }
  function Ln(x1, x2, y) { return { t: 'ink', x1: x1, x2: x2, y: y }; }
  return [
    /* day 1: the big capital M */
    R(84, 22, 56, 56, '#2F4F8F'), P('M82 20h60v60h-60z M86 24v52h52v-52z', '#C9A227'),
    R(94, 34, 7, 34, '#E3B93A'), G('94,34 101,34 116,55 112,61', '#E3B93A'), G('123,34 130,34 112,61 108,55', '#E3B93A'),
    R(123, 34, 7, 34, '#E3B93A'), { t: 'dots', f: '#B5473A' }, R(82, 84, 60, 3, '#C9A227'),
    /* day 2: the border */
    R(74, 12, 88, 5, '#2F5D9E'), R(162, 12, 84, 5, '#B5473A'), R(241, 17, 5, 85, '#2F5D9E'), R(241, 102, 5, 86, '#B5473A'),
    R(160, 183, 86, 5, '#2F5D9E'), R(74, 183, 86, 5, '#B5473A'), R(74, 100, 5, 83, '#2F5D9E'), R(74, 17, 5, 83, '#B5473A'),
    /* day 3: the little picture */
    R(84, 92, 70, 44, '#8DB6E0'), R(84, 136, 70, 26, '#6E9E4E'), R(96, 112, 46, 26, '#CFC6B2'), R(92, 100, 12, 38, '#BDB29E'),
    R(134, 100, 12, 38, '#BDB29E'), P('M113 138v-12a6 6 0 0 1 12 0v12z', '#6B4423'), P('M98 100V88l10 3-10 3', '#B5473A'), C(120, 101, 6, '#F2C94C'),
    /* day 4: the lines of writing */
    Ln(148, 236, 32), Ln(148, 236, 44), Ln(148, 236, 56), Ln(148, 236, 68),
    Ln(162, 236, 102), Ln(162, 236, 116), Ln(162, 236, 130), Ln(162, 236, 144)
  ];
}
function illumSVG(laid, day, per) {
  var total = per * 4, pcs = illumPieces();
  var s = '<svg viewBox="0 0 320 200" width="100%" style="max-width:340px" role="img" aria-label="' + Math.min(laid, total) + ' of ' + total + ' parts of the page are painted">' +
    '<rect width="320" height="200" rx="12" fill="#8B5E3C"/>' +
    '<path d="M0 40 H320 M0 95 H320 M0 150 H320" stroke="#7A5233" stroke-width="1.5"/>' +
    '<rect x="73" y="11" width="180" height="184" fill="#5E3D24" opacity=".45"/>' +
    '<rect x="70" y="8" width="180" height="184" fill="#F3E7C9" stroke="#C8B48A" stroke-width="1"/>';
  pcs.forEach(function (p, k) {
    if (k >= total) return;
    var on = k < laid, today = k >= (day - 1) * per && k < day * per;
    var ghost = 'fill="none" stroke="' + (today ? '#8A6212' : '#B8A57F') + '" stroke-width="' + (today ? 1.2 : 0.9) + '" stroke-dasharray="3 2"';
    if (p.t === 'ink') {
      if (on) s += '<rect x="' + p.x1 + '" y="' + (p.y - 1.5) + '" width="6" height="4" fill="#B5473A"/>' +
                   '<path d="M' + (p.x1 + 8) + ' ' + p.y + ' H' + p.x2 + '" stroke="#3B2A14" stroke-width="2.4" stroke-dasharray="9 2 14 2 6 2" stroke-linecap="round"/>';
      else s += '<path d="M' + p.x1 + ' ' + p.y + ' H' + p.x2 + '" stroke="' + (today ? '#8A6212' : '#C2B08A') + '" stroke-width=".8" stroke-dasharray="3 2"/>';
    } else if (p.t === 'dots') {
      [[82, 20], [142, 20], [82, 80], [142, 80]].forEach(function (c) {
        s += '<circle cx="' + c[0] + '" cy="' + c[1] + '" r="4" ' + (on ? 'fill="' + p.f + '" stroke="#6B2A22" stroke-width="1"' : ghost) + '/>';
      });
    } else {
      s += '<' + p.t + ' ' + p.a + ' ' + (on ? 'fill="' + p.f + '" stroke="#4A3A24" stroke-width="0.8"' : ghost) + '/>';
    }
  });
  if (laid >= total) s += '<circle cx="226" cy="168" r="11" fill="#9E2B25" stroke="#6B1A16" stroke-width="1.5"/><path d="M220 168l4 4 8-8" stroke="#F3E7C9" stroke-width="2.4" fill="none" stroke-linecap="round"/>';
  return s + '</svg>';
}
WORDGAME.illuminate = function (cfg) {
  var items = cfg.items || []; if (!items.length) return;
  var panel = document.getElementById('tab-words'); if (!panel) return;
  var anchor = panel.querySelector('.tab-next-wrap');
  var day = dayNum(LESSON.day), PER = items.length;
  var KEY = 'oao.g3ela.wg.' + LID;
  var st = Sparkle.get(KEY, null) || { i: 0, misses: 0 };
  if (st.i > PER) st.i = PER;
  var card = cardShell({ id: 'illuminate', kind: 'illuminate', title: cfg.title || 'Illuminate the Page', sub: cfg.sub || '' }, '🖌️');
  var body = card.querySelector('.spk-card-body');
  body.insertAdjacentHTML('beforeend', lookCard(cfg.look, cfg.todo) +
    '<div class="g3-tw-grid"><div class="g3-illum"></div><div class="g3-tw-play" aria-live="polite"></div></div>');
  var mapEl = body.querySelector('.g3-illum'), play = body.querySelector('.g3-tw-play');
  function laid() { return (day - 1) * PER + st.i; }
  function paint(msg, ok, tried) {
    mapEl.innerHTML = illumSVG(laid(), day, PER);
    if (st.i >= PER) {
      play.innerHTML = '<div class="g3-finish">✓ ' + esc(day === 4 ? (cfg.winWeek || cfg.win || '') : (cfg.win || '')) + '</div>' +
        '<button type="button" class="spk-mini-btn g3-again">Play today’s round again</button>';
      play.querySelector('.g3-again').onclick = function () { st = { i: 0, misses: 0 }; Sparkle.set(KEY, st); paint(); };
      return;
    }
    var it = items[st.i];
    var h = stepHead(st.i + 1, PER, it.title || 'Paint a part') + '<p class="g3-tw-q">' + it.q + '</p><div class="g3-opts">';
    it.opts.forEach(function (o, n) {
      h += '<button type="button" class="g3-opt-btn' + (tried && tried.indexOf(n) >= 0 ? ' tried' : '') + '" data-n="' + n + '">' + esc(o) + '</button>';
    });
    h += '</div>';
    if (msg) h += '<div class="g3-fb ' + (ok ? 'ok' : 'no') + '">' + msg + '</div>';
    play.innerHTML = h;
    play.querySelectorAll('.g3-opt-btn').forEach(function (b) {
      b.onclick = function () {
        var n = +b.getAttribute('data-n');
        if (n === it.a) {
          st.i++; Sparkle.set(KEY, st); wgSfx(st.i >= PER ? 'win' : 'chime');
          if (st.i >= PER) { paint(); return; }
          paint('✓ ' + (it.why || 'The paint goes on.'), true);
        } else {
          st.misses++; Sparkle.set(KEY, st); wgSfx('bonk');
          var t = (tried || []).concat([n]);
          paint('🖌️ Not that one. ' + ((it.miss || {})[n] || 'Read it again, then try another answer.'), false, t);
        }
      };
    });
  }
  paint();
  if (anchor) anchor.parentNode.insertBefore(card, anchor); else panel.appendChild(card);
};

/* ── Market Day: one round a day (week 24, medieval nonfiction) ──
   DATA.wordgame = { type:'market', title, sub, look, todo, stepTitle, win, winWeek,
     bins:[ {id, label, ic} ] (2-4 stalls), items:[ {t, bin, why, miss:{binId:'…'}} ] }
   A market square in a medieval town: one striped stall per bin, each with
   its picture sign. Read the word on the basket, tap the stall that sells
   it (the buttons carry the words; nothing is written on the picture).
   Each right answer puts a crate on that stall's counter and brings one
   customer into the square. Day d starts with days 1…d-1's customers, so
   the week fills one square. Practice only; never fills a graded box. */
function marketSVG(have, day, per, bins, crates) {
  var total = per * 4, n = bins.length, W = 320, H = 210;
  var awn = [['#B5473A', '#F3E7C9'], ['#2F5D9E', '#F3E7C9'], ['#2F7A4A', '#F3E7C9'], ['#C7922C', '#F3E7C9']];
  var s = '<svg viewBox="0 0 ' + W + ' ' + H + '" width="100%" style="max-width:360px" role="img" aria-label="' +
    Math.min(have, total) + ' of ' + total + ' customers are at the market">' +
    '<rect width="' + W + '" height="' + H + '" rx="12" fill="#DCEBF5"/>' +
    /* town houses behind the square */
    '<path d="M0 70 L20 52 L40 70 Z M40 70 L64 46 L88 70 Z M88 70 L106 54 L124 70 Z M196 70 L220 48 L244 70 Z M244 70 L266 54 L288 70 Z M288 70 L304 56 L320 70 Z" fill="#9E5A44"/>' +
    '<rect x="0" y="70" width="124" height="34" fill="#E9D8B4"/><rect x="196" y="70" width="124" height="34" fill="#E9D8B4"/>' +
    '<path d="M136 104 V56 L160 26 L184 56 V104 Z" fill="#CFC6B2" stroke="#8A7F68"/><path d="M152 104 v-14 a8 8 0 0 1 16 0 v14 Z" fill="#6B4423"/>' +
    '<path d="M160 26 v-10 M155 20 h10" stroke="#6B4423" stroke-width="2"/>' +
    [14, 54, 98, 206, 250, 292].map(function (x) { return '<rect x="' + x + '" y="80" width="10" height="12" fill="#6E8FB0"/>'; }).join('') +
    /* cobbled square */
    '<rect x="0" y="104" width="' + W + '" height="' + (H - 104) + '" fill="#C9B79A"/>' +
    '<path d="M0 122 H320 M0 146 H320 M0 172 H320 M0 196 H320" stroke="#B3A083" stroke-width="1"/>';
  var sw = Math.min(70, (W - 30) / n - 8), gap = (W - n * sw) / (n + 1);
  bins.forEach(function (b, k) {
    var x = gap + k * (sw + gap), c = awn[k % 4], top = 92, cy = 128;
    /* posts stand on the cobbles */
    s += '<rect x="' + (x + 3) + '" y="' + top + '" width="4" height="' + (cy + 22 - top) + '" fill="#6B4423"/>' +
         '<rect x="' + (x + sw - 7) + '" y="' + top + '" width="4" height="' + (cy + 22 - top) + '" fill="#6B4423"/>';
    /* striped awning */
    for (var i = 0; i < 5; i++) {
      var sx = x - 3 + i * (sw + 6) / 5;
      s += '<path d="M' + sx.toFixed(1) + ' ' + top + ' h' + ((sw + 6) / 5).toFixed(1) + ' v14 q' + (-(sw + 6) / 10).toFixed(1) + ' 7 ' + (-(sw + 6) / 5).toFixed(1) + ' 0 Z" fill="' + c[i % 2] + '" stroke="#5E3D24" stroke-width=".6"/>';
    }
    /* picture sign hangs from the awning */
    s += '<path d="M' + (x + sw / 2 - 6) + ' ' + (top + 14) + ' v6 M' + (x + sw / 2 + 6) + ' ' + (top + 14) + ' v6" stroke="#5E3D24" stroke-width="1"/>' +
         '<rect x="' + (x + sw / 2 - 11) + '" y="' + (top + 19) + '" width="22" height="16" rx="3" fill="#F3E7C9" stroke="#5E3D24"/>' +
         '<text x="' + (x + sw / 2) + '" y="' + (top + 31.5) + '" text-anchor="middle" font-size="11">' + (b.ic || '🧺') + '</text>';
    /* counter */
    s += '<rect x="' + (x - 2) + '" y="' + cy + '" width="' + (sw + 4) + '" height="22" fill="#8A5A2B" stroke="#4E3016" stroke-width="1.5"/>' +
         '<path d="M' + (x - 2) + ' ' + (cy + 8) + ' h' + (sw + 4) + '" stroke="#6B4423"/>';
    /* crates sold today sit on the counter */
    var got = crates[b.id] || 0;
    for (var j = 0; j < Math.min(got, 4); j++) {
      var bx = x + 3 + j * ((sw - 6) / 4);
      s += '<rect x="' + bx.toFixed(1) + '" y="' + (cy - 9) + '" width="' + ((sw - 6) / 4 - 2).toFixed(1) + '" height="9" fill="#C7922C" stroke="#6B4423" stroke-width="1"/>';
    }
  });
  /* customers: two rows standing on the cobbles, feet on the ground line */
  for (var p = 0; p < total; p++) {
    var row = Math.floor(p / 16), col = p % 16;
    var fx = 12 + col * 19 + (row ? 9 : 0), fy = row ? 205 : 180;
    var today = p >= (day - 1) * per && p < day * per;
    var tun = ['#7A3B69', '#2F5D9E', '#2F7A4A', '#B5473A', '#8A6212'][p % 5];
    if (p < have) {
      s += '<path d="M' + (fx - 2.5) + ' ' + fy + ' v-6 M' + (fx + 2.5) + ' ' + fy + ' v-6" stroke="#3B2A14" stroke-width="2"/>' +
           '<path d="M' + (fx - 5) + ' ' + (fy - 5) + ' L' + (fx - 3.5) + ' ' + (fy - 15) + ' H' + (fx + 3.5) + ' L' + (fx + 5) + ' ' + (fy - 5) + ' Z" fill="' + tun + '"/>' +
           '<circle cx="' + fx + '" cy="' + (fy - 18.5) + '" r="3.6" fill="#E8B98F" stroke="#7A5233" stroke-width=".6"/>';
    } else if (today) {
      s += '<path d="M' + (fx - 5) + ' ' + fy + ' L' + (fx - 3.5) + ' ' + (fy - 15) + ' H' + (fx + 3.5) + ' L' + (fx + 5) + ' ' + fy + ' Z" fill="none" stroke="#8A7A5A" stroke-width=".8" stroke-dasharray="2 2"/>' +
           '<circle cx="' + fx + '" cy="' + (fy - 18.5) + '" r="3.6" fill="none" stroke="#8A7A5A" stroke-width=".8" stroke-dasharray="2 2"/>';
    }
  }
  if (have >= total) s += '<rect x="96" y="6" width="128" height="22" rx="11" fill="#2F7A4A"/><text x="160" y="21.5" text-anchor="middle" font-family="Nunito,sans-serif" font-weight="800" font-size="13" fill="#fff">The square is full!</text>';
  return s + '</svg>';
}
WORDGAME.market = function (cfg) {
  var items = cfg.items || [], bins = cfg.bins || []; if (!items.length || bins.length < 2) return;
  var panel = document.getElementById('tab-words'); if (!panel) return;
  var anchor = panel.querySelector('.tab-next-wrap');
  var day = dayNum(LESSON.day), PER = items.length;
  var KEY = 'oao.g3ela.wg.' + LID;
  var st = Sparkle.get(KEY, null) || { i: 0, misses: 0, c: {} };
  if (!st.c) st.c = {};
  if (st.i > PER) st.i = PER;
  var card = cardShell({ id: 'market', kind: 'market', title: cfg.title || 'Market Day', sub: cfg.sub || '' }, '🧺');
  var body = card.querySelector('.spk-card-body');
  body.insertAdjacentHTML('beforeend', lookCard(cfg.look, cfg.todo) +
    '<div class="g3-tw-grid"><div class="g3-market"></div><div class="g3-tw-play" aria-live="polite"></div></div>');
  var mk = body.querySelector('.g3-market'), play = body.querySelector('.g3-tw-play');
  function have() { return (day - 1) * PER + st.i; }
  function paint(msg, ok, tried) {
    mk.innerHTML = marketSVG(have(), day, PER, bins, st.c);
    if (st.i >= PER) {
      play.innerHTML = '<div class="g3-finish">✓ ' + esc(day === 4 ? (cfg.winWeek || cfg.win || '') : (cfg.win || '')) + '</div>' +
        '<button type="button" class="spk-mini-btn g3-again">Play today’s round again</button>';
      play.querySelector('.g3-again').onclick = function () { st = { i: 0, misses: 0, c: {} }; Sparkle.set(KEY, st); paint(); };
      return;
    }
    var it = items[st.i];
    var h = stepHead(st.i + 1, PER, cfg.stepTitle || 'Which stall sells it?') +
      '<div class="g3-mk-basket"><span class="g3-mk-ic" aria-hidden="true">🧺</span><span>' + it.t + '</span></div><div class="g3-stalls">';
    bins.forEach(function (b) {
      h += '<button type="button" class="g3-stall' + (tried && tried.indexOf(b.id) >= 0 ? ' tried' : '') + '" data-b="' + esc(b.id) + '">' +
           '<span class="g3-sack-ic" aria-hidden="true">' + esc(b.ic || '🧺') + '</span><span>' + esc(b.label) + '</span></button>';
    });
    h += '</div>';
    if (msg) h += '<div class="g3-fb ' + (ok ? 'ok' : 'no') + '">' + msg + '</div>';
    play.innerHTML = h;
    play.querySelectorAll('.g3-stall').forEach(function (b) {
      b.onclick = function () {
        var id = b.getAttribute('data-b');
        if (id === it.bin) {
          st.i++; st.c[id] = (st.c[id] || 0) + 1; Sparkle.set(KEY, st); wgSfx(st.i >= PER ? 'win' : 'chime');
          if (st.i >= PER) { paint(); return; }
          paint('✓ ' + esc(it.why || 'Sold! A customer comes to the market.'), true);
          var sv = mk.querySelector('svg'); if (sv) { sv.classList.remove('g3-clink'); void sv.getBoundingClientRect(); sv.classList.add('g3-clink'); }
        } else {
          st.misses++; Sparkle.set(KEY, st); wgSfx('bonk');
          paint(esc((it.miss || {})[id] || 'Not that stall. Read the word again, then try another.'), false, (tried || []).concat([id]));
        }
      };
    });
  }
  paint();
  if (anchor) anchor.parentNode.insertBefore(card, anchor); else panel.appendChild(card);
};

/* ── Through the Wardrobe: one round a day (week 25, LWW Ch. 1-3) ──
   DATA.wordgame = { type:'wardrobe', title, sub, look, todo, stepTitle, win, winWeek,
     bins:[ {id, label, ic} ] (2-4 vowels), items:[ {t, bin, why, miss:{binId:'…'}} ] }
   The inside of an old wardrobe: a row of fur coats hangs on the rail and
   hides what is behind. Read the word on the coat tag (in the play area,
   never on the picture), tap the vowel that makes its lazy schwa. Each right
   answer slides one coat to the side, so more of the snowy wood and the
   lamp-post shows. Snow falls for every right answer all week; the lamp-post
   glows brighter each day and shines when the day's coats are all aside.
   Practice only; never fills a graded box. */
function wardrobeSVG(have, day, per, done) {
  var total = per * 4, W = 320, H = 220, ox = 34, ow = 252, oy = 22, oh = 180;
  var lit = Math.min(1, ((day - 1) * per + done) / total), full = done >= per;
  var s = '<svg viewBox="0 0 ' + W + ' ' + H + '" width="100%" style="max-width:360px" role="img" aria-label="' +
    done + ' of ' + per + ' coats pushed aside today">' +
    '<defs><radialGradient id="g3wdGlow"><stop offset="0" stop-color="#FFE9A8" stop-opacity="1"/><stop offset="1" stop-color="#FFE9A8" stop-opacity="0"/></radialGradient>' +
    '<linearGradient id="g3wdSky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#0E1C42"/><stop offset="1" stop-color="#2E4777"/></linearGradient></defs>' +
    /* the wardrobe: dark wood frame, doors swung open at the sides, standing on its feet */
    '<rect x="14" y="8" width="292" height="200" rx="6" fill="#5A3A22" stroke="#3B2414" stroke-width="2"/>' +
    '<path d="M2 18 L32 22 V202 L2 206 Z" fill="#6E4A2C" stroke="#3B2414" stroke-width="1.5"/><path d="M318 18 L288 22 V202 L318 206 Z" fill="#6E4A2C" stroke="#3B2414" stroke-width="1.5"/>' +
    '<rect x="22" y="208" width="14" height="10" fill="#3B2414"/><rect x="284" y="208" width="14" height="10" fill="#3B2414"/>' +
    /* behind the coats: the snowy wood at night */
    '<rect x="' + ox + '" y="' + oy + '" width="' + ow + '" height="' + oh + '" fill="url(#g3wdSky)"/>' +
    [[50, 150, 26], [84, 140, 34], [236, 142, 32], [268, 152, 24], [118, 156, 20], [204, 158, 20]].map(function (t) {
      return '<path d="M' + t[0] + ' ' + (t[1] - t[2] * 2) + ' L' + (t[0] + t[2] * .6) + ' ' + t[1] + ' H' + (t[0] - t[2] * .6) + ' Z" fill="#1F4A3A"/>' +
             '<path d="M' + t[0] + ' ' + (t[1] - t[2] * 2) + ' l' + (t[2] * .25) + ' ' + (t[2] * .6) + ' h' + (-t[2] * .5) + ' Z" fill="#F4F8FF"/>' +
             '<rect x="' + (t[0] - 2) + '" y="' + t[1] + '" width="4" height="12" fill="#3B2A1A"/>';
    }).join('') +
    '<path d="M' + ox + ' 168 Q160 156 ' + (ox + ow) + ' 168 V' + (oy + oh) + ' H' + ox + ' Z" fill="#EEF3FA"/>' +
    /* the lamp-post stands in the snow; its glow grows all week */
    '<circle cx="160" cy="98" r="' + (16 + 34 * lit + (full ? 10 : 0)) + '" fill="url(#g3wdGlow)" opacity="' + (0.25 + 0.75 * lit).toFixed(2) + '"/>' +
    '<rect x="157.5" y="104" width="5" height="62" fill="#2B2B2B"/><rect x="152" y="162" width="16" height="5" rx="1" fill="#2B2B2B"/>' +
    '<path d="M151 92 h18 l-3 12 h-12 Z" fill="' + (lit > 0 ? '#FFE28A' : '#8A8A70') + '" stroke="#2B2B2B" stroke-width="1.5"/><path d="M149 92 h22 l-11 -7 Z" fill="#2B2B2B"/>';
  /* snow: one flake for every right answer this week */
  for (var k = 0; k < Math.min(have, total); k++) {
    var fx = ox + 8 + ((k * 73) % (ow - 16)), fy = oy + 8 + ((k * 47) % 140);
    s += '<circle cx="' + fx + '" cy="' + fy + '" r="1.8" fill="#FFFFFF" opacity=".9"/>';
  }
  /* the rail, then the coats hanging from it by hooks */
  s += '<rect x="' + ox + '" y="30" width="' + ow + '" height="4" rx="2" fill="#9A7A4A" stroke="#5E4426" stroke-width=".8"/>';
  var furs = ['#7A5638', '#5E4A3E', '#8C6E52', '#4E3B30', '#9A7F66', '#6B5240', '#857060', '#594436'];
  function coat(x, w, c) {
    return '<path d="M' + (x + w / 2) + ' 34 v-5 a3 3 0 1 1 3 -3" fill="none" stroke="#3B3B3B" stroke-width="1.2"/>' +
      '<path d="M' + (x + w / 2) + ' 34 L' + (x + 2) + ' 44 H' + (x + w - 2) + ' Z" fill="none" stroke="#3B3B3B" stroke-width="1.2"/>' +
      '<path d="M' + (x + 3) + ' 42 Q' + (x + w / 2) + ' 36 ' + (x + w - 3) + ' 42 L' + (x + w) + ' 188 Q' + (x + w / 2) + ' 194 ' + x + ' 188 Z" fill="' + c + '" stroke="#2E2018" stroke-width="1"/>' +
      '<path d="M' + (x + w * .3) + ' 60 v120 M' + (x + w * .62) + ' 54 v128" stroke="#000" stroke-opacity=".12" stroke-width="1.5"/>' +
      '<path d="M' + (x + 1) + ' 182 Q' + (x + w / 2) + ' 192 ' + (x + w - 1) + ' 182" stroke="#E8DCCB" stroke-width="3" fill="none" opacity=".7"/>';
  }
  var cw = ow / per;
  for (var i = 0; i < per; i++) {
    if (i < done) {   /* pushed aside: squashed against the side walls */
      var left = i % 2 === 0, slot = Math.floor(i / 2);
      s += coat(left ? ox + slot * 6 : ox + ow - 10 - slot * 6, 10, furs[i % 8]);
    } else {
      s += coat(ox + i * cw - 2, cw + 4, furs[i % 8]);
    }
  }
  if (full) s += '<rect x="86" y="196" width="148" height="20" rx="10" fill="#1F4A3A"/><text x="160" y="210" text-anchor="middle" font-family="Nunito,sans-serif" font-weight="800" font-size="12" fill="#fff">' +
                 (day >= 4 ? 'All the way through!' : 'The lamp-post is shining!') + '</text>';
  return s + '</svg>';
}
WORDGAME.wardrobe = function (cfg) {
  var items = cfg.items || [], bins = cfg.bins || []; if (!items.length || bins.length < 2) return;
  var panel = document.getElementById('tab-words'); if (!panel) return;
  var anchor = panel.querySelector('.tab-next-wrap');
  var day = dayNum(LESSON.day), PER = items.length;
  var KEY = 'oao.g3ela.wg.' + LID;
  var st = Sparkle.get(KEY, null) || { i: 0, misses: 0 };
  if (st.i > PER) st.i = PER;
  var card = cardShell({ id: 'wardrobe', kind: 'wardrobe', title: cfg.title || 'Through the Wardrobe', sub: cfg.sub || '' }, '🧥');
  var body = card.querySelector('.spk-card-body');
  body.insertAdjacentHTML('beforeend', lookCard(cfg.look, cfg.todo) +
    '<div class="g3-tw-grid"><div class="g3-wardrobe"></div><div class="g3-tw-play" aria-live="polite"></div></div>');
  var wd = body.querySelector('.g3-wardrobe'), play = body.querySelector('.g3-tw-play');
  function have() { return (day - 1) * PER + st.i; }
  function paint(msg, ok, tried) {
    wd.innerHTML = wardrobeSVG(have(), day, PER, st.i);
    if (st.i >= PER) {
      play.innerHTML = '<div class="g3-finish">✓ ' + esc(day === 4 ? (cfg.winWeek || cfg.win || '') : (cfg.win || '')) + '</div>' +
        '<button type="button" class="spk-mini-btn g3-again">Play today’s round again</button>';
      play.querySelector('.g3-again').onclick = function () { st = { i: 0, misses: 0 }; Sparkle.set(KEY, st); paint(); };
      return;
    }
    var it = items[st.i];
    var h = stepHead(st.i + 1, PER, cfg.stepTitle || 'Which vowel says uh?') +
      '<div class="g3-mk-basket g3-wd-tag"><span class="g3-mk-ic" aria-hidden="true">🧥</span><span>' + it.t + '</span></div><div class="g3-stalls g3-vowels">';
    bins.forEach(function (b) {
      h += '<button type="button" class="g3-stall' + (tried && tried.indexOf(b.id) >= 0 ? ' tried' : '') + '" data-b="' + esc(b.id) + '">' +
           '<span class="g3-vowel-ic" aria-hidden="true">' + esc(b.ic || b.id) + '</span><span>' + esc(b.label) + '</span></button>';
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
          paint('✓ ' + esc(it.why || 'Right! The coat slides aside.'), true);
          var sv = wd.querySelector('svg'); if (sv) { sv.classList.remove('g3-clink'); void sv.getBoundingClientRect(); sv.classList.add('g3-clink'); }
        } else {
          st.misses++; Sparkle.set(KEY, st); wgSfx('bonk');
          paint(esc((it.miss || {})[id] || 'Not that vowel. Say the word again, then try another.'), false, (tried || []).concat([id]));
        }
      };
    });
  }
  paint();
  if (anchor) anchor.parentNode.insertBefore(card, anchor); else panel.appendChild(card);
};

/* ── The Turkish Delight Box: one round a day (week 26, LWW Ch. 4-6) ──
   DATA.wordgame = { type:'delight', title, sub, look, todo, stepTitle, win, winWeek,
     bins:[ {id, label, ic} ] (2-4), items:[ {t, bin, why, miss:{binId:'…'}} ] }
   The Queen's round box, tied with green silk ribbon, sits open on the snow.
   Read what is on the sweet (in the play area, never on the picture), tap
   the right answer. Each right answer puts one sweet in its place; day d
   starts with days 1…d-1's sweets, so the week fills one box (4 rows of
   8). Practice only; never fills a graded box. */
function delightSVG(have, day, per) {
  var total = per * 4, W = 320, H = 210;
  var s = '<svg viewBox="0 0 ' + W + ' ' + H + '" width="100%" style="max-width:360px" role="img" aria-label="' +
    Math.min(have, total) + ' of ' + total + ' sweets are in the box">' +
    '<rect width="' + W + '" height="' + H + '" rx="12" fill="#E8EEF7"/>' +
    /* snow the box sits on */
    '<path d="M0 168 Q160 150 320 168 V210 H0 Z" fill="#FFFFFF"/>' +
    /* lid leaning behind, with its green silk ribbon */
    '<path d="M44 22 H276 L268 58 H52 Z" fill="#B23A48" stroke="#6E1F2A" stroke-width="2"/>' +
    '<path d="M154 22 h12 l-2 36 h-8 Z" fill="#2F7A4A"/>' +
    '<path d="M160 30 q-26 -22 -30 2 q6 8 30 -2 q26 -22 30 2 q-6 8 -30 -2" fill="#3C9A5D" stroke="#1E5C35" stroke-width="1.2"/>' +
    /* the open box: wooden-red sides, cream paper inside, standing on the snow */
    '<path d="M30 70 H290 L282 170 H38 Z" fill="#8E2A36" stroke="#5A1520" stroke-width="2"/>' +
    '<rect x="44" y="78" width="232" height="84" rx="4" fill="#F6EBDD"/>';
  var cw = 232 / 8, ch = 84 / 4;
  for (var k = 0; k < total; k++) {
    var row = Math.floor(k / 8), col = k % 8;
    var x = 44 + col * cw + 3, y = 78 + row * ch + 3, w2 = cw - 6, h2 = ch - 6;
    var today = k >= (day - 1) * per && k < day * per;
    if (k < have) {
      var c = ['#F4B6C2', '#FBE3B0', '#F7F2EA', '#C9E7C5'][k % 4];
      s += '<rect x="' + x.toFixed(1) + '" y="' + y.toFixed(1) + '" width="' + w2.toFixed(1) + '" height="' + h2.toFixed(1) + '" rx="3" fill="' + c + '" stroke="#C8A9A0" stroke-width=".8"/>' +
           '<circle cx="' + (x + w2 * .3).toFixed(1) + '" cy="' + (y + h2 * .35).toFixed(1) + '" r="1.3" fill="#fff"/><circle cx="' + (x + w2 * .7).toFixed(1) + '" cy="' + (y + h2 * .6).toFixed(1) + '" r="1.1" fill="#fff"/>';
    } else if (today) {
      s += '<rect x="' + x.toFixed(1) + '" y="' + y.toFixed(1) + '" width="' + w2.toFixed(1) + '" height="' + h2.toFixed(1) + '" rx="3" fill="none" stroke="#B9A08F" stroke-width=".9" stroke-dasharray="2 2"/>';
    }
  }
  if (have >= total) s += '<rect x="92" y="180" width="136" height="22" rx="11" fill="#2F7A4A"/><text x="160" y="195.5" text-anchor="middle" font-family="Nunito,sans-serif" font-weight="800" font-size="13" fill="#fff">The box is full!</text>';
  return s + '</svg>';
}
WORDGAME.delight = function (cfg) {
  var items = cfg.items || [], bins = cfg.bins || []; if (!items.length || bins.length < 2) return;
  var panel = document.getElementById('tab-words'); if (!panel) return;
  var anchor = panel.querySelector('.tab-next-wrap');
  var day = dayNum(LESSON.day), PER = items.length;
  var KEY = 'oao.g3ela.wg.' + LID;
  var st = Sparkle.get(KEY, null) || { i: 0, misses: 0 };
  if (st.i > PER) st.i = PER;
  var card = cardShell({ id: 'delight', kind: 'delight', title: cfg.title || 'The Turkish Delight Box', sub: cfg.sub || '' }, '🍬');
  var body = card.querySelector('.spk-card-body');
  body.insertAdjacentHTML('beforeend', lookCard(cfg.look, cfg.todo) +
    '<div class="g3-tw-grid"><div class="g3-delight"></div><div class="g3-tw-play" aria-live="polite"></div></div>');
  var bx = body.querySelector('.g3-delight'), play = body.querySelector('.g3-tw-play');
  function have() { return (day - 1) * PER + st.i; }
  function paint(msg, ok, tried) {
    bx.innerHTML = delightSVG(have(), day, PER);
    if (st.i >= PER) {
      play.innerHTML = '<div class="g3-finish">✓ ' + esc(day === 4 ? (cfg.winWeek || cfg.win || '') : (cfg.win || '')) + '</div>' +
        '<button type="button" class="spk-mini-btn g3-again">Play today’s round again</button>';
      play.querySelector('.g3-again').onclick = function () { st = { i: 0, misses: 0 }; Sparkle.set(KEY, st); paint(); };
      return;
    }
    var it = items[st.i];
    var h = stepHead(st.i + 1, PER, cfg.stepTitle || 'Which one is right?') +
      '<div class="g3-mk-basket"><span class="g3-mk-ic" aria-hidden="true">🍬</span><span>' + it.t + '</span></div><div class="g3-stalls">';
    bins.forEach(function (b) {
      h += '<button type="button" class="g3-stall' + (tried && tried.indexOf(b.id) >= 0 ? ' tried' : '') + '" data-b="' + esc(b.id) + '">' +
           '<span class="g3-sack-ic" aria-hidden="true">' + esc(b.ic || '🍬') + '</span><span>' + esc(b.label) + '</span></button>';
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
          paint('✓ ' + esc(it.why || 'Right! A sweet goes in the box.'), true);
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
var SAY_FOR_CARD = { 'spk-copia-card': 'copia', 'g3card-tower': 'tower', 'g3card-wagon': 'wagon', 'g3card-chase': 'chase', 'g3card-sewer': 'sewer', 'g3card-castle': 'castle', 'g3card-illuminate': 'illuminate', 'g3card-market': 'market', 'g3card-wardrobe': 'wardrobe', 'g3card-delight': 'delight', 'g3card-backward': 'backward' };
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
/* Opti video (Nov 13 2026, week 19 pilot): a teach mod with `video`
   shows Opti's short film (assets/video/<video>.mp4 + .jpg poster, same
   recorded clip as the button) in place of the button. If the film
   can't load, the button comes back, so nothing is lost. */
function teachVideo(m) {
  var src = (window.G3_VIDEO_SRC && window.G3_VIDEO_SRC[m.video]) || ('assets/video/' + m.video + '.mp4');
  var poster = (window.G3_VIDEO_POSTER && window.G3_VIDEO_POSTER[m.video]) || ('assets/video/' + m.video + '.jpg');
  var row = document.createElement('div'); row.className = 'g3-teach g3-teach-video';
  row.innerHTML = '<div class="g3-teach-vk"><span class="g3-teach-face" aria-hidden="true">' + owlSVG('opti', 34) + '</span>' +
    '<span><b>Watch Opti first.</b> Then do the activity.</span></div>';
  var v = document.createElement('video'); v.className = 'g3-teach-v'; v.controls = true; v.preload = 'metadata';
  v.setAttribute('playsinline', ''); v.poster = poster;
  v.addEventListener('play', function () { if (window.speechSynthesis) speechSynthesis.cancel(); if (typeof audioStopAll === 'function') audioStopAll(); });
  v.addEventListener('error', function () {
    var b = teachPlayer(m.label || 'Opti teaches this', teachSrc('teach', m.id), m.script);
    if (row.parentNode) row.parentNode.replaceChild(b, row);
  });
  v.src = src; row.appendChild(v);
  return row;
}
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
    var row = m.script ? (m.video ? teachVideo(m) : teachPlayer(m.label || 'Opti teaches this', teachSrc('teach', m.id), m.script)) : null;
    var folds = [];
    (m.fold || []).forEach(function (s) { body.querySelectorAll(s).forEach(function (e) { if (folds.indexOf(e) < 0) folds.push(e); }); });
    (m.foldText || []).forEach(function (rx) {
      var re = new RegExp(rx, 'i');
      [].forEach.call(body.children, function (e) { if (re.test(e.textContent || '') && folds.indexOf(e) < 0) folds.push(e); });
    });
    var aft = m.after && body.querySelector(m.after);
    if (row) { if (aft) aft.parentNode.insertBefore(row, aft.nextSibling); else body.insertBefore(row, body.firstChild); }
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
