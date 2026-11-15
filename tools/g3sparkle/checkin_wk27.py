#!/usr/bin/env python3
"""Week 27 check-in as a Canvas quiz: JSON source of truth + readable key. Audit: claude/g3-ela-wk27-audit.md findings 22-26.
Passage = The Lion, the Witch and the Wardrobe, Ch. 7 (the same lines as the week 27 fluency page), checked against
Planning docs/lww_text.txt. DRAFT until Bethany approves; .zip only after that."""
import json, io, html
Q = {
 "id": "g3-ela-wk27-checkin",
 "title": "Week 27 Check-In · The Lion, the Witch and the Wardrobe",
 "description": "This week you read Chapters 7 to 9: the children meet the Beavers and hear the name Aslan, and Edmund slips away to the White Witch's house. You practiced irregular verbs, the word parts in- and im- (they mean not), and reading words built from a prefix and a base word. Show what you know!",
 "quarter": 4, "chapters": "Ch. 7–9",
 "questions": [
  {"n":1,"section":"Grammar","type":"multiple_choice_question","points":1,"text":"Which sentence uses the right past-tense verb?",
   "options":["The children runned to the Beavers' house.","The children ran to the Beavers' house.","The children runed to the Beavers' house."],"answer":1,"from":"27.1 The Rule + passage, 27.2 Now check your thinking","status":"kept"},
  {"n":2,"section":"Grammar","type":"essay_question","points":1,"text":"Fix the verb, and write the sentence the right way: “Mr. Beaver telled them everything about Aslan and the White Witch.”",
   "from":"27.2 four sentences (telled → told), 27.3 fix the sentence","status":"kept (Ch. 8 fact checked)"},
  {"n":3,"section":"Grammar","type":"essay_question","points":1,"text":"Write a sentence in the past tense about what the children did at the Beavers' house. Use at least one irregular verb, like ate, saw, told, went or sat.",
   "from":"27.3 fix the sentence + list three more verbs","status":"kept (wording made plain)"},
  {"n":4,"section":"Word Parts","type":"essay_question","points":1,"text":"The word parts in- and im- both mean not. Break apart the word impatient. What does it mean?",
   "from":"27.1 See if you were right, 27.2 match, 27.3 build","status":"new (old Q4 tested the root form, from week 26)"},
  {"n":5,"section":"Word Parts","type":"multiple_choice_question","points":1,"text":"Which word means “not able to be seen”?",
   "options":["imvisible","invisible","revisible"],"answer":1,"from":"27.1–27.4 Morphology (im- only before m or p)","status":"new (old Q5 tested uniform)"},
  {"n":6,"section":"Word Parts","type":"essay_question","points":1,"text":"Choose one: impossible, incorrect or invisible. Write a sentence that shows what the word means.",
   "from":"27.1–27.4 Morphology","status":"new (old Q6 used reform, inform, uniform)"},
  {"n":7,"section":"Spelling","type":"multiple_choice_question","points":1,"text":"Which word is built from a prefix and a base word?",
   "options":["ribbon","rewrite","ready"],"answer":1,"from":"27.1 sort, 27.2 prefix hunt","status":"replaced (old Q7 asked students to underline and circle, which Canvas can't do)"},
  {"n":8,"section":"Spelling","type":"essay_question","points":1,"text":"How does knowing a prefix help you read a word you have never seen before? Give an example.",
   "from":"27.1 Now name the pattern, 27.4 Prefix Dice","status":"kept"},
  {"n":9,"section":"Spelling","type":"multiple_choice_question","points":1,"text":"One word is spelled wrong. Which one?",
   "options":["unhappy","remak","disobey"],"answer":1,"from":"27.3 Proofreader","status":"kept (now auto-graded)"},
  {"n":10,"section":"Reading","type":"essay_question","points":1,"text":"How does each child feel when they hear Aslan's name? Use at least two details from the passage.",
   "from":"27.1 Q1","status":"kept (passage is now the book’s own words)"},
  {"n":11,"section":"Reading","type":"essay_question","points":1,"text":"Edmund feels “mysterious horror” while the others feel brave, happy or excited. What does this difference tell us about Edmund?",
   "from":"27.1 Q3","status":"kept"},
  {"n":12,"section":"Reading","type":"essay_question","points":1,"text":"Lucy and Edmund hear the same name, but they feel opposite things. Why do you think they feel so differently? Use what you know about each of them from Chapters 7 to 9.",
   "from":"27.4 Q1–Q3; What Good Readers Do (perspective)","status":"replaced (old Q12 asked about foreshadowing, not taught this week)"},
  {"n":13,"section":"Writing","type":"essay_question","points":1,"text":"Model sentence from the book: “For the mention of Aslan gave him a mysterious and horrible feeling just as it gave the others a mysterious and lovely feeling.” This one sentence shows two opposite feelings about the same thing. Write your own sentence that shows two characters feeling opposite ways about the same thing.",
   "from":"27.1–27.4 Writer’s Workshop (compare two perspectives)","status":"fixed (old model sentence was invented)"},
  {"n":14,"section":"Writing","type":"essay_question","points":1,"text":"Compare how Edmund and one other character see Aslan. Write 1–2 sentences. Use a word like shows, reveals or suggests.",
   "from":"27.2–27.4 Writer’s Workshop","status":"replaced (old Q14 asked about foreshadowing, not taught this week)"}
 ],
 "passage": {"before": 10, "title": "Reading passage (The Lion, the Witch and the Wardrobe, Chapter 7)",
   "text": "None of the children knew who Aslan was any more than you do; but the moment the Beaver had spoken these words everyone felt quite different. At the name of Aslan each one of the children felt something jump in its inside. Edmund felt a sensation of mysterious horror. Peter felt suddenly brave and adventurous. Susan felt as if some delicious smell or some delightful strain of music had just floated by her. And Lucy got the feeling you have when you wake up in the morning and realize that it is the beginning of the holidays or the beginning of summer.\n— C.S. Lewis, The Lion, the Witch and the Wardrobe, Chapter 7"}
}
io.open('assessments/g3-ela-wk27-checkin.json', 'w', encoding='utf-8').write(json.dumps(Q, ensure_ascii=False, indent=1))
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
page = '''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Week 27 Check-In Key</title>
<style>body{font:16px/1.5 system-ui,sans-serif;max-width:820px;margin:0 auto;padding:16px;background:#F0F2F8;color:#24324F}
h1{font-size:22px;color:#0E1C42}.q,.psg{background:#fff;border:1px solid #D9E0F0;border-radius:10px;padding:12px 16px;margin:12px 0}
.q.new{border-left:5px solid #2B5BA8}.psg{background:#FFF8E6}.h{font-weight:700;color:#0E1C42}.n{display:inline-block;background:#0E1C42;color:#fff;border-radius:50%%;width:26px;height:26px;text-align:center;line-height:26px;margin-right:6px}
.ok{color:#24502A;font-weight:700}.m{font-size:13px;color:#6B7690;margin-top:6px}</style></head><body>
<h1>%s</h1><p>%s</p><p><b>Quarter 4 · %s · %d questions · %d points.</b> Blue edge = new question (the old one tested something week 27 doesn’t teach).</p>%s</body></html>''' % (
    e(Q['title']), e(Q['description']), e(Q['chapters']), len(Q['questions']), sum(q['points'] for q in Q['questions']), rows)
io.open('assessments/g3-ela-wk27-checkin-key.html', 'w', encoding='utf-8').write(page)
print('ok')
