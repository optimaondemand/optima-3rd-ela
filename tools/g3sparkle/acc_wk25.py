"""Week 25 (LWW Ch. 1-3) accuracy + wording fixes, approved by Bethany Nov 14 2026 (claude/g3-ela-wk25-audit.md
findings 1-14, 16). Finding 15 is plain_wk25.py; 17-20 (check-in) live in the quiz JSON (checkin_wk25.py).
Run once on the pre-sparkle files:  python tools/g3sparkle/acc_wk25.py [--dir D] [--apply]"""
import re, sys

def spots(fn, sid, words):
    """words: list of (text, correct)"""
    return ' '.join('<span class="spotter-word" onclick="%s(this,\'%s\')" data-correct="%s">%s</span>' % (fn, sid, 'true' if c else 'false', w)
                    for w, c in words)
def plain(text, keys, fn='gramSpotAll', sid='gspot1'):
    out = []
    for w in text.split():
        out.append((w, w in keys))
    return spots(fn, sid, out)
def oldspots(fn, sid, star):
    return spots(fn, sid, [(w.rstrip('*'), w.endswith('*')) for w in star.split()])

def ol(icon, k, t): return '<div class="obj-line"><span class="obj-icon">%s</span><span><strong>%s:</strong> %s</span></div>' % (icon, k, t)
OBJ_OLD = {
 1: ('I will identify the setting details Lewis uses to build Narnia.', 'I will define what a complex sentence is.', 'I will define the schwa sound and find it in longer words.'),
 2: ('I will identify details from Ch. 2–3 that make Narnia feel like a real world.', 'I will identify the connecting word in complex sentences.', 'I will identify the schwa syllable in longer words.'),
 3: ('I will use evidence from Ch. 1–3 to explain how Lewis builds the setting.', 'I will write my own complex sentence about the story.', "I will apply what I know about schwa to spell this week's words."),
 4: ('I will explain how Lewis creates the setting of Narnia using specific evidence.', 'I will revise a simple sentence to make it complex.', 'I will explain why the schwa makes long words tricky to spell.'),
}
OBJ = {
 1: [('📖','Reading','I will find the details Lewis uses to build Narnia in Ch. 1.'),
     ('🌱','Word parts','I will build words that start with tele-, which means far.'),
     ('✏️','Grammar','I will find where the comma goes in a complex sentence.'),
     ('🔤','Spelling','I will sort words by the vowel that makes the lazy schwa sound.'),
     ('✍️','Writing','I will brainstorm details about the setting of Narnia.')],
 2: [('📖','Reading','I will find details from Ch. 2–3 that make Narnia feel real.'),
     ('🌱','Word parts','I will match tele- words to their meanings.'),
     ('✏️','Grammar','I will find the connecting word in complex sentences.'),
     ('🔤','Spelling','I will find words that have a schwa beat.'),
     ('✍️','Writing','I will draft the opening sentence of my literary response.')],
 3: [('📖','Reading','I will use details from Ch. 1–3 to explain how Lewis builds the setting.'),
     ('🌱','Word parts','I will build tele- words from their parts.'),
     ('✏️','Grammar','I will join two sentences into one complex sentence.'),
     ('🔤','Spelling','I will find which vowel blurs in a long word.'),
     ('✍️','Writing','I will write two evidence sentences with short quotes.')],
 4: [('📖','Reading','I will explain how Lewis makes Narnia feel real, using details from the book.'),
     ('🌱','Word parts','I will explain how tele- changes a word.'),
     ('✏️','Grammar','I will fix capitals, an apostrophe and a comma in a passage.'),
     ('🔤','Spelling','I will explain why the schwa makes long words tricky to spell.'),
     ('✍️','Writing','I will write the closing sentence of my literary response.')],
}
def objrep(d):
    r, g, s = OBJ_OLD[d]
    old = (ol('📖','Reading',r) + '\n' + ol('✏️','Grammar',g) + '\n' + ol('🔤','Spelling',s))
    return (old, '\n'.join(ol(*x) for x in OBJ[d]))
QOLD = '&ldquo;She found herself standing in the middle of a wood at night-time with snow under her feet.&rdquo;</div>\n  <div class="quote-strip-attr" style="color:#D4AF37;font-size:13px;margin-top:8px;">&mdash; C.S. Lewis, Ch. 1</div>'
QNEW = '&ldquo;%s&rdquo;</div>\n  <div class="quote-strip-attr" style="color:#D4AF37;font-size:13px;margin-top:8px;">&mdash; C.S. Lewis, Ch. %s</div>'
QS = {1: ('A moment later she found that she was standing in the middle of a wood at night-time with snow under her feet and snowflakes falling through the air.', '1'),
      2: ('And really it was a wonderful tea.', '2'),
      3: ('Everything was perfectly still, as if he were the only living creature in that country.', '3'),
      4: ('This must be a simply enormous wardrobe!', '1')}
CH = [('Lucy Looks into a Wardrobe; What Lucy Fo…</div>', 'Lucy Looks into a Wardrobe; What Lucy Found There; Edmund and the Wardrobe</div>'),
      ('Ch. 1–3 — Lucy Looks into a Wardrobe; What Lucy Found There;</strong>', 'Ch. 1–3 — Lucy Looks into a Wardrobe; What Lucy Found There; Edmund and the Wardrobe</strong>')]
def ALL(d): return [objrep(d), (QOLD, QNEW % QS[d])] + CH

def hw(tip, t): return '<span class="dol-highlight-word" onclick="dolHighlight(this,\'%s\')">%s</span>' % (tip, t)
POEM_NOTE_OLD = 'Blake asks who could <strong>frame</strong> the tiger, as if the animal were built by hand. The forests are given a night to belong to. In Narnia this is not even a figure of speech &mdash; the woods really do wake up &mdash; which makes it a good place to notice the move.'
POEM_NOTE_NEW = 'Blake talks to the tiger as if it could listen and answer him, the way you would talk to a person. That is personification: giving something that is not a person a person&rsquo;s way of acting.'

R = {
 'lesson-25-1-lww.html': ALL(1) + [
  (oldspots('gramSpotAll','gspot1','Although Lucy was afraid* she stepped through the wardrobe. When Edmund followed her* he told nobody. Because the lamp post glowed* they found their way back.'),
   plain('Although Lucy felt a little frightened she walked on through the wood. When Edmund jumped in he shut the door. Because Mr. Tumnus was sorry he took Lucy back to the lamp-post.', {'frightened','in','sorry'})),
  ('<span class="decode-part decode-part-root">inquire-</span><span class="decode-part-plus">+</span><span class="decode-part decode-part-affix">-itiv</div>',
   '<span class="decode-part decode-part-root">inquis (ask, seek)</span><span class="decode-part-plus">+</span><span class="decode-part decode-part-affix">-itive (likes to)</span></div>'),
  ('Everything was completely still and silent. Lewis uses', 'Snowflakes were falling through the air. Lewis uses'),
 ],
 'lesson-25-2-lww.html': ALL(2) + [
  (hw('A capital letter begins every sentence.','The') + ' ' + hw('A title used as a name — both words are capitalized.','White Witch') + ' stopped her sledge in the ' +
   hw('The comma comes before &quot;and&quot; because it joins two complete sentences.','snow,') + ' and ' + hw('A name — capital E.','Edmund') + ' stared at her ' + hw('A period ends the sentence.','crown.'),
   hw('A capital letter begins every sentence.','The') + ' ' + hw('A title used as a name — capital Q.','Queen') + ' told the dwarf to ' +
   hw('The comma comes before &quot;and&quot; because it joins two complete sentences.','stop,') + ' and ' + hw('A name — capital E.','Edmund') + ' stared at her golden ' + hw('A period ends the sentence.','crown.')),
  ('the white witch drove her sledge across the frozen river and the reindeer ran very fast', 'the queen of narnia sat high on the sledge and the dwarf cracked his whip'),
  ('<strong>Corrected:</strong> The White Witch drove her sledge across the frozen river, and the reindeer ran very fast.', '<strong>Corrected:</strong> The Queen of Narnia sat high on the sledge, and the dwarf cracked his whip.'),
  ('The White Witch is a proper noun title (capital W); comma before and joining two independent clauses; period ends.',
   'Capital T begins the sentence; Queen is a title used as her name (capital Q); Narnia is a place name (capital N); comma before and joining two complete thoughts; period ends.'),
  ('Lucy ran back when she heard the Faun begin to sob.', 'When the Faun began to sob, Lucy lent him her handkerchief.'),
  ('If the Witch finds out, Mr Tumnus will be turned to stone.', 'If the Witch is very angry, she may turn Mr Tumnus into stone.'),
  (oldspots('gramSpotAll','gspot1','although* lucy* was afraid, she stepped through the wardrobe. the* professors* house was very old* and edmund* did not believe her.'),
   plain('although lucy felt frightened, she walked on through the wood. the professors house was very old and edmund did not believe her.', {'although','lucy','the','professors','old','edmund'})),
  (oldspots('spellSpotAll','spellSpot1','About* a moment* after the soldiers arrived*').replace('</span> <span','</span> <span') , None),
  (POEM_NOTE_OLD, POEM_NOTE_NEW),
 ],
 'lesson-25-3-lww.html': ALL(3) + [
  ('when edmund found the lamp-post he remembered what lucy had told him', 'when edmund called for lucy there was no answer'),
  ('<strong>Corrected:</strong> When Edmund found the lamp-post, he remembered what Lucy had told him.', '<strong>Corrected:</strong> When Edmund called for Lucy, there was no answer.'),
  ('Lucy was afraid. She stepped through the wardrobe anyway.', 'Lucy felt a little frightened. She walked on through the wood.'),
  ('Although Lucy was afraid, she stepped through the wardrobe anyway.', 'Although Lucy felt a little frightened, she walked on through the wood.'),
 ],
 'lesson-25-4-lww.html': ALL(4) + [
  (oldspots('gramSpotAll','gspot1','when* the four children reached cair* paravel,* aslan* crowned them. the* witchs* power was broken* and narnia* was free at last.'),
   plain('when the four children reached the professors house, lucy found the wardrobe. the faun took her back to the lamp-post and lucy ran back through the wardrobe.',
         set()).replace('X','X')),
  ('<p>Capitals: <strong>when, cair, paravel, aslan, the, narnia</strong> &mdash; sentence starts and names.</p>\n<p><strong>witchs</strong> &rarr; Witch&rsquo;s &mdash; a possessive noun from Week 9 (capital W, because <em>the Witch</em> is used as her name).</p>\n<p>A comma goes after <strong>broken</strong>, before <em>and</em>, because it joins two complete thoughts &mdash; from Week 19.</p>',
   '<p>Capitals: <strong>when, lucy, the, faun, lucy</strong> &mdash; sentence starts and names (<em>the Faun</em> is used as his name).</p>\n<p><strong>professors</strong> &rarr; Professor&rsquo;s &mdash; a possessive noun from Week 9 (capital P, because <em>the Professor</em> is used as his name).</p>\n<p>A comma goes after <strong>lamp-post</strong>, before <em>and</em>, because it joins two complete thoughts &mdash; from Week 19.</p>'),
  (POEM_NOTE_OLD, POEM_NOTE_NEW),
  ('In the chapters you are reading, find one thing that is not a person but behaves like one. Copy the sentence and underline what gives it away.',
   'Mr. Tumnus is a Faun, not a person, but he does many things people do. Name two things he does in Ch. 2.'),
  ('<em>"not a few inches away where the back ought to have been"</em>', '<em>"not a few inches away where the back of the wardrobe ought to have been"</em>'),
  ('step through that wardrobe seventy years later.', 'step through that wardrobe more than seventy years after it was written.'),
 ],
}
# 25.2 spelling sentence: rebuild the whole spotter run (keeps the commas/periods between spans)
SP_OLD_RE = re.compile(r'<span class="spotter-word" onclick="spellSpotAll\(this,\'spellSpot1\'\)" data-correct="true">About</span>.*?data-correct="true">amazed</span>\.', re.S)
SP_NEW = (plain('Lucy was afraid for a moment, but she walked along through the snow.', {'afraid','moment,','along'}, 'spellSpotAll', 'spellSpot1')
          + ' ' + plain('She had left the wardrobe door open.', {'open.'}, 'spellSpotAll', 'spellSpot1'))
# 25.4 grammar keys
G4 = {'when','professors','lucy','the','faun','lamp-post'}
def fix_g4(new):
    words = 'when the four children reached the professors house, lucy found the wardrobe. the faun took her back to the lamp-post and lucy ran back through the wardrobe.'.split()
    keyed = []
    for i, w in enumerate(words):
        k = (i == 0) or w in ('professors', 'lucy', 'faun', 'lamp-post') or (w == 'the' and i == 9)
        keyed.append((w, k))
    return spots('gramSpotAll', 'gspot1', keyed)

FLU_LINES_OLD = ['Lucy stepped forward, and something cold and soft fell across her hand.', 'She looked up. Snowflakes were drifting silently between the dark trees.',
 'Behind her, the wardrobe door stood open — a small patch of ordinary light.', 'Ahead of her, a lamp-post glowed in the middle of the forest.',
 'It was the strangest and most beautiful thing she had ever seen.', 'She took a deep breath of cold air.', 'Then, slowly and carefully, she walked toward the light.']
FLU_LINES_NEW = ['Next moment she found that what was rubbing against her face and hands was no longer soft fur but something hard and rough and even prickly.',
 '&ldquo;Why, it is just like branches of trees!&rdquo; exclaimed Lucy.',
 'And then she saw that there was a light ahead of her; not a few inches away where the back of the wardrobe ought to have been, but a long way off.',
 'Something cold and soft was falling on her.',
 'A moment later she found that she was standing in the middle of a wood at night-time with snow under her feet and snowflakes falling through the air.',
 '&mdash; C.S. Lewis, <em>The Lion, the Witch and the Wardrobe</em>, Ch. 1']
FDIV = '<div style="font-family:Lora,Georgia,serif;font-size:18px;color:#0E1C42;line-height:2.0;padding:3px 0;">%s</div>'
CHIP = '<span style="display:inline-block;background:#EAF4EE;border:2px solid #B8E0C8;border-radius:20px;padding:4px 12px;font-size:15px;font-weight:700;color:#0E1C42;margin:4px;">%s</span>'
R['lesson-25-fluency.html'] = [
  (''.join(FDIV % l for l in FLU_LINES_OLD), ''.join(FDIV % l for l in FLU_LINES_NEW[:-1]) + '<div style="font-size:13px;color:#7A88A8;margin-top:8px;">%s</div>' % FLU_LINES_NEW[-1]),
  (''.join(CHIP % w for w in ['snowflakes','silently','ordinary','strangest','carefully']), ''.join(CHIP % w for w in ['prickly','exclaimed','branches','wardrobe','snowflakes'])),
  ('Read with wonder and careful pacing. The sentences grow longer as Lucy grows braver.', 'Read with wonder and careful pacing. Slow down where Lucy is surprised.', 2),
]

if __name__ == '__main__':
    dry = '--apply' not in sys.argv
    d = sys.argv[sys.argv.index('--dir') + 1] + '/' if '--dir' in sys.argv else ''
    for f, reps in R.items():
        s = open(d + f, encoding='utf-8', newline='').read()
        o = s.count('<div') - s.count('</div')
        for r in reps:
            old, new = r[0], r[1]; n = r[2] if len(r) > 2 else 1
            if new is None: continue
            if f == 'lesson-25-4-lww.html' and old.startswith('<span class="spotter-word" onclick="gramSpotAll'):
                new = fix_g4(new)
            c = s.count(old)
            assert c == n, (f, c, old[:120])
            s = s.replace(old, new)
        if f == 'lesson-25-2-lww.html':
            s, k = SP_OLD_RE.subn(SP_NEW, s); assert k == 1, k
        if f != 'lesson-25-fluency.html':
            k = s.count('Mr Tumnus'); s = s.replace('Mr Tumnus', 'Mr. Tumnus'); print('  Mr. Tumnus x', k)
        assert s.count('<div') - s.count('</div') == o, f
        if not dry: open(d + f, 'w', encoding='utf-8', newline='').write(s)
        print('ok' if not dry else 'dry-ok', f, len(reps))
