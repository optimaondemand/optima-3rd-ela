"""Week 20 accuracy + small wording fixes (approved by Bethany Nov 13 2026). Run once on the pre-sparkle files."""
SP = ('<p class="socratic-q" style="font-style:normal;">Prince Brat refuses to run the outlaws&rsquo; errand even though obeying would set him free. Jemmy, who has every reason to let him suffer, covers for him with a quick story about &ldquo;stubborn fits&rdquo; &mdash; and when Hold-Your-Nose Billy rips off his belt, Jemmy steps in again with a new plan: send the horse.</p>')
def sp(t): return '<p class="socratic-q" style="font-style:normal;">' + t + '</p>'
OBJ = ('I will using text evidence in a sentence.', 'I will use details from the book in a sentence.')
POEM = ('but count the lines. Four, not three.', 'but count the lines in this verse. Four, not three.')
R = {
 'lesson-20-1-wb.html': [OBJ,
  ('<p>Type the missing <strong>prefix</strong> at the start of each word.</p>', '<p>Type the missing <strong>word part</strong> at the end of each word.</p>'),
  ('<div class="textbox-prompt">Use the prefix and its meaning.</div>', '<div class="textbox-prompt">Use the root and its meaning.</div>'),
  ('<div class="activity-sub">Words from this week\'s chapters.</div>', '<div class="activity-sub">Words from The Whipping Boy.</div>'),
  ("<div class=\"decode-sentence\">Hold-Your-Nose Billy's red eyebrows shot up in bewildered surprise.</div>",
   "<div class=\"decode-sentence\">Hold-Your-Nose Billy's red eyebrows shot up in bewildered surprise. (Chapter 8)</div>"),
  ("then watches with satisfaction.</div>", "then gets angry when Jemmy won't cry.</div>"),
  ("then watches without feeling sorry.", "then gets angry when Jemmy won&rsquo;t cry."),
  ('<span class="sort-chip" data-group="a" onclick="pickSortChip(this)">forgotten</span><span class="sort-chip" data-group="b" onclick="pickSortChip(this)">expected</span><span class="sort-chip" data-group="b" onclick="pickSortChip(this)">powerful</span><span class="sort-chip" data-group="a" onclick="pickSortChip(this)">servant</span><span class="sort-chip" data-group="b" onclick="pickSortChip(this)">adventure</span><span class="sort-chip" data-group="a" onclick="pickSortChip(this)">determined</span>',
   '<span class="sort-chip" data-group="a" onclick="pickSortChip(this)">forgotten</span><span class="sort-chip" data-group="b" onclick="pickSortChip(this)">volcano</span><span class="sort-chip" data-group="a" onclick="pickSortChip(this)">expected</span><span class="sort-chip" data-group="b" onclick="pickSortChip(this)">sunshine</span><span class="sort-chip" data-group="a" onclick="pickSortChip(this)">servant</span><span class="sort-chip" data-group="b" onclick="pickSortChip(this)">potato</span>'),
  ('>Mostly closed/r-controlled syllables<', '>Only closed or r-controlled syllables<'),
  ('>Contains open or silent-e<', '>Has an open syllable or a silent e<'),
 ],
 'lesson-20-2-wb.html': [OBJ, POEM,
  ('<div class="socratic-label">&#x1F451; Standing between:</div>\n        ' + SP,
   '<div class="socratic-label">&#x1F451; In Chapters 13&ndash;14:</div>\n        ' + sp('Jemmy is furious that the prince gave him away. When the prince hears Jemmy&rsquo;s side, he says, &ldquo;Then I forgive you.&rdquo; Jemmy tells him to find his own way back to the castle, but the prince follows him through the brambles anyway.')),
 ],
 'lesson-20-3-wb.html': [OBJ,
  ('People in Jemmy&rsquo;s city had a name for this: <em>mudlarking</em>. (You&rsquo;ll see the word itself in Chapter 18.)',
   'When the prince asks what he is doing, Jemmy answers with one word: &ldquo;Mudlarking.&rdquo;'),
  ('The boys crept down the steep river <input class="fillin-input" id="vcloze2" data-answer="embankment" maxlength="14" placeholder="______"> in the dark, trying not to slip.',
   'The boys walked below the grassy river <input class="fillin-input" id="vcloze2" data-answer="embankment" maxlength="14" placeholder="______">, out of sight of the road.'),
  ('Jemmy&rsquo;s old boots were <input class="fillin-input" id="vcloze3" data-answer="battered" maxlength="12" placeholder="______"> from years of running cobblestone streets.',
   'Jemmy found a bent and <input class="fillin-input" id="vcloze3" data-answer="battered" maxlength="12" placeholder="______"> birdcage in the mud.'),
  ('<div class="socratic-label">&#x1F451; Standing between:</div>\n        ' + SP,
   '<div class="socratic-label">&#x1F451; In Chapter 15:</div>\n        ' + sp('Jemmy plans to give the prince the slip. On the mud flat, the prince picks up a broken chair leg and asks, &ldquo;Is this worth anything?&rdquo; Later, Jemmy rides off in Captain Nips&rsquo; coach. He looks back, sees the prince standing alone in the road, and shouts, &ldquo;Stop, Cap&rsquo;n! We left my friend behind.&rdquo;')),
 ],
 'lesson-20-4-wb.html': [OBJ, POEM,
  ('<div class="socratic-label">&#x1F451; Standing between:</div>\n        ' + SP,
   '<div class="socratic-label">&#x1F451; Looking back:</div>\n        ' + sp('In Chapter 12, the prince gives Jemmy away. In Chapter 15, Jemmy goes back for the prince and calls him his friend. In between, the boys run from Cutwater, argue in the forest, meet Betsy, and dig for treasure in the mud together.')),
 ],
 'lesson-20-fluency.html': [
  ('<div class="quote-strip-text">&ldquo;Read it again for smoothness. Read it a third time with expression.&rdquo;</div>',
   '<div class="quote-strip-text">&ldquo;Jemmy flung open the door and ran.&rdquo;</div>'),
  ('<div class="quote-strip-attr">&mdash; The 5-Step Fluency Routine</div>', '<div class="quote-strip-attr">&mdash; Sid Fleischman, The Whipping Boy</div>'),
  ('ELA.4.F.1.4 — Read grade-level texts', 'ELA.3.F.1.4 — Read grade-level texts'),
  ('this is an escape! read it fast and urgent.', 'this is an escape! Read it fast and urgent.'),
 ],
}
if __name__ == '__main__':
    for f, reps in R.items():
        s = open(f, encoding='utf-8', newline='').read()
        crlf = '\r\n' in s
        if crlf: s = s.replace('\r\n', '\n')
        for r in reps:
            old, new = r[0], r[1]; n = r[2] if len(r) > 2 else 1
            c = s.count(old)
            assert c == n, (f, c, old[:80])
            s = s.replace(old, new)
        if crlf: s = s.replace('\n', '\r\n')
        open(f, 'w', encoding='utf-8', newline='').write(s)
        print('ok', f, len(reps))
