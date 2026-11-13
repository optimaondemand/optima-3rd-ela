#!/usr/bin/env python3
"""Port the G4 ELA sparkle layer to G3 ELA (optima-3rd-ela).

    python port.py <g4 sparkle.js> <g4 sparkle.css> <g3mod.js> <g3.css> <out dir>

Writes <out>/g3-sparkle.js and <out>/g3-sparkle.css. Every edit is an
exact-match replacement that must hit the expected number of times, so a
change upstream in G4 fails loudly here instead of porting half a layer.
"""
import re, sys, io

g4js, g4css, mod, g3css, out = sys.argv[1:6]
js = io.open(g4js, encoding='utf-8').read()
css = io.open(g4css, encoding='utf-8').read()

def rep(s, a, b, n=1):
    c = s.count(a)
    if c != n:
        sys.exit('port: expected %d of %r, found %d' % (n, a[:80], c))
    return s.replace(a, b)

def cut(s, start, end, insert=''):
    i = s.find(start); j = s.find(end, i + 1)
    if i < 0 or j < 0:
        sys.exit('port: cut markers not found: %r .. %r' % (start[:50], end[:50]))
    return s[:i] + insert + s[j:]

def block(s, start, new):
    """replace `var NAME = [ ... ];` / `{ ... };` starting at `start`"""
    i = s.find(start)
    if i < 0: sys.exit('port: no ' + start)
    close = '\n];' if start.rstrip().endswith('[') else '\n};'
    j = s.find(close, i)
    return s[:i] + new + s[j + len(close):]

# ── header ──────────────────────────────────────────────────────────
js = rep(js, js[:js.find('(function () {')],
  '/* ══════════════════════════════════════════════════════════════\n'
  '   OAO SPARKLE · G3 ELA (Opti\'s Story Map)\n'
  '   Ported Nov 2026 from optima-4th-ela/sparkle.js by\n'
  '   tools/g3sparkle/port.py. Lesson content never lives here: each\n'
  '   lesson carries its own DATA block (see tools/inject.py).\n'
  '   ══════════════════════════════════════════════════════════════ */\n')

# ── storage namespace: G3 keeps its own progress, profile and settings.
#    Same origin as G4 (optimaondemand.github.io), and families have
#    children in both grades on one computer.
js = js.replace("'oao.g4ela.", "'oao.g3ela.")
js = rep(js, "Sparkle.get('oao.profile', null)", "Sparkle.get('oao.g3ela.profile', null)")
js = rep(js, "Sparkle.set('oao.profile',", "Sparkle.set('oao.g3ela.profile',")
js = js.replace("g4ela-", "g3ela-")
js = rep(js, "var LESSON = { grade: 4, subject: 'ela', book: 'anne', week: 7, day: 1 };",
             "var LESSON = { grade: 3, subject: 'ela', book: 'wb', week: 18, day: 1 };")

# ── the course ──────────────────────────────────────────────────────
js = block(js, 'var COURSE = [', '''var COURSE = [
  { id:'stanley', title:'Flat Stanley',                 weeks:[1,5],   place:'the Lambchops\\u2019 house' },
  { id:'nonfic',  title:'Letters and Maps',             weeks:[6,7],   place:null, kind:'nonfiction' },
  { id:'desp',    title:'The Tale of Despereaux',       weeks:[8,17],  place:'the castle' },
  { id:'wb',      title:'The Whipping Boy',             weeks:[18,22], place:'the king\\u2019s castle' },
  { id:'med',     title:'Castles and Knights',          weeks:[23,24], place:null, kind:'nonfiction' },
  { id:'lww',     title:'The Lion, the Witch and the Wardrobe', weeks:[25,30], place:'Narnia' },
  { id:'ext',     title:'Journey\\u2019s End',          weeks:[31,32], place:null, kind:'synthesis' }
];''')
js = block(js, 'var SHELF = [', '''var SHELF = [
  { id:'stanley', short:'Flat Stanley' },
  { id:'desp',    short:'Despereaux' },
  { id:'wb',      short:'The Whipping Boy', gold:true },
  { id:'lww',     short:'Narnia' }
];''')
js = block(js, 'var WRITING_ARCS = [', '''var WRITING_ARCS = [
  { weeks:[1,5],   name:'a personal narrative',  gloss:'a true story from your own life' },
  { weeks:[6,7],   name:'a friendly letter',     gloss:'a letter to a real person, with a greeting and a closing' },
  { weeks:[8,17],  name:'a story response',      gloss:'writing about what happens in a book and why' },
  { weeks:[18,22], name:'an opinion paragraph',  gloss:'writing where you say what you think and give reasons' },
  { weeks:[23,24], name:'an informational piece',gloss:'writing that teaches facts about a topic' },
  { weeks:[25,30], name:'a fantasy story',       gloss:'a made-up story with magic in it' },
  { weeks:[31,32], name:'your year-end project', gloss:'looking back at the books you read this year' }
];''')
js = block(js, 'var REGION = {', '''var REGION = {
  stanley: { wash:'#F3D9A6', ink:'#A8701F', label:'Stanley\\u2019s Street' },
  nonfic:  { wash:'#CFE2C8', ink:'#4F7A3E', label:'The Post Office' },
  desp:    { wash:'#E4C7D6', ink:'#8A3E66', label:'The Mouse Castle' },
  wb:      { wash:'#C8CEE6', ink:'#3B4A86', label:'The North Tower' },
  med:     { wash:'#E2D6BC', ink:'#7A6234', label:'Knights\\u2019 Hall' },
  lww:     { wash:'#D3E6EE', ink:'#2F6380', label:'The Lamp-Post' },
  ext:     { wash:'#F1D79C', ink:'#A8801F', label:'Journey\\u2019s End' }
};''')
js = block(js, 'var LANDMARK = {', '''var LANDMARK = {
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
};''')
# G4's painted board is G4's art. G3 uses the drawn road: no board, no
# covers (the shelf shows title spines; covers are copyrighted), and no
# ornaments, seals or headpieces until G3 has its own.
js = rep(js, "board: { src: 'maps/year-board.jpg' },", "board: { src: 'art/road/year-board.jpg' },")
js, n1 = re.subn(r"\n  covers: \{\n.*?\n  \},", """
  /* the four novels on the G3 shelf. Covers are stored in the repo
     (from Open Library, sized for the shelf); a cover that fails to load
     falls back to a drawn spine, so the shelf never shows a hole. */
  covers: {
    stanley: 'art/covers/stanley.jpg',
    desp:    'art/covers/desp.jpg',
    wb:      'art/covers/wb.jpg',
    lww:     'art/covers/lww.jpg'
  },""", js, count=1, flags=re.S)
js, n2 = re.subn(r"\n  worlds: \{\n.*?\n  \},", "\n  worlds: {},", js, count=1, flags=re.S)
if n1 != 1 or n2 != 1: sys.exit('port: covers/worlds not replaced')
js = rep(js, "    scholar: 'seals/scholar.png',\n    mark:    'seals/scholar-mark.png'", "    scholar: '',\n    mark:    ''")
js = re.sub(r"  banners: \{.*?\},\n", "  banners: {},\n", js, count=1, flags=re.S)
js = re.sub(r"  ornaments: \{.*?\},\n", "  ornaments: {},\n", js, count=1, flags=re.S)
js = rep(js, "companions: { optima: 'companions/owl.png' }", "companions: { opti: 'companions/owl.png' }")
js = rep(js, "barn:        { label:'Barn',", "opti:        { label:'Opti', body:'#B87333', face:'#EBD3A8', tuft:'#8A5220' },\n  barn:        { label:'Barn',")
js = rep(js, "who + ' · Grade Four</text>';", "who + ' · Grade Three</text>';")
js = rep(js, "Thirty-two weeks, one road, six worlds — and the shelf you fill as you go",
             "Thirty-two weeks, one road, seven stops, and the shelf you fill as you go")
js = rep(js, "(LESSON.book === 'anne' ? 'Anne' : 'we')", "'Opti'")
# (Nov 11 2026) the owl line is already "Opti ... him" in the G4 layer; no rewrite needed

# ── the plate: G3 plates are public-domain art, credited, with a
#    notice/wonder under the picture; one tap tells what it is
js = rep(js, """      if (dp.credit) {
        var cap = document.createElement('figcaption');
        cap.className = 'spk-plate-credit'; cap.textContent = dp.credit;
        plate.appendChild(cap);
      }""", """      if (dp.look) plate.insertAdjacentHTML('beforeend', noticeCard(esc(dp.look), dp.lookBtn));
      if (dp.credit) {
        var cap = document.createElement('figcaption');
        cap.className = 'spk-plate-credit'; cap.textContent = dp.credit;
        plate.appendChild(cap);
      }""")

# ── media: Opti speaks every clip; G3 voices only welcome + 3 notes
js = rep(js, """    { id:'welcome', kind:'audio', at:{greeting:true},
      path:'guide/welcome/g3ela-{w}-{d}',
      label:'Listen to today’s welcome' },""", """    { id:'welcome', kind:'audio', at:{greeting:true},
      path:'guide/opti/g3ela-{w}-{d}-welcome',
      label:'Opti’s welcome' },""")
js = rep(js, "path:'guide/turn/g3ela-{w}-{d}-1',\n      label:'Before you begin the word work' },",
             "path:'guide/opti/g3ela-{w}-{d}-1',\n      label:'Opti · before the word work' },")
js = rep(js, "path:'guide/turn/g3ela-{w}-{d}-2',\n      label:'Before you open the book' },",
             "path:'guide/opti/g3ela-{w}-{d}-2',\n      label:'Opti · before you open the book' },")
js = rep(js, "path:'guide/turn/g3ela-{w}-{d}-3',\n      label:'Before you write' },",
             "path:'guide/opti/g3ela-{w}-{d}-3',\n      label:'Opti · before you write' },")
js = rep(js, "{ id:'rwm',        kind:'audio', at:{sel:'.rwm-box'},", "{ id:'rwm',        kind:'', at:{sel:'.rwm-box'},")
js = rep(js, "{ id:'copia',      kind:'audio', at:{sel:'.spk-copia-card'},", "{ id:'copia',      kind:'', at:{sel:'.spk-copia-card'},")
js = rep(js, "var _GENERIC = /^(chapter|", "var _GENERIC = /^(opti|chapter|")

# ── word games: G4's themed games are G4's. G3 brings its own (g3mod).
js = cut(js, '/* ── Build the bridge:', 'function buildWordGame() {')
js = rep(js, """  var cfg = DATA.wordgame;
  if (!cfg || !WORDGAME[cfg.type]) return;              /* no themed game for this lesson */""",
"""  var cfg = DATA.wordgame;
  if (!cfg || !WORDGAME[cfg.type]) return;              /* no themed game for this lesson */
  if (cfg.type === 'tower' || cfg.type === 'wagon' || cfg.type === 'chase') { WORDGAME[cfg.type](cfg); return; }   /* G3: self-contained, not built from a page game */""")
js = rep(js, "'guide/narrator/g3ela-'", "'guide/opti/g3ela-'")

# ── the G4 book kits (bridge / NTS / Freedom Train) are G4's
js = cut(js, '/* Bridge week (15.x):', '\n/* ══════════════════════════════════════════════════════════════\n   THE COMPACT PAGE TOP')
for k in ("    ['bridgekit',   buildBridgeKit],\n", "    ['ntskit',      buildNtsKit],\n", "    ['ftkit',       buildFtKit],\n"):
    js = rep(js, k, '')


# ── hint ladders reach every G3 fill-in checker, not only checkFillIn:
#    morphology uses checkMorphFill(btn), grammar gramFillCheck(gid)
js = rep(js, """var _origCheckFillIn = window.checkFillIn;
window.checkFillIn = function (btn) {
  var g = (btn && btn.closest) ? btn.closest('.fillin-game') : null;
  var scope = g || document;""", """function spkHintWrap(_orig, scopeOf) { return function (arg) {
  var scope = scopeOf(arg) || document;""")
js = rep(js, """  var r = _origCheckFillIn.apply(this, arguments);""", """  var r = _orig ? _orig.apply(this, arguments) : undefined;""")
js = rep(js, """  if (stuck) owlSay(OWL.stuck);
  else if (!anyWrong) owlCorrect();
  return r;
};
""", """  if (stuck) owlSay(OWL.stuck);
  else if (!anyWrong) owlCorrect();
  return r;
}; }
function _spkGame(btn) { return (btn && btn.closest) ? btn.closest('.fillin-game') : null; }
if (typeof window.checkFillIn === 'function')   window.checkFillIn   = spkHintWrap(window.checkFillIn, _spkGame);
if (typeof window.checkMorphFill === 'function') window.checkMorphFill = spkHintWrap(window.checkMorphFill, _spkGame);
if (typeof window.gramFillCheck === 'function')  window.gramFillCheck  = spkHintWrap(window.gramFillCheck, function (id) { return document.getElementById(id); });
if (typeof window.checkVocabCloze === 'function') window.checkVocabCloze = spkHintWrap(window.checkVocabCloze, function () { var i = document.querySelector('[id^="vcloze"]'); return i ? i.closest('.activity') : null; });
""")


# ── copia opens like every G3 module: "What to do:" (Opti reads it)
js = rep(js, """    '<div class="spk-copia-seed">' + DATA.copia.seed + '</div>';""",
             """    lookCard(DATA.copia.look, DATA.copia.todo) +
    '<div class="spk-copia-seed">' + DATA.copia.seed + '</div>';""")

# ── G3 keeps the page's own palette (Bethany, Nov 7): no G4 cream
js = rep(js, "    ['warm',        function () { document.body.classList.add('spk-warm'); }],\n", "")

js = rep(js, "  a.preload = 'metadata';\n  a.src = src;\n", "  a.preload = 'metadata';\n  a.src = src;\n  wrap._spkAudio = a;\n")
# ── the G3 painted board (Bethany's art, 1536x1024, Nov 2026) ───────
#    32 painted spaces = 32 weeks, one space a week. Centres measured off
#    the file with a circle finder, not eyeballed. Each row reads left to
#    right, bottom row first, like lines on a page: the painting's curves
#    join the rows at the other ends, so the owl hops back to the left
#    at the end of rows 1 and 3.
js = rep(js, "var BOARD_W = 1448, BOARD_H = 1086, BOARD_R = 23;", "var BOARD_W = 1536, BOARD_H = 1024, BOARD_R = 35;")
js = block(js, 'var BOARD_WORLDS = [', """var BOARD_WORLDS = [
  { id:'stanley', x:  30, y: 700, w: 560, h: 310 },
  { id:'nonfic',  x: 740, y: 700, w: 780, h: 310 },
  { id:'desp',    x:  30, y: 470, w:1490, h: 240 },
  { id:'wb',      x:  40, y: 290, w:1040, h: 215 },
  { id:'med',     x:1060, y: 320, w: 460, h: 215 },
  { id:'lww',     x:  30, y:  95, w:1100, h: 235 },
  { id:'ext',     x:1110, y: 100, w: 410, h: 230 }
];""")
js = block(js, 'var BOARD_SPACES = [', """var BOARD_SPACES = [
  [296,961,'#A8701F'], [415,952,'#A8701F'], [535,940,'#A8701F'], [651,928,'#A8701F'], [777,923,'#A8701F'],
  [1241,917,'#4F7A3E'], [1364,916,'#4F7A3E'],
  [505,657,'#8A3E66'], [611,649,'#8A3E66'], [713,641,'#8A3E66'], [819,640,'#8A3E66'], [925,637,'#8A3E66'],
  [1033,640,'#8A3E66'], [1141,644,'#8A3E66'], [1243,656,'#8A3E66'], [1347,656,'#8A3E66'], [1444,627,'#8A3E66'],
  [544,467,'#3B4A86'], [665,449,'#3B4A86'], [785,447,'#3B4A86'], [908,449,'#3B4A86'], [1029,465,'#3B4A86'],
  [1213,489,'#7A6234'], [1352,478,'#7A6234'],
  [400,269,'#2F6380'], [527,267,'#2F6380'], [657,278,'#2F6380'], [778,280,'#2F6380'], [897,286,'#2F6380'], [1023,290,'#2F6380'],
  [1181,279,'#A8801F'], [1304,272,'#A8801F']
];""")
js = block(js, 'var BOARD_LEGS = [', """var BOARD_LEGS = [
  { id:'stanley', weeks:[1,  5], spaces:[ 1,  5] },
  { id:'nonfic',  weeks:[6,  7], spaces:[ 6,  7] },
  { id:'desp',    weeks:[8, 17], spaces:[ 8, 17] },
  { id:'wb',      weeks:[18,22], spaces:[18, 22] },
  { id:'med',     weeks:[23,24], spaces:[23, 24] },
  { id:'lww',     weeks:[25,30], spaces:[25, 30] },
  { id:'ext',     weeks:[31,32], spaces:[31, 32] }
];""")
# no open field on this painting for the student's name: it goes on a
# small ribbon under the title banner instead
js = rep(js, """    s += '<text x="724" y="543" font-size="30" text-anchor="middle" ' +""",
             """    s += '<text x="768" y="148" font-size="26" text-anchor="middle" ' +""")
# the owl is a little smaller on this board, and the LESSON pill sits
# under the space so it never covers the next one along the row
js = rep(js, "var me = BOARD_SPACES[cur - 1], OW = 150;", "var me = BOARD_SPACES[cur - 1], OW = 124;")
js = rep(js, """  var bx = me[0] < BOARD_W - 200 ? me[0] + 46 : me[0] - 46 - bw;
  s += '<rect x="' + bx + '" y="' + (me[1] - 17) + '" width="' + bw + '" height="34" rx="17" fill="#C7922C"/>' +
       '<text x="' + (bx + bw / 2) + '" y="' + (me[1] + 7) + '" font-size="18" text-anchor="middle" ' +""",
             """  var bx = Math.max(8, Math.min(BOARD_W - bw - 8, me[0] - bw / 2)), by = me[1] + BOARD_R + 12;
  s += '<rect x="' + bx + '" y="' + by + '" width="' + bw + '" height="34" rx="17" fill="#C7922C" stroke="#FFF8E9" stroke-width="2"/>' +
       '<text x="' + (bx + bw / 2) + '" y="' + (by + 24) + '" font-size="18" text-anchor="middle" ' +""")
# ── plain words (Nov 8): no story about Erasmus, no "no wrong answer",
#    the writing project is named by what it is, and books light up
js = rep(js, "'<div class=\"spk-card-sub\">Long ago, a teacher named Erasmus had his students rewrite one sentence a hundred ways. You only need three.</div>' +",
             "'<div class=\"spk-card-sub\">Write one sentence three new ways.</div>' +")
js = rep(js, "    '<p style=\"font-size:15px;color:#3A4A6B;\">Here is one sentence about this week’s reading. There is no wrong answer here — only more ways to say it.</p>' +\n", "")
js = rep(js, "'That way your whole ' + (/report/i.test(arc.name) ? 'report' : /essay|analysis/i.test(arc.name) ? 'essay' : /project/i.test(arc.name) ? 'project' : 'story') + ' is in one place and nothing gets lost.</p>' +",
             "'That way your whole ' + (/paragraph/i.test(arc.name) ? 'paragraph' : /letter/i.test(arc.name) ? 'letter' : /report/i.test(arc.name) ? 'report' : /essay|analysis/i.test(arc.name) ? 'essay' : /project/i.test(arc.name) ? 'project' : 'story') + ' is in one place and nothing gets lost.</p>' +")
js = rep(js, "note.textContent = 'Your document is the one that always has your whole story.';", "note.textContent = 'Your document always has all of your writing.';")
js = rep(js, "['Change the opener', 'Start with a when or a where.'],", "['Change the opener', 'Start with when or where it happened.'],")
js = rep(js, "['Swap the verb', 'Find a stronger word than the one in bold.'],", "['Swap the verb', 'Use a stronger word than the bold word.'],")
js = rep(js, "A book stands up once you have read all of it.", "A book lights up once you have read all of it.")
# ── fewer words (pilot, Nov 10 2026): "a lot of reading for 3rd grade"
#    Writer's Workshop banner: title + week line + one line on where to keep it
js = rep(js, "    '<div class=\"spk-goal-gloss\">' + arc.gloss + '</div>' +\n", "")
js = cut(js, "      '<div class=\"spk-keep-title\">Keep your writing in one place</div>' +", "    '</div>';\n  var firstReal",
  "      '<p><b>Every day:</b> copy your writing into one document called <b>My ' +\n"
  "      titleCase(arc.name.replace(/^an? /, '').replace(/^your /, '')) + '</b>.</p>' +\n")
#    Explorer / Scholar in one line each, no note under them
js = rep(js, "'<div class=\"spk-roads-label\">Pick how you want to answer today\\u2019s three questions.</div>' +",
             "'<div class=\"spk-roads-label\">Pick one. Both finish the lesson.</div>' +")
js = rep(js, """        '<span class="spk-road-line">Every question asks you for <b>one more thing</b>: another detail, ' +
        'or <b>why</b> you think so. Finish all three and you earn the Scholar\\u2019s seal.</span>' +""",
             """        '<span class="spk-road-line">Add <b>one more</b> detail or reason to each answer. Earn the Scholar\\u2019s seal.</span>' +""")
js = rep(js, "    '<div class=\"spk-roads-note\">Either one finishes the lesson. You can switch whenever you want.</div>' +\n", "")

# ── G3 additions, inside the IIFE, ahead of boot
m = io.open(mod, encoding='utf-8').read()
js = rep(js, '\nfunction boot() {', '\n' + m + '\n\nfunction boot() {')
js = rep(js, "    ['wordgame',    buildWordGame],\n",
             "    ['wordgame',    buildWordGame],\n    ['glossary',    buildGlossary],\n    ['saywords',    buildSayWords],\n    ['cards',       buildCards],\n    ['tips',        hookTips],\n    ['bookflip',    buildBookFlip],\n    ['readalong',   buildReadAlong],\n    ['spotlight',   buildSpotlight],\n    ['saydo',       buildSayDo],\n")
js = rep(js, "    ['journal',     buildJournal],\n", "    ['journal',     buildJournal],\n    ['opti',        optiFaces],\n    ['teach',       buildTeach],\n    ['howto',       buildHowTo],\n")
# the greeting builds media again after a name is entered; Opti follows
js = rep(js, "  try { buildMedia(); } catch (e) {}\n  dividerAfterOpening();",
             "  try { buildMedia(); } catch (e) {}\n  try { optiFaces(); } catch (e) {}\n  dividerAfterOpening();")

# ── a new tab starts at the top (pilot, Nov 10 2026): no G4 scroll-hold;
#    the 👆 tap rule + key line, and g3TabTop, run with the hooks
js = rep(js, "hookGather(); hookTabScroll(); }],", "hookGather(); }],\n    ['taps',        buildTaps],")

if 'g4ela' in js: sys.exit('port: g4ela left in the layer')
io.open(out + '/g3-sparkle.js', 'w', encoding='utf-8').write(js)
css += '\n\n' + io.open(g3css, encoding='utf-8').read()
io.open(out + '/g3-sparkle.css', 'w', encoding='utf-8').write(css)
print('g3-sparkle.js %d bytes, g3-sparkle.css %d bytes' % (len(js.encode()), len(css.encode())))
