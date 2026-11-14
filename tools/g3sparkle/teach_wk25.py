#!/usr/bin/env python3
"""Week 25 (LWW Ch. 1-3): the Nov 10 2026 pilot fixes, as on weeks 18-24, for the new Narnia page template.
Writes DATA.teach, plate.lookBtn and DATA.virtue (Truth Watch: honesty, the Narnia unit's trait; 3 moments a day from
Ch. 1-3, checked against Planning docs/lww_text.txt) into data/lesson-25-N.json AND the page's oao-data block.
Word Study scripts are written for the Opti films: Day 1 teaches each idea; Days 2-4 show that day's activity with an
example that is not an answer anywhere in the week (telegraph, telework, telephoto, teleconference; spiteful, glimpse;
Narnia, Edmund, Susan, apart, lion, Tumnus), and no two films open the same way. NO RECORDINGS (Bethany, Nov 14 2026):
films are built silent with captions; scripts stay written to the budget for later.

    python tools/g3sparkle/teach_wk25.py
"""
import io, json, re

GRAM_FOLD = [":scope > .callout:not(:has(+ .spotter-game)):not(:has(+ .fillin-game)):not(:has(+ .sort-game)):not(:has(+ .dol-check-btn))"]
WGRD = {"id": "wgrd", "find": "What Good Readers", "fold": [":scope > p:not(.g3-do)", ":scope > .key-concept", ":scope > .socratic-box"],
        "todo": "Listen to Opti. Then tap the lens you will use today."}
VOCAB_FOLD = [":scope > .g3-model-h", ":scope > .decode-steps", ":scope > .key-concept"]
WRITE = {"id": "write", "find": "Writer.s Workshop", "fold": [":scope > .callout"], "foldText": ["watch how", "today.s tool"]}
DOL_TODO = "Tap the yellow parts. Then pick Sentence A or B and type it the right way."
VTITLE = "Truth Watch: Is someone being honest?"
LENS_END = "Then tap one of the two lenses below to use while you read. You don't need to write anything."
Q_TODO = "Answer each question in full sentences. Use details from the book."
READ = {"id": "read", "find": "^\\W*(Read:|Look Back)", "fold": []}
CHQ = {"id": "chq", "find": "Q1 —", "fold": [], "todo": Q_TODO}
def dol(script): return {"id": "dol", "find": "Daily Oral", "fold": [], "todo": DOL_TODO, "script": "Let's fix a sentence. The correct one first. " + script + " Tap the yellow parts. Then pick Sentence A or Sentence B, and type it the right way."}
L = {
1: {"lookBtn": "Tap to learn about this painting of a snowy wood", "mods": [
 dict(WGRD, script="[warmly] Here's this week's reading tip. In a fantasy story, the author builds a whole new world out of words. So slow down. Notice the weather, the light, and anything that could never happen at home. " + LENS_END),
 dol("Lucy met the Faun by the lamp-post, and he invited her home for tea. Lucy is a name, so it gets a capital. See the comma before and? It joins two complete thoughts."),
 {"id": "morph", "find": "Morphology", "fold": [":scope > .socratic-box", ":scope > .key-concept:not(:has(+ .fillin-game))"],
  "todo": "Think about the question. Tap See what was hiding. Type each whole word.",
  "script": "[curious] In Chapter 1, Lucy sees a light ahead of her. Not close by. A long way off. Far! There's a word part that means far. Tele. Here's a word that's not on your list. Telegraph. Long ago, a telegraph sent messages far away, over wires. Tele, far. Graph, write. Writing sent far! Read the four words and their parts. Then tap See what was hiding, and type each word."},
 {"id": "vocab", "find": "Vocabulary", "fold": VOCAB_FOLD, "todo": "Fill in each sentence from the word bank. Tap Check My Work. Then play the matching game.",
  "script": "Be a word detective with me. Spiteful. Here's the sentence. Edmund could be spiteful, and on this occasion he was spiteful. He sneered and jeered at Lucy. One, read the sentence: he was mean to her on purpose. Two, look for word parts: spite, plus ful, full of. Three, check it. Spiteful means full of meanness. +how:vocabcloze"},
 {"id": "gram", "find": "Grammar", "fold": GRAM_FOLD, "todo": "Tap Now check your thinking. Then tap the word each missing comma goes after.",
  "script": "[warmly] Some sentences have two parts. One part can stand alone. The other part can't. Listen. When Lucy felt something crunching. When Lucy felt something crunching, what? It can't stand alone! Add the main idea: she stooped down to feel it. When the part that can't stand alone comes first, put a comma after it. Read The Rule box, and tap Now check your thinking. Then find where each comma goes."},
 {"id": "spell", "find": "Spelling", "fold": [], "todo": "Say the words. Tap Now name the pattern. Then sort all eight words.",
  "script": "Say this name with me. Narnia. Nar, nee, uh. Hear that last beat? It's quiet and lazy. It says uh. That lazy sound is called the schwa. Now try Edmund. Ed, mund. The u says uh! Any vowel can make the schwa. Say the eight words in the sort, and tap Now name the pattern. Then sort the words."},
 {"id": "copia", "sel": ".spk-copia-card", "label": "Opti shows you how", "fold": [], "todo": "Write the sentence three new ways, one box at a time.",
  "script": "[warmly] Here's copia: one idea, said many ways. Let me try a different sentence first. The Faun dropped his parcels. Box one, change the opener: In the snowy wood, the Faun dropped his parcels. Box two, a stronger verb: The Faun spilled his parcels. Box three, add a detail: The surprised Faun dropped all his brown-paper parcels. Now it's your turn, one box at a time. If you get stuck, tap Show one way."},
 dict(READ, todo="Read Chapter 1 in your book. Then try the Truth Watch below.",
  script="Read Chapter 1 in your book, with your lens in mind. Watch for the moment the wardrobe stops being a wardrobe. When you finish, try the Truth Watch right after this box. Then answer the three questions."),
 dict(CHQ, script="Three questions, in full sentences, with details from the book. One, two details about the snowy wood. Two, Lucy has two feelings at once. Name them both. Three, the most surprising detail in Chapter 1, and why it surprised you."),
 dict(WRITE, todo="Look back at Chapter 1. Write two or three details Lewis uses to describe Narnia.",
  script="Today you brainstorm. Clara's first try just said Narnia has snow and a lamp-post. Then she looked back at the book and found what the snow felt like and sounded like. Look back at Chapter 1. Write two or three details Lewis uses to describe Narnia."),
], "cards": {},
 "virtue": [
  {"t": "Mr. Tumnus tells Lucy that he was going to hand her over to the White Witch.", "ok": True, "why": "He told the hard truth, even though it made him look bad."},
  {"t": "Lucy tells Mr. Tumnus that what he did was pretty bad, but she says it gently.", "ok": True, "why": "Lucy wanted to be truthful and kind at the same time."},
  {"t": "Mr. Tumnus pretended to be Lucy’s friend and asked her to tea.", "ok": False, "why": "Pretending is not honest. That is why he felt so bad."}]},
2: {"lookBtn": "Tap to learn about this painting of hunters in the snow", "mods": [
 dict(WGRD, script="[warmly] Here's today's reading tip. A setting can change with the mood. A warm cave with a fire feels very different from a cold, quiet wood. Notice how each place makes you feel. " + LENS_END),
 dol("The Queen told the dwarf to stop, and Edmund stared at her golden crown. Queen gets a capital, because it's used as her name. And there's that comma before and again."),
 {"id": "poem", "find": "Poetry", "fold": [":scope > .callout"], "todo": "Read the poem out loud. Then answer the question.",
  "script": "[curious] Here's a poem by William Blake, written more than two hundred years ago. Read it out loud. Blake talks right to the tiger, as if it could listen and answer him. That's personification. Then answer the question: what is Blake asking the tiger?"},
 {"id": "morph", "find": "Morphology", "fold": [":scope > .callout:not(:has(+ .match-game))", ":scope > .key-concept"], "todo": "Tap a word, then tap what it means. Match all four words.",
  "script": "Watch one match first. Find tele, and remember: it means far. Telework. Tele, far. Work. Telework means working far from the office, like at home. That's my match! +how:morph2"},
 {"id": "vocab", "find": "Vocabulary", "fold": [], "todo": "Tap a word, then tap its meaning. Match all four words.",
  "script": "Here's another word from Chapter 1. Glimpse. Lucy could even catch a glimpse of the empty room. Just a quick look, through the trees. So a glimpse is a quick look. Now tap a word, then tap its meaning. Match all four."},
 {"id": "gram", "find": "Grammar", "fold": GRAM_FOLD, "todo": "Find the connecting words. Tap Now check your thinking. Then tap every word that is wrong.",
  "script": "Spot the connecting word. Because it was raining, the children explored the house. Because! It starts the part that can't stand alone. Find the connecting word in each sentence, and tap Now check your thinking. Then fix the paragraph. Read slowly: the mistakes aren't all the same kind."},
 {"id": "spell", "find": "Spelling", "fold": [], "foldText": ["The Rule:"], "todo": "Read the rule. Tap every word with a lazy schwa beat.",
  "script": "Lazy beat hunt! Susan pulled the coats apart. Susan. Soo, zun. A lazy beat, yes! Pulled? Just one beat, no. Apart. Uh, part. Yes! Read the rule. Then tap every word with a schwa in the two sentences."},
 dict(READ, todo="Read Chapters 2 and 3 in your book. Then try the Truth Watch below.",
  script="Read Chapters 2 and 3 in your book, with your lens in mind. Then try the Truth Watch, and watch my video in the Read Like a Writer box before you write."),
 {"id": "rwm", "sel": ".rwm-box", "after": ":scope > .rwm-header", "label": "Opti shows you how", "fold": [],
  "script": "[warmly] Let's try all three parts with a different sentence from Chapter 3. There was crisp, dry snow under his feet and more snow lying on the branches of the trees. Part one, read like a reader. Edmund is in Narnia now, and it's winter. Part two, read like a writer. Lewis starts at Edmund's feet, then looks up at the trees, so you look around with him. Part three, mimic. Here's mine: There was cold, wet sand under my feet and more sand stuck to my shoes. Now it's your turn with Lewis's sentence about the house. Write one sentence in each box."},
 dict(CHQ, script="Three questions, in full sentences. One, two details that make Mr. Tumnus's cave cozy. Two, why the others don't believe Lucy. Think about the time, and the back of the wardrobe. Three, how Narnia and the Professor's house feel different."),
 dict(WRITE, todo="Write your opening sentence: the book, the author, and what you will show.",
  script="Today you write one sentence: your opening. Clara's rough try didn't say much. Her new one names the book, the author, and what she will prove. Do the same for yours."),
], "cards": {},
 "virtue": [
  {"t": "Lucy tells the others she has been away for hours and hours.", "ok": True, "why": "She tells them what really happened to her."},
  {"t": "Edmund taps his head and calls Lucy batty.", "ok": False, "why": "Making fun of someone is not about telling the truth. It hurts Lucy."},
  {"t": "Lucy says, “It wasn’t a hoax at all. Honestly it was. I promise.”", "ok": True, "why": "She keeps telling the truth, even when no one believes her."}]},
3: {"lookBtn": "Tap to learn about this painting of a lamp-lit street", "mods": [
 dict(WGRD, script="[warmly] Here's today's reading tip. Detectives point to proof. When you say Narnia feels real, point to Lewis's exact words: what Lucy felt, and what she heard. " + LENS_END),
 dol("When Lucy stepped through the fur coats, she felt snow under her shoes. When starts the part that can't stand alone. The comma goes right where that part ends."),
 {"id": "morph", "find": "Morphology", "fold": [":scope > .callout:not(:has(+ .fillin-game))", ":scope > .key-concept"], "todo": "Say the parts out loud. Type the whole word in each box. Tap Check My Answers.",
  "script": "Snap the parts together, like blocks. Tele. Photo. Telephoto! A telephoto lens on a camera takes pictures of things far away. +how:morph3"},
 {"id": "vocab", "find": "Vocabulary", "fold": [], "todo": "Read each sentence. Pick the word that fits.",
  "script": "Try each word in the blank, and keep the one that makes sense. Here's my sentence. Lucy took a quick blank back at the wardrobe. Spiteful? No. Glimpse? Yes! A glimpse is a quick look. Now pick the word that fits each sentence."},
 {"id": "gram", "find": "Grammar", "fold": GRAM_FOLD, "todo": "Read the before and after. Join the two sentences in the box.",
  "script": "Two short sentences can become one. The others did not believe Lucy. She was very unhappy. Put a joining word in front: Because the others did not believe her, comma, Lucy was very unhappy. Read the before and after. Then join the two sentences in the box."},
 {"id": "spell", "find": "Spelling", "fold": [], "foldText": ["The Rule:"], "todo": "Read the rule. Tap each card to see which vowel blurred.",
  "script": "Oops! I spelled lion like this: L, I, U, N. That's how it sounds. Li, un. But that lazy uh is spelled with an o. Lion. The schwa hides the real letter. Read the rule. Then tap each card to see which vowel blurred."},
 dict(READ, todo="Look back through Chapters 1 to 3. Then try the Truth Watch below.",
  script="No new chapters today. Look back through Chapters 1 to 3, and find Lewis's exact words. Then try the Truth Watch and the three questions."),
 dict(CHQ, script="Three questions, in full sentences. One, a detail you can touch and one you can hear, in Lewis's own words. Two, why the lamp-post is there, and how it makes you feel. Three, how the wardrobe seems ordinary at first, then magical."),
 dict(WRITE, todo="Write two evidence sentences. Use a short quote and say what it shows.",
  script="Today you add evidence. Clara used a short quote from the book, then told what it shows. Quote, then explain. Write two evidence sentences like that."),
], "cards": {},
 "virtue": [
  {"t": "Lucy could have said the story was made up for fun, but she would not say it.", "ok": True, "why": "Lucy was a very truthful girl, even when it made her unhappy."},
  {"t": "Edmund sneered and jeered, and asked if Lucy had found new countries in other cupboards.", "ok": False, "why": "He was being spiteful, not honest."},
  {"t": "In Narnia, Edmund shouts, “I’m sorry I didn’t believe you. I see now you were right all along.”", "ok": True, "why": "He says out loud that he was wrong."}]},
4: {"lookBtn": "Tap to learn about this picture of reindeer sledges", "mods": [
 dict(WGRD, script="[warmly] Here's today's reading tip. Why do readers believe in a world that isn't real? Because the small details feel true. Look for the one detail that convinces you most. " + LENS_END),
 dol("Although Mr. Tumnus served a fine tea, he could not hide his sadness from Lucy. Although starts the part that can't stand alone, so a comma follows tea."),
 {"id": "poem", "find": "Poetry", "fold": [":scope > .callout"], "todo": "Read the poem again. Then answer the question out loud.",
  "script": "Here's Blake's tiger poem again. Now think about Mr. Tumnus. He's a Faun, not a person, but he does so many things people do. Read the poem out loud again. Then answer the question about Mr. Tumnus out loud."},
 {"id": "morph", "find": "Morphology", "fold": [":scope > .key-concept"], "foldText": ["Before you roll"], "todo": "Tap Roll the Dice. Say what the word means. Tap Check My Thinking. Roll all six words.",
  "script": "Eyes closed for a second. What does tele mean? Far! Keep that in your head. Here's a word that's not on the dice. Teleconference. A meeting with people far away, on a screen. Now tap Roll the Dice. Say what each word means, and tap Check My Thinking. Roll all six."},
 {"id": "vocab", "find": "Vocabulary", "fold": [], "todo": "Choose one word. Write one sentence about Chapters 1 to 3.",
  "script": "Can one word tell a whole moment? Spiteful. Edmund was spiteful when he jeered at Lucy about countries in cupboards. One word, one moment from the book. Now choose one of your words and write your own sentence."},
 {"id": "gram", "find": "Grammar", "fold": GRAM_FOLD, "todo": "Tap Check yourself. Tap every word that needs fixing. Then tap See the answers.",
  "script": "Editors read in passes. Watch me. The queens sledge had bells and edmund heard them. Pass one, capitals: The, Queen, Edmund. Pass two, apostrophes: Queen's sledge. It belongs to her. Pass three, commas: one before and. Now do your passes, and tap every word that needs fixing."},
 {"id": "spell", "find": "Spelling", "fold": [], "foldText": ["The Rule:"], "todo": "Tap Roll the dice. Find the lazy beat. Tap Check my answer. Roll all six.",
  "script": "Here's my roll. Tumnus. Tum, nus. Which beat is quiet and lazy? The second one. Which vowel blurs? The u! Tap Roll the dice, say the word, and find the lazy beat. Then tap Check my answer."},
 dict(READ, todo="Look back at Chapters 1 to 3. Then try the Truth Watch below.",
  script="No new chapters today. Look back at Chapters 1 to 3, and choose the one detail that makes Narnia feel most real. Then try the Truth Watch and the three questions."),
 dict(CHQ, script="Three questions to finish the week, in full sentences. One, finish the sentence: Lewis makes Narnia feel real by. Two, the one best detail, and why it works. Three, one example that proves authors create a world with details."),
 dict(WRITE, todo="Write your closing sentence. Say your main idea in a new way.",
  script="Last step: your closing. Clara's first try just stopped. Her new closing says her main idea in a new way, and tells why it matters. Write your closing sentence."),
], "cards": {},
 "virtue": [
  {"t": "When the Faun asks, Lucy tells him the truth: she is human.", "ok": True, "why": "She answers him truthfully."},
  {"t": "Peter says Lucy’s story is “a jolly good hoax.”", "ok": False, "why": "Peter thinks Lucy made it up. He is wrong about her."},
  {"t": "Lucy tells the others, “It’s a magic wardrobe. There’s a wood inside it.”", "ok": True, "why": "She tells them exactly what she saw."}]},
}

HOW = {'morph3': 'Say each pair of parts out loud. Type the whole word in the box. Then tap Check My Answers.',
       'morph2': 'Read the Remember box. Then tap a word, and tap what it means. Match all four words.',
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
        if m['id'] in ids: m['video'] = 'g3ela-25-%d-teach-%s' % (d, m['id'])

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
                out['g3ela-25-%d-teach-%s' % (d, m['id'])] = t
        for w, t in cfg['cards'].items(): out['g3ela-25-%d-say-%s' % (d, w)] = t
    return out

if __name__ == '__main__':
    import sys
    for d, cfg in L.items():
        p = 'data/lesson-25-%d.json' % d
        j = json.load(io.open(p, encoding='utf-8'))
        if 'plate' in j: j['plate']['lookBtn'] = cfg['lookBtn']
        j['teach'] = {"dropTurnNotes": True, "mods": cfg['mods'], "cards": cfg['cards']}
        j['virtue'] = {"name": "honesty", "title": VTITLE, "items": cfg['virtue']}
        io.open(p, 'w', encoding='utf-8').write(json.dumps(j, ensure_ascii=False, indent=1))
        write_page('lesson-25-%d-lww.html' % d, j)
    rec = recorded(); tot = 0
    for k, t in rec.items():
        n = len(t); tot += n; print('%-32s %4d' % (k, n))
    print('recorded this week: %d / 6260 credits (%.0f%%)' % (tot, 100.0 * tot / 6260))
    io.open('/tmp/wk25_rec.json', 'w', encoding='utf-8').write(json.dumps(rec, ensure_ascii=False, indent=1))
