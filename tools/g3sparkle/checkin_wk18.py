#!/usr/bin/env python3
"""Week 18 check-in as a Canvas quiz: JSON source of truth + readable key."""
import json, io, html
Q = {
 "id": "g3-ela-wk18-checkin",
 "title": "Week 18 Check-In · The Whipping Boy",
 "description": "This week you started The Whipping Boy and met two very different boys: a spoiled prince and Jemmy, the orphan boy who takes his punishments. You practiced conjunctions (and, but, so), the prefixes inter- and sub-, and vowel team syllables. Show what you know!",
 "quarter": 3, "chapters": "Ch. 1–5",
 "questions": [
  {"n":1,"section":"Grammar","type":"multiple_choice_question","points":1,"text":"Which sentence correctly uses a conjunction to join two ideas?",
   "options":["The prince was spoiled, but Jemmy was clever.","The prince was spoiled but, Jemmy was clever.","The prince was spoiled. But Jemmy was clever."],"answer":0,
   "from":"18.1–18.4 Grammar (and, but, so)","status":"kept"},
  {"n":2,"section":"Grammar","type":"essay_question","points":1,"text":"Combine these two sentences into one using a conjunction: “The prince could not write his name. Jemmy could read and write.”",
   "from":"18.3 Grammar (join each pair)","status":"kept"},
  {"n":3,"section":"Grammar","type":"essay_question","points":1,"text":"Write your own compound sentence using “but” to show a difference between two characters or ideas.",
   "from":"18.1 Grammar SWYK, 18.3 Grammar","status":"kept (one word: contrast → difference, the word the lessons use)"},
  {"n":4,"section":"Morphology","type":"essay_question","points":1,"text":"The prefix inter- means “between.” Break apart the word interrupt. What does it mean?",
   "from":"18.1 Morphology (inter- + rupt)","status":"new (old Q4 tested over-, not taught)"},
  {"n":5,"section":"Morphology","type":"multiple_choice_question","points":1,"text":"The prefix sub- means “under.” A subway train most likely runs —",
   "options":["under the city streets","between two cities","high above the city"],"answer":0,
   "from":"18.1 Morphology (“What does a subway go under?”)","status":"new (old Q5 tested over-)"},
  {"n":6,"section":"Morphology","type":"essay_question","points":1,"text":"Choose one: interrupt, interact, or international. Write a sentence that shows what the word means.",
   "from":"18.1–18.3 Morphology word list","status":"new (old Q6 tested over-)"},
  {"n":7,"section":"Spelling","type":"essay_question","points":1,"text":"Each word has a vowel team. Write each word and split it into syllables with a slash mark (example: rain/bow). season · explain · railroad",
   "from":"18.3 Spelling (Vowel Team Splitter)","status":"new (old Q7 tested closed syllables, not taught)"},
  {"n":8,"section":"Spelling","type":"essay_question","points":1,"text":"A vowel team is two vowels that work together to make one sound. Explain this rule in your own words and give one example word.",
   "from":"18.1 Spelling rule","status":"new (old Q8 tested closed syllables)"},
  {"n":9,"section":"Spelling","type":"multiple_choice_question","points":1,"text":"Which word is split into syllables the wrong way?",
   "options":["rain/bow","se/ason","pea/nut"],"answer":1,
   "from":"18.3 Spelling (a team never gets split up)","status":"new (old Q9 tested closed syllables)"},
  {"n":10,"section":"Reading","type":"essay_question","points":1,"text":"How are Jemmy and Prince Brat different, according to this passage? Use a detail from the text.",
   "from":"18.1 Reading (Ch. 1–2), 18.4 review Q1","status":"kept"},
  {"n":11,"section":"Reading","type":"essay_question","points":1,"text":"Jemmy sat in on the prince’s lessons, but only Jemmy learned. Why do you think Jemmy learned when the prince didn’t? What does this tell you about him?",
   "from":"18.1 Reading (Ch. 2)","status":"kept"},
  {"n":12,"section":"Reading","type":"essay_question","points":1,"text":"Does it seem fair that Jemmy has to take the prince’s punishments? Use details from the passage to explain your thinking.",
   "from":"18.1 Big Question, 18.4 review","status":"kept"},
  {"n":13,"section":"Writing","type":"essay_question","points":1,"text":"Model sentence: “The prince had everything — fine food, warm clothes, and a throne to sit on — but Jemmy had only his wits.” Notice how the dashes and the word “but” show a sharp difference. Write your own sentence that shows a difference between two characters, using this pattern.",
   "from":"18.1–18.4 conjunction but; RWM sentence work","status":"kept"},
  {"n":14,"section":"Writing","type":"essay_question","points":1,"text":"Write 1–2 sentences describing what each boy wants at the start of the story. What does Prince Brat seem to want? What does Jemmy seem to want?",
   "from":"18.1–18.2 Reading; Writer’s Workshop claim","status":"kept"}
 ],
 "passage": {"before": 10, "title": "Reading passage (summary of Ch. 1–2)",
   "text": "The prince was known throughout the kingdom as Prince Brat. He had never been whipped in his life, for it was the law: no one was allowed to strike a prince. Jemmy had been brought to the castle to take his punishments for him. Jemmy had to sit close at hand during the prince’s daily lessons. The prince learned nothing — but Jemmy learned to read, write, and do sums."}
}
io.open('/home/claude/g3/repo/assessments/g3-ela-wk18-checkin.json', 'w', encoding='utf-8').write(json.dumps(Q, ensure_ascii=False, indent=1))
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
page = '''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Week 18 Check-In Key</title>
<style>body{font:16px/1.5 system-ui,sans-serif;max-width:820px;margin:0 auto;padding:16px;background:#F0F2F8;color:#24324F}
h1{font-size:22px;color:#0E1C42}.q,.psg{background:#fff;border:1px solid #D9E0F0;border-radius:10px;padding:12px 16px;margin:12px 0}
.q.new{border-left:5px solid #2B5BA8}.psg{background:#FFF8E6}.h{font-weight:700;color:#0E1C42}.n{display:inline-block;background:#0E1C42;color:#fff;border-radius:50%%;width:26px;height:26px;text-align:center;line-height:26px;margin-right:6px}
.ok{color:#24502A;font-weight:700}.m{font-size:13px;color:#6B7690;margin-top:6px}</style></head><body>
<h1>%s</h1><p>%s</p><p><b>Quarter 3 · %s · %d questions · %d points.</b> Blue edge = new question (the old one tested something week 18 doesn’t teach).</p>%s</body></html>''' % (
    e(Q['title']), e(Q['description']), e(Q['chapters']), len(Q['questions']), sum(q['points'] for q in Q['questions']), rows)
io.open('/home/claude/g3/repo/assessments/g3-ela-wk18-checkin-key.html', 'w', encoding='utf-8').write(page)
print('ok')
