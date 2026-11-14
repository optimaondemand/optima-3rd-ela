#!/usr/bin/env python3
"""Week 23 (Medieval Nonfiction, part 1: four articles): the Nov 10 2026 pilot fixes, as on weeks 18-21.
Writes DATA.teach, plate.lookBtn and DATA.virtue (Diligence Watch, 3 facts a day from that day's article) into data/lesson-23-N.json AND the page's oao-data block.
Word Study scripts are written for the Opti films from the start: Day 1 teaches each idea; Days 2-4
show that day's activity with an example that is not an answer anywhere in the week, and no two
films open the same way. Article quotes are the articles' own words after acc_wk23.py.

    python tools/g3sparkle/teach_wk23.py
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
1: {"lookBtn": "Tap to learn about this painting of a real castle", "mods": [
 dict(WGRD, script="[warmly] Here's today's reading tip. Every article has one big idea it keeps coming back to. That's the central idea. The other facts are details that help prove it. " + LENS_END),
 {"id": "dol", "find": "Daily Oral", "fold": [], "todo": DOL_TODO,
  "script": "Let's fix a sentence. Look at the correct one first. King Henry lived in the Tower of London during the Middle Ages. King Henry is a person, the Tower of London is a place, and the Middle Ages is a time in history. Names get capitals. Tap the yellow parts. Then pick Sentence A or Sentence B, and type it the right way."},
 {"id": "morph", "find": "Morphology", "fold": [":scope > .callout:not(:has(+ .fillin-game)):not(:has(+ .dol-check-btn))"],
  "todo": "Think about the questions. Tap See if you cracked it. Type the missing part of each word.",
  "script": "[curious] Have you ever walked across a bridge? You start on one side and end up on the other. There's a word part that means across. Trans. T, r, a, n, s. Trans, plus Pacific, makes transpacific: across the Pacific Ocean. But careful! Tranquil starts with t, r, a, n, and it just means calm. Nothing goes across. Read the three words, and think about the questions. Then tap See if you cracked it, and type the missing parts."},
 {"id": "vocab", "find": "Vocabulary", "fold": VOCAB_FOLD, "todo": VOCAB_CLOZE_TODO,
  "script": "Let's be word detectives with a word that's not in your bank. Chamber. Here's a sentence. The lord slept in a small chamber at the top of the tower. He slept in it, so a chamber must be a room. One, read the sentence. Two, look for word parts. Three, check that the meaning fits. Fill in each sentence with a word from the bank, and tap Check My Work. Then play the matching game."},
 {"id": "gram", "find": "Grammar", "fold": GRAM_FOLD, "todo": "Tap Now check your thinking. Then sort each name: a person, a place, or a title.",
  "script": "[warmly] Some words are names, and names get capital letters. Listen. Stories say Robin Hood lived in Sherwood Forest. Robin Hood names a person. Sherwood Forest names a place. Every important word in a name gets a capital. A book title does too, like The Wind in the Willows. But little words inside, like in and the, stay small. Tap Now check your thinking. Then sort each name: a person, a place, or a title."},
 {"id": "spell", "find": "Spelling", "fold": [], "todo": "Say the words. Tap See the Rule. Then sort all eight words.",
  "script": "Watch me split a long word. Puppet. Find the vowels: u, and e. In between sit two consonants, p and p. Vowel, consonant, consonant, vowel. That's V C C V! So I split right between the two consonants. Pup. Pet. Say the words in Group A and Group B out loud, and tap See the Rule. Then sort all eight words."},
 {"id": "copia", "sel": ".spk-copia-card", "label": "Opti shows you how", "fold": [], "todo": "Write the sentence three new ways, one box at a time.",
  "script": "[warmly] Here's copia: one idea, said many ways. Let me try a different sentence first. The cook stirred the soup. Box one, change the opener: In the hot kitchen, the cook stirred the soup. Box two, a stronger verb: The cook swirled the soup. Box three, add a detail: The tired cook stirred the thick soup. Now it's your turn, one box at a time. If you get stuck, tap Show one way."},
 {"id": "read", "find": "Pause", "fold": [], "todo": READ_TODO,
  "script": "Read the two Pause and Think questions first. Then read the castle article below, with your lens in mind. When you finish, try the Diligence Watch right after the article. You don't write your Pause and Think answers."},
 {"id": "chq", "find": "Article Thinking", "fold": [], "todo": ART_TODO,
  "script": "Now answer in full sentences, with details from the article. One, what is the central idea? Say it in one sentence. Two, name two details that prove it. Three, how are the people in this castle like the people in The Whipping Boy's castle, and how are they different?"},
 dict(WRITE, todo="Write your own topic: one thing about medieval life you want to explain.",
  script="Clara started with castles. Too big! So she made it smaller: what servants did in a castle. A good topic is one thing you can explain. Write your own topic in the box. Use a sentence frame if you get stuck."),
], "cards": {},
 "virtue": [
  {"t": "Servants cooked food, cleaned, and cared for the horses.", "ok": True, "why": "They did hard jobs every day to keep the castle going."},
  {"t": "The keep was the strongest part of the castle.", "ok": False, "why": "That is a fact about a building, not about someone working."},
  {"t": "Young boys from noble families trained for years as pages.", "ok": True, "why": "Training for years takes steady, hard work."}]},
2: {"lookBtn": "Tap to learn about this drawing of a baker", "mods": [
 dict(WGRD, script="[warmly] Here's today's reading tip. This article has two paragraphs. Ask what each one is mostly about. Then find the one big idea that fits both. " + LENS_END),
 {"id": "dol", "find": "Daily Oral", "fold": [], "todo": DOL_TODO,
  "script": "Let's fix a sentence. Look at the correct one first. In medieval England, an apprentice might work for Master Thomas for seven years. See the comma after England? It ends the opening part. And Master Thomas gets two capitals: one for the title, one for the name. Tap the yellow parts. Then pick Sentence A or Sentence B, and type it the right way."},
 {"id": "poem", "find": "Poetry", "fold": [":scope > .callout", ":scope > .socratic-box"], "todo": "Read the poem out loud. Then say how it is different from a lie.",
  "script": "Here's a funny poem by Edward Lear, written long ago. Read it out loud. Could two owls, a hen, four larks and a wren really nest in one beard? No way! Lear stretches the truth on purpose. That's called hyperbole. Now think: how is this different from a lie? Say your answer out loud."},
 {"id": "morph", "find": "Morphology", "fold": [":scope > .callout:not(:has(+ .match-game))", ":scope > .key-concept"], "todo": "Tap a word, then tap what it means. Match all four words.",
  "script": "Remember, trans means across. Here's a long one that's not on your list. Transcontinental. Find trans at the front. A continent is a giant piece of land. So a transcontinental train goes all the way across it! +how:morph2"},
 {"id": "vocab", "find": "Vocabulary", "fold": VOCAB_FOLD, "todo": VOCAB_CLOZE_TODO,
  "script": "Here's a word from the world of trades. Guild. A guild was a club for one kind of worker, like all the bakers in a town. Read each sentence with a bank word in the blank. If it makes sense, keep it. Then play the matching game."},
 {"id": "gram", "find": "Grammar", "fold": GRAM_FOLD, "todo": "Read the Remember box. Then tap every word that needs a capital.",
  "script": "Spot the capitals with me. abbot peter walked to bath abbey. Abbot starts the sentence, and it's his title. Peter is his name. Bath Abbey is a place, so both words get capitals. That's four! Read the Remember box. Then tap every word that needs a capital."},
 {"id": "spell", "find": "Spelling", "fold": [], "foldText": ["The Rule:"], "todo": "Read the rule. In each row, tap the word with two consonants in the middle.",
  "script": "Use your eyes for this one. Sofa. Pony. Doctor. Which one has two consonants between its vowels? Doctor! O, then c and t, then o. Doc. Tor. Read the rule. Then in each row, tap the one word with two consonants in the middle."},
 {"id": "read", "find": "Pause", "fold": [], "todo": READ_TODO,
  "script": "Read the two Pause and Think questions first. Then read about servants and apprentices. After that, try the Diligence Watch, and watch my video in the Read Like a Writer box before you write."},
 {"id": "rwm", "sel": ".rwm-box", "after": ":scope > .rwm-header", "label": "Opti shows you how", "fold": [],
  "script": "[warmly] Let's try all three parts with a different sentence from today's article. Poor children worked in the fields or served in the homes of nobles. Part one, read like a reader. Poor children had jobs, in the fields or in a noble's home. Part two, read like a writer. The little word or joins two choices, and both halves have the same shape: worked in, served in. Part three, mimic. Here's mine: Opti worked in the library or perched in the old oak. Now it's your turn with the apprentice sentence. Write one sentence in each box."},
 {"id": "chq", "find": "Article Thinking", "fold": [], "todo": ART_TODO,
  "script": "Now answer in full sentences. One, what is the central idea? Say it in one sentence. Two, name one way boys and girls were alike, and one way they were different. Three, does Jemmy's job seem real, based on the article? Use one detail."},
 dict(WRITE, todo="Write your research question. Then write two notes from each of two articles, with their titles.",
  script="Clara's first notes were fuzzy, and they came from just one place. So she asked a research question first. Then she took notes from two articles, and wrote each title. Write your research question. Then take two notes from today's article and two from another one this week."),
], "cards": {},
 "virtue": [
  {"t": "An apprentice worked for a master craftsman for several years, learning every part of the job.", "ok": True, "why": "He kept at it for years until he knew the whole job."},
  {"t": "In the Middle Ages, most children did not go to school.", "ok": False, "why": "That tells what children did not do. It is not about someone working."},
  {"t": "Girls learned to weave and sew.", "ok": True, "why": "Weaving and sewing take patient, careful work."}]},
3: {"lookBtn": "Tap to learn about this painting of a king's feast", "mods": [
 dict(WGRD, script="[warmly] Here's today's reading tip. When you meet a new word, look at the sentences around it. They often explain it. Then ask: what does the author most want me to know about royal courts? " + LENS_END),
 {"id": "dol", "find": "Daily Oral", "fold": [], "todo": DOL_TODO,
  "script": "Let's fix a sentence. Look at the correct one first. Duke Richard of York bowed before Queen Margaret at the court of Westminster. Duke and Queen are titles, right before names, so they get capitals. But court stays small here, because it isn't part of a name. Tap the yellow parts. Then pick Sentence A or Sentence B, and type it the right way."},
 {"id": "morph", "find": "Morphology", "fold": [":scope > .callout:not(:has(+ .fillin-game))", ":scope > .key-concept"], "todo": "Say the parts out loud. Type the whole word in each box. Tap Check My Answers.",
  "script": "Let's build one together. Trans. It. Push them together: transit! Transit means going across, from one place to another, like a bus ride across town. +how:morph3"},
 {"id": "vocab", "find": "Vocabulary", "fold": VOCAB_FOLD, "todo": VOCAB_CLOZE_TODO,
  "script": "At court, people called the king Your Majesty. Majesty is a word for the greatness of a king or queen. Saying it showed respect. +how:vocabcloze"},
 {"id": "gram", "find": "Grammar", "fold": GRAM_FOLD, "todo": "Read the Remember box. Count the capitals in each sentence and type the number.",
  "script": "Count with me. earl roger sailed to ireland. Earl starts the sentence, and it's his title. One. Roger is his name. Two. Ireland is a place. Three. Sailed and to aren't names, so they stay small. Read the Remember box. Then count the capitals in each sentence, and type the number."},
 {"id": "spell", "find": "Spelling", "fold": [], "foldText": ["The Rule:"], "todo": "Read the rule. Tap each word to split it.",
  "script": "Oops. I split garlic like this: ga, rlic. That sounds wrong! The two consonants in the middle are r and l. Split between them. Gar. Lic. Garlic! Read the rule. Then tap each word to split it between its two middle consonants."},
 {"id": "read", "find": "Pause", "fold": [], "todo": READ_TODO,
  "script": "Read the two Pause and Think questions first. Then read about royal courts. Watch how the author explains the word protocol, right in the article. Then try the Diligence Watch and the Read Like a Writer box."},
 {"id": "chq", "find": "Article Thinking", "fold": [], "todo": ART_TODO,
  "script": "Four questions today, in full sentences. One, the central idea. Two, what the seating at the table shows about rank. Three, is it realistic that the prince was not punished? Four, why did the author write this: to tell a story, to explain, or to convince you?"},
 dict(WRITE, todo="Plan your paragraph in the box: a topic sentence, two details, and a closing sentence.",
  script="Today you plan. Clara put her notes in order. A topic sentence. Two details. And a closing sentence that doesn't just say the first one again. Plan your own paragraph the same way, in the box."),
], "cards": {},
 "virtue": [
  {"t": "Servants stood near the walls, ready to serve.", "ok": True, "why": "They stayed on their feet and ready to work the whole meal."},
  {"t": "Dukes and earls sat nearest the throne.", "ok": False, "why": "That is about where people sat, not about someone working."},
  {"t": "People at court had to learn strict rules about who bowed to whom.", "ok": True, "why": "Learning all those rules took care and effort."}]},
4: {"lookBtn": "Tap to learn about this painting of a lord at dinner", "mods": [
 dict(WGRD, script="[warmly] Here's today's reading tip. This article shows two sides, the rich and the poor. Watch for the words that tell you the author is switching sides. " + LENS_END),
 {"id": "dol", "find": "Daily Oral", "fold": [], "todo": DOL_TODO,
  "script": "Let's fix a sentence. Look at the correct one first. At the feast of Saint George, Lord Pembroke served roasted boar and French wine. French gets a capital, because it comes from the name of a country, France. Tap the yellow parts. Then pick Sentence A or Sentence B, and type it the right way."},
 {"id": "poem", "find": "Poetry", "fold": [":scope > .callout", ":scope > .socratic-box"], "todo": "Read the poem again. Then make up a hyperbole and say it out loud.",
  "script": "Here's Lear's beard poem again. This time, you make the hyperbole! How long does a school day feel? Stretch it so far that nobody could believe it. Say your sentence out loud. You don't need to write it."},
 {"id": "morph", "find": "Morphology", "fold": [":scope > .key-concept"], "foldText": ["Before you roll"], "todo": "Tap Roll the Dice. Say what the word means. Tap Check My Thinking. Roll all six words.",
  "script": "Riddle time. I come at the front of a word. I have five letters. And I mean across. What am I? Trans! Try this one. Transcribe. To write across, copying words from one place to another. Tap Roll the Dice. Say what each word means, and tap Check My Thinking. Roll all six."},
 {"id": "vocab", "find": "Vocabulary", "fold": VOCAB_FOLD, "todo": VOCAB_CLOZE_TODO,
  "script": "One more food word before you go. Trencher. The article says some people ate from thick slices of bread called trenchers. A plate you could eat! Read each sentence with a bank word in the blank. If it makes sense, keep it. Then play the matching game."},
 {"id": "gram", "find": "Grammar", "fold": GRAM_FOLD, "todo": "Tap the wrong word, or tap No mistake. Then tap See the answers and answer the question in the box.",
  "script": "Something looks funny here. We saw a Castle on the hill. Castle has a capital, but it isn't the name of one castle. It could be any castle! So it stays small. Read each sentence out loud. Tap the word that's wrong, or tap No mistake."},
 {"id": "spell", "find": "Spelling", "fold": [], "foldText": ["The Rule:", "Before you roll"], "todo": "Tap Roll the dice. Split the word. Tap Check my answer. Roll all six.",
  "script": "Roll one with me. Window! The vowels are i and o. In the middle sit n and w. Split between them. Win. Dow. +how:spell4"},
 {"id": "read", "find": "Pause", "fold": [], "todo": READ_TODO,
  "script": "Read the two Pause and Think questions first. Then read about medieval food. Look for the two sides, the rich and the poor. Then try the Diligence Watch and the Read Like a Writer box."},
 {"id": "chq", "find": "Article Thinking", "fold": [], "todo": ART_TODO,
  "script": "Now answer in full sentences. One, the central idea, in one sentence. Two, one food the rich ate, and one food the poor ate. Three, think about Chapter 6 of The Whipping Boy. Why did the prince and Jemmy eat so differently?"},
 dict(WRITE, todo="Write your topic sentence and at least one detail sentence. Use your plan from Day 3.",
  script="Today you start writing! Clara's topic sentence tells the main idea, and it makes you want to read more. Write your topic sentence and at least one detail. Use your plan from Day 3."),
], "cards": {},
 "virtue": [
  {"t": "People grew their own food in gardens or small farm plots.", "ok": True, "why": "Growing food takes work every day, all season long."},
  {"t": "A king's feast might include roasted meat, pies, fish, fruits, and sweet pastries.", "ok": False, "why": "That tells what was on the table, not who worked to make it."},
  {"t": "Meat was a rare treat for most ordinary people.", "ok": False, "why": "That is a fact about food, not about someone working."}]},
}

HOW = {'morph2': 'Read the Remember box. Then tap a word, and tap what it means. Match all four words.',
       'morph3': 'Say each pair of parts out loud. Type the whole word in the box. Then tap Check My Answers.',
       'vocabcloze': 'Read how we figured out the first word. Then fill in each sentence with a word from the word bank, and tap Check My Work. Last, play the matching game.',
       'spell4': 'Tap Roll the dice. Say the word out loud and split it into syllables. Then tap Check my answer. Roll all six words.'}
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
        if m['id'] in ids: m['video'] = 'g3ela-23-%d-teach-%s' % (d, m['id'])

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
                out['g3ela-23-%d-teach-%s' % (d, m['id'])] = t
        for w, t in cfg['cards'].items(): out['g3ela-23-%d-say-%s' % (d, w)] = t
    return out

if __name__ == '__main__':
    import sys
    for d, cfg in L.items():
        p = 'data/lesson-23-%d.json' % d
        j = json.load(io.open(p, encoding='utf-8'))
        if 'plate' in j: j['plate']['lookBtn'] = cfg['lookBtn']
        j['teach'] = {"dropTurnNotes": True, "mods": cfg['mods'], "cards": cfg['cards']}
        j['virtue'] = {"name": "diligence", "title": VTITLE, "items": cfg['virtue']}
        io.open(p, 'w', encoding='utf-8').write(json.dumps(j, ensure_ascii=False, indent=1))
        write_page('lesson-23-%d-med.html' % d, j)
    rec = recorded(); tot = 0
    for k, t in rec.items():
        n = len(t); tot += n; print('%-32s %4d' % (k, n))
    print('recorded this week: %d / 6260 credits (%.0f%%)' % (tot, 100.0 * tot / 6260))
    io.open('/tmp/wk23_rec.json', 'w', encoding='utf-8').write(json.dumps(rec, ensure_ascii=False, indent=1))
