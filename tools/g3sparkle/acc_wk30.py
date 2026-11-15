"""Week 30 (LWW Ch. 16-17 + synthesis) accuracy + wording fixes, approved by Bethany Nov 15 2026 (claude/g3-ela-wk30-audit.md
findings 1-15 + 24 (30.1 decode word parts span broken: "sovereig", no closing tag); 16-23 (check-in) live in the quiz JSON).
Run once on the pre-sparkle files:  python tools/g3sparkle/acc_wk30.py [--apply]"""
import sys, re
def ol(icon, k, t): return '<div class="obj-line"><span class="obj-icon">%s</span><span><strong>%s:</strong> %s</span></div>' % (icon, k, t)
OBJ = {
 1: [('📖','Reading','I will read Ch. 16–17 and explain how the ending shows the theme.'), ('🌱','Word parts','I will name the meanings of roots I learned this year.'),
     ('✏️','Grammar','I will find the words that need a capital letter.'), ('🔤','Spelling','I will sort words by their spelling pattern.'), ('✍️','Writing','I will add proof from the ending to my literary response.')],
 2: [('📖','Reading','I will find moments from across the book that prove the theme.'), ('🌱','Word parts','I will match words to their meanings by their roots.'),
     ('✏️','Grammar','I will find four different kinds of mistakes in one sentence.'), ('🔤','Spelling','I will find silent-e, vowel-team and r-controlled syllables.'), ('✍️','Writing','I will edit my response for capitals and punctuation.')],
 3: [('📖','Reading','I will write a paragraph that tells what the whole book is about.'), ('🌱','Word parts','I will build words from roots and prefixes.'),
     ('✏️','Grammar','I will fix the capitals, apostrophes and comma in a sentence.'), ('🔤','Spelling','I will spell words by their syllable types.'), ('✍️','Writing','I will give my response a title and make one last improvement.')],
 4: [('📖','Reading','I will explain the theme with proof from the whole book.'), ('🌱','Word parts','I will explain how a root changes a word’s meaning.'),
     ('✏️','Grammar','I will fix a short passage in passes.'), ('🔤','Spelling','I will split words and name their syllable types.'), ('✍️','Writing','I will publish my final literary response.')],
}
OBJ_RE = re.compile(r'<div class="obj-line"><span class="obj-icon">📖</span>.*?\n<div class="obj-line"><span class="obj-icon">✏️</span>.*?\n<div class="obj-line"><span class="obj-icon">🔤</span>.*?</span></div>')
QOLD = '&ldquo;Once a King in Narnia, always a King in Narnia.&rdquo;</div>\n  <div class="quote-strip-attr" style="color:#D4AF37;font-size:13px;margin-top:8px;">&mdash; the Professor, back in England, Ch. 17'
QNEW = '&ldquo;%s&rdquo;</div>\n  <div class="quote-strip-attr" style="color:#D4AF37;font-size:13px;margin-top:8px;">&mdash; %s'
QS = {1: ('Bear it well, Sons of Adam! Bear it well, Daughters of Eve!', 'Aslan, Ch. 17'),
      2: ('He had become his real old self again and could look you in the face.', 'C.S. Lewis, about Edmund, Ch. 17'),
      3: ('Long Live King Peter! Long Live Queen Susan! Long Live King Edmund! Long Live Queen Lucy!', 'Ch. 17'),
      4: ('It&rsquo;ll happen when you&rsquo;re not looking for it.', 'the Professor, Ch. 17')}
T2 = 'What Happened About the Statues; The Hunting of the White Stag'
CHAP_OLD = ['What Happened About the Statues; The Hun…', 'Ch. 16–17 + Synthesis — What Happened About the Statues; The Hunting of th']
CHAP_NEW = [T2, 'Ch. 16–17 + Synthesis — ' + T2]
def hw(tip, t): return '<span class="dol-highlight-word" onclick="dolHighlight(this,\'%s\')">%s</span>' % (tip, t)
def sp(w, ok): return '<span class="spotter-word" onclick="gramSpotAll(this,\'gspot1\')" data-correct="%s">%s</span>' % ('true' if ok else 'false', w)
DOL_RE = re.compile(r'(<div class="dol-sentence-wrap" id="dolModel">).*?(</div>)')
SPOT_RE = re.compile(r'(<div class="spotter-sentence" id="gspot1" data-done="false" style="font-family:Georgia,serif;line-height:2.2;">).*?(<div class="spotter-result" id="gspot1-result">)', re.S)
DOL2 = (hw('A capital letter begins every sentence.', 'The') + ' battle was over in a few ' +
        hw('The comma comes before &quot;and&quot; because it joins two complete sentences.', 'minutes,') + ' and ' +
        hw('A name &mdash; capital P.', 'Peter') + ' and ' + hw('A name &mdash; capital A.', 'Aslan') + ' shook ' + hw('A period ends the sentence.', 'hands.'))
SPOT4 = [('the',1),('childrens',1),('coats',0),('were',0),('left',0),('in',0),('narnia.',1),('lucy',1),('was',0),('home',0),('again',1),('and',0),('nobody',0),('knew',0),('she',0),('had',0),('been',0),('gone.',0)]
WHY = '<p style="font-size:13px;color:#7A88A8;font-style:italic;">%s</p>'
FIX = '<div class="dol-sentence-wrap" style="border-left:4px solid #C7922C;">%s</div>'
COR = '<p style="margin-bottom:6px;"><strong>Corrected:</strong> %s</p>'
def ss(w, ok): return '<span class="spotter-word" onclick="spellSpotAll(this,\'spellSpot1\')" data-correct="%s">%s</span>' % ('true' if ok else 'false', w)
COL = '<div class="sort-col"><div class="sort-col-header" style="background:linear-gradient(135deg,%s);">%s</div><div class="sort-col-drop" data-col="%s" onclick="dropSortChip(this,\'%s\')"></div></div>'
COLS_RE = re.compile(r'<div class="sort-col"><div class="sort-col-header" style="background:linear-gradient\(135deg,#1B7A4E,#2EA863\);">Magic-e or vowel team</div>.*?Prefix base-</div><div class="sort-col-drop" data-col="prefix_base" onclick="dropSortChip\(this,\'prefix_base\'\)"></div></div>', re.S)
COLS_NEW = ('\n            '.join([COL % ('#1B7A4E,#2EA863', 'Magic-e', 'magic_e', 'magic_e'), COL % ('#8B6914,#a87f1f', 'Vowel team', 'vowel_team', 'vowel_team'),
                                COL % ('#C7922C,#C7922C', 'Prefix + base word', 'prefix_base', 'prefix_base')]))
POEM_OLD = ('<div class="poem-title">Barter (first stanza)</div>', 'Holding wonder like a cup.</div>')
POEM_NEW = ('<div class="poem-title">Barter (first and last stanzas)</div>',
            'Holding wonder like a cup.\n\nSpend all you have for loveliness,\nBuy it and never count the cost;\nFor one white singing hour of peace\nCount many a year of strife well lost,\nAnd for a breath of ecstasy\nGive all you have been, or could be.</div>')
NOTE_OLD = 'And a face can hold wonder &ldquo;like a cup&rdquo; only if you stretch it, which is closer to <strong>hyperbole</strong>. One short verse, three tools.'
NOTE_NEW = ('Faces &ldquo;holding wonder like a cup&rdquo; is a <strong>simile</strong>: a comparison that uses <em>like</em>. In the last stanza, &ldquo;Give all you have been, or could be&rdquo; stretches far past the truth, which is <strong>hyperbole</strong>. One short poem, three tools.')
R = {
 'lesson-30-1-lww.html': [
  (FIX % 'when the four children were crowned at cair paravel aslan roared and all of narnia celebrated', FIX % 'when the four children were crowned at cair paravel the mermaids sang'),
  (COR % 'When the four children were crowned at Cair Paravel, Aslan roared and all of Narnia celebrated.', COR % 'When the four children were crowned at Cair Paravel, the mermaids sang.'),
  (WHY % 'When begins the dependent clause; Cair Paravel = proper noun (two capitals); comma after Paravel; Aslan and Narnia are proper nouns (capitals); period ends.',
   WHY % 'When begins the opening part; Cair Paravel = a place name (two capitals); comma after Paravel; period ends. (Ch. 17: the mermen and mermaids sang outside the eastern door.)'),
  ('<div class="decode-sentence">&ldquo;Once a King in Narnia, always a King in Narnia.&rdquo;</div>',
   '<div class="decode-sentence">&ldquo;Aslan crowned the four children, and they became the sovereign rulers of all Narnia.&rdquo; <small>(Opti&rsquo;s sentence)</small></div>'),
  ('The Professor says this back in England, after the children come home through the wardrobe. They were crowned at Cair Paravel with full authority over Narnia, and he tells them they are still its kings and queens. Sovereign probably means',
   'Aslan crowns the four children at Cair Paravel, and they rule all of Narnia. Sovereign probably means'),
  ('<div class="decode-word-parts"><span class="decode-part decode-part-affix">sovereig</div>', '<div class="decode-word-parts"><span class="decode-part decode-part-root">sovereign</span></div>'),
  ('data-group="vowel_team" onclick="pickSortChip(this)">roar</span>', 'data-group="vowel_team" onclick="pickSortChip(this)">queen</span>'),
 ],
 'lesson-30-2-lww.html': [
  (FIX % 'the white witch was defeated at last and narnia had four kings and queens for the first time', FIX % 'the white witch was defeated at last and narnia had two kings and two queens'),
  (COR % 'The White Witch was defeated at last, and Narnia had four kings and queens for the first time.', COR % 'The White Witch was defeated at last, and Narnia had two kings and two queens.'),
  ('possessive noun, Week 9.', 'a word that shows belonging, from Week 28.'),
  (ss('stone', 1) + ' ' + ss('table', 0) + ' ' + ss('cracked', 0), ss('battle', 0) + ' ' + ss('ended', 0)),
  (ss('lay', 0), ss('lay', 1)),
  (POEM_OLD[0], POEM_NEW[0]), (POEM_OLD[1], POEM_NEW[1]), (NOTE_OLD, NOTE_NEW),
 ],
 'lesson-30-3-lww.html': [
  ('lucy looked back at the lamp post and she remembered the professors house.', 'the professor believed the childrens story and he didnt laugh at them.'),
 ],
 'lesson-30-4-lww.html': [
  ('>C. S. Lewis</span>', '>C.S. Lewis</span>'),
  ('<div class="task-sentence">the childrens coats hung in the wardrobe.</div>', '<div class="task-sentence">the childrens coats were left in narnia.</div>'),
  ('<div class="task-sentence">lucy told edmund everything and he believed her.</div>', '<div class="task-sentence">lucy was home again and nobody knew she had been gone.</div>'),
  (POEM_OLD[0], POEM_NEW[0]), (POEM_OLD[1], POEM_NEW[1]), (NOTE_OLD, NOTE_NEW),
 ],
}
FDIV = '<div style="font-family:Lora,Georgia,serif;font-size:18px;color:#0E1C42;line-height:2.0;padding:3px 0;">%s</div>'
CHIP = '<span style="display:inline-block;background:#EAF4EE;border:2px solid #B8E0C8;border-radius:20px;padding:4px 12px;font-size:15px;font-weight:700;color:#0E1C42;margin:4px;">%s</span>'
FL_NEW = ['And they themselves grew and changed as the years passed over them.',
 'And Peter became a tall and deep-chested man and a great warrior, and he was called King Peter the Magnificent.',
 'And Susan grew into a tall and gracious woman &hellip; And she was called Susan the Gentle.',
 'Edmund was a graver and quieter man than Peter, and great in council and judgment.',
 'He was called King Edmund the Just.',
 'But as for Lucy, &hellip; her own people called her Queen Lucy the Valiant.']
if __name__ == '__main__':
    dry = '--apply' not in sys.argv
    for day in (1, 2, 3, 4):
        f = 'lesson-30-%d-lww.html' % day
        s = open(f, encoding='utf-8', newline='').read()
        o = s.count('<div') - s.count('</div')
        s, n = OBJ_RE.subn('\n'.join(ol(*x) for x in OBJ[day]), s); assert n == 1, (f, 'obj', n)
        assert s.count(QOLD) == 1, (f, 'quote'); s = s.replace(QOLD, QNEW % QS[day])
        for a, b in zip(CHAP_OLD, CHAP_NEW):
            assert s.count(a) >= 1, (f, a); s = s.replace(a, b)
        if day == 2:
            s, n = DOL_RE.subn(lambda m: m.group(1) + DOL2 + m.group(2), s, count=1); assert n == 1
        if day == 4:
            s, n = SPOT_RE.subn(lambda m: m.group(1) + ' '.join(sp(w, k) for w, k in SPOT4) + m.group(2), s); assert n == 1, (f, 'spot')
        if day == 1:
            s, n = COLS_RE.subn(COLS_NEW, s); assert n == 1, (f, 'cols')
        for old, new in R[f]:
            c = s.count(old); assert c == 1, (f, c, old[:140]); s = s.replace(old, new)
        s = s.replace('Mr and Mrs Beaver', 'Mr. and Mrs. Beaver').replace('Mrs Beaver', 'Mrs. Beaver').replace('Mr Beaver', 'Mr. Beaver').replace('Mr Tumnus', 'Mr. Tumnus')
        assert s.count('<div') - s.count('</div') == o, f
        if not dry: open(f, 'w', encoding='utf-8', newline='').write(s)
        print('ok' if not dry else 'dry-ok', f)
    f = 'lesson-30-fluency.html'; s = open(f, encoding='utf-8', newline='').read(); o = s.count('<div') - s.count('</div')
    m = re.search(r'(border-left:6px solid #D4AF37;">)((?:<div style="font-family:Lora[^>]*>[^<]*</div>)+)', s); assert m and 'crowned at Cair Paravel' in m.group(2), 'passage'
    s = s.replace(m.group(2), ''.join(FDIV % l for l in FL_NEW) + '<div style="font-size:13px;color:#7A88A8;margin-top:8px;">&mdash; C.S. Lewis, <em>The Lion, the Witch and the Wardrobe</em>, Ch. 17</div>')
    old = ''.join(CHIP % w for w in ['crowned','celebrated','gracious','beloved','dignity']); assert s.count(old) == 1, 'chips'
    s = s.replace(old, ''.join(CHIP % w for w in ['magnificent','gracious','council','judgment','valiant']))
    n = s.count('Once a King or Queen'); assert n >= 2, n; s = s.replace('Once a King or Queen', 'Long and Happy Was Their Reign')
    a = "  if (tabId === 'warmup') { intro.classList.remove('collapsed'); }\n  else { intro.classList.add('collapsed'); }"
    assert s.count(a) == 1, 'intro'
    s = s.replace(a, "  if (intro) { if (tabId === 'warmup') { intro.classList.remove('collapsed'); }\n  else { intro.classList.add('collapsed'); } }")
    assert s.count('<div') - s.count('</div') == o
    if not dry: open(f, 'w', encoding='utf-8', newline='').write(s)
    print('ok' if not dry else 'dry-ok', f)
