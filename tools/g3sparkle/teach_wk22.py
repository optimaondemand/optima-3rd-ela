#!/usr/bin/env python3
"""Week 22 (The Whipping Boy wrap-up, no new chapters): the Nov 10 2026 pilot fixes, as on weeks 18-21.
Writes DATA.teach, plate.lookBtn and DATA.virtue (Courage Watch, 3 moments a day from the whole book,
none repeated from weeks 18-21) into data/lesson-22-N.json AND the page's oao-data block.
Word Study scripts are written for the Opti films from the start: Day 1 teaches each idea; Days 2-4
show that day's activity with an example that is not an answer anywhere in the week, and no two
films open the same way. Book quotes checked against Planning docs/whipping_boy_ocr.txt.

    python tools/g3sparkle/teach_wk22.py
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

LB = "Then tap one of the two lenses below to use while you look back. You don't need to write anything."
READ_TODO = "Read the two questions. Then look back through the whole book."
L = {
1: {"lookBtn": "Tap to learn about this painting of a young prince", "mods": [
 dict(WGRD, script="[warmly] Here's today's reading tip. At the start of the book, Jemmy and the prince could hardly stand each other. By the end, they're friends. Good readers look back and ask: who changed, and what changed them? " + LB),
 {"id": "dol", "find": "Daily Oral", "fold": [], "todo": DOL_TODO,
  "script": "Let's fix a sentence. The correct one is from Chapter 20. Dismissed, both of you, said the king. The king's words go inside quotation marks, and the comma goes inside too. Then comes who said it. Tap the yellow parts. Then pick Sentence A or Sentence B, and type it the right way."},
 {"id": "morph", "find": "Morphology", "fold": [":scope > .callout:not(:has(+ .fillin-game)):not(:has(+ .dol-check-btn))"],
  "todo": "Think about the questions. Tap See what was hiding. Type the missing word part in each box.",
  "script": "[curious] What do a castle, a tower, and a bridge have in common? Somebody built them. Long ago, the Romans had a word for build, and we still use a piece of it. Struct. S, t, r, u, c, t. When you spot those six letters inside a long word, think: build. Read the three words, and think about the questions. Then tap See what was hiding, and type the missing parts."},
 {"id": "vocab", "find": "Vocabulary", "fold": VOCAB_FOLD, "todo": VOCAB_FLIP_TODO,
  "script": "Let's be word detectives with a word that's not on your cards. Unlikely. Un means not, and likely means it will probably happen. So unlikely means not likely at all. Jemmy and the prince were an unlikely pair of friends! Listen to each card, guess the meaning, and flip it. Then play the matching game."},
 {"id": "gram", "find": "Grammar", "fold": GRAM_FOLD, "todo": "Tap Now check your thinking. Then sort each pronoun by its job.",
  "script": "[warmly] Pronouns are little words that stand in for names, and each one has a job. Listen. We ran. Betsy helped us. It was our coach. We does the action. Us gets the action. Our shows whose coach. Here's a trick for pairs. Betsy and us laughed? Cover Betsy. Us laughed? No! We laughed. Tap Now check your thinking. Then sort each pronoun by its job."},
 {"id": "spell", "find": "Spelling", "fold": [], "todo": "Say the words. Tap Now name the pattern. Then sort all eight words.",
  "script": "Watch me take one apart. Cupcake. Cup, plus cake. Two real words, joined into one. That's a compound word. Now be careful. Beautiful is a long word, but can you split it into two real words? No. Long doesn't mean compound. Say the words out loud, and tap Now name the pattern. Then sort all eight."},
 {"id": "copia", "sel": ".spk-copia-card", "label": "Opti shows you how", "fold": [], "todo": "Write the sentence three new ways, one box at a time.",
  "script": "[warmly] Here's copia again: one idea, said many ways. I'll try a different sentence first. The king smiled. Box one, change the opener: At the golden doors, the king smiled. Box two, a stronger verb: The king beamed. Box three, add a detail: The tired old king smiled. Now it's your turn, one box at a time. If you get stuck, tap Show one way."},
 {"id": "spotlight", "find": "Character Spotlight", "fold": [":scope > .socratic-box"],
  "script": "Here's something to think about. In Chapter 1, Jemmy takes the whacks for the prince's tricks. In Chapter 20, the prince tells his father that it's thanks to Jemmy he got home safe. That's a big change. What happened in between?"},
 {"id": "read", "find": "Looking Back", "fold": [], "todo": READ_TODO,
  "script": "There are no new chapters today. Read the two Pause and Think questions first. Then flip back to Chapter 1, and then to Chapter 20. How did Jemmy talk about the prince at the start? How does he feel about him at the end? Think about your answers. You don't write them here."},
 {"id": "chq", "find": "Chapter Thinking", "fold": [], "todo": CHQ_TODO,
  "script": "Now answer in full sentences, with details from the book. One, how did Jemmy change? Use one detail from early and one from late. Two, how did the prince change? Three, how are the two boys alike? For a challenge, pick Scholar, and add one more detail to each answer."},
 dict(WRITE, todo="Find one vague sentence in your comparison paragraph. Write it again with a chapter number.",
  script="A vague sentence is fuzzy. Prince Brat changed a lot. Changed how? When? Clara made hers specific: she named Chapter 20, and said what the prince did there. Find one fuzzy sentence in your comparison paragraph. Write it again with a chapter number."),
], "cards": {
 "transform": "Transform. Both boys transform by the end of the story. Transform means to change completely.",
 "compare": "Compare. When you compare two boys, you look at them side by side, for what is the same and what is different.",
 "contrast": "Contrast. When you contrast two things, you point out only how they are different.",
 "develop": "Develop. A character can develop over a whole book. Develop means to grow and change over time."},
 "virtue": [
  {"t": "In Chapter 17, the prince gets up off the mud flat after his whipping. Jemmy sees “a cast-iron streak of pluck” in him.", "ok": True, "why": "He was hurt, and he got back up."},
  {"t": "In Chapter 14, the prince says he may never go back to the castle. “This is the best time I ever had!”", "ok": False, "why": "He is having fun, but he is staying away from his father instead of facing him."},
  {"t": "In Chapter 20, Jemmy stands alone in front of the king, who says, “You ought to be whipped.”", "ok": True, "why": "He is afraid, but he stays and answers, “Yes, My Lord.”"}]},
2: {"lookBtn": "Tap to learn about this painting of two street boys", "mods": [
 dict(WGRD, script="[warmly] Here's today's reading tip. A story is more than what happens. It also teaches a lesson, and that lesson is the theme. Today, say it in your own words, so it would fit anybody, not just Jemmy. " + LB),
 {"id": "dol", "find": "Daily Oral", "fold": [], "todo": DOL_TODO,
  "script": "Let's fix a sentence. The correct one is from Chapter 17. Jemmy couldn't sort out his feelings. Couldn't is could not, squeezed together, and the apostrophe stands in for the missing o. Tap the yellow parts. Then pick Sentence A or Sentence B, and type it the right way."},
 {"id": "poem", "find": "Poetry", "fold": [":scope > .callout", ":scope > .socratic-box"], "todo": "Read the poem out loud. Then find two creatures that act like people.",
  "script": "Here's a short poem by Christina Rossetti. Read it out loud. Now look closer. Can a cricket really be cheerful? Can a gnat really dance? The poet gives little creatures feelings and actions that people have. That's personification. Find two creatures in the poem that act like people."},
 {"id": "morph", "find": "Morphology", "fold": [":scope > .callout:not(:has(+ .match-game))", ":scope > .key-concept"], "todo": "Tap a word, then tap what it means. Match all four words.",
  "script": "Remember, struct means build. Here's a word that's not on your list. Restructure. Cover the re at the front, and the u, r, e at the end. Struct is in the middle. Build! Re means again. So restructure means build again in a new way. +how:morph2"},
 {"id": "vocab", "find": "Vocabulary", "fold": VOCAB_FOLD, "todo": VOCAB_FLIP_TODO,
  "script": "Here's a puzzle. What happens in a story, and what a story means, are two different things. Today's four words help you talk about what it means. Listen to each card, guess the meaning, and flip it. Then match all four."},
 {"id": "gram", "find": "Grammar", "fold": GRAM_FOLD, "todo": "Read the Remember box. Then tap every pronoun in each sentence.",
  "script": "Spot the pronouns with me. She gave us her map. She is doing the giving. Us gets the map. Her shows whose map it is. Three pronouns, three jobs, in one sentence. Read the Remember box. Then tap every pronoun in each sentence. Each one has three."},
 {"id": "spell", "find": "Spelling", "fold": [], "foldText": ["The Rule:"], "todo": "Read the rule. In each row, tap the one compound word.",
  "script": "Use your ears for this one. Kitten. Window. Doghouse. Paper. Which one is two small words? Dog, plus house. Doghouse! Say each word in the row out loud. Listen for two small words hiding inside. Then tap the compound word."},
 {"id": "spotlight", "find": "Character Spotlight", "fold": [":scope > .socratic-box"],
  "script": "Think about this. In the dark sewer, the prince tells Jemmy, I wish I were like you. He thinks Jemmy is never afraid. But Jemmy says he is! What does that tell you about being brave?"},
 {"id": "read", "find": "Looking Back", "fold": [], "todo": READ_TODO,
  "script": "There are no new chapters today. Read the two Pause and Think questions first. Then look back for two moments that show the same lesson, one early in the book and one late. After that, watch my video in the Read Like a Writer box before you try it."},
 {"id": "rwm", "sel": ".rwm-box", "after": ":scope > .rwm-header", "label": "Opti shows you how", "fold": [],
  "script": "[warmly] Let's try all three parts with a different sentence, from Chapter 19. Careful, he thought. Part one, read like a reader. Jemmy is in the dark sewer, choosing which tunnel to take. Part two, read like a writer. There are no quotation marks. We hear Jemmy's own word, careful, right inside his head. Part three, mimic. Here's mine: Hush, Opti thought, the story is just getting good. Now it's your turn with Jemmy's sentence. Write one sentence in each box."},
 {"id": "chq", "find": "Chapter Thinking", "fold": [], "todo": CHQ_TODO,
  "script": "Now answer in full sentences. One, say the theme in one sentence. It's a life lesson, not what happened. Two, find one moment from Chapters 1 to 10 that shows it. Three, find one from Chapters 11 to 20. For a challenge, pick Scholar, and add one more detail to each answer."},
 dict(WRITE, todo="Write your conclusion again. Add a sentence that says what the story teaches.",
  script="A conclusion can do more than end. It can say what the story teaches. Clara's first try was: both boys learned to trust each other. Then she added the lesson the whole book shows. Write your conclusion again, and add a sentence that says what The Whipping Boy teaches."),
], "cards": {
 "theme": "Theme. The theme is the big message or lesson of a story.",
 "evidence": "Evidence. Evidence is a detail from the book that proves your idea is true.",
 "resolution": "Resolution. The resolution is how the problem is settled at the end of a story.",
 "character development": "Character development. That's how a character grows and changes across a story."},
 "virtue": [
  {"t": "In Chapter 19, the prince’s voice is stiff with fear, but he tells Jemmy, “I won’t go back to the castle unless you go with me.”", "ok": True, "why": "He is scared, and he still sticks by his friend."},
  {"t": "In Chapter 11, the prince says, “It doesn’t please me to take orders from common rascals.”", "ok": False, "why": "He is being proud and rude, not brave."},
  {"t": "In Chapter 17, a big bear sniffs at the prince. He doesn’t move a muscle, and he whispers, “Rein in your beast.”", "ok": True, "why": "A bear is right next to him, and he stays calm."}]},
3: {"lookBtn": "Tap to learn about this picture of people watching a play", "mods": [
 dict(WGRD, script="[warmly] Here's today's reading tip. Every character in this book sounds different. The prince sounds bossy, Betsy sounds bold, and Jemmy talks like the streets. Today you read a scene out loud, so listen for each voice. " + LB),
 {"id": "dol", "find": "Daily Oral", "fold": [], "todo": DOL_TODO,
  "script": "Let's fix a sentence. The correct one is from Chapter 17. Steady on your legs? Jemmy asked. It's a question, so the question mark goes inside the quotation marks. And asked starts with a small letter, because the sentence keeps going. Tap the yellow parts. Then pick Sentence A or Sentence B, and type it the right way."},
 {"id": "morph", "find": "Morphology", "fold": [":scope > .callout:not(:has(+ .fillin-game))", ":scope > .key-concept"], "todo": "Say the parts out loud. Type the whole word in each box. Tap Check My Answers.",
  "script": "Look what one little ending can do. Act, plus i o n. Action! The ending i o n turns a doing word into a thing. Today you'll stick it on struct words, and you'll add some front parts too. Say the parts out loud, push them together, and type the whole word. Then tap Check My Answers."},
 {"id": "vocab", "find": "Vocabulary", "fold": VOCAB_FOLD, "todo": VOCAB_CLOZE_TODO,
  "script": "Here's a reading-aloud word that's not in your bank. Pause. When you pause, you stop for just a moment, like at a comma. Reader's Theater is full of pauses! +how:vocabcloze"},
 {"id": "gram", "find": "Grammar", "fold": GRAM_FOLD, "todo": "Read the Remember box. Type a pronoun from the word bank in each blank.",
  "script": "Listen to this. Betsy fed Betsy's bear, and Betsy's bear licked Betsy. Clunky! Let's fix it. Betsy fed her bear, and the bear licked her. Much better. Read the Remember box. Then type a pronoun from the word bank in each blank, so no name is said twice."},
 {"id": "spell", "find": "Spelling", "fold": [], "foldText": ["The Rule:"], "todo": "Tap each card to join the two small words. Then answer the question in the box.",
  "script": "Oops. I wrote foot, then a space, then ball. But a football is one thing, so it's one word. Foot and ball join right up, with no space. Tap each card to join the two small words. Say the new word out loud. Then answer the question in the box."},
 {"id": "spotlight", "find": "Character Spotlight", "fold": [":scope > .socratic-box"],
  "script": "Try reading this out loud. Which way is south? Straight on! You certain? Certain I'm certain. Jemmy sounds lost. Betsy sounds sure of herself. Can you hear the difference in your own voice?"},
 {"id": "read", "find": "Looking Back", "fold": [], "todo": READ_TODO,
  "script": "There are no new chapters today. Read the two Pause and Think questions first. Then flip through the book and find the scene you'd most like to read out loud. Read it in your head first. How should each character sound? Then do the Read Like a Writer box."},
 {"id": "chq", "find": "Chapter Thinking", "fold": [], "todo": CHQ_TODO,
  "script": "Now answer in full sentences. One, which scene did you pick, and which chapter is it in? Two, read it out loud two times, and tell how your reading changed. Three, how should each character sound? For a challenge, pick Scholar, and add one more detail to each answer."},
 dict(WRITE, todo="Find one pronoun in your comparison paragraph. Check it, and write the sentence the right way.",
  script="Today you check your pronouns. Clara found this: Both him and Jemmy changed. Cover Jemmy. Him changed? No. He changed. So she fixed it. Find one pronoun in your comparison paragraph. Check it the same way, and write the sentence the right way."),
], "cards": {},
 "virtue": [
  {"t": "In Chapter 18, Smudge holds out his hand. The prince shakes it, even though no one is allowed to shake a prince’s hand.", "ok": True, "why": "He tries something new and treats Smudge like a friend."},
  {"t": "In Chapter 2, the prince tells the tutor, “I can always get someone to write my name for me.”", "ok": False, "why": "He won’t try something hard. He wants someone else to do it."},
  {"t": "In Chapter 17, Betsy runs up to the two outlaws and shouts, “Stop it!”", "ok": True, "why": "She stands up to two bullies to help a boy she doesn’t even know."}]},
4: {"lookBtn": "Tap to learn about this old picture of a print shop", "mods": [
 dict(WGRD, script="[warmly] Here's today's reading tip. A good book stays with you after you close it. Today, think about the whole road, from the first page to the last. What moment would you tell a friend about? " + LB),
 {"id": "dol", "find": "Daily Oral", "fold": [], "todo": DOL_TODO,
  "script": "Let's fix a sentence. The correct one is from Chapter 20. The king broke into a smile you could warm your hands over. Capital letter at the start, period at the end. What a picture that sentence makes! Tap the yellow parts. Then pick Sentence A or Sentence B, and type it the right way."},
 {"id": "poem", "find": "Poetry", "fold": [":scope > .callout", ":scope > .socratic-box"], "todo": "Read the poem out loud again. Then answer the question in the box.",
  "script": "Here's the Rossetti poem again. This time, think about why she wrote it this way. She could have just said, don't step on bugs. Instead the cricket is cheerful, and the gnat dances. Which way makes you care more? Answer the question in the box."},
 {"id": "morph", "find": "Morphology", "fold": [":scope > .key-concept"], "foldText": ["Before you roll"], "todo": "Tap Roll the Dice. Say what the word means. Tap Check My Thinking. Roll all six words.",
  "script": "Riddle time. I'm six letters long. I hide inside big words. And I mean build. What am I? Struct! Roll a word, find struct inside it, and say what the whole word means, out loud. Then tap Check My Thinking. Roll all six."},
 {"id": "vocab", "find": "Vocabulary", "fold": VOCAB_FOLD, "todo": VOCAB_CLOZE_TODO,
  "script": "One more word before we say goodbye to this book. Farewell. Fare, plus well. It means goodbye, and good luck! Read each sentence with a bank word in the blank. If it sounds right and makes sense, keep it. Then play the matching game."},
 {"id": "gram", "find": "Grammar", "fold": GRAM_FOLD, "todo": "Tap the wrong word, or tap No mistake. Then tap See the answers and answer the question in the box.",
  "script": "Spot the mistake with me. The boy lost him hat. Him hat? The hat belongs to the boy, so it's his hat. A pronoun in the wrong job sounds funny when you say it out loud. Read each sentence out loud. Tap the wrong word, or tap No mistake."},
 {"id": "spell", "find": "Spelling", "fold": [], "foldText": ["The Rule:", "Before you roll"], "todo": "Tap Roll the dice. Say the two small words. Tap Check my answer. Roll all six.",
  "script": "Roll one with me. Toothbrush! Say it slowly. Tooth. Brush. Two small words make one big word. Now roll all six. Say each word out loud, then say the two small words that make it."},
 {"id": "spotlight", "find": "Character Spotlight", "fold": [":scope > .socratic-box"],
  "script": "Here's the very last thing the king says. If you boys decide to run away again, take me with you. At the start of the book, would you ever have pictured the king saying that? What changed?"},
 {"id": "read", "find": "Looking Back", "fold": [], "todo": READ_TODO,
  "script": "There are no new chapters today. Read the two Pause and Think questions first. Then think back over the whole book. Which boy changed the most? And if you could tell the author one thing, what would it be? Then do the Read Like a Writer box."},
 {"id": "chq", "find": "Chapter Thinking", "fold": [], "todo": CHQ_TODO,
  "script": "Now look back at your own writing, and answer in full sentences. One, do you still believe the claim in your opinion paragraph? Two, copy your strongest sentence, and tell why it's strong. Three, what moment will you remember longest? For a challenge, pick Scholar, and add one more detail."},
 dict(WRITE, todo="Read your comparison paragraph out loud. Then write what you noticed.",
  script="Today you publish, which means you share your writing. Clara read her paragraph out loud at home, and her listener asked her a good question. Read your comparison paragraph out loud to someone, or to yourself. Then write what you noticed when you heard it."),
], "cards": {},
 "virtue": [
  {"t": "In Chapter 3, Jemmy asks, “Ain’t you afraid o’ the dark?” The prince answers, “Lies!”", "ok": False, "why": "He hides that he is scared instead of saying so."},
  {"t": "In Chapter 17, when Petunia roars, Hold-Your-Nose Billy charges off into the river.", "ok": False, "why": "He runs to save himself."},
  {"t": "In Chapter 20, Jemmy has a price on his head, but he tells Betsy, “Better do what he says,” and goes along with the prince’s plan.", "ok": True, "why": "He trusts his friend, even though it is a big risk."}]},
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
VIDEO = {1: ['morph', 'vocab', 'gram', 'spell'], 2: ['morph', 'vocab', 'gram', 'spell', 'rwm'],
         3: ['morph', 'vocab', 'gram', 'spell'], 4: ['morph', 'vocab', 'gram', 'spell']}
for d, ids in VIDEO.items():
    for m in L[d]['mods']:
        if m['id'] in ids: m['video'] = 'g3ela-22-%d-teach-%s' % (d, m['id'])

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
                out['g3ela-22-%d-teach-%s' % (d, m['id'])] = t
        for w, t in cfg['cards'].items(): out['g3ela-22-%d-say-%s' % (d, w)] = t
    return out

if __name__ == '__main__':
    import sys
    for d, cfg in L.items():
        p = 'data/lesson-22-%d.json' % d
        j = json.load(io.open(p, encoding='utf-8'))
        if 'plate' in j: j['plate']['lookBtn'] = cfg['lookBtn']
        j['teach'] = {"dropTurnNotes": True, "mods": cfg['mods'], "cards": cfg['cards']}
        j['virtue'] = {"name": "courage", "title": VTITLE, "items": cfg['virtue']}
        io.open(p, 'w', encoding='utf-8').write(json.dumps(j, ensure_ascii=False, indent=1))
        write_page('lesson-22-%d-wb.html' % d, j)
    rec = recorded(); tot = 0
    for k, t in rec.items():
        n = len(t); tot += n; print('%-32s %4d' % (k, n))
    print('recorded this week: %d / 6260 credits (%.0f%%)' % (tot, 100.0 * tot / 6260))
    io.open('/tmp/wk22_rec.json', 'w', encoding='utf-8').write(json.dumps(rec, ensure_ascii=False, indent=1))
