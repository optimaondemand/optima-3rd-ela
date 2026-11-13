#!/usr/bin/env python3
"""Week 20 (The Whipping Boy, Ch. 11-15): the Nov 10 2026 pilot fixes, as on weeks 18-19.
Writes DATA.teach (Opti teaches before each activity; turns on one-step + Start here),
plate.lookBtn (notice first, reveal after) and DATA.virtue (Courage Watch)
into data/lesson-20-N.json AND the page's oao-data block.
Word Study scripts were written for the Opti films from the start (Nov 13 2026):
Day 1 teaches each idea; Days 2-4 show that day's activity with an example that is
not an answer anywhere in the week, and no two films open the same way.
Book quotes checked against Planning docs/whipping_boy_ocr.txt.

    python tools/g3sparkle/teach_wk20.py
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
VTITLE = "Courage Watch: Did they show courage?"
LENS_END = "Then tap one of the two lenses below to use while you read. You don't need to write anything."

L = {
1: {"lookBtn": "Tap to learn about this painting of a barn", "mods": [
 dict(WGRD, script="[warmly] Here's today's reading tip. Sometimes a character doesn't say how he feels. So watch what he does instead. In Chapter 12, Jemmy dives under the straw to hide. He never says, I'm scared. What do his actions tell you? " + LENS_END),
 {"id": "dol", "find": "Daily Oral", "fold": [], "todo": DOL_TODO,
  "script": "Let's fix a sentence. Look at the correct one first. The prince had crossed to the wicker basket and snatched up an uneaten apple tart. Nobody is talking, so there are no quotation marks. It starts with a capital letter, and a period ends it. Tap the yellow parts to see each rule. Then pick Sentence A or Sentence B, and type it the right way."},
 {"id": "morph", "find": "Morphology", "fold": [":scope > .callout:not(:has(+ .fillin-game)):not(:has(+ .dol-check-btn))"],
  "todo": "Think about the three questions. Tap See if you were right. Then type the missing word part in each box and tap Check My Work.",
  "script": "Here's a puzzle. Inspect. Spectator. Respect. Say them out loud. What five letters hide inside all three? Now picture a spectator at a ball game. What is a spectator doing the whole time? Watching! So what could that hidden part mean? Tap See if you were right. Then type the missing part in each box. Careful with suspect and expect. Say them slowly and listen for the s."},
 {"id": "vocab", "find": "Vocabulary", "fold": VOCAB_FOLD, "todo": "Listen to each card. Guess the meaning, then flip the card. Then play the matching game.",
  "script": "Let's be word detectives. Back in Chapter 8, Billy's red eyebrows shot up in bewildered surprise. Jemmy had just shocked him. Now the parts: be, wilder, e d. Wilder is an old word for getting lost in a wild place. So bewildered means so confused you feel lost. Now tap Opti reads it on each card. Guess, then flip. Then play the matching game."},
 {"id": "gram", "find": "Grammar", "fold": GRAM_FOLD, "todo": "Tap Now check your thinking. Then sort each phrase: where, when, or how.",
  "script": "Two sentences. Leaves crackled. Leaves crackled under Jemmy's feet. What did the second one add? It tells you more about the leaves, and it starts with the little word under. Under is a preposition. It sits in front of a noun and ties it to the rest of the sentence. Some prepositions tell where. Some tell when. Some tell how. Tap Now check your thinking. Then tap each phrase, and tap the question it answers."},
 {"id": "spell", "find": "Spelling", "fold": [], "todo": "Say and clap the words in Group A and B. Tap See the Rule. Then sort the six words.",
  "script": "Clap this one with me. Im, por, tant. Three beats! A long word is just small chunks stacked up. Find the vowels, split between them, read each chunk, then push them together. Say the words in Group A and Group B, and clap them. Tap See the Rule. Then sort the six words. Look at each chunk. Does one end with a vowel, like ba in bacon? Or end with a silent e, like cake?"},
 {"id": "copia", "sel": ".spk-copia-card", "label": "Opti shows you how", "fold": [], "todo": "Write the sentence three new ways, one box at a time.",
  "script": "[warmly] Remember copia? It means saying one idea in many ways. Watch me try one first, with a different sentence. The outlaw rode away. Box one, change the opener: Without a word, the outlaw rode away. Box two, swap the verb for a stronger one: The outlaw galloped away. Box three, add a detail: The big outlaw rode away on the king's horse. Now it's your turn, one box at a time. If you get stuck, tap Show one way."},
 {"id": "spotlight", "find": "Character Spotlight", "fold": [":scope > .socratic-box"],
  "script": "Here's something to think about. In Chapter 11, the prince refuses to go home, and Billy pulls off his belt. Jemmy steps in with a new plan. Jemmy has every reason to let the prince suffer. So why does he keep helping him? Keep that question with you while you read."},
 {"id": "read", "find": "^\\s*\\S*\\s*Read:", "fold": [], "todo": "Read the two questions. Skim Ch. 11 again. Then read Ch. 12 closely.",
  "script": "Time to read. You met Chapter 11 last week, so skim it to remember what happened. Then slow down for Chapter 12. First, read the two Pause and Think questions below. In Chapter 12, Jemmy makes a plan to escape, and he needs the prince to say one thing to Cutwater. Watch what the prince says instead. Stop at each question, think, and keep reading."},
 {"id": "chq", "find": "Chapter Thinking", "fold": [], "todo": CHQ_TODO,
  "script": "Now show what you understood. Answer in full sentences, with details from the book. One, when Cutwater comes back into the hut, what does the prince tell him? Two, why is Jemmy so surprised? Think about how the prince acted before. Three, is it a betrayal, or could there be another reason? For a challenge, pick Scholar, and add one more detail to each answer."},
 dict(WRITE, todo="Find one example in your paragraph. Write it again with the chapter number in it.",
  script="Good writers prove what they say. Listen to Clara. Her weak example was: the prince watches Jemmy get whipped. Which chapter? What exactly happened? Her strong example names Chapter 2, and gives the prince's own words. Now find one example in your paragraph that needs a chapter number. Write it again with the chapter and a clear detail."),
], "cards": {
 "bewildered": "Bewildered. Hold-Your-Nose Billy's red eyebrows shot up in bewildered surprise. Bewildered means completely confused.",
 "trifle": "Trifle. That crown! A trifle, scoffed Hold-Your-Nose Billy. A trifle is a small thing that is not worth much. Billy thinks a golden crown is not enough!",
 "truss": "Truss. Lads, you won't mind if I truss you up like a Christmas goose. To truss someone means to tie them up tight. That's Cutwater, in Chapter 12.",
 "ransom": "Ransom. The outlaws want gold from the king before they let the prince go. That gold is a ransom."},
 "virtue": [
  {"t": "Jemmy burrows under the moldy straw so he can slip away from Cutwater.", "ok": True, "why": "He is in danger, but he makes a plan and carries it out."},
  {"t": "Jemmy tells the prince, “Jemmy protects himself,” and says how he will escape.", "ok": True, "why": "He does not wait for someone to save him. He is ready to run."},
  {"t": "Cutwater asks where the prince is. The prince says, “Him? Over there. Under the straw.”", "ok": False, "why": "He gives Jemmy away instead of helping him."}]},
2: {"lookBtn": "Tap to learn about this forest painting", "mods": [
 dict(WGRD, script="[warmly] Here's today's reading tip. When two people argue, listen to both sides. After the chase in Chapter 13, Jemmy and the prince argue. Jemmy is furious. But the prince has something to say too. Ask yourself: does each boy have a point? " + LENS_END),
 {"id": "dol", "find": "Daily Oral", "fold": [], "todo": DOL_TODO,
  "script": "Let's fix a sentence. The correct one is from Chapter 13: Jemmy vanished into the wild green tangle. Jemmy is a name, so it starts with a capital. A period ends it. Now look at the sentence to fix. Dark and tangled both describe the same thing, so they need a comma between them. Tap the yellow parts. Then pick Sentence A or Sentence B, and type it the right way."},
 {"id": "poem", "find": "Poetry", "fold": [":scope > .callout", ":scope > .socratic-box"], "todo": "Read the poem out loud and count its lines. Then give two reasons it is not a haiku.",
  "script": "Here's a short poem about a little turtle. Is it a haiku? Let's check. A haiku has three lines: five beats, then seven, then five. And a haiku doesn't rhyme. Read the turtle poem out loud. Count the lines. Then listen to the ends of the lines. Do any of them rhyme? Now give two reasons it is not a haiku."},
 {"id": "morph", "find": "Morphology", "fold": [":scope > .callout:not(:has(+ .match-game))", ":scope > .key-concept"], "todo": "Tap a word, then tap what it means. Match all four words."},
 {"id": "vocab", "find": "Vocabulary", "fold": VOCAB_FOLD, "todo": "Listen to each card. Guess the meaning, then flip the card. Then play the matching game."},
 {"id": "gram", "find": "Grammar", "fold": GRAM_FOLD, "todo": "Tap Check yourself. Then tap every preposition in each sentence. Last, answer the question in the box."},
 {"id": "spell", "find": "^\\s*\\S*\\s*Spelling: Multi", "fold": [":scope > .socratic-box"], "foldText": SPELL_FOLDTEXT, "todo": "Say each word and clap its beats. In each row, tap the word with three syllables."},
 {"id": "spell2", "find": "Spelling Bonus", "fold": [], "todo": "Say the eight words. Tap Now name the pattern. Then sort each word: soft or hard.",
  "script": "Here's a bonus. Say these two words: cat, and city. Both start with c. But they don't sound the same! The letter after the c is the clue. When c or g comes right before e, i, or y, it goes soft. C says s, and g says j. Before any other letter, they stay hard. Say the eight words in the sort, and think about the questions. Tap Now name the pattern. Then sort each word."},
 {"id": "spotlight", "find": "Character Spotlight", "fold": [":scope > .socratic-box"],
  "script": "Think about this before you read. The prince gave Jemmy away. Then, after the chase, the prince says, Then I forgive you. Forgive Jemmy? For what? Watch both boys while they argue. Each one thinks he is the one who got wronged."},
 {"id": "read", "find": "^\\s*\\S*\\s*Read:", "fold": [], "todo": "Read the two questions. Then read Ch. 13–14 in your book.",
  "script": "Time to read Chapters 13 and 14. First, read the two Pause and Think questions below. Chapter 13 moves fast, so hang on. After the chase, listen to both sides of the argument. In Chapter 14, a girl comes through the woods calling for someone named Petunia. Then watch my video in the Read Like a Writer box before you try it."},
 {"id": "rwm", "sel": ".rwm-box", "after": ":scope > .rwm-header", "label": "Opti shows you how", "fold": [],
  "script": "[warmly] Read Like a Writer has three parts. Let me show you with a different sentence, from Chapter 14. Brambles, reaching out like cat's claws, tore at their fine garments. Part one, read like a reader. What is happening? The boys push through thorny bushes, and the thorns rip their fancy clothes. Part two, read like a writer. What does the author do? He says the brambles are like cat's claws, so we can almost feel the scratch. Part three, mimic. Here's mine: The snow, stinging like tiny bees, bit at my cheeks. Now it's your turn with the chase sentence. Write one sentence in each box."},
 {"id": "chq", "find": "Chapter Thinking", "fold": [], "todo": CHQ_TODO,
  "script": "Now answer in full sentences, with details from the book. One, tell Jemmy's escape step by step: how he gets out of the hut, what he does in the forest, and where he hides. Two, what does the prince say when Jemmy says, You betrayed me? Three, who is Betsy looking for, and which way does she point? For a challenge, pick Scholar, and add one more detail to each answer."},
 dict(WRITE, todo="Write your conclusion again. End with a question or a challenge.",
  script="Endings matter. Listen to Clara's first conclusion. It's fine, but it doesn't make you think. Her new one ends with a question: if no one ever teaches a prince to care about others, what kind of king will he become? Now that's an ending! Write your conclusion again. End with a question, or a challenge that starts with, If he never learns."),
], "cards": {
 "instinct": "Instinct. A thoroughbred of the streets, Jemmy acted on instinct. Instinct is doing something without stopping to think.",
 "foliage": "Foliage. Jemmy turned to the right and beat his way back into the foliage. Foliage means the leaves and branches of plants.",
 "tilt": "Tilt. Jemmy covered the ground at full tilt. At full tilt means as fast as you can go.",
 "bramble": "Bramble. Brambles, reaching out like cat's claws, tore at their fine garments. A bramble is a prickly, thorny bush."},
 "virtue": [
  {"t": "Jemmy bursts out of the straw and runs for the door before Cutwater can grab him.", "ok": True, "why": "He moves fast, even with an outlaw right there."},
  {"t": "The prince tells Jemmy, “Then I forgive you,” when it was the prince who gave Jemmy away.", "ok": False, "why": "Forgiving someone for being angry with you is not courage."},
  {"t": "Jemmy steps out of the trees and asks Betsy, a stranger, which way to the river.", "ok": True, "why": "He doesn’t know who she is, but he speaks up to get help."}]},
3: {"lookBtn": "Tap to learn about this river painting", "mods": [
 dict(WGRD, script="[warmly] Here's today's reading tip. Small things can tell you a lot about a character. On the mud flat in Chapter 15, watch what each boy picks up, and what each one says about it. What do those small moments show you? " + LENS_END),
 {"id": "dol", "find": "Daily Oral", "fold": [], "todo": DOL_TODO,
  "script": "Let's fix a sentence. The correct one is from Chapter 15: He spotted a barrel stave and pounced upon it. That's two actions, spotted and pounced, joined by and. Two actions joined like that don't need a comma. Capital letter at the start, period at the end. Tap the yellow parts. Then pick Sentence A or Sentence B, and type it the right way."},
 {"id": "morph", "find": "Morphology", "fold": [":scope > .callout:not(:has(+ .fillin-game))", ":scope > .key-concept"], "todo": "Say the parts out loud. Type the whole word in each box. Tap Check My Answers."},
 {"id": "vocab", "find": "Vocabulary", "fold": VOCAB_FOLD, "todo": "Fill in each sentence with a word from the word bank. Tap Check My Work. Then play the matching game."},
 {"id": "gram", "find": "Grammar", "fold": GRAM_FOLD, "todo": "Tap Check yourself. Type a bank word in each blank. Tap Check My Answers. Then write two sentences."},
 {"id": "spell", "find": "Spelling", "fold": [":scope > .socratic-box"], "foldText": SPELL_FOLDTEXT, "todo": "Clap the word. Then tap its chunks in order to build it."},
 {"id": "spotlight", "find": "Character Spotlight", "fold": [":scope > .socratic-box"],
  "script": "Think about this before you read. Jemmy says he'll give the prince the slip as soon as he can. He means it! But plans can change. Watch for the moment Jemmy looks back, and think about why he does what he does next."},
 {"id": "read", "find": "^\\s*\\S*\\s*Read:", "fold": [], "todo": "Read the two questions. Then read Ch. 15 in your book.",
  "script": "Time to read Chapter 15. First, read the two Pause and Think questions below. The tide is out, and the mud along the river has treasure in it, if you know where to look. Jemmy knows. Then a rickety old coach comes along. Stop at each question, think, and keep reading. After you read, do the Read Like a Writer box."},
 {"id": "chq", "find": "Chapter Thinking", "fold": [], "todo": CHQ_TODO,
  "script": "Now answer in full sentences, with details from the book. One, what is mudlarking, and why does Jemmy do it? Two, the prince picks up a broken chair leg and asks if it's worth anything. What does that small moment show? Three, what is Jemmy feeling when he sees the prince standing alone in the road? For a challenge, pick Scholar, and add one more detail to each answer."},
 dict(WRITE, todo="Check your paragraph with the checklist. Write one mistake you fixed.",
  script="Today you're the editor. Before anyone reads your paragraph, you check it. Go down the checklist one line at a time. Does every sentence start with a capital? Is there a comma before and, but, or so? Are names like Jemmy and Prince Brat capitalized? Fix what you find. Then write one mistake you fixed: what it was, and what it is now."),
], "cards": {},
 "virtue": [
  {"t": "The prince calls Jemmy’s mudlarking “Trash” and walks on ahead.", "ok": False, "why": "Making fun of someone’s work is not courage."},
  {"t": "Jemmy crawls over the embankment and asks a stranger, Captain Nips, for a ride.", "ok": True, "why": "He speaks up to a stranger to get where he needs to go."},
  {"t": "Jemmy shouts, “Stop, Cap’n!” and has the coach wait for the prince.", "ok": True, "why": "He could ride away free, but he goes back for the prince."}]},
4: {"lookBtn": "Tap to learn about this painting of an old coach", "mods": [
 dict(WGRD, script="[warmly] There are no new chapters today. Instead, look back. In Chapter 12, the prince gave Jemmy away. In Chapter 15, Jemmy went back for him. Something changed in between. Which moment do you think changed the story the most? Then tap one of the two lenses below to use while you look back. You don't need to write anything."),
 {"id": "dol", "find": "Daily Oral", "fold": [], "todo": DOL_TODO,
  "script": "Let's fix a sentence. Look at the correct one. Jemmy thought he saw a smile flash across the prince's face. The face belongs to the prince, so prince's needs an apostrophe before the s. Now look at the sentence to fix. Does something belong to someone there too? Tap the yellow parts. Then pick Sentence A or Sentence B, and type it the right way."},
 {"id": "poem", "find": "Poetry", "fold": [":scope > .callout", ":scope > .socratic-box"], "todo": "Make up a haiku about the turtle. Count 5, 7, 5, with no rhyme. Say it out loud.",
  "script": "Here's the turtle poem again. Today, turn it into a haiku. Remember, three lines, five beats, then seven, then five, and no rhyme. You can't fit everything in, so pick the best part. Maybe the box, or the puddle, or the rocks. Count the beats on your fingers. Say your haiku out loud. Then think: what did you leave out?"},
 {"id": "morph", "find": "Morphology", "fold": [":scope > .key-concept"], "foldText": ["Before you roll"], "todo": "Tap Roll the Dice. Say what the word means. Tap Check My Thinking. Roll all six words."},
 {"id": "vocab", "find": "Vocabulary", "fold": VOCAB_FOLD, "todo": "Fill in each sentence with a word from the word bank. Tap Check My Work. Then play the matching game."},
 {"id": "gram", "find": "Grammar", "fold": GRAM_FOLD, "todo": "Tap the wrong word, or tap No mistake. Then tap See the answers and answer the question in the box."},
 {"id": "spell", "find": "Spelling", "fold": [":scope > .socratic-box", ":scope > .dol-check-btn", "#spellRuleReveal"], "foldText": SPELL_FOLDTEXT, "todo": "Tap Roll the dice. Say the word and split it. Tap Check my answer. Roll all six words."},
 {"id": "spotlight", "find": "Character Spotlight", "fold": [":scope > .socratic-box"],
  "script": "Look back at the whole week. In Chapter 12, the prince gives Jemmy away. In Chapter 15, Jemmy calls the prince his friend. Then he wonders why he said it! What happened in between? Was it the chase, the argument, Betsy, or the mud flat?"},
 {"id": "read", "find": "Look Back", "fold": [], "todo": "Read the two questions. Then look back through Ch. 11–15 in your book.",
  "script": "There are no new chapters today. Instead, look back through Chapters 11 to 15 in your book. First, read the two Pause and Think questions below. One asks which event tells you the most about the prince. The other asks if Jemmy trusts the prince more now. Flip back through the pages to find clues. Then do the Read Like a Writer box."},
 {"id": "chq", "find": "Chapter Thinking", "fold": [], "todo": CHQ_TODO,
  "script": "Now look back and answer in full sentences, with details from the book. One, the prince gives Jemmy away, and later Jemmy goes back for him. What does that tell you about Jemmy? Two, how does Betsy's direction help the boys? Three, what danger is still coming at the end of Chapter 15? For a challenge, pick Scholar, and add one more detail to each answer."},
 dict(WRITE, todo="Label the five parts of your paragraph. Write one thing you are proud of and one thing you would make better.",
  script="Today you finish your opinion paragraph. Clara checked hers by labeling every part: claim, reason, example, the other side, and conclusion. All five were there, so she was ready. Now label the parts in yours. Is anything missing? Then write one thing you're proud of, and one thing you'd make better next time."),
], "cards": {},
 "virtue": [
  {"t": "Jemmy runs from Cutwater and hides inside a hollow tree.", "ok": True, "why": "He keeps his head and finds a hiding place, even with an outlaw right behind him."},
  {"t": "Cutwater asks where the prince is, and the prince points to the straw.", "ok": False, "why": "He gives Jemmy away to save himself."},
  {"t": "Jemmy has the coach stop for the prince, even after the prince gave him away.", "ok": True, "why": "Going back for someone who hurt you takes courage."}]},
}

# Opti films (skill §8h): every Word Study section, Days 1-4, + Day 2 Read Like a Writer.
# Day 1 scripts above teach each idea. Days 2-4: short, show that day's activity with an
# example that is not an answer anywhere in week 20, no Day 1 re-teaching, no two openers alike.
# "+how:" ending = a shared direction clip already recorded (clip-log: same voice, same words);
# only the part before it is recorded, then the two are joined.
WS2 = {
 2: {"morph": "Quick reminder: spect means look. Now try a new one. Spectacular. Find spect. The fireworks were spectacular. So amazing that everybody had to look! Do the same with each word on the left. Find spect, look at the parts around it, then tap the meaning that fits.",
     "vocab": "Here's instinct, from Chapter 13. Jemmy acted on instinct. He didn't stop to think. He just ran! Instinct is what you do before your brain catches up. Listen to each card, guess the meaning, then flip it. Then match all four.",
     "gram": "Sentences love prepositions. Listen. The prince ran across the clearing to the edge of the woods. Across. To. Of. Three! Tap Check yourself. Then tap every preposition in each sentence. Keep going until you find them all.",
     "spell": "Clap this word: ham, bur, ger. Hamburger. Three beats! In each row, three words have two beats, and one word has three. Clap every word out loud, then tap the one with three beats."},
 3: {"morph": "Let's build one together. Pro, plus spect, plus or. Prospector! A person who looks for gold. The last word on your page has three parts too. Push all three together. +how:morph3",
     "vocab": "When the prince asks Jemmy what he's doing in the mud, Jemmy answers with one word. Mudlarking! Mud, plus lark, which means to poke about. +how:vocabcloze",
     "gram": "Same coach, three places. The coach rolled into the mud. Stuck! The coach rolled through the mud. It kept going. The coach rolled past the mud. It never touched it! Only one word changed. Now read each sentence below, and check the clue at the end: where, when, or how. Type the bank word that fits.",
     "spell": "Here's a word in pieces. Tic. Fan. Tas. That's the wrong order! Clap it first: fan, tas, tic. Fantastic! Now tap the chunks in order. First, middle, last. If a chunk won't stick, try another one."},
 4: {"morph": "Ready to roll? Every word on the dice has spect in it, so every word is about looking. Look at the parts around spect. They tell you what kind of looking. Say what the whole word means out loud. Then tap Check My Thinking. Do all six.",
     "vocab": "I can't have you sticking to me like a barnacle! That's Jemmy, grumbling at the prince in Chapter 14. A barnacle is a little sea creature that glues itself to ships. Now read each sentence out loud with a bank word in the blank. If it sounds right, keep it.",
     "gram": "Captain Nips sat under his coach and drove away. Wait, under? He'd be in the mud! He sat on his coach. That's a preposition doing the wrong job. Read each sentence and picture it. Tap the wrong word, or tap No mistake.",
     "spell": "Watch me split a long one. Hel, i, cop, ter. Helicopter. Four beats. +how:spell4"},
}
HOW = {'morph3': 'Say each pair of parts out loud. Type the whole word in the box. Then tap Check My Answers.',
       'vocabcloze': 'Read how we figured out the first word. Then fill in each sentence with a word from the word bank, and tap Check My Work. Last, play the matching game.',
       'spell4': 'Tap Roll the dice. Say the word out loud and split it into syllables. Then tap Check my answer. Roll all six words.'}
SPLICE = {}
for d, scr in WS2.items():
    for m in L[d]['mods']:
        if m['id'] in scr:
            t = scr[m['id']]
            if '+how:' in t:
                new, slug = t.split(' +how:')
                SPLICE[(d, m['id'])] = 'g3ela-how-' + slug
                t = new + ' ' + HOW[slug]
            m['script'] = t
VIDEO = {1: ['morph', 'vocab', 'gram', 'spell'], 2: ['morph', 'vocab', 'gram', 'spell', 'rwm'],
         3: ['morph', 'vocab', 'gram', 'spell'], 4: ['morph', 'vocab', 'gram', 'spell']}
for d, ids in VIDEO.items():
    for m in L[d]['mods']:
        if m['id'] in ids: m['video'] = 'g3ela-20-%d-teach-%s' % (d, m['id'])

def write_page(f, D):
    html = io.open(f, encoding='utf-8', newline='').read()
    m = re.search(r'(<script type="application/json" id="oao-data">)(.*?)(</script>)', html, re.S)
    old = m.group(2)
    if '\n' not in old.strip(): body = json.dumps(D, ensure_ascii=False, separators=(',', ':'))
    else: body = json.dumps(D, ensure_ascii=False, indent=1)
    body = body.replace('</script', '<\\/script')
    lead = old[:len(old) - len(old.lstrip())]; tail = old[len(old.rstrip()):]
    io.open(f, 'w', encoding='utf-8', newline='').write(html[:m.start(2)] + lead + body + tail + html[m.end(2):])

for d, cfg in L.items():
    p = 'data/lesson-20-%d.json' % d
    j = json.load(io.open(p, encoding='utf-8'))
    j['plate']['lookBtn'] = cfg['lookBtn']
    j['teach'] = {"dropTurnNotes": True, "mods": cfg['mods'], "cards": cfg['cards']}
    j['virtue'] = {"name": "courage", "title": VTITLE, "items": cfg['virtue']}
    io.open(p, 'w', encoding='utf-8').write(json.dumps(j, ensure_ascii=False, indent=1))
    write_page('lesson-20-%d-wb.html' % d, j)
    n = sum(len(re.sub(r'\[[^\]]*\]\s*', '', x.get('script', ''))) for x in cfg['mods']) + sum(len(v) for v in cfg['cards'].values())
    print('20.%d teach credits %d' % (d, n))
