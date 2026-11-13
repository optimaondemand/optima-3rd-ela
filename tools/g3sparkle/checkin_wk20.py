#!/usr/bin/env python3
"""Week 20 check-in as a Canvas quiz: JSON source of truth + readable key."""
import json, io, html
Q = {
 "id": "g3-ela-wk20-checkin",
 "title": "Week 20 Check-In · The Whipping Boy",
 "description": "This week the prince gave away Jemmy’s hiding place, Jemmy ran for the forest, the boys met Betsy, and Jemmy went back for the prince. You practiced prepositions, the root spect (look), long words, and soft c and g. Show what you know!",
 "quarter": 3, "chapters": "Ch. 11–15",
 "questions": [
  {"n":1,"section":"Grammar","type":"multiple_choice_question","points":1,"text":"Which word in this sentence is a preposition? “Jemmy hid under the straw.”",
   "options":["hid","under","Jemmy"],"answer":1,"from":"20.1 sort, 20.2 tap every preposition","status":"fixed (option “barn” removed; there is no barn in the book)"},
  {"n":2,"section":"Grammar","type":"essay_question","points":1,"text":"Fill in the prepositions and write the whole sentence: “Jemmy crept ___ the dark forest and hid ___ a hollow tree.” (Use: through, inside)",
   "from":"20.3 Grammar (pick the preposition)","status":"kept"},
  {"n":3,"section":"Grammar","type":"essay_question","points":1,"text":"Write a sentence that tells where a character is hiding. Use at least one preposition.",
   "from":"20.1–20.3 Grammar (prepositions that tell where)","status":"kept"},
  {"n":4,"section":"Morphology","type":"essay_question","points":1,"text":"The root spect means “look.” Break apart the word inspect. What does it mean?",
   "from":"20.1 notice, 20.3 build (in + spect)","status":"new (old Q4 tested the suffix -est, not taught)"},
  {"n":5,"section":"Morphology","type":"multiple_choice_question","points":1,"text":"The root spect means “look.” A spectator at a game —",
   "options":["watches the game","carries the ball","writes about the game"],"answer":0,"from":"20.1–20.2 Morphology (spect + ator)","status":"new (old Q5 tested -est)"},
  {"n":6,"section":"Morphology","type":"essay_question","points":1,"text":"Choose one: respect, inspector, or suspect. Write a sentence that shows what the word means.",
   "from":"20.2 match, 20.4 dice","status":"new (old Q6 tested -est)"},
  {"n":7,"section":"Spelling","type":"essay_question","points":1,"text":"Split each long word into beats with slash marks (example: im/por/tant). wonderful · remember · together",
   "from":"20.1–20.4 Spelling (find the vowels, split, read each chunk)","status":"new (old Q7 tested r-controlled syllables, not taught)"},
  {"n":8,"section":"Spelling","type":"multiple_choice_question","points":1,"text":"Which word has three syllables?",
   "options":["garden","adventure","basket"],"answer":1,"from":"20.2 Sound Detective, 20.3 Syllable Tiles","status":"new (old Q8 tested r-controlled syllables)"},
  {"n":9,"section":"Spelling","type":"multiple_choice_question","points":1,"text":"Which word has a soft g, like the g in giant?",
   "options":["gentle","gold","garlic"],"answer":0,"from":"20.2 Spelling Bonus (soft c and soft g)","status":"new (old Q9 tested r-controlled syllables)"},
  {"n":10,"section":"Reading","type":"essay_question","points":1,"text":"What did the prince do that gave Jemmy away? Use a detail from the passage.",
   "from":"20.1 Chapter Thinking Q1 (Ch. 12)","status":"kept"},
  {"n":11,"section":"Reading","type":"essay_question","points":1,"text":"Jemmy asked the prince to tell Cutwater he slipped out the door. Why is the prince’s answer such a surprise to Jemmy?",
   "from":"20.1 Chapter Thinking Q2","status":"fixed (old question was built on “Jemmy had trusted no one his whole life,” which the book does not say)"},
  {"n":12,"section":"Reading","type":"essay_question","points":1,"text":"Do you think the prince knew how wrong his choice was? Use what you know about his character to explain.",
   "from":"20.1 Q3, 20.2 Q2 (Then I forgive you)","status":"kept"},
  {"n":13,"section":"Writing","type":"essay_question","points":1,"text":"Model sentence: “Under the moldy straw, Jemmy held very still and waited for his chance to run.” Notice how the prepositional phrase at the start puts you right into the scene. Write your own sentence that begins with a prepositional phrase.",
   "from":"20.1–20.4 prepositions","status":"kept"},
  {"n":14,"section":"Writing","type":"essay_question","points":1,"text":"In Chapter 15, Jemmy has the coach stop for the prince. Write 1–2 sentences: why do you think Jemmy went back for him?",
   "from":"20.3 Chapter Thinking Q3, 20.4 Q1","status":"new (old Q14 asked the same thing as Q12)"}
 ],
 "passage": {"before": 10, "title": "Reading passage (summary of Ch. 12–13)",
   "text": "Jemmy burrowed under the moldy straw in the outlaws’ hut, waiting for his chance to slip away. He asked the prince to tell Cutwater that he had slipped out the door. But when Cutwater asked where the prince was, Prince Brat answered right away: “Him? Over there. Under the straw.” Jemmy burst out of the straw and ran for his life, with Cutwater close behind. But this, he had not expected: when he finally stopped running, the prince had followed him."}
}
io.open('assessments/g3-ela-wk20-checkin.json', 'w', encoding='utf-8').write(json.dumps(Q, ensure_ascii=False, indent=1))
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
page = '''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Week 20 Check-In Key</title>
<style>body{font:16px/1.5 system-ui,sans-serif;max-width:820px;margin:0 auto;padding:16px;background:#F0F2F8;color:#24324F}
h1{font-size:22px;color:#0E1C42}.q,.psg{background:#fff;border:1px solid #D9E0F0;border-radius:10px;padding:12px 16px;margin:12px 0}
.q.new{border-left:5px solid #2B5BA8}.psg{background:#FFF8E6}.h{font-weight:700;color:#0E1C42}.n{display:inline-block;background:#0E1C42;color:#fff;border-radius:50%%;width:26px;height:26px;text-align:center;line-height:26px;margin-right:6px}
.ok{color:#24502A;font-weight:700}.m{font-size:13px;color:#6B7690;margin-top:6px}</style></head><body>
<h1>%s</h1><p>%s</p><p><b>Quarter 3 · %s · %d questions · %d points.</b> Blue edge = new question (the old one tested something week 20 doesn’t teach).</p>%s</body></html>''' % (
    e(Q['title']), e(Q['description']), e(Q['chapters']), len(Q['questions']), sum(q['points'] for q in Q['questions']), rows)
io.open('assessments/g3-ela-wk20-checkin-key.html', 'w', encoding='utf-8').write(page)
print('ok')
