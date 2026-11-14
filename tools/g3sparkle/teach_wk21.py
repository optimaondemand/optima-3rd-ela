#!/usr/bin/env python3
"""Week 21 (The Whipping Boy, Ch. 16-20): the Nov 10 2026 pilot fixes, as on weeks 18-20.
Writes DATA.teach (Opti teaches before each activity; turns on one-step + Start here),
plate.lookBtn (notice first, reveal after) and DATA.virtue (Courage Watch)
into data/lesson-21-N.json AND the page's oao-data block.
Word Study scripts are written for the Opti films from the start: Day 1 teaches each idea
(and Day 2's Spelling Bonus teaches their/there/they're); Days 2-4 show that day's activity
with an example that is not an answer anywhere in the week, and no two films open the same way.
Book quotes checked against Planning docs/whipping_boy_ocr.txt.

    python tools/g3sparkle/teach_wk21.py
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
VOCAB_FLIP_TODO = "Listen to each card. Guess the meaning, then flip the card. Then play the matching game."
VOCAB_CLOZE_TODO = "Fill in each sentence with a word from the word bank. Tap Check My Work. Then play the matching game."

L = {
1: {"lookBtn": "Tap to learn about this painting of a dancing bear", "mods": [
 dict(WGRD, script="[warmly] Here's today's reading tip. At the end of a book, the characters have usually learned something. That lesson is called the theme. In Chapters 16 and 17, watch the prince. Has he learned something? Has Jemmy? " + LENS_END),
 {"id": "dol", "find": "Daily Oral", "fold": [], "todo": DOL_TODO,
  "script": "Let's fix a sentence. Look at the correct one first. Bawl out! Jemmy shouted. I won't tell anyone! Jemmy says two things, so each one gets its own quotation marks. The exclamation marks go inside. Tap the yellow parts to see each rule. Then pick Sentence A or Sentence B, and type it the right way."},
 {"id": "morph", "find": "Morphology", "fold": [":scope > .callout:not(:has(+ .fillin-game)):not(:has(+ .dol-check-btn))"],
  "todo": "Think about the question. Tap See what was hiding. Then type each whole word and tap Check My Answers.",
  "script": "[warmly] Here's a trick for big words. Cover the front part. Retell. Cover the re, and tell is left. Re means again, so retell means tell again. Five word parts work like that. Re means again. Pre means before. Mis means wrong. And two of them mean not: un and dis. Read the five words, and think about the question. Then tap See what was hiding. Last, type each whole word."},
 {"id": "vocab", "find": "Vocabulary", "fold": VOCAB_FOLD, "todo": VOCAB_FLIP_TODO,
  "script": "Let's be word detectives. In Chapter 17, Jemmy watches the prince get up off the mud, and he thinks: There was a cast-iron streak of pluck in him. Cast iron is hard and strong. So pluck must be something strong inside a person. Courage! Now tap Opti reads it on each card. Guess, then flip. Then play the matching game."},
 {"id": "gram", "find": "Grammar", "fold": GRAM_FOLD, "todo": "Tap Now check your thinking. Then sort each phrase: where, when, or how.",
  "script": "Listen. Jemmy hid. Jemmy hid under the potatoes. The new part starts with under and ends with potatoes. That whole group is a prepositional phrase. It starts with a preposition and ends on a noun. Some tell where, like under the potatoes. Some tell when, like after dark. Some tell how, like with a shout. Tap Now check your thinking. Then sort each phrase: where, when, or how."},
 {"id": "spell", "find": "Spelling", "fold": [], "todo": "Read the three sentences. Tap See the Rule. Then sort each phrase: to, two, or too.",
  "script": "Say these with me. To. Two. Too. They sound exactly the same! Your ears can't help you, so the spelling has to. Two, t w o, is the number, like two boys. Too, with two o's, means also, or more than enough, like too hot. To points somewhere, like to the castle. Read the three sentences, and tap See the Rule. Then tap each phrase, and tap the spelling it needs."},
 {"id": "copia", "sel": ".spk-copia-card", "label": "Opti shows you how", "fold": [], "todo": "Write the sentence three new ways, one box at a time.",
  "script": "[warmly] Remember copia? It means saying one idea in many ways. Watch me try one first, with a different sentence. The coach stopped. Box one, change the opener: On the river road, the coach stopped. Box two, swap the verb for a stronger one: The coach jolted to a halt. Box three, add a detail: The old potato coach stopped. Now it's your turn, one box at a time. If you get stuck, tap Show one way."},
 {"id": "spotlight", "find": "Character Spotlight", "fold": [":scope > .socratic-box"],
  "script": "Here's something to think about. Jemmy tells the prince to say he swam the river. Then he hides, and he holds his breath. He thinks the prince might give him away again, like he did in Chapter 12. Will he? Keep that question with you while you read."},
 {"id": "read", "find": "^\\s*\\S*\\s*Read:", "fold": [], "todo": "Read the two questions. Then read Ch. 16–17 in your book.",
  "script": "Time to read Chapters 16 and 17. First, read the two Pause and Think questions below. In Chapter 16, the outlaws stop the coach, and Billy picks up a whip. Watch the prince's face, and listen for what he does not say. Then in Chapter 17, someone comes to help. Stop at each question, think, and keep reading."},
 {"id": "chq", "find": "Chapter Thinking", "fold": [], "todo": CHQ_TODO,
  "script": "Now show what you understood. Answer in full sentences, with details from the book. One, the prince makes no sound when he is whipped, just like Jemmy always did. What does that tell you? Two, what does Jemmy think about the prince afterward? Three, where does each outlaw go when the bear charges? For a challenge, pick Scholar, and add one more detail to each answer."},
 dict(WRITE, todo="Fill in the chart for each boy: beginning, end, and what changed him.",
  script="This week you compare Jemmy and the prince. Clara started with rough notes. Then she made them better: for each boy, she wrote how he acted at the beginning, how he acts later, and the chapter where she saw it. Now fill in the chart for both boys. Beginning, end, and what changed him."),
], "cards": {
 "pluck": "Pluck. There was a cast-iron streak of pluck in him. Pluck means courage, being brave when things are hard.",
 "defiant": "Defiant. The prince remained defiant. I'm staying, he said. Defiant means refusing to give in.",
 "girded": "Girded. Prince Brat only girded himself for the next blow. Girded means he got ready for something hard.",
 "snarling": "Snarling. The bear came snarling down the embankment. Snarling means making a low, angry growl."},
 "virtue": [
  {"t": "Jemmy tells the outlaws, “Lay down the whip,” and calls them simpletons.", "ok": True, "why": "He speaks up to two outlaws to stop the whipping."},
  {"t": "Billy whips the prince, and the prince does not make a sound.", "ok": True, "why": "He is hurt, but he stays strong."},
  {"t": "When the bear charges, Cutwater drops the prince and runs off like a greyhound.", "ok": False, "why": "He runs to save himself and leaves the boy behind."}]},
2: {"lookBtn": "Tap to learn about this picture of an old fair", "mods": [
 dict(WGRD, script="[warmly] Here's today's reading tip. Sometimes one small word means a lot. Today, listen for the word friend. Who says it, and how does the other boy answer? " + LENS_END),
 {"id": "dol", "find": "Daily Oral", "fold": [], "todo": DOL_TODO,
  "script": "Let's fix a sentence. The correct one is from Chapter 18: The prince drained the mug and shuffled away. One person does two things, drained and shuffled, joined by and. No comma needed. Now look at the sentence to fix. Something belongs to someone there, so watch for an apostrophe. Tap the yellow parts. Then pick Sentence A or Sentence B, and type it the right way."},
 {"id": "poem", "find": "Poetry", "fold": [":scope > .callout", ":scope > .socratic-box"], "todo": "Read the poem out loud. Then find two things in the poem that act like people.",
  "script": "Here's a short poem about an eagle on a high rock. Read it out loud. Now look closer. Does an eagle really have hands? Can the sea really crawl? The poet writes about them as if they were people. That's called personification. Find two things in the poem that act like people."},
 {"id": "morph", "find": "Morphology", "fold": [":scope > .callout:not(:has(+ .match-game))", ":scope > .key-concept"], "todo": "Tap a word, then tap what it means. Match all four words.",
  "script": "Can you spot the front part in replay? Re. Cover it, and play is left. So replay means play again. Do that with every word on the left. Find the front part, then look at what is left. +how:morph2"},
 {"id": "vocab", "find": "Vocabulary", "fold": VOCAB_FOLD, "todo": VOCAB_FLIP_TODO,
  "script": "At the fair, Jemmy hears something brand new. The prince laughs! The book calls that sound merriment. Merry, plus ment. Happy laughing and fun. Listen to each card, guess the meaning, then flip it. Then match all four."},
 {"id": "spell2", "find": "Spelling Bonus", "fold": [], "todo": "Read the two sentences. Tap Now check your thinking. Sort the words. Then pick the right spelling in each sentence.",
  "script": "Here's a riddle. Which word has the word here hiding inside it? There! And there is a place, just like here. Their means it belongs to them, like their cart. They're is two words squished together: they are. The apostrophe stands in for the missing letter. Its and it's work the same way. Read the two sentences, and tap Now check your thinking. Then sort the words, and pick the right spelling in each sentence."},
 {"id": "spell", "find": "^\\s*\\S*\\s*Spelling: Homophones", "fold": [], "foldText": SPELL_FOLDTEXT, "todo": "Read each whole sentence. Tap the spelling that fits.",
  "script": "Watch me pick one. Blank coats were torn. Try they are. They are coats were torn? No! Is it a place? No. The coats belong to the boys. So it's their, t h e i r. Read each whole sentence first. Then tap the spelling that fits."},
 {"id": "spotlight", "find": "Character Spotlight", "fold": [":scope > .socratic-box"],
  "script": "Think about this before you read. At the fair, the prince gives himself a new name. And in the dark sewer, the boys end up holding hands. Not long ago, they couldn't stand each other. What changed?"},
 {"id": "read", "find": "^\\s*\\S*\\s*Read:", "fold": [], "todo": "Read the two questions. Then read Ch. 18–19 in your book.",
  "script": "Time to read Chapters 18 and 19. First, read the two Pause and Think questions below. At the fair, the prince carries something for the first time in his life. Then a news seller shouts about the whipping boy, and Jemmy runs for the sewers. Watch who follows him. After you read, watch my video in the Read Like a Writer box before you try it."},
 {"id": "rwm", "sel": ".rwm-box", "after": ":scope > .rwm-header", "label": "Opti shows you how", "fold": [],
  "script": "[warmly] Read Like a Writer has three parts. Let me show you with a different sentence, from Chapter 18. The news seller appeared, his tongue wagging like a bell clapper. Part one, read like a reader. What is happening? A man is selling news, and he shouts and shouts. Part two, read like a writer. The author says his tongue is like a bell clapper, the part that swings inside a bell and bangs. Now we can hear how loud he is! Part three, mimic. Here's mine: The puppy's tail thumped like a drum. Now it's your turn with Jemmy's sentence. Write one sentence in each box."},
 {"id": "chq", "find": "Chapter Thinking", "fold": [], "todo": CHQ_TODO,
  "script": "Now answer in full sentences, with details from the book. One, what does the prince say when he carries the kettle, and what does it show? Two, what does the news seller shout, and how does Jemmy feel? Three, what happens between the boys in the dark sewer? For a challenge, pick Scholar, and add one more detail to each answer."},
 dict(WRITE, todo="Write the opening sentence of your comparison. Name both boys.",
  script="A comparison needs a strong first sentence. Clara's first try was: Jemmy and Prince Brat both changed. True, but short! Her new one tells how each boy started, and says they both changed. Now write your opening sentence. Name both boys, and say how each one started."),
], "cards": {
 "merriment": "Merriment. The sound of merriment lingered in his head. Merriment means happy laughing and fun.",
 "hubbub": "Hubbub. Through the hubbub came a great squeaky voice. A hubbub is a loud, busy noise from a crowd.",
 "broadside": "Broadside. The news seller had a bundle of broadsides under his arm. A broadside is a big printed news sheet.",
 "grain-fed": "Grain-fed. Grain-fed rats were swarming over the two of them. Grain-fed means fed well on grain."},
 "virtue": [
  {"t": "The prince is terrified of the dark, but he jumps into the black sewer after Jemmy.", "ok": True, "why": "He is scared, and he does it anyway."},
  {"t": "Cutwater cries, “Mercy on us!” when he finds out they whipped the real prince.", "ok": False, "why": "He is afraid of what the king will do to him."},
  {"t": "With the outlaws close by, the prince grabs the birdcage and throws it toward the brewery.", "ok": True, "why": "He acts fast to send the outlaws the wrong way."}]},
3: {"lookBtn": "Tap to learn about this painting of a throne room", "mods": [
 dict(WGRD, script="[warmly] Here's today's reading tip. Today you read the very last chapter. The theme is the big lesson the story wants you to take away. As you read, ask: what is this story saying about friends, and about people changing? " + LENS_END),
 {"id": "dol", "find": "Daily Oral", "fold": [], "todo": DOL_TODO,
  "script": "Let's fix a sentence. Look at the correct one. We're going back to the castle, said the prince. The words he says go inside quotation marks, with a comma before the closing mark. Then comes who said it. Tap the yellow parts. Then pick Sentence A or Sentence B, and type it the right way."},
 {"id": "morph", "find": "Morphology", "fold": [":scope > .callout:not(:has(+ .fillin-game))", ":scope > .key-concept"], "todo": "Say the parts out loud. Type the whole word in each box. Tap Check My Answers.",
  "script": "Watch this. Pre, plus pay. Prepay! To pay before. +how:morph3"},
 {"id": "vocab", "find": "Vocabulary", "fold": VOCAB_FOLD, "todo": VOCAB_CLOZE_TODO,
  "script": "Here's a word from Chapter 20 that's not on your list. The ballad sellers sang about the notorious life of Hold-Your-Nose Billy. Notorious means famous for something bad. Billy sure was! +how:vocabcloze"},
 {"id": "gram", "find": "Grammar", "fold": GRAM_FOLD, "todo": "Read the Remember box. Type the noun each phrase ends on. Tap Check My Answers.",
  "script": "Where does a prepositional phrase stop? On a noun. Behind the golden doors. Behind. The. Golden. Doors! Doors is the noun, so that's where it stops. Read each sentence, find the phrase, and type the noun it ends on. Use the word bank."},
 {"id": "spell", "find": "Spelling", "fold": [], "foldText": SPELL_FOLDTEXT, "todo": "Read each sentence. Tap the spelling that fits.",
  "script": "Spot my mistake. Petunia can dance two. Two is a number! I mean also, so it's t o o. Say each sentence with the meaning in your head. Then tap the spelling that fits."},
 {"id": "spotlight", "find": "Character Spotlight", "fold": [":scope > .socratic-box"],
  "script": "Think about this before you read. Jemmy has a price on his head. The king thinks he is a rascal. And the prince wants to walk him right back to the castle. Is that a trick, or a plan? Watch the prince closely."},
 {"id": "read", "find": "^\\s*\\S*\\s*Read:", "fold": [], "todo": "Read the two questions. Then read Ch. 20 in your book.",
  "script": "Time to read Chapter 20, the last chapter. First, read the two Pause and Think questions below. The prince does something that looks like a betrayal. Keep reading, and watch his face. Then the boys stand in front of the king. Listen for the promise the prince made. After you read, do the Read Like a Writer box."},
 {"id": "chq", "find": "Chapter Thinking", "fold": [], "todo": CHQ_TODO,
  "script": "Now answer in full sentences, with details from the book. One, why doesn't Jemmy want to go back, and how does the prince get him to come? Two, what has the prince sworn to do, and what does Jemmy figure out? Three, what does the king say at the very end? For a challenge, pick Scholar, and add one more detail to each answer."},
 dict(WRITE, todo="Write one way the boys changed the same, and one way they changed differently.",
  script="The middle of a comparison has two parts. First, how are the boys alike? Then, how are they different? Clara says both boys learned to trust someone very different. Then she says how each boy changed in his own way. Now write one way they changed the same, and one way they changed differently."),
], "cards": {},
 "virtue": [
  {"t": "Jemmy has a price on his head, but he follows the prince back toward the castle.", "ok": True, "why": "He is scared, and he goes anyway."},
  {"t": "Betsy is told to turn Jemmy in, and she says, “I’ll do no such thing.”", "ok": True, "why": "She stands up for Jemmy, even when a boy says he is the prince."},
  {"t": "When the prince says to turn him in, Jemmy thinks, Run for it.", "ok": False, "why": "At first he wants to run away. Then he sees the wink."}]},
4: {"lookBtn": "Tap to learn about this painting of a ship", "mods": [
 dict(WGRD, script="[warmly] You finished the whole book! There are no new chapters today. Think about the prince in Chapter 1, and the prince in Chapter 20. Think about Jemmy too. What was this story really about? Then tap one of the two lenses below to use while you look back. You don't need to write anything."),
 {"id": "dol", "find": "Daily Oral", "fold": [], "todo": DOL_TODO,
  "script": "Let's fix a sentence. The correct one is from Chapter 20. You got me off without so much as a single whack, Jemmy whispered. His words go inside quotation marks, and a comma goes before the closing mark. Tap the yellow parts. Then pick Sentence A or Sentence B, and type it the right way."},
 {"id": "poem", "find": "Poetry", "fold": [":scope > .callout", ":scope > .socratic-box"], "todo": "Read the poem out loud again. Then answer the question about the word crawls.",
  "script": "Here's the eagle poem again. This time, look at just one word: crawls. The wrinkled sea beneath him crawls. Picture the sea from way up high. Does it look fast or slow? Big or small? Answer the question about what that one word tells you."},
 {"id": "morph", "find": "Morphology", "fold": [":scope > .key-concept"], "foldText": ["Before you roll"], "todo": "Tap Roll the Dice. Say what the word means. Tap Check My Thinking. Roll all six words.",
  "script": "Five word parts, one dice. Roll a word. Find the front part, and say what it means. Then say what the whole word means, out loud. Tap Check My Thinking to see if you were right. Roll all six."},
 {"id": "vocab", "find": "Vocabulary", "fold": VOCAB_FOLD, "todo": VOCAB_CLOZE_TODO,
  "script": "Gaw! That's Jemmy's word when something amazes him. Today's words come from the whole week. Read each sentence out loud with a bank word in the blank. If it sounds right and makes sense, keep it. Then play the matching game."},
 {"id": "gram", "find": "Grammar", "fold": GRAM_FOLD, "todo": "Tap the wrong word, or tap No mistake. Then tap See the answers and answer the question in the box.",
  "script": "Picture this. The bear danced on of the cart. On of? Two prepositions in a row, and it makes no sense. A phrase needs one preposition and one noun. Read each sentence and picture it. Tap the broken word, or tap No mistake."},
 {"id": "spell", "find": "Spelling", "fold": [], "foldText": SPELL_FOLDTEXT, "todo": "Tap Roll the dice. Say which spelling fits and why. Tap Check my answer. Roll all six.",
  "script": "Roll one with me. Blank big dogs. Is it a number? Yes, two dogs, so t w o. Now roll all six. Say which spelling fits, and say why."},
 {"id": "spotlight", "find": "Character Spotlight", "fold": [":scope > .socratic-box"],
  "script": "Look back at the whole book. In Chapter 1, Jemmy is whipped for the prince's tricks. By Chapter 20, the prince makes promises so Jemmy can stay safe. Which moment do you think changed the prince the most?"},
 {"id": "read", "find": "Look Back", "fold": [], "todo": "Read the two questions. Then look back through Ch. 16–20 in your book.",
  "script": "There are no new chapters today. Instead, look back through Chapters 16 to 20 in your book. First, read the two Pause and Think questions below. One asks how the king sees Jemmy now. The other is about the ballad sellers at the very end. Flip back to find clues. Then do the Read Like a Writer box."},
 {"id": "chq", "find": "Chapter Thinking", "fold": [], "todo": CHQ_TODO,
  "script": "Now look back and answer in full sentences, with details from the book. One, what was the prince's real plan when he said to turn Jemmy in? Two, what deal does the king make, and is it fair? Three, what is the theme? Say it in one sentence, and use one event to show it. For a challenge, pick Scholar, and add one more detail."},
 dict(WRITE, todo="Write a conclusion for your comparison, then one sentence that says what the story teaches.",
  script="Today you finish. A strong conclusion names both boys one last time, says what they both learned, and ends with a sentence your reader will remember. Clara's ends with: they left as something neither of them expected. Write your conclusion. Then add one sentence that says what the story teaches."),
], "cards": {},
 "virtue": [
  {"t": "When the outlaws ask where the whipping boy went, the prince says, “Swam the river.”", "ok": True, "why": "He keeps Jemmy’s secret, even with the outlaws right there."},
  {"t": "Hold-Your-Nose Billy and Cutwater sneak onto a ship to get away.", "ok": False, "why": "They run away instead of facing what they did."},
  {"t": "In the dark sewer, Jemmy tells the scared prince, “Hang on to me,” and leads the way.", "ok": True, "why": "He keeps going in the dark and helps someone who is afraid."}]},
}

HOW = {'morph2': 'Read the Remember box. Then tap a word, and tap what it means. Match all four words.',
       'morph3': 'Say each pair of parts out loud. Type the whole word in the box. Then tap Check My Answers.',
       'vocabcloze': 'Read how we figured out the first word. Then fill in each sentence with a word from the word bank, and tap Check My Work. Last, play the matching game.'}
SPLICE = {}
for d, cfg in L.items():
    for m in cfg['mods']:
        t = m.get('script', '')
        if '+how:' in t:
            new, slug = t.split(' +how:')
            SPLICE[(d, m['id'])] = 'g3ela-how-' + slug
            m['script'] = new + ' ' + HOW[slug]
VIDEO = {1: ['morph', 'vocab', 'gram', 'spell'], 2: ['morph', 'vocab', 'spell2', 'spell', 'rwm'],
         3: ['morph', 'vocab', 'gram', 'spell'], 4: ['morph', 'vocab', 'gram', 'spell']}
for d, ids in VIDEO.items():
    for m in L[d]['mods']:
        if m['id'] in ids: m['video'] = 'g3ela-21-%d-teach-%s' % (d, m['id'])

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
                out['g3ela-21-%d-teach-%s' % (d, m['id'])] = t
        for w, t in cfg['cards'].items(): out['g3ela-21-%d-say-%s' % (d, w)] = t
    return out

if __name__ == '__main__':
    import sys
    for d, cfg in L.items():
        p = 'data/lesson-21-%d.json' % d
        j = json.load(io.open(p, encoding='utf-8'))
        if 'plate' in j: j['plate']['lookBtn'] = cfg['lookBtn']
        j['teach'] = {"dropTurnNotes": True, "mods": cfg['mods'], "cards": cfg['cards']}
        j['virtue'] = {"name": "courage", "title": VTITLE, "items": cfg['virtue']}
        io.open(p, 'w', encoding='utf-8').write(json.dumps(j, ensure_ascii=False, indent=1))
        write_page('lesson-21-%d-wb.html' % d, j)
    rec = recorded(); tot = 0
    for k, t in rec.items():
        n = len(t); tot += n; print('%-32s %4d' % (k, n))
    print('recorded this week: %d / 6260 credits (%.0f%%)' % (tot, 100.0 * tot / 6260))
    io.open('/tmp/wk21_rec.json', 'w', encoding='utf-8').write(json.dumps(rec, ensure_ascii=False, indent=1))
