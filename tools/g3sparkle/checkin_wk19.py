#!/usr/bin/env python3
"""Week 19 check-in as a Canvas quiz: JSON source of truth + readable key."""
import json, io, html
Q = {
 "id": "g3-ela-wk19-checkin",
 "title": "Week 19 Check-In · The Whipping Boy",
 "description": "This week the story turned upside down. The outlaws mixed up the two boys, decided Jemmy was the prince, and Jemmy wrote a ransom note to the king. You practiced compound sentences, the root port (carry), and consonant-le syllables. Show what you know!",
 "quarter": 3, "chapters": "Ch. 6–11",
 "questions": [
  {"n":1,"section":"Grammar","type":"multiple_choice_question","points":1,"text":"Which is a correctly punctuated compound sentence?",
   "options":["Jemmy wanted to escape, but the prince refused to move.","Jemmy wanted to escape but, the prince refused to move.","Jemmy wanted to escape but the prince refused to move."],"answer":0,
   "from":"19.3 Grammar (where the comma goes), 19.4 mistake hunt","status":"kept"},
  {"n":2,"section":"Grammar","type":"essay_question","points":1,"text":"Join these into a compound sentence: “The outlaws captured them. Jemmy knew they were in serious trouble.”",
   "from":"19.2 Grammar (two complete thoughts)","status":"kept"},
  {"n":3,"section":"Grammar","type":"essay_question","points":1,"text":"Write your own compound sentence about two characters making different choices.",
   "from":"19.3 Grammar SWYK","status":"kept"},
  {"n":4,"section":"Morphology","type":"essay_question","points":1,"text":"The root port means “carry.” Break apart the word export. What does it mean?",
   "from":"19.1–19.4 Morphology (ex + port)","status":"new (old Q4 tested the suffix -er, not taught)"},
  {"n":5,"section":"Morphology","type":"multiple_choice_question","points":1,"text":"The root port means “carry.” Something that is portable —",
   "options":["can be carried from place to place","must stay in one spot","is too heavy to lift"],"answer":0,
   "from":"19.2 match and 19.3 build (port + able)","status":"new (old Q5 tested -er)"},
  {"n":6,"section":"Morphology","type":"essay_question","points":1,"text":"Choose one: transport, import, or report. Write a sentence that shows what the word means.",
   "from":"19.1 Morphology word list","status":"new (old Q6 tested -er)"},
  {"n":7,"section":"Spelling","type":"essay_question","points":1,"text":"Each word ends in a consonant-le syllable. Write each word and split it into syllables with a slash mark (example: ta/ble). little · candle · purple",
   "from":"19.1 rule, 19.3 Syllable Tiles","status":"new (old Q7 tested open syllables, not taught)"},
  {"n":8,"section":"Spelling","type":"essay_question","points":1,"text":"Explain the consonant-le rule in your own words. Give one example word.",
   "from":"19.1 Spelling rule","status":"new (old Q8 tested open syllables)"},
  {"n":9,"section":"Spelling","type":"multiple_choice_question","points":1,"text":"Which word is split into syllables the right way?",
   "options":["can/dle","cand/le","ca/ndle"],"answer":0,
   "from":"19.1–19.4 Spelling (the consonant goes with -le)","status":"new (old Q9 tested open syllables)"},
  {"n":10,"section":"Reading","type":"essay_question","points":1,"text":"What do the outlaws plan to do with the boy they think is the prince? Use a detail from the passage.",
   "from":"19.1–19.2 Reading (Ch. 6–8)","status":"kept"},
  {"n":11,"section":"Reading","type":"essay_question","points":1,"text":"The passage says being royal “didn’t seem to be any advantage at all.” What does this mean? Why is it surprising, given how the story started?",
   "from":"19.1 Q2 (who has power now)","status":"kept (“ironic” → “surprising”; ironic is not taught)"},
  {"n":12,"section":"Reading","type":"essay_question","points":1,"text":"Do you think Jemmy or the prince is better prepared for this situation? Use details to explain your thinking.",
   "from":"19.4 review Q3 (who is cleverer)","status":"kept"},
  {"n":13,"section":"Writing","type":"essay_question","points":1,"text":"Model sentence: “The prince could have gone home, but he stayed — and Jemmy was struck dumb.” Notice the contrast (could have / but), the dash, and the short ending. Write your own sentence about a character’s choice using this pattern.",
   "from":"19.1–19.4 compound sentences with but; 19.3 Ch. 11","status":"fixed (old model said Jemmy stayed instead of running; that is not what happens)"},
  {"n":14,"section":"Writing","type":"essay_question","points":1,"text":"The prince is used to giving orders, but now he has no power. Write 1–2 sentences predicting how this situation might change him.",
   "from":"19.4 Big Question (is anyone changing?)","status":"kept"}
 ],
 "passage": {"before": 10, "title": "Reading passage (summary of Ch. 7–8)",
   "text": "Hold-Your-Nose Billy watched the two boys closely. The ragged whipping boy knew his letters, but the boy who called himself a prince could not even sign his own name. “Something’s amiss here,” Billy said. He decided Jemmy must be the real prince and made plans to trade him to the king for a ransom of gold. The real prince shouted that he was His Royal Highness, but Billy told him to hush. For the first time, being royal didn’t seem to be any advantage at all."}
}
io.open('/home/claude/g3/repo/assessments/g3-ela-wk19-checkin.json', 'w', encoding='utf-8').write(json.dumps(Q, ensure_ascii=False, indent=1))
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
             % ('new' if q['status'].startswith('new') else '', q['n'], e(q['section']), kind, q['points'], e(q['text']), opts, e(q['from']), e(q['status'])))
page = '''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Week 19 Check-In Key</title>
<style>body{font:16px/1.5 system-ui,sans-serif;max-width:820px;margin:0 auto;padding:16px;background:#F0F2F8;color:#24324F}
h1{font-size:22px;color:#0E1C42}.q,.psg{background:#fff;border:1px solid #D9E0F0;border-radius:10px;padding:12px 16px;margin:12px 0}
.q.new{border-left:5px solid #2B5BA8}.psg{background:#FFF8E6}.h{font-weight:700;color:#0E1C42}.n{display:inline-block;background:#0E1C42;color:#fff;border-radius:50%%;width:26px;height:26px;text-align:center;line-height:26px;margin-right:6px}
.ok{color:#24502A;font-weight:700}.m{font-size:13px;color:#6B7690;margin-top:6px}</style></head><body>
<h1>%s</h1><p>%s</p><p><b>Quarter 3 · %s · %d questions · %d points.</b> Blue edge = new question (the old one tested something week 19 doesn’t teach).</p>%s</body></html>''' % (
    e(Q['title']), e(Q['description']), e(Q['chapters']), len(Q['questions']), sum(q['points'] for q in Q['questions']), rows)
io.open('/home/claude/g3/repo/assessments/g3-ela-wk19-checkin-key.html', 'w', encoding='utf-8').write(page)
print('ok')
