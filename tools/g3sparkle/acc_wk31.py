"""Week 31 (Paired Texts: The Courage to Act) accuracy + wording fixes, approved by Bethany Nov 16 2026
(claude/g3-ela-wk31-audit.md; she chose to KEEP both course-written texts and fix their errors).
Check-in fixes live in the quiz JSON. Run once on the pre-sparkle files:  python tools/g3sparkle/acc_wk31.py [--apply]"""
import sys, re

def ol(icon, k, t): return '<div class="obj-line"><span class="obj-icon">%s</span><span><strong>%s:</strong> %s</span></div>' % (icon, k, t)
OBJ = {
 1: [('📖', 'Reading', 'I will read Text 1 and explain what it says courage is.'), ('🌱', 'Word parts', 'I will build words with prefixes and suffixes from this year.'),
     ('✏️', 'Grammar', 'I will find capital, comma, apostrophe and verb mistakes in a passage.'), ('🔤', 'Spelling', 'I will sort words by whether they have a prefix or a suffix.'),
     ('✍️', 'Writing', 'I will plan my comparison and write my claim.')],
 2: [('📖', 'Reading', 'I will read Text 2 and find how the author shows courage.'), ('🌱', 'Word parts', 'I will match words with prefixes and suffixes to their meanings.'),
     ('✏️', 'Grammar', 'I will name simple, compound and complex sentences.'), ('🔤', 'Spelling', 'I will split long words into their parts.'),
     ('✍️', 'Writing', 'I will draft the opening of my comparison.')],
 3: [('📖', 'Reading', 'I will collect details from both texts.'), ('🌱', 'Word parts', 'I will put word parts together to build words.'),
     ('✏️', 'Grammar', 'I will fix every mistake in a sentence, like an editor.'), ('🔤', 'Spelling', 'I will build long words one syllable at a time.'),
     ('✍️', 'Writing', 'I will draft one paragraph for each text.')],
 4: [('📖', 'Reading', 'I will explain what both texts teach about courage.'), ('🌱', 'Word parts', 'I will explain how a prefix or suffix changes a word.'),
     ('✏️', 'Grammar', 'I will edit a passage in passes: capitals, apostrophes, then the rest.'), ('🔤', 'Spelling', 'I will count the beats in long words and say where they split.'),
     ('✍️', 'Writing', 'I will write my closing and finish my comparison.')],
}
OBJ_RE = re.compile(r'<div class="obj-line"><span class="obj-icon">📖</span>.*?\n<div class="obj-line"><span class="obj-icon">✏️</span>.*?\n<div class="obj-line"><span class="obj-icon">🔤</span>.*?</span></div>')
QOLD = '&ldquo;Courage is not the absence of fear. It is deciding that something else is more important.&rdquo;</div>\n  <div class="quote-strip-attr" style="color:#D4AF37;font-size:13px;margin-top:8px;">&mdash; Week 31 — Big Idea'
QNEW = '&ldquo;%s&rdquo;</div>\n  <div class="quote-strip-attr" style="color:#D4AF37;font-size:13px;margin-top:8px;">&mdash; %s'
QS = {1: ('Courage shows up in many different forms.', 'Text 1, &ldquo;What Is Courage?&rdquo;'),
      2: ('Her voice came out steadier than she expected.', 'Text 2, &ldquo;The Choice at the Bridge&rdquo;'),
      3: ('Instead, she took a breath. She walked onto the bridge.', 'Text 2, &ldquo;The Choice at the Bridge&rdquo;'),
      4: ('I just decided that he mattered more than my fear did.', 'Mira, Text 2')}
UNIT_OLD = '<div class="info-value">Unit 5</div><div class="info-detail">The Lion, the Witch and the Wardrobe</div>'
UNIT_NEW = '<div class="info-value">Year-End</div><div class="info-detail">Two texts about courage</div>'
PILL_OLD = '<div class="info-detail">Compare how two authors present the them…</div>'
PILL_NEW = '<div class="info-detail">Two texts about courage</div>'
NOW_OLD = 'Now reading: <strong>Week 31 — Compare how two authors present the theme of coura</strong>'
NOW_NEW = 'Now reading: <strong>Week 31 — Two texts about courage</strong>'
T1_OLD = 'What Is Courage? (Informational Text)</div>'
T1_NEW = 'What Is Courage? (Informational Text)</div>\n    <div style="font-size:13px;color:#7A88A8;font-style:italic;margin:-2px 0 6px;">Written for Optima Academy Online</div>'
T2_OLD = 'The Choice at the Bridge (Original Fiction Scene)</div>'
T2_NEW = 'The Choice at the Bridge (Original Fiction Scene)</div>\n    <div style="font-size:13px;color:#7A88A8;font-style:italic;margin:-2px 0 6px;">A made-up story, written for Optima Academy Online</div>'
TEXT1 = [('Psychologists who study courage say that it is not the absence of fear. In fact, most courageous acts involve fear.',
          'Courage is not the same as having no fear. In fact, most courageous acts involve fear.'),
         ('Ancient philosophers listed courage as one of the most important virtues a person could develop. Many educators today still teach it as a core value, sometimes called one of the pillars of good character.',
          'More than two thousand years ago, the Greek thinker Plato named courage as one of the four most important virtues a person can have. Many schools today still teach it as one of the pillars of good character.')]
EVID = 'Use evidence from the book in your answer.'
EV_TEXT = 'Use details from the text in your answer.'
EV_BOTH = 'Use details from both texts in your answer.'
EV_BOOK = 'Use one detail from the book you choose.'
EV_PLAN = {1: [EV_TEXT, EV_TEXT, EV_BOOK], 2: [EV_TEXT, EV_BOTH, EV_BOTH], 3: [EV_TEXT, EV_BOTH, EV_BOOK], 4: [EV_BOTH, EV_BOTH, EV_BOOK]}

def sw(w, ok): return '<span class="spotter-word" onclick="gramSpotAll(this,\'gspot1\')" data-correct="%s">%s</span>' % ('true' if ok else 'false', w)
SPOT_RE = re.compile(r'(<div class="spotter-sentence" id="gspot1" data-done="false" style="[^"]*">).*?(<div class="spotter-result" id="gspot1-result">)')
def spot(words): return ' '.join(sw(w, ok) for w, ok in words)
P = lambda s: [(w[1:], 1) if w.startswith('*') else (w, 0) for w in s.split()]
SPOT = {1: P('*although *mira was *scared she *goed onto the bridge. *the small *boys face was white with fear.'),
        2: P('*miras heart *hammered and her feet wanted to run. *she *taked a breath.'),
        4: P('*the small *boys face was *white and he *couldnt move. *mira *goed onto the *bridge and she spoke to the three boys.')}
def hw(tip, t): return '<span class="dol-highlight-word" onclick="dolHighlight(this,\'%s\')">%s</span>' % (tip, t)
DOL_RE = re.compile(r'(<div class="dol-sentence-wrap" id="dolModel">).*?(</div>)')
DOL2 = (hw('This word begins the opening part &mdash; it cannot stand alone.', 'Although') + ' Mira was ' +
        hw('The comma comes after the opening part, before the main sentence.', 'afraid,') + ' she walked onto the ' + hw('A period ends the sentence.', 'bridge.'))
FIX = '<div class="dol-sentence-wrap" style="border-left:4px solid #C7922C;">%s</div>'
COR = '<p style="margin-bottom:6px;"><strong>Corrected:</strong> %s</p>'
WHY = '<p style="font-size:13px;color:#7A88A8;font-style:italic;">%s</p>'
SORT_CHIPS = [('suffix', 'courageous'), ('suffix', 'fearless'), ('prefix', 'rebuild'), ('prefix', 'unafraid'),
              ('prefix', 'transform'), ('suffix', 'hopeful'), ('prefix', 'interact'), ('suffix', 'careless')]
BANK_RE = re.compile(r'<div class="sort-bank" id="sortBank">.*?</div>')
BANK = '<div class="sort-bank" id="sortBank">' + ''.join('<span class="sort-chip" data-group="%s" onclick="pickSortChip(this)">%s</span> ' % c for c in SORT_CHIPS) + '</div>'
COLS_RE = re.compile(r'<div class="sort-columns">.*?\n        </div>\n          <div class="sort-score"', re.S)
COL = '<div class="sort-col"><div class="sort-col-header" style="background:linear-gradient(135deg,%s);">%s</div><div class="sort-col-drop" data-col="%s" onclick="dropSortChip(this,\'%s\')"></div></div>'
COLS_NEW = ('<div class="sort-columns">\n            ' + COL % ('#1B7A4E,#2EA863', 'Prefix at the front', 'prefix', 'prefix') + '\n            ' +
            COL % ('#8B6914,#a87f1f', 'Suffix at the end', 'suffix', 'suffix') + '\n        </div>\n          <div class="sort-score"')

R = {
 1: [('<td style="padding:6px 10px;color:#1B7A4E;font-weight:600;">courageous, hopeful, faithful</td>', '<td style="padding:6px 10px;color:#1B7A4E;font-weight:600;">careful, hopeful, faithful</td>'),
     ('<span style="font-weight:700;color:#0E1C42;">fear-</span>', '<span style="font-weight:700;color:#0E1C42;">fear +</span>'),
     ('Example: un + courage + ous = uncourageous.', 'Example: un + help + ful = unhelpful.'),
     ('Desper&eacute;aux&rsquo;s <input class="fillin-input" id="vcloze2" data-answer="perseverance" maxlength="16" placeholder="______"> showed in every chapter &mdash; he kept going even when the dungeon seemed endless.',
      'Despereaux showed <input class="fillin-input" id="vcloze2" data-answer="perseverance" maxlength="16" placeholder="______"> when he kept going, even in the dark dungeon.'),
     ('Ancient philosophers agreed that courage is not just a skill but a <input class="fillin-input" id="vcloze3" data-answer="virtue" maxlength="10" placeholder="______"> &mdash; something built through practice over time.',
      'Text 1 says courage is a <input class="fillin-input" id="vcloze3" data-answer="virtue" maxlength="10" placeholder="______">, a quality of good character you build one choice at a time.'),
     ('Sort these words into the correct spelling pattern group.', 'Sort each word: does it have a prefix at the front or a suffix at the end?')],
 2: [(FIX % 'although prince brat had been selfish and cruel he learned what real courage looked like when jemmy protected him',
      FIX % 'after a long moment the three boys turned and walked away'),
     (COR % 'Although Prince Brat had been selfish and cruel, he learned what real courage looked like when Jemmy protected him.',
      COR % 'After a long moment, the three boys turned and walked away.'),
     (WHY % 'Although begins the dependent clause; comma after cruel; Prince Brat = proper noun (capitals); when begins second dependent clause; period ends.',
      WHY % 'After begins the opening part, so it gets a capital; a comma comes after the opening part (moment); period ends. (Text 2: &ldquo;But after a long moment &hellip; they turned and walked away.&rdquo;)'),
     ("Text 1 says courage is 'deciding to act even when you are afraid.' How does Mira's actions in Text 2 match — or not match — that definition?",
      "Text 1 says an act is courageous when &ldquo;the person chooses to act anyway.&rdquo; How do Mira&rsquo;s actions in Text 2 match &mdash; or not match &mdash; that idea?"),
     ("the fiction scene shows it through one character's choice on a cold afternoon.", "the fiction scene shows it through one girl&rsquo;s choice on an old, narrow bridge.")],
 3: [('although lucy was scared she goed through the wardrobe and she didnt look back.', 'although mira was scared she goed onto the bridge and she didnt run away.'),
     ('Although Lucy was scared, she went through the wardrobe, and she didn&rsquo;t look back.', 'Although Mira was scared, she went onto the bridge, and she didn&rsquo;t run away.'),
     ('when edmund reached the witchs sleigh he didnt turn around and he runned faster.', 'when the three boys heard miras voice they stared at her and then they goed away.')],
 4: [('<p>Capitals at sentence starts and on every name: <strong>although, the, lucy, jemmy, narnia, when, edmund</strong>.</p>',
      '<p>Capitals at sentence starts and on every name: <strong>the &rarr; The, mira &rarr; Mira</strong>.</p>'),
     ('<p>Possessive apostrophes: <strong>princes</strong> &rarr; prince&rsquo;s, <strong>bears</strong> &rarr; bear&rsquo;s, <strong>childrens</strong> &rarr; children&rsquo;s, <strong>lucys</strong> &rarr; Lucy&rsquo;s.</p>',
      '<p>Possessive apostrophe: <strong>boys</strong> &rarr; boy&rsquo;s (the face belongs to the boy).</p>'),
     ('<p>Contractions: <strong>didnt</strong> &rarr; didn&rsquo;t.</p>', '<p>Contraction: <strong>couldnt</strong> &rarr; couldn&rsquo;t.</p>'),
     ('<p>Irregular past forms: <strong>goed</strong> &rarr; went, <strong>runned</strong> &rarr; ran.</p>', '<p>Irregular past form: <strong>goed</strong> &rarr; went.</p>')],
}
COMMA_OLD = '<p>A comma after an opening clause, and a comma before <em>and</em> when it joins two complete thoughts.</p>'
COMMA_NEW = '<p>Commas before <em>and</em> when it joins two complete thoughts: <strong>white,</strong> and <strong>bridge,</strong></p>'

def sub1(s, a, b, f):
    n = s.count(a)
    assert n == 1, (f, n, a[:90])
    return s.replace(a, b)

def main(apply):
    for d in (1, 2, 3, 4):
        f = 'lesson-31-%d-ext.html' % d
        s = open(f, encoding='utf-8').read(); o = s
        s = sub1(s, QOLD, QNEW % QS[d], f)
        s = sub1(s, UNIT_OLD, UNIT_NEW, f)
        s = sub1(s, PILL_OLD, PILL_NEW, f)
        s = sub1(s, NOW_OLD, NOW_NEW, f)
        assert len(OBJ_RE.findall(s)) == 1, (f, 'obj')
        s = OBJ_RE.sub(lambda m: '\n'.join(ol(*x) for x in OBJ[d]), s)
        s = sub1(s, T1_OLD, T1_NEW, f)
        if d > 1: s = sub1(s, T2_OLD, T2_NEW, f)
        for a, b in TEXT1: s = sub1(s, a, b, f)
        assert s.count(EVID) == 3, (f, s.count(EVID))
        for e in EV_PLAN[d]: s = s.replace(EVID, e, 1)
        if d in SPOT:
            assert len(SPOT_RE.findall(s)) == 1, (f, 'spot')
            s = SPOT_RE.sub(lambda m: m.group(1) + spot(SPOT[d]) + m.group(2), s)
        if d == 2:
            assert len(DOL_RE.findall(s)) == 1
            s = DOL_RE.sub(lambda m: m.group(1) + DOL2 + m.group(2), s)
        if d == 1:
            assert len(BANK_RE.findall(s)) == 1 and len(COLS_RE.findall(s)) == 1, (f, 'sort')
            s = BANK_RE.sub(lambda m: BANK, s); s = COLS_RE.sub(lambda m: COLS_NEW, s)
        if d == 4: s = sub1(s, COMMA_OLD, COMMA_NEW, f)
        for a, b in R[d]: s = sub1(s, a, b, f)
        assert s.count('<div') - s.count('</div>') == o.count('<div') - o.count('</div>'), (f, 'div balance')
        print(f, 'ok', len(o), '->', len(s))
        if apply: open(f, 'w', encoding='utf-8').write(s)

if __name__ == '__main__':
    main('--apply' in sys.argv)
