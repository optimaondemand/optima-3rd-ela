/* ══════════════════════════════════════════════════════════════
   OAO SPARKLE · G3 ELA (Opti's Story Map)
   Ported Nov 2026 from optima-4th-ela/sparkle.js by
   tools/g3sparkle/port.py. Lesson content never lives here: each
   lesson carries its own DATA block (see tools/inject.py).
   ══════════════════════════════════════════════════════════════ */
(function () {
"use strict";

/* ── §1 storage layer ──────────────────────────────────────── */
var Sparkle = {
  get: function (k, dflt) {
    try { var v = localStorage.getItem(k); return v ? JSON.parse(v) : (dflt === undefined ? null : dflt); }
    catch (e) { return dflt === undefined ? null : dflt; }
  },
  set: function (k, v) { try { localStorage.setItem(k, JSON.stringify(v)); } catch (e) {} }
};
window.Sparkle = Sparkle;

var REDUCED = false;
try { REDUCED = window.matchMedia('(prefers-reduced-motion: reduce)').matches; } catch (e) {}

/* ── §1 lesson declaration ─────────────────────────────────── */
var LESSON = { grade: 3, subject: 'ela', book: 'wb', week: 18, day: 1 };
try {
  var decl = document.getElementById('oao-lesson');
  if (decl) LESSON = JSON.parse(decl.textContent);
} catch (e) {}
var LID = LESSON.week + '.' + LESSON.day;

/* ── §1.2 course map ───────────────────────────────────────── */
var COURSE = [
  { id:'stanley', title:'Flat Stanley',                 weeks:[1,5],   place:'the Lambchops\u2019 house' },
  { id:'nonfic',  title:'Letters and Maps',             weeks:[6,7],   place:null, kind:'nonfiction' },
  { id:'desp',    title:'The Tale of Despereaux',       weeks:[8,17],  place:'the castle' },
  { id:'wb',      title:'The Whipping Boy',             weeks:[18,22], place:'the king\u2019s castle' },
  { id:'med',     title:'Castles and Knights',          weeks:[23,24], place:null, kind:'nonfiction' },
  { id:'lww',     title:'The Lion, the Witch and the Wardrobe', weeks:[25,30], place:'Narnia' },
  { id:'ext',     title:'Journey\u2019s End',          weeks:[31,32], place:null, kind:'synthesis' }
];
/* The shelf holds the five novels only. The student's own writing is
   not a book on the shelf — it lives on the map, at Writer's Workshop
   and again at Journey's End. */
var SHELF = [
  { id:'stanley', short:'Flat Stanley' },
  { id:'desp',    short:'Despereaux' },
  { id:'wb',      short:'The Whipping Boy', gold:true },
  { id:'lww',     short:'Narnia' }
];

/* ══════════════════════════════════════════════════════════════
   ART — the ONLY place image files are named.
   Drop Bethany's files in and every use of them updates at once.
   Anything left as '' falls back to the drawn version, so the
   lesson is never broken by a missing or slow image.
   `base` is prepended to any path that isn't already absolute.
   ══════════════════════════════════════════════════════════════ */
var ART = {
  /* ── PRODUCTION ─────────────────────────────────────────────
     When the assets are pushed to the repo, delete the embedded
     data URIs below and use these instead:

       base: 'https://optimaondemand.github.io/optima-4th-ela/assets/',
       covers: { frisby:'covers/frisby.jpg', anne:'covers/anne.jpg',
                 nts:'covers/nts.jpg', ft:'covers/ft.jpg',
                 pc:'covers/pc.jpg', mywriting:'covers/mywriting.svg' },
       companions: { optima:'companions/owl.png' }

     The demo embeds them so the file works by double-click with
     no server and no deploy.
     ──────────────────────────────────────────────────────────── */
  /* Every image is a PATH, never an embedded data: URI.

     This is deliberate and it is about the child's connection, not
     tidiness. Baked into the page, this art is ~2 MB that cannot be
     cached between lessons, so a student re-downloads the identical
     map and ornaments on all 129 of them — roughly 250 MB over a year.
     Referenced, the browser fetches each file once in week 7 and every
     later lesson is instant.

     The cost of the choice: a lesson only works served from the repo
     or Pages, not opened as a loose file off a desktop. That is the
     accepted trade. Do not inline something to make one file portable. */
  base: 'assets/',

  /* §2.2 the year map. Bethany's painted board — the spaces are part
     of the picture, so their coordinates were measured off the file
     (BOARD_SPACES below) and the progress layer is drawn on top. */
  board: { src: 'art/road/year-board.jpg' },

  /* the four novels on the G3 shelf. Covers are stored in the repo
     (from Open Library, sized for the shelf); a cover that fails to load
     falls back to a drawn spine, so the shelf never shows a hole. */
  covers: {
    stanley: 'art/covers/stanley.jpg',
    desp:    'art/covers/desp.jpg',
    wb:      'art/covers/wb.jpg',
    lww:     'art/covers/lww.jpg'
  },

  /* per-world art. `terrain` paints that stretch of the map and is
     feathered into its neighbours so the map stays one picture;
     `landmark` is the object that stands beside the road. Either
     can be left '' and the drawn version is used instead. */
  worlds: {},

  /* The chapter illustration — one per lesson, printed under the quote
     the way a chapter heading sits on the page of a good children's
     book. No caption: the chapter quote above it is the only words.

     Not listed here, because it is not one file: the path is built
     from the lesson's own book and chapters by plateSrc() below. */
  plate: { src: '' },

  /* Two sizes of one mark. `scholar` is the full wreathed seal for the
     published page; `mark` is the wax disc alone, because at 46px on
     the year map the laurel closes into a smudge and the disc inside
     it is all that survives. */
  seals: {
    scholar: '',
    mark:    ''
  },

  /* Writer's Workshop headpieces, one per genre arc. */
  banners: {},

  /* pen-and-ink spot ornaments. Used sparingly and always decoratively —
     none of them carries meaning, so all are aria-hidden / CSS-only.
     The set is closed; eight is enough that the rotation does not show. */
  ornaments: {},

  companions: { opti: 'companions/owl.png' }
};

/* The chapter plate's filename, built from the lesson declaration:
     book 'anne' + chapters 'Ch. 3 & 4'  ->  plates/anne-ch3-4.png
     book 'anne' + chapters 'Ch. 1'      ->  plates/anne-ch1.png
   .png always. If the file is not there the plate simply does not
   render, and it appears the moment the file lands — no rebuild. */
function plateSrc() {
  if (ART.plate && ART.plate.src) return artURL(ART.plate.src);   /* override */
  /* a lesson with no chapter numbers (the bridge week) names its own
     picture in DATA.plate = { src, alt, credit } — a historical photo
     rather than a painted plate, so it carries its own credit line */
  if (DATA.plate && DATA.plate.src) return artURL(DATA.plate.src);
  var nums = String(LESSON.chapters || '').match(/\d+/g);
  if (!nums || !nums.length || !LESSON.book) return '';
  return artURL('plates/' + LESSON.book + '-ch' + nums.join('-') + '.png');
}
window.OAO_ART = ART;   /* exposed so art can be swapped without touching code */
/* after changing OAO_ART, call this to repaint everything that uses it */
window.OAO_refreshArt = function () {
  try { drawShelf(); } catch (e) {}
  try { if (document.getElementById('spkMap')) drawMap(); } catch (e) {}
};
/* the companions we have art for, in picker order */
function companionKeys() {
  return Object.keys(ART.companions).filter(function (k) { return !!artURL(ART.companions[k]); });
}
function defaultCompanion() { return companionKeys()[0] || 'tawny'; }
/* a profile saved by an earlier build may name a companion we no longer
   have art for — resolve it to one we do */
function resolveCompanion(key) {
  if (key && artURL(ART.companions[key])) return key;
  return companionKeys().length ? defaultCompanion() : (key || 'tawny');
}
function artURL(pathish) {
  if (!pathish) return '';
  return /^(https?:|data:|\/)/.test(pathish) ? pathish : (ART.base + pathish);
}

/* ── owl copy (§2.4) ───────────────────────────────────────── */
var OWL = {
  correct: ['Well spotted.', "That's the one.", 'Just so.', 'Good eye.'],
  complete: 'Well read',
  stuck: "Let's look at it together."
};
var owlCorrectIdx = 0;
window.__spkOwlDrawn = function (k, n) { return owlDrawn(k, n); };
/* inside an <svg> an <img> is invalid — use <image> there */
function owlMarkSVG(key, size) {
  key = resolveCompanion(key);
  var img = artURL(ART.companions[key]);
  /* stand the owl on the road: anchor the art to the bottom of its box */
  if (img) return '<image href="' + img + '" x="0" y="0" width="' + size + '" height="' + size +
                  '" preserveAspectRatio="xMidYMax meet"/>';
  return owlDrawn(key, size);
}

/* ── owl plumages (§2.5) ───────────────────────────────────── */
var PLUMAGE = {
  opti:        { label:'Opti', body:'#B87333', face:'#EBD3A8', tuft:'#8A5220' },
  barn:        { label:'Barn',        body:'#D9B98C', face:'#FBF4E7', tuft:'#C29A68' },
  snowy:       { label:'Snowy',       body:'#EDF2FA', face:'#FFFFFF', tuft:'#CBD8EA' },
  greathorned: { label:'Great Horned',body:'#8A6A4B', face:'#E4CBA8', tuft:'#5E452E' },
  tawny:       { label:'Tawny',       body:'#B87333', face:'#EBD3A8', tuft:'#8A5220' }
};
function owlSVG(key, size) {
  key = resolveCompanion(key);
  size = size || 44;
  var img = artURL(ART.companions[key]);
  if (img) {
    /* portrait artwork: give it a height and let the width follow, or
       a square box squashes the bird */
    return '<img class="spk-companion-img" src="' + img + '" height="' + size +
           '" alt="" onerror="this.outerHTML=window.__spkOwlDrawn(\'' + key + '\',' + size + ')" />';
  }
  return owlDrawn(key, size);
}
function owlDrawn(key, size) {
  var p = PLUMAGE[key] || PLUMAGE.tawny; size = size || 44;
  return '<svg viewBox="0 0 64 64" width="' + size + '" height="' + size + '" aria-hidden="true">' +
    '<circle cx="32" cy="32" r="31" fill="' + p.body + '"/>' +
    '<path d="M12 18 L20 6 L26 17 Z" fill="' + p.tuft + '"/>' +
    '<path d="M52 18 L44 6 L38 17 Z" fill="' + p.tuft + '"/>' +
    '<ellipse cx="23" cy="30" rx="10" ry="11" fill="' + p.face + '"/>' +
    '<ellipse cx="41" cy="30" rx="10" ry="11" fill="' + p.face + '"/>' +
    '<circle cx="23" cy="30" r="4.6" fill="#0E1C42"/>' +
    '<circle cx="41" cy="30" r="4.6" fill="#0E1C42"/>' +
    '<circle cx="24.6" cy="28.4" r="1.5" fill="#fff"/>' +
    '<circle cx="42.6" cy="28.4" r="1.5" fill="#fff"/>' +
    '<path d="M32 33 L28 39 L36 39 Z" fill="#C7922C"/>' +
    '<path d="M22 46 Q32 54 42 46" stroke="' + p.tuft + '" stroke-width="2.5" fill="none" stroke-linecap="round"/>' +
    '</svg>';
}

/* ══════════════════════════════════════════════════════════════
   LESSON CONTENT (§3) — the authored data this lesson's
   sparkle features read. In the full build this lives in the
   HTML as data-* attributes; kept here so the demo file is
   readable in one place.
   ══════════════════════════════════════════════════════════════ */
/* ── §1.3 the lesson's own content ──────────────────────────────
   DATA is PER LESSON and lives in the lesson file, not here.

   This was the rollout's worst bug: DATA used to be ~98 lines of
   lesson 7.1 written into this layer. Every sparkled lesson in the
   year would have shown Mrs. Rachel's sentence, chapter one's hint
   ladders and a connector about closing Mrs. Frisby — on lesson 12.3,
   on lesson 20.1, everywhere. The layer rendered beautifully and said
   the wrong thing, which is the worst failure mode available.

   So it is a second JSON block in the lesson's own <head>, written by
   tools/inject.py:

     <script type="application/json" id="oao-data"> { ... } </script>

   Everything in it is optional. A missing key costs exactly its own
   feature — no DOL choice, no hint ladder, no copia card — and never
   somebody else's lesson content. An EMPTY DATA is a valid lesson.

   There is no `poem` key. The By Heart card belongs to
   assets/js/oao-sparkle.js. */
var DATA = {};
try {
  var dataEl = document.getElementById('oao-data');
  if (dataEl) DATA = JSON.parse(dataEl.textContent) || {};
} catch (e) {
  if (window.console && console.warn) console.warn('[sparkle] DATA did not parse:', e);
}
window.OAO_DATA = DATA;

/* ══════════════════════════════════════════════════════════════
   THE WRITING PROJECT
   Writing runs the whole year in six genre arcs (see the scope &
   sequence). A lesson used to name only the day's step — "Week 7 ·
   VOICE" — so a student never learned what they were building. Each
   Workshop card now says the genre, what it means, and when it is
   published.
   ══════════════════════════════════════════════════════════════ */
var WRITING_ARCS = [
  { weeks:[1,5],   name:'a personal narrative',  gloss:'a true story from your own life' },
  { weeks:[6,7],   name:'a friendly letter',     gloss:'a letter to a real person, with a greeting and a closing' },
  { weeks:[8,17],  name:'a story response',      gloss:'writing about what happens in a book and why' },
  { weeks:[18,22], name:'an opinion paragraph',  gloss:'writing where you say what you think and give reasons' },
  { weeks:[23,24], name:'an informational piece',gloss:'writing that teaches facts about a topic' },
  { weeks:[25,30], name:'a fantasy story',       gloss:'a made-up story with magic in it' },
  { weeks:[31,32], name:'your year-end project', gloss:'looking back at the books you read this year' }
];
function titleCase(str) {
  return str.replace(/\b[a-z]/g, function (c) { return c.toUpperCase(); });
}
function writingArc(week) {
  for (var i = 0; i < WRITING_ARCS.length; i++) {
    var a = WRITING_ARCS[i];
    if (week >= a.weeks[0] && week <= a.weeks[1]) return a;
  }
  return null;
}

/* Every Workshop entry is mirrored into one shared place so the next
   day's lesson can read it. The lesson's own autoSave is keyed to
   _lessonKey (which comes from document.title), so Monday's writing
   is saved but invisible on Tuesday — which defeats a project that
   is supposed to build day by day. */
function writingSaveEntry(text) {
  var all = Sparkle.get('oao.g3ela.writing', {});
  if (!text || !text.trim()) { delete all[LID]; }
  else { all[LID] = { text: text, at: new Date().toISOString(), focus: DATA.writingFocus || '' }; }
  Sparkle.set('oao.g3ela.writing', all);
}
function writingEarlierEntries() {
  var all = Sparkle.get('oao.g3ela.writing', {});
  var arc = writingArc(LESSON.week); if (!arc) return [];
  return Object.keys(all).map(function (k) {
    var p = k.split('.');
    return { id: k, week: +p[0], day: +p[1], entry: all[k] };
  }).filter(function (e) {
    return e.week >= arc.weeks[0] && e.week <= arc.weeks[1] &&
           (e.week < LESSON.week || (e.week === LESSON.week && e.day < LESSON.day));
  }).sort(function (a, b) { return a.week - b.week || a.day - b.day; });
}

function buildWritingProject() {
  var box = document.getElementById('journal-writing'); if (!box) return;
  var card = box.closest('.activity'); if (!card) return;
  var body = card.querySelector('.activity-body'); if (!body) return;
  var arc = writingArc(LESSON.week); if (!arc) return;
  var step = LESSON.week - arc.weeks[0] + 1;
  var of = arc.weeks[1] - arc.weeks[0] + 1;

  /* the headpiece for this genre, above everything else in the card.
     Six arcs, six pictures — the Workshop used to look identical in
     every week of the year. Decorative only; the goal card below
     still says the genre in words. */
  var ARC_ART = ['narrative', 'fiction', 'opinion', 'research', 'analysis', 'yearend'];
  var arcKey = ARC_ART[WRITING_ARCS.indexOf(arc)];
  var headSrc = artURL((ART.banners || {})[arcKey]);
  if (headSrc) {
    var head = document.createElement('div');
    head.className = 'spk-arc-head';
    head.setAttribute('aria-hidden', 'true');
    var hi = document.createElement('img');
    hi.src = headSrc; hi.alt = ''; hi.loading = 'lazy';
    hi.onerror = function () { head.remove(); };
    head.appendChild(hi);
    body.insertBefore(head, body.firstChild);
  }

  /* the goal banner — first thing in the card */
  var goal = document.createElement('div');
  goal.className = 'spk-goal';
  goal.innerHTML =
    '<div class="spk-goal-label">What you are writing</div>' +
    '<div class="spk-goal-title">' + arc.name.charAt(0).toUpperCase() + arc.name.slice(1) + '</div>' +
    '<div class="spk-goal-gloss">' + arc.gloss + '</div>' +
    '<div class="spk-goal-meta">Week ' + step + ' of ' + of + ' \u00b7 you finish it and publish it in Week ' +
      arc.weeks[1] + '</div>' +
    '<div class="spk-keep">' +
      '<div class="spk-keep-title">Keep your writing in one place</div>' +
      '<p>Make one document just for this project and call it <b>My ' +
      titleCase(arc.name.replace(/^an? /, '').replace(/^your /, '')) +
      '</b> \u2014 a Google Doc or a Word file. ' +
      'Every day: write in the box below, then <b>copy it into your own document</b>. ' +
      'That way your whole ' + (/report/i.test(arc.name) ? 'report' : /essay|analysis/i.test(arc.name) ? 'essay' : /project/i.test(arc.name) ? 'project' : 'story') + ' is in one place and nothing gets lost.</p>' +
    '</div>';
  var firstReal = document.querySelector('.spk-arc-head');
  if (firstReal && firstReal.parentNode === body) body.insertBefore(goal, firstReal.nextSibling);
  else body.insertBefore(goal, body.firstChild);

  /* what they wrote on the earlier days of this project */
  var earlier = writingEarlierEntries();
  if (earlier.length) {
    var box2 = document.createElement('details');
    box2.className = 'spk-earlier';
    var items = earlier.map(function (e) {
      var d = document.createElement('div');
      d.className = 'spk-earlier-item';
      var h = document.createElement('div');
      h.className = 'spk-earlier-when';
      h.textContent = 'Lesson ' + e.id + (e.entry.focus ? ' \u00b7 ' + e.entry.focus : '');
      var t = document.createElement('p');
      t.className = 'spk-earlier-text'; t.textContent = e.entry.text;   /* student text: never innerHTML */
      d.appendChild(h); d.appendChild(t);
      return d;
    });
    var sum = document.createElement('summary');
    sum.textContent = 'What you wrote on this project before (' + earlier.length + ')';
    var caveat = document.createElement('p');
    caveat.className = 'spk-earlier-caveat';
    caveat.textContent = 'This only remembers work done on this computer. Your own document is the ' +
      'copy that always has everything.';
    box2.appendChild(sum);
    box2.appendChild(caveat);
    items.forEach(function (d) { box2.appendChild(d); });

    var last = earlier[earlier.length - 1];
    var carry = document.createElement('button');
    carry.type = 'button'; carry.className = 'spk-mini-btn';
    carry.textContent = 'Put my last writing in the box below';
    carry.onclick = function () {
      if (box.value.trim()) { carry.textContent = 'Your box already has writing in it'; return; }
      box.value = last.entry.text;
      box.dispatchEvent(new Event('input', { bubbles: true }));
      carry.textContent = 'Copied \u2014 keep building on it';
      carry.disabled = true; carry.style.opacity = '.6';
    };
    box2.appendChild(carry);
    body.insertBefore(box2, goal.nextSibling);
  }

  /* a one-tap copy, so "put it in your own document" is easy to obey */
  var tools = document.createElement('div');
  tools.className = 'spk-write-tools';
  var copy = document.createElement('button');
  copy.type = 'button'; copy.className = 'spk-btn spk-copy-writing';
  copy.textContent = 'Copy today\u2019s writing';
  var note = document.createElement('span');
  note.className = 'spk-write-note';
  note.textContent = 'Then paste it into your own document.';
  copy.onclick = function () {
    var text = box.value;
    if (!text.trim()) { note.textContent = 'Write something first, then copy it.'; return; }
    function done() {
      copy.textContent = 'Copied \u2014 now paste it in your document';
      note.textContent = 'Your document is the one that always has your whole story.';
      setTimeout(function () { copy.textContent = 'Copy today\u2019s writing'; }, 4000);
    }
    try {
      navigator.clipboard.writeText(text).then(done, function () { box.select(); document.execCommand('copy'); done(); });
    } catch (e) { box.select(); document.execCommand('copy'); done(); }
  };
  tools.appendChild(copy); tools.appendChild(note);
  box.parentNode.insertBefore(tools, box.nextSibling);

  /* mirror every keystroke into the shared store */
  box.addEventListener('input', function () { writingSaveEntry(box.value); });
  if (box.value.trim()) writingSaveEntry(box.value);
}

/* ══════════════════════════════════════════════════════════════
   §2.1  PROFILE + GREETING
   ══════════════════════════════════════════════════════════════ */
function profile() { return Sparkle.get('oao.g3ela.profile', null); }
function storageWorks() {
  try { var k = 'oao.__probe'; localStorage.setItem(k, '1'); localStorage.removeItem(k); return true; }
  catch (e) { return false; }
}

/* ══════════════════════════════════════════════════════════════
   NAME CHECK
   Two lists, because one cannot do both jobs:
     STRONG — matched anywhere in the name. These strings do not
              occur inside real first names.
     WHOLE  — matched only as a whole word. "ass" and "hell" sit
              inside Cassandra and Hellen, so a substring match
              would turn away real children by name.
   Leetspeak is folded first (4>a, 3>e, 1>i, 0>o, $>s) and repeated
   letters collapsed, so "sh1t" and "fuuuuck" are caught too.
   A starter list, not a guarantee — worth swapping for a maintained
   one before the course ships.
   ══════════════════════════════════════════════════════════════ */
var NAME_STRONG = [
  'fuck','shit','bitch','cunt','whore','slut','wank','bollock','bastard',
  'penis','vagina','boob','anus','turd','scrotum','testicle',
  'nigg','fagg','retard','kike','chink','tranny',
  'porn','rape','nazi','hitler'
];
var NAME_WHOLE = [
  'ass','arse','hell','damn','crap','piss','poop','pee','fart','butt','bum',
  'dick','cock','prick','knob','willy','tit','sex','kill',
  'dumb','stupid','idiot','loser','ugly','fatso','poopy','poopyhead'
];
function nameFold(v) {
  return String(v).toLowerCase()
    .replace(/[4@]/g, 'a').replace(/3/g, 'e').replace(/[1!|]/g, 'i')
    .replace(/0/g, 'o').replace(/[$5]/g, 's').replace(/7/g, 't')
    .replace(/[^a-z ]+/g, ' ')
    .replace(/(.)\1+/g, '$1')
    .replace(/\s+/g, ' ').trim();
}
var _STRONG_F = null, _WHOLE_F = null;
function nameProblem(raw) {
  if (!_STRONG_F) {
    _STRONG_F = NAME_STRONG.map(nameFold);
    _WHOLE_F  = NAME_WHOLE.map(nameFold);
  }
  var name = String(raw || '').trim();
  if (!name) return 'Type your first name.';
  if (name.replace(/[^A-Za-z]/g, '').length < 2) return 'That is a bit short \u2014 what do people call you?';
  var folded = nameFold(name);
  if (!folded) return 'Use letters for your name.';
  var i;
  for (i = 0; i < NAME_STRONG.length; i++) {
    if (_STRONG_F[i] && folded.indexOf(_STRONG_F[i]) !== -1) return 'block';
  }
  /* "F U C K" — letters spaced out. Check the de-spaced form too, but
     only against entries of 4+ folded characters: shorter ones would
     start matching across the join in ordinary two-part names. */
  var squashed = folded.replace(/ /g, '');
  for (i = 0; i < _STRONG_F.length; i++) {
    if (_STRONG_F[i].length >= 4 && squashed.indexOf(_STRONG_F[i]) !== -1) return 'block';
  }
  var words = folded.split(' ');
  for (i = 0; i < words.length; i++) {
    if (_WHOLE_F.indexOf(words[i]) !== -1) return 'block';
  }
  return null;
}
/* the map title is built by string concatenation into innerHTML */
function esc(t) {
  return String(t).replace(/&/g, '&amp;').replace(/</g, '&lt;')
                  .replace(/>/g, '&gt;').replace(/"/g, '&quot;');
}

/* returns [before-the-name, after-the-name] so the name itself can
   be set apart. Never innerHTML — the name is always textContent. */
function greetingParts(p) {
  var prog = Sparkle.get('oao.g3ela.progress', {});
  var me = prog[LID];
  if (LESSON.day === 'fluency') return ['Time to read aloud, ', '.'];
  if (me && me.tabs && me.tabs.length > 1) return ['Picking up where you left off, ', '.'];
  if (LESSON.day === 1) return ['Welcome back, ', '. A new week \u2014 and a new chapter.'];
  var prev = LESSON.week + '.' + (LESSON.day - 1);
  if (prog[prev] && prog[prev].done) return ['Welcome back, ', '. Last time you finished Lesson ' + prev + '.'];
  return ['Welcome back, ', '.'];
}

function renderGreeting() {
  var p = profile(); if (!p) return;
  var panel = document.getElementById('tab-warmup'); if (!panel) return;
  var line = document.getElementById('spkGreet');
  if (!line) {
    line = document.createElement('section');
    line.className = 'spk-open'; line.id = 'spkGreet';
    line.innerHTML =
      '<div class="spk-open-head">' +
        '<span class="spk-open-owl" id="spkGreetOwl"></span>' +
        '<h2 class="spk-open-greet"><span id="spkGreetA"></span>' +
        '<b class="spk-greet-name" id="spkGreetName"></b>' +
        '<span id="spkGreetB"></span>' +
        '<button type="button" class="spk-greet-edit" title="Fix the spelling of my name">\u270E</button></h2>' +
      '</div>' +
      '<p class="spk-open-say" id="spkOpenSay"></p>';
    line.querySelector('.spk-greet-edit').onclick = function () { showProfileCard(true); };
    panel.insertBefore(line, panel.firstChild);
  }
  var parts = greetingParts(p);
  document.getElementById('spkGreetA').textContent = parts[0];
  document.getElementById('spkGreetName').textContent = p.name;   /* never innerHTML */
  document.getElementById('spkGreetB').textContent = parts[1];
  document.getElementById('spkGreetOwl').innerHTML = owlSVG(p.owl, 52);
  var say = document.getElementById('spkOpenSay');
  if (DATA.connector) say.textContent = DATA.connector;
  else say.remove();
  try { buildMedia(); } catch (e) {}
  try { optiFaces(); } catch (e) {}
  dividerAfterOpening();
}

/* The header logo is the Optima mark and is never replaced. The
   student's chosen companion appears on the map and on the profile
   card only. */

function showProfileCard(isEdit) {
  if (document.getElementById('spkProfileCard')) return;
  var anchor = document.getElementById('introSection');
  if (!anchor) return;
  var p = profile() || { name: '', owl: defaultCompanion() };
  var card = document.createElement('div');
  card.className = 'spk-profile-card'; card.id = 'spkProfileCard';
  var keys = companionKeys();
  var pickable = keys.length > 1 ? keys : [];
  var owls = pickable.map(function (k) {
    return '<button type="button" class="spk-owl-pick' + (p.owl === k ? ' sel' : '') +
      '" data-owl="' + k + '">' + owlSVG(k, 44) +
      '<span>' + ((PLUMAGE[k] && PLUMAGE[k].label) || k) + '</span></button>';
  }).join('');
  card.innerHTML =
    '<h3>' + (isEdit ? 'Fix your name' : 'Before we begin: what should ' + 'Opti' + ' call you?') + '</h3>' +
    '<p class="spk-sub">Just your first name. It stays on this computer — nobody else sees it.</p>' +
    '<div class="spk-name-row">' +
      '<input class="spk-name-input" id="spkNameInput" maxlength="24" autocomplete="off" placeholder="Your name" />' +
      '<button class="spk-btn" id="spkBegin" type="button">' + (isEdit ? 'Save' : 'Begin') + '</button>' +
    '</div>' +
    (pickable.length
      ? '<div class="spk-owl-label">Which owl will read with you?</div>' +
        '<div class="spk-owl-row" id="spkOwlRow">' + owls + '</div>'
      : '<div class="spk-companion-solo">' + owlSVG(defaultCompanion(), 62) +
        '<span>This is Opti, the owl who reads along with you. You\u2019ll see him on the Reading Road.</span></div>');
  anchor.parentNode.insertBefore(card, anchor);

  var input = card.querySelector('#spkNameInput');
  input.value = p.name || '';
  var chosen = p.owl || defaultCompanion();
  card.querySelectorAll('.spk-owl-pick').forEach(function (b) {
    b.onclick = function () {
      chosen = b.getAttribute('data-owl');
      card.querySelectorAll('.spk-owl-pick').forEach(function (x) { x.classList.remove('sel'); });
      b.classList.add('sel');
    };
  });
  var begin = card.querySelector('#spkBegin');
  function clean(v) { return (v || '').replace(/[^A-Za-z \-']/g, '').trim().slice(0, 24); }
  function sync() { begin.disabled = clean(input.value).length === 0; }
  input.addEventListener('input', sync); sync();
  input.addEventListener('keydown', function (e) { if (e.key === 'Enter' && !begin.disabled) begin.click(); });
  var warn = document.createElement('div');
  warn.className = 'spk-name-warn'; warn.style.display = 'none';
  card.querySelector('.spk-name-row').insertAdjacentElement('afterend', warn);
  input.addEventListener('input', function () { warn.style.display = 'none'; });

  begin.onclick = function () {
    var name = clean(input.value);
    /* test what they typed AND what we keep — clean() strips digits,
       which is the whole trick behind "sh1t" and "n1gger" */
    var problem = nameProblem(input.value) || nameProblem(name);
    if (problem) {
      warn.style.display = 'block';
      warn.textContent = problem === 'block'
        ? 'Let\u2019s use your real first name \u2014 this is the name that goes on your work.'
        : problem;
      input.focus();
      return;
    }
    warn.style.display = 'none';
    var old = profile();
    Sparkle.set('oao.g3ela.profile', { name: name, owl: chosen, created: (old && old.created) || new Date().toISOString() });
    card.parentNode.removeChild(card);
    renderGreeting();
    renderIllumAuthor();
    owlSay('Well met, ' + name + '.');
  };
  input.focus();
}

/* ══════════════════════════════════════════════════════════════
   §2.4  OWL SPEECH SLIP
   ══════════════════════════════════════════════════════════════ */
var owlTimer = null;
function owlSay(text) {
  var brand = document.querySelector('.header'); if (!brand) return;
  var slip = document.getElementById('spkOwlSlip');
  if (!slip) {
    slip = document.createElement('div');
    slip.className = 'spk-owl-slip'; slip.id = 'spkOwlSlip';
    brand.appendChild(slip);
  }
  slip.textContent = text;
  slip.classList.add('show');
  clearTimeout(owlTimer);
  owlTimer = setTimeout(function () { slip.classList.remove('show'); }, 2500);
}
function owlCorrect() {
  owlSay(OWL.correct[owlCorrectIdx % OWL.correct.length]); owlCorrectIdx++;
}

/* ══════════════════════════════════════════════════════════════
   §2.2  PROGRESS: dot track + year map   §2.3 bookshelf
   ══════════════════════════════════════════════════════════════ */
function lessonHref(week, day) {
  if (day === 'fluency') return 'lesson-' + week + '-fluency.html';
  /* Demo build knows only Week 7's filenames; the real script
     derives these from the repo's naming convention. */
  var MAP = { '7.1':'lesson-7-1-anne-ch1.html', '7.2':'lesson-7-2-anne-ch2.html',
              '7.3':'lesson-7-3-anne-ch3-4.html', '7.4':'lesson-7-4-anne-ch5.html' };
  return MAP[week + '.' + day] || null;
}

function markTabs(tabIds) {
  var prog = Sparkle.get('oao.g3ela.progress', {});
  var me = prog[LID] || { tabs: [], done: false, doneAt: null };
  tabIds.forEach(function (t) { if (me.tabs.indexOf(t) === -1) me.tabs.push(t); });
  prog[LID] = me; Sparkle.set('oao.g3ela.progress', prog);
}
function markDone() {
  var prog = Sparkle.get('oao.g3ela.progress', {});
  var me = prog[LID] || { tabs: [], done: false, doneAt: null };
  if (me.done) return false;
  me.done = true; me.doneAt = new Date().toISOString();
  prog[LID] = me; Sparkle.set('oao.g3ela.progress', prog);

  var book = COURSE.filter(function (b) { return b.id === LESSON.book; })[0];
  if (book && LESSON.week === book.weeks[1] && LESSON.day === 4) {
    var all = true;
    for (var w = book.weeks[0]; w <= book.weeks[1]; w++) {
      var k = w + '.4'; if (!(prog[k] && prog[k].done)) all = false;
    }
    if (all) {
      var books = Sparkle.get('oao.g3ela.books', {});
      books[book.id] = { done: true, doneAt: new Date().toISOString() };
      Sparkle.set('oao.g3ela.books', books);
      document.dispatchEvent(new CustomEvent('oao:bookfinished', { detail: { book: book } }));
      return true;
    }
  }
  return false;
}

function buildTrack() {
  var wrap = document.querySelector('.progress-wrap'); if (!wrap) return;
  var box = document.createElement('div');
  box.className = 'spk-track'; box.id = 'spkTrack';
  box.innerHTML =
    '<div class="spk-track-row"><span class="spk-track-label">This week</span><span id="spkDots"></span>' +
    '<button type="button" class="spk-track-jump" id="spkJump">See the Reading Road \u2192</button></div>';
  wrap.parentNode.insertBefore(box, wrap.nextSibling);
  document.getElementById('spkJump').onclick = function () {
    if (window.switchTab) window.switchTab('reading');
    setTimeout(function () {
      var c = document.querySelector('.spk-journey');
      if (c) c.scrollIntoView({ behavior: REDUCED ? 'auto' : 'smooth', block: 'center' });
    }, 320);
  };
  drawDots();
}

function drawDots() {
  var host = document.getElementById('spkDots'); if (!host) return;
  var prog = Sparkle.get('oao.g3ela.progress', {});
  var items = [['1','7.1'],['2','7.2'],['3','7.3'],['4','7.4'],['fluency','Read Aloud']];
  host.innerHTML = '';
  items.forEach(function (it) {
    var day = it[0] === 'fluency' ? 'fluency' : parseInt(it[0], 10);
    var key = LESSON.week + '.' + (day === 'fluency' ? 'fluency' : day);
    var isMe = String(LESSON.day) === String(day);
    var done = prog[key] && prog[key].done;
    var d = document.createElement('span');
    d.className = 'spk-dot' + (isMe ? ' current' + (REDUCED ? '' : ' pulse') : (done ? ' done' : ''));
    d.textContent = it[1];
    var href = lessonHref(LESSON.week, day);
    if (!isMe && done && href) { d.onclick = function () { window.location.href = href; }; }
    if (isMe) d.title = 'You are here';
    host.appendChild(d);
  });
}

/* ── world palettes + vignettes (§2.10 atlas) ───────────────── */
/* ══════════════════════════════════════════════════════════════
   §2.2 / §2.3  THE READING JOURNEY
   One continuous illustrated map. A single winding road of 32
   week-spaces runs through eight regions that blend into each
   other; the student's owl stands on this week's space. The
   shelf lives in the same card, below the map.
   Lives on the Reading tab. The week's four dots stay up top.
   ══════════════════════════════════════════════════════════════ */

/* region identity: the wash of color the land takes on, and the
   ink the landmark and label are drawn in */
var REGION = {
  stanley: { wash:'#F3D9A6', ink:'#A8701F', label:'Stanley\u2019s Street' },
  nonfic:  { wash:'#CFE2C8', ink:'#4F7A3E', label:'The Post Office' },
  desp:    { wash:'#E4C7D6', ink:'#8A3E66', label:'The Mouse Castle' },
  wb:      { wash:'#C8CEE6', ink:'#3B4A86', label:'The North Tower' },
  med:     { wash:'#E2D6BC', ink:'#7A6234', label:'Knights\u2019 Hall' },
  lww:     { wash:'#D3E6EE', ink:'#2F6380', label:'The Lamp-Post' },
  ext:     { wash:'#F1D79C', ink:'#A8801F', label:'Journey\u2019s End' }
};

/* Landmarks sit on the land beside the road. Drawn around (0,0)
   with the ground at y = 0, roughly 70 wide. */
var LANDMARK = {
  stanley: function () {   /* an envelope with a stamp: Stanley travels by mail */
    return '<rect x="-26" y="-30" width="52" height="34" rx="2" fill="#FFFDF4" stroke="#C9A97F" stroke-width="1.6"/>' +
      '<path d="M-26 -30 L0 -10 L26 -30" fill="none" stroke="#C9A97F" stroke-width="1.6"/>' +
      '<rect x="12" y="-27" width="10" height="11" fill="#C0623F"/><circle cx="-14" cy="-4" r="0" fill="none"/>' +
      '<rect x="-34" y="-1" width="68" height="3" rx="1" fill="#A8701F" opacity=".35"/>';
  },
  nonfic: function () {    /* a mailbox and a rolled map */
    return '<rect x="-20" y="-30" width="22" height="18" rx="9" fill="#4F7A3E"/><rect x="-11" y="-12" width="4" height="12" fill="#5E4A2E"/>' +
      '<rect x="0" y="-32" width="3" height="10" fill="#C0623F"/>' +
      '<rect x="8" y="-14" width="26" height="12" rx="6" fill="#F6E9CE" stroke="#C9A97F" stroke-width="1.4"/>';
  },
  desp: function () {      /* a castle with a needle and spool of red thread */
    return '<path d="M-30 0 V-26 h7 v5 h6 v-5 h7 V0 Z" fill="#B9A8B4"/><path d="M-12 0 V-34 h8 v6 h6 v-6 h8 V0 Z" fill="#A595A2"/>' +
      '<rect x="-8" y="-12" width="6" height="12" rx="3" fill="#5E4A5A"/>' +
      '<rect x="18" y="-14" width="12" height="14" rx="2" fill="#C0392B"/><rect x="16" y="-16" width="16" height="3" fill="#8A6A4B"/><rect x="16" y="-1" width="16" height="3" fill="#8A6A4B"/>' +
      '<path d="M24 -16 L26 -40" stroke="#9AA4B0" stroke-width="1.6"/>';
  },
  wb: function () {        /* the north tower under a crescent moon, a crown at its foot */
    return '<path d="M-14 0 V-36 h-4 v-8 h6 v4 h5 v-4 h6 v4 h5 v-4 h6 v8 h-4 V0 Z" fill="#8F95AE"/>' +
      '<path d="M-3 -26 v-6 q3 -4 6 0 v6 Z" fill="#F2C14E"/>' +
      '<path d="M26 -44 a8 8 0 1 0 6 12 a6 6 0 1 1 -6 -12 Z" fill="#F4E7B8"/>' +
      '<path d="M18 0 L16 -10 L21 -6 L24 -12 L27 -6 L32 -10 L30 0 Z" fill="#E9C46A" stroke="#A8801F" stroke-width="1"/>';
  },
  med: function () {       /* a shield and a banner */
    return '<path d="M-16 -32 H8 V-16 Q8 -4 -4 2 Q-16 -4 -16 -16 Z" fill="#7A6234" stroke="#C7922C" stroke-width="2"/>' +
      '<path d="M-4 -30 V0" stroke="#C7922C" stroke-width="1.5"/>' +
      '<rect x="16" y="-40" width="2.5" height="40" fill="#5E4A2E"/><path d="M18.5 -40 h16 l-5 6 5 6 h-16 Z" fill="#C0392B"/>';
  },
  lww: function () {       /* a lamp-post in the snow */
    return '<ellipse cx="0" cy="-1" rx="34" ry="5" fill="#FFFFFF" opacity=".9"/>' +
      '<rect x="-1.6" y="-40" width="3.2" height="40" fill="#2F3B48"/>' +
      '<path d="M-6 -40 h12 l-2 -9 h-8 Z" fill="#2F3B48"/><rect x="-4.5" y="-48" width="9" height="8" fill="#FFE08A"/>' +
      '<circle cx="0" cy="-44" r="10" fill="#FFE08A" opacity=".3"/>' +
      '<path d="M18 0 L26 -24 L34 0 Z" fill="#2F6B4B"/><path d="M22 -12 L26 -22 L30 -12 Z" fill="#FFFFFF" opacity=".8"/>';
  },
  ext: function () {       /* an open book on a laurel */
    return '<path d="M0 -8 Q-18 -16 -34 -12 L-34 -34 Q-18 -38 0 -30 Z" fill="#FFFDF4" stroke="#D8C49A" stroke-width="1.2"/>' +
      '<path d="M0 -8 Q18 -16 34 -12 L34 -34 Q18 -38 0 -30 Z" fill="#FFFDF4" stroke="#D8C49A" stroke-width="1.2"/>' +
      '<path d="M0 -30 V-8" stroke="#C7922C" stroke-width="1.4"/>' +
      '<path d="M-38 -26 q-11 10 -6 24 M38 -26 q11 10 6 24" stroke="#6E9450" stroke-width="2.2" fill="none"/>';
  }
};

/* ── the painted board ──────────────────────────────────────
   Bethany's artwork is 1448x1086 and carries its own title, its own
   six worlds and its own forty spaces. Nothing here draws a map; it
   only lights up what the painting already shows. The coordinates
   were measured off the file (connected-component centroids), not
   eyeballed, so a repaint means re-measuring, not nudging.
   Thirty-six spaces, thirty-two weeks: a week claims its space by
   proportion, which keeps Start at week 1 and Finish at week 32
   without leaving gaps in the middle.                            */
var BOARD_W = 1536, BOARD_H = 1024, BOARD_R = 35;
/* the painted vignettes, measured off the artwork. A world the
   student has not reached yet is desaturated and veiled, exactly the
   way an unread book lies flat on the shelf: the board then shows the
   year filling with colour as they go. */
var BOARD_WORLDS = [
  { id:'stanley', x:  30, y: 700, w: 560, h: 310 },
  { id:'nonfic',  x: 740, y: 700, w: 780, h: 310 },
  { id:'desp',    x:  30, y: 470, w:1490, h: 240 },
  { id:'wb',      x:  40, y: 290, w:1040, h: 215 },
  { id:'med',     x:1060, y: 320, w: 460, h: 215 },
  { id:'lww',     x:  30, y:  95, w:1100, h: 235 },
  { id:'ext',     x:1110, y: 100, w: 410, h: 230 }
];
/* a world is 'reached' once this lesson's week is inside it or past
   it, or once storage says any of its weeks has been worked */
function worldReached(prog, id) {
  var b = COURSE.filter(function (c) { return c.id === id; })[0];
  if (!b) return true;
  if (LESSON.week >= b.weeks[0]) return true;
  for (var w = b.weeks[0]; w <= b.weeks[1]; w++) {
    for (var d = 1; d <= 4; d++) { var k = prog[w + '.' + d]; if (k && (k.done || (k.tabs && k.tabs.length))) return true; }
  }
  return false;
}
var BOARD_SPACES = [
  [296,961,'#A8701F'], [415,952,'#A8701F'], [535,940,'#A8701F'], [651,928,'#A8701F'], [777,923,'#A8701F'],
  [1241,917,'#4F7A3E'], [1364,916,'#4F7A3E'],
  [505,657,'#8A3E66'], [611,649,'#8A3E66'], [713,641,'#8A3E66'], [819,640,'#8A3E66'], [925,637,'#8A3E66'],
  [1033,640,'#8A3E66'], [1141,644,'#8A3E66'], [1243,656,'#8A3E66'], [1347,656,'#8A3E66'], [1444,627,'#8A3E66'],
  [544,467,'#3B4A86'], [665,449,'#3B4A86'], [785,447,'#3B4A86'], [908,449,'#3B4A86'], [1029,465,'#3B4A86'],
  [1213,489,'#7A6234'], [1352,478,'#7A6234'],
  [400,269,'#2F6380'], [527,267,'#2F6380'], [657,278,'#2F6380'], [778,280,'#2F6380'], [897,286,'#2F6380'], [1023,290,'#2F6380'],
  [1181,279,'#A8801F'], [1304,272,'#A8801F']
];
var BOARD_N = BOARD_SPACES.length;
/* ── where the owl stands ───────────────────────────────────────
   One step per LESSON DAY, not per week: 32 weeks x 4 lessons = 128
   days across 36 painted spaces, so the owl moves roughly one space
   every three lessons and the board lasts the whole year.

   The spaces are not divided evenly, because the artist placed the
   six vignettes for composition rather than in curriculum order. Each
   book is anchored to the stretch of path that actually runs past its
   own picture, so a student reading Anne stands under the green
   gables for all eight of those weeks. Freedom Train gets the
   left-hand loop, which suits a book about a journey (the road
   arrows straight past Prince Caspian's tree to get there); Prince Caspian gets the four spaces beneath its own tree.
   Change the artwork and these anchors have to be re-measured with
   it — they describe the painting, not the curriculum. */
var BOARD_LEGS = [
  { id:'stanley', weeks:[1,  5], spaces:[ 1,  5] },
  { id:'nonfic',  weeks:[6,  7], spaces:[ 6,  7] },
  { id:'desp',    weeks:[8, 17], spaces:[ 8, 17] },
  { id:'wb',      weeks:[18,22], spaces:[18, 22] },
  { id:'med',     weeks:[23,24], spaces:[23, 24] },
  { id:'lww',     weeks:[25,30], spaces:[25, 30] },
  { id:'ext',     weeks:[31,32], spaces:[31, 32] }
];
function legOfWeek(w) {
  for (var i = 0; i < BOARD_LEGS.length; i++) {
    if (w >= BOARD_LEGS[i].weeks[0] && w <= BOARD_LEGS[i].weeks[1]) return BOARD_LEGS[i];
  }
  return BOARD_LEGS[w < 1 ? 0 : BOARD_LEGS.length - 1];
}
/* the fluency page is not a numbered lesson day; it sits with day 4 */
function dayNum(d) { var n = parseInt(d, 10); return (n >= 1 && n <= 4) ? n : 4; }

/* lesson (week, day) -> space 1..36 */
function spaceOfLesson(w, d) {
  var leg = legOfWeek(w);
  var days = (leg.weeks[1] - leg.weeks[0] + 1) * 4;
  var idx  = (w - leg.weeks[0]) * 4 + dayNum(d);            /* 1..days */
  var n    = leg.spaces[1] - leg.spaces[0] + 1;
  var sp   = leg.spaces[0] + Math.floor((idx - 1) * n / days);
  return Math.max(leg.spaces[0], Math.min(leg.spaces[1], sp));
}
/* how many lesson days are behind this one, out of 128 */
function lessonIndex(w, d) { return (w - 1) * 4 + dayNum(d); }

/* space -> the week it belongs to, for the tooltip and the seal lookup */
function weekOfSpace(i) {
  for (var k = 0; k < BOARD_LEGS.length; k++) {
    var leg = BOARD_LEGS[k];
    if (i < leg.spaces[0] || i > leg.spaces[1]) continue;
    var n = leg.spaces[1] - leg.spaces[0] + 1;
    var days = (leg.weeks[1] - leg.weeks[0] + 1) * 4;
    var idx = Math.floor((i - leg.spaces[0]) * days / n);    /* 0-based day */
    return Math.min(leg.weeks[1], leg.weeks[0] + Math.floor(idx / 4));
  }
  return i <= 1 ? 1 : 32;
}

/* the one road, bottom-left to top-left, four passes */
var ROAD_D = 'M 58 600 C 200 580, 320 620, 460 598 C 600 576, 720 615, 812 591 ' +
             'C 868 577, 872 517, 812 497 C 700 475, 560 513, 420 489 ' +
             'C 300 469, 175 503, 104 479 C 46 460, 44 399, 104 377 ' +
             'C 220 357, 360 393, 500 371 C 620 353, 742 383, 816 361 ' +
             'C 872 345, 876 285, 816 263 C 700 241, 560 275, 430 253 ' +
             'C 344 239, 250 259, 176 241';

/* which region a given week belongs to */
function regionOfWeek(w) {
  for (var i = 0; i < COURSE.length; i++) {
    if (w >= COURSE[i].weeks[0] && w <= COURSE[i].weeks[1]) return COURSE[i];
  }
  return COURSE[0];
}
/* A student opening Lesson 7.1 has already read Mrs. Frisby — they
   just did it before any of this existed. So a week earlier than the
   one this lesson belongs to counts as travelled, whether or not
   local storage happens to remember it. Storage can only ever add to
   that picture, never take it away. */
function weekDone(prog, w) {
  if (w < LESSON.week) return 'done';
  var any = false, all = true;
  for (var d = 1; d <= 4; d++) {
    var k = w + '.' + d;
    if (prog[k] && prog[k].done) any = true; else all = false;
  }
  return all ? 'done' : (any ? 'started' : 'ahead');
}
/* likewise: a book whose last week is behind us has been read */
function bookRead(books, b) {
  if (books[b.id] && books[b.id].done) return true;
  return b.weeks[1] < LESSON.week;
}

/* ── the card, on the Reading tab ──────────────────────────── */
/* §2.10 chapter plate — under the quote banner, and on the left page
   of the open book. Printed with multiply so the illustration's own
   paper melts into the page instead of sitting in a white box. */
/* §2.10b the illuminated chapter numeral. A manuscript initial, set
   above the epigraph the way a chapter opens in a well-made children's
   book: numeral, then the line, then the picture. Purely decorative —
   the chapter is already named in the lesson header — so it is hidden
   from assistive tech. */
var ROMAN = [[10,'X'],[9,'IX'],[5,'V'],[4,'IV'],[1,'I']];
function roman(n) {
  var out = '';
  for (var i = 0; i < ROMAN.length; i++) { while (n >= ROMAN[i][0]) { out += ROMAN[i][1]; n -= ROMAN[i][0]; } }
  return out;
}
var WORDNUM = ['', 'ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT',
               'NINE', 'TEN', 'ELEVEN', 'TWELVE'];
function chapterNumbers() {
  var m = String(LESSON.chapters || '').match(/\d+/g);
  return m ? m.map(Number) : [];
}
function buildNumeral() {
  var quote = document.querySelector('.quote-strip'); if (!quote) return;
  var ns = chapterNumbers(); if (!ns.length) return;
  var n = ns[0];
  var rn = roman(n) || String(n);
  var size = rn.length > 2 ? 30 : 40;

  var fig = document.createElement('div');
  fig.className = 'spk-numeral';
  fig.setAttribute('aria-hidden', 'true');
  fig.innerHTML =
    '<svg viewBox="0 0 96 96" width="76" height="76">' +
      '<rect x="8" y="8" width="80" height="80" rx="4" fill="#0E1C42"/>' +
      '<rect x="12.5" y="12.5" width="71" height="71" rx="2.5" fill="none" stroke="#FFFDF7" stroke-width="1.1" opacity=".85"/>' +
      /* corner vines */
      '<path d="M16 34 q0 -18 18 -18 M80 62 q0 18 -18 18" stroke="#C7922C" stroke-width="1.6" fill="none" stroke-linecap="round"/>' +
      '<path d="M18 30 q7 -4 9 -11 q4 7 11 8 q-8 2 -10 10 q-3 -6 -10 -7 Z" fill="#C7922C" opacity=".9"/>' +
      '<path d="M78 66 q-7 4 -9 11 q-4 -7 -11 -8 q8 -2 10 -10 q3 6 10 7 Z" fill="#C7922C" opacity=".9"/>' +
      '<circle cx="74" cy="22" r="2.6" fill="#8FAE6A"/><circle cx="22" cy="74" r="2.6" fill="#8FAE6A"/>' +
      '<text x="48" y="' + (48 + size * 0.36) + '" font-size="' + size + '" text-anchor="middle" ' +
        'font-family="Lora,Georgia,serif" font-weight="700" fill="#E9C46A" letter-spacing="1">' + rn + '</text>' +
    '</svg>' +
    '<div class="spk-numeral-word">CHAPTER ' + (WORDNUM[n] || n) + '</div>';
  quote.parentNode.insertBefore(fig, quote);
}

function buildPlate() {
  /* built from the lesson's own book + chapters; hidden if absent */
  var src = plateSrc(); if (!src) return;

  var quote = document.querySelector('.quote-strip');
  if (quote) {
    var plate = document.createElement('figure');
    plate.className = 'spk-plate';
    var img = document.createElement('img');
    var dp = (DATA.plate && DATA.plate.src) ? DATA.plate : null;
    img.src = src; img.alt = (dp && dp.alt) || 'Chapter illustration'; img.loading = 'lazy';
    img.onerror = function () { plate.remove(); };
    plate.appendChild(img);
    if (dp) {
      plate.classList.add('spk-plate-photo');
      if (dp.look) {
        var lk = document.createElement('div');
        lk.className = 'g3-look g3-plate-look';
        var lh = document.createElement('div'); lh.className = 'g3-look-h'; lh.textContent = '\ud83d\udc40 What am I looking at?';
        var lp = document.createElement('p'); lp.textContent = dp.look;
        lk.appendChild(lh); lk.appendChild(lp); plate.appendChild(lk);
      }
      if (dp.credit) {
        var cap = document.createElement('figcaption');
        cap.className = 'spk-plate-credit'; cap.textContent = dp.credit;
        plate.appendChild(cap);
      }
    }
    quote.parentNode.insertBefore(plate, quote.nextSibling);
  }

  /* the open book gets the same picture on its left page */
  var left = document.querySelector('.open-book-left');
  if (left) {
    var deco = left.querySelector('.open-book-left-deco');
    if (deco) deco.style.display = 'none';
    var bi = document.createElement('img');
    bi.className = 'spk-book-plate'; bi.src = src; bi.alt = ''; bi.loading = 'lazy';
    bi.onerror = function () { bi.remove(); if (deco) deco.style.display = ''; };
    left.appendChild(bi);
  }
}

function buildJourney() {
  var panel = document.getElementById('tab-reading'); if (!panel) return;
  /* the old per-chapter tracker is retired — the Reading Road covers the
     same ground for the whole year, and two trackers on one tab is one
     too many */
  var after = panel.querySelector('.tracker-card');
  if (after) { after.remove(); after = null; }
  var card = document.createElement('div');
  card.className = 'spk-card spk-journey';
  /* The map and the shelf are a keepsake, not a task — lovely to visit,
     in the way every day. So the card folds, and remembers whether the
     student left it open. Closed is the default: the road is still one
     click away, and the chapter is the reason they came. */
  card.innerHTML =
    '<button type="button" class="spk-card-head spk-fold" id="spkRoadFold" aria-expanded="false" aria-controls="spkRoadBody">' +
      '<div class="spk-card-num">✦</div><div>' +
      '<div class="spk-card-title">The Reading Road</div>' +
      '<div class="spk-card-sub">Thirty-two weeks, one road, seven stops, and the shelf you fill as you go</div>' +
      '</div><span class="spk-fold-chev" aria-hidden="true"></span>' +
    '</button>' +
    '<div class="spk-card-body spk-journey-body" id="spkRoadBody" hidden>' +
      '<div class="spk-map-wrap"><svg class="spk-map" id="spkMap" viewBox="0 0 900 660"></svg></div>' +
      '<div class="spk-here" id="spkHere"></div>' +
      '<div class="spk-shelf-head">Your shelf</div>' +
      /* the case around the books. Purely decorative furniture — the
         books themselves are still the only thing in #spkShelf, so
         drawShelf() is untouched and nothing here is announced. */
      '<div class="spk-bookcase" aria-hidden="false">' +
        '<div class="spk-case-crown" aria-hidden="true">' +
          '<span class="spk-case-medallion"></span></div>' +
        '<span class="spk-case-dentil" aria-hidden="true"></span>' +
        '<div class="spk-case-body">' +
          '<span class="spk-case-stile left" aria-hidden="true"></span>' +
          '<div class="spk-shelf" id="spkShelf"></div>' +
          '<span class="spk-case-stile right" aria-hidden="true"></span>' +
          '<span class="spk-case-board" aria-hidden="true"></span>' +
        '</div>' +
        '<div class="spk-case-plinth" aria-hidden="true">' +
          '<span class="spk-case-foot left"></span>' +
          '<span class="spk-case-foot right"></span></div>' +
      '</div>' +
      '<div class="spk-shelf-note" id="spkShelfNote">A book stands up once you have read all of it.</div>' +
    '</div>';
  if (after && after.nextSibling) after.parentNode.insertBefore(card, after.nextSibling);
  else panel.insertBefore(card, panel.firstChild);
  var fold = document.getElementById('spkRoadFold');
  var body = document.getElementById('spkRoadBody');
  var openRoad = Sparkle.get('oao.g3ela.roadOpen', false) === true;
  function setFold(open) {
    body.hidden = !open;
    fold.setAttribute('aria-expanded', open ? 'true' : 'false');
    card.classList.toggle('spk-open-road', open);
    Sparkle.set('oao.g3ela.roadOpen', open);
    /* the map measures itself off the DOM, so it can only be drawn
       once the body is actually on the page */
    if (open) { try { drawMap(); drawShelf(); } catch (e) {} }
  }
  fold.onclick = function () { setFold(body.hidden); };
  setFold(openRoad);
}

/* ── §2.2 the painted board, lit up ─────────────────────────────
   The picture is the base layer. On top of it go exactly three
   things: a cream veil over the road still ahead, an ink fill on
   the spaces already travelled, and the owl standing on today's
   space. If the art ever fails to load the generated road below
   is still there to fall back on. */
function drawBoardMap(svg) {
  var prog  = Sparkle.get('oao.g3ela.progress', {});
  var seals = Sparkle.get('oao.g3ela.scholar', {});
  var p     = profile();
  var art   = artURL(ART.board.src);
  var cur   = spaceOfLesson(LESSON.week, LESSON.day);

  svg.setAttribute('viewBox', '0 0 ' + BOARD_W + ' ' + BOARD_H);
  svg.classList.add('spk-map-board');

  var s = '<defs><filter id="spkUnread" color-interpolation-filters="sRGB">' +
          '<feColorMatrix type="saturate" values="0.10"/></filter>';
  /* a blurred mask rather than a hard clip: a rectangle with visible
     corners would read as a UI panel dropped on the painting. Feathered,
     it reads as light that has not reached that part of the board yet. */
  s += '<filter id="spkSoftEdge" x="-20%" y="-20%" width="140%" height="140%">' +
       '<feGaussianBlur stdDeviation="17"/></filter>';
  BOARD_WORLDS.forEach(function (v) {
    s += '<mask id="spkWorldMask_' + v.id + '" maskUnits="userSpaceOnUse" ' +
         'x="0" y="0" width="' + BOARD_W + '" height="' + BOARD_H + '">' +
         '<rect x="' + (v.x + 6) + '" y="' + (v.y + 6) + '" width="' + (v.w - 12) +
         '" height="' + (v.h - 12) + '" rx="26" fill="#fff" filter="url(#spkSoftEdge)"/></mask>';
  });
  s += '</defs>';
  s += '<image id="spkBoardImg" href="' + art + '" x="0" y="0" width="' + BOARD_W + '" height="' + BOARD_H + '"/>';

  /* worlds not yet reached lie quiet — colour drained, paper veiled */
  BOARD_WORLDS.forEach(function (v) {
    if (worldReached(prog, v.id)) return;
    s += '<g class="spk-world-unread" data-world="' + v.id + '" mask="url(#spkWorldMask_' + v.id + ')">' +
         '<use href="#spkBoardImg" filter="url(#spkUnread)"/>' +
         '<rect x="' + v.x + '" y="' + v.y + '" width="' + v.w + '" height="' + v.h +
         '" fill="#FBF3DF" opacity=".40"/></g>';
  });

  /* the student's name, hand-written into the open field the artist
     left in the middle of the board. Second place the name appears. */
  if (p && p.name) {
    s += '<text x="768" y="148" font-size="26" text-anchor="middle" ' +
         'font-family="Lora,Georgia,serif" font-style="italic" fill="#8B6914" opacity=".85">' +
         esc(p.name) + '’s journey</text>';
  }

  for (var i = 1; i <= BOARD_N; i++) {
    var sp = BOARD_SPACES[i - 1], x = sp[0], y = sp[1], ink = sp[2];
    var w  = weekOfSpace(i);
    var st = i < cur ? 'done' : (i === cur ? 'here' : weekDone(prog, w));
    s += '<g class="spk-space spk-' + st + '" data-week="' + w + '" data-space="' + i + '">' +
         '<title>Week ' + w + ' · ' + REGION[regionOfWeek(w).id].label + '</title>';

    var sealed = !!seals['w' + w];
    var sealArt = artURL((ART.seals || {}).mark) || artURL((ART.seals || {}).scholar);
    if (st === 'done' && sealed && sealArt) {
      /* a week that earned the Scholar's mark wears the seal instead of
         the tick — the higher honour replaces the lower one, and it sits
         inside the space's own footprint so it can never collide with
         the owl standing on today's space */
      s += '<circle cx="' + x + '" cy="' + y + '" r="' + BOARD_R + '" fill="' + ink + '" opacity=".88"/>';
    } else if (st === 'done') {
      s += '<circle cx="' + x + '" cy="' + y + '" r="' + BOARD_R + '" fill="' + ink + '" opacity=".88"/>' +
           '<path d="M' + (x - 9) + ' ' + y + ' l6 7 12 -14" stroke="#FFF8E9" stroke-width="4" ' +
           'fill="none" stroke-linecap="round" stroke-linejoin="round"/>';
    } else if (st === 'here') {
      s += '<circle cx="' + x + '" cy="' + y + '" r="' + (BOARD_R + 6) + '" fill="none" ' +
           'stroke="#C7922C" stroke-width="5"/>';
    } else {
      /* still ahead: veil it back so the travelled road reads first */
      s += '<circle cx="' + x + '" cy="' + y + '" r="' + (BOARD_R + 1) + '" fill="#FBF3DF" opacity=".5"/>';
      if (st === 'started') {
        s += '<circle cx="' + x + '" cy="' + y + '" r="8" fill="' + ink + '" opacity=".55"/>';
      }
    }
    if (sealed) {                               /* the Scholar's mark for that week */
      if (sealArt) {
        s += '<image href="' + sealArt + '" x="' + (x - 27) + '" y="' + (y - 27) +
             '" width="54" height="54" preserveAspectRatio="xMidYMid meet"/>';
      } else {
        s += '<path d="M' + (x - 26) + ' ' + (y + 4) + ' q-7 -19 7 -30 M' +
             (x + 26) + ' ' + (y + 4) + ' q7 -19 -7 -30" stroke="#C7922C" stroke-width="4" ' +
             'fill="none" stroke-linecap="round"/>';
      }
    }
    s += '</g>';
  }

  /* the owl stands on today's space */
  var me = BOARD_SPACES[cur - 1], OW = 124;
  /* the owl stands clear of the ring rather than on top of it, so the
     gold marker still reads as the space the student is on */
  var oy = me[1] - OW - 26;
  s += '<g transform="translate(' + (me[0] - OW / 2) + ',' + oy + ')">' +
       owlMarkSVG(p && p.owl ? p.owl : defaultCompanion(), OW) + '</g>';
  var label = 'LESSON ' + LESSON.week + '.' + dayNum(LESSON.day);
  var bw = 20 + label.length * 10.5;
  var bx = Math.max(8, Math.min(BOARD_W - bw - 8, me[0] - bw / 2)), by = me[1] + BOARD_R + 12;
  s += '<rect x="' + bx + '" y="' + by + '" width="' + bw + '" height="34" rx="17" fill="#C7922C" stroke="#FFF8E9" stroke-width="2"/>' +
       '<text x="' + (bx + bw / 2) + '" y="' + (by + 24) + '" font-size="18" text-anchor="middle" ' +
       'font-family="Nunito,sans-serif" font-weight="800" fill="#FFF8E9">' + label + '</text>';

  svg.innerHTML = s;

  var here = document.getElementById('spkHere');
  if (here) {
    var behind = lessonIndex(LESSON.week, LESSON.day) - 1;
    here.textContent = 'Lesson ' + LESSON.week + '.' + dayNum(LESSON.day) + ' \u2014 week ' +
      LESSON.week + ' of 32, in ' + REGION[LESSON.book].label + '. ' +
      behind + (behind === 1 ? ' lesson' : ' lessons') + ' behind you, of 128.';
  }
}

function drawMap() {
  var svg = document.getElementById('spkMap'); if (!svg) return;
  if (artURL((ART.board || {}).src)) { drawBoardMap(svg); return; }
  var prog = Sparkle.get('oao.g3ela.progress', {});
  var books = Sparkle.get('oao.g3ela.books', {});
  var seals = Sparkle.get('oao.g3ela.scholar', {});
  var p = profile();

  /* 1. the land: soft washes that bleed into one another */
  var defs = '<radialGradient id="spkVig" cx="50%" cy="50%" r="62%">' +
    '<stop offset="60%" stop-color="#FFF8E9" stop-opacity="0"/>' +
    '<stop offset="100%" stop-color="#E8D6AE" stop-opacity=".55"/></radialGradient>';
  var s = '<rect width="900" height="660" fill="#FCF3DF"/>';

  /* measure the road so everything can be placed along it */
  svg.innerHTML = '<path id="spkRoadMeasure" d="' + ROAD_D + '" fill="none"/>';
  var road = svg.querySelector('#spkRoadMeasure');
  var L = road.getTotalLength();
  function at(t) { var pt = road.getPointAtLength(Math.max(0, Math.min(L, t * L))); return { x: pt.x, y: pt.y }; }

  /* week w (1..32) sits at this fraction along the road */
  function weekT(w) { return (w - 0.5) / 32; }

  COURSE.forEach(function (b, i) {
    var r = REGION[b.id];
    var mid = at(weekT((b.weeks[0] + b.weeks[1]) / 2));
    var span = (b.weeks[1] - b.weeks[0] + 1);
    var rad = 92 + span * 9;
    var terrain = artURL((ART.worlds[b.id] || {}).terrain);
    /* one feather mask per region — this is what keeps eight pieces
       of art reading as a single continuous land */
    defs += '<radialGradient id="spkFeather' + i + '" cx="50%" cy="50%" r="50%">' +
            '<stop offset="0" stop-color="#fff" stop-opacity="1"/>' +
            '<stop offset="58%" stop-color="#fff" stop-opacity=".92"/>' +
            '<stop offset="100%" stop-color="#fff" stop-opacity="0"/></radialGradient>' +
            '<mask id="spkMask' + i + '"><circle cx="' + mid.x.toFixed(1) + '" cy="' + mid.y.toFixed(1) +
            '" r="' + rad + '" fill="url(#spkFeather' + i + ')"/></mask>';
    if (terrain) {
      s += '<g mask="url(#spkMask' + i + ')"><image href="' + terrain + '" x="' + (mid.x - rad).toFixed(1) +
           '" y="' + (mid.y - rad).toFixed(1) + '" width="' + (rad * 2) + '" height="' + (rad * 2) +
           '" preserveAspectRatio="xMidYMid slice"/></g>';
    } else {
      defs += '<radialGradient id="spkW' + b.id + '" cx="50%" cy="50%" r="50%">' +
              '<stop offset="0" stop-color="' + r.wash + '" stop-opacity=".92"/>' +
              '<stop offset="65%" stop-color="' + r.wash + '" stop-opacity=".45"/>' +
              '<stop offset="100%" stop-color="' + r.wash + '" stop-opacity="0"/></radialGradient>';
      s += '<circle cx="' + mid.x.toFixed(1) + '" cy="' + mid.y.toFixed(1) + '" r="' + rad +
           '" fill="url(#spkW' + b.id + ')"/>';
    }
  });

  /* 2. the road itself */
  s += '<path d="' + ROAD_D + '" fill="none" stroke="#C9A97F" stroke-width="17" stroke-linecap="round"/>';
  s += '<path d="' + ROAD_D + '" fill="none" stroke="#F6E9CE" stroke-width="12" stroke-linecap="round"/>';

  /* 3. landmarks stand on the land above the road; the name sits below it */
  COURSE.forEach(function (b) {
    var r = REGION[b.id];
    var mid = at(weekT((b.weeks[0] + b.weeks[1]) / 2));
    var fin = bookRead(books, b);
    var lm = artURL((ART.worlds[b.id] || {}).landmark);
    if (lm) {
      s += '<image href="' + lm + '" x="' + (mid.x - 55).toFixed(1) + '" y="' + (mid.y - 104).toFixed(1) +
           '" width="110" height="82" preserveAspectRatio="xMidYMax meet"/>';
    } else {
      s += '<g transform="translate(' + mid.x.toFixed(1) + ',' + (mid.y - 26).toFixed(1) + ')">' +
           LANDMARK[b.id]() + '</g>';
    }
    var name = r.label + ' \u00b7 Wk ' +
      (b.weeks[0] === b.weeks[1] ? b.weeks[0] : b.weeks[0] + '\u2013' + b.weeks[1]) +
      (fin ? ' \u00b7 read' : '');
    s += '<text x="' + mid.x.toFixed(1) + '" y="' + (mid.y + 27).toFixed(1) + '" font-size="13.5" text-anchor="middle" ' +
         'font-family="Lora,Georgia,serif" font-style="italic" paint-order="stroke" stroke="#FCF3DF" stroke-width="4.5" ' +
         'stroke-linejoin="round" fill="' + r.ink + '">' + name + '</text>';
  });

  /* 4. the thirty-two week spaces */
  for (var w = 1; w <= 32; w++) {
    var pt = at(weekT(w));
    var st = weekDone(prog, w);
    var cur = w === LESSON.week;
    var ink = REGION[regionOfWeek(w).id].ink;
    var fill = st === 'done' ? ink : st === 'started' ? '#FFFDF4' : '#FFFDF4';
    s += '<g class="spk-space" data-week="' + w + '"><title>Week ' + w + ' · ' + REGION[regionOfWeek(w).id].label + '</title>' +
      '<circle cx="' + pt.x.toFixed(1) + '" cy="' + pt.y.toFixed(1) + '" r="' + (cur ? 11 : 8) + '" fill="' + fill +
        '" stroke="' + (cur ? '#C7922C' : ink) + '" stroke-width="' + (cur ? 3 : 1.8) + '" opacity="' + (st === 'ahead' && !cur ? .5 : 1) + '"/>';
    if (st === 'started' && !cur) {
      s += '<circle cx="' + pt.x.toFixed(1) + '" cy="' + pt.y.toFixed(1) + '" r="4" fill="' + ink + '" opacity=".55"/>';
    }
    if (seals['w' + w]) {                              /* a Scholar's laurel on that week */
      s += '<path d="M' + (pt.x - 11).toFixed(1) + ' ' + (pt.y + 2).toFixed(1) + ' q-3 -8 3 -13 M' +
           (pt.x + 11).toFixed(1) + ' ' + (pt.y + 2).toFixed(1) + ' q3 -8 -3 -13" stroke="#C7922C" stroke-width="2" fill="none" stroke-linecap="round"/>';
    }
    s += '</g>';
  }

  /* 5. the owl guide — the student's traveller on the road */
  var me = at(weekT(LESSON.week));
  var OW = 66;
  s += '<ellipse cx="' + me.x.toFixed(1) + '" cy="' + (me.y + 6).toFixed(1) +
    '" rx="22" ry="6" fill="#6B4E2A" opacity=".2"/>';
  s += '<g transform="translate(' + (me.x - OW / 2).toFixed(1) + ',' + (me.y - OW - 2).toFixed(1) + ')">' +
    owlMarkSVG(p && p.owl ? p.owl : defaultCompanion(), OW) + '</g>';
  var bw = 72, right = me.x < 760;
  var bx = right ? me.x + 24 : me.x - 24 - bw;
  s += '<rect x="' + bx.toFixed(1) + '" y="' + (me.y - 44).toFixed(1) +
    '" width="' + bw + '" height="19" rx="9.5" fill="#C7922C"/>' +
    '<text x="' + (bx + bw / 2).toFixed(1) + '" y="' + (me.y - 30).toFixed(1) + '" font-size="10.5" text-anchor="middle" ' +
    'font-family="Nunito,sans-serif" font-weight="800" fill="#FFF8E9">WEEK ' + LESSON.week + '</text>';

  s += '<rect width="900" height="660" fill="url(#spkVig)" pointer-events="none"/>';
  /* the second place their name appears: the map is the keepsake */
  var who = (p && p.name) ? esc(p.name) + '’s Year of Reading' : 'A Year of Reading';
  s += '<text x="450" y="34" font-size="19" text-anchor="middle" font-family="Lora,Georgia,serif" font-style="italic" fill="#8B6914">' +
       who + ' · Grade Three</text>';

  svg.innerHTML = '<defs>' + defs + '</defs>' + s;

  var here = document.getElementById('spkHere');
  if (here) {
    var done = 0; for (var k = 1; k <= 32; k++) if (weekDone(prog, k) === 'done') done++;
    here.innerHTML = '';
    var line = document.createElement('span');
    line.textContent = 'You are on week ' + LESSON.week + ' of 32, in ' +
      REGION[LESSON.book].label + '. ' + done + (done === 1 ? ' week' : ' weeks') + ' behind you.';
    here.appendChild(line);
  }
}

function drawShelf(fillId) {
  var host = document.getElementById('spkShelf'); if (!host) return;
  var books = Sparkle.get('oao.g3ela.books', {});
  host.innerHTML = '';
  host.classList.toggle('spk-shelf-covers', SHELF.some(function (b) { return !!artURL(ART.covers[b.id]); }));

  SHELF.forEach(function (b) {
    var course = COURSE.filter(function (c) { return c.id === b.id; })[0];
    var done = !b.writing && course && bookRead(books, course);
    var cover = artURL(ART.covers[b.id]);
    var el = document.createElement('div');
    el.className = 'spk-book' + (done ? ' read' : '') + (cover ? ' has-cover' : ' no-cover') +
                   (b.gold ? ' gold' : '') + (b.writing ? ' writing' : '');

    if (cover) {
      var im = document.createElement('img');
      im.className = 'spk-book-cover';
      im.src = cover; im.alt = b.short; im.loading = 'lazy';
      /* a cover that fails to load must not leave a hole */
      im.onerror = function () { el.classList.remove('has-cover'); el.classList.add('no-cover'); im.remove(); addSpine(); };
      el.appendChild(im);
    } else { addSpine(); }

    function addSpine() {
      var sp = document.createElement('span');
      sp.className = 'spk-book-spine'; sp.textContent = b.short;
      el.appendChild(sp);
    }

    if (!b.writing) {
      el.title = done ? b.short + ' \u2014 read' : 'Find ' + REGION[b.id].label + ' on the map';
      el.onmouseenter = function () { flashRegion(b.id, true); };
      el.onmouseleave = function () { flashRegion(b.id, false); };
      el.onclick = function () { flashRegion(b.id, true); setTimeout(function () { flashRegion(b.id, false); }, 1400); };
    } else { el.title = 'Your own writing, published at the end of the year'; }

    if (b.id === fillId && !REDUCED) {
      el.classList.add('spk-book-arriving');
      setTimeout(function () { el.classList.remove('spk-book-arriving'); }, 40);
    }
    host.appendChild(el);
  });
}

/* ring the weeks of one book on the map — the shelf and the road
   are the same journey seen two ways */
function flashRegion(bookId, on) {
  var svg = document.getElementById('spkMap'); if (!svg) return;
  var b = COURSE.filter(function (x) { return x.id === bookId; })[0]; if (!b) return;
  svg.querySelectorAll('.spk-space').forEach(function (g) {
    var w = +g.getAttribute('data-week');
    var mine = w >= b.weeks[0] && w <= b.weeks[1];
    var c = g.querySelector('circle');
    if (!mine || !c) return;
    if (on) { c.setAttribute('stroke', '#C7922C'); c.setAttribute('stroke-width', '3.4'); c.setAttribute('opacity', '1'); }
    else { drawMap(); }
  });
}

document.addEventListener('oao:bookfinished', function (e) {
  drawMap(); drawShelf(e.detail.book.id);
  owlSay('The book is closed, and kept.');
  var note = document.getElementById('spkShelfNote');
  if (note) note.innerHTML = 'You have read all of <em>' + e.detail.book.title + '</em>. It is on your shelf now!';
});

function buildDolChoice() {
  if (!DATA.dol || !DATA.dol.a || !DATA.dol.b) return;   /* no second sentence for this lesson */
  var label = document.querySelector('.dol-fix-label'); if (!label) return;
  var old = label.nextElementSibling;                       /* .dol-sentence-wrap  */
  var hint = old && old.nextElementSibling;                  /* .dol-hint           */
  var btn = document.querySelector('.dol-check-btn');
  var ans = document.getElementById('dolAns');
  if (!old || !ans) return;

  label.innerHTML = '🔧 Choose one to fix';
  old.style.display = 'none';

  var box = document.createElement('div');
  box.className = 'spk-dol-choice'; box.id = 'spkDolChoice';
  box.innerHTML =
    '<div class="spk-dol-card" data-pick="a"><span class="spk-dol-tag">Sentence A</span><span class="spk-dol-text">' + DATA.dol.a.raw + '</span></div>' +
    '<div class="spk-dol-card" data-pick="b"><span class="spk-dol-tag">Sentence B</span><span class="spk-dol-text">' + DATA.dol.b.raw + '</span></div>';
  label.parentNode.insertBefore(box, old);

  var swap = document.createElement('button');
  swap.type = 'button'; swap.className = 'spk-dol-swap'; swap.textContent = 'Show me the other one instead';
  swap.style.display = 'none';
  box.parentNode.insertBefore(swap, box.nextSibling);

  function paint(pick) {
    box.querySelectorAll('.spk-dol-card').forEach(function (c) {
      var mine = c.getAttribute('data-pick') === pick;
      c.classList.toggle('chosen', mine);
      c.classList.toggle('folded', !!pick && !mine);
    });
    swap.style.display = pick ? 'inline-block' : 'none';
    if (hint) hint.style.display = pick ? '' : 'none';
    if (btn) btn.style.display = pick ? '' : 'none';
    if (pick) {
      ans.innerHTML =
        '<p style="margin-bottom:6px;"><strong>Corrected:</strong> ' + DATA.dol[pick].fixed + '</p>' +
        '<p style="font-size:13px;color:#7A88A8;font-style:italic;">' + DATA.dol[pick].why + '</p>';
    } else { ans.classList.remove('show'); }
  }
  box.querySelectorAll('.spk-dol-card').forEach(function (c) {
    c.onclick = function () {
      var pick = c.getAttribute('data-pick');
      var all = Sparkle.get('oao.g3ela.dol', {}); all[LID] = pick; Sparkle.set('oao.g3ela.dol', all);
      paint(pick);
    };
  });
  swap.onclick = function () {
    var all = Sparkle.get('oao.g3ela.dol', {});
    var next = all[LID] === 'a' ? 'b' : 'a';
    all[LID] = next; Sparkle.set('oao.g3ela.dol', all);
    ans.classList.remove('show'); paint(next);
  };
  paint(Sparkle.get('oao.g3ela.dol', {})[LID] || null);
}

/* ══════════════════════════════════════════════════════════════
   §2.5  EXPLORER / SCHOLAR   +   §2.6  COACHING
   ══════════════════════════════════════════════════════════════ */
/* ══════════════════════════════════════════════════════════════
   §2.5  EXPLORER / SCHOLAR — the two roads
   Choosing Scholar has to feel like choosing something, so it
   pays three ways, all of them visible and none of them points:
     · the section illuminates the moment you choose it
     · finishing it seals the work with a laurel
     · the seal shows on your published page, in the work you
       turn in, and on that week's space on the map
   ══════════════════════════════════════════════════════════════ */
function currentTier() {
  var t = Sparkle.get('oao.g3ela.tier', {});
  return t[LID] || t._last || 'explorer';
}
function setTier(v) {
  var t = Sparkle.get('oao.g3ela.tier', {});
  t[LID] = v; t._last = v; Sparkle.set('oao.g3ela.tier', t);
}
function hasSeal() { return !!Sparkle.get('oao.g3ela.scholar', {})[LID]; }
function grantSeal() {
  var s = Sparkle.get('oao.g3ela.scholar', {});
  if (s[LID]) return false;
  s[LID] = true; s['w' + LESSON.week] = true;
  Sparkle.set('oao.g3ela.scholar', s);
  return true;
}

function laurelSVG(size) {
  size = size || 76;
  /* the painted seal when there is one; the drawn fallback below
     otherwise, so the mark never simply disappears. Under ~56px the
     wreath closes into a smudge, so the wax disc alone is used. */
  var seal = ART.seals || {};
  var src = (size < 56 ? (artURL(seal.mark) || artURL(seal.scholar))
                       : (artURL(seal.scholar) || artURL(seal.mark)));
  if (src) {
    return '<img class="spk-seal-img" src="' + src + '" width="' + size +
           '" alt="" aria-hidden="true" loading="lazy">';
  }
  return '<svg viewBox="0 0 100 100" width="' + size + '" height="' + size + '" aria-hidden="true">' +
    '<circle cx="50" cy="50" r="30" fill="#FFF3DC" stroke="#C7922C" stroke-width="2"/>' +
    '<path d="M32 24 Q14 46 30 74 M68 24 Q86 46 70 74" stroke="#6E9450" stroke-width="3" fill="none" stroke-linecap="round"/>' +
    '<ellipse cx="24" cy="36" rx="6" ry="3" fill="#7DA85C" transform="rotate(-40 24 36)"/>' +
    '<ellipse cx="20" cy="50" rx="6" ry="3" fill="#7DA85C" transform="rotate(-8 20 50)"/>' +
    '<ellipse cx="24" cy="64" rx="6" ry="3" fill="#7DA85C" transform="rotate(26 24 64)"/>' +
    '<ellipse cx="76" cy="36" rx="6" ry="3" fill="#7DA85C" transform="rotate(40 76 36)"/>' +
    '<ellipse cx="80" cy="50" rx="6" ry="3" fill="#7DA85C" transform="rotate(8 80 50)"/>' +
    '<ellipse cx="76" cy="64" rx="6" ry="3" fill="#7DA85C" transform="rotate(-26 76 64)"/>' +
    (size >= 56
      ? '<text x="50" y="45" font-size="15" text-anchor="middle" font-family="Lora,Georgia,serif" font-style="italic" fill="#8B6914">Scholar</text>' +
        '<path d="M34 52 h32" stroke="#C7922C" stroke-width="1.2"/>' +
        '<text x="50" y="66" font-size="10.5" text-anchor="middle" font-family="Nunito,sans-serif" font-weight="800" fill="#A8801F">EVIDENCE</text>'
      : '<path d="M38 50 l7 8 16 -18" stroke="#C7922C" stroke-width="5" fill="none" stroke-linecap="round" stroke-linejoin="round"/>') +
    '</svg>';
}

function buildTiers() {
  if (!DATA.scholar) return;                            /* no Scholar clauses for this lesson */
  var q1 = document.getElementById('journal-q1'); if (!q1) return;
  var body = q1.closest('.activity-body');
  var firstBlock = body.querySelector('.q-block'); if (!firstBlock) return;
  var activity = q1.closest('.activity');

  var sw = document.createElement('div');
  sw.className = 'spk-roads';
  sw.innerHTML =
    '<div class="spk-roads-label">Pick how you want to answer today\u2019s three questions.</div>' +
    '<div class="spk-roads-cards">' +
      '<button type="button" class="spk-road" data-tier="explorer">' +
        '<span class="spk-road-name">Explorer</span>' +
        '<span class="spk-road-line">Answer all three questions.</span>' +
      '</button>' +
      '<button type="button" class="spk-road" data-tier="scholar">' +
        '<span class="spk-road-laurel">' + laurelSVG(46) + '</span>' +
        '<span class="spk-road-name">Scholar \u2014 go further</span>' +
        '<span class="spk-road-line">Every question asks you for <b>one more thing</b>: another detail, ' +
        'or <b>why</b> you think so. Finish all three and you earn the Scholar\u2019s seal.</span>' +
      '</button>' +
    '</div>' +
    '<div class="spk-roads-note">Either one finishes the lesson. You can switch whenever you want.</div>' +
    '<div class="spk-seal-strip" id="spkSealStrip"></div>';
  firstBlock.parentNode.insertBefore(sw, firstBlock);

  Object.keys(DATA.scholar).forEach(function (id) {
    var ta = document.getElementById(id); if (!ta) return;
    var block = ta.previousElementSibling;
    while (block && !block.classList.contains('q-block')) block = block.previousElementSibling;
    if (!block) return;
    var add = document.createElement('span');
    add.className = 'spk-scholar-add'; add.setAttribute('data-for', id);
    add.textContent = DATA.scholar[id]; add.style.display = 'none';
    block.querySelector('.q-text').appendChild(add);
  });

  function paint(v) {
    sw.querySelectorAll('.spk-road').forEach(function (b) {
      b.classList.toggle('on', b.getAttribute('data-tier') === v);
    });
    document.querySelectorAll('.spk-scholar-add').forEach(function (a) {
      a.style.display = v === 'scholar' ? 'block' : 'none';
    });
    if (activity) activity.classList.toggle('spk-illuminated', v === 'scholar');
    Object.keys(DATA.flags).forEach(function (id) { coach(document.getElementById(id)); });
    sealCheck(true);
  }
  sw.querySelectorAll('.spk-road').forEach(function (b) {
    b.onclick = function () {
      var v = b.getAttribute('data-tier'), was = currentTier();
      setTier(v); paint(v);
      if (v === 'scholar' && was !== 'scholar') {
        owlSay('The longer road, then. Good.');
        if (!REDUCED && activity) {
          activity.classList.remove('spk-lightup'); void activity.offsetWidth; activity.classList.add('spk-lightup');
        }
      }
    };
  });
  paint(currentTier());
}

/* the seal lands when all three Scholar answers are actually done */
function sealCheck(quiet) {
  var strip = document.getElementById('spkSealStrip'); if (!strip) return;
  var ids = Object.keys(DATA.scholar);
  var earned = hasSeal();

  if (currentTier() !== 'scholar' && !earned) { strip.innerHTML = ''; return; }

  if (!earned) {
    var ready = 0;
    ids.forEach(function (id) {
      var ta = document.getElementById(id);
      if (ta && words(ta.value) >= 20) ready++;
    });
    if (ready >= ids.length) {
      earned = grantSeal();
      if (!quiet && earned) {
        owlSay('Sealed. That is scholar’s work.');
        /* deliberately no confetti here: the stamp is the reward, and the
           spec's rule is classical, not gamified. To add it back, this
           line is all it takes:   window.fireConfetti();                */
      }
    } else {
      strip.innerHTML = '<div class="spk-seal-progress">' +
        '<span class="spk-seal-ghost">' + laurelSVG(40) + '</span>' +
        '<span><b>' + ready + ' of ' + ids.length + ' answers are long enough so far.</b><br>' +
        'To earn the seal, write about 3 sentences for each question, and say <b>why</b> you think so ' +
        '\u2014 or use words from the book.</span></div>';
      return;
    }
  }

  if (earned && !strip.querySelector('.spk-seal-won')) {
    strip.innerHTML = '<div class="spk-seal-won">' +
      '<span class="spk-seal-stamp">' + laurelSVG(86) + '</span>' +
      '<span><b>You earned the Scholar\u2019s seal.</b><br>It goes on the work you hand in, on your ' +
      'published page, and on Week ' + LESSON.week + ' of your Reading Road.</span></div>';
    drawMapIfPresent();
    if (window.gatherAnswers) window.gatherAnswers();
  }
}
function drawMapIfPresent() {
  var b = document.getElementById('spkRoadBody');
  if (b && b.hidden) return;                 /* folded away — nothing to redraw */
  if (document.getElementById('spkMap')) drawMap();
}

function words(s) { return (s.trim().match(/[A-Za-z0-9'’-]+/g) || []).length; }
function hasQuote(s) {
  return /"[^"]{2,}"/.test(s) || /“[^”]{2,}”/.test(s) || /'[^']{4,}'/.test(s);
}
function countCues(s) {
  var t = ' ' + s.toLowerCase() + ' ';
  var cues = [' and ', ' also ', ' second ', ' another ', ' then ', ' too '];
  var n = 0; cues.forEach(function (c) { if (t.indexOf(c) !== -1) n++; });
  if ((s.match(/[.!?]\s+[A-Za-z]/g) || []).length >= 1) n++;
  return n;
}

function coach(ta) {
  if (!ta) return;
  var line = ta.parentNode.querySelector('.spk-coach[data-for="' + ta.id + '"]');
  if (!line) return;
  var flags = (DATA.flags || {})[ta.id] || {};
  var v = ta.value, w = words(v);
  var minW = currentTier() === 'scholar' ? 20 : 12;
  line.classList.remove('good');
  if (!v.trim()) { line.textContent = ''; return; }
  if (w < minW) { line.textContent = 'Keep going — a full answer is about three sentences.'; return; }
  if (flags.quote && !hasQuote(v)) { line.textContent = 'Add words from the book, with "quotation marks" around them.'; return; }
  if (flags.count >= 2 && countCues(v) < 2) { line.textContent = 'This question asks for two details. I can only find one so far.'; return; }
  if (/\bbecause\b|\bso\b/i.test(v) || hasQuote(v)) {
    line.textContent = 'Good — you told why, and you used the book.'; line.classList.add('good');
    clearTimeout(line._t); line._t = setTimeout(function () { line.style.opacity = '0'; setTimeout(function () { line.textContent=''; line.style.opacity=''; }, 260); }, 3000);
    return;
  }
  line.textContent = '';
}

function buildCoaches() {
  if (!DATA.flags) return;                              /* no coaching flags for this lesson */
  Object.keys(DATA.flags).forEach(function (id) {
    var ta = document.getElementById(id); if (!ta) return;
    var line = document.createElement('div');
    line.className = 'spk-coach'; line.setAttribute('data-for', id);
    ta.parentNode.insertBefore(line, ta.nextSibling);
    var t = null;
    ta.addEventListener('input', function () {
      line.style.opacity = ''; clearTimeout(t);
      t = setTimeout(function () { coach(ta); sealCheck(false); }, 400);
    });
    coach(ta);
  });
}

/* ══════════════════════════════════════════════════════════════
   §2.7  HINT LADDERS + DISTRACTOR FEEDBACK
   ══════════════════════════════════════════════════════════════ */
function bumpHint(key) {
  var h = Sparkle.get('oao.g3ela.hints', {});
  h[LID + ':' + key] = (h[LID + ':' + key] || 0) + 1;
  Sparkle.set('oao.g3ela.hints', h);
  return h[LID + ':' + key];
}
function hintSlot(inp) {
  var slot = inp.parentNode.querySelector('.spk-hint');
  if (!slot) {
    slot = document.createElement('div'); slot.className = 'spk-hint';
    inp.parentNode.appendChild(slot);
  }
  return slot;
}
function blanks(word) {
  return word.charAt(0) + ' ' + word.slice(1).split('').map(function () { return '_'; }).join(' ');
}
window._spkRevealed = window._spkRevealed || {};

/* wraps the lesson's own checkFillIn */
function spkHintWrap(_orig, scopeOf) { return function (arg) {
  var scope = scopeOf(arg) || document;
  var inputs = [].slice.call(scope.querySelectorAll('.fillin-input'));
  var anyWrong = false, stuck = false;

  /* an answer with a curly apostrophe (isn’t) can never be typed on a
     plain keyboard, which gives a straight one (isn't). Match the
     student's apostrophes to the answer's before anything compares. */
  inputs.forEach(function (inp) {
    if (inp.disabled) return;
    var ans = inp.getAttribute('data-answer') || '';
    if (ans.indexOf('\u2019') >= 0) inp.value = inp.value.replace(/['\u2018`\u00B4]/g, '\u2019');
    else if (ans.indexOf("'") >= 0) inp.value = inp.value.replace(/[\u2018\u2019`\u00B4]/g, "'");
  });
  inputs.forEach(function (inp) {
    if (inp.disabled) return;
    var answer = (inp.getAttribute('data-answer') || '').toLowerCase();
    var val = inp.value.trim().toLowerCase();
    var cfg = (DATA.hints || {})[inp.id];
    var slot = cfg ? hintSlot(inp) : null;
    if (val === answer) { if (slot) slot.remove(); return; }
    anyWrong = true;
    /* An empty box is not a wrong try — the ladder only advances on
       an attempt, so tapping Check early never spends a student's hints. */
    if (val === '') { if (slot) slot.remove(); return; }
    if (!cfg) return;
    var n = bumpHint(inp.id);
    if (n === 1) { slot.className = 'spk-hint'; slot.innerHTML = cfg.h1; }
    else if (n === 2) {
      slot.className = 'spk-hint';
      slot.innerHTML = cfg.h1 + '<br><span class="spk-blanks">' + blanks(answer) + '</span>';
    } else {
      slot.className = 'spk-hint reveal';
      slot.innerHTML = '<b>' + answer + '</b> — ' + cfg.why;
      inp.value = answer; inp.disabled = true;
      inp.classList.add('spk-revealed'); inp.classList.remove('wrong', 'correct');
      window._spkRevealed[inp.id] = true;
      stuck = true;
    }
  });

  var r = _orig ? _orig.apply(this, arguments) : undefined;
  /* re-apply the revealed look the original may have cleared */
  inputs.forEach(function (inp) {
    if (window._spkRevealed[inp.id]) { inp.classList.add('spk-revealed'); inp.classList.remove('correct'); }
  });
  if (stuck) owlSay(OWL.stuck);
  else if (!anyWrong) owlCorrect();
  return r;
}; }
function _spkGame(btn) { return (btn && btn.closest) ? btn.closest('.fillin-game') : null; }
if (typeof window.checkFillIn === 'function')   window.checkFillIn   = spkHintWrap(window.checkFillIn, _spkGame);
if (typeof window.checkMorphFill === 'function') window.checkMorphFill = spkHintWrap(window.checkMorphFill, _spkGame);
if (typeof window.gramFillCheck === 'function')  window.gramFillCheck  = spkHintWrap(window.gramFillCheck, function (id) { return document.getElementById(id); });
if (typeof window.checkVocabCloze === 'function') window.checkVocabCloze = spkHintWrap(window.checkVocabCloze, function () { var i = document.querySelector('[id^="vcloze"]'); return i ? i.closest('.activity') : null; });

/* match-game distractor lines */
function missLine(host, text) {
  if (!text) return;
  var slot = host.querySelector('.spk-miss');
  if (!slot) { slot = document.createElement('div'); slot.className = 'spk-miss'; host.appendChild(slot); }
  slot.textContent = text;
  slot.style.animation = 'none'; void slot.offsetWidth; slot.style.animation = '';
  clearTimeout(slot._t);
  slot._t = setTimeout(function () { if (slot.parentNode) slot.parentNode.removeChild(slot); }, 4200);
}

var _origMatchClick = window.matchClick;
window.matchClick = function (item) {
  var grid = item.closest('.match-grid');
  var before = grid ? grid.querySelectorAll('.match-item.matched').length : 0;
  var sel = grid ? grid.querySelector('.match-item.selected') : null;
  var r = _origMatchClick.apply(this, arguments);
  if (!grid) return r;
  var after = grid.querySelectorAll('.match-item.matched').length;
  if (after > before) { owlCorrect(); return r; }
  if (sel && sel !== item) {
    var wordEl = sel.classList.contains('is-word') ? sel : (item.classList.contains('is-word') ? item : null);
    if (wordEl) missLine(grid.parentNode, ((DATA.miss || {}).match || {})[wordEl.textContent.trim()]);
  }
  return r;
};

var _origDrop = window.dropSortChip;
window.dropSortChip = function (colDrop, colName) {
  var g = colDrop.closest('.sort-game');
  var sel = g ? g._oaoSel : null;
  var wrong = sel && sel.getAttribute('data-group') !== colName;
  var label = sel ? sel.textContent.trim() : '';
  var r = _origDrop.apply(this, arguments);
  if (wrong) { missLine(g, ((DATA.miss || {}).sort || {})[label]); bumpHint('sort'); }
  else if (sel) { owlCorrect(); }
  return r;
};

/* ══════════════════════════════════════════════════════════════
   §2.8b  WORD GAMES — one word-study strand gets a themed game.
   Modeled on the G4 social studies vocabulary games: the theme
   acts out the word part's meaning, a "why" card explains the
   theme first, every success moves and makes a quiet sound, a
   wrong try bounces back with a hint, and finishing looks finished.

   DATA.wordgame = { type:'bridge', strand:'Morphology', kicker, h,
     voice, why:{icon,q,t}, win, winDay, spans,
     meanings:{ trans:'across', pro:'forward' }, miss:{ fill1:'…' } }

   The WORDS come from the strand's own fill-in game on the page
   (data-answer = the word part; item text = stem — meaning), so
   DATA carries only the theme and the page stays the one source of
   truth. The fill-in stays underneath: finishing the game fills it
   and runs its own check, so progress, gathered work and the
   layer-off page all behave exactly as before.
   Word clips (narrator): assets/audio/guide/narrator/
     g3ela-<w>-<d>-word-<n>.mp3 — requested only on a tap, silent
   when the file is not there yet.
   ══════════════════════════════════════════════════════════════ */
var WORDGAME = {};
function wgActivity(strand) {
  var want = String(strand || 'Morphology').toLowerCase();
  var acts = document.querySelectorAll('#tab-words .activity');
  for (var i = 0; i < acts.length; i++) {
    var t = acts[i].querySelector('.activity-title');
    if (t && t.textContent.toLowerCase().indexOf(want) >= 0) return acts[i];
  }
  return null;
}
function wgWords(game) {
  return [].slice.call(game.querySelectorAll('.fillin-item')).map(function (item) {
    var inp = item.querySelector('.fillin-input');
    var txt = item.textContent.replace(/\s+/g, ' ').trim();
    var parts = txt.split(/\s+[—–-]\s+/);
    return { id: inp ? inp.id : '', a: inp ? (inp.getAttribute('data-answer') || '').toLowerCase() : '',
             stem: (parts[0] || '').trim(), m: parts.slice(1).join(' — ').trim(), inp: inp };
  }).filter(function (w) { return w.inp && w.a && w.stem; });
}
var _wgAC = null;
function wgSfx(kind) {
  try {
    _wgAC = _wgAC || new (window.AudioContext || window.webkitAudioContext)();
    if (_wgAC.state === 'suspended') _wgAC.resume();
    var t = _wgAC.currentTime;
    var tone = function (f, f2, dur, vol, type, at) {
      var o = _wgAC.createOscillator(), g = _wgAC.createGain(); at = t + (at || 0);
      o.type = type || 'sine'; o.frequency.setValueAtTime(f, at);
      if (f2) o.frequency.exponentialRampToValueAtTime(f2, at + dur);
      g.gain.setValueAtTime(0.0001, at); g.gain.exponentialRampToValueAtTime(vol, at + 0.01);
      g.gain.exponentialRampToValueAtTime(0.0001, at + dur);
      o.connect(g); g.connect(_wgAC.destination); o.start(at); o.stop(at + dur + 0.05);
    };
    if (kind === 'thud') {                     /* a plank landing on the beams */
      tone(140, 70, 0.22, 0.18, 'sine');
      var len = Math.floor(_wgAC.sampleRate * 0.08), buf = _wgAC.createBuffer(1, len, _wgAC.sampleRate), d = buf.getChannelData(0);
      for (var i = 0; i < len; i++) d[i] = (Math.random() * 2 - 1) * Math.pow(1 - i / len, 3);
      var n = _wgAC.createBufferSource(), lp = _wgAC.createBiquadFilter(), ng = _wgAC.createGain();
      lp.type = 'lowpass'; lp.frequency.value = 900; ng.gain.value = 0.12;
      n.buffer = buf; n.connect(lp); lp.connect(ng); ng.connect(_wgAC.destination); n.start(t);
    } else if (kind === 'bonk') {              /* a gentle no */
      tone(220, 180, 0.16, 0.06, 'triangle');
    } else if (kind === 'chime') {             /* a star coming out */
      [1568, 2093].forEach(function (f, k) { tone(f, 0, 0.7, 0.05, 'sine', k * 0.07); });
    } else if (kind === 'win') {               /* across */
      [523, 659, 784].forEach(function (f, k) { tone(f, 0, 0.9, 0.08, 'sine', k * 0.16); });
    }
  } catch (e) {}
}
var _wgClip = null;
function wgClip(n) {
  try {
    if (_wgClip) _wgClip.pause();
    var a = new Audio(MEDIA.audioBase + 'guide/opti/g3ela-' + LESSON.week + '-' + dayNum(LESSON.day) + '-word-' + n + '.mp3');
    _wgClip = a; if (typeof audioStopAll === 'function') audioStopAll(a);
    var p = a.play(); if (p && p.catch) p.catch(function () {});
  } catch (e) {}
}
function wgWhy(why) {
  if (!why || !why.t) return '';
  return '<div class="spk-wg-why"><span class="i">' + (why.icon || '💡') + '</span><div><b>' + esc(why.q || '') + '</b>' +
         '<p>' + why.t + '</p></div></div>';
}

function buildWordGame() {
  var cfg = DATA.wordgame;
  if (!cfg || !WORDGAME[cfg.type]) return;              /* no themed game for this lesson */
  if (cfg.type === 'tower') { WORDGAME.tower(cfg); return; }   /* G3: self-contained, not built from a page game */
  var act = wgActivity(cfg.strand); if (!act) return;
  var game = act.querySelector('.fillin-game'); if (!game) return;
  var W = wgWords(game); if (W.length < 2) return;
  WORDGAME[cfg.type](cfg, act, game, W);
}

/* ══════════════════════════════════════════════════════════════
   §2.8  COPIA
   ══════════════════════════════════════════════════════════════ */
function buildCopia() {
  if (!DATA.copia || !DATA.copia.seed) return;           /* no copia seed for this lesson */
  var panel = document.getElementById('tab-words'); if (!panel) return;
  var anchor = panel.querySelector('.tab-next-wrap'); if (!anchor) return;
  var card = document.createElement('div');
  card.className = 'spk-card spk-copia-card';
  var slots = [
    ['Change the opener', 'Start with a when or a where.'],
    ['Swap the verb', 'Find a stronger word than the one in bold.'],
    ['Add a where or a how', 'Tell us where it happened, or how it was done.']
  ];
  var html =
    '<div class="spk-card-head"><div class="spk-card-num">✎</div><div>' +
    '<div class="spk-card-title">Copia · Say It Three Ways</div>' +
    '<div class="spk-card-sub">Long ago, a teacher named Erasmus had his students rewrite one sentence a hundred ways. You only need three.</div>' +
    '</div></div><div class="spk-card-body">' +
    '<p style="font-size:15px;color:#3A4A6B;">Here is one sentence about this week’s reading. There is no wrong answer here — only more ways to say it.</p>' +
    lookCard(DATA.copia.look, DATA.copia.todo) +
    '<div class="spk-copia-seed">' + DATA.copia.seed + '</div>';
  slots.forEach(function (s, i) {
    var id = 'journal-copia' + (i + 1);
    html += '<div class="spk-copia-slot">' +
      '<div class="spk-copia-slot-label">' + (i + 1) + '. ' + s[0] + '</div>' +
      '<div class="spk-copia-slot-hint">' + s[1] + '</div>' +
      '<textarea class="journal-box" id="' + id + '" data-label="Copia ' + (i + 1) + ': ' + s[0] + '" ' +
      'placeholder="Write your way here…" style="min-height:64px;"></textarea>' +
      '<button type="button" class="spk-mini-btn" data-eg="' + i + '">Show one way</button>' +
      '</div>';
  });
  html += '</div>';
  card.innerHTML = html;
  anchor.parentNode.insertBefore(card, anchor);

  card.querySelectorAll('textarea.journal-box').forEach(function (ta) {
    try { var v = localStorage.getItem(window._lessonKey + '-' + ta.id); if (v) ta.value = v; } catch (e) {}
    ta.addEventListener('input', function () {
      try { localStorage.setItem(window._lessonKey + '-' + ta.id, ta.value); } catch (e) {}
      if (window.gatherAnswers) window.gatherAnswers();
    });
  });
  card.querySelectorAll('.spk-mini-btn').forEach(function (b) {
    b.onclick = function () {
      var i = +b.getAttribute('data-eg');
      if (b.nextElementSibling && b.nextElementSibling.classList.contains('spk-copia-eg')) return;
      var eg = document.createElement('div');
      eg.className = 'spk-copia-eg';
      /* the examples carry one <i> around the swapped word. textContent
         printed the tag itself; building the node keeps the markup as
         markup without ever handing a string to innerHTML. */
      eg.appendChild(document.createTextNode('“'));
      DATA.copia.eg[i].split(/<i>|<\/i>/).forEach(function (part, n) {
        if (!part) return;
        if (n % 2) { var em = document.createElement('i'); em.textContent = part; eg.appendChild(em); }
        else eg.appendChild(document.createTextNode(part));
      });
      eg.appendChild(document.createTextNode('”'));
      b.parentNode.insertBefore(eg, b.nextSibling);
      b.textContent = 'One way, shown';
      b.disabled = true; b.style.opacity = '.6';
    };
  });
}

/* ══════════════════════════════════════════════════════════════
   §2.9  MEMORY-WORK FADE LADDER
   ══════════════════════════════════════════════════════════════ */
function memState() {
  var m = Sparkle.get('oao.g3ela.memory', {});
  if (!m[LESSON.book]) m[LESSON.book] = { rung: 1, advancedOn: null };
  return m;
}
function rungFor(week) { return Math.max(1, Math.min(8, week - 6)); }

/* which word indices are hidden at a given rung */
function fadeMask(lineWords, lineIdx, rung) {
  var n = lineWords.length, hide = {};
  function last(k) { for (var i = Math.max(0, n - k); i < n; i++) hide[i] = 1; }
  if (rung >= 2) last(1);
  if (rung >= 3 && lineIdx % 2 === 1) last(2);
  if (rung >= 4) last(2);
  if (rung >= 5 && lineIdx % 2 === 0) last(3);
  if (rung >= 6) last(Math.ceil(n / 2));
  if (rung >= 7) for (var i = 1; i < n; i++) hide[i] = 1;
  if (rung >= 8) for (var j = 0; j < n; j++) hide[j] = 1;
  return hide;
}

/* ══════════════════════════════════════════════════════════════
   §2.11  RECORDED VOICE

   Every recording is declared in the slot table below and keyed per
   lesson. There is no poem clip here: the By Heart card and its
   reading belong to assets/js/oao-sparkle.js.

   Nothing is per-lesson in the code: drop the file in the right folder
   under the naming rule and the control appears. Take it away and the
   control disappears. There is never a dead button, because the
   control starts hidden and only shows once the browser has the file's
   metadata in hand.
   ══════════════════════════════════════════════════════════════ */
/* ══════════════════════════════════════════════════════════════
   §2.12  THE MEDIA SLOT TABLE

   Every recording on the page — the welcome, the three guiding-voice
   clips, the poem, and any strand section you want to add one to — is
   ONE ROW in the table below. A row says where it mounts, what it is
   called, and what kind of thing it is:

     kind: ''          the slot is off. Nothing renders, nothing is
                       fetched. This is the default.
     kind: 'audio'     an .mp3 from assets/audio/
     kind: 'video'     an .mp4 from assets/video/
     kind: 'youtube'   an embedded YouTube player; needs `yt`

   Switching a slot between voice and film is a one-word edit in this
   table. Adding a recording to a section that has never had one is a
   row. No lesson HTML changes for either.

   THE ONE ASYMMETRY, and it matters:

     audio and video are hidden until the browser confirms the file is
     really there, so a missing recording is invisible — exactly like a
     missing chapter plate.

     A YouTube embed cannot be checked from the page. The iframe is a
     sealed box: if the id is wrong, private, deleted or blocked, it
     shows YouTube's own error inside the frame and the page has no way
     to know. So for 'youtube' the manifest IS the check — a row with
     no `yt` renders nothing, and a row with a bad `yt` renders a
     broken player rather than silence. Validate ids at build time.
   ══════════════════════════════════════════════════════════════ */

var MEDIA = {
  audioBase: 'assets/audio/',
  videoBase: 'assets/video/',
  /* youtube-nocookie: no cookie is written until the viewer presses
     play. For a K-5 course this is the host to use, not youtube.com. */
  ytBase: 'https://www.youtube-nocookie.com/embed/',

  slots: [
    /* ---- the guiding voice: on today ---- */
    { id:'welcome', kind:'audio', at:{greeting:true},
      path:'guide/opti/g3ela-{w}-{d}-welcome',
      label:'Opti’s welcome' },

    { id:'guide1',  kind:'audio', at:{tab:'words'},
      path:'guide/opti/g3ela-{w}-{d}-1',
      label:'Opti · before the word work' },

    { id:'guide2',  kind:'audio', at:{tab:'reading'},
      path:'guide/opti/g3ela-{w}-{d}-2',
      label:'Opti · before you open the book' },

    { id:'guide3',  kind:'audio', at:{tab:'assignment'},
      path:'guide/opti/g3ela-{w}-{d}-3',
      label:'Opti · before you write' },


    /* ---- the sections: every one, all off until you give it a kind ----
       `section` matches the text of an .activity-title, so a clip lands
       at the head of that activity wherever it sits on the page. The
       count after each is how many of the 129 lessons have it; where a
       lesson does not, the slot simply does not render.

       Turning one on means a script for it in that lesson's script doc.
       All seventeen on, every day, would be 2,193 recordings for the
       year and far too many voices for a nine-year-old — these exist so
       you can choose the few that earn it, not so they all get used. */
    { id:'wgrd',       kind:'', at:{section:/what good readers do/i},   /* 127 */
      path:'guide/wgrd/g3ela-{w}-{d}',     label:'About today’s reading move' },
    { id:'dol',        kind:'', at:{section:/daily oral/i},             /* 127 */
      path:'guide/dol/g3ela-{w}-{d}',      label:'About today’s sentence' },
    { id:'vocabulary', kind:'', at:{section:/vocabular/i},              /* 126 */
      path:'guide/vocab/g3ela-{w}-{d}',    label:'About today’s words' },
    { id:'grammar',    kind:'', at:{section:/grammar/i},                /* 127 */
      path:'guide/grammar/g3ela-{w}-{d}',  label:'About today’s grammar' },
    { id:'morphology', kind:'', at:{section:/morpholog/i},              /* 127 */
      path:'guide/morph/g3ela-{w}-{d}',    label:'About today’s word parts' },
    { id:'spelling',   kind:'', at:{section:/spelling/i},               /* 125 */
      path:'guide/spelling/g3ela-{w}-{d}', label:'About today’s spelling' },
    { id:'workshop',   kind:'', at:{section:/writer.s workshop/i},      /* 100 */
      path:'guide/workshop/g3ela-{w}-{d}', label:'About today’s writing' },
    { id:'chapter',    kind:'', at:{section:/chapter thinking/i},       /* 100 */
      path:'guide/chapter/g3ela-{w}-{d}',  label:'About today’s chapter' },
    { id:'read',       kind:'', at:{section:/open your (book|sources)|^[\W_]*read\b/i}, /* 103 */
      path:'guide/read/g3ela-{w}-{d}',     label:'Before you read' },
    { id:'poetry',     kind:'', at:{section:/poetry corner/i},          /* 63 */
      path:'guide/poetry/g3ela-{w}-{d}',   label:'About the poem' },
    { id:'wordconn',   kind:'', at:{section:/word study connection/i},  /* 98 */
      path:'guide/wordconn/g3ela-{w}-{d}', label:'How this connects' },
    { id:'copywork',   kind:'', at:{section:/copywork/i},               /* 18 */
      path:'guide/copywork/g3ela-{w}-{d}', label:'About today’s copywork' },
    { id:'shelf',      kind:'', at:{section:/your reading shelf/i},     /* 5 */
      path:'guide/shelf/g3ela-{w}-{d}',    label:'About your shelf' },
    /* RWM is not an .activity: it is a .rwm-box inside the Reading tab,
       so it mounts by selector, just under its header. On by default:
       its clip and its video each stay hidden until the file exists. */
    { id:'rwm',        kind:'', at:{sel:'.rwm-box'},               /* 48 */
      path:'guide/rwm/g3ela-{w}-{d}',      label:'About Read like a Writer' },
    /* Copia is built by this layer (buildCopia runs before buildMedia),
       so it mounts under the card's own heading. On by default, like RWM. */
    { id:'copia',      kind:'', at:{sel:'.spk-copia-card'},
      path:'guide/copia/g3ela-{w}-{d}',    label:'About Say It Three Ways' }
  ]
};
window.OAO_MEDIA = MEDIA;
/* test hook: the media functions, for the headless sweep */
window.OAO_MEDIA_FNS = null;

/* A per-lesson override, set from the lesson's DATA block. Lets one
   lesson use film where the rest of the year uses voice, without
   touching the table above:
     DATA.media = { guide2:{kind:'youtube', yt:'dQw4w9WgXcQ'} }            */
function mediaSlots() {
  var over = (typeof DATA === 'object' && DATA && DATA.media) || {};
  return MEDIA.slots.map(function (s) {
    var o = over[s.id]; if (!o) return s;
    var m = {}; for (var k in s) m[k] = s[k];
    for (var k2 in o) m[k2] = o[k2];
    return m;
  });
}

function mediaPath(slot) {
  return String(slot.path || '')
    .replace('{w}', LESSON.week)
    .replace('{d}', dayNum(LESSON.day));
  /* there is no {poem} token: the poem card and its clip belong to
     assets/js/oao-sparkle.js, not to this layer. */
}
function mediaSrc(slot) {
  var p = mediaPath(slot); if (!p) return '';
  if (slot.src) return slot.src;                  /* explicit wins */
  if (slot.kind === 'audio') return MEDIA.audioBase + p + '.mp3';
  if (slot.kind === 'video') return MEDIA.videoBase + p + '.mp4';
  return '';
}

var GUIDE_NOTE = null;   /* what the Watch block used to say */

/* one clip plays at a time, and starting one silences the page's
   text-to-speech reader — two voices at once is the worst outcome */
var _nowPlaying = null;
function audioStopAll(except) {
  if (_nowPlaying && _nowPlaying !== except) { try { _nowPlaying.pause(); } catch (e) {} }
  try { if (window.speechSynthesis) window.speechSynthesis.cancel(); } catch (e) {}
}
function mmss(t) {
  if (!isFinite(t)) return '';
  var m = Math.floor(t / 60), s = Math.floor(t % 60);
  return m + ':' + (s < 10 ? '0' : '') + s;
}

  /* ═══ Spotlight: page parts light up, pop, point and reveal exactly when the recorded voice names them (PowerPoint-style).
   Ported from the G4 Science Field Station layer (fs-sparkle.js cueRunner), 22 Oct 2026.
   DATA.cues     = { <clip id>: [ {at: 'regex for the spoken word (first match after the previous cue)', sel: 'CSS selector',
                                   i: n (n-th match) | all: true, fx: 'glow'|'pop'|'wiggle'|'point'|'trace'|'reveal', tag: 'short label', scroll: true} ] }
   DATA.cueWords = { <clip id>: [[start, end, 'word'], …] }  (from an ElevenLabs Scribe transcript of the clip; without it the times are estimated)
   spotlight(id, script, audio) wires one <audio>/Audio object. Nothing happens for a clip with no cues. ═══ */
function spotlight(id, script, audio) {
  var D_ = (typeof DATA === 'object' && DATA) || {};
  var C = (D_.cues || {})[id]; if (!C || !C.length || !audio) return;
  var RM = false; try { RM = window.matchMedia('(prefers-reduced-motion: reduce)').matches; } catch (e) {}
  var toks = String(script || '').split(/\s+/).filter(Boolean), from = 0, beats = [];
  function clean(t) { return String(t).replace(/^[^\w’']+|[^\w’']+$/g, ''); }
  C.forEach(function (c) {
    var re = new RegExp(c.at, 'i'), k = from;
    while (k < toks.length && !re.test(clean(toks[k]))) k++;
    if (k >= toks.length) { try { console.warn('spotlight: cue "' + c.at + '" is not in the ' + id + ' script'); } catch (e) {} return; }
    beats.push({ c: c, k: k }); from = k + 1;
  });
  var W = (D_.cueWords || {})[id];
  if (W && W.length) { var wf = 0; beats.forEach(function (b) { var re = new RegExp(b.c.at, 'i'), j = wf; while (j < W.length && !re.test(clean(W[j][2]))) j++; if (j < W.length) { b.t = W[j][0]; wf = j + 1; } }); }
  function est(k, dur) {
    var wt = function (t) { return t.length + 2 + (/[.!?]$/.test(t) ? 7 : /[,;:]$/.test(t) ? 3 : 0); };
    var tot = toks.reduce(function (n, t) { return n + wt(t); }, 0), before = 0;
    for (var i = 0; i < k; i++) before += wt(toks[i]);
    return Math.max(0, before / (tot || 1) * (dur || 30) - 0.15);
  }
  var fired = -1, live = [], raf = 0, clr = 0;
  function els(c) { var a = [].slice.call(document.querySelectorAll(c.sel)); if (c.i != null) return a[c.i] ? [a[c.i]] : []; return c.all ? a : a.slice(0, 1); }
  function clearNow() { live.forEach(function (e) { e.classList.remove('spk-cue-now', 'spk-cue-pop', 'spk-cue-wiggle', 'spk-cue-point', 'spk-cue-trace'); var t = e.querySelector(':scope > .spk-cue-tag'); if (t) t.remove(); }); live = []; }
  function fire(i) {
    var b = beats[i]; if (!b) return; clearNow();
    els(b.c).forEach(function (e) {
      e.classList.remove('spk-cue-wait'); e.classList.add('spk-cue-lit', 'spk-cue-now');
      var fx = b.c.fx || 'glow'; if (fx !== 'glow' && fx !== 'reveal' && !RM) { void e.offsetWidth; e.classList.add('spk-cue-' + fx); }
      if ((b.c.tag || fx === 'point') && getComputedStyle(e).position === 'static') e.classList.add('spk-cue-rel');
      if (b.c.tag) { var t = document.createElement('span'); t.className = 'spk-cue-tag'; t.setAttribute('aria-hidden', 'true'); t.textContent = b.c.tag; e.appendChild(t); }
      if (b.c.scroll) { var r = e.getBoundingClientRect(); if (r.bottom < 60 || r.top > innerHeight - 60) e.scrollIntoView({ block: 'center', behavior: RM ? 'auto' : 'smooth' }); }
      live.push(e);
    });
  }
  function at(t, dur) { var n = -1; beats.forEach(function (b, i) { if (t >= (b.t != null ? b.t - 0.1 : est(b.k, dur))) n = i; }); while (fired < n) { fired++; fire(fired); } }
  function tick() { if (audio.paused) return; at(audio.currentTime, audio.duration); raf = requestAnimationFrame(tick); }
  audio.addEventListener('play', function () {
    clearTimeout(clr); if (audio.currentTime < 0.3) { fired = -1; clearNow(); }
    beats.forEach(function (b) { if ((b.c.fx || '') === 'reveal') els(b.c).forEach(function (e) { if (!e.classList.contains('spk-cue-lit')) e.classList.add('spk-cue-wait'); }); });
    document.documentElement.classList.add('spk-cueing'); cancelAnimationFrame(raf); raf = requestAnimationFrame(tick);
  });
  audio.addEventListener('timeupdate', function () { if (!audio.paused) at(audio.currentTime, audio.duration); });
  function end(done) { cancelAnimationFrame(raf); document.documentElement.classList.remove('spk-cueing');
    [].forEach.call(document.querySelectorAll('.spk-cue-wait'), function (e) { e.classList.remove('spk-cue-wait'); });
    clr = setTimeout(clearNow, done ? 1600 : 0); if (done) fired = -1; }
  audio.addEventListener('pause', function () { if (!audio.ended) end(false); });
  audio.addEventListener('ended', function () { end(true); });
}

/* Built hidden, revealed only once the file is known to exist.
   A missing recording is silent in both senses. */
function audioControl(label, src) {
  if (!src) return null;
  var wrap = document.createElement('div');
  wrap.className = 'spk-audio';
  wrap.hidden = true;
  wrap.innerHTML =
    '<button type="button" class="spk-audio-btn">' +
      '<span class="spk-audio-ico" aria-hidden="true"></span>' +
      '<span class="spk-audio-label"></span>' +
    '</button>' +
    '<span class="spk-audio-bar"><i></i></span>' +
    '<span class="spk-audio-time"></span>';

  var btn  = wrap.querySelector('.spk-audio-btn');
  var lab  = wrap.querySelector('.spk-audio-label');
  var fill = wrap.querySelector('.spk-audio-bar i');
  var time = wrap.querySelector('.spk-audio-time');
  lab.textContent = label;
  btn.setAttribute('aria-label', label);

  var a = new Audio();
  a.preload = 'metadata';
  a.src = src;
  wrap._spkAudio = a;

  a.addEventListener('loadedmetadata', function () {
    wrap.hidden = false;                       /* the file is really there */
    time.textContent = mmss(a.duration);
  });
  a.addEventListener('error', function () { wrap.remove(); });
  a.addEventListener('timeupdate', function () {
    if (a.duration) fill.style.width = (a.currentTime / a.duration * 100) + '%';
  });
  a.addEventListener('ended', function () {
    wrap.classList.remove('playing'); btn.setAttribute('aria-pressed', 'false');
    fill.style.width = '0%'; time.textContent = mmss(a.duration); _nowPlaying = null;
  });
  a.addEventListener('pause', function () {
    wrap.classList.remove('playing'); btn.setAttribute('aria-pressed', 'false');
  });
  a.addEventListener('play', function () {
    wrap.classList.add('playing'); btn.setAttribute('aria-pressed', 'true');
  });

  btn.setAttribute('aria-pressed', 'false');
  btn.onclick = function () {
    if (a.paused) { audioStopAll(a); _nowPlaying = a; a.play().catch(function () {}); }
    else { a.pause(); }
  };
  wrap._audio = a;
  return wrap;
}

/* A film served from the repo. Same contract as the audio control:
   built hidden, revealed only once the browser confirms it can decode
   the file, removed if it cannot. That check is what catches an
   unplayable profile — the page shows nothing rather than a black box.

   Encode browser-safe or it will not play at all:
     H.264 High profile, yuv420p, AAC audio, +faststart.
   High 4:4:4 Predictive / yuv444p — what several AI video tools emit
   by default — has no decoder in any mainstream browser. */
function videoControl(label, src) {
  if (!src) return null;
  var fig = document.createElement('figure');
  fig.className = 'spk-media';
  fig.hidden = true;

  var v = document.createElement('video');
  v.className = 'spk-media-video';
  v.controls = true;
  v.playsInline = true;
  v.setAttribute('playsinline', '');
  v.preload = 'metadata';
  v.setAttribute('aria-label', label);

  var srcEl = document.createElement('source');
  srcEl.src = src;
  srcEl.type = /\.webm(\?|$)/i.test(src) ? 'video/webm' : 'video/mp4';
  v.appendChild(srcEl);

  var settled = false;
  v.addEventListener('loadedmetadata', function () {
    settled = true;
    fig.hidden = false;
    var poster = src.replace(/\.(mp4|webm)(\?|$)/i, '.jpg$2');
    if (poster !== src) v.poster = poster;
    if (v.videoWidth && v.videoHeight) {
      fig.style.setProperty('--spk-ar', v.videoWidth + ' / ' + v.videoHeight);
      if (v.videoHeight > v.videoWidth) fig.classList.add('spk-media-tall');
    }
  });
  var fail = function () {
    if (settled) return;
    settled = true;
    fig.remove();                  /* no film, or one no browser can play */
  };
  v.addEventListener('error', fail);
  srcEl.addEventListener('error', fail);
  v.addEventListener('play', function () { audioStopAll(v); _nowPlaying = v; });

  /* No caption: the films are of the teacher, not the character the
     slot label names, and the label repeats the audio button above. */
  fig.appendChild(v);
  addCaptions(v, src);
  addQuestions(v, src, label);
  return fig;
}

/* Closed captions. A film with a .vtt of the same name beside it
   (g3ela-15-2-read.mp4 + g3ela-15-2-read.vtt, as the Video Studio saves
   them) gets them as a track. The player then shows its CC button.
   Captions start OFF; a student turns them on with CC. A film with no
   .vtt is left exactly as it was: the file is checked first, so no CC
   button appears for nothing. */
function addCaptions(v, src) {
  if (!v || v.getAttribute('data-spk-cc')) return;
  v.setAttribute('data-spk-cc', '1');
  if (!src) {
    var s0 = v.querySelector('source');
    src = v.currentSrc || v.getAttribute('src') || (s0 && s0.getAttribute('src')) || '';
  }
  var vtt = String(src).replace(/\.(mp4|webm)(\?.*)?$/i, '.vtt');
  if (!vtt || vtt === src || !window.fetch || v.querySelector('track')) return;
  fetch(vtt, { method: 'HEAD', cache: 'no-cache' }).then(function (r) {
    if (!r.ok) return;
    var t = document.createElement('track');
    t.kind = 'captions';
    t.srclang = 'en';
    t.label = 'English';
    t.src = vtt;                 /* no `default`: off until CC is pressed */
    v.appendChild(t);
    if (t.track) t.track.mode = 'disabled';
    ccButton(v, t);
  }).catch(function () {});
}

/* a big, plain Captions button under every teacher video that has a
   .vtt (the Video Studio saves one). Off by default; a student's choice
   is remembered for every video on every lesson. */
function capsOn() { try { return localStorage.getItem('oao.g3ela.captions') === '1'; } catch (e) { return false; } }
function ccButton(v, t) {
  if (v.getAttribute('data-spk-ccb')) return;
  v.setAttribute('data-spk-ccb', '1');
  var b = document.createElement('button');
  b.type = 'button'; b.className = 'spk-cc';
  b.innerHTML = '<span class="spk-cc-i">CC</span> <span class="spk-cc-t">Captions: off</span>';
  function apply(on) {
    if (t.track) t.track.mode = on ? 'showing' : 'hidden';
    b.classList.toggle('on', on); b.setAttribute('aria-pressed', on ? 'true' : 'false');
    b.querySelector('.spk-cc-t').textContent = on ? 'Captions: on' : 'Captions: off';
  }
  b.__set = apply;
  b.addEventListener('click', function () {
    var on = !b.classList.contains('on');
    try { localStorage.setItem('oao.g3ela.captions', on ? '1' : '0'); } catch (e) {}
    document.querySelectorAll('.spk-cc').forEach(function (x) { if (x.__set) x.__set(on); });
  });
  t.addEventListener('load', function () { apply(capsOn()); });
  v.parentNode.insertBefore(b, v.nextSibling);
  apply(capsOn());
}

function captionAllFilms() {
  var vs = document.querySelectorAll('video');
  for (var i = 0; i < vs.length; i++) { addCaptions(vs[i]); addQuestions(vs[i]); }
}

/* Stop-and-answer films. A film with a <name>.questions.json beside it
   (made in the Video Studio) stops at each question until the student
   answers; see assets/js/oao-video-questions.js, which is only loaded
   when a page has such a film. */
var _vqWaiting = null;
function addQuestions(v, src, label) {
  if (!v || v.getAttribute('data-spk-vq')) return;
  v.setAttribute('data-spk-vq', '1');
  if (!src) {
    var s0 = v.querySelector('source');
    src = v.getAttribute('src') || (s0 && s0.getAttribute('src')) || '';
  }
  var url = String(src).replace(/\.(mp4|webm)(\?.*)?$/i, '.questions.json');
  if (!src || url === src || !window.fetch) return;
  fetch(url, { cache: 'no-cache' }).then(function (r) { return r.ok ? r.json() : null; }).then(function (d) {
    if (!d || !d.questions || !d.questions.length) return;
    var go = function () { if (window.OAOVideoQ) window.OAOVideoQ.attach(v, d, src, label); };
    if (window.OAOVideoQ) { go(); return; }
    if (_vqWaiting) { _vqWaiting.push(go); return; }
    _vqWaiting = [go];
    var s = document.createElement('script');
    s.src = artURL('js/oao-video-questions.js');
    s.charset = 'utf-8';
    s.onload = function () { var w = _vqWaiting; _vqWaiting = []; w.forEach(function (f) { f(); }); };
    document.head.appendChild(s);
  }).catch(function () {});
}

/* A YouTube embed.

   Unlike the two above, this CANNOT be verified from the page — the
   iframe is cross-origin and silent about its own failures. So the
   only check is the one made here: no id, no element. A wrong id will
   render a player showing YouTube's error, which is why ids are
   checked when the lesson is built, not when it loads.

   The iframe is created lazily, on click, behind a still frame. That
   keeps YouTube from being contacted at all unless the student chooses
   to watch — which is both faster and the right default for children.
     rel=0        related videos limited to the same channel
     modestbranding=1  smaller YouTube wordmark
     playsinline=1     iOS plays in place instead of going fullscreen  */
function youtubeControl(label, id) {
  if (!id || !/^[A-Za-z0-9_-]{6,20}$/.test(id)) return null;

  var fig = document.createElement('figure');
  fig.className = 'spk-media spk-media-yt';

  var btn = document.createElement('button');
  btn.type = 'button';
  btn.className = 'spk-yt-poster';
  btn.setAttribute('aria-label', 'Play video: ' + label);
  var img = document.createElement('img');
  img.src = 'https://i.ytimg.com/vi/' + id + '/hqdefault.jpg';
  img.alt = '';
  img.loading = 'lazy';
  var play = document.createElement('span');
  play.className = 'spk-yt-play';
  play.setAttribute('aria-hidden', 'true');
  btn.appendChild(img); btn.appendChild(play);

  btn.onclick = function () {
    audioStopAll(null);
    var f = document.createElement('iframe');
    f.className = 'spk-media-video';
    f.src = MEDIA.ytBase + id +
      '?autoplay=1&rel=0&modestbranding=1&playsinline=1';
    f.title = label;
    f.allow = 'accelerometer; autoplay; encrypted-media; picture-in-picture';
    f.setAttribute('allowfullscreen', '');
    f.setAttribute('frameborder', '0');
    btn.replaceWith(f);
  };

  var cap = document.createElement('figcaption');
  cap.className = 'spk-media-cap';
  cap.textContent = label;
  fig.appendChild(btn); fig.appendChild(cap);
  return fig;
}

/* Build whichever element this slot's `kind` calls for. */
function mediaElement(slot) {
  if (slot.kind === 'audio')   { var ac = audioControl(slot.label, mediaSrc(slot)); if (ac && ac._audio) spotlight(slot.id, (DATA.transcripts || {})[slot.id], ac._audio); return ac; }
  if (slot.kind === 'video')   return videoControl(slot.label, mediaSrc(slot));
  if (slot.kind === 'youtube') return youtubeControl(slot.label, slot.yt);
  return null;                                     /* kind:'' — slot off */
}

/* Where a slot mounts. Three anchors, in the order they are tried. */
function mediaMount(slot) {
  var at = slot.at || {};
  if (at.greeting) {
    var say = document.getElementById('spkOpenSay');
    return say ? { host: say.parentNode, before: say.nextSibling } : null;
  }
  if (at.el) {
    var e = document.getElementById(at.el);
    return e ? { host: e.parentNode, before: e.nextSibling } : null;
  }
  if (at.sel) {
    var box = document.querySelector(at.sel); if (!box) return null;
    var top = box.firstElementChild;
    return { host: box, before: top ? top.nextSibling : box.firstChild };
  }
  if (at.tab) {
    var p = document.getElementById('tab-' + at.tab);
    return p ? { host: p, before: p.firstChild } : null;
  }
  if (at.section) {
    var titles = document.querySelectorAll('.activity-title');
    for (var i = 0; i < titles.length; i++) {
      if (at.section.test(titles[i].textContent || '')) {
        var head = titles[i].closest('.activity-head') ||
                   titles[i].closest('.activity');
        var act  = titles[i].closest('.activity');
        if (!act) return null;
        return { host: act, before: head && head.parentNode === act
                                    ? head.nextSibling : act.firstChild };
      }
    }
  }
  return null;
}

/* Flow fix (Oct 28 2026, parent feedback): who speaks a clip, read from its folder
   (assets/audio/guide/marilla/... -> "Marilla"). Generic slot folders
   (guide/read/, guide/turn/ ...) give no name. */
var _GENERIC = /^(opti|chapter|copia|copywork|dol|grammar|morph|poetry|read|rwm|shelf|spelling|turn|vocab|welcome|wgrd|wordconn|workshop)$/;
function speakerOf(slot) {
  var m = /(?:^|\/)guide\/([a-z-]+)\//.exec(mediaPath(slot) || slot.src || '');
  if (!m || _GENERIC.test(m[1])) return '';
  return m[1].charAt(0).toUpperCase() + m[1].slice(1);
}

function buildMedia() {
  /* Safe to call more than once. On a first visit the greeting does
     not exist at boot — it appears only after the student enters a
     name — so renderGreeting() calls this again, and each slot checks
     whether it has already been filled. */
  mediaSlots().forEach(function (slot) {
    if (!slot.kind) return;                        /* slot off */
    var m = mediaMount(slot); if (!m) return;      /* nowhere to put it */

    var scope = m.host;
    if (scope.querySelector('[data-spk-slot="' + slot.id + '"]')) return;

    var el = mediaElement(slot); if (!el) return;
    el.setAttribute('data-spk-slot', slot.id);
    if (slot.inline) el.classList.add('spk-audio-inline');
    if (slot.at && (slot.at.tab || slot.at.section)) el.classList.add('spk-guide');

    /* A section that plays audio may also carry a video. It is looked
       for at the same name under assets/video/ (…/g3ela-7-3-grammar.mp4
       beside …/g3ela-7-3-grammar.mp3) and, like the audio, stays hidden
       unless the file is really there. Both present: both show, audio
       first. DATA.media.<slot>.video:false switches the look-up off;
       videoSrc gives an explicit file. */
    var vid = null;
    if (slot.kind === 'audio' && slot.video !== false) {
      var vp = mediaPath(slot);
      vid = videoControl(slot.label, slot.videoSrc || (vp ? MEDIA.videoBase + vp + '.mp4' : ''));
      if (vid) {
        vid.setAttribute('data-spk-slot', slot.id + '-video');
        if (slot.at && (slot.at.tab || slot.at.section)) vid.classList.add('spk-guide');
      }
    }

    var wrap = el;
    /* "Read along": the clip's own script, folded under it. Words come
       from DATA.transcripts[slot.id] and appear only once the recording
       is confirmed, so a clip that has not been made shows nothing. */
    var words = (DATA.transcripts || {})[slot.id];
    var watch = slot.id === 'guide2' && GUIDE_NOTE && GUIDE_NOTE.text;
    if (words || watch || vid) {
      wrap = document.createElement('div');
      wrap.className = 'spk-guide-wrap';
      wrap.setAttribute('data-spk-slot', slot.id);
      wrap.appendChild(el);
      if (vid) wrap.appendChild(vid);
    }
    /* Flow fix (Oct 28 2026, parent feedback): audio and film together = two steps, in order.
       Labels go on only once the film really loads (a missing film is
       removed, and then the audio stays a plain single step). */
    if (vid) {
      var v0 = vid.querySelector('video');
      var stepUp = function () {
        /* Nov 3 2026: number the steps only when BOTH are really there.
           No recording yet = the film stands alone, no "②". */
        if (el.hidden || !el.isConnected || vid.hidden || !vid.isConnected) return;
        var lab = el.querySelector('.spk-audio-label');
        if (lab && lab.textContent.indexOf('\u2460') !== 0) lab.textContent = '\u2460 Listen first \u00b7 ' + lab.textContent;
        if (!vid.querySelector('.spk-step-label')) {
          var step2 = document.createElement('div');
          step2.className = 'spk-step-label';
          step2.textContent = '\u2461 Then watch your teacher';
          vid.insertBefore(step2, vid.firstChild);
        }
      };
      if (v0) v0.addEventListener('loadedmetadata', stepUp);
      if (window.MutationObserver) {
        var stObs = new MutationObserver(function () { if (!el.hidden) { stObs.disconnect(); stepUp(); } });
        stObs.observe(el, { attributes: true, attributeFilter: ['hidden'] });
      }
    }
    if (words) {
      var ra = document.createElement('details');
      ra.className = 'spk-note spk-readalong';
      ra.hidden = true;
      var raSum = document.createElement('summary');
      var whoRA = speakerOf(slot);
      raSum.textContent = '\ud83d\udcc4 Read ' + (whoRA ? whoRA + '\u2019s' : 'the') + ' words instead';
      ra.appendChild(raSum);
      var raBody = document.createElement('div');
      raBody.className = 'spk-note-body';
      raBody.textContent = words;                /* never innerHTML */
      ra.appendChild(raBody);
      wrap.appendChild(ra);
      /* shown only once the clip itself is confirmed (Nov 3 2026): these
         are the speaker's words, so a teacher film alone does not show them */
      var seen = [el];
      var anyShown = function () { return seen.some(function (x) { return !x.hidden; }); };
      if (slot.kind === 'youtube' || anyShown()) ra.hidden = false;
      else if (window.MutationObserver) {
        var raObs = new MutationObserver(function () {
          if (anyShown()) { ra.hidden = false; raObs.disconnect(); }
        });
        seen.forEach(function (x) { raObs.observe(x, { attributes: true, attributeFilter: ['hidden'] }); });
      }
    }
    /* the Reading clip carries what the Watch block used to say, so
       its words go underneath it, folded */
    if (watch) {
      var det = document.createElement('details');
      det.className = 'spk-note';
      var sum = document.createElement('summary');
      sum.textContent = 'Read it instead' +
        (GUIDE_NOTE.title ? ' · ' + titleCase(GUIDE_NOTE.title.toLowerCase()) : '');
      det.appendChild(sum);
      var body = document.createElement('div');
      body.className = 'spk-note-body';
      body.textContent = GUIDE_NOTE.text;        /* never innerHTML */
      det.appendChild(body);
      wrap.appendChild(det);
    }
    m.host.insertBefore(wrap, m.before || null);
  });
}

/* The thematic strand runs all year under a different name per book:
     Virtue Watch      wk 1-5    (Mrs. Frisby)
     Virtue Words      wk 6
     Growing-Up Watch  wk 7-14   (Anne)
     Courage Watch     wk 15-19  (Number the Stars)
     Freedom Watch     wk 20-24  (Freedom Train)
   and nothing after 24.1 — see claude/g4-virtue-strand-survey.md.
   Match the family, not one name, or four fifths of the year is
   missed.

   The block comes off the Reading tab — it was carrying too much, and
   this is the part a teacher would simply have said. Its words are not
   thrown away: they are lifted out first and folded under the Reading
   clip as a transcript, so a student with the sound off, or on a
   lesson whose recording has not been made yet, can still read them.
   Audio is never the only copy. */
function liftWatchBlock() {
  var titles = document.querySelectorAll('.activity-title');
  for (var i = 0; i < titles.length; i++) {
    if (/\b(virtue|growing-up|courage|freedom|belief|character)\s+(watch|words)\b/i.test(titles[i].textContent || '')) {
      var act = titles[i].closest('.activity'); if (!act) return;
      var raw = (titles[i].textContent || '').trim();
      var head = raw.indexOf(':') > -1 ? raw.split(':').slice(1).join(':').trim() : raw;
      var body = act.querySelector('.activity-body');
      GUIDE_NOTE = { title: head, text: body ? (body.innerText || body.textContent || '').trim() : '' };
      act.remove();
      return;
    }
  }
}

/* kept so older call sites keep working */
function buildAudio() { liftWatchBlock(); buildMedia(); }
window.OAO_MEDIA_FNS = { buildMedia: buildMedia, liftWatchBlock: liftWatchBlock, mediaSlots: mediaSlots, mediaSrc: mediaSrc, plateSrc: plateSrc };
function buildGuide() { buildMedia(); }


/* §2.9 memory work — REMOVED, deliberately.

   The "By Heart" card is NOT ours. `assets/js/oao-sparkle.js` already
   ships it — one poem per book, an eight-rung ladder, a little less to
   lean on each week — and 66 lesson files load it. This layer used to
   build a SECOND card with a different poem, which meant two By Heart
   cards on every day-2 and day-4 lesson.

   It went unnoticed because the demo was built on lesson 7.1, and days
   1 and 3 are exactly the lessons that do NOT load the shipped script:
   Poetry Corner lives on days 2 and 4. The empty space looked like a
   gap to fill. It was not.

   So: the shipped card is the poem system. Do not rebuild it here, and
   do not add a poem key to DATA. If poetry needs changing, it changes
   in assets/js/oao-sparkle.js, which is a conversation with Bethany,
   not an edit. */

/* ══════════════════════════════════════════════════════════════
   §2.10  ILLUMINATED PUBLISHING + MARGINALIA
   ══════════════════════════════════════════════════════════════ */
function dropCapSVG(letter) {
  return '<svg viewBox="0 0 62 62" width="62" height="62" aria-hidden="true">' +
    '<rect width="62" height="62" rx="3" fill="#0E1C42"/>' +
    '<rect x="3.5" y="3.5" width="55" height="55" rx="2" fill="none" stroke="#FFFDF7" stroke-width="1"/>' +
    '<path d="M8 54 q6 -10 2 -18 q8 5 9 -3 M54 8 q-6 10 -2 18 q-8 -5 -9 3" stroke="#C7922C" stroke-width="1.4" fill="none" stroke-linecap="round" opacity=".85"/>' +
    '<circle cx="10" cy="11" r="2" fill="#C7922C"/><circle cx="52" cy="51" r="2" fill="#C7922C"/>' +
    '<text x="31" y="45" font-size="38" text-anchor="middle" font-family="Lora,Georgia,serif" font-weight="700" fill="#C7922C">' +
    letter + '</text></svg>';
}

function renderIllumAuthor() {
  var by = document.querySelector('.spk-illum .spk-by'); if (!by) return;
  var p = profile();
  by.textContent = 'by ' + (p ? p.name : 'a fourth-grade writer') +
    ' · Optima Academy Online · ' + LESSON.bookTitle + ' unit';
}

function buildPublish() {
  var actions = document.querySelector('.gathered-actions'); if (!actions) return;
  var btn = document.createElement('button');
  btn.type = 'button';
  btn.className = 'gathered-btn'; btn.style.cssText = 'background:#C7922C;color:#fff;';
  btn.innerHTML = '✒️ Publish My Writing';
  actions.appendChild(btn);

  var page = document.createElement('div');
  page.className = 'spk-illum'; page.id = 'spkIllum'; page.style.display = 'none';
  page.innerHTML =
    '<h2 id="spkIllumTitle"></h2><div class="spk-by"></div>' +
    '<div class="spk-illum-seal" id="spkIllumSeal"></div>' +
    '<div class="spk-illum-body" id="spkIllumBody"></div>' +
    '<div class="spk-colophon" id="spkColophon"></div>';
  actions.parentNode.appendChild(page);
  renderIllumAuthor();

  btn.onclick = function () {
    var src = document.getElementById('journal-writing');
    var text = (src && src.value.trim()) || '';
    if (!text) {
      text = 'Write your Writer’s Workshop piece above, then press Publish again — this page is where it goes.';
    }
    var first = text.charAt(0).toUpperCase(), rest = text.slice(1);
    document.getElementById('spkIllumTitle').textContent = 'Week ' + LESSON.week + ' · Voice';
    var body = document.getElementById('spkIllumBody');
    body.innerHTML = '<span class="spk-dropcap">' + dropCapSVG(first) + '</span>';
    var para = document.createElement('span');
    para.textContent = rest;                       /* never innerHTML with student text */
    body.appendChild(para);
    renderIllumAuthor();
    var sealSlot = document.getElementById('spkIllumSeal');
    sealSlot.innerHTML = hasSeal() ? laurelSVG(72) : '';
    document.getElementById('spkColophon').textContent =
      (hasSeal() ? 'Written on the Scholar’s road. ' : '') +
      'Set down at Optima Academy Online on ' +
      new Date().toLocaleDateString(undefined, { year: 'numeric', month: 'long', day: 'numeric' }) + '.';
    page.style.display = 'block';
    page.scrollIntoView({ behavior: REDUCED ? 'auto' : 'smooth', block: 'start' });
    owlSay('A page worth keeping.');
  };
}

function marginalia() {
  ['morphNotice', 'spellReveal', 'g4w7SRev', 'dolAns'].forEach(function (id) {
    var el = document.getElementById(id); if (el) el.classList.add('spk-marginalia');
  });
  document.querySelectorAll('.flip-card-back').forEach(function (b) { b.classList.add('spk-marginalia'); });
  /* emoji out of reveal bodies (§2.10); buttons keep theirs */
  var EMO = /(✅|🔍|📖|🧩|🎉|✨|🌱)️?\s*/g;
  document.querySelectorAll('.dol-answer, .flip-card-back, .decode-reveal, .sort-score, .fillin-feedback, .match-feedback').forEach(function (el) {
    var walk = document.createTreeWalker(el, NodeFilter.SHOW_TEXT, null, false), t;
    while ((t = walk.nextNode())) { t.nodeValue = t.nodeValue.replace(EMO, ''); }
  });
  document.querySelectorAll('.sort-game[data-win]').forEach(function (g) {
    g.setAttribute('data-win', g.getAttribute('data-win').replace(EMO, ''));
  });
}

/* ══════════════════════════════════════════════════════════════
   HOOKS into the lesson's own functions
   ══════════════════════════════════════════════════════════════ */
function hookProgress() {
  var _orig = window.updateProgress;
  window.updateProgress = function () {
    var r = _orig.apply(this, arguments);
    var visited = [].slice.call(document.querySelectorAll('.tab-btn.visited'))
      .map(function (b) { return b.getAttribute('data-tab'); });
    markTabs(visited);
    var total = document.querySelectorAll('.tab-btn').length;
    if (visited.length >= total) {
      var finishedBook = markDone();
      if (!window._spkComplete) {
        window._spkComplete = true;
        var p = profile();
        if (!finishedBook) owlSay(OWL.complete + (p ? ', ' + p.name : '') + '.');
      }
    }
    drawDots();
    drawMapIfPresent();
    return r;
  };
}

function hookTabs() {
  var _orig = window.switchTab;
  window.switchTab = function (tabId) {
    var out = document.querySelector('.tab-panel.active');
    var r = _orig.apply(this, arguments);
    var plate = document.querySelector('.spk-plate');
    if (plate) plate.classList.toggle('spk-folded', tabId !== 'warmup');
    var next = document.getElementById('tab-' + tabId);
    if (next && !REDUCED && out !== next) {
      next.classList.remove('spk-in'); void next.offsetWidth; next.classList.add('spk-in');
      var voice = next.querySelector('.tab-transition-voice');
      if (voice) { voice.style.opacity = '0'; setTimeout(function () { voice.style.transition = 'opacity .2s'; voice.style.opacity = ''; }, 200); }
    }
    return r;
  };
}

function hookGather() {
  var _orig = window.gatherAnswers;
  window.gatherAnswers = function () {
    var r = _orig.apply(this, arguments);
    var out = document.getElementById('gatheredOutput'); if (!out) return r;
    var extra = '\n—— SPARKLE ——\n';
    extra += 'Question path: ' + (currentTier() === 'scholar' ? 'Scholar' : 'Explorer') + '\n';
    if (hasSeal()) extra += 'THE SCHOLAR\u2019S SEAL \u2014 all three answers given with evidence.\n';
    var dol = Sparkle.get('oao.g3ela.dol', {})[LID];
    if (dol) extra += 'DOL sentence chosen: ' + dol.toUpperCase() + '\n';
    var helped = Object.keys(window._spkRevealed || {});
    if (helped.length) extra += 'Answered with help: ' + helped.join(', ') + '\n';
    var copia = ['journal-copia1', 'journal-copia2', 'journal-copia3']
      .map(function (id) { var e = document.getElementById(id); return e && e.value.trim() ? e.value.trim() : null; })
      .filter(Boolean);
    if (copia.length) {
      extra += '\n✎ COPIA — SAY IT THREE WAYS\n────────────────\n';
      copia.forEach(function (c, i) { extra += (i + 1) + '. ' + c + '\n'; });
    }
    /* the boxes the layer added (the DOL fix, reading notes, other on-page
       answers) go into what the student copies and turns in */
    var added = Array.prototype.filter.call(document.querySelectorAll('textarea.spk-onpage'), function (e) { return e.value.trim(); });
    if (added.length) {
      extra += '\n📝 MORE OF MY WORK\n────────────────\n';
      added.forEach(function (e) { extra += (e.getAttribute('data-label') || e.id) + '\n' + e.value.trim() + '\n\n'; });
    }
    /* many lessons' own header names another day's chapter (copied
       forward from week 7); say the right lesson and chapter */
    if (LESSON.bookTitle && LESSON.chapters) {
      out.value = out.value.replace(/^LESSON [^\n]*\n/, 'LESSON ' + LID + ' \u2014 ' + LESSON.bookTitle + ', ' + LESSON.chapters + '\n');
    }
    out.value += extra;
    return r;
  };
}

/* ══════════════════════════════════════════════════════════════
   BOOT
   ══════════════════════════════════════════════════════════════ */
function ornaments() {
  var o = ART.ornaments || {}, root = document.documentElement;
  ['divider', 'corner', 'quill', 'blossom', 'books', 'letter', 'sprig', 'divider2'].forEach(function (k) {
    var u = artURL(o[k]);
    if (u) root.style.setProperty('--spk-orn-' + k, 'url("' + u + '")');
  });
  if (!artURL(o.divider)) return;
  /* a rule at the close of each tab, and under the opening card */
  /* two dividers now, alternating, so four section breaks in a row do
     not print the same sprig four times */
  var alt = !!artURL(o.divider2), n = 0;
  document.querySelectorAll('.tab-next-wrap').forEach(function (w) {
    var d = document.createElement('div');
    d.className = 'spk-divider' + (alt && (n++ % 2) ? ' spk-divider-b' : '');
    d.setAttribute('aria-hidden', 'true');
    w.parentNode.insertBefore(d, w);
  });
  dividerAfterOpening();
}
/* called again after the greeting card is created, because on a first
   visit that happens after ornaments() has already run */
function dividerAfterOpening() {
  if (!artURL((ART.ornaments || {}).divider)) return;
  var open = document.getElementById('spkGreet');
  if (!open || open.nextElementSibling && open.nextElementSibling.classList.contains('spk-divider')) return;
  var d = document.createElement('div');
  d.className = 'spk-divider'; d.setAttribute('aria-hidden', 'true');
  open.parentNode.insertBefore(d, open.nextSibling);
}

/* ══════════════════════════════════════════════════════════════
   §2.14  DECLUTTER

   Four small removals, all additive: the original file is untouched,
   and dropping the sparkle layer puts every one of them back.
   ══════════════════════════════════════════════════════════════ */
function declutter() {
  /* 1. Today's Path and the You'll-need strip. Both restate the tab bar
     and the materials the student already has in front of them, and
     they sit in the most valuable space on the page — above the fold,
     before the lesson starts. */
  ['.todays-path', '.need-strip'].forEach(function (sel) {
    document.querySelectorAll(sel).forEach(function (el) { el.remove(); });
  });

  /* 2. The "you don't have to write this down" reassurances. They sit
     under prompts that are already marked as thinking prompts, so they
     tell a student something the page has just told them — 295 times
     across 102 of the 129 files, six different wordings, which is why
     matching one string was not enough.

     The rule is whole-line: a thinking-stop goes only when reassurance
     is ALL it says. Anything that also carries a direction survives —
     "Hold this question in your mind as you read", "you'll answer
     these in the Assignment", every "Think: …" prompt. That leaves
     181 of the 476 standing, which are the ones doing work. */
  var FILLER = new RegExp(
    '^(?:\\u{1F4AD}\\s*)?(?:' +
      "pause and think(?: about this)?\\s*-\\s*no need to write(?: here)?" +
      "|think about this as you read today\\s*-\\s*you don't need to write anything here" +
      "|think:?\\s*no need to write\\s*-\\s*just carry this question into your reading" +
      "|let this question sit with you\\s*-\\s*you don't need to write anything here" +
    ')\\.?$', 'iu');
  document.querySelectorAll('.thinking-stop').forEach(function (el) {
    var t = (el.textContent || '')
      .replace(/[\u2018\u2019]/g, "'")        /* curly apostrophes */
      .replace(/[\u2013\u2014]/g, '-')        /* en and em dashes  */
      .replace(/\s+/g, ' ').trim();
    if (FILLER.test(t)) el.remove();
  });
}

/* 3. Changing tabs used to jump to the top of the page. That is
   disorienting: a student two thirds of the way down Word Study clicks
   Reading and is thrown back to the header. The tab bar is sticky, so
   there is nothing to go back up for. This holds the scroll position
   across the switch by suppressing the original's scrollIntoView for
   the length of the call, then putting the scroll back. */
function hookTabScroll() {
  if (typeof window.switchTab !== 'function') return;
  var inner = window.switchTab;
  window.switchTab = function (tabId) {
    var y = window.pageYOffset || document.documentElement.scrollTop || 0;
    var top = document.getElementById('pageTop');
    var real = top && top.scrollIntoView;
    if (real) top.scrollIntoView = function () {};     /* muzzle it */
    try { return inner.apply(this, arguments); }
    finally {
      if (real) top.scrollIntoView = real;
      /* the browser may still settle a frame later, so put it back
         twice rather than fight the timing */
      window.scrollTo(0, y);
      requestAnimationFrame(function () { window.scrollTo(0, y); });
    }
  };
}

/* ══════════════════════════════════════════════════════════════
   MY LEARNING JOURNAL
   The Assignment tab's "Download as PDF" used to print only the
   chapter answers. On a lesson whose DATA carries `notes`, it now
   prints a journal page the student can keep: the day's Big
   Question, one-line notes on what was taught (reading move,
   vocabulary, word parts, grammar, spelling), everything they
   typed, each under the question it answers, and their writing.
   Lessons without `notes` keep the lesson's own download untouched,
   so this rolls out lesson by lesson.

   DATA.notes = {
     wgrd:      "one line",
     vocab:     [["word","short meaning"], ...],
     wordParts: "one line",
     grammar:   "one line",
     spelling:  "one line",
     more:      ["optional extra one-liners"]
   }
   ══════════════════════════════════════════════════════════════ */
function buildJournal() {
  if (!DATA.notes) return;
  window.downloadJournal = sparkleJournal;
  /* the button now gives a journal, not a bare PDF of answers, so say so */
  var btns = document.querySelectorAll('.gathered-btn-pdf');
  for (var i = 0; i < btns.length; i++) btns[i].textContent = '\ud83d\udcd3 Download your ELA journal for the day';
  var intros = document.querySelectorAll('.gathered-intro');
  for (var j = 0; j < intros.length; j++) {
    intros[j].textContent = intros[j].textContent.replace(/download as a PDF\./i, 'download your ELA journal for the day.');
  }
}

function journalText(el) {
  return el ? (el.innerText || el.textContent || '').replace(/\s+/g, ' ').trim() : '';
}

/* the prompt a box answers: the nearest question before it, trying
   the real question first and the hint line only as a fallback */
function journalPrompt(field) {
  if (field.id === 'my-story') return 'My story so far';
  if (/^journal-copia/.test(field.id)) return field.getAttribute('data-label') || '';
  var order = ['.q-text', '.swyk-prompt', '.rwm-step-label', '.task-instruction', '.textbox-prompt'];
  var node = field.parentElement;
  for (var up = 0; node && up < 5; up++, node = node.parentElement) {
    for (var c = 0; c < order.length; c++) {
      var found = node.querySelectorAll(order[c]), best = null;
      for (var i = 0; i < found.length; i++) {
        if (found[i].compareDocumentPosition(field) & Node.DOCUMENT_POSITION_FOLLOWING) best = found[i];
      }
      if (best) {
        /* the Scholar road adds a clause to the question; keep it, set apart */
        var extra = best.querySelector('.spk-scholar-add'), more = '';
        if (extra && extra.style.display !== 'none') more = journalText(extra);
        var copy = best.cloneNode(true), x = copy.querySelector('.spk-scholar-add');
        if (x) x.remove();
        var q = journalText(copy).replace(/^\d+[.)]?\s*/, '').replace(/^[^A-Za-z0-9\u201c"]+/, '');
        return more ? q + ' Scholar: ' + more.replace(/^[\u2026.\s]+/, '') : q;
      }
    }
  }
  return field.getAttribute('data-label') || '';
}

/* which part of the lesson a box sits in, e.g. "Grammar: Irregular Plural Nouns" */
function journalSection(field) {
  var rwm = field.closest('.rwm-box');
  if (rwm) { var sen = journalText(rwm.querySelector('.rwm-sentence')); return 'Read like a Writer' + (sen ? ' · ' + sen : ''); }
  var act = field.closest('.activity');
  var t = act ? act.querySelector('.activity-title') : null;
  if (!t && field.closest('.spk-copia-card')) return 'Copia · Say It Three Ways';
  return t ? journalText(t).replace(/^[^A-Za-z]+/, '') : '';
}

function sparkleJournal() {
  try { if (window.gatherAnswers) window.gatherAnswers(); } catch (e) {}
  var N = DATA.notes || {};
  var p = profile();
  var name = p && p.name ? p.name : '';
  var bq = journalText(document.querySelector('.theme-question .intro-card-body p'));
  var today = new Date().toLocaleDateString(undefined, { year: 'numeric', month: 'long', day: 'numeric' });
  var title = (LESSON.bookTitle || '') + (LESSON.chapters ? ' — ' + LESSON.chapters : '');

  var TABS = [['tab-warmup', 'Warm-Up'], ['tab-words', 'Word Study'],
              ['tab-reading', 'Reading'], ['tab-assignment', 'Chapter Thinking']];
  var WRITING = /^(my-story|journal-writing|spk-)/;

  var h = '<!DOCTYPE html><html><head><meta charset="UTF-8"><title>My Learning Journal — Lesson ' + esc(LID) + '</title><style>' +
    "body{font-family:Georgia,'Lora',serif;max-width:720px;margin:36px auto;padding:0 24px;color:#1F2A44;line-height:1.6;font-size:16px}" +
    'h1{font-size:26px;margin:0;color:#0E1C42}' +
    '.sub{color:#5A4A2C;font-style:italic;margin:2px 0 4px}' +
    '.meta{font-family:Arial,sans-serif;font-size:13px;color:#56627F;border-bottom:3px double #C7922C;padding-bottom:10px;margin-bottom:18px}' +
    '.bq{background:#FFF7E6;border-left:5px solid #C7922C;padding:10px 14px;margin:0 0 20px;font-size:17px}' +
    '.bq b{display:block;font-family:Arial,sans-serif;font-size:12px;letter-spacing:.06em;text-transform:uppercase;color:#8A6212}' +
    'h2{font-size:19px;color:#0E1C42;margin:26px 0 8px;padding-bottom:4px;border-bottom:1px solid #E4D3AC}' +
    'ul{margin:6px 0 0 0;padding-left:20px}li{margin:4px 0}' +
    '.k{font-weight:bold;color:#0E1C42}' +
    'h3{font-family:Arial,sans-serif;font-size:13px;letter-spacing:.05em;text-transform:uppercase;color:#56627F;margin:18px 0 4px}' +
    '.s{font-style:italic;color:#6A5A3A;margin:16px 0 0;font-size:15px}' +
    '.q{font-weight:bold;margin:12px 0 3px;font-size:15px}' +
    '.a{white-space:pre-wrap;background:#FAFBFF;border-left:3px solid #9FB4D8;padding:6px 12px;border-radius:3px}' +
    '.none{color:#8A93A8;font-style:italic}' +
    '@media print{body{margin:0}h2{break-after:avoid}.q{break-after:avoid}}' +
    '</style></head><body>';
  h += '<h1>My Learning Journal</h1>';
  h += '<div class="sub">Lesson ' + esc(LID) + (title ? ' · ' + esc(title) : '') + '</div>';
  h += '<div class="meta">' + (name ? esc(name) + ' · ' : '') + esc(today) + '</div>';
  if (bq) h += '<div class="bq"><b>Big Question</b>' + esc(bq) + '</div>';

  /* what was taught, one line each */
  var notes = '';
  if (N.wgrd) notes += '<li><span class="k">What good readers do:</span> ' + esc(N.wgrd) + '</li>';
  if (N.vocab && N.vocab.length) {
    notes += '<li><span class="k">Vocabulary:</span><ul>';
    N.vocab.forEach(function (v) { notes += '<li><span class="k">' + esc(v[0]) + '</span> — ' + esc(v[1]) + '</li>'; });
    notes += '</ul></li>';
  }
  if (N.wordParts) notes += '<li><span class="k">Word parts:</span> ' + esc(N.wordParts) + '</li>';
  if (N.grammar) notes += '<li><span class="k">Grammar:</span> ' + esc(N.grammar) + '</li>';
  if (N.spelling) notes += '<li><span class="k">Spelling:</span> ' + esc(N.spelling) + '</li>';
  (N.more || []).forEach(function (m) { notes += '<li>' + esc(m) + '</li>'; });
  if (notes) h += '<h2>What I learned</h2><ul>' + notes + '</ul>';

  /* everything they typed, in page order, under its question */
  var thinking = '', writing = '';
  TABS.forEach(function (t) {
    var panel = document.getElementById(t[0]); if (!panel) return;
    var part = '', lastSec = '';
    panel.querySelectorAll('textarea[data-label], input[type="text"][data-label]').forEach(function (f) {
      var val = (f.value || '').trim();
      var sec = journalSection(f);
      if (sec === t[1]) sec = '';
      var block = (sec && sec !== lastSec ? '<div class="s">' + esc(sec) + '</div>' : '') +
                  '<div class="q">' + esc(journalPrompt(f)) + '</div>' +
                  (val ? '<div class="a">' + esc(val) + '</div>' : '<div class="a none">(not answered yet)</div>');
      lastSec = sec;
      if (WRITING.test(f.id || '')) writing += block; else part += block;
    });
    if (part) thinking += '<h3>' + t[1] + '</h3>' + part;
  });
  if (thinking) h += '<h2>My thinking</h2>' + thinking;
  if (writing) h += '<h2>My writing</h2>' + writing;
  h += '</body></html>';

  var win = window.open('', '_blank');
  if (!win) { alert('Please allow pop-ups so your journal can open.'); return; }
  win.document.write(h);
  win.document.close();
  setTimeout(function () { try { win.focus(); win.print(); } catch (e) {} }, 400);
}


/* ══════════════════════════════════════════════════════════════
   THE COMPACT PAGE TOP (28 Oct 2026, from science / social studies)
   One header row: title, a meta line, a 🔊 Read aloud pill that opens
   the existing read-aloud player, and a ⓘ Lesson details pill that
   holds the unit / week / reading / focus cells and the standards.
   The progress bar, the standards bar and the info strip leave the
   top. The chapter numeral, quote and Big Question show on the first
   tab only (the plate already folds off it). Nothing is deleted: the
   original nodes are moved or hidden, so the lesson's own scripts
   keep working.
   ══════════════════════════════════════════════════════════════ */
function buildTop() {
  var header = document.querySelector('.header'); if (!header) return;
  var root = document.documentElement;
  root.classList.add('spk-top');
  header.classList.add('spk-hd');

  var title = header.querySelector('.header-title');
  var badge = header.querySelector('.header-badge-text');
  var meta = document.createElement('div');
  meta.className = 'spk-hd-meta';
  var bits = [];
  if (badge && badge.textContent.trim()) bits.push('<b>' + esc(badge.textContent.trim()) + '</b>');
  if (LESSON.week) bits.push('Week ' + LESSON.week);
  meta.innerHTML = bits.join(' · ');
  if (title) title.appendChild(meta);

  var tools = document.createElement('div');
  tools.className = 'spk-hd-tools';
  header.appendChild(tools);

  var after = header;
  function panel(html) {
    var pn = document.createElement('div');
    pn.className = 'spk-hd-panel';
    pn.innerHTML = html || '';
    after.parentNode.insertBefore(pn, after.nextSibling);
    after = pn;
    return pn;
  }
  function pill(label, pn, aria) {
    var b = document.createElement('button');
    b.type = 'button'; b.className = 'spk-pill'; b.innerHTML = label;
    b.setAttribute('aria-expanded', 'false');
    if (aria) b.setAttribute('aria-label', aria);
    b.addEventListener('click', function () {
      var open = !pn.classList.contains('open');
      document.querySelectorAll('.spk-hd-panel.open').forEach(function (x) { x.classList.remove('open'); });
      document.querySelectorAll('.spk-pill[aria-expanded="true"]').forEach(function (x) { x.setAttribute('aria-expanded', 'false'); });
      if (open) { pn.classList.add('open'); b.setAttribute('aria-expanded', 'true'); }
      try { localStorage.setItem('oao.g3ela.hdOpen', open ? (pn.getAttribute('data-k') || '') : ''); } catch (e) {}
    });
    tools.appendChild(b);
    return b;
  }

  /* 🔊 Read aloud — the player itself is the page's own, just moved */
  var ra = document.getElementById('optima-read-aloud');
  var raPill = null;
  if (ra) {
    var rp = panel(''); rp.setAttribute('data-k', 'ra'); rp.classList.add('spk-hd-ra');
    rp.appendChild(ra);
    raPill = pill('🔊 Read aloud', rp);
  }

  /* ⓘ Lesson details — the info strip cells and both standards lists */
  var dl = '';
  document.querySelectorAll('.info-strip .info-cell').forEach(function (c) {
    var l = c.querySelector('.info-label'), v = c.querySelector('.info-value'), d = c.querySelector('.info-detail');
    if (!l || !v) return;
    dl += '<dt>' + esc(l.textContent.trim()) + '</dt><dd><b>' + esc(v.textContent.trim()) + '</b>' +
          (d && d.textContent.trim() ? ' · ' + esc(d.textContent.replace(/\s+/g, ' ').trim()) : '') + '</dd>';
  });
  document.querySelectorAll('.standards-panel .standards-group').forEach(function (g) {
    var l = g.querySelector('.standards-group-label');
    var codes = Array.prototype.map.call(g.querySelectorAll('.standards-codes span'), function (x) { return x.textContent.trim(); })
      .filter(function (x) { return x && x !== '·'; });
    if (!l || !codes.length) return;
    dl += '<dt>' + esc(l.textContent.trim()) + '</dt><dd class="spk-std">' + codes.map(esc).join(' · ') + '</dd>';
  });
  if (dl) {
    var dp = panel('<dl>' + dl + '</dl>'); dp.setAttribute('data-k', 'details');
    pill('ⓘ Lesson details', dp);
  }

  /* the first tab carries the chapter's front matter; the others don't */
  function mark(id) { root.setAttribute('data-spk-tab', id || 'warmup'); }
  var active = document.querySelector('.tab-panel.active');
  mark(active && active.id ? active.id.replace(/^tab-/, '') : 'warmup');
  var inner = window.switchTab;
  if (typeof inner === 'function') {
    window.switchTab = function (id) { var r = inner.apply(this, arguments); mark(id); return r; };
  }
}

/* ══════════════════════════════════════════════════════════════
   EVERYTHING ANSWERED ON THE PAGE (28 Oct 2026)
   1. Every "rewrite this sentence … in your notebook" (the Daily Oral
      Language fix, the mimic lines) gets a box right there, and the
      line is reworded to point at it.
   2. DATA.inputs adds a box anywhere else a lesson asks for writing
      with nowhere to put it:
        inputs: [{ id, after: '<text the element starts with or contains>',
                   label, hint, rows, min }]
   3. Every journal box shows a live word counter. A goal shows only when
      DATA.counters[id] sets one (about 8 words per sentence the task
      asks for); with no goal it simply counts.
   Each box is a journal-box with a data-label, so it is saved, and it
   reaches the journal download under its tab.
   ══════════════════════════════════════════════════════════════ */
function onPageBox(id, label, hint, rows) {
  var ta = document.createElement('textarea');
  ta.className = 'journal-box spk-onpage';
  ta.id = id;
  ta.setAttribute('data-label', label);
  ta.placeholder = hint || 'Type here…';
  ta.rows = rows || 2;
  try { var v = localStorage.getItem(window._lessonKey + '-' + id); if (v) ta.value = v; } catch (e) {}
  ta.addEventListener('input', function () {
    try { localStorage.setItem(window._lessonKey + '-' + id, ta.value); } catch (e) {}
    if (window.gatherAnswers) try { window.gatherAnswers(); } catch (e) {}
  });
  return ta;
}
var NOTEBOOK_RX = /\b(?:rewrite|write|try)\b[^.]*?\b(?:in|into) your (?:reading )?(?:notebook|journal)\b/i;

/* ══════════════════════════════════════════════════════════════
   WHAT GOOD READERS DO: THE NOTE-CATCHER (28 Oct 2026)
   The reading move asks students to jot, chart or tally while they
   read; this gives them the place to do it, shaped like that day's
   How-to. It sits in What Good Readers Do, follows the student to the
   Reading tab as a "📝 My reading notes" drawer, opens from the
   Assignment question that uses the same skill, and its boxes go into
   the journal.
     DATA.wgrd = { catcher: { title, intro, layout: 'stack'|'row',
                              fields: [{ label, hint, rows }],
                              end: { label, hint } },          // optional "put it together" line
                   useAt: ['journal-q1', …] }
   Short notes, no word goals.
   ══════════════════════════════════════════════════════════════ */
function buildCatcher() {
  var W = DATA.wgrd, C = W && W.catcher;
  if (!C || !C.fields || !C.fields.length) return;
  var act = null;
  document.querySelectorAll('.activity').forEach(function (a) {
    var t = a.querySelector('.activity-title');
    if (!act && t && /What Good Readers Do/i.test(t.textContent)) act = a;
  });
  if (!act) return;
  var body = act.querySelector('.activity-body') || act;
  var card = document.createElement('div');
  card.className = 'spk-catcher' + (C.layout === 'row' ? ' spk-catcher-row' : '');
  var html = '<div class="spk-catcher-head">📝 ' + esc(C.title || 'My reading notes') + '</div>' +
    (C.intro ? '<p class="spk-catcher-intro">' + C.intro + '</p>' : '') + '<div class="spk-catcher-fields"></div>';
  card.innerHTML = html;
  var wrap = card.querySelector('.spk-catcher-fields');
  C.fields.forEach(function (f, i) {
    var cell = document.createElement('label');
    cell.className = 'spk-catcher-cell';
    cell.innerHTML = '<span class="spk-catcher-l">' + esc(f.label) + '</span>';
    var ta = onPageBox('journal-wgrd' + (i + 1), 'Reading notes: ' + f.label, f.hint || '', f.rows || 2);
    ta.classList.add('spk-catcher-box');
    cell.appendChild(ta);
    wrap.appendChild(cell);
  });
  if (C.end) {
    var endc = document.createElement('label');
    endc.className = 'spk-catcher-cell spk-catcher-end';
    endc.innerHTML = '<span class="spk-catcher-l">' + esc(C.end.label) + '</span>';
    var te = onPageBox('journal-wgrd-end', 'Reading notes: ' + C.end.label, C.end.hint || '', 2);
    te.classList.add('spk-catcher-box');
    endc.appendChild(te);
    card.appendChild(endc);
  }
  /* the notes live where the reading happens: at the end of the Read activity on
     the Reading tab, every day. If What Good Readers Do sits on another tab (days
     1-2), it gets a one-line pointer instead, so nobody clicks back mid-chapter. */
  var readAct = null;
  document.querySelectorAll('#tab-reading .activity').forEach(function (a) {
    var t = a.querySelector('.activity-title');
    if (!readAct && t && /^\W*Read\b/.test(t.textContent.trim())) readAct = a;
  });
  var wgrdPanel = act.closest('.tab-panel');
  if (readAct) {
    (readAct.querySelector('.activity-body') || readAct).appendChild(card);
    if (!(wgrdPanel && wgrdPanel.id === 'tab-reading')) {
      var ptr = document.createElement('p');
      ptr.className = 'spk-catcher-ptr';
      ptr.innerHTML = '📝 Your note boxes for this, <b>' + esc(C.title || 'My reading notes') + '</b>, are on the <b>Reading</b> tab, right where you read.';
      var bx = body.querySelector('.socratic-box');
      if (bx) bx.parentNode.insertBefore(ptr, bx); else body.appendChild(ptr);
    }
  } else {
    var before = body.querySelector('.socratic-box');
    if (before) before.parentNode.insertBefore(card, before); else body.appendChild(card);
  }
  var home = card.parentNode, homeNext = card.nextSibling;

  /* the drawer: the same card, carried along to the Reading tab */
  var drawer = document.createElement('div');
  drawer.className = 'spk-notes-drawer';
  drawer.setAttribute('role', 'dialog');
  drawer.setAttribute('aria-label', 'My reading notes');
  drawer.innerHTML = '<div class="spk-notes-top"><b>📝 My reading notes</b><button type="button" class="spk-notes-x" aria-label="Close my reading notes">✕</button></div><div class="spk-notes-in"></div>';
  document.body.appendChild(drawer);
  var fab = document.createElement('button');
  fab.type = 'button'; fab.className = 'spk-notes-fab'; fab.textContent = '📝 My reading notes';
  /* the notes sit on the Reading tab now, so the floating button would only
     repeat them there; 'Use your reading notes' still opens the drawer later */
  var homePanel = card.closest('.tab-panel');
  if (homePanel && homePanel.id === 'tab-reading') fab.classList.add('hide');
  document.body.appendChild(fab);
  function open() { drawer.querySelector('.spk-notes-in').appendChild(card); drawer.classList.add('open'); fab.classList.add('hide'); var f = card.querySelector('textarea'); if (f) try { f.focus({ preventScroll: true }); } catch (e) {} }
  function close() { home.insertBefore(card, homeNext && homeNext.parentNode === home ? homeNext : null); drawer.classList.remove('open'); if (!(homePanel && homePanel.id === 'tab-reading')) fab.classList.remove('hide'); }
  fab.addEventListener('click', open);
  drawer.querySelector('.spk-notes-x').addEventListener('click', close);
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape' && drawer.classList.contains('open')) close(); });
  /* put the card home before the journal reads the page */
  var dj = window.downloadJournal;
  if (typeof dj === 'function') window.downloadJournal = function () { if (drawer.classList.contains('open')) close(); return dj.apply(this, arguments); };

  (W.useAt || []).forEach(function (id) {
    var ta = document.getElementById(id); if (!ta) return;
    var b = document.createElement('button');
    b.type = 'button'; b.className = 'spk-notes-use'; b.textContent = '📝 Use your reading notes';
    b.addEventListener('click', open);
    ta.parentNode.insertBefore(b, ta);
  });
}

function buildOnPage() {
  var made = 0;
  /* 1. the notebook lines */
  document.querySelectorAll('.dol-hint, .tab-panel p, .tab-panel div').forEach(function (el) {
    if (el.closest('.spk-card') || el.getAttribute('data-spk-np')) return;
    if (Array.prototype.some.call(el.children, function (c) { return !/^(B|I|EM|STRONG|SPAN|U|BR)$/.test(c.tagName); })) return;
    var t = el.textContent.replace(/\s+/g, ' ').trim();
    if (t.length > 220 || !NOTEBOOK_RX.test(t)) return;
    if (/cursive|copywork|copy (?:it|this|the)/i.test(t)) return;   /* handwriting stays on paper */
    el.setAttribute('data-spk-np', '1');
    var isDol = !!el.closest('.dol-fix, [class*="dol"]') || el.classList.contains('dol-hint') || /rewrite this sentence/i.test(t);
    var id = isDol ? 'journal-dol' : ('journal-np' + (++made));
    if (document.getElementById(id)) id = 'journal-np' + (++made);
    /* swap only the words "in your notebook / journal", keeping the line's own formatting */
    var tw = document.createTreeWalker(el, NodeFilter.SHOW_TEXT, null), tn;
    while ((tn = tw.nextNode())) tn.nodeValue = tn.nodeValue.replace(/\s*\b(?:in|into) your (?:reading )?(?:notebook|journal)\b/i, ' in the box below');
    /* a "Your turn" line followed by a fill-in frame (Statement: ___) gets
       its box under the frame, so students read the frame first */
    var at = el, nx = el.nextElementSibling;
    if (!isDol && nx && /_{3,}/.test(nx.textContent)) at = nx;
    var box = onPageBox(id, isDol ? 'Daily Oral Language: my fixed sentence' : 'My sentence',
      isDol ? 'Type your sentence here, with every fix made…' : (at !== el ? 'Copy the frame and fill it in here…' : 'Type your sentence here…'), at !== el ? 3 : 2);
    if (at !== el) el.innerHTML = el.innerHTML.replace(' in the box below', ' in the box under the frame');
    at.parentNode.insertBefore(box, at.nextSibling);
  });
  /* 2. DATA.inputs */
  (DATA.inputs || []).forEach(function (I, n) {
    if (!I || !I.after || document.getElementById(I.id || ('journal-in' + n))) return;
    var want = String(I.after).toLowerCase(), hit = null;
    document.querySelectorAll('.tab-panel p, .tab-panel li, .tab-panel div, .tab-panel h3, .tab-panel h4').forEach(function (el) {
      if (hit || el.children.length > 3) return;
      if (el.textContent.replace(/\s+/g, ' ').trim().toLowerCase().indexOf(want) >= 0) hit = el;
    });
    if (!hit) { (window.OAO_SPARKLE_MISSED = window.OAO_SPARKLE_MISSED || []).push('inputs: ' + I.after); return; }
    var box = onPageBox(I.id || ('journal-in' + n), I.label || 'My notes', I.hint, I.rows || 2);
    if (I.swap) hit.innerHTML = I.swap;
    hit.parentNode.insertBefore(box, hit.nextSibling);
    if (I.min) (DATA.counters = DATA.counters || {})[box.id] = I.min;
  });
  /* 3. word counters on every journal box */
  document.querySelectorAll('textarea.journal-box').forEach(addCounter);
}
function words(t) { return (String(t).trim().match(/[A-Za-z0-9’']+/g) || []).length; }
function addCounter(ta) {
  if (!ta || ta.getAttribute('data-spk-wc') || ta.readOnly || ta.id === 'gatheredOutput') return;
  if (document.getElementById(ta.id + '-count')) return;      /* My Story keeps its own counter */
  ta.setAttribute('data-spk-wc', '1');
  /* goals come only from DATA.counters, set from each task by hand:
     reading the number off the prompt guessed wrong too often ("pick ONE
     sentence from Anne" is a quote, not a length) */
  var goal = (DATA.counters && DATA.counters[ta.id]) || 0;
  var c = document.createElement('div');
  c.className = 'spk-wc';
  c.setAttribute('aria-live', 'polite');
  ta.parentNode.insertBefore(c, ta.nextSibling);
  function upd() {
    var n = words(ta.value);
    if (goal) {
      c.textContent = '📝 ' + n + ' of ' + goal + ' words' + (n >= goal ? ' ✓' : n ? '. Keep going…' : '');
      c.classList.toggle('met', n >= goal);
    } else c.textContent = '📝 ' + n + (n === 1 ? ' word' : ' words');
  }
  ta.addEventListener('input', upd); upd();
  setTimeout(upd, 600);            /* after the lesson restores saved answers */
}

/* ══════════════════════════════════════════════════════════════
   G3 ELA ADDITIONS (Nov 2026): Opti's Story Map
   Everything here is driven by the lesson's own DATA. Nothing below
   names a lesson, a book or a chapter.
     DATA.glossary  = [ {w, m, key} ]      dotted words, 🔊 on key words
     DATA.sayWords  = [ 'word', … ]          🔊 on the vocab cards (says just the word)
     DATA.cards     = [ {id, kind, tab, after, title, sub, look, todo, …} ]
     DATA.wordgame  = {type:'tower', …}      Up the North Tower
   The six rules for 8-year-olds: every module opens with
   "👀 What am I looking at?" and a "What to do:" line, and shows one
   step at a time.
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

/* "👀 What am I looking at?" + "What to do:", the opening of every module */
function lookCard(look, todo) {
  var h = '';
  if (look) h += '<div class="g3-look"><div class="g3-look-h">👀 What am I looking at?</div><p>' + look + '</p></div>';
  if (todo) h += '<p class="g3-todo"><b>What to do:</b> ' + todo + '</p>';
  return h;
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
  var h = lookCard(c.look, c.todo) + artFig(c.art);
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
  var ICON = { info: '👀', tapwords: '💬', crest: '🛡️' };
  /* reversed, so two cards anchored to the same activity keep DATA order */
  C.slice().reverse().forEach(function (c) {
    if (document.getElementById('g3card-' + c.id)) return;
    var at = g3Anchor(c); if (!at) return;
    var card = cardShell(c, c.icon || ICON[c.kind]);
    var body = card.querySelector('.spk-card-body');
    if (c.kind === 'info') cardInfo(c, body);
    else if (c.kind === 'tapwords') cardTapwords(c, body);
    else if (c.kind === 'crest') cardCrest(c, body);
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


function boot() {
  /* Each step is isolated. Previously all eighteen sat inside one
     try/catch, so a lesson whose DATA was missing a key — no DOL pair,
     no copia seed — threw in the middle and silently skipped every step
     after it: no guiding voice, no ornaments, no declutter, and only a
     console warning to say so. Rolling this across 129 lessons, that
     failure mode would have been invisible and common.

     Now a builder that throws costs exactly its own feature. The names
     are logged so a broken lesson says which piece is missing. */
  var steps = [
    ['hooks',       function () { hookProgress(); hookTabs(); hookGather(); hookTabScroll(); }],
    ['declutter',   declutter],
    ['top',         buildTop],
    ['numeral',     buildNumeral],
    ['plate',       buildPlate],
    ['writing',     buildWritingProject],
    ['journey',     buildJourney],
    ['greeting',    function () {
        /* Ask for the name on whichever sparkled lesson a student
           reaches first, not only on day 1: someone starting on day 2
           would otherwise never see the greeting, the connector or the
           welcome clip. Where storage is blocked the name cannot be
           kept, so off day 1 we don't ask on every page load. */
        if (profile()) renderGreeting();
        else if (LESSON.day === 1 || storageWorks()) showProfileCard(false);
    }],
    ['dol',         buildDolChoice],
    ['tiers',       buildTiers],
    ['coaches',     buildCoaches],
    ['copia',       buildCopia],
    ['wordgame',    buildWordGame],
    ['glossary',    buildGlossary],
    ['saywords',    buildSayWords],
    ['cards',       buildCards],
    ['tips',        hookTips],
    ['bookflip',    buildBookFlip],
    ['readalong',   buildReadAlong],
    ['spotlight',   buildSpotlight],
    ['watch',       liftWatchBlock],
    ['media',       buildMedia],
    ['captions',    captionAllFilms],
    ['publish',     buildPublish],
    ['catcher',     buildCatcher],
    ['onpage',      buildOnPage],
    ['journal',     buildJournal],
    ['opti',        optiFaces],
    ['marginalia',  marginalia],
    ['ornaments',   ornaments],
    ['seal',        function () { sealCheck(true); }],
    ['progress',    function () { if (window.updateProgress) window.updateProgress(); }]
  ];
  var failed = [];
  for (var i = 0; i < steps.length; i++) {
    try { steps[i][1](); }
    catch (e) {
      failed.push(steps[i][0]);
      if (window.console && console.warn) console.warn('[sparkle] ' + steps[i][0] + ' failed:', e);
    }
  }
  if (failed.length && window.console && console.warn) {
    console.warn('[sparkle] ' + failed.length + ' of ' + steps.length +
                 ' steps did not run: ' + failed.join(', '));
  }
  window.OAO_SPARKLE_FAILED = failed;   /* the sweep asserts this is empty */
}


if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', boot);
else boot();

/* Flow fix (Oct 28 2026, parent feedback): remember the open tab, so a Canvas reload (after
   Submit) reopens where the student was instead of on Warm-Up. */
(function () {
  var KEY = 'oao-tab-' + location.pathname;
  function put(v) { try { localStorage.setItem(KEY, v); } catch (e) { try { sessionStorage.setItem(KEY, v); } catch (e2) {} } }
  function get() { try { return localStorage.getItem(KEY); } catch (e) { try { return sessionStorage.getItem(KEY); } catch (e2) { return null; } } }
  function hook() {
    if (typeof window.switchTab !== 'function' || window.switchTab._remembers) return;
    var orig = window.switchTab;
    var wrapped = function (id) { var r = orig.apply(this, arguments); put(id); return r; };
    wrapped._remembers = true;
    window.switchTab = wrapped;
    var last = get();
    if (last && last !== 'warmup' && document.getElementById('tab-' + last)) {
      var pt = document.getElementById('pageTop'), keep = pt && pt.scrollIntoView;
      if (pt) pt.scrollIntoView = function () {};   /* no jump on restore */
      try { orig(last); } catch (e) {}
      if (pt) pt.scrollIntoView = keep;
    }
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', hook);
  else hook();
})();

})();
