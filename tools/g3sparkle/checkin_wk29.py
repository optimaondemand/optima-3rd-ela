#!/usr/bin/env python3
"""Week 29 check-in as a Canvas quiz: JSON source of truth + readable key. Audit: claude/g3-ela-wk29-audit.md findings 23-29.
Passage = The Lion, the Witch and the Wardrobe, Ch. 15 (Aslan explains the Deeper Magic), checked against Planning docs/lww_text.txt.
DRAFT until Bethany approves; .zip only after that."""
import json, io, html
Q = {
 "id": "g3-ela-wk29-checkin",
 "title": "Week 29 Check-In · The Lion, the Witch and the Wardrobe",
 "description": "This week you read Chapters 13 to 15: Edmund is rescued and forgiven, Aslan gives his life at the Stone Table, and at sunrise the Deeper Magic changes everything. You practiced punctuating dialogue, the root ject (it means throw), and long words built from a root with parts added. Show what you know!",
 "quarter": 4, "chapters": "Ch. 13–15",
 "questions": [
  {"n":1,"section":"Grammar","type":"multiple_choice_question","points":1,"text":"Which sentence uses dialogue punctuation the right way?",
   "options":["“We couldn’t sleep,” said Lucy.","“We couldn’t sleep, said Lucy.”","We couldn’t sleep, “said Lucy.”"],"answer":0,
   "from":"29.1 The Rule + DOL, 29.2 DOL (“We couldn’t sleep,” said Lucy.)","status":"fixed (old right answer was a run-on and not a book line)"},
  {"n":2,"section":"Grammar","type":"essay_question","points":1,"text":"Fix this sentence. Add the quotation marks, capital letters and the comma: i feel afraid to turn round said susan",
   "from":"29.1 Rule, 29.3 Now you (fix a line of dialogue)","status":"fixed (old sentence was invented; this is Susan in Ch. 15)"},
  {"n":3,"section":"Grammar","type":"essay_question","points":1,"text":"Write a line of dialogue that Lucy or Susan might say on the walk with Aslan in Chapter 14. Use quotation marks, a capital letter, and a comma or question mark inside the quotation mark.",
   "from":"29.1–29.4 Grammar","status":"fixed (was “at the Stone Table”; the walk is gentler and also in Ch. 14)"},
  {"n":4,"section":"Word Parts","type":"essay_question","points":1,"text":"The root ject means throw. Break apart the word reject. What does it mean?",
   "from":"29.1 See if you were right, 29.2 match, 29.3 build","status":"kept"},
  {"n":5,"section":"Word Parts","type":"multiple_choice_question","points":1,"text":"What does the word project most likely mean?",
   "options":["It means to throw something forward.","It means to throw something away.","It means to throw something backward."],"answer":0,
   "from":"29.1–29.4 Morphology (pro- = forward)","status":"kept (options now whole sentences)"},
  {"n":6,"section":"Word Parts","type":"essay_question","points":1,"text":"Choose one: eject, inject or project. Write a sentence that shows what the word means.",
   "from":"29.1–29.4 Morphology","status":"kept"},
  {"n":7,"section":"Spelling","type":"essay_question","points":1,"text":"Write each word: injected, ejected, rejected. Then write what each one means, using what you know about ject and the part in front of it.",
   "from":"29.1–29.4 Morphology, 29.2 Spelling (find the root)","status":"fixed (projection was never taught; now ejected)"},
  {"n":8,"section":"Spelling","type":"essay_question","points":1,"text":"Explain how knowing the root ject helps you understand a word you haven’t seen before. Give an example.",
   "from":"29.1 Now name the pattern, 29.4 Root and Affix Dice","status":"kept"},
  {"n":9,"section":"Spelling","type":"multiple_choice_question","points":1,"text":"One word is spelled wrong. Which one?",
   "options":["inject","project","ejeckt"],"answer":2,"from":"29.1 sort, 29.3 build (eject)","status":"kept"},
  {"n":10,"section":"Reading","type":"essay_question","points":1,"text":"What does Aslan explain to Susan in this passage? Use two details from the passage.",
   "from":"29.3 Q1 (the Deeper Magic)","status":"fixed (passage is now the book’s own words)"},
  {"n":11,"section":"Reading","type":"essay_question","points":1,"text":"The Witch knew the Deep Magic, but not the magic deeper still. Why does that matter in the story?",
   "from":"29.3 Q1 and Q3","status":"fixed (old question quoted the invented passage)"},
  {"n":12,"section":"Reading","type":"essay_question","points":1,"text":"Why do you think Aslan gave up his life for Edmund? What does his choice tell us about what the story values most?",
   "from":"29.2 Q1–Q3, 29.4 Q1","status":"kept (gentler wording)"},
  {"n":13,"section":"Writing","type":"essay_question","points":1,"text":"Model sentences from the book: “In the wood behind them a bird gave a chuckling sound. It had been so still for hours and hours that it startled them.” A small, quiet sound after a long silence shows that something is about to change. Write your own short, quiet sentence about a serious moment. Show what happened without saying how to feel.",
   "from":"29.3 Read Like a Writer, 29.4 Read Like a Writer (a plain detail does the work)","status":"fixed (old model sentence was invented)"},
  {"n":14,"section":"Writing","type":"essay_question","points":1,"text":"Write your theme for The Lion, the Witch and the Wardrobe as a full sentence that starts “The story shows that.” Then give one detail from the book that proves it, with its chapter number.",
   "from":"29.1–29.4 Writer’s Workshop (theme response)","status":"fixed (old Q14 repeated Q12; now the week’s writing)"}
 ],
 "passage": {"before": 10, "title": "Reading passage (The Lion, the Witch and the Wardrobe, Chapter 15)",
   "text": "“But what does it all mean?” asked Susan when they were somewhat calmer.\n“It means,” said Aslan, “that though the Witch knew the Deep Magic, there is a magic deeper still which she did not know. Her knowledge goes back only to the dawn of time. But if she could have looked a little further back, into the stillness and the darkness before Time dawned, she would have read there a different incantation. She would have known that when a willing victim who had committed no treachery was killed in a traitor’s stead, the Table would crack and Death itself would start working backwards.”\n— C.S. Lewis, The Lion, the Witch and the Wardrobe, Chapter 15"}
}
io.open('assessments/g3-ela-wk29-checkin.json', 'w', encoding='utf-8').write(json.dumps(Q, ensure_ascii=False, indent=1))
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
page = '''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Week 29 Check-In Key</title>
<style>body{font:16px/1.5 system-ui,sans-serif;max-width:820px;margin:0 auto;padding:16px;background:#F0F2F8;color:#24324F}
h1{font-size:22px;color:#0E1C42}.q,.psg{background:#fff;border:1px solid #D9E0F0;border-radius:10px;padding:12px 16px;margin:12px 0}
.q.new{border-left:5px solid #2B5BA8}.psg{background:#FFF8E6}.h{font-weight:700;color:#0E1C42}.n{display:inline-block;background:#0E1C42;color:#fff;border-radius:50%%;width:26px;height:26px;text-align:center;line-height:26px;margin-right:6px}
.ok{color:#24502A;font-weight:700}.m{font-size:13px;color:#6B7690;margin-top:6px}</style></head><body>
<h1>%s</h1><p>%s</p><p><b>Quarter 4 · %s · %d questions · %d points.</b> Blue edge = fixed or new question.</p>%s</body></html>''' % (
    e(Q['title']), e(Q['description']), e(Q['chapters']), len(Q['questions']), sum(q['points'] for q in Q['questions']), rows)
io.open('assessments/g3-ela-wk29-checkin-key.html', 'w', encoding='utf-8').write(page)
print('ok')
