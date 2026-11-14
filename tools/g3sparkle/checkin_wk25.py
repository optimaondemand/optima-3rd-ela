#!/usr/bin/env python3
"""Week 25 check-in as a Canvas quiz: JSON source of truth + readable key. Audit: claude/g3-ela-wk25-audit.md findings 17-20.
Passage = The Lion, the Witch and the Wardrobe, Ch. 1, checked against Planning docs/lww_text.txt (OCR semicolon after
"trunks" printed as the book's comma)."""
import json, io, html
Q = {
 "id": "g3-ela-wk25-checkin",
 "title": "Week 25 Check-In · The Lion, the Witch and the Wardrobe",
 "description": "This week you started The Lion, the Witch and the Wardrobe (Ch. 1–3) and followed Lucy through the wardrobe into a snowy wood. You practiced complex sentences, the word part tele (far), and the lazy schwa sound. Show what you know!",
 "quarter": 4, "chapters": "Ch. 1–3",
 "questions": [
  {"n":1,"section":"Grammar","type":"multiple_choice_question","points":1,"text":"Which is a complex sentence?",
   "options":["Lucy opened the wardrobe and found coats.","Lucy opened the wardrobe, but it was dark inside.","Although the others did not believe her, Lucy knew what she had seen."],"answer":2,"from":"25.1 The Rule, 25.2 find the connecting word","status":"kept"},
  {"n":2,"section":"Grammar","type":"essay_question","points":1,"text":"Join these two sentences into one complex sentence. Use when, because or although, and remember the comma: “Lucy stepped through the wardrobe. She felt cold snow under her feet.”",
   "from":"25.3 join two sentences","status":"kept (wording made plain; joining words match the week)"},
  {"n":3,"section":"Grammar","type":"essay_question","points":1,"text":"Write your own complex sentence about a character in Chapters 1 to 3. Start it with when, because, although or if, and put the comma in the right place.",
   "from":"25.1–25.4 Grammar","status":"kept (old list had after, which the week doesn’t teach)"},
  {"n":4,"section":"Morphology","type":"essay_question","points":1,"text":"The word part tele means far. Break apart the word television. What does it mean?",
   "from":"25.1 build the word, 25.2 match","status":"new (old Q4 tested the prefix inter-, never taught)"},
  {"n":5,"section":"Morphology","type":"multiple_choice_question","points":1,"text":"A telescope is a tool for —",
   "options":["looking at things far away","hearing sounds close by","writing a message by hand"],"answer":0,"from":"25.1 See what was hiding, 25.3 build, 25.4 dice","status":"new (old Q5 tested inter-)"},
  {"n":6,"section":"Morphology","type":"essay_question","points":1,"text":"Choose one: telephone, telegram or telescope. Write a sentence that shows what the word means.",
   "from":"25.1–25.4 Morphology","status":"new (old Q6 tested inter-)"},
  {"n":7,"section":"Spelling","type":"multiple_choice_question","points":1,"text":"Say the word lemon. Which letter makes the lazy uh sound, the schwa?",
   "options":["e","o","m"],"answer":1,"from":"25.1 sort, 25.3 Find the Schwa","status":"new (old Q7 tested drop-the-e, not this week)"},
  {"n":8,"section":"Spelling","type":"essay_question","points":1,"text":"What is a schwa? Explain in your own words why it makes long words tricky to spell.",
   "from":"25.1 Now name the pattern, 25.4 objective","status":"new (old Q8 tested drop-the-e)"},
  {"n":9,"section":"Spelling","type":"multiple_choice_question","points":1,"text":"One word is spelled wrong. Which one?",
   "options":["about","problum","moment"],"answer":1,"from":"25.1 sort, 25.2 tap the schwa","status":"new (old Q9 tested drop-the-e)"},
  {"n":10,"section":"Reading","type":"essay_question","points":1,"text":"Lucy is in a brand-new place. Name two details from the passage that tell you what this place is like.",
   "from":"25.1 Q1 setting details, 25.3 Q1 touch and sound","status":"fixed (passage is now the book’s own words)"},
  {"n":11,"section":"Reading","type":"essay_question","points":1,"text":"The passage says Lucy has two feelings at the same time. Name both feelings, and tell why she might feel each one.",
   "from":"25.1 Q2 Lucy’s feelings","status":"replaced (old Q11 quoted a line the passage invented)"},
  {"n":12,"section":"Reading","type":"essay_question","points":1,"text":"Why don’t Peter, Susan and Edmund believe Lucy’s story when she first comes back? Use details from Chapter 3.",
   "from":"25.2 Q2 Lucy’s story; Truth Watch","status":"kept (wording made plain)"},
  {"n":13,"section":"Writing","type":"essay_question","points":1,"text":"Model sentence: “A moment later she found that she was standing in the middle of a wood at night-time with snow under her feet and snowflakes falling through the air.” Lewis tells what Lucy feels under her feet and what falls through the air. Write your own setting sentence with at least two details you could feel, see or hear.",
   "from":"25.3 Writer’s Workshop evidence; 25.1 banner","status":"fixed (old model sentence misquoted the book)"},
  {"n":14,"section":"Writing","type":"essay_question","points":1,"text":"Lucy discovers something wonderful, but no one believes her. Write 1–2 sentences about how that might feel.",
   "from":"25.2 Q2; Truth Watch","status":"kept"}
 ],
 "passage": {"before": 10, "title": "Reading passage (The Lion, the Witch and the Wardrobe, Chapter 1)",
   "text": "Lucy felt a little frightened, but she felt very inquisitive and excited as well. She looked back over her shoulder and there, between the dark tree trunks, she could still see the open doorway of the wardrobe and even catch a glimpse of the empty room from which she had set out. (She had, of course, left the door open, for she knew that it is a very silly thing to shut oneself into a wardrobe.) It seemed to be still daylight there. “I can always get back if anything goes wrong,” thought Lucy. She began to walk forward, crunch-crunch over the snow and through the wood towards the other light. In about ten minutes she reached it and found it was a lamp-post.\n— C.S. Lewis, The Lion, the Witch and the Wardrobe, Chapter 1"}
}
io.open('assessments/g3-ela-wk25-checkin.json', 'w', encoding='utf-8').write(json.dumps(Q, ensure_ascii=False, indent=1))
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
page = '''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Week 25 Check-In Key</title>
<style>body{font:16px/1.5 system-ui,sans-serif;max-width:820px;margin:0 auto;padding:16px;background:#F0F2F8;color:#24324F}
h1{font-size:22px;color:#0E1C42}.q,.psg{background:#fff;border:1px solid #D9E0F0;border-radius:10px;padding:12px 16px;margin:12px 0}
.q.new{border-left:5px solid #2B5BA8}.psg{background:#FFF8E6}.h{font-weight:700;color:#0E1C42}.n{display:inline-block;background:#0E1C42;color:#fff;border-radius:50%%;width:26px;height:26px;text-align:center;line-height:26px;margin-right:6px}
.ok{color:#24502A;font-weight:700}.m{font-size:13px;color:#6B7690;margin-top:6px}</style></head><body>
<h1>%s</h1><p>%s</p><p><b>Quarter 4 · %s · %d questions · %d points.</b> Blue edge = new question (the old one tested something week 25 doesn’t teach).</p>%s</body></html>''' % (
    e(Q['title']), e(Q['description']), e(Q['chapters']), len(Q['questions']), sum(q['points'] for q in Q['questions']), rows)
io.open('assessments/g3-ela-wk25-checkin-key.html', 'w', encoding='utf-8').write(page)
print('ok')
