"""Week 28 (LWW Ch. 10-12) accuracy + wording fixes, approved by Bethany Nov 15 2026 (claude/g3-ela-wk28-audit.md
findings 1-19, 21-22; 20 = note only; 23-27 (check-in) live in the quiz JSON).
Run once on the pre-sparkle files:  python tools/g3sparkle/acc_wk28.py [--dir D] [--apply]"""
import sys, re
def ol(icon, k, t): return '<div class="obj-line"><span class="obj-icon">%s</span><span><strong>%s:</strong> %s</span></div>' % (icon, k, t)
OBJ = {
 1: [('📖','Reading','I will find what Father Christmas and his gifts stand for in Ch. 10.'), ('🌱','Word parts','I will learn that com- and con- mean with or together.'),
     ('✏️','Grammar','I will tell an apostrophe that joins two words from one that shows belonging.'), ('🔤','Spelling','I will learn three ways a base word changes before an ending: double, drop the e, or change y to i.'), ('✍️','Writing','I will write a paragraph about one symbol.')],
 2: [('📖','Reading','I will find symbols and repeated ideas in Ch. 11.'), ('🌱','Word parts','I will match com- and con- words to their meanings.'),
     ('✏️','Grammar','I will find contractions and possessives in sentences.'), ('🔤','Spelling','I will find which change each word made when the ending went on.'), ('✍️','Writing','I will revise my symbol paragraph with more precise words.')],
 3: [('📖','Reading','I will use details from Ch. 12 to explain what Peter&rsquo;s battle means.'), ('🌱','Word parts','I will build com- and con- words from their parts.'),
     ('✏️','Grammar','I will put apostrophes in the right places and say what each one does.'), ('🔤','Spelling','I will build new words with endings using the three changes.'), ('✍️','Writing','I will add my symbol paragraph to my literary response.')],
 4: [('📖','Reading','I will explain what one symbol in Ch. 10&ndash;12 means, with details from the book.'), ('🌱','Word parts','I will explain how com- or con- changes a word.'),
     ('✏️','Grammar','I will fix capitals and apostrophes in a short passage.'), ('🔤','Spelling','I will explain which change a word needs, or none.'), ('✍️','Writing','I will polish my literary response.')],
}
OBJ_RE = re.compile(r'<div class="obj-line"><span class="obj-icon">📖</span>.*?\n<div class="obj-line"><span class="obj-icon">✏️</span>.*?\n<div class="obj-line"><span class="obj-icon">🔤</span>.*?</span></div>')
QOLD = '&ldquo;Wrong will be right, when Aslan comes in sight, at the sound of his roar sorrows will be no more.&rdquo;</div>\n  <div class="quote-strip-attr" style="color:#D4AF37;font-size:13px;margin-top:8px;">&mdash; C.S. Lewis, Ch. 8'
QNEW = '&ldquo;%s&rdquo;</div>\n  <div class="quote-strip-attr" style="color:#D4AF37;font-size:13px;margin-top:8px;">&mdash; %s'
QS = {1: ('Aslan is on the move. The Witch&rsquo;s magic is weakening.', 'Father Christmas, Ch. 10'),
      2: ('This is no thaw. This is Spring.', 'the dwarf, Ch. 11'),
      3: ('His voice was deep and rich and somehow took the fidgets out of them.', 'C.S. Lewis, Ch. 12'),
      4: ('Every moment the patches of green grew bigger and the patches of snow grew smaller.', 'C.S. Lewis, Ch. 11')}
CHAP_OLD = ['The Spell Begins to Break; Aslan is Near…', 'Ch. 10–12 — The Spell Begins to Break; Aslan is Nearer; Peter\'']
CHAP_NEW = ['The Spell Begins to Break; Aslan Is Nearer; Peter&rsquo;s First Battle', 'Ch. 10–12 — The Spell Begins to Break; Aslan Is Nearer; Peter&rsquo;s First Battle']
def hw(tip, t): return '<span class="dol-highlight-word" onclick="dolHighlight(this,\'%s\')">%s</span>' % (tip, t)
def sp(w, ok): return '<span class="spotter-word" onclick="gramSpotAll(this,\'gspot1\')" data-correct="%s">%s</span>' % ('true' if ok else 'false', w)
DOL_RE = re.compile(r'(<div class="dol-sentence-wrap" id="dolModel">).*?(</div>)')
SPOT_RE = re.compile(r'(<div class="spotter-sentence" id="gspot1" data-done="false" style="font-family:Georgia,serif;line-height:2.2;">).*?(<div class="spotter-result" id="gspot1-result">)', re.S)
POSS = 'The apostrophe and s show the %s belongs to %s.'
DOL = {
 4: hw('A contraction of &quot;it is&quot; — not the possessive &quot;its.&quot;', 'It&#x27;s') + ' ' + hw(POSS % ('horn', 'Susan'), 'Susan&#x27;s') + ' ' +
    hw('The comma comes before &quot;and&quot; because it joins two complete sentences.', 'horn,') + ' and Peter ' +
    hw('A contraction of &quot;does not.&quot;', 'doesn&#x27;t') + ' stop to ' + hw('A period ends the sentence.', 'think.'),
}
SPOT = {
 1: [('The',0),('Witchs',1),('sledge',0),('was',0),('fast.',0),('Edmund',0),('didnt',1),('have',0),('a',0),('coat.',0),('Lucys',1),('gift',0),('was',0),('a',0),('little',0),('bottle,',0),('and',0),('Peters',1),('sword',0),('wasnt',1),('too',0),('heavy.',0)],
 4: [('the',1),('witchs',1),('sledge',0),('stuck',0),('in',0),('the',0),('mud,',0),('and',0),('edmund',1),('didnt',1),('get',0),('any',0),('breakfast.',0),('the',1),('childrens',1),('long',0),('walk',0),('ended',0),('at',0),('the',0),('stone',1),('table.',1)],
}
WHY = '<p style="font-size:13px;color:#7A88A8;font-style:italic;">%s</p>'
R = {
 'lesson-28-1-lww.html': [
  ('the robins song wasnt something they had heard before and the creatures of narnia couldnt believe what was happening', 'peters gifts werent toys and lucys bottle looked like glass'),
  ("<strong>Corrected:</strong> The robin's song wasn't something they had heard before, and the creatures of Narnia couldn't believe what was happening.", "<strong>Corrected:</strong> Peter's gifts weren't toys, and Lucy's bottle looked like glass."),
  (WHY % "Robin's = possessive (apostrophe + s); wasn't = was + not (contraction); Narnia = proper noun (capital N); couldn't = could + not (contraction); comma before and; period ends.",
   WHY % "Peter and Lucy are names (capitals); Peter's and Lucy's = possessive (apostrophe + s); weren't = were + not (contraction); comma before and; period ends."),
  ('&ldquo;This is no thaw,&rdquo; said the dwarf, suddenly stopping. &ldquo;This is Spring.&rdquo;', 'After a long sleep and a hot breakfast, Lucy felt renewed and ready to walk again.'),
  ('The snow is melting, animals are waking up, and the world of Narnia is coming back to life. Renewed probably means made fresh and new again.',
   'Lucy was tired and stiff. Sleep and food changed that. Renewed probably means made fresh and new again.'),
  ('As the snow began to melt and green shoots appeared, Narnia felt <input class="fillin-input" id="vcloze1" data-answer="renewed" maxlength="11" placeholder="______"> &mdash; alive again after the long winter.',
   'After a few hours of sleep in the cave, the tired travelers woke up feeling <input class="fillin-input" id="vcloze1" data-answer="renewed" maxlength="11" placeholder="______">.'),
  ('Aslan wore a <input class="fillin-input" id="vcloze3" data-answer="solemn" maxlength="10" placeholder="______"> expression when he returned from the Stone Table, as if he carried a great weight.',
   'When the children saw Father Christmas, they felt very glad, but also <input class="fillin-input" id="vcloze3" data-answer="solemn" maxlength="10" placeholder="______">.'),
  ('Chapters 10 and 11 are some of the most hopeful in the book. In Ch. 10, Father Christmas arrives. In Ch. 11, the snow begins to melt and spring comes to Narnia. Lewis fills these chapters with symbols — things that represent bigger ideas. As you read, ask: what does the thaw represent?',
   'Chapter 10 is one of the most hopeful in the book. The Beavers and the children escape in the night, and in the morning Father Christmas arrives. Lewis fills this chapter with symbols — things that represent bigger ideas. As you read, ask: what does his arrival stand for?'),
  ('<div class="activity-title">Q1 — The Thaw</div>', '<div class="activity-title">Q1 — Father Christmas&rsquo;s News</div>'),
  ('In Ch. 11, the snow begins to melt and spring arrives. What do you think the thaw represents — what bigger idea might it stand for?',
   'Father Christmas says, &ldquo;Aslan is on the move. The Witch&rsquo;s magic is weakening.&rdquo; What do you think his arrival represents &mdash; what bigger idea might it stand for?'),
  ("Clara's rough try: The thaw means winter is over. That is good for Narnia.", "Clara's rough try: Father Christmas came. That is good for Narnia."),
  ("Clara's revised paragraph: Lewis uses the thawing snow as a symbol of hope. When the snow begins to melt in Ch. 11, it is not just a change in weather — it represents the end of the Witch's cruel power over Narnia. Lewis links the thaw directly to Aslan's return, suggesting that goodness and warmth are the same thing in this story.",
   "Clara's revised paragraph: Lewis uses Father Christmas as a symbol of hope. For a hundred years the Witch kept him out, so it was always winter and never Christmas. When he finally arrives in Ch. 10, he says the Witch's magic is weakening. His arrival shows that her power is starting to crack."),
  ("Write 2–3 sentences about one symbol from Ch. 10–12.", "Write 2–3 sentences about one symbol from Ch. 10."),
 ],
 'lesson-28-2-lww.html': [
  ('the witchs sledge couldnt move because the snow had melted and her reindeers hooves sank in the mud', 'the witchs sledge couldnt move in the thaw and the dwarf cut the reindeers harness'),
  ("<strong>Corrected:</strong> The Witch's sledge couldn't move because the snow had melted, and her reindeer's hooves sank in the mud.", "<strong>Corrected:</strong> The Witch's sledge couldn't move in the thaw, and the dwarf cut the reindeer's harness."),
  ("Witch's = possessive; couldn't = contraction (could not); comma before and; reindeer's = possessive; period ends.", "The begins the sentence; Witch's = possessive; couldn't = contraction (could not); comma before and; reindeer's = possessive (the harness belongs to the reindeer); period ends."),
  ("Edmund couldn't remember the way to the castle.", "Edmund couldn't hear the running water at first."),
  ('<p>contraction and possessive</p>\n<p>possessive and contraction</p>\n<p>possessive and contraction</p>', '<p>contraction and possessive</p>\n<p>possessive and contraction</p>\n<p>contraction only</p>'),
  ('Tap <strong>every</strong> word that is wrong. One of these is not about apostrophes at all.', 'Tap <strong>every</strong> word that is wrong. Some mistakes are apostrophes. Others are capitals, a missing comma, or a word for more than one.'),
  ('<div class="swyk-prompt">Which mistake was not about apostrophes? What was it about?</div>', '<div class="swyk-prompt">Which mistakes were not about apostrophes? What were they about?</div>'),
  ('<div class="activity-sub">Identify the pattern by ear.</div>', '<div class="activity-sub">Find the word that changed.</div>'),
  (' Near the end of this week&rsquo;s reading, Aslan sends a rescue party to save Edmund from the Witch.', ''),
  ('The party has left the Beavers&rsquo; house and set off for the Stone Table. What is the night like as they go?',
   'This is from Chapter 10. The party has left the Beavers&rsquo; house and set off for the Stone Table. What is the night like as they go?'),
 ],
 'lesson-28-3-lww.html': [
  ('Aslan wore a <select id="vocab_sel_1"', 'When the children looked at Aslan, they saw his great, royal, <select id="vocab_sel_1"'),
  ('</select> expression when he spoke about the Deep Magic.', '</select> eyes.'),
  ('The robin had been a <select id="vocab_sel_2"', 'The jingling bells were a <select id="vocab_sel_2"'),
  ('</select> of spring, arriving just before the snow began to melt.', '</select> of Father Christmas, ringing just before he appeared.'),
  ('The childrens coats wouldnt fit inside the witchs sleigh.', 'The childrens coats werent needed once the Witchs winter melted.'),
  ('<li>List the changes. How many are capitals? How many are punctuation?</li>', '<li>How many apostrophes did the editor add? Which one joins two words?</li>'),
 ],
 'lesson-28-4-lww.html': [
  ('<p>Capitals: <strong>the, aslan, edmund, the</strong> &mdash; sentence starts and names.</p>', '<p>Capitals: <strong>the, edmund, the, stone table</strong> &mdash; sentence starts, a name and a place name.</p>'),
  ('The party is leaving the Beavers&rsquo; house in a hurry, in the dark, with the Witch coming. How does Lewis show you the group setting off?',
   'This is from Chapter 10. The party is leaving the Beavers&rsquo; house in a hurry, in the dark, with the Witch coming. How does Lewis show you the group setting off?'),
 ],
}
FDIV = '<div style="font-family:Lora,Georgia,serif;font-size:18px;color:#0E1C42;line-height:2.0;padding:3px 0;">%s</div>'
CHIP = '<span style="display:inline-block;background:#EAF4EE;border:2px solid #B8E0C8;border-radius:20px;padding:4px 12px;font-size:15px;font-weight:700;color:#0E1C42;margin:4px;">%s</span>'
FL_NEW = ['Every moment the patches of green grew bigger and the patches of snow grew smaller.',
 'Every moment more and more of the trees shook off their robes of snow.',
 'Soon, wherever you looked, instead of white shapes you saw the dark green of firs or the black prickly branches of bare oaks and beeches and elms.',
 'Then the mist turned from white to gold and presently cleared away altogether.',
 'Shafts of delicious sunlight struck down on to the forest floor and overhead you could see a blue sky between the tree tops.',
 'Soon there were more wonderful things happening.',
 'Coming suddenly round a corner into a glade of silver birch trees Edmund saw the ground covered in all directions with little yellow flowers &ndash; celandines.']
FL_FOCUS_NEW = 'Read the two &ldquo;Every moment&rdquo; sentences a little faster each time, like the thaw speeding up. Slow down for the sunlight and the flowers.'
if __name__ == '__main__':
    dry = '--apply' not in sys.argv
    d = sys.argv[sys.argv.index('--dir') + 1] + '/' if '--dir' in sys.argv else ''
    for day in (1, 2, 3, 4):
        f = 'lesson-28-%d-lww.html' % day
        s = open(d + f, encoding='utf-8', newline='').read()
        o = s.count('<div') - s.count('</div')
        s, n = OBJ_RE.subn('\n'.join(ol(*x) for x in OBJ[day]), s); assert n == 1, (f, 'obj', n)
        assert s.count(QOLD) == 1, (f, 'quote'); s = s.replace(QOLD, QNEW % QS[day])
        for a, b in zip(CHAP_OLD, CHAP_NEW):
            assert s.count(a) >= 1, (f, a); s = s.replace(a, b)
        if day in DOL:
            s, n = DOL_RE.subn(lambda m: m.group(1) + DOL[day] + m.group(2), s, count=1); assert n == 1, (f, 'dol')
        if day in SPOT:
            s, n = SPOT_RE.subn(lambda m: m.group(1) + ' '.join(sp(w, k) for w, k in SPOT[day]) + m.group(2), s); assert n == 1, (f, 'spot')
        for old, new in R[f]:
            c = s.count(old); assert c == 1, (f, c, old[:140]); s = s.replace(old, new)
        k = s.count('Mr Beaver') + s.count('Mrs Beaver')
        s = s.replace('Mr and Mrs Beaver', 'Mr. and Mrs. Beaver').replace('Mrs Beaver', 'Mrs. Beaver').replace('Mr Beaver', 'Mr. Beaver')
        assert s.count('<div') - s.count('</div') == o, f
        if not dry: open(d + f, 'w', encoding='utf-8', newline='').write(s)
        print('ok' if not dry else 'dry-ok', f, len(R[f]) + 3, 'Mr.', k)
    f = 'lesson-28-fluency.html'; s = open(d + f, encoding='utf-8', newline='').read(); o = s.count('<div') - s.count('</div')
    m = re.search(r'(border-left:6px solid #D4AF37;">)((?:<div style="font-family:Lora[^>]*>[^<]*</div>)+)', s); assert m and 'icicle' in m.group(2), 'passage'
    s = s.replace(m.group(2), ''.join(FDIV % l for l in FL_NEW) + '<div style="font-size:13px;color:#7A88A8;margin-top:8px;">&mdash; C.S. Lewis, <em>The Lion, the Witch and the Wardrobe</em>, Ch. 11</div>')
    old = ''.join(CHIP % w for w in ['icicle','appeared','patches','somewhere']); assert s.count(old) == 1, 'chips'
    s = s.replace(old, ''.join(CHIP % w for w in ['prickly','presently','delicious','glade','celandines']))
    n = 0
    for fo in ('Start slow and quiet. Build pace and energy as the thaw takes hold. End in silence.',):
        n += s.count(fo); s = s.replace(fo, FL_FOCUS_NEW)
    assert n >= 2, n
    n = s.count('The Thaw Begins'); s = s.replace('The Thaw Begins', 'Green Patches'); assert n >= 2, n
    a = "  if (tabId === 'warmup') { intro.classList.remove('collapsed'); }\n  else { intro.classList.add('collapsed'); }"
    assert s.count(a) == 1, 'intro'
    s = s.replace(a, "  if (intro) { if (tabId === 'warmup') { intro.classList.remove('collapsed'); }\n  else { intro.classList.add('collapsed'); } }")
    assert s.count('<div') - s.count('</div') == o
    if not dry: open(d + f, 'w', encoding='utf-8', newline='').write(s)
    print('ok' if not dry else 'dry-ok', f)
