"""Week 27 (LWW Ch. 7-9) accuracy + wording fixes, approved by Bethany Nov 14 2026 (claude/g3-ela-wk27-audit.md
findings 1-15, 17-21). 16 (27.3 grammar Think/Check yourself) is plain_wk27.py; 22-26 (check-in) live in the quiz JSON.
Run once on the pre-sparkle files:  python tools/g3sparkle/acc_wk27.py [--dir D] [--apply]"""
import sys, re
def ol(icon, k, t): return '<div class="obj-line"><span class="obj-icon">%s</span><span><strong>%s:</strong> %s</span></div>' % (icon, k, t)
OBJ = {
 1: [('📖','Reading','I will tell how different characters feel when they hear Aslan’s name in Ch. 7.'), ('🌱','Word parts','I will learn that in- and im- mean not.'),
     ('✏️','Grammar','I will find past-tense verbs that do not use -ed.'), ('🔤','Spelling','I will peel a prefix off a base word to read it.'), ('✍️','Writing','I will plan a short response comparing two characters.')],
 2: [('📖','Reading','I will find clues in Ch. 8 that show what Edmund is thinking.'), ('🌱','Word parts','I will match in- and im- words to their meanings.'),
     ('✏️','Grammar','I will fix irregular past-tense verbs in sentences.'), ('🔤','Spelling','I will find the prefix and base word in longer words.'), ('✍️','Writing','I will draft my comparison.')],
 3: [('📖','Reading','I will use details from Ch. 9 to explain how Edmund sees the Witch.'), ('🌱','Word parts','I will build in- and im- words from their parts.'),
     ('✏️','Grammar','I will write irregular past-tense verbs correctly.'), ('🔤','Spelling','I will fix misspelled prefix words.'), ('✍️','Writing','I will revise my comparison with more precise words.')],
 4: [('📖','Reading','I will explain what Edmund’s and Lucy’s different views show.'), ('🌱','Word parts','I will explain how in- or im- changes a word.'),
     ('✏️','Grammar','I will fix capitals, an apostrophe, a comma and verbs in a passage.'), ('🔤','Spelling','I will explain the prefix and base in new words.'), ('✍️','Writing','I will publish my comparison.')],
}
OBJ_RE = re.compile(r'<div class="obj-line"><span class="obj-icon">📖</span>.*?\n<div class="obj-line"><span class="obj-icon">✏️</span>.*?\n<div class="obj-line"><span class="obj-icon">🔤</span>.*?</span></div>')
QOLD = '&ldquo;They say Aslan is on the move — perhaps has already landed.&rdquo;</div>\n  <div class="quote-strip-attr" style="color:#D4AF37;font-size:13px;margin-top:8px;">&mdash; Mr Beaver, Ch. 7'
QNEW = '&ldquo;%s&rdquo;</div>\n  <div class="quote-strip-attr" style="color:#D4AF37;font-size:13px;margin-top:8px;">&mdash; %s'
QS = {1: ('They say Aslan is on the move — perhaps has already landed.', 'Mr. Beaver, Ch. 7'),
      2: ('Aslan is a lion — the Lion, the great Lion.', 'Mr. Beaver, Ch. 8'),
      3: ('But it was too late to think of turning back now.', 'C.S. Lewis, Ch. 9'),
      4: ('Edmund felt a sensation of mysterious horror.', 'C.S. Lewis, Ch. 7')}
CHAP_RE = re.compile(r'A Day With the Beavers; What Happened Af(?:…|ter Dinner)')
CHAP = 'A Day with the Beavers; What Happened after Dinner; In the Witch&rsquo;s House'
def hw(tip, t): return '<span class="dol-highlight-word" onclick="dolHighlight(this,\'%s\')">%s</span>' % (tip, t)
def sp(w, ok, g='gspot1'): return '<span class="spotter-word" onclick="gramSpotAll(this,\'%s\')" data-correct="%s">%s</span>' % (g, 'true' if ok else 'false', w)
def pp(good, shown=None, why=''):
    if shown is None: return '<span onclick="proofPick(this)" data-good="%s" data-why="" data-ok="1" style="cursor:pointer;border-bottom:2px dotted #B9C4DC;padding:0 3px;">%s</span>' % (good, good)
    return '<span onclick="proofPick(this)" data-good="%s" data-why="%s" style="cursor:pointer;border-bottom:2px dotted #B9C4DC;padding:0 3px;">%s</span>' % (good, why, shown)
WHY = "<p style=\"font-size:13px;color:#7A88A8;font-style:italic;\">%s</p>"
R = {
 'lesson-27-1-lww.html': [
  (' '.join([sp('teached', True), sp('him', False), sp('to', False), sp('lie.', False)]),
   ' '.join([sp('he', False), sp('eated', True), sp('them', False), sp('all.', False)])),
 ],
 'lesson-27-2-lww.html': [
  (hw('A name — capital L.', 'Lucy') + ' ' + hw('The irregular past tense of &quot;wake&quot; — not &quot;waked.&quot;', 'woke') + ' before ' +
   hw('The comma comes before &quot;and&quot; because it joins two complete sentences.', 'dawn,') + ' and she ' +
   hw('The irregular past tense of &quot;go&quot; — not &quot;goed.&quot;', 'went') + ' outside where the snow had ' +
   hw('The past participle of &quot;begin,&quot; used here after &quot;had.&quot;', 'begun') + ' to melt.',
   hw('A title and a name — both capitalized, and Mr. ends with a period.', 'Mr. Beaver') + ' ' + hw('The irregular past tense of &quot;tell&quot; — not &quot;telled.&quot;', 'told') +
   ' the children about ' + hw('The comma comes before &quot;and&quot; because it joins two complete sentences.', 'Aslan,') + ' and nobody ' +
   hw('The irregular past tense of &quot;see&quot; — not &quot;seed.&quot;', 'saw') + ' ' + hw('A name — capital E.', 'Edmund') + ' go.'),
  ('<div class="swyk-prompt">Sort the mistakes you found into two piles and name each pile.</div>', '<div class="swyk-prompt">Sort the mistakes you found into three piles and name each pile.</div>'),
  ('What does Edmund do at the end of Ch. 8? What does he tell himself to justify his decision?', 'What does Edmund do near the end of Ch. 8? When do the others notice?'),
  ('Something has been moving in the trees while the children stand and watch. What do they finally see?',
   'This is from Chapter 7. Something has been moving in the trees while the children stand and watch. What do they finally see?'),
 ],
 'lesson-27-3-lww.html': [
  (hw('This word begins a dependent clause — it cannot stand alone.', 'When') + ' Aslan ' + hw('The irregular past tense of &quot;come&quot; — not &quot;comed.&quot;', 'came') + ' to the ' +
   hw('The comma separates the opening clause from the main part of the sentence.', 'camp,') + ' the creatures ' +
   hw('The irregular past tense of &quot;see&quot; — not &quot;seed.&quot;', 'saw') + ' him and ' + hw('The irregular past tense of &quot;know&quot; — not &quot;knowed.&quot;', 'knew') + ' that winter was ending.',
   hw('This word begins a dependent clause — it cannot stand alone.', 'When') + ' Edmund ' + hw('The irregular past tense of &quot;come&quot; — not &quot;comed.&quot;', 'came') + ' to the ' +
   hw('The comma separates the opening clause from the main part of the sentence.', 'lion,') + ' he ' +
   hw('The irregular past tense of &quot;feel&quot; — not &quot;feeled.&quot;', 'felt') + ' cold stone and ' + hw('The irregular past tense of &quot;know&quot; — not &quot;knowed.&quot;', 'knew') + ' that it was only a statue.'),
  ('when edmund came to the witchs house he saw many stone creatures in the yard and he knowed he was in the wrong place',
   'when edmund came to the witchs house he saw a stone lion in the courtyard and he thinked it was aslan'),
  ('<strong>Corrected:</strong> When Edmund came to the Witch\'s house, he saw many stone creatures in the yard, and he knew he was in the wrong place.',
   '<strong>Corrected:</strong> When Edmund came to the Witch\'s house, he saw a stone lion in the courtyard, and he thought it was Aslan.'),
  ("When begins the dependent clause; Witch's = possessive (apostrophe + s, capital W); came, saw, knew are all irregular past tenses; two commas needed; period ends.",
   "When begins the dependent clause; Edmund and Aslan are names; Witch's = possessive (apostrophe + s, capital W); came, saw, thought are all irregular past tenses; two commas needed; period ends."),
  ('Only Aslan had the <select id="vocab_sel_0"', 'Mr. Beaver said that Aslan, not the Witch, had the <select id="vocab_sel_0"'),
  ('</select> to call all the creatures of Narnia to battle.', '</select> to rule Narnia.'),
  ('Edmund runned to the witch and bringed her the news.', 'Edmund runned to the Witch and bringed her the news.'),
  ('&ldquo;said Edmund, giving Peter a look which was as much as to say &ldquo;What did I tell you?&rdquo;&rdquo;',
   '&ldquo;&lsquo;And now what are we to do?&rsquo; said Edmund, giving Peter a look which was as much as to say &lsquo;What did I tell you?&rsquo;&rdquo;'),
  ('The children have just met something strange in the trees. What is Edmund doing to Peter here &mdash; without saying it out loud?',
   'This is from Chapter 7, right after the robin flies away and the children are lost. What is Edmund doing to Peter here &mdash; without saying it out loud?'),
  (pp('Peter'), pp('Dad')), (pp('sledge'), pp('sled')),
  (pp('Edmund'), pp('My') + '\n' + pp('brother')),
  (pp('Mrs') + '\n' + pp('Beaver'), pp('Mom')),
  (pp('Lucy'), pp('My') + '\n' + pp('sister')),
 ],
 'lesson-27-4-lww.html': [
  (hw('A capital letter begins every sentence.', 'The') + ' girls ' + hw('The irregular past tense of &quot;run&quot; — not &quot;runned.&quot;', 'ran') + ' across the melting ' +
   hw('The comma comes before &quot;and&quot; because it joins two complete sentences.', 'ice,') + ' and they ' + hw('The irregular past tense of &quot;come.&quot;', 'came') + ' to the ' +
   hw('The name of a particular place — both words capitalized.', 'Stone Table') + ' at last.',
   hw('A capital letter begins every sentence.', 'The') + ' children ' + hw('The irregular past tense of &quot;come&quot; — not &quot;comed.&quot;', 'came') + ' to the ' +
   hw('Beavers&rsquo; ends with an apostrophe: the house belongs to both Beavers.', 'Beavers&rsquo;') + ' ' +
   hw('The comma comes before &quot;and&quot; because it joins two complete sentences.', 'house,') + ' and they ' + hw('The irregular past tense of &quot;eat&quot; — not &quot;eated.&quot;', 'ate') + ' fresh fish for dinner.'),
  ('the children ran through the dark woods and they came to a wide frozen river that they had to cross', 'the children followed mr beaver through the woods and they came to a wide frozen river'),
  ('<strong>Corrected:</strong> The children ran through the dark woods, and they came to a wide frozen river that they had to cross.',
   '<strong>Corrected:</strong> The children followed Mr. Beaver through the woods, and they came to a wide frozen river.'),
  ('Capitalize The at the start; ran and came are irregular past tenses; comma before and joining two independent clauses; period ends.',
   'Capitalize The at the start; Mr. Beaver is a title and a name; came is an irregular past tense; comma before and joining two complete thoughts; period ends.'),
  ('<p><strong>goed</strong> &rarr; went. <strong>runned</strong> &rarr; ran.</p>', '<p><strong>eated</strong> &rarr; ate. <strong>goed</strong> &rarr; went.</p>'),
  ('<p>Capitals: <strong>the, lucy, she</strong> &mdash; sentence starts and names. A comma goes after <strong>wardrobe</strong>, before <em>and</em>, in the first sentence, because it joins two complete thoughts.</p>',
   '<p>Capitals: <strong>the, edmund, he</strong> &mdash; sentence starts and names. A comma goes after <strong>fish</strong>, before <em>and</em>, in the first sentence, because it joins two complete thoughts.</p>'),
  ("Clara's final closing: Lewis uses these contrasting reactions to show that the battle in Narnia is not just between armies — it is between choices.",
   "Clara's final closing: Lewis uses these opposite reactions to show that each character&rsquo;s choices shape what they see."),
  ('Something is moving among the trees and the children cannot tell what it is. What is the mood in this moment?',
   'This is from Chapter 7. Something is moving among the trees and the children cannot tell what it is. What is the mood in this moment?'),
 ],
}
G4_RE = re.compile(r'(<div class="spotter-sentence" id="gspot1" data-done="false" style="font-family:Georgia,serif;line-height:2.2;">).*?(<div class="spotter-result" id="gspot1-result">)', re.S)
G4_NEW = [('the',1),('childrens',1),('dinner',0),('was',0),('hot',0),('fish',1),('and',0),('edmund',1),('eated',1),('his',0),('share.',0),('he',1),('goed',1),('out',0),('into',0),('the',0),('snow',0),('without',0),('his',0),('coat.',0)]
FDIV = '<div style="font-family:Lora,Georgia,serif;font-size:18px;color:#0E1C42;line-height:2.0;padding:3px 0;">%s</div>'
CHIP = '<span style="display:inline-block;background:#EAF4EE;border:2px solid #B8E0C8;border-radius:20px;padding:4px 12px;font-size:15px;font-weight:700;color:#0E1C42;margin:4px;">%s</span>'
FL_NEW = ['None of the children knew who Aslan was any more than you do; but the moment the Beaver had spoken these words everyone felt quite different.',
 'At the name of Aslan each one of the children felt something jump in its inside.',
 'Edmund felt a sensation of mysterious horror.', 'Peter felt suddenly brave and adventurous.',
 'Susan felt as if some delicious smell or some delightful strain of music had just floated by her.',
 'And Lucy got the feeling you have when you wake up in the morning and realize that it is the beginning of the holidays or the beginning of summer.']
FL_FOCUS = ('Pause after the third line. Give each child&#x27;s reaction a slightly different tone.', "Pause after the third line. Give each child's reaction a slightly different tone.")
FL_FOCUS_NEW = 'Read the first two sentences calmly. Then give each child&rsquo;s feeling its own voice: dark for Edmund, bold for Peter, dreamy for Susan, happy for Lucy.'
if __name__ == '__main__':
    dry = '--apply' not in sys.argv
    d = sys.argv[sys.argv.index('--dir') + 1] + '/' if '--dir' in sys.argv else ''
    for day in (1, 2, 3, 4):
        f = 'lesson-27-%d-lww.html' % day
        s = open(d + f, encoding='utf-8', newline='').read()
        o = s.count('<div') - s.count('</div')
        s, n = OBJ_RE.subn('\n'.join(ol(*x) for x in OBJ[day]), s); assert n == 1, (f, 'obj', n)
        assert s.count(QOLD) == 1, (f, 'quote'); s = s.replace(QOLD, QNEW % QS[day])
        s, n = CHAP_RE.subn(CHAP, s); assert n >= 2, (f, 'chap', n)
        if day == 4:
            s, n = G4_RE.subn(lambda m: m.group(1) + ' '.join(sp(w, k) for w, k in G4_NEW) + m.group(2), s); assert n == 1, (f, 'g4')
        for old, new in R[f]:
            c = s.count(old); assert c == 1, (f, c, old[:140]); s = s.replace(old, new)
        k = s.count('Mr Beaver') + s.count('Mrs Beaver') + s.count('Mr and Mrs')
        s = s.replace('Mr and Mrs Beaver', 'Mr. and Mrs. Beaver').replace('Mrs Beaver', 'Mrs. Beaver').replace('Mr Beaver', 'Mr. Beaver')
        assert s.count('<div') - s.count('</div') == o, f
        if not dry: open(d + f, 'w', encoding='utf-8', newline='').write(s)
        print('ok' if not dry else 'dry-ok', f, len(R[f]) + 3, 'Mr.', k)
    f = 'lesson-27-fluency.html'; s = open(d + f, encoding='utf-8', newline='').read(); o = s.count('<div') - s.count('</div')
    m = re.search(r'(border-left:6px solid #D4AF37;">)((?:<div style="font-family:Lora[^>]*>[^<]*</div>)+)', s); assert m and 'Mr Beaver leaned' in m.group(2)
    s = s.replace(m.group(2), ''.join(FDIV % l for l in FL_NEW) + '<div style="font-size:13px;color:#7A88A8;margin-top:8px;">&mdash; C.S. Lewis, <em>The Lion, the Witch and the Wardrobe</em>, Ch. 7</div>')
    old = ''.join(CHIP % w for w in ['suddenly','whisper','hollow','reaction','faint']); assert s.count(old) == 1
    s = s.replace(old, ''.join(CHIP % w for w in ['mysterious','sensation','adventurous','delightful','holidays']))
    n = 0
    for fo in FL_FOCUS: n += s.count(fo); s = s.replace(fo, FL_FOCUS_NEW)
    assert n == 2, n
    a = "  if (tabId === 'warmup') { intro.classList.remove('collapsed'); }\n  else { intro.classList.add('collapsed'); }"
    assert s.count(a) == 1, 'intro'
    s = s.replace(a, "  if (intro) { if (tabId === 'warmup') { intro.classList.remove('collapsed'); }\n  else { intro.classList.add('collapsed'); } }")
    s = s.replace('Mr Beaver', 'Mr. Beaver')
    assert s.count('<div') - s.count('</div') == o
    if not dry: open(d + f, 'w', encoding='utf-8', newline='').write(s)
    print('ok' if not dry else 'dry-ok', f)
