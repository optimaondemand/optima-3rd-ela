"""Week 29 (LWW Ch. 13-15) accuracy + wording fixes, approved by Bethany Nov 15 2026 (claude/g3-ela-wk29-audit.md
findings 1-22, with #5 = move "resurrection" from 29.2 to 29.3; 23-29 (check-in) live in the quiz JSON).
Run once on the pre-sparkle files:  python tools/g3sparkle/acc_wk29.py [--dir D] [--apply]"""
import sys, re
def ol(icon, k, t): return '<div class="obj-line"><span class="obj-icon">%s</span><span><strong>%s:</strong> %s</span></div>' % (icon, k, t)
OBJ = {
 1: [('📖','Reading','I will find big ideas forming in Ch. 13 and tell a topic from a theme.'), ('🌱','Word parts','I will learn that the root ject means throw.'),
     ('✏️','Grammar','I will put quotation marks, commas and capitals in the right places when someone speaks.'), ('🔤','Spelling','I will find the root and the parts added to long words.'), ('✍️','Writing','I will brainstorm two or three possible themes.')],
 2: [('📖','Reading','I will find moments in Ch. 14 that support a theme.'), ('🌱','Word parts','I will match ject words to their meanings.'),
     ('✏️','Grammar','I will find and fix dialogue mistakes in sentences.'), ('🔤','Spelling','I will find words built from a root with parts added.'), ('✍️','Writing','I will draft my literary response on theme.')],
 3: [('📖','Reading','I will use details from Ch. 15 to make my theme response stronger.'), ('🌱','Word parts','I will build ject words from their parts.'),
     ('✏️','Grammar','I will fix a line of dialogue and list what I changed.'), ('🔤','Spelling','I will spell long words by finding the root first.'), ('✍️','Writing','I will revise my response with evidence from Ch. 15.')],
 4: [('📖','Reading','I will explain how my theme grows from the start of the book to Ch. 15.'), ('🌱','Word parts','I will explain how a prefix changes a ject word.'),
     ('✏️','Grammar','I will fix capitals, apostrophes, commas and dialogue in a short passage.'), ('🔤','Spelling','I will name the root and the added parts of long words.'), ('✍️','Writing','I will finish my literary response on theme.')],
}
OBJ_RE = re.compile(r'<div class="obj-line"><span class="obj-icon">📖</span>.*?\n<div class="obj-line"><span class="obj-icon">✏️</span>.*?\n<div class="obj-line"><span class="obj-icon">🔤</span>.*?</span></div>')
QOLD = '&ldquo;Though the Witch knew the Deep Magic, there is a magic deeper still which she did not know.&rdquo;</div>\n  <div class="quote-strip-attr" style="color:#D4AF37;font-size:13px;margin-top:8px;">&mdash; Aslan, Ch. 15'
QNEW = '&ldquo;%s&rdquo;</div>\n  <div class="quote-strip-attr" style="color:#D4AF37;font-size:13px;margin-top:8px;">&mdash; %s'
QS = {1: ('There is no need to talk to him about what is past.', 'Aslan, Ch. 13'),
      2: ('Lay your hands on my mane so that I can feel you are there.', 'Aslan, Ch. 14'),
      3: ('It was such a romp as no one has ever had except in Narnia.', 'C.S. Lewis, Ch. 15'),
      4: ('Though the Witch knew the Deep Magic, there is a magic deeper still which she did not know.', 'Aslan, Ch. 15')}
T3 = 'Deep Magic From the Dawn of Time; The Triumph of the Witch; Deeper Magic From Before the Dawn of Time'
CHAP_OLD = ['Deep Magic From the Dawn of Time; The Tr…', 'Ch. 13–15 — Deep Magic From the Dawn of Time; The Triumph of t']
CHAP_NEW = [T3, 'Ch. 13–15 — ' + T3]
def hw(tip, t): return '<span class="dol-highlight-word" onclick="dolHighlight(this,\'%s\')">%s</span>' % (tip, t)
def sp(w, ok): return '<span class="spotter-word" onclick="gramSpotAll(this,\'gspot1\')" data-correct="%s">%s</span>' % ('true' if ok else 'false', w)
DOL_RE = re.compile(r'(<div class="dol-sentence-wrap" id="dolModel">).*?(</div>)')
SPOT_RE = re.compile(r'(<div class="spotter-sentence" id="gspot1" data-done="false" style="font-family:Georgia,serif;line-height:2.2;">).*?(<div class="spotter-result" id="gspot1-result">)', re.S)
OPEN = 'The opening quotation mark, and a capital letter for the first word of the speech.'
CIN = 'The comma goes INSIDE the closing quotation mark.'
DOL = {
 1: hw(OPEN, '&quot;Let') + ' him ' + hw(CIN, 'approach,&quot;') + ' said ' + hw('A name (capital A). The dialogue tag ends with a period.', 'Aslan.'),
 2: hw(OPEN, '&quot;We') + ' couldn&#x27;t ' + hw(CIN, 'sleep,&quot;') + ' said ' + hw('A name (capital L). The dialogue tag ends with a period.', 'Lucy.'),
 3: hw(OPEN, '&quot;And') + ' ' + hw(CIN, 'now,&quot;') + ' said Aslan ' + hw('A comma after the dialogue tag, because the same sentence of speech keeps going.', 'presently,') + ' ' +
    hw('A quotation mark reopens the speech, but &quot;to&quot; stays lowercase because it continues the same sentence.', '&quot;to') + ' ' + hw('The period goes INSIDE the closing quotation mark.', 'business.&quot;'),
 4: hw(OPEN, '&quot;Fall') + ' back, all of ' + hw(CIN, 'you,&quot;') + ' said ' + hw('A name (capital A), and a comma after the tag because the speech continues.', 'Aslan,') + ' ' +
    hw('Lowercase &quot;and&quot; &mdash; the second half continues the same spoken sentence.', '&quot;and') + ' I will talk to the Witch ' + hw('The period goes INSIDE the closing quotation mark.', 'alone.&quot;'),
}
SPOT = {
 1: [('"It\'ll',0),('be',0),('all',0),('right",',1),('whispered',0),('Peter.',0),('"I',0),('have',0),('settled',0),('the',0),('matter",',1),('said',0),('Aslan.',0),('"but',1),('how',0),('do',0),('I',0),('know',0),('this',0),('promise',0),('will',0),('be',0),('kept?"',0),('asked',0),('the',0),('Witch.',0)],
 2: [('"we',1),('couldnt',1),('sleep,"',0),('said',0),('lucy.',1),('aslan',1),('was',0),('sad',0),('and',0),('lonely',1),('and',0),('susan',1),('held',0),('his',0),('mane.',0)],
 4: [('"i',1),('think',0),('theyre',1),('friendly',0),('mice,"',0),('said',0),('lucy.',1),('susans',1),('hand',0),('was',0),('cold',1),('and',0),('the',0),('mice',0),('didnt',1),('stop',0),('nibbling.',0)],
}
WHY = '<p style="font-size:13px;color:#7A88A8;font-style:italic;">%s</p>'
FIX = '<div class="dol-sentence-wrap" style="border-left:4px solid #C7922C;">%s</div>'
COR = '<p style="margin-bottom:6px;"><strong>Corrected:</strong> %s</p>'
GS = '<div style="font-family:Lora,serif;font-size:15px;color:#0E1C42;margin-bottom:6px;">%s</div>'
R = {
 'lesson-29-1-lww.html': [
  (FIX % '"what do you want" said the witch and she looked hard at aslan', FIX % '"have you forgotten the deep magic" asked the witch'),
  (COR % '"What do you want?" said the Witch, and she looked hard at Aslan.', COR % '"Have you forgotten the Deep Magic?" asked the Witch.'),
  (WHY % 'Opening quotation mark before What; capital W for the first word of speech; question mark inside the closing quotation mark; Witch and Aslan are proper nouns (capitals); comma after the dialogue tag Witch; period ends.',
   WHY % 'Opening quotation mark before Have; capital H for the first word of speech; question mark inside the closing quotation mark; Deep Magic and Witch are names (capitals); period ends. (Ch. 13)'),
  ('"Mr Tumnus is in trouble," said Lucy.', '"Let him approach," said Aslan.'),
  ('Aslan made the greatest <input class="fillin-input" id="vcloze3" data-answer="sacrifice" maxlength="13" placeholder="______"> a leader can make &mdash; giving up his own life for someone else&rsquo;s.',
   'Mom made a <input class="fillin-input" id="vcloze3" data-answer="sacrifice" maxlength="13" placeholder="______"> when she gave up her free Saturday to help at the food bank.'),
  ('(1) The story shows that sacrifice can free someone from the consequences of their own choices.', '(1) The story shows that forgiveness can give someone a fresh start.'),
  ('what does this moment say about justice, and about sacrifice?', 'what does this moment say about justice, and about forgiveness?'),
  ('What might the story be saying about sacrifice or love?', 'What might the story be saying about forgiveness or loyalty?'),
 ],
 'lesson-29-2-lww.html': [
  (FIX % '"why are you here" demanded the witch "this is my table"', FIX % '"where is he now" said lucy "is he here in the pavilion"'),
  (COR % '"Why are you here?" demanded the Witch. "This is my table."', COR % '"Where is he now?" said Lucy. "Is he here in the pavilion?"'),
  (WHY % 'Capital W for Why (first word of speech); question mark inside the quotation mark; Witch is a proper noun (capital W); period ends the first piece of dialogue; new opening quotation mark begins the second; capital T for This; period inside the final quotation mark.',
   WHY % 'Capital W for Where (first word of speech); question mark inside the quotation mark; Lucy is a name (capital L); a period ends the tag; a new quotation mark begins the second question; capital I for Is; question mark inside the final quotation mark. (Ch. 14)'),
  (GS % '"aslan is here," said Susan quietly.', GS % '"i&rsquo;ve a most horrible feeling," said Lucy.'),
  (GS % '"he is not safe." Mr. Beaver replied.', GS % '"Where is he now?" said lucy.'),
  (GS % '"but he is good." added Mr. Beaver.', GS % '"We couldn&rsquo;t sleep." said Lucy.'),
  (GS % '"The Stone Table has broken!" Lucy cried.', GS % '"Are you ill, dear Aslan?" asked Susan.'),
  ('<p>Aslan — capital A is needed for the proper noun inside speech.</p>\n<p>He — capital H needed as the first word of speech.</p>\n<p>But — capital B needed as the first word of speech.</p>\n<p>Already correct — capital T, exclamation inside quotation mark.</p>',
   '<p>I&rsquo;ve &mdash; capital I needed as the first word of speech.</p>\n<p>Lucy &mdash; capital L needed for a name in the dialogue tag.</p>\n<p>sleep, &mdash; a comma, not a period, goes inside the quotation mark when the tag comes next.</p>\n<p>Already correct &mdash; capital A, question mark inside the quotation mark.</p>'),
  ('<div class="match-item is-word" data-match="D" onclick="matchClick(this)">resurrection</div><div class="match-item" data-match="D" onclick="matchClick(this)">Coming back to life after death.</div>', ''),
  ('The Witch is gathering her army before the battle. Who does she send for?', 'This is from Chapter 13. The Witch says, &ldquo;We will fight.&rdquo; Who does she send for?'),
 ],
 'lesson-29-3-lww.html': [
  (FIX % '"the stone table is broken" said lucy "and aslan is alive"', FIX % '"oh children" said the lion "i feel my strength coming back to me"'),
  (COR % '"The Stone Table is broken," said Lucy, "and Aslan is alive!"', COR % '"Oh, children," said the Lion, "I feel my strength coming back to me."'),
  (WHY % 'Capital T for The (first word of speech); Stone Table = proper noun (capitals); comma inside the quotation mark after broken; dialogue tag said Lucy with comma; second speech continues lowercase and; Aslan is a proper noun; exclamation inside the final quotation mark.',
   WHY % 'Capital O for Oh (first word of speech); comma after Oh; comma inside the quotation mark after children; the Lion is Aslan&rsquo;s title (capital L); comma after the tag; I is always a capital; period inside the final quotation mark. (Ch. 15)'),
  ('his actions in the final battle would begin to do that.', 'Saying sorry was only a start.'),
  ('<div style="font-style:italic;font-size:13px;margin-top:4px;">"we must go to aslan", said Peter.</div>', '<div style="font-style:italic;font-size:13px;margin-top:4px;">"i&rsquo;m so cold", said Lucy.</div>'),
  ('<div style="font-size:13px;margin-top:4px;">&ldquo;We must go to Aslan,&rdquo; said Peter.</div>', '<div style="font-size:13px;margin-top:4px;">&ldquo;I&rsquo;m so cold,&rdquo; said Lucy.</div>'),
  ('"the witch wants edmund", susan whispered.', '"lets walk about a bit", said susan.'),
 ],
 'lesson-29-4-lww.html': [
  (FIX % '"the deeper magic is older than time" aslan told them "and it is what will save narnia"', FIX % '"itll be all right" whispered peter "he wouldnt send them if it werent"'),
  (COR % '"The Deeper Magic is older than time," Aslan told them, "and it is what will save Narnia."', COR % '"It\'ll be all right," whispered Peter. "He wouldn\'t send them if it weren\'t."'),
  (WHY % 'Capital T for The; Deeper Magic = proper noun (capitals); comma inside quotation mark; Aslan = proper noun; comma after them for the split dialogue tag; second piece continues lowercase and; Narnia = proper noun; period inside the final quotation mark.',
   WHY % 'Capital I for It&rsquo;ll; apostrophes in It&rsquo;ll, wouldn&rsquo;t and weren&rsquo;t; comma inside the quotation mark; Peter is a name; a period ends the tag; a new quotation mark and capital H start the second sentence; period inside the final quotation mark. (Ch. 13)'),
  ('<p>Speech starts with a capital letter, like any sentence: <strong>"run</strong> &rarr; &ldquo;Run. (<strong>"and</strong> stays lowercase &mdash; it continues the same spoken sentence.)</p>\n<p>Names take capitals: <strong>lucy, peters, susan</strong>.</p>\n<p>Apostrophes: <strong>peters</strong> &rarr; Peter&rsquo;s, <strong>didnt</strong> &rarr; didn&rsquo;t, <strong>dont</strong> &rarr; don&rsquo;t.</p>\n<p>A comma goes after <strong>ready</strong>, before <em>and</em>, in the last sentence, because it joins two complete thoughts.</p>',
   '<p>Speech starts with a capital letter, like any sentence: <strong>"i</strong> &rarr; &ldquo;I.</p>\n<p>Names take capitals: <strong>lucy, susans</strong>.</p>\n<p>Apostrophes: <strong>theyre</strong> &rarr; they&rsquo;re, <strong>susans</strong> &rarr; Susan&rsquo;s, <strong>didnt</strong> &rarr; didn&rsquo;t.</p>\n<p>A comma goes after <strong>cold</strong>, before <em>and</em>, because it joins two complete thoughts.</p>'),
  ('Choose from: <strong>traitor</strong>, <strong>atone</strong>, <strong>sacrifice</strong>', 'Choose from: <strong>traitor</strong>, <strong>atone</strong>, <strong>sacrifice</strong>, <strong>resurrection</strong>'),
  ('This is Ch. 13. In a dark valley, Edmund is tied to a tree, and the Witch takes off her mantle because she is about to kill him. How does this sentence make you feel about what she is going to do?',
   'This is from Chapter 13. In a dark valley, Edmund is tied to a tree and the Witch takes off her cloak. (Aslan&rsquo;s rescuers arrive moments later.) How does this sentence make you feel?'),
  ('the theme is proven from the very first chapter to the very last.', 'the theme is proven from the first chapter all the way to Chapter 15.'),
 ],
}
SEL = '<select id="vocab_sel_%d" onchange="checkVocabSel(%d,\'%s\')" style="padding:4px 8px;border:2px solid #1B7A4E;border-radius:8px;font-family:Nunito,sans-serif;font-size:15px;cursor:pointer;"><option value="-- choose --">-- choose --</option><option value="atone">atone</option><option value="traitor">traitor</option><option value="sacrifice">sacrifice</option>'
BOX = '            <div style="padding:12px 16px;background:#fff;border:2px solid #E2E8F4;border-radius:12px;margin-bottom:12px;font-size:16px;color:#0E1C42;line-height:1.7;">\n'
FDIV = '<div style="font-family:Lora,Georgia,serif;font-size:18px;color:#0E1C42;line-height:2.0;padding:3px 0;">%s</div>'
CHIP = '<span style="display:inline-block;background:#EAF4EE;border:2px solid #B8E0C8;border-radius:20px;padding:4px 12px;font-size:15px;font-weight:700;color:#0E1C42;margin:4px;">%s</span>'
FL_NEW = ['Forward they went again and one of the girls walked on each side of the Lion.',
 'But how slowly he walked!',
 'And his great, royal head drooped so that his nose nearly touched the grass.',
 'Presently he stumbled and gave a low moan.',
 '&ldquo;Aslan! Dear Aslan!&rdquo; said Lucy, &ldquo;what is wrong? Can&rsquo;t you tell us?&rdquo;',
 '&ldquo;Are you ill, dear Aslan?&rdquo; asked Susan.',
 '&ldquo;No,&rdquo; said Aslan. &ldquo;I am sad and lonely. Lay your hands on my mane so that I can feel you are there and let us walk like that.&rdquo;']
FL_FOCUS_OLD = 'Read quietly and slowly. Every pause matters. This passage is about dread and waiting.'
FL_FOCUS_NEW = 'Read slowly and gently. Pause at every period. Let Lucy and Susan sound worried, and let Aslan&rsquo;s answer sound quiet.'
if __name__ == '__main__':
    dry = '--apply' not in sys.argv
    d = sys.argv[sys.argv.index('--dir') + 1] + '/' if '--dir' in sys.argv else ''
    for day in (1, 2, 3, 4):
        f = 'lesson-29-%d-lww.html' % day
        s = open(d + f, encoding='utf-8', newline='').read()
        o = s.count('<div') - s.count('</div')
        s, n = OBJ_RE.subn('\n'.join(ol(*x) for x in OBJ[day]), s); assert n == 1, (f, 'obj', n)
        assert s.count(QOLD) == 1, (f, 'quote'); s = s.replace(QOLD, QNEW % QS[day])
        for a, b in zip(CHAP_OLD, CHAP_NEW):
            assert s.count(a) >= 1, (f, a); s = s.replace(a, b)
        s, n = DOL_RE.subn(lambda m: m.group(1) + DOL[day] + m.group(2), s, count=1); assert n == 1, (f, 'dol')
        if day in SPOT:
            s, n = SPOT_RE.subn(lambda m: m.group(1) + ' '.join(sp(w, k) for w, k in SPOT[day]) + m.group(2), s); assert n == 1, (f, 'spot')
        for old, new in R[f]:
            c = s.count(old); assert c == 1, (f, c, old[:140]); s = s.replace(old, new)
        if day == 2:
            assert s.count('matchCount >= 4') == 3; s = s.replace('matchCount >= 4', 'matchCount >= 3')
        if day == 3:
            for i, a in ((0, 'atone'), (1, 'sacrifice'), (2, 'traitor')):
                old = SEL % (i, i, a); assert s.count(old) == 1, (f, 'sel', i)
                s = s.replace(old, old + '<option value="resurrection">resurrection</option>')
            anchor = '              <span id="vocab_fb_2" style="margin-left:8px;font-size:14px;font-weight:700;"></span>\n            </div>\n'
            assert s.count(anchor) == 1
            s = s.replace(anchor, anchor + BOX + '              The girls could hardly believe Aslan&rsquo;s ' + SEL % (3, 3, 'resurrection') +
                '<option value="resurrection">resurrection</option></select> when he stood before them, alive, in the sunrise.\n              <span id="vocab_fb_3" style="margin-left:8px;font-size:14px;font-weight:700;"></span>\n            </div>\n')
        k = s.count('Mr Beaver') + s.count('Mrs Beaver')
        s = s.replace('Mr and Mrs Beaver', 'Mr. and Mrs. Beaver').replace('Mrs Beaver', 'Mrs. Beaver').replace('Mr Beaver', 'Mr. Beaver')
        assert s.count('<div') - s.count('</div') == o, f
        if not dry: open(d + f, 'w', encoding='utf-8', newline='').write(s)
        print('ok' if not dry else 'dry-ok', f, len(R[f]) + 3, 'Mr.', k)
    f = 'lesson-29-fluency.html'; s = open(d + f, encoding='utf-8', newline='').read(); o = s.count('<div') - s.count('</div')
    m = re.search(r'(border-left:6px solid #D4AF37;">)((?:<div style="font-family:Lora[^>]*>[^<]*</div>)+)', s); assert m and 'Stone Table stood' in m.group(2), 'passage'
    s = s.replace(m.group(2), ''.join(FDIV % l for l in FL_NEW) + '<div style="font-size:13px;color:#7A88A8;margin-top:8px;">&mdash; C.S. Lewis, <em>The Lion, the Witch and the Wardrobe</em>, Ch. 14</div>')
    old = ''.join(CHIP % w for w in ['ancient','frightening','prepared','together','overhead']); assert s.count(old) == 1, 'chips'
    s = s.replace(old, ''.join(CHIP % w for w in ['royal','drooped','stumbled','moan','lonely']))
    n = s.count(FL_FOCUS_OLD); assert n >= 2, n; s = s.replace(FL_FOCUS_OLD, FL_FOCUS_NEW)
    n = s.count('The Stone Table<'); assert n >= 2, n; s = s.replace('The Stone Table<', 'Sad and Lonely<')
    s = s.replace('&mdash; The Stone Table', '&mdash; Sad and Lonely')
    a = "  if (tabId === 'warmup') { intro.classList.remove('collapsed'); }\n  else { intro.classList.add('collapsed'); }"
    assert s.count(a) == 1, 'intro'
    s = s.replace(a, "  if (intro) { if (tabId === 'warmup') { intro.classList.remove('collapsed'); }\n  else { intro.classList.add('collapsed'); } }")
    assert s.count('<div') - s.count('</div') == o
    if not dry: open(d + f, 'w', encoding='utf-8', newline='').write(s)
    print('ok' if not dry else 'dry-ok', f)
