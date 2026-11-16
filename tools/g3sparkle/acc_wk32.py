"""Week 32 (Year-End Culmination: The 7 Pillars of Virtue) accuracy fixes, approved by Bethany Nov 16 2026
(claude/g3-ela-wk32-audit.md, "Approve all"). Every character example is checked in the novel texts in Planning docs.
Check-in fixes live in the quiz JSON. Run once on the pre-sparkle files:  python tools/g3sparkle/acc_wk32.py [--apply]"""
import sys, re

QOLD = '&ldquo;The books we read become part of who we are.&rdquo;</div>'
QS = {1: ('But they can try.', 'Mrs. Lambchop, <em>Flat Stanley</em>'),
      2: ('Lay down the whip,&rdquo; he commanded with a princely air.', 'Jemmy, <em>The Whipping Boy</em>'),
      3: ('&hellip;the Pea was a kind person, and perhaps more important, she was empathetic.', '<em>The Tale of Despereaux</em>'),
      4: ('But nothing would stop him.', 'Peter, about Edmund, <em>The Lion, the Witch and the Wardrobe</em>')}
ATTR_RE = re.compile(r'(<div class="quote-strip-attr"[^>]*>)(?:&mdash;|—) Week 32 (?:&mdash;|—) Year-End Reflection')
UNIT = ('<div class="info-value">Unit 5</div><div class="info-detail">The Lion, the Witch and the Wardrobe</div>',
        '<div class="info-value">Year-End</div><div class="info-detail">All four books</div>')
PILL = ('<div class="info-detail">Honesty · Respect · Courtesy · Responsib…</div>', '<div class="info-detail">The 7 Pillars of Virtue</div>')
NOW = ('Now reading: <strong>Week 32 — Honesty · Respect · Courtesy · Responsibility · Co</strong>', 'Now reading: <strong>Week 32 — The 7 Pillars of Virtue</strong>')
EVID = '<div class="textbox-prompt">Use evidence from the book in your answer.</div>'
EB = '<div class="textbox-prompt">%s</div>'
D_BOOK = "Use a detail from your character&rsquo;s book."
EV_PLAN = {1: [D_BOOK] * 3, 2: [D_BOOK] * 3, 3: [D_BOOK] * 3,
           4: [D_BOOK, 'Think about your own reading this year.', 'Write to a new 3rd grader.']}

def sw(w, ok): return '<span class="spotter-word" onclick="gramSpotAll(this,\'gspot1\')" data-correct="%s">%s</span>' % ('true' if ok else 'false', w)
SPOT_RE = re.compile(r'(<div class="spotter-sentence" id="gspot1" data-done="false" style="[^"]*">).*?(<div class="spotter-result" id="gspot1-result">)', re.S)
P = lambda s: [(w[1:], 1) if w.startswith('*') else (w, 0) for w in s.split()]
SPOT = {1: P('*stanley was flat. *despereaux was brave. *jemmy *runned from the castle. *lucy *goed through the wardrobe to *narnia.'),
        2: P('*stanley *goed to *california in an envelope. *the sneak thieves *didnt get away.'),
        4: P('*the four children *was crowned in *narnia. *edmund *didnt give up in the battle, and he *breaked the *witchs wand.')}
def spot(words): return ' '.join(sw(w, ok) for w, ok in words)

def ex(color, t): return '<p style="font-size:13px;color:%s;font-weight:600;">📖 Example: %s</p>' % (color, t)
PILLARS = [
 ('#D4AF37', 'Despereaux treats the princess with complete respect even though he is a mouse.',
  'Mrs. Lambchop tells Stanley, &ldquo;It is wrong to dislike people for their shapes.&rdquo; (<em>Flat Stanley</em>)'),
 ('#8B6FC0', 'Flat Stanley writes kind letters and treats new people with courtesy wherever he travels.',
  'Despereaux tells the princess, &ldquo;I honor you,&rdquo; the polite words a knight says in his book of stories. (<em>The Tale of Despereaux</em>)'),
 ('#1B7A4E', 'Edmund takes responsibility for his betrayal and makes it right through his actions.',
  'Edmund says &ldquo;I&rsquo;m sorry&rdquo; to each of his brother and sisters. (<em>The Lion, the Witch and the Wardrobe</em>)'),
 ('#C7922C', 'Jemmy protects Prince Brat even when it puts his own life at risk.',
  'Jemmy orders the outlaws, &ldquo;Lay down the whip,&rdquo; to stop them from whipping the prince. (<em>The Whipping Boy</em>)'),
 ('#5B8DD9', "Aslan's sacrifice is the ultimate act of service — giving everything for another's freedom.",
  'Stanley stays in a picture frame all night at the museum to help catch the sneak thieves. (<em>Flat Stanley</em>)'),
 ('#E05C7A', 'Despereaux never stops trying to reach the princess, no matter how many times he is stopped.',
  'Despereaux loses his tail and goes down to the dungeon, back out, and back in again to save the princess. (<em>The Tale of Despereaux</em>)'),
 ('#1B7A4E', 'Lucy is honest about Narnia even when no one believes her.',
  'Lucy keeps telling the truth about Narnia, even when no one believes her. (<em>The Lion, the Witch and the Wardrobe</em>)'),
]
SORT_CHIPS = [('suffix', 'honesty'), ('suffix', 'courageous'), ('prefix', 'unafraid'), ('prefix', 'rebuild'),
              ('suffix', 'fearless'), ('prefix', 'unkind'), ('suffix', 'perseverance'), ('suffix', 'hopeful')]
BANK_RE = re.compile(r'<div class="sort-bank" id="sortBank">.*?</div>')
BANK = '<div class="sort-bank" id="sortBank">' + ''.join('<span class="sort-chip" data-group="%s" onclick="pickSortChip(this)">%s</span> ' % c for c in SORT_CHIPS) + '</div>'
COLS_RE = re.compile(r'<div class="sort-columns">.*?\n        </div>\n          <div class="sort-score"', re.S)
COL = '<div class="sort-col"><div class="sort-col-header" style="background:linear-gradient(135deg,%s);">%s</div><div class="sort-col-drop" data-col="%s" onclick="dropSortChip(this,\'%s\')"></div></div>'
COLS_NEW = ('<div class="sort-columns">\n            ' + COL % ('#1B7A4E,#2EA863', 'Prefix at the front', 'prefix', 'prefix') + '\n            ' +
            COL % ('#8B6914,#a87f1f', 'Suffix at the end', 'suffix', 'suffix') + '\n        </div>\n          <div class="sort-score"')
SEL = '<select id="vocab_sel_0" onchange="checkVocabSel(0,\'empathy\')"'
CLARA1_OLD = "Pillars I will cover: Honesty (he eventually confesses the truth), Responsibility (he accepts the consequences of his betrayal), Courage (he fights in the final battle), Perseverance (he keeps going even after making a terrible mistake), Service (he breaks the Witch's wand at great personal risk)."
CLARA1_NEW = ("Pillars I will cover: Responsibility (he says &ldquo;I&rsquo;m sorry&rdquo; to each of his brother and sisters), Courage (in the battle he smashes the Witch&rsquo;s wand with his sword), "
              "Service (Peter says they would have been beaten without him), Perseverance (Peter says &ldquo;nothing would stop him&rdquo;).")
CLARA2_OLD = "This is important because Edmund had previously used his fear as an excuse to make selfish choices. In the final battle, he overcomes that fear entirely."
CLARA2_NEW = "Peter says Edmund fought his way through three ogres to reach her. Earlier in the story Edmund helped the Witch; now he is the one who stops her."
R = {
 1: [('his courage and honesty at the end of the story showed that he had changed.', 'his courage in the battle showed that he had changed.'),
     ('Desper&eacute;aux showed <input class="fillin-input" id="vcloze2" data-answer="empathy" maxlength="11" placeholder="______"> when he stopped to listen to Princess Pea&rsquo;s grief, even in the midst of his own fear.',
      'The Princess Pea had <input class="fillin-input" id="vcloze2" data-answer="empathy" maxlength="11" placeholder="______">: she could feel what other people felt.'),
     ('Jemmy&rsquo;s <input class="fillin-input" id="vcloze3" data-answer="resilience" maxlength="14" placeholder="______"> was remarkable &mdash; each time life knocked him down, he found a way to stand back up.',
      'Jemmy showed <input class="fillin-input" id="vcloze3" data-answer="resilience" maxlength="14" placeholder="______">: he grew up in the streets and sewers, and he kept finding a way.'),
     ('<span class="decode-part decode-part-root">integer</span><span class="decode-part-plus">+</span><span class="decode-part decode-part-affix">-ity</div>',
      '<span class="decode-part decode-part-root">integer (whole)</span><span class="decode-part-plus">+</span><span class="decode-part decode-part-affix">-ity</span></div>'),
     ('<p>Fill in the missing part after the prefix to build the word.</p>', '<p>Type the missing part to build each word.</p>'),
     ('<p>Sort these words into the correct spelling pattern group.</p>', '<p>Sort each word: does it have a prefix at the front or a suffix at the end?</p>'),
     (CLARA1_OLD, CLARA1_NEW)],
 2: [('&ldquo;It is wrong to dislike people for their shapes. Or their religion, or the color of their skin.&rdquo;',
      '&ldquo;It is wrong to dislike people for their shapes. Or their religion, for that matter, or the color of their skin.&rdquo;'),
     ('This is from <em>Flat Stanley</em>, the first book you read this year.', 'Mrs. Lambchop says this to Stanley in <em>Flat Stanley</em>, the first book you read this year.'),
     ('The author could have used one long sentence; instead he stops, then adds more &mdash; <strong>Or their religion, or the color of their skin.</strong>',
      'Mrs. Lambchop could have said it in one long sentence; instead she stops, then adds more &mdash; <strong>Or their religion, for that matter, or the color of their skin.</strong>'),
     (CLARA2_OLD, CLARA2_NEW),
     ('<div class="info-value">Draft — Write the Response</div>', '<div class="info-value">Draft your response</div>'),
     ('<div class="activity-sub">Draft — Write the Response — master the pattern</div>', '<div class="activity-sub">Use the rules: tap the right word in each row.</div>')],
 3: [('stanleys brother didnt believe him and he goed to california anyway.', 'stanleys family didnt buy a ticket and he goed to california in an envelope.'),
     ('Stanley&rsquo;s brother didn&rsquo;t believe him, and he went to California anyway.', 'Stanley&rsquo;s family didn&rsquo;t buy a ticket, and he went to California in an envelope.'),
     ('despereauxs sister didnt understand him and he goed to the dungeon alone.', 'despereauxs sister showed him the library and he readed a book about a knight.'),
     ("Despereaux showed " + SEL, "The Princess Pea showed " + SEL),
     ("— he understood the princess's sadness as if it were his own.", "— she could feel what other people felt."),
     ('&ldquo;Once a King or Queen in Narnia, always a King or Queen.&rdquo;', '&ldquo;Once a king or queen in Narnia, always a king or queen.&rdquo;'),
     ('Aslan says this to the children at the end of their story.', 'Aslan says this when he crowns the four children.'),
     ('he has demonstrated honesty, responsibility, courage, service, and perseverance', 'he has shown responsibility, courage, service, and perseverance')],
 4: [('<p>Capitals: <strong>stanley, despereaux, jemmy, lucy, narnia, california, arthur, the, when</strong>.</p>',
      '<p>Capitals: <strong>the &rarr; The, narnia &rarr; Narnia, edmund &rarr; Edmund, witchs &rarr; Witch&rsquo;s</strong> (the White Witch is a name).</p>'),
     ('<p>Possessives: <strong>lucys</strong> &rarr; Lucy&rsquo;s, <strong>stanleys</strong> &rarr; Stanley&rsquo;s, <strong>museums</strong> &rarr; museum&rsquo;s, <strong>despereauxs</strong> &rarr; Despereaux&rsquo;s.</p>',
      '<p>Possessive: <strong>witchs</strong> &rarr; Witch&rsquo;s (the wand belongs to the Witch).</p>'),
     ('<p>Irregular past: <strong>goed</strong> &rarr; went, <strong>runned</strong> &rarr; ran.</p>',
      '<p>Verbs: <strong>was</strong> &rarr; were (four children is more than one), <strong>breaked</strong> &rarr; broke.</p>'),
     ('<p>And a comma before <em>and</em> when it joins two complete thoughts.</p>', '<p>The comma before <em>and</em> is already right: it joins two complete thoughts.</p>'),
     ('This is Jemmy at the very end of <em>The Whipping Boy</em>, realising what the prince actually wanted all along.',
      'This is what Jemmy thinks at the very end of <em>The Whipping Boy</em>, realizing what the prince wanted all along.'),
     ('<div class="info-value">Present — Year-End Celebration</div>', '<div class="info-value">Present and celebrate</div>'),
     ('<div class="activity-sub">Present — Year-End Celebration — master the pattern</div>', '<div class="activity-sub">Roll a word and name its spelling rule.</div>')],
}

def sub1(s, a, b, f):
    n = s.count(a)
    assert n == 1, (f, n, a[:90])
    return s.replace(a, b)

def main(apply):
    for d in (1, 2, 3, 4):
        f = 'lesson-32-%d-ext.html' % d
        s = open(f, encoding='utf-8').read(); o = s
        q, a = QS[d]
        s = sub1(s, QOLD, '&ldquo;%s%s</div>' % (q, '' if q.endswith('air.') else '&rdquo;'), f)
        m = ATTR_RE.findall(s); assert len(m) == 1, (f, 'attr', m)
        s = ATTR_RE.sub(lambda m: m.group(1) + '&mdash; ' + a, s)
        for x, y in (UNIT, PILL, NOW): s = sub1(s, x, y, f)
        assert s.count(EVID) == 3, (f, s.count(EVID))
        for e in EV_PLAN[d]: s = s.replace(EVID, EB % e, 1)
        if d in SPOT:
            assert len(SPOT_RE.findall(s)) == 1, (f, 'spot')
            s = SPOT_RE.sub(lambda m: m.group(1) + spot(SPOT[d]) + m.group(2), s, count=1)
        if d == 1:
            for c, old, new in PILLARS: s = sub1(s, ex(c, old), ex(c, new), f)
            assert len(BANK_RE.findall(s)) == 1 and len(COLS_RE.findall(s)) == 1, (f, 'sort')
            s = BANK_RE.sub(lambda m: BANK, s); s = COLS_RE.sub(lambda m: COLS_NEW, s)
        for x, y in R[d]: s = sub1(s, x, y, f)
        assert s.count('<div') - s.count('</div>') == o.count('<div') - o.count('</div>'), (f, 'div balance')
        print(f, 'ok', len(o), '->', len(s))
        if apply: open(f, 'w', encoding='utf-8').write(s)

if __name__ == '__main__':
    main('--apply' in sys.argv)
