#!/usr/bin/env python3
"""Week 23 check-in as a Canvas quiz: JSON source of truth + readable key."""
import json, io, html
Q = {
 "id": "g3-ela-wk23-checkin",
 "title": "Week 23 Check-In · Medieval Nonfiction",
 "description": "This week you read four true articles about life in the Middle Ages: castles, apprentices, royal courts and food. You found the central idea, practiced capital letters for names, places and titles, the word part trans (across), and splitting VCCV words. Show what you know!",
 "quarter": 3, "chapters": "Articles 23.1–23.4",
 "questions": [
  {"n":1,"section":"Grammar","type":"multiple_choice_question","points":1,"text":"Which sentence uses capital letters correctly?",
   "options":["King henry lived in london during the middle ages.","King Henry lived in London during the Middle Ages.","king Henry lived in London during the middle ages."],"answer":1,"from":"23.1 DOL model and sort; 23.2 tap the capitals","status":"kept"},
  {"n":2,"section":"Grammar","type":"essay_question","points":1,"text":"Fix the capital letters and write the sentence the right way: “the lord of the castle lived in the tower of london in england.”",
   "from":"23.2 tap the capitals, 23.4 find the mistake","status":"kept"},
  {"n":3,"section":"Grammar","type":"essay_question","points":1,"text":"Write a sentence about a real or make-believe place. Use capital letters for every name, title and place.",
   "from":"23.1–23.4 Grammar","status":"kept (wording made plain)"},
  {"n":4,"section":"Morphology","type":"essay_question","points":1,"text":"The word part trans means across. Break apart the word transport. What does it mean?",
   "from":"23.1 crack the word, 23.2 match","status":"new (old Q4 tested struct from week 22)"},
  {"n":5,"section":"Morphology","type":"multiple_choice_question","points":1,"text":"Which word means “to change into a new shape”?",
   "options":["transform","transport","translate"],"answer":0,"from":"23.2 match, 23.3 build the word","status":"new (old Q5 tested struct)"},
  {"n":6,"section":"Morphology","type":"essay_question","points":1,"text":"Choose one: translate, transfer, or transplant. Write a sentence that shows what the word means.",
   "from":"23.2 match, 23.3 build, 23.4 dice","status":"new (old Q6 tested struct)"},
  {"n":7,"section":"Spelling","type":"multiple_choice_question","points":1,"text":"Which word has two consonants between its vowels, so it splits between them?",
   "options":["tiger","basket","music"],"answer":1,"from":"23.1 sort, 23.2 Sound Detective","status":"new (old Q7 tested consonant-le, week 21)"},
  {"n":8,"section":"Spelling","type":"essay_question","points":1,"text":"Split each word into syllables between its two middle consonants: rabbit, contest, helmet.",
   "from":"23.1 sort, 23.3 splitter, 23.4 dice","status":"new (old Q8 tested consonant-le)"},
  {"n":9,"section":"Spelling","type":"multiple_choice_question","points":1,"text":"Where does the word tunnel split?",
   "options":["tu · nnel","tun · nel","tunn · el"],"answer":1,"from":"23.1 Group B, 23.1 sort","status":"new (old Q9 tested a consonant-le spelling)"},
  {"n":10,"section":"Reading","type":"essay_question","points":1,"text":"What is the central idea of this article? Use one detail from the article to support your answer.",
   "from":"23.1 What Good Readers Do + Article Thinking Q1–Q2","status":"fixed (passage is now the 23.1 article’s own words)"},
  {"n":11,"section":"Reading","type":"essay_question","points":1,"text":"Name two kinds of work people did in the castle, according to the article.",
   "from":"23.1 Article Thinking Q2","status":"fixed (old wording named jobs the passage invented: steward, guards)"},
  {"n":12,"section":"Reading","type":"essay_question","points":1,"text":"Which castle job do you think was the hardest? Explain using details from the article.",
   "from":"23.1 article + Diligence Watch","status":"kept (wording made plain)"},
  {"n":13,"section":"Writing","type":"essay_question","points":1,"text":"Model topic sentence: “Food in the Middle Ages depended almost entirely on who you were.” It makes one careful claim. Write your own topic sentence about a medieval topic.",
   "from":"23.4 Read Like a Writer; 23.3–23.4 Writer’s Workshop (topic sentence)","status":"fixed (old model sentence misquoted the article and asked for a dash, which was not taught)"},
  {"n":14,"section":"Writing","type":"essay_question","points":1,"text":"Write 1–2 sentences about one fact from this week’s articles that surprised you. Say which article it came from.",
   "from":"23.2 Writer’s Workshop (notes from two sources)","status":"kept (now names the source)"}
 ],
 "passage": {"before": 10, "title": "Reading passage (the 23.1 article, “Life in a Medieval Castle”)",
   "text": "A medieval castle was not just a home — it was a fortress, a workplace, and a whole community. The king or lord often lived in the strongest part of the castle, called the keep. Surrounding the keep were great halls, kitchens, stables, and chapels. Many people worked inside the castle walls every day.\nMost castle workers were servants. Some cooked food, others cleaned, and some cared for the horses. Young boys from noble families could become pages, training to be knights one day. The castle was always busy — and always protected."}
}
io.open('assessments/g3-ela-wk23-checkin.json', 'w', encoding='utf-8').write(json.dumps(Q, ensure_ascii=False, indent=1))
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
page = '''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Week 23 Check-In Key</title>
<style>body{font:16px/1.5 system-ui,sans-serif;max-width:820px;margin:0 auto;padding:16px;background:#F0F2F8;color:#24324F}
h1{font-size:22px;color:#0E1C42}.q,.psg{background:#fff;border:1px solid #D9E0F0;border-radius:10px;padding:12px 16px;margin:12px 0}
.q.new{border-left:5px solid #2B5BA8}.psg{background:#FFF8E6}.h{font-weight:700;color:#0E1C42}.n{display:inline-block;background:#0E1C42;color:#fff;border-radius:50%%;width:26px;height:26px;text-align:center;line-height:26px;margin-right:6px}
.ok{color:#24502A;font-weight:700}.m{font-size:13px;color:#6B7690;margin-top:6px}</style></head><body>
<h1>%s</h1><p>%s</p><p><b>Quarter 3 · %s · %d questions · %d points.</b> Blue edge = new question (the old one tested something week 23 doesn’t teach).</p>%s</body></html>''' % (
    e(Q['title']), e(Q['description']), e(Q['chapters']), len(Q['questions']), sum(q['points'] for q in Q['questions']), rows)
io.open('assessments/g3-ela-wk23-checkin-key.html', 'w', encoding='utf-8').write(page)
print('ok')
