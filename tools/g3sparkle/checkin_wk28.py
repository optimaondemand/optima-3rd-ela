#!/usr/bin/env python3
"""Week 28 check-in as a Canvas quiz: JSON source of truth + readable key. Audit: claude/g3-ela-wk28-audit.md findings 23-27.
Passage = The Lion, the Witch and the Wardrobe, Ch. 11 (the dwarf: "This is no thaw"), checked against Planning docs/lww_text.txt.
DRAFT until Bethany approves; .zip only after that."""
import json, io, html
Q = {
 "id": "g3-ela-wk28-checkin",
 "title": "Week 28 Check-In · The Lion, the Witch and the Wardrobe",
 "description": "This week you read Chapters 10 to 12: Father Christmas comes to Narnia, the snow melts into spring, and Peter fights his first battle. You practiced apostrophes in contractions and words that show belonging, the word parts com- and con- (they mean with or together), and endings that change a base word. Show what you know!",
 "quarter": 4, "chapters": "Ch. 10–12",
 "questions": [
  {"n":1,"section":"Grammar","type":"multiple_choice_question","points":1,"text":"Which sentence uses the apostrophe the right way?",
   "options":["It’s spring in Narnia at last.","Its’ spring in Narnia at last.","Its spring in Narnia at last."],"answer":0,"from":"28.1 Think it through (it’s and its), 28.4 DOL","status":"kept (options now whole sentences)"},
  {"n":2,"section":"Grammar","type":"essay_question","points":1,"text":"Write each contraction as two words: can’t, didn’t, wasn’t.",
   "from":"28.1 Now check your thinking (can’t = can + not), 28.1–28.3 passages","status":"fixed (they’ve swapped for wasn’t; the week only teaches n’t contractions)"},
  {"n":3,"section":"Grammar","type":"essay_question","points":1,"text":"Write two sentences about what happens in Narnia in Chapters 10 to 12. Use one contraction and one word that shows belonging, like Peter’s.",
   "from":"28.1–28.4 Grammar (contractions and possessives)","status":"kept (now asks for both apostrophe jobs)"},
  {"n":4,"section":"Word Parts","type":"essay_question","points":1,"text":"The word parts com- and con- both mean with or together. Break apart the word combine. What does it mean?",
   "from":"28.1 See what was hiding, 28.2 match, 28.3 build","status":"new (old Q4 tested the root script, not taught this week)"},
  {"n":5,"section":"Word Parts","type":"multiple_choice_question","points":1,"text":"Which word means “to join two things together”?",
   "options":["unhook","combine","rebuild"],"answer":1,"from":"28.1–28.4 Morphology","status":"new (old Q5 tested inscription)"},
  {"n":6,"section":"Word Parts","type":"essay_question","points":1,"text":"Choose one: company, connect or conversation. Write a sentence that shows what the word means.",
   "from":"28.1–28.4 Morphology","status":"new (old Q6 used script, describe, inscription)"},
  {"n":7,"section":"Spelling","type":"multiple_choice_question","points":1,"text":"Which word is spelled the right way?",
   "options":["stoped","stopped","stopt"],"answer":1,"from":"28.1 sort (doubled), 28.2 Change Detective","status":"new (old Q7 asked students to underline a root)"},
  {"n":8,"section":"Spelling","type":"essay_question","points":1,"text":"Some endings change the base word before they go on: double the last letter, drop the silent e, or change y to i. Explain one of these changes, and give an example.",
   "from":"28.1 Now name the pattern, 28.4 Which Change Dice","status":"new (old Q8 asked about the root script)"},
  {"n":9,"section":"Spelling","type":"multiple_choice_question","points":1,"text":"One word is spelled wrong. Which one?",
   "options":["carried","shineing","nodding"],"answer":1,"from":"28.1 sort (shining), 28.3 Change It Builder","status":"new (old Q9 tested discribe)"},
  {"n":10,"section":"Reading","type":"essay_question","points":1,"text":"What is happening to Narnia in this passage? Use two details from the passage.",
   "from":"28.2 Q1–Q2","status":"kept (passage is now the book’s own words)"},
  {"n":11,"section":"Reading","type":"essay_question","points":1,"text":"Why is the dwarf so worried when he says “This is Spring”? What does spring mean in Narnia?",
   "from":"28.2 Q1 (the Witch’s response), 28.4 Q2","status":"fixed (old Q11 said the Witch spoke this line; it was the dwarf)"},
  {"n":12,"section":"Reading","type":"essay_question","points":1,"text":"The melting snow is a symbol of hope coming back. What other symbol of hope can you find in Chapters 10 to 12? Explain what it stands for.",
   "from":"28.1 Q1–Q2, 28.4 Q1 and Q3","status":"kept"},
  {"n":13,"section":"Writing","type":"essay_question","points":1,"text":"Model sentence from the book: “And then, as he looked at one tree he saw a great load of snow slide off it and for the first time since he had entered Narnia he saw the dark green of a fir tree.” A small detail (the green of one tree) stands for something big (winter is ending). Write your own sentence where a small detail stands for something bigger.",
   "from":"28.1–28.4 Writer’s Workshop (symbol paragraph)","status":"fixed (old model sentence was invented)"},
  {"n":14,"section":"Writing","type":"essay_question","points":1,"text":"Choose one image from Chapters 10 to 12 (the melting snow, Father Christmas’s gifts, or the spring flowers). Write 1–2 sentences about what it stands for in the story. Use a word like represents, suggests or symbolizes.",
   "from":"28.1–28.4 Writer’s Workshop","status":"kept (green buds swapped for spring flowers, which are in the book; literary verbs from 28.2)"}
 ],
 "passage": {"before": 10, "title": "Reading passage (The Lion, the Witch and the Wardrobe, Chapter 11)",
   "text": "The trees began to come fully alive. The larches and birches were covered with green, the laburnums with gold. Soon the beech trees had put forth their delicate, transparent leaves. … A bee buzzed across their path.\n“This is no thaw,” said the dwarf, suddenly stopping. “This is Spring. What are we to do? Your winter has been destroyed, I tell you! This is Aslan’s doing.”\n— C.S. Lewis, The Lion, the Witch and the Wardrobe, Chapter 11"}
}
io.open('assessments/g3-ela-wk28-checkin.json', 'w', encoding='utf-8').write(json.dumps(Q, ensure_ascii=False, indent=1))
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
page = '''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Week 28 Check-In Key</title>
<style>body{font:16px/1.5 system-ui,sans-serif;max-width:820px;margin:0 auto;padding:16px;background:#F0F2F8;color:#24324F}
h1{font-size:22px;color:#0E1C42}.q,.psg{background:#fff;border:1px solid #D9E0F0;border-radius:10px;padding:12px 16px;margin:12px 0}
.q.new{border-left:5px solid #2B5BA8}.psg{background:#FFF8E6}.h{font-weight:700;color:#0E1C42}.n{display:inline-block;background:#0E1C42;color:#fff;border-radius:50%%;width:26px;height:26px;text-align:center;line-height:26px;margin-right:6px}
.ok{color:#24502A;font-weight:700}.m{font-size:13px;color:#6B7690;margin-top:6px}</style></head><body>
<h1>%s</h1><p>%s</p><p><b>Quarter 4 · %s · %d questions · %d points.</b> Blue edge = new question (the old one tested something week 28 doesn’t teach).</p>%s</body></html>''' % (
    e(Q['title']), e(Q['description']), e(Q['chapters']), len(Q['questions']), sum(q['points'] for q in Q['questions']), rows)
io.open('assessments/g3-ela-wk28-checkin-key.html', 'w', encoding='utf-8').write(page)
print('ok')
