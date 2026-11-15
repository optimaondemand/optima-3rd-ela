#!/usr/bin/env python3
"""Week 30 check-in as a Canvas quiz: JSON source of truth + readable key. Audit: claude/g3-ela-wk30-audit.md findings 16-23.
Passage = The Lion, the Witch and the Wardrobe, Ch. 17 ("And they made good laws ..."), checked against Planning docs/lww_text.txt.
DRAFT until Bethany approves; .zip only after that."""
import json, io, html
Q = {
 "id": "g3-ela-wk30-checkin",
 "title": "Week 30 Check-In · The Lion, the Witch and the Wardrobe",
 "description": "This week you finished The Lion, the Witch and the Wardrobe: the statues come alive, the battle is won, and the four children are crowned kings and queens at Cair Paravel. You practiced editing for capitals and punctuation, and reviewed the roots and spelling patterns from the whole year. Show what you know!",
 "quarter": 4, "chapters": "Ch. 16–17",
 "questions": [
  {"n":1,"section":"Grammar","type":"multiple_choice_question","points":1,"text":"Which sentence has no punctuation mistake?",
   "options":["“It was all Edmund’s doing, Aslan,” Peter was saying.","“It was all Edmunds doing, Aslan” Peter was saying.","It was all Edmund’s doing, Aslan, “Peter was saying.”"],"answer":0,
   "from":"30.1–30.4 Grammar (capitals, apostrophes, commas), week 29 dialogue","status":"fixed (old lines were invented: Peter never says “Aslan is alive”)"},
  {"n":2,"section":"Grammar","type":"essay_question","points":1,"text":"Fix all the mistakes in these two sentences: once edmund had broken the witchs wand the battle turned. peter told aslan it was all edmunds doing.",
   "from":"30.2 four kinds of mistakes, 30.3 before and after, 30.4 passes","status":"fixed (old paragraph was invented)"},
  {"n":3,"section":"Grammar","type":"essay_question","points":1,"text":"Write 2–3 sentences about the ending of the story with correct punctuation. Include one sentence where someone speaks, and one contraction.",
   "from":"30.1–30.4 Grammar, week 29 dialogue","status":"kept"},
  {"n":4,"section":"Word Parts","type":"essay_question","points":1,"text":"Find the word part in each word and write what it means: transform (prefix), hopeless (suffix), inspector (root).",
   "from":"30.1 roots from the year, 30.2 match (inspect)","status":"kept"},
  {"n":5,"section":"Word Parts","type":"multiple_choice_question","points":1,"text":"What does the word construct most likely mean?",
   "options":["It means to build something.","It means to break something.","It means to look at something."],"answer":0,
   "from":"30.2 match, 30.3 build, 30.4 dice (con + struct)","status":"fixed (incredible uses the root cred, never taught)"},
  {"n":6,"section":"Word Parts","type":"essay_question","points":1,"text":"Choose any word you studied this year that has a prefix, suffix or root. Write the word, break it apart, and use it in a sentence.",
   "from":"30.1–30.4 Morphology","status":"kept"},
  {"n":7,"section":"Spelling","type":"essay_question","points":1,"text":"Write each word, and name the pattern that helps you spell it: because (the au vowel team), hoping (the silent e drops), inspect (the root spect).",
   "from":"30.1–30.4 Spelling (patterns from the year)","status":"kept (clearer wording)"},
  {"n":8,"section":"Spelling","type":"essay_question","points":1,"text":"What spelling strategy has helped you most this year? Explain it in your own words, and give an example of a word where you use it.",
   "from":"30.1 Now name the pattern","status":"kept"},
  {"n":9,"section":"Spelling","type":"multiple_choice_question","points":1,"text":"One word is spelled wrong. Which one?",
   "options":["because","hopeing","inspect"],"answer":1,"from":"30.1–30.4 Spelling, week 28 endings","status":"kept"},
  {"n":10,"section":"Reading","type":"essay_question","points":1,"text":"What kinds of things did the four kings and queens do for Narnia? Use two details from the passage.",
   "from":"30.1 Q3, 30.3 Q2","status":"kept (passage is now the book’s own words)"},
  {"n":11,"section":"Reading","type":"essay_question","points":1,"text":"The book ends: “And that is the very end of the adventure of the wardrobe. But if the Professor was right, it was only the beginning of the adventures of Narnia.” Is the story really over? Explain your thinking.",
   "from":"30.4 Read Like a Writer","status":"fixed (now quotes the book’s real last lines)"},
  {"n":12,"section":"Reading","type":"essay_question","points":1,"text":"How is Edmund different at the end of the book from how he was at the beginning? Use a detail from Chapter 17.",
   "from":"30.1 Q2, 30.2 Q2","status":"fixed (old Q12 asked about Stanley, Despereaux and Jemmy, not taught this week)"},
  {"n":13,"section":"Writing","type":"essay_question","points":1,"text":"Model sentences from the book: “And that is the very end of the adventure of the wardrobe. But if the Professor was right, it was only the beginning of the adventures of Narnia.” The word But turns an ending into a beginning. Write your own two sentences about the end of a story, where the second one starts with But and hints that there is more to come.",
   "from":"30.4 Read Like a Writer (But opening a new thought)","status":"fixed (old model sentence was invented)"},
  {"n":14,"section":"Writing","type":"essay_question","points":1,"text":"Write 2–3 sentences that start “The ending shows that…” Tell how the end of The Lion, the Witch and the Wardrobe proves its theme.",
   "from":"30.1 Q3, 30.1–30.4 Writer’s Workshop (final revision)","status":"fixed (old Q14 repeated Q12)"}
 ],
 "passage": {"before": 10, "title": "Reading passage (The Lion, the Witch and the Wardrobe, Chapter 17)",
   "text": "And they made good laws and kept the peace and saved good trees from being unnecessarily cut down, and liberated young dwarfs and young satyrs from being sent to school, and generally stopped busybodies and interferers and encouraged ordinary people who wanted to live and let live.\n— C.S. Lewis, The Lion, the Witch and the Wardrobe, Chapter 17"}
}
io.open('assessments/g3-ela-wk30-checkin.json', 'w', encoding='utf-8').write(json.dumps(Q, ensure_ascii=False, indent=1))
e = html.escape
rows = ''
for q in Q['questions']:
    if q['n'] == Q['passage']['before']:
        rows += '<div class="psg"><b>%s</b><p>%s</p></div>' % (e(Q['passage']['title']), e(Q['passage']['text']).replace('\n','<br>'))
    opts = ''
    if 'options' in q:
        opts = '<ol type="A">' + ''.join('<li%s>%s%s</li>' % (' class="ok"' if i == q['answer'] else '', e(o), ' ✓' if i == q['answer'] else '') for i, o in enumerate(q['options'])) + '</ol>'
    kind = 'Multiple choice (auto-graded)' if q['type'] != 'essay_question' else 'Written (teacher-graded)'
    rows += ('<div class="q %s"><div class="h"><span class="n">%d</span> %s · %s · %d pt</div><p>%s</p>%s<div class="m">Taught in: %s<br>Audit: %s</div></div>'
             % ('new' if q['status'].startswith(('new', 'fixed')) else '', q['n'], e(q['section']), kind, q['points'], e(q['text']), opts, e(q['from']), e(q['status'])))
page = '''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Week 30 Check-In Key</title>
<style>body{font:16px/1.5 system-ui,sans-serif;max-width:820px;margin:0 auto;padding:16px;background:#F0F2F8;color:#24324F}
h1{font-size:22px;color:#0E1C42}.q,.psg{background:#fff;border:1px solid #D9E0F0;border-radius:10px;padding:12px 16px;margin:12px 0}
.q.new{border-left:5px solid #2B5BA8}.psg{background:#FFF8E6}.h{font-weight:700;color:#0E1C42}.n{display:inline-block;background:#0E1C42;color:#fff;border-radius:50%%;width:26px;height:26px;text-align:center;line-height:26px;margin-right:6px}
.ok{color:#24502A;font-weight:700}.m{font-size:13px;color:#6B7690;margin-top:6px}</style></head><body>
<h1>%s</h1><p>%s</p><p><b>Quarter 4 · %s · %d questions · %d points.</b> Blue edge = fixed or new question.</p>%s</body></html>''' % (
    e(Q['title']), e(Q['description']), e(Q['chapters']), len(Q['questions']), sum(q['points'] for q in Q['questions']), rows)
io.open('assessments/g3-ela-wk30-checkin-key.html', 'w', encoding='utf-8').write(page)
print('ok')
