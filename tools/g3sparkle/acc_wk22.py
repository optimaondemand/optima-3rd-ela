"""Week 22 accuracy + small wording fixes (approved by Bethany Nov 14 2026). Run once on the pre-sparkle files."""
def sp(label, t): return '<div class="socratic-label">&#x1F451; ' + label + '</div>\n        <p class="socratic-q" style="font-style:normal;">' + t + '</p>'
OLDSP_LBL = '<div class="socratic-label">&#x1F451; What the whole book was building to:</div>\n        <p class="socratic-q" style="font-style:normal;">In the throne room the prince makes one promise &mdash; to do his lessons, blow out his night candle and behave &mdash; and Jemmy walks out without a single whack. &ldquo;Gaw!&rdquo; he thinks. &ldquo;You must want me for a friend awful bad to promise all that. '
SP1_OLD = OLDSP_LBL + 'So help me, if it&rsquo;s a friend you ran off looking for, it&rsquo;s a friend you found!&rdquo;</p>'
SP_OLD = OLDSP_LBL + 'If it&rsquo;s a friend you ran off looking for, it&rsquo;s a friend you found.&rdquo;</p>'
SP = {
 1: sp('Chapter 1 and Chapter 20:', 'In Chapter 1, Jemmy takes the whacks for the prince&rsquo;s tricks. In Chapter 20, the king tells Jemmy, &ldquo;He tells me it&rsquo;s thanks to you that he&rsquo;s back, sound and safe.&rdquo;'),
 2: sp('In Chapter 19:', 'In the dark sewer, the prince says, &ldquo;I wish I were like you.&rdquo; He thinks Jemmy is not afraid of anything. Jemmy answers, &ldquo;Course I am.&rdquo;'),
 3: sp('In Chapter 14:', 'Jemmy asks Betsy the way to the river. &ldquo;Which way is south?&rdquo; &ldquo;Straight on!&rdquo; &ldquo;You certain?&rdquo; &ldquo;Certain I&rsquo;m certain.&rdquo;'),
 4: sp('In Chapter 20:', 'At the golden doors, the king calls, &ldquo;One more thing!&rdquo; Then he smiles. &ldquo;If you boys decide to run away again, take me with you.&rdquo;'),
}
OBJ_R = '<strong>Reading:</strong> I will strong comparisons use similarities and differences.</span>'
OBJ = {1: 'I will compare how Jemmy and the prince changed, using details from the book.',
       2: 'I will name what the story teaches and find two events that show it.',
       3: 'I will read a scene aloud with expression.',
       4: 'I will share my comparison paragraph and look back on the book.'}
GRAM = ('<strong>Grammar:</strong> I will study pronoun review.</span>', '<strong>Grammar:</strong> I will tell which pronouns do the action, receive it, or show belonging.</span>')
SPELL = ('<strong>Spelling:</strong> I will practice spelling compound words.</span>', '<strong>Spelling:</strong> I will spell compound words.</span>')
RULE = ('<em>mail</em> + <em>box</em> = <strong>mailbox</strong>', '<em>rain</em> + <em>bow</em> = <strong>rainbow</strong>')
LI_OLD = ('      <li><strong>Go back to the beginning:</strong> Remind yourself who each character was on the first pages.</li>\n'
          '      <li><strong>Mark the moments that changed them:</strong> Find two or three turning points along the way.</li>\n'
          '      <li><strong>Compare them side by side:</strong> Say what is different about each character now, and what caused it.</li>')
def lis(*xs): return '\n'.join('      <li><strong>%s</strong> %s</li>' % x for x in xs)
LI = {
 2: lis(('Look for the lesson:', 'Ask what a character learned, not just what happened.'),
        ('Look for proof:', 'Find one moment early and one moment late that show the same lesson.'),
        ('Say it for everyone:', 'Write the lesson so it fits any person, not only Jemmy.')),
 3: lis(('Listen for the voice:', 'Hear how each character talks: bossy, scared, sly, or kind.'),
        ('Watch the marks:', 'Let ! and ? and commas tell your voice when to rise, ask, or pause.'),
        ('Act it out:', 'Use your face and hands the way the character would.')),
 4: lis(('Remember the best part:', 'Pick the moment you would tell a friend about.'),
        ('Look at the whole road:', 'Think about where Jemmy and the prince started and where they ended.'),
        ('Share it:', 'Say your favorite part out loud to someone.')),
}
def hw(txt, word): return '<span class="dol-highlight-word" onclick="dolHighlight(this,\'%s\')">%s</span>' % (txt, word)
DOL1_OLD = 'The king <span class="dol-highlight-word" onclick="dolHighlight(this,\'A comma comes after the dialogue tag, before the speech.\')">said,</span> <span class="dol-highlight-word" onclick="dolHighlight(this,\'Quotation marks wrap the exact word, with the exclamation point inside.\')">"Dismissed!"</span> and the boys walked <span class="dol-highlight-word" onclick="dolHighlight(this,\'A preposition — it shows which way he walked.\')">toward</span> the golden <span class="dol-highlight-word" onclick="dolHighlight(this,\'A period ends the sentence.\')">doors.</span>'
DOL1_NEW = (hw('Quotation marks open the exact words. A capital D starts what he says.', '"Dismissed,') + ' both of ' +
            hw('The comma sits inside the closing quotation mark.', 'you,"') + ' ' +
            hw('The speaker tag comes after the words, so said starts with a small s.', 'said') + ' the ' + hw('A period ends the whole sentence.', 'king.'))
DOL2_OLD = '<span class="dol-highlight-word" onclick="dolHighlight(this,\'A name — capital J.\')">Jemmy</span> could not sort out'
DOL2_NEW = '<span class="dol-highlight-word" onclick="dolHighlight(this,\'A name — capital J.\')">Jemmy</span> ' + hw('An apostrophe takes the place of the missing o in could not.', 'couldn&rsquo;t') + ' sort out'
def fi(n, a, b, c, ans, mean):
    return '<div class="fillin-item">%s + %s%s &rarr; <input class="fillin-input" id="mfill%d" data-answer="%s" maxlength="16" placeholder="______"> &mdash; %s</div>' % (a, b, c, n, ans, mean)
OLD3 = '\n'.join([
 '<div class="fillin-item">con- + struct &rarr; <input class="fillin-input" id="mfill1" data-answer="construct" maxlength="16" placeholder="______"> &mdash; to build together</div>',
 '<div class="fillin-item">struct + ure &rarr; <input class="fillin-input" id="mfill2" data-answer="structure" maxlength="16" placeholder="______"> &mdash; something built</div>',
 '<div class="fillin-item">in- + struct &rarr; <input class="fillin-input" id="mfill3" data-answer="instruct" maxlength="16" placeholder="______"> &mdash; to build knowledge into someone</div>',
 '<div class="fillin-item">de- + struct &rarr; <input class="fillin-input" id="mfill4" data-answer="destruct" maxlength="16" placeholder="______"> &mdash; to un-build</div>'])
NEW3 = '\n'.join([fi(1, 'con-', 'struct', ' + -ion', 'construction', 'the work of building something'),
                  fi(2, 'in-', 'struct', ' + -ion', 'instruction', 'teaching; steps that tell you how'),
                  fi(3, 'de-', 'struct', ' + -ion', 'destruction', 'tearing something down'),
                  fi(4, 'ob-', 'struct', '', 'obstruct', 'to build something in the way; to block')])
ALL = lambda d: [(OBJ_R, '<strong>Reading:</strong> ' + OBJ[d] + '</span>'), GRAM, SPELL, RULE, ((SP1_OLD if d == 1 else SP_OLD), SP[d])] + ([(LI_OLD, LI[d])] if d in LI else [])
R = {
 'lesson-22-1-wb.html': ALL(1) + [
  (DOL1_OLD, DOL1_NEW),
  ('          betsy laughed hurrah and bowed toward the king\n', '          the reward is yours the king announced\n'),
  ('<strong>Corrected:</strong> Betsy laughed, "Hurrah!" and bowed toward the king.</p>', '<strong>Corrected:</strong> "The reward is yours," the king announced.</p>'),
  ('Capital B on Betsy; comma after laughed; opening quotation mark; capital H on Hurrah; exclamation mark inside the closing quote; lowercase and; period ends.',
   'Opening quotation mark; capital T on The; comma inside the closing quotation mark; small t on the; period ends.'),
  ('Type the missing <strong>prefix</strong> at the start of each word.', 'Type the missing <strong>word part</strong> in each word.'),
  ('<div class="textbox-prompt">Use the prefix and its meaning.</div>', '<div class="textbox-prompt">Use the root and its meaning.</div>'),
  ("In Chapter 20, Prince Brat asked the king to protect Jemmy — something he never would have done in Chapter 1.",
   "In Chapter 20, Prince Brat told the king that Jemmy saved him — something he never would have done in Chapter 1.", 2),
 ],
 'lesson-22-2-wb.html': ALL(2) + [
  (DOL2_OLD, DOL2_NEW),
  ('What is he realising?', 'What is he realizing?'),
  ("it is about going back for someone even when you don't have to.", "it is about standing up for someone even when it hurts."),
 ],
 'lesson-22-3-wb.html': ALL(3) + [(OLD3, NEW3)],
 'lesson-22-4-wb.html': ALL(4) + [
  ('The moment Jemmy decided to go back was the most <input', 'The prince&rsquo;s wink in Chapter 20 was the most <input'),
  ('<div class="activity" style="margin-bottom:14px;">\n  <div class="activity-head"><div class="activity-num" style="background:#1B7A4E;font-size:14px;">Q4</div><div><div class="activity-title">Q4 — Summarize the Whole Book</div>',
   '<div class="activity bl-cyan" style="margin-bottom:14px;">\n  <div class="activity-head"><div class="activity-num" style="background:#5C2D91;">B</div><div><div class="activity-title">📝 Summarize the Whole Book</div>'),
  ('<div class="activity" style="margin-bottom:14px;">\n  <div class="activity-head"><div class="activity-num" style="background:#1B7A4E;font-size:14px;">Q5</div><div><div class="activity-title">Q5 — Say It Out Loud</div>',
   '<div class="activity bl-cyan" style="margin-bottom:14px;">\n  <div class="activity-head"><div class="activity-num" style="background:#5C2D91;">C</div><div><div class="activity-title">🎤 Say It Out Loud</div>'),
  ('<div class="activity-num" style="background:#8B6FC0;">B</div><div><div class="activity-title">🔤 Word Study Connection', '<div class="activity-num" style="background:#8B6FC0;">D</div><div><div class="activity-title">🔤 Word Study Connection'),
 ],
 'lesson-22-fluency.html': [
  ('<div class="quote-strip-text">&ldquo;Read it again for smoothness. Read it a third time with expression.&rdquo;</div>',
   '<div class="quote-strip-text">&ldquo;If you boys decide to run away again, take me with you.&rdquo;</div>'),
  ('<div class="quote-strip-attr">&mdash; The 5-Step Fluency Routine</div>', '<div class="quote-strip-attr">&mdash; Sid Fleischman, The Whipping Boy</div>'),
  ('ELA.4.F.1.4 — Read grade-level texts', 'ELA.3.F.1.4 — Read grade-level texts'),
 ],
}
if __name__ == '__main__':
    import sys
    dry = '--apply' not in sys.argv
    for f, reps in R.items():
        s = open(f, encoding='utf-8', newline='').read()
        o = s.count('<div') - s.count('</div')
        for r in reps:
            old, new = r[0], r[1]; n = r[2] if len(r) > 2 else 1
            c = s.count(old)
            assert c == n, (f, c, old[:110])
            s = s.replace(old, new)
        assert s.count('<div') - s.count('</div') == o, f
        if not dry: open(f, 'w', encoding='utf-8', newline='').write(s)
        print('ok' if not dry else 'dry-ok', f, len(reps))
