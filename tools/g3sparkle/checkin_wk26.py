#!/usr/bin/env python3
"""Week 26 check-in as a Canvas quiz: JSON source of truth + readable key. Audit: claude/g3-ela-wk26-audit.md findings 16-19.
Passage = The Lion, the Witch and the Wardrobe, Ch. 4 (the same lines as the week 26 fluency page), checked against
Planning docs/lww_text.txt."""
import json, io, html
Q = {
 "id": "g3-ela-wk26-checkin",
 "title": "Week 26 Check-In · The Lion, the Witch and the Wardrobe",
 "description": "This week you read Chapters 4 to 6: Edmund meets the Queen, lies about Narnia, and all four children step through the wardrobe. You practiced keeping verbs in the same tense, the root form (shape), and counting the beats in long school words. Show what you know!",
 "quarter": 4, "chapters": "Ch. 4–6",
 "questions": [
  {"n":1,"section":"Grammar","type":"multiple_choice_question","points":1,"text":"Which sentence has a verb tense mistake?",
   "options":["Edmund walked into Narnia and felt the cold air.","Edmund walked into Narnia and feels the cold air.","Edmund walks into Narnia and feels the cold air."],"answer":1,"from":"26.1 The Rule, 26.2 find the slipped verb","status":"kept"},
  {"n":2,"section":"Grammar","type":"essay_question","points":1,"text":"Fix the verb that slipped, and write the sentence: “The Queen smiled at Edmund and gives him a hot drink.”",
   "from":"26.2 fix the paragraph, 26.3 rewrite in the past","status":"fixed (old sentence said she offered more Turkish Delight; she refused)"},
  {"n":3,"section":"Grammar","type":"essay_question","points":1,"text":"Write 2–3 sentences, all in the past tense, about what happens when Edmund meets the Queen.",
   "from":"26.3 rewrite in the past","status":"kept (wording made plain)"},
  {"n":4,"section":"Morphology","type":"essay_question","points":1,"text":"The root form means shape. Break apart the word transform. What does it mean?",
   "from":"26.1 See what was hiding, 26.2 match","status":"new (old Q4 tested the prefix trans- as its own skill, with transport, never taught)"},
  {"n":5,"section":"Morphology","type":"multiple_choice_question","points":1,"text":"A uniform is —",
   "options":["clothes that look the same for everyone in a group","a shape that keeps changing","a word that means far away"],"answer":0,"from":"26.1–26.3 Morphology","status":"new"},
  {"n":6,"section":"Morphology","type":"essay_question","points":1,"text":"Choose one: uniform, reform or transform. Write a sentence that shows what the word means.",
   "from":"26.1–26.4 Morphology","status":"new (old Q6 used transport and translate)"},
  {"n":7,"section":"Spelling","type":"multiple_choice_question","points":1,"text":"Clap the word information. How many beats does it have?",
   "options":["3","4","5"],"answer":1,"from":"26.1 sort, 26.3 split it","status":"new (old Q7 tested vowel teams)"},
  {"n":8,"section":"Spelling","type":"essay_question","points":1,"text":"Why do you count vowel sounds, not vowel letters, to find the beats in a word? Use the word detail in your answer.",
   "from":"26.1 See the Rule, 26.2 Beat Detective","status":"new (old Q8 tested vowel teams)"},
  {"n":9,"section":"Spelling","type":"multiple_choice_question","points":1,"text":"Which word has five beats?",
   "options":["summary","imagination","sequence"],"answer":1,"from":"26.2 Beat Detective, 26.3 split it","status":"new (old Q9 tested a vowel-team spelling)"},
  {"n":10,"section":"Reading","type":"essay_question","points":1,"text":"What does the Queen keep doing while Edmund eats? Use a detail from the passage.",
   "from":"26.1 Q1–Q2 (Edmund's choice, the Witch's plan)","status":"fixed (passage is now the book’s own words)"},
  {"n":11,"section":"Reading","type":"essay_question","points":1,"text":"The passage says Edmund “never asked himself why the Queen should be so inquisitive.” What should Edmund have wondered about? Why?",
   "from":"26.1 Q1, What Good Readers Do (ask what they knew)","status":"replaced (old Q11 quoted a line the passage invented)"},
  {"n":12,"section":"Reading","type":"essay_question","points":1,"text":"Is Edmund responsible for his choices in Chapters 4 and 5, or is the enchanted Turkish Delight mostly to blame? Use details to support your opinion.",
   "from":"26.4 Q1–Q2; Truth Watch","status":"kept (chapters named)"},
  {"n":13,"section":"Writing","type":"essay_question","points":1,"text":"Model sentence from the book: “The more he ate the more he wanted to eat, and he never asked himself why the Queen should be so inquisitive.” Write your own sentence that starts with “The more…” and shows one thing leading to another.",
   "from":"26.1 banner; 26.4 Writer’s Workshop","status":"fixed (old model sentence was invented)"},
  {"n":14,"section":"Writing","type":"essay_question","points":1,"text":"What did Edmund want, and how did the Queen use that to get what she wanted? Write 1–2 sentences.",
   "from":"26.1 Q2; Writer’s Workshop (choice, reason, consequence)","status":"kept (wording made plain)"}
 ],
 "passage": {"before": 10, "title": "Reading passage (The Lion, the Witch and the Wardrobe, Chapter 4)",
   "text": "While he was eating the Queen kept asking him questions. At first Edmund tried to remember that it is rude to speak with one’s mouth full, but soon he forgot about this and thought only of trying to shovel down as much Turkish Delight as he could, and the more he ate the more he wanted to eat, and he never asked himself why the Queen should be so inquisitive. She got him to tell her that he had one brother and two sisters, and that one of his sisters had already been in Narnia and had met a Faun there.\n— C.S. Lewis, The Lion, the Witch and the Wardrobe, Chapter 4"}
}
io.open('assessments/g3-ela-wk26-checkin.json', 'w', encoding='utf-8').write(json.dumps(Q, ensure_ascii=False, indent=1))
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
             % ('new' if q['status'].startswith('new') else '', q['n'], e(q['section']), kind, q['points'], e(q['text']), opts, e(q['from']), e(q['status'])))
page = '''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Week 26 Check-In Key</title>
<style>body{font:16px/1.5 system-ui,sans-serif;max-width:820px;margin:0 auto;padding:16px;background:#F0F2F8;color:#24324F}
h1{font-size:22px;color:#0E1C42}.q,.psg{background:#fff;border:1px solid #D9E0F0;border-radius:10px;padding:12px 16px;margin:12px 0}
.q.new{border-left:5px solid #2B5BA8}.psg{background:#FFF8E6}.h{font-weight:700;color:#0E1C42}.n{display:inline-block;background:#0E1C42;color:#fff;border-radius:50%%;width:26px;height:26px;text-align:center;line-height:26px;margin-right:6px}
.ok{color:#24502A;font-weight:700}.m{font-size:13px;color:#6B7690;margin-top:6px}</style></head><body>
<h1>%s</h1><p>%s</p><p><b>Quarter 4 · %s · %d questions · %d points.</b> Blue edge = new question (the old one tested something week 26 doesn’t teach).</p>%s</body></html>''' % (
    e(Q['title']), e(Q['description']), e(Q['chapters']), len(Q['questions']), sum(q['points'] for q in Q['questions']), rows)
io.open('assessments/g3-ela-wk26-checkin-key.html', 'w', encoding='utf-8').write(page)
print('ok')
