"""Week 26 (LWW Ch. 4-6) accuracy + wording fixes, approved by Bethany Nov 14 2026 (claude/g3-ela-wk26-audit.md
findings 1-13, 15). 14 is plain_wk26.py; 16-19 (check-in) live in the quiz JSON (checkin_wk26.py). Run once on the
pre-sparkle files:  python tools/g3sparkle/acc_wk26.py [--dir D] [--apply]"""
import sys
def ol(icon, k, t): return '<div class="obj-line"><span class="obj-icon">%s</span><span><strong>%s:</strong> %s</span></div>' % (icon, k, t)
OBJ_OLD = {
 1: ('I will identify the choices Edmund makes in Ch. 4 and their results.', 'I will define verb tense consistency.', 'I will <em>define</em> how to count the beats in a long academic word.'),
 2: ('I will identify choices and consequences in Ch. 5.', 'I will identify tense errors in a paragraph.', 'I will <em>identify</em> how many beats an academic word has by ear.'),
 3: ("I will use evidence from Ch. 6 to explain a character's decision.", 'I will apply verb tense consistency when writing about the story.', 'I will <em>split</em> long academic words into syllables and read them in chunks.'),
 4: ("I will explain how a character's choice leads to a consequence using evidence.", 'I will explain why verb tense consistency matters in writing.', 'I will <em>explain</em> how I knew where each syllable split belonged.'),
}
OBJ = {
 1: [('📖','Reading','I will name the choices Edmund makes in Ch. 4 and what happens because of them.'), ('🌱','Word parts','I will build words with form, which means shape.'),
     ('✏️','Grammar','I will find verbs that slip out of the past tense.'), ('🔤','Spelling','I will count the beats in long school words.'), ('✍️','Writing','I will draft a paragraph about a character’s choice.')],
 2: [('📖','Reading','I will find choices and what they cost in Ch. 5.'), ('🌱','Word parts','I will match form words to their meanings.'),
     ('✏️','Grammar','I will fix verbs that switch tense in a paragraph.'), ('🔤','Spelling','I will hear how many beats a long word has.'), ('✍️','Writing','I will add connecting words to make my paragraph clearer.')],
 3: [('📖','Reading','I will use details from Ch. 6 to explain a character’s choice.'), ('🌱','Word parts','I will build form words from their parts.'),
     ('✏️','Grammar','I will rewrite sentences so every verb is in the past tense.'), ('🔤','Spelling','I will split long school words into beats.'), ('✍️','Writing','I will put my whole paragraph together.')],
 4: [('📖','Reading','I will explain how Edmund’s choice leads to what happens next.'), ('🌱','Word parts','I will explain how form changes a word.'),
     ('✏️','Grammar','I will fix capitals, verb tense and a comma in a passage.'), ('🔤','Spelling','I will explain how I knew where each word splits.'), ('✍️','Writing','I will polish my paragraph with a stronger word.')],
}
def objrep(d):
    r, g, s = OBJ_OLD[d]
    return (ol('📖','Reading',r) + '\n' + ol('✏️','Grammar',g) + '\n' + ol('🔤','Spelling',s), '\n'.join(ol(*x) for x in OBJ[d]))
QOLD = '&ldquo;The more he ate the more he wanted to eat, and he never asked himself why the Queen should be so inquisitive.&rdquo;</div>\n  <div class="quote-strip-attr" style="color:#D4AF37;font-size:13px;margin-top:8px;">&mdash; C.S. Lewis, Ch. 4</div>'
QNEW = '&ldquo;%s&rdquo;</div>\n  <div class="quote-strip-attr" style="color:#D4AF37;font-size:13px;margin-top:8px;">&mdash; C.S. Lewis, Ch. %s</div>'
QS = {2: ('Poor Lucy gave Edmund one look and rushed out of the room.', '5'), 3: ('We simply must try to rescue him.', '6'), 4: ('&lsquo;I&rsquo;ll try,&rsquo; said Edmund, still looking at the empty box.', '4')}
CH = [('Turkish Delight; Back on This Side of th…</div>', 'Turkish Delight; Back on This Side of the Door; Into the Forest</div>'),
      ('Ch. 4–6 — Turkish Delight; Back on This Side of the Door; In</strong>', 'Ch. 4–6 — Turkish Delight; Back on This Side of the Door; Into the Forest</strong>')]
def ALL(d):
    r = [objrep(d)] + CH
    if d in QS: r.append((QOLD, QNEW % QS[d]))
    return r
def hw(tip, t): return '<span class="dol-highlight-word" onclick="dolHighlight(this,\'%s\')">%s</span>' % (tip, t)
R = {
 'lesson-26-1-lww.html': ALL(1) + [
  ('The ' + hw('A title used as a name — both words are capitalized.', 'White Queen') + ' ' + hw('Present tense — it is happening now.', 'smiles') + ' at ' +
   hw('A name, and the comma that comes before &quot;and&quot; joining two complete sentences.', 'Edmund,') + ' and she ' +
   hw('Present tense too — it matches &quot;smiles.&quot; Keep the tense the same all the way through.', 'offers') + ' him another piece of ' +
   hw('The name of a particular thing — both words capitalized — and a period to close.', 'Turkish Delight.'),
   'The ' + hw('A title used as her name — capital Q.', 'Queen') + ' ' + hw('Present tense — it is happening now.', 'smiles') + ' at ' +
   hw('A name, and the comma that comes before &quot;and&quot; joining two complete sentences.', 'Edmund,') + ' and she ' +
   hw('Present tense too — it matches &quot;smiles.&quot; Keep the tense the same all the way through.', 'gives') + ' him a box of ' +
   hw('The name of a particular thing — both words capitalized — and a period to close.', 'Turkish Delight.')),
  ('the white queen gives edmund enchanted sweets and he forgets all about his family', 'the queen asks edmund many questions and he answers them all'),
  ('<strong>Corrected:</strong> The White Queen gives Edmund enchanted sweets, and he forgets all about his family.', '<strong>Corrected:</strong> The Queen asks Edmund many questions, and he answers them all.'),
  ('Capitalize The White Queen (proper noun title); comma before and joining two complete thoughts; consistent present-tense verbs (gives, forgets); period ends.',
   'Capital T begins the sentence; Queen is used as her name (capital Q); Edmund is a name; comma before and joining two complete thoughts; consistent present-tense verbs (asks, answers); period ends.'),
  ('&ldquo;How did you come to enter my <input class="fillin-input" id="vcloze2" data-answer="dominions" maxlength="13" placeholder="______">?&rdquo; the White Witch asked, her cold eyes fixed on Edmund.',
   '&ldquo;And how, pray, did you come to enter my <input class="fillin-input" id="vcloze2" data-answer="dominions" maxlength="13" placeholder="______">?&rdquo; the Queen asked Edmund.'),
  ('Edmund felt <input class="fillin-input" id="vcloze3" data-answer="wretched" maxlength="12" placeholder="______"> sitting alone in the cold, wishing he had not followed the White Witch at all.',
   'Lucy felt <input class="fillin-input" id="vcloze3" data-answer="wretched" maxlength="12" placeholder="______"> for days, because the others thought she had told a silly lie.'),
  ('<span class="sort-chip" data-group="four" onclick="pickSortChip(this)">imagination</span>', '<span class="sort-chip" data-group="four" onclick="pickSortChip(this)">education</span>'),
  ('As a result, he agrees to betray his own family to get more sweets.', 'As a result, he promises to bring his brother and sisters to her house.'),
 ],
 'lesson-26-2-lww.html': ALL(2) + [
  (hw('A name — capital E.', 'Edmund') + ' ' + hw('Past tense — it matches &quot;said&quot; later in the sentence.', 'knew') + ' about ' +
   hw('A place name (capital N), and the comma that comes before &quot;but&quot; joining two complete sentences.', 'Narnia,') + ' but he ' +
   hw('Past tense too — the sentence never switches to the present.', 'said') + ' nothing to Peter and ' + hw('A name, and the period that ends the sentence.', 'Susan.'),
   hw('A name — capital E.', 'Edmund') + ' had ' + hw('Past tense — it matches &quot;told&quot; later in the sentence.', 'been') + ' to ' +
   hw('A place name (capital N), and the comma that comes before &quot;but&quot; joining two complete sentences.', 'Narnia,') + ' but he ' +
   hw('Past tense too — the sentence never switches to the present.', 'told') + ' Peter and Susan it was only a ' + hw('The period that ends the sentence.', 'game.')),
  ('<div class="swyk-prompt">Three kinds of mistake again. Name them.</div>', '<div class="swyk-prompt">Four kinds of mistake this time. Name them.</div>'),
  ('&ldquo;Edmund, who was tired and pretending not to be tired, which always made him bad-tempered.&rdquo;',
   '&ldquo;&lsquo;Oh, come off it!&rsquo; said Edmund, who was tired and pretending not to be tired, which always made him bad-tempered.&rdquo;'),
  ('The children have just arrived and are talking before bed. What is going on with Edmund?',
   'This is from Chapter 1, the children’s first night at the Professor’s house, talking before bed. What is going on with Edmund?'),
 ],
 'lesson-26-3-lww.html': ALL(3) + [
  ('Edmund felt <select id="vocab_sel_2"', 'Mr. Tumnus cried and called himself a <select id="vocab_sel_2"'),
  ('</select> about what he had done, but he told himself he did not care.', '</select> Faun for planning to hand Lucy to the Witch.'),
 ],
 'lesson-26-4-lww.html': ALL(4) + [
  (' but she meant none of ' + hw('A period ends the sentence.', 'it.'), ' but Lucy said she was a terrible ' + hw('A period ends the sentence.', 'person.')),
  ('<div class="swyk-prompt">Two of those were about capitals and the rest were about verbs. Which was which?</div>',
   '<div class="swyk-prompt">Which kind of mistake was hardest to spot: capitals, verbs, or the comma? Why?</div>'),
 ],
}
FL_OLD = ['Edmund sat on the sledge and thought about what the Queen had promised.', 'A crown. A castle. Rooms full of Turkish Delight.',
 'He knew, somewhere deep inside, that Lucy had been right about the White Witch.', 'But the sweets had been so good — so warm and sweet and impossible to forget.',
 'He told himself it would all work out.', 'He told himself the others would understand.', 'He pushed the small, cold voice of doubt away and kept walking toward the hills.']
FL_NEW = ['While he was eating the Queen kept asking him questions.',
 'At first Edmund tried to remember that it is rude to speak with one&rsquo;s mouth full, but soon he forgot about this and thought only of trying to shovel down as much Turkish Delight as he could, and the more he ate the more he wanted to eat, and he never asked himself why the Queen should be so inquisitive.',
 'She got him to tell her that he had one brother and two sisters, and that one of his sisters had already been in Narnia and had met a Faun there.']
FDIV = '<div style="font-family:Lora,Georgia,serif;font-size:18px;color:#0E1C42;line-height:2.0;padding:3px 0;">%s</div>'
CHIP = '<span style="display:inline-block;background:#EAF4EE;border:2px solid #B8E0C8;border-radius:20px;padding:4px 12px;font-size:15px;font-weight:700;color:#0E1C42;margin:4px;">%s</span>'
if __name__ == '__main__':
    dry = '--apply' not in sys.argv
    d = sys.argv[sys.argv.index('--dir') + 1] + '/' if '--dir' in sys.argv else ''
    f = 'lesson-26-fluency.html'; s = open(d + f, encoding='utf-8', newline='').read()
    old_chips = [w for w in ['somewhere','impossible','understand','promised','uncomfortable']]
    R[f] = [(''.join(FDIV % l for l in FL_OLD), ''.join(FDIV % l for l in FL_NEW) + '<div style="font-size:13px;color:#7A88A8;margin-top:8px;">&mdash; C.S. Lewis, <em>The Lion, the Witch and the Wardrobe</em>, Ch. 4</div>'),
            (''.join(CHIP % w for w in old_chips), ''.join(CHIP % w for w in ['questions','remember','shovel','delight','inquisitive'])),
            ('Read the short sentences quickly — they show Edmund rushing past uncomfortable thoughts.', 'Read the short first sentence calmly. Then read the long sentence in one smooth run, the way Edmund keeps on eating.')]
    for f, reps in R.items():
        s = open(d + f, encoding='utf-8', newline='').read()
        o = s.count('<div') - s.count('</div')
        for old, new in reps:
            c = s.count(old); assert c >= 1, (f, c, old[:120]); s = s.replace(old, new)
        if f != 'lesson-26-fluency.html':
            k = s.count('Mr Tumnus'); s = s.replace('Mr Tumnus', 'Mr. Tumnus'); print('  Mr. x', k)
        assert s.count('<div') - s.count('</div') == o, f
        if not dry: open(d + f, 'w', encoding='utf-8', newline='').write(s)
        print('ok' if not dry else 'dry-ok', f, len(reps))
