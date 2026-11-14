#!/usr/bin/env python3
"""Week 24 check-in as a Canvas quiz: JSON source of truth + readable key."""
import json, io, html
Q = {
 "id": "g3-ela-wk24-checkin",
 "title": "Week 24 Check-In · Medieval Nonfiction",
 "description": "This week you read four true articles about the Middle Ages: how castles were built, knights, medieval towns, and what stories get right and wrong. You found main ideas and details, the root script/scribe (write), and the endings -ful, -less, -ness and -ly. Show what you know!",
 "quarter": 3, "chapters": "Articles 24.1–24.4",
 "questions": [
  {"n":1,"section":"Grammar","type":"multiple_choice_question","points":1,"text":"Read this: “Castle builders dug deep foundations. They used stone, not wood. Stone walls could last for hundreds of years.” What is the main idea?",
   "options":["Building with stone made castles strong and lasting.","Castles were built near rivers.","Workers dug deep holes first."],"answer":0,"from":"24.1 sort, 24.2 find the main idea","status":"kept"},
  {"n":2,"section":"Grammar","type":"essay_question","points":1,"text":"Read these details: “Workers carried stone in baskets. Teams of horses pulled heavy carts. Cranes made of wood lifted the largest blocks.” Write a main idea sentence for this paragraph.",
   "from":"24.3 name the topic, then write a main idea sentence","status":"kept"},
  {"n":3,"section":"Grammar","type":"essay_question","points":1,"text":"Write one main idea sentence and one detail sentence that supports it, about any topic you know well.",
   "from":"24.1–24.4 Grammar; Writer’s Workshop paragraph","status":"kept (wording made plain)"},
  {"n":4,"section":"Morphology","type":"essay_question","points":1,"text":"The root script or scribe means write. Break apart the word manuscript. What does it mean?",
   "from":"24.1 crack the word, 24.2 match","status":"new (old Q4 tested the prefix sub-, never taught)"},
  {"n":5,"section":"Morphology","type":"multiple_choice_question","points":1,"text":"Which word means “to write about something so others can see it”?",
   "options":["describe","manuscript","inscription"],"answer":0,"from":"24.2 match, 24.3 build the word","status":"new (old Q5 tested sub-)"},
  {"n":6,"section":"Morphology","type":"essay_question","points":1,"text":"Choose one: script, inscription, or prescription. Write a sentence that shows what the word means.",
   "from":"24.1 fill-in, 24.2 match, 24.4 dice","status":"new (old Q6 tested sub-)"},
  {"n":7,"section":"Spelling","type":"multiple_choice_question","points":1,"text":"Which word means “without fear”?",
   "options":["fearful","fearless","fear"],"answer":1,"from":"24.1 Group A and sort, 24.2 Suffix Detective","status":"new (old Q7 tested VCCV, week 23)"},
  {"n":8,"section":"Spelling","type":"essay_question","points":1,"text":"Add -ness or -ly so each word fits, and write the two sentences: “The knight was known for his kind___.” “The page walked quiet___ past the guards.”",
   "from":"24.1 Group B, 24.3 break it apart, 24.4 dice","status":"new (old Q8 tested VCCV)"},
  {"n":9,"section":"Spelling","type":"multiple_choice_question","points":1,"text":"Which ending turns a describing word into a thing you can talk about, like kindness?",
   "options":["-ful","-ness","-ly"],"answer":1,"from":"24.1 See the Rule, 24.2 Suffix Detective","status":"new (old Q9 tested a VCCV spelling)"},
  {"n":10,"section":"Reading","type":"essay_question","points":1,"text":"What is the central idea of this passage? Use one detail from the passage to support your answer.",
   "from":"24.1 Article Thinking Q1","status":"fixed (passage is now the 24.1 article’s own words)"},
  {"n":11,"section":"Reading","type":"essay_question","points":1,"text":"The passage says a large castle could take many years to finish. Why do you think it took so long? Use details from the passage.",
   "from":"24.1 Pause & Think 2, cause and effect","status":"fixed (old wording quoted words the passage invented)"},
  {"n":12,"section":"Reading","type":"essay_question","points":1,"text":"Name one part of a castle’s design and explain how it helped keep enemies out. Use the word because.",
   "from":"24.1 What Good Readers Do (cause and effect), Article Thinking Q2","status":"replaced (old Q12 asked about knights riding on top of the walls, which the article never says)"},
  {"n":13,"section":"Writing","type":"essay_question","points":1,"text":"Model topic sentence: “Becoming a knight took years of training.” Six words set up a whole paragraph. Write your own short topic sentence about something that takes a long time to learn.",
   "from":"24.2 Read Like a Writer; Writer’s Workshop topic sentence","status":"fixed (old model sentence was invented)"},
  {"n":14,"section":"Writing","type":"essay_question","points":1,"text":"Imagine you are a worker helping build a castle in the Middle Ages. Write 1–2 sentences about what your job might be and what it would feel like.",
   "from":"24.1 article + Job Spotlight: The Stonemason","status":"kept"}
 ],
 "passage": {"before": 10, "title": "Reading passage (the 24.1 article, “How Castles Were Built”)",
   "text": "Building a medieval castle was one of the biggest construction projects of its time. A large stone castle could take many years to finish, and some took more than thirty. Hundreds of workers — stonemasons, carpenters, blacksmiths, and laborers — worked on the site every day.\nCastles were built for defense. The walls were thick — often ten feet or more — to withstand attack. A deep ditch called a moat was often dug around the outside and filled with water. A drawbridge could be raised to block the entrance. Every part of the castle’s design was meant to make it as difficult as possible for an enemy to get inside."}
}
io.open('assessments/g3-ela-wk24-checkin.json', 'w', encoding='utf-8').write(json.dumps(Q, ensure_ascii=False, indent=1))
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
page = '''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Week 24 Check-In Key</title>
<style>body{font:16px/1.5 system-ui,sans-serif;max-width:820px;margin:0 auto;padding:16px;background:#F0F2F8;color:#24324F}
h1{font-size:22px;color:#0E1C42}.q,.psg{background:#fff;border:1px solid #D9E0F0;border-radius:10px;padding:12px 16px;margin:12px 0}
.q.new{border-left:5px solid #2B5BA8}.psg{background:#FFF8E6}.h{font-weight:700;color:#0E1C42}.n{display:inline-block;background:#0E1C42;color:#fff;border-radius:50%%;width:26px;height:26px;text-align:center;line-height:26px;margin-right:6px}
.ok{color:#24502A;font-weight:700}.m{font-size:13px;color:#6B7690;margin-top:6px}</style></head><body>
<h1>%s</h1><p>%s</p><p><b>Quarter 3 · %s · %d questions · %d points.</b> Blue edge = new question (the old one tested something week 24 doesn’t teach).</p>%s</body></html>''' % (
    e(Q['title']), e(Q['description']), e(Q['chapters']), len(Q['questions']), sum(q['points'] for q in Q['questions']), rows)
io.open('assessments/g3-ela-wk24-checkin-key.html', 'w', encoding='utf-8').write(page)
print('ok')
