#!/usr/bin/env python3
"""Week 31 check-in as a Canvas quiz: JSON source of truth + readable key. Audit: claude/g3-ela-wk31-audit.md findings 15-16
(old check-in named Joan of Arc 4 times, had an invented "synthesis" passage and tested character comparison across the
year, which this week does not teach). Passage = Text 1, "What Is Courage?" (written for Optima; as corrected in acc_wk31.py).
DRAFT until Bethany approves; .zip only after that."""
import json, io, html
Q = {
 "id": "g3-ela-wk31-checkin",
 "title": "Week 31 Check-In · Paired Texts: The Courage to Act",
 "description": "This week you read two texts about courage: an informational text, “What Is Courage?”, and a made-up story, “The Choice at the Bridge.” You compared how the two authors write about courage, reviewed prefixes and suffixes, split long words into syllables, and reviewed grammar from the whole year.",
 "quarter": 4, "chapters": "Text 1 + Text 2",
 "questions": [
  {"n":1,"section":"Grammar","type":"multiple_choice_question","points":1,"text":"Which sentence is written correctly?",
   "options":["Although Mira was scared, she walked onto the bridge.","although Mira was scared she walked onto the bridge.","Although mira was scared, she goed onto the bridge."],"answer":0,
   "from":"31.1 year review passage, 31.2 DOL (comma after the opening part)","status":"new (old Q1 named Joan of Arc)"},
  {"n":2,"section":"Grammar","type":"essay_question","points":1,"text":"Fix all the mistakes. Write the sentences correctly: after a long moment the three boys walked away. mira didnt feel brave but she was.",
   "from":"31.1, 31.2 and 31.4 year review passages; 31.3 editor sentence","status":"fixed (old sentence used “Prince Horace … was friends”)"},
  {"n":3,"section":"Grammar","type":"essay_question","points":1,"text":"Write two sentences about Text 2: one compound sentence (two complete thoughts joined by and, but or so) and one complex sentence (starting with although, when or because).",
   "from":"31.2 Grammar (simple, compound, complex)","status":"fixed (old Q3 compared characters from the year)"},
  {"n":4,"section":"Word Parts","type":"multiple_choice_question","points":1,"text":"The prefix un- means “not.” What does unlucky mean?",
   "options":["It means not lucky.","It means very lucky.","It means lucky again."],"answer":0,
   "from":"31.1 table, 31.2 match, 31.4 dice (un- = not)","status":"new"},
  {"n":5,"section":"Word Parts","type":"multiple_choice_question","points":1,"text":"The suffix -less means “without.” Which word means “without fear”?",
   "options":["fearful","fearless","feared"],"answer":1,"from":"31.1 table and build (fear + less)","status":"kept"},
  {"n":6,"section":"Word Parts","type":"essay_question","points":1,"text":"Choose one prefix (re-, un-, trans- or inter-) and one suffix (-ful or -less). Write what each one means, and one word that uses each.",
   "from":"31.1–31.4 Morphology","status":"fixed (no longer asks about a character from the year)"},
  {"n":7,"section":"Spelling","type":"multiple_choice_question","points":1,"text":"How many syllables (beats) are in the word remember?",
   "options":["2","3","4"],"answer":1,"from":"31.2 tap the long words, 31.4 dice (count the beats)","status":"new"},
  {"n":8,"section":"Spelling","type":"essay_question","points":1,"text":"Split each word into its syllables, like this: res-cue. Then write how many beats each one has: together, wonderful, important.",
   "from":"31.1 rule, 31.3 syllable tiles, 31.4 dice","status":"fixed (old list had reformation and impossible)"},
  {"n":9,"section":"Spelling","type":"multiple_choice_question","points":1,"text":"Which word is split into syllables the right way?",
   "options":["car-pen-ter","ca-rpen-ter","carp-ent-er"],"answer":0,"from":"31.1 rule (find the vowels, split between them)","status":"new"},
  {"n":10,"section":"Reading","type":"multiple_choice_question","points":1,"text":"According to the passage from Text 1, what makes an act courageous?",
   "options":["The person has no fear at all.","The person chooses to act anyway, because it is important or right.","The person is the strongest one there."],"answer":1,
   "from":"31.1 Q1, 31.4 Read Like a Writer","status":"new (passage is now from this week’s Text 1)"},
  {"n":11,"section":"Reading","type":"essay_question","points":1,"text":"In Text 2, how does the author show that Mira is afraid without using the word afraid? Give one detail from the story.",
   "from":"31.2 Q1 and Read Like a Writer","status":"new"},
  {"n":12,"section":"Reading","type":"essay_question","points":1,"text":"How are Text 1 and Text 2 alike? How are they different? Write one sentence for each.",
   "from":"31.1–31.4 What Good Readers Do (compare two authors on one topic), 31.2 Q3","status":"fixed (old Q12 asked about characters from the whole year)"},
  {"n":13,"section":"Writing","type":"essay_question","points":1,"text":"Model sentence from Text 2: “Her voice came out steadier than she expected.” Write your own sentence about someone who was braver than they thought they would be. Use the same shape: Her (or His) ___ came out ___ than ___ expected.",
   "from":"31.2–31.4 Read Like a Writer (show, don’t tell)","status":"fixed (old model sentence put Despereaux beside Joan of Arc)"},
  {"n":14,"section":"Writing","type":"essay_question","points":1,"text":"Write your claim: one sentence that tells what both texts say about courage.",
   "from":"31.1–31.4 Writer’s Workshop (comparison response: plan and claim)","status":"fixed (old Q14 was a character comparison topic sentence)"}
 ],
 "passage": {"before": 10, "title": "Reading passage (Text 1, “What Is Courage?”, written for Optima Academy Online)",
   "text": "Courage is not the same as having no fear. In fact, most courageous acts involve fear. What makes an act courageous is that the person chooses to act anyway — because they believe the action is important or right."}
}
io.open('assessments/g3-ela-wk31-checkin.json', 'w', encoding='utf-8').write(json.dumps(Q, ensure_ascii=False, indent=1))
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
page = '''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Week 31 Check-In Key</title>
<style>body{font:16px/1.5 system-ui,sans-serif;max-width:820px;margin:0 auto;padding:16px;background:#F0F2F8;color:#24324F}
h1{font-size:22px;color:#0E1C42}.q,.psg{background:#fff;border:1px solid #D9E0F0;border-radius:10px;padding:12px 16px;margin:12px 0}
.q.new{border-left:5px solid #2B5BA8}.psg{background:#FFF8E6}.h{font-weight:700;color:#0E1C42}.n{display:inline-block;background:#0E1C42;color:#fff;border-radius:50%%;width:26px;height:26px;text-align:center;line-height:26px;margin-right:6px}
.ok{color:#24502A;font-weight:700}.m{font-size:13px;color:#6B7690;margin-top:6px}</style></head><body>
<h1>%s</h1><p>%s</p><p><b>Quarter 4 · %s · %d questions · %d points.</b> Blue edge = fixed or new question.</p>%s</body></html>''' % (
    e(Q['title']), e(Q['description']), e(Q['chapters']), len(Q['questions']), sum(q['points'] for q in Q['questions']), rows)
io.open('assessments/g3-ela-wk31-checkin-key.html', 'w', encoding='utf-8').write(page)
print('ok')
