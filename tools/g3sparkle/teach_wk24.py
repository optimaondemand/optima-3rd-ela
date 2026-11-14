#!/usr/bin/env python3
"""Week 24 (Medieval Nonfiction, part 2: four articles): the Nov 10 2026 pilot fixes, as on weeks 18-21.
Writes DATA.teach, plate.lookBtn and DATA.virtue (Diligence Watch, 3 facts a day from that day's article) into data/lesson-24-N.json AND the page's oao-data block.
Word Study scripts are written for the Opti films from the start: Day 1 teaches each idea; Days 2-4
show that day's activity with an example that is not an answer anywhere in the week, and no two
films open the same way. Article quotes are the articles' own words after acc_wk24.py.

    python tools/g3sparkle/teach_wk24.py
"""
import io, json, re

GRAM_FOLD = [":scope > .callout:not(:has(+ .spotter-game)):not(:has(+ .fillin-game)):not(:has(+ .sort-game)):not(:has(+ .dol-check-btn))"]
WGRD = {"id": "wgrd", "find": "What Good Readers", "fold": [":scope > p:not(.g3-do)", ":scope > .key-concept", ":scope > .socratic-box"],
        "todo": "Listen to Opti. Then tap the lens you will use today."}
VOCAB_FOLD = [":scope > .g3-model-h", ":scope > .decode-steps"]
SPELL_FOLDTEXT = ["^\\s*👂", "^\\s*This week:", "The Rule:", "^\\s*Sort and explain"]
WRITE = {"id": "write", "find": "Writer.s Workshop", "fold": [":scope > .callout"], "foldText": ["watch how", "today.s tool"]}
DOL_TODO = "Tap the yellow parts. Then pick Sentence A or B and type it the right way."
CHQ_TODO = "Pick Explorer or Scholar. Answer the three questions in full sentences."
VTITLE = "Diligence Watch: Is someone working hard?"
LENS_END = "Then tap one of the two lenses below to use while you read. You don't need to write anything."
VOCAB_FLIP_TODO = "Listen to each card. Guess the meaning, then flip the card. Then play the matching game."
VOCAB_CLOZE_TODO = "Fill in each sentence with a word from the word bank. Tap Check My Work. Then play the matching game."

READ_TODO = "Read the two questions. Then read the article below."
ART_TODO = "Answer each question in full sentences. Use details from the article."
L = {
1: {"lookBtn": "Tap to learn about this painting of builders at work", "mods": [
 dict(WGRD, script="[warmly] Here's today's reading tip. A cause is why something happens. The effect is what happens. Castle builders did everything for a reason, and the article tells you why. " + LENS_END),
 {"id": "dol", "find": "Daily Oral", "fold": [], "todo": DOL_TODO,
  "script": "Let's fix a sentence. Look at the correct one first. The workers at Dover Castle built a great tower for King Henry the Second. Dover Castle is the name of one castle, so both words get capitals. King is a title right before a name. Tap the yellow parts. Then pick Sentence A or Sentence B, and type it the right way."},
 {"id": "morph", "find": "Morphology", "fold": [":scope > .callout:not(:has(+ .fillin-game)):not(:has(+ .dol-check-btn))"],
  "todo": "Think about the questions. Tap See if you cracked it. Type the missing part of each word.",
  "script": "[curious] What do a letter, a story, and a grocery list have in common? Somebody wrote them! There's a root that means write, and it has two spellings. Script. And scribe. Here's a word that's not on your list. Postscript. Post means after. So a postscript is writing you add after a letter: P.S.! Read the four words and think about the questions. Then tap See if you cracked it, and type the missing parts."},
 {"id": "vocab", "find": "Vocabulary", "fold": VOCAB_FOLD, "todo": VOCAB_CLOZE_TODO,
  "script": "Be a word detective with me. Battlements. Here's a sentence. The archers hid behind the battlements at the top of the wall. They hid behind them, up on top of the wall. So battlements must be the bumpy stone edge on top of a castle wall. One, read the sentence. Two, look for word parts. Three, check that the meaning fits. Now fill in each sentence from the word bank, and tap Check My Work. Then play the matching game."},
 {"id": "gram", "find": "Grammar", "fold": GRAM_FOLD, "todo": "Tap Now check your thinking. Then sort each sentence: main idea, detail, or off the topic.",
  "script": "[warmly] Think of a paragraph like a table. The main idea is the tabletop. The details are the legs that hold it up. Listen. Knights trained hard. They practiced with swords. They rode horses every day. Knights trained hard is the main idea. The other two hold it up. And I like pizza? That's off the topic. Read the paragraph, and tap Now check your thinking. Then sort each sentence: main idea, detail, or off the topic."},
 {"id": "spell", "find": "Spelling", "fold": [], "todo": "Say the words. Tap See the Rule. Then sort all eight words.",
  "script": "Say these with me. Painful. Painless. Same base word: pain. Ful means full of, so painful is full of pain. Less means without. Now two more jobs. Calm, calmness. Ness turns a describing word into a thing. Calm, calmly. Ly tells how something was done. Say the words in Group A and Group B, and tap See the Rule. Then sort all eight words."},
 {"id": "copia", "sel": ".spk-copia-card", "label": "Opti shows you how", "fold": [], "todo": "Write the sentence three new ways, one box at a time.",
  "script": "[warmly] Here's copia: one idea, said many ways. Let me try a different sentence first. The mason cut the stone. Box one, change the opener: In the cold morning, the mason cut the stone. Box two, a stronger verb: The mason chipped the stone. Box three, add a detail: The busy mason cut the heavy gray stone. Now it's your turn, one box at a time. If you get stuck, tap Show one way."},
 {"id": "read", "find": "Pause", "fold": [], "todo": READ_TODO,
  "script": "Read the two Pause and Think questions first. Then read how castles were built, with your lens in mind. When you finish, try the Diligence Watch right after the article. You don't write your Pause and Think answers."},
 {"id": "chq", "find": "Article Thinking", "fold": [], "todo": ART_TODO,
  "script": "Now answer in full sentences, with details from the article. One, what is the central idea? Say it in one sentence. Two, explain one cause and effect. Use because or so that. Three, in The Whipping Boy, the boys run away from a castle. How would its walls and gates make that easy, and hard?"},
 dict(WRITE, todo="Write your whole paragraph: a topic sentence, two details, and a closing sentence.",
  script="Today you write the whole thing! Clara's first draft had only two short sentences. Her new one has a topic sentence, two details with facts, and a closing sentence. Write your whole paragraph in the box. Borrow a sentence frame if you get stuck."),
], "cards": {},
 "virtue": [
  {"t": "Hundreds of workers worked on the castle site every day.", "ok": True, "why": "They kept working, day after day, on one huge job."},
  {"t": "A drawbridge could be raised to block the entrance.", "ok": False, "why": "That is a fact about the castle, not about someone working."},
  {"t": "Workers kept building one big castle for many years, and some took more than thirty.", "ok": True, "why": "Sticking with one job for years is diligence."}]},
2: {"lookBtn": "Tap to learn about this painting of two knights", "mods": [
 dict(WGRD, script="[warmly] Here's today's reading tip. Becoming a knight happened in steps. Each step had a reason: it got a boy ready for the next one. Ask why each step came first. " + LENS_END),
 {"id": "dol", "find": "Daily Oral", "fold": [], "todo": DOL_TODO,
  "script": "Let's fix a sentence. Look at the correct one first. Sir William of Bath was dubbed a knight by King Edward at Windsor Castle. Sir and King are titles right before names. But knight stays small. It isn't a name. Tap the yellow parts. Then pick Sentence A or Sentence B, and type it the right way."},
 {"id": "poem", "find": "Poetry", "fold": [":scope > .callout", ":scope > .socratic-box"], "todo": "Read the poem out loud. Then find the real words and the made-up ones.",
  "script": "Here's a very silly poem by Lewis Carroll. Read it out loud. Brillig? Slithy toves? Those aren't real words! But you can still tell the toves are some kind of creature, because they do things. Find the real words and the made-up ones. Then say how you can tell what a made-up word is doing."},
 {"id": "morph", "find": "Morphology", "fold": [":scope > .callout:not(:has(+ .match-game))", ":scope > .key-concept"], "todo": "Tap a word, then tap what it means. Match all four words.",
  "script": "Watch one match first. Script and scribe mean write, so look for them. Scriptwriter. A scriptwriter writes the words actors say in a movie. Script, writing. That's my match! +how:morph2"},
 {"id": "vocab", "find": "Vocabulary", "fold": VOCAB_FOLD, "todo": VOCAB_CLOZE_TODO,
  "script": "Ever seen a joust? Two knights charge at each other on horseback, each holding a long wooden lance. Lance. They charge holding it, so a lance must be a long pole for fighting on a horse. +how:vocabcloze"},
 {"id": "gram", "find": "Grammar", "fold": GRAM_FOLD, "todo": "Read the Remember box. Then tap the main idea in each paragraph.",
  "script": "Which one holds up the others? Bakers made bread. The castle kitchen was busy. Cooks roasted meat. It's the middle one! The kitchen was busy, and the other two show how. Read the Remember box. Then in each mixed-up paragraph, tap the main idea."},
 {"id": "spell", "find": "Spelling", "fold": [], "foldText": ["The Rule:"], "todo": "Read the rule. In each row, tap the word with the named ending.",
  "script": "Be a suffix detective. Which word means without? Mindful. Breathless. Fondness. Softly. Breathless! Breath, plus less: without breath. Read the rule. Then in each row, tap the one word with the ending named above it."},
 {"id": "read", "find": "Pause", "fold": [], "todo": READ_TODO,
  "script": "Read the two Pause and Think questions first. Then read about knights. After that, try the Diligence Watch, and watch my video in the Read Like a Writer box before you write."},
 {"id": "rwm", "sel": ".rwm-box", "after": ":scope > .rwm-header", "label": "Opti shows you how", "fold": [],
  "script": "[warmly] Let's try all three parts with a different sentence from today's article. In reality, not every knight followed the code. Part one, read like a reader. Some knights broke the rules of chivalry. Part two, read like a writer. It's short, and In reality warns you a surprise is coming: the truth, not the story. Part three, mimic. Here's mine: In reality, not every owl stays up all night. Now it's your turn with the sentence about years of training. Write one sentence in each box."},
 {"id": "chq", "find": "Article Thinking", "fold": [], "todo": ART_TODO,
  "script": "Now answer in full sentences. One, what is the central idea? Two, tell the steps to becoming a knight, with first, then and finally. Three, in The Whipping Boy, who comes closest to acting with chivalry by the end? Give one example."},
 dict(WRITE, todo="Read your paragraph out loud. Write the sentence you cut or fixed, and how you changed it.",
  script="Clara read her paragraph out loud and found a problem. Her paragraph was about servants, but one sentence was about knights. So she cut it. Read your paragraph out loud. Find a sentence that doesn't fit your topic, and fix it or cut it."),
], "cards": {},
 "virtue": [
  {"t": "A squire cared for a knight's armor and horse, and trained with sword and horse.", "ok": True, "why": "Caring for armor and training every day is hard, steady work."},
  {"t": "Becoming a knight took years of training.", "ok": True, "why": "Years of training take diligence."},
  {"t": "In reality, not every knight followed the code.", "ok": False, "why": "That is about knights breaking rules, not about someone working hard."}]},
3: {"lookBtn": "Tap to learn about this painting of a busy town", "mods": [
 dict(WGRD, script="[warmly] Here's today's reading tip. Today's article helps you see, hear and smell a medieval town. Every busy sound and bad smell had a cause. Ask what caused it. " + LENS_END),
 {"id": "dol", "find": "Daily Oral", "fold": [], "todo": DOL_TODO,
  "script": "Let's fix a sentence. Look at the correct one first. In the market town of Shrewsbury, merchants from France sold silk and spices every Thursday. See the comma after Shrewsbury? It ends the opening part. And Thursday gets a capital, because the days of the week are names. Tap the yellow parts. Then pick Sentence A or Sentence B, and type it the right way."},
 {"id": "morph", "find": "Morphology", "fold": [":scope > .callout:not(:has(+ .fillin-game))", ":scope > .key-concept"], "todo": "Say the parts out loud. Type the whole word in each box. Tap Check My Answers.",
  "script": "Let's snap three parts together, like blocks. De. Script. Ion. Description! A description writes down what something is like. Say the parts out loud, then say them fast as one word. Type the whole word in each box, and tap Check My Answers."},
 {"id": "vocab", "find": "Vocabulary", "fold": VOCAB_FOLD, "todo": VOCAB_CLOZE_TODO,
  "script": "Listen for this word in a busy town. Stall. A merchant sold apples from his stall in the market square. He sold things from it, outside, so a stall must be a little shop with a table. Put a bank word in each blank. If the sentence makes sense, keep it. Then try the matching game."},
 {"id": "gram", "find": "Grammar", "fold": GRAM_FOLD, "todo": "Read the Remember box. Type the one word each set of details is about.",
  "script": "Three details, one topic. Smiths made tools. Weavers made cloth. Potters made bowls. What one word are they all about? Workers! That one word is the topic. Read the Remember box. Then read each set of details, and type the one word they're about."},
 {"id": "spell", "find": "Spelling", "fold": [], "foldText": ["The Rule:"], "todo": "Read the rule. Tap each card to break the word apart.",
  "script": "Oops! I split gladness like this: gladn, ess. That's not right. The base word is glad. So it breaks into glad, and ness. Glad is a describing word, and ness turns it into a thing. Read the rule. Then tap each card to break the word apart."},
 {"id": "read", "find": "Pause", "fold": [], "todo": READ_TODO,
  "script": "Read the two Pause and Think questions first. Then read about medieval towns. Look for what you could see, hear and smell. Then try the Diligence Watch and the Read Like a Writer box."},
 {"id": "chq", "find": "Article Thinking", "fold": [], "todo": ART_TODO,
  "script": "Four questions today, in full sentences. One, the central idea. Two, why towns grew near cathedrals, rivers and trade routes. Three, which details from The Whipping Boy seem real? Four, find two details that prove a town was loud, busy and smelly."},
 dict(WRITE, todo="Check your paragraph with the checklist. Write one mistake you fixed.",
  script="Today you edit, like a careful scribe. Clara found two sentences with no capital at the start, and a number to write as a word. Check your paragraph with the checklist, one line at a time. Then write one mistake you fixed."),
], "cards": {},
 "virtue": [
  {"t": "Craftsmen hammered and shouted from their workshops.", "ok": True, "why": "They were busy at their work all day long."},
  {"t": "Animals wandered the streets.", "ok": False, "why": "That is about animals, not about someone working."},
  {"t": "Barbers pulled teeth and treated cuts.", "ok": True, "why": "Barbers did careful, hard jobs for the people in town."}]},
4: {"lookBtn": "Tap to learn about this painting of a knight", "mods": [
 dict(WGRD, script="[warmly] Here's today's reading tip. Think like a history detective. Stories change real life for a reason. When you find something a story changed, ask why the storyteller changed it. " + LENS_END),
 {"id": "dol", "find": "Daily Oral", "fold": [], "todo": DOL_TODO,
  "script": "Let's fix a sentence. Look at the correct one first. Historians debate whether whipping boys really existed in the courts of England and France. England and France are names of countries, so they get capitals. Historians gets one too, because it starts the sentence. Tap the yellow parts. Then pick Sentence A or Sentence B, and type it the right way."},
 {"id": "poem", "find": "Poetry", "fold": [":scope > .callout", ":scope > .socratic-box"], "todo": "Read the poem again. Then make up two words and use them in a sentence out loud.",
  "script": "Here's Carroll's silly poem again. This time, you're the word maker! Make up two words of your own. Then use them in one sentence, so a listener can tell what they mean. Say it out loud. You don't need to write it."},
 {"id": "morph", "find": "Morphology", "fold": [":scope > .key-concept"], "foldText": ["Before you roll"], "todo": "Tap Roll the Dice. Say what the word means. Tap Check My Thinking. Roll all six words.",
  "script": "Eyes closed for a second. What do script and scribe mean? Write! Keep that in your head. Here's a word that's not on the dice. Subscription. You write your name to sign up. Now tap Roll the Dice. Say what each word means, and tap Check My Thinking. Roll all six."},
 {"id": "vocab", "find": "Vocabulary", "fold": VOCAB_FOLD, "todo": VOCAB_CLOZE_TODO,
  "script": "Today's article talks about legends. A legend is an old story people told for years, like the stories of King Arthur. Did it really happen? Nobody knows for sure. Try each bank word in a blank, and keep the one that makes sense. Then finish with the matching game."},
 {"id": "gram", "find": "Grammar", "fold": GRAM_FOLD, "todo": "Tap the off-topic sentence, or tap No mistake. Then tap See the answers and answer the question in the box.",
  "script": "One of these wandered off. The market was busy. People bought fish. My cat is orange. Which one? My cat is orange! It isn't about the market. In each paragraph, tap the sentence that's off the topic. If every sentence fits, tap No mistake."},
 {"id": "spell", "find": "Spelling", "fold": [], "foldText": ["The Rule:"], "todo": "Tap Roll the dice. Pick an ending and say why. Tap Check my answer. Roll all six.",
  "script": "Here's my roll. Thought. Do I want full of thought? Then I pick ful: thoughtful. Without thought? Less: thoughtless. I choose the ending that does the job I need. Tap Roll the dice, pick an ending, and say why. Then tap Check my answer."},
 {"id": "read", "find": "Pause", "fold": [], "todo": READ_TODO,
  "script": "Read the two Pause and Think questions first. Then read the last article. Sort what is real from what stories made up. Then try the Diligence Watch and the Read Like a Writer box."},
 {"id": "chq", "find": "Article Thinking", "fold": [], "todo": ART_TODO,
  "script": "Three questions to finish the unit, in full sentences. One, the central idea. Two, name two real things stories like The Whipping Boy get right, and one thing that might be made up. Three, what is the most important thing you learned, and how does it change the way you think about The Whipping Boy?"},
 dict(WRITE, todo="Read your paragraph with the checklist. Then write what you are most proud of.",
  script="Publishing day! Clara read her paragraph one last time with the checklist. Then she thought about what she did well, and what she'd change next time. Do the same with yours. Then write what you're most proud of."),
], "cards": {},
 "virtue": [
  {"t": "Apprentices really did spend years learning a trade.", "ok": True, "why": "Learning a trade for years takes diligence."},
  {"t": "In real medieval life, most peasants never met a king.", "ok": False, "why": "That is about who met a king, not about someone working."},
  {"t": "Whipping boys may or may not have existed.", "ok": False, "why": "That is something historians argue about, not someone working hard."}]},
}

HOW = {'morph2': 'Read the Remember box. Then tap a word, and tap what it means. Match all four words.',
       'vocabcloze': 'Read how we figured out the first word. Then fill in each sentence with a word from the word bank, and tap Check My Work. Last, play the matching game.'}
SPLICE = {}
for d, cfg in L.items():
    for m in cfg['mods']:
        t = m.get('script', '')
        if '+how:' in t:
            new, slug = t.split(' +how:')
            SPLICE[(d, m['id'])] = 'g3ela-how-' + slug
            m['script'] = new + ' ' + HOW[slug]
VIDEO = {1: ['morph', 'vocab', 'gram', 'spell'], 2: ['morph', 'vocab', 'gram', 'spell', 'rwm'],
         3: ['morph', 'vocab', 'gram', 'spell'], 4: ['morph', 'vocab', 'gram', 'spell']}
for d, ids in VIDEO.items():
    for m in L[d]['mods']:
        if m['id'] in ids: m['video'] = 'g3ela-24-%d-teach-%s' % (d, m['id'])

def write_page(f, D):
    html = io.open(f, encoding='utf-8', newline='').read()
    m = re.search(r'(<script type="application/json" id="oao-data">)(.*?)(</script>)', html, re.S)
    old = m.group(2)
    if '\n' not in old.strip(): body = json.dumps(D, ensure_ascii=False, separators=(',', ':'))
    else: body = json.dumps(D, ensure_ascii=False, indent=1)
    body = body.replace('</script', '<\\/script')
    lead = old[:len(old) - len(old.lstrip())]; tail = old[len(old.rstrip()):]
    io.open(f, 'w', encoding='utf-8', newline='').write(html[:m.start(2)] + lead + body + tail + html[m.end(2):])

def recorded():
    """What gets voiced this week: the 17 film clips (minus any shared ending) + the vocab cards."""
    out = {}
    for d, cfg in L.items():
        for m in cfg['mods']:
            if 'video' in m:
                t = m['script']
                if (d, m['id']) in SPLICE: t = t[:len(t) - len(HOW[SPLICE[(d, m['id'])][len('g3ela-how-'):]])].rstrip()
                out['g3ela-24-%d-teach-%s' % (d, m['id'])] = t
        for w, t in cfg['cards'].items(): out['g3ela-24-%d-say-%s' % (d, w)] = t
    return out

if __name__ == '__main__':
    import sys
    for d, cfg in L.items():
        p = 'data/lesson-24-%d.json' % d
        j = json.load(io.open(p, encoding='utf-8'))
        if 'plate' in j: j['plate']['lookBtn'] = cfg['lookBtn']
        j['teach'] = {"dropTurnNotes": True, "mods": cfg['mods'], "cards": cfg['cards']}
        j['virtue'] = {"name": "diligence", "title": VTITLE, "items": cfg['virtue']}
        io.open(p, 'w', encoding='utf-8').write(json.dumps(j, ensure_ascii=False, indent=1))
        write_page('lesson-24-%d-med.html' % d, j)
    rec = recorded(); tot = 0
    for k, t in rec.items():
        n = len(t); tot += n; print('%-32s %4d' % (k, n))
    print('recorded this week: %d / 6260 credits (%.0f%%)' % (tot, 100.0 * tot / 6260))
    io.open('/tmp/wk24_rec.json', 'w', encoding='utf-8').write(json.dumps(rec, ensure_ascii=False, indent=1))
