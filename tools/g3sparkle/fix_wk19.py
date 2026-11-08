"""Week 19 accuracy fixes A-L (approved by Bethany Nov 8 2026). Run once on the pre-sparkle files."""
import sys
R = {
 'lesson-19-1-wb.html': [
  ('I will opinion writing needs reasons.', 'I will learn that opinion writing needs reasons.'),
  ("What is Jemmy's trick in Chapter 7? <strong>How does he try to outsmart the outlaws using the ransom note?</strong>",
   "In Chapter 7, Billy decides Jemmy is the prince. <strong>Why does Jemmy play along?</strong>"),
  ('>The bear growled.<', '>The outlaw growled.<'),
  ('>Jemmy ran, and the bear followed.<', '>Jemmy ran, and the outlaw followed.<'),
  ('>Because the bear came.<', '>Because the outlaw came.<'),
 ],
 'lesson-19-2-wb.html': [
  ("Revealing Jemmy's plan to trick villains", "Revealing Jemmy's plan to trick the villains", 2),
  ('Jemmy has been pretending to be the prince so the outlaws will not hurt them.',
   'The outlaws think Jemmy is the prince, and Jemmy is playing along.'),
  ('>the bear followed close behind.<', '>the outlaw followed close behind.<'),
 ],
 'lesson-19-3-wb.html': [
  ('at being unprinced.&rdquo;', 'at being un-princed.&rdquo;'),
  ('invents a word: <strong>unprinced</strong>.', 'invents a word: <strong>un-princed</strong>.'),
  ('invented word <em>unprinced</em>', 'invented word <em>un-princed</em>'),
  ('Chapter 11: Cutwater threatens the prince, and Jemmy steps in. <strong>What does Jemmy do, and how does the prince react?</strong>',
   'Chapter 11: Billy pulls off his belt to whip the prince, and Jemmy steps in. <strong>What does Jemmy suggest instead?</strong>'),
  ('Look at what the prince says when Jemmy gives him the chance to escape.',
   'Look at what the prince says when the outlaws tell him to carry the crown to the castle.'),
  ('Jemmy ran and the bear followed. &mdash;', 'Jemmy ran and the outlaw followed. &mdash;'),
 ],
 'lesson-19-4-wb.html': [
  ('&#9989; Correct Model &mdash; based on the novel', '&#9989; Correct Model &mdash; from the novel'),
  ("""<span class="dol-highlight-word" onclick="dolHighlight(this,'The opening quotation mark, and a contraction of &quot;it is&quot; — not the possessive &quot;its.&quot;')">"It's</span> not me you think <span class="dol-highlight-word" onclick="dolHighlight(this,'A contraction of &quot;you are&quot; — not &quot;your.&quot;')">you're</span> <span class="dol-highlight-word" onclick="dolHighlight(this,'The comma goes INSIDE the closing quotation mark.')">protecting,"</span> said <span class="dol-highlight-word" onclick="dolHighlight(this,'A name, and the period that ends the sentence.')">Jemmy.</span>""",
   """<span class="dol-highlight-word" onclick="dolHighlight(this,'The opening quotation mark, and a capital letter to start what the prince says.')">"It</span> <span class="dol-highlight-word" onclick="dolHighlight(this,'A contraction of &quot;does not.&quot; The apostrophe stands for the missing o.')">doesn't</span> please me to take orders from common <span class="dol-highlight-word" onclick="dolHighlight(this,'The comma goes INSIDE the closing quotation mark.')">rascals,"</span> <span class="dol-highlight-word" onclick="dolHighlight(this,'A name gets capital letters.')">Prince Brat</span> said <span class="dol-highlight-word" onclick="dolHighlight(this,'The period that ends the sentence.')">coldly.</span>"""),
  ("Jemmy says: 'It's not me you think you're protecting.' What does he mean?",
   "Jemmy says: 'It's not me you think you're protecting, is it?' What does he mean?"),
  ('Think about who will receive the note — and who it will make look guilty.',
   'Think about what Jemmy says the outlaws will do when they find out he tricked them.'),
  ('data-correct="false">bear</span>', 'data-correct="false">outlaw</span>'),
 ],
 'lesson-19-fluency.html': [
  ('<div class="info-value">From Chapter 5</div>', '<div class="info-value">From Chapter 11</div>'),
  ('Read the passage from Chapter 5 several times', 'Read the passage from Chapter 11 several times'),
  ('From Chapter 5 — Ch. 6–11', 'From Chapter 11 — Ch. 6–11'),
  ('''        Billy was a big man, he saw, big and raw as a skinned ox. And he smelled like a ton of garlic.

"Not much of a catch — two sparrows," said Billy. "But ain't they trimmed up in fancy rags, Cutwater?"

"Got any gold in your pockets, lads?"

"No business of yours!" snapped the prince.

Jemmy gave the prince a sudden jab of his elbow to keep his mouth shut. Not a word!''',
   '''        Jemmy was struck dumb. Did Prince Brat have sand for brains? Gaw! Didn't he realize he could snatch up his crown and go free?

"It doesn't please me to take orders from common rascals," Prince Brat said coldly.

"It would please me to shake the teeth out of your confounded face!" replied Hold-Your-Nose Billy. "You may live in the castle, but you're only a whipping boy. Do as we say!"

"I'll do what I choose. And I choose not to run your errands."'''),
  ("Read Billy's voice loud and booming. The prince should sound sharp and proud. When Jemmy jabs the prince, let your voice go suddenly quiet — like a warning.",
   "Read Jemmy's thoughts fast and amazed. The prince should sound cold and slow. Read Billy's voice loud and angry. Make the prince's last line calm and stubborn."),
  ("read billy's voice loud and booming.", "read Billy's voice loud and angry."),
  ("Did I use different voices for Billy, the prince, and Jemmy's silent action?",
   "Did I use different voices for Jemmy's thoughts, the prince, and Billy?"),
 ],
}
for f, reps in R.items():
    s = open(f, encoding='utf-8', newline='').read()
    crlf = '\r\n' in s
    if crlf: s = s.replace('\r\n', '\n')
    for r in reps:
        old, new = r[0], r[1]; n = r[2] if len(r) > 2 else 1
        c = s.count(old)
        assert c == n, (f, c, old[:70])
        s = s.replace(old, new)
    if crlf: s = s.replace('\n', '\r\n')
    open(f, 'w', encoding='utf-8', newline='').write(s)
    print('ok', f, len(reps))
