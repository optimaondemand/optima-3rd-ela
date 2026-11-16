#!/usr/bin/env python3
"""Week 32 check-in as a Canvas quiz: JSON source of truth + readable key. Audit: claude/g3-ela-wk32-audit.md finding 26
(old check-in named "Flat Stanley, Despereaux, and Joan of Arc", tested word parts this week never taught (form, ject,
reformation), used an invented "reflection" passage, and never asked about the 7 pillars). Rebuilt from what the four
week 32 pages teach. Passage = the week's own 7 Pillars text (written for Optima). Book moments checked in Planning docs.
DRAFT until Bethany approves; .zip only after that."""
import json, io, html
Q = {
 "id": "g3-ela-wk32-checkin",
 "title": "Week 32 Check-In · Year-End: The 7 Pillars of Virtue",
 "description": "This week you learned the 7 pillars of good character and wrote about one character from this year’s books. You reviewed the word parts, spelling rules and editing rules from the whole year. This is your last check-in of 3rd grade ELA!",
 "quarter": 4, "chapters": "All four books",
 "questions": [
  {"n":1,"section":"Grammar","type":"multiple_choice_question","points":1,"text":"Which sentence is edited correctly?",
   "options":["This year, I read about Flat Stanley, Despereaux, and Lucy.","this year i read about flat stanley despereaux and lucy.","This Year, I read about Flat stanley, despereaux, And Lucy."],"answer":0,
   "from":"32.4 DOL (commas in a list), 32.1–32.4 year review passages (capitals on names)","status":"fixed (old Q1 named Joan of Arc)"},
  {"n":2,"section":"Grammar","type":"essay_question","points":1,"text":"Fix all the mistakes. Write the sentence correctly: lucys brother didnt believe her and she goed back to narnia.",
   "from":"32.1–32.4 year review passages (capitals, apostrophes, irregular past, comma before and)","status":"fixed (old sentence tested are/our, not taught this week)"},
  {"n":3,"section":"Grammar","type":"essay_question","points":1,"text":"Write two or three sentences about your favorite book from this year. Check your capitals, commas and apostrophes before you finish.",
   "from":"32.1–32.4 Grammar (final editing review)","status":"kept"},
  {"n":4,"section":"Word Parts","type":"multiple_choice_question","points":1,"text":"What does the ending -ous mean in the word courageous?",
   "options":["full of","without","again"],"answer":0,"from":"32.1 table, 32.2 match, 32.3 build (courage + ous = full of courage)","status":"new"},
  {"n":5,"section":"Word Parts","type":"multiple_choice_question","points":1,"text":"What is the base word in perseverance?",
   "options":["serve","persevere","ance"],"answer":1,"from":"32.1 table, 32.3 build (persevere + ance)","status":"fixed (old Q5 tested reformation, not taught)"},
  {"n":6,"section":"Vocabulary","type":"multiple_choice_question","points":1,"text":"The Princess Pea could feel what other people felt. Which word fits her best?",
   "options":["integrity","empathy","resilience"],"answer":1,"from":"32.1 vocabulary (word bank + match), 32.3 pick the word","status":"fixed (old Q6 was open-ended about any word from the year)"},
  {"n":7,"section":"Spelling","type":"multiple_choice_question","points":1,"text":"Which word dropped a silent e before adding -ing?",
   "options":["taking","jumping","sitting"],"answer":0,"from":"32.1 rule, 32.2 rule rows, 32.4 dice (drop the silent e)","status":"new"},
  {"n":8,"section":"Spelling","type":"multiple_choice_question","points":1,"text":"Which word changed y to i before adding an ending?",
   "options":["plays","cities","toys"],"answer":1,"from":"32.2 rule rows, 32.3 proofread, 32.4 dice (change y to i)","status":"new"},
  {"n":9,"section":"Spelling","type":"essay_question","points":1,"text":"Fix the spelling of each word. Then write the rule you used: hopeing, babys, runing.",
   "from":"32.1–32.4 Spelling (find the base word, then the rule)","status":"fixed (old list had projecttion and reformation)"},
  {"n":10,"section":"Reading","type":"multiple_choice_question","points":1,"text":"According to the passage, which pillar means helping others without expecting a reward?",
   "options":["Courage","Service","Perseverance"],"answer":1,"from":"32.1 The 7 Pillars of Virtue","status":"new (passage is now this week’s 7 pillars text)"},
  {"n":11,"section":"Reading","type":"multiple_choice_question","points":1,"text":"In The Whipping Boy, Jemmy orders the outlaws, “Lay down the whip,” to stop them from whipping the prince. Which pillar does this show?",
   "options":["Courage","Courtesy","Honesty"],"answer":0,"from":"32.1 pillars card (Courage example), 32.2 Pillar Watch","status":"new"},
  {"n":12,"section":"Reading","type":"multiple_choice_question","points":1,"text":"In The Lion, the Witch and the Wardrobe, Edmund says “I’m sorry” to each of his brother and sisters. Which pillar does this show?",
   "options":["Service","Perseverance","Responsibility"],"answer":2,"from":"32.1 pillars card (Responsibility example), 32.3 Pillar Watch, Clara’s model","status":"new"},
  {"n":13,"section":"Writing","type":"essay_question","points":1,"text":"Mrs. Lambchop says, “It is wrong to dislike people for their shapes. Or their religion, for that matter, or the color of their skin.” Write your own sentence about something you believe. Stop it early, then add more with Or.",
   "from":"32.2 Read Like a Writer (Flat Stanley)","status":"fixed (old model sentence was not from the week)"},
  {"n":14,"section":"Writing","type":"essay_question","points":1,"text":"Write the opening of a response: name one character from this year’s books, the book, and the one pillar that matters most for that character. Tell why in one sentence.",
   "from":"32.1–32.4 Writer’s Workshop (culmination response: opening with a claim)","status":"fixed (old Q14 was a general portfolio reflection)"}
 ],
 "passage": {"before": 10, "title": "Reading passage (The 7 Pillars of Virtue, written for Optima Academy Online)",
   "text": "The 7 Pillars of Virtue are honesty, respect, courtesy, responsibility, courage, service and perseverance. Courage means acting even when you are afraid, because something matters more than your fear. Service means helping others without expecting a reward. Perseverance means continuing to try even when things are hard."}
}
io.open('assessments/g3-ela-wk32-checkin.json', 'w', encoding='utf-8').write(json.dumps(Q, ensure_ascii=False, indent=1))
e = html.escape
rows = ''
for q in Q['questions']:
    if q['n'] == Q['passage']['before']:
        rows += '<div class="psg"><b>%s</b><p>%s</p></div>' % (e(Q['passage']['title']), e(Q['passage']['text']))
    opts = ''
    if 'options' in q:
        opts = '<ol type="A">' + ''.join('<li%s>%s%s</li>' % (' class="ok"' if i == q['answer'] else '', e(o), ' ✓' if i == q['answer'] else '') for i, o in enumerate(q['options'])) + '</ol>'
    kind = 'Multiple choice (auto-graded)' if q['type'] != 'essay_question' else 'Written (teacher-graded)'
    rows += ('<div class="q %s"><div class="h"><span class="n">%d</span> %s · %s · %d pt</div><p>%s</p>%s<div class="m">Taught in: %s<br>Audit: %s</div></div>'
             % ('new' if q['status'].startswith(('new', 'fixed')) else '', q['n'], e(q['section']), kind, q['points'], e(q['text']), opts, e(q['from']), e(q['status'])))
page = '''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Week 32 Check-In Key</title>
<style>body{font:16px/1.5 system-ui,sans-serif;max-width:820px;margin:0 auto;padding:16px;background:#F0F2F8;color:#24324F}
h1{font-size:22px;color:#0E1C42}.q,.psg{background:#fff;border:1px solid #D9E0F0;border-radius:10px;padding:12px 16px;margin:12px 0}
.q.new{border-left:5px solid #2B5BA8}.psg{background:#FFF8E6}.h{font-weight:700;color:#0E1C42}.n{display:inline-block;background:#0E1C42;color:#fff;border-radius:50%%;width:26px;height:26px;text-align:center;line-height:26px;margin-right:6px}
.ok{color:#24502A;font-weight:700}.m{font-size:13px;color:#6B7690;margin-top:6px}</style></head><body>
<h1>%s</h1><p>%s</p><p><b>Quarter 4 · %s · %d questions · %d points.</b> Blue edge = fixed or new question.</p>%s</body></html>''' % (
    e(Q['title']), e(Q['description']), e(Q['chapters']), len(Q['questions']), sum(q['points'] for q in Q['questions']), rows)
io.open('assessments/g3-ela-wk32-checkin-key.html', 'w', encoding='utf-8').write(page)
print('ok')
