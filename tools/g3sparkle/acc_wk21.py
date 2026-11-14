"""Week 21 accuracy + small wording fixes (approved by Bethany Nov 14 2026). Run once on the pre-sparkle files."""
LBL = '<div class="socratic-label">&#x1F451; The lie that protects:</div>\n        <p class="socratic-q" style="font-style:normal;">When Cutwater yanks open the coach door, takes him for the whipping boy, and asks, &ldquo;Where&rsquo;s your master, eh?&rdquo; Prince Brat answers, &ldquo;Swam the river.&rdquo; Later he takes the stripes himself and does not yell. &ldquo;You should have yelled and bellowed,&rdquo; Jemmy tells him. &ldquo;And humble myself?&rdquo; says the prince. &ldquo;You never did.&rdquo;</p>'
def sp(label, t): return '<div class="socratic-label">&#x1F451; ' + label + '</div>\n        <p class="socratic-q" style="font-style:normal;">' + t + '</p>'
OBJ = ('I will a conclusion restates the opinion in a fresh way.', 'I will use details from the book to say what the story teaches.')
MEANS = ('<p><strong>re-, un-, pre-, dis-, mis-</strong> means <strong>the five prefixes you met first</strong>.</p>',
         '<p>Each of these word parts goes at the <strong>front</strong> of a word and changes its meaning.</p>')
def fi(n, a, b, ans, extra=''):
    return '<div class="fillin-item">%s- + %s &rarr; <input class="fillin-input" id="mfill%d" data-answer="%s" maxlength="16" placeholder="______">%s</div>' % (a, b, n, ans, extra)
OLD3 = '\n'.join([fi(1,'re','build','rebuild',' &mdash; to build again'), fi(2,'un','happy','unhappy',' &mdash; not happy'),
                  fi(3,'pre','view','preview',' &mdash; to view before'), fi(4,'dis','agree','disagree',' &mdash; to not agree')])
NEW3 = '\n'.join([fi(1,'re','read','reread',' &mdash; to read again'), fi(2,'un','fair','unfair',' &mdash; not fair'),
                  fi(3,'pre','heat','preheat',' &mdash; to heat before'), fi(4,'dis','trust','distrust',' &mdash; to not trust'),
                  fi(5,'mis','spell','misspell',' &mdash; to spell wrong')])
def hw(cls, txt, word): return '<span class="dol-highlight-word" onclick="dolHighlight(this,\'%s\')">%s</span>' % (txt, word)
R = {
 'lesson-21-1-wb.html': [OBJ,
  ('<p>re-, un-, pre-, dis-, mis- means <strong>the five prefixes you met first</strong>.</p>',
   '<p>Each of these word parts goes at the <strong>front</strong> of a word and changes its meaning.</p>'),
  ('<p><strong>disagree</strong> &mdash; dis- + agree</p>\n</div>', '<p><strong>disagree</strong> &mdash; dis- + agree</p>\n<p><strong>misread</strong> &mdash; mis- + read</p>\n</div>'),
  ('<p><strong>disagree</strong> &mdash; to not agree</p>\n</div>', '<p><strong>disagree</strong> &mdash; to not agree</p>\n<p><strong>misread</strong> &mdash; to read wrong</p>\n</div>'),
  (fi(4,'dis','agree','disagree'), fi(4,'dis','agree','disagree') + '\n' + fi(5,'mis','read','misread')),
  ('>before the sun rose</span>', '>before sunrise</span>'),
  ("Ch. 15 — calls prince 'me friend' and goes back for him.", "Ch. 15 — calls prince 'my friend' and goes back for him."),
  ('Ch. 17 — takes a whipping himself without crying.', 'Ch. 16 — takes a whipping himself without crying.'),
 ],
 'lesson-21-2-wb.html': [OBJ, MEANS,
  ('He had never before heard Prince Brat laugh.', 'He&rsquo;d never before heard Prince Brat laugh.'),
  ("An accidental word like 'friend' can reveal more than a whole speech.", "A small word like &lsquo;friend&rsquo; can mean more than a whole speech.", 3),
  ('<span class="dol-highlight-word" onclick="dolHighlight(this,\'A name — capital J.\')">Jemmy</span> straightened <span class="dol-highlight-word" onclick="dolHighlight(this,\'&quot;And&quot; joins two verbs with the same subject, so it takes no comma.\')">and</span> folded <span class="dol-highlight-word" onclick="dolHighlight(this,\'A possessive pronoun — no apostrophe is needed on &quot;his.&quot;\')">his</span> <span class="dol-highlight-word" onclick="dolHighlight(this,\'A period ends the sentence.\')">arms.</span>',
   hw(0,'A capital T starts the sentence.','The') + ' prince drained the mug ' + hw(0,'&quot;And&quot; joins two verbs with the same subject, so it takes no comma.','and') + ' shuffled ' + hw(0,'A period ends the sentence.','away.')),
  (LBL, sp('In Chapters 18&ndash;19:', 'At the fair, the prince tells Smudge, &ldquo;Friend-O&rsquo;-Jemmy&rsquo;s the name,&rdquo; and shakes his hand. In the sewer, Jemmy tells him, &ldquo;Reckon I do trust you.&rdquo; The prince answers, &ldquo;I won&rsquo;t go back to the castle unless you go with me.&rdquo;')),
 ],
 'lesson-21-3-wb.html': [OBJ, MEANS, (OLD3, NEW3),
  ('<p>The prince asks the king to protect Jemmy. Why is this the most important moment in the whole book?</p>',
   '<p>The prince promises to do his lessons and behave so Jemmy can stay safe. Why is this a big moment?</p>'),
  ('What deal does the king make with Jemmy? <strong>Is it a fair deal? Why or why not?</strong>',
   'The king says, &ldquo;You ought to be whipped.&rdquo; <strong>What does he do instead?</strong>'),
  ('The king&rsquo;s <input class="fillin-input" id="vcloze3" data-answer="decree" maxlength="10" placeholder="______"> made it official: the whipping boy would be punished no more.',
   '&ldquo;But you&rsquo;re my friend,&rdquo; the prince said, as if he were giving a royal <input class="fillin-input" id="vcloze3" data-answer="decree" maxlength="10" placeholder="______">.'),
  ('Write two sentences about Chapter 15, each with', 'Write two sentences about Chapter 20, each with'),
  (LBL, sp('In Chapter 20:', 'The prince tells Betsy and Captain Nips to turn Jemmy in for the reward. Jemmy feels betrayed, until the prince gives him a quick, playful wink. In the throne room, the king says the prince has sworn to do his lessons, blow out his night candle, and behave.')),
 ],
 'lesson-21-4-wb.html': [OBJ, MEANS,
  ('Even the outlaws had to admit that Jemmy had acted <input class="fillin-input" id="vcloze2" data-answer="nobly" maxlength="9" placeholder="______"> in a very un-prince-like way.',
   '&ldquo;You&rsquo;ve served your prince <input class="fillin-input" id="vcloze2" data-answer="nobly" maxlength="9" placeholder="______">,&rdquo; the prince told Betsy and Captain Nips.'),
  ('It took real <input class="fillin-input" id="vcloze3" data-answer="pluck" maxlength="9" placeholder="______"> for Jemmy to walk back into danger for someone he barely trusted.',
   'Jemmy saw a cast-iron streak of <input class="fillin-input" id="vcloze3" data-answer="pluck" maxlength="9" placeholder="______"> in the prince.'),
  ('The prince was completely <input class="fillin-input" id="vcloze4" data-answer="befuddled" maxlength="13" placeholder="______"> by the way common people actually lived.',
   'The prince&rsquo;s wink <input class="fillin-input" id="vcloze4" data-answer="befuddled" maxlength="13" placeholder="______"> Jemmy for an instant.'),
  ('''<span class="spotter-word" onclick="gramSpotFix(this,'gspot1')" data-correct="false">Jemmy</span> <span class="spotter-word" onclick="gramSpotFix(this,'gspot1')" data-correct="false">hid</span>''',
   '''<span class="spotter-word" onclick="gramSpotFix(this,'gspot1')" data-correct="false">The</span> <span class="spotter-word" onclick="gramSpotFix(this,'gspot1')" data-correct="false">prince</span> <span class="spotter-word" onclick="gramSpotFix(this,'gspot1')" data-correct="false">hid</span>'''),
  ('It should be <em>on a pile of the straw</em>.', 'It should be <em>on the straw</em>.'),
  ('Split it, then name both syllable types.', 'Say which spelling fits and why.'),
  (LBL, sp('Looking back:', 'In Chapter 1, Jemmy is whipped for the prince&rsquo;s tricks. In Chapter 16, the prince takes a whipping himself and makes no sound. In Chapter 20, the prince makes promises to his father so Jemmy can stay safe.')),
 ],
 'lesson-21-fluency.html': [
  ('<div class="quote-strip-text">&ldquo;Read it again for smoothness. Read it a third time with expression.&rdquo;</div>',
   '<div class="quote-strip-text">&ldquo;The bear came snarling down the embankment.&rdquo;</div>'),
  ('<div class="quote-strip-attr">&mdash; The 5-Step Fluency Routine</div>', '<div class="quote-strip-attr">&mdash; Sid Fleischman, The Whipping Boy</div>'),
  ('ELA.4.F.1.4 — Read grade-level texts', 'ELA.3.F.1.4 — Read grade-level texts'),
 ],
}
if __name__ == '__main__':
    for f, reps in R.items():
        s = open(f, encoding='utf-8', newline='').read()
        for r in reps:
            old, new = r[0], r[1]; n = r[2] if len(r) > 2 else 1
            c = s.count(old)
            assert c == n, (f, c, old[:90])
            s = s.replace(old, new)
        open(f, 'w', encoding='utf-8', newline='').write(s)
        print('ok', f, len(reps))
