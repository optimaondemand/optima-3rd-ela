#!/usr/bin/env python3
"""Week 28 (LWW Ch. 10-12): the Nov 10 2026 pilot fixes, as on weeks 18-27, for the Narnia page template.
Writes DATA.teach, plate.lookBtn and DATA.virtue (Truth Watch: honesty, the Narnia unit's trait; 3 moments a day from
that day's chapter, Day 4 from the whole week, checked against Planning docs/lww_text.txt) into data/lesson-28-N.json
AND the page's oao-data block. Word Study scripts are written for the Opti films: Day 1 teaches each idea; Days 2-4 show
that day's activity with an example that is not an answer anywhere in the week (constellation, companion, contact,
community; uncombed, repulsive, my grandpa's nap, solemn Peter; can't / dog's, Mrs. Beaver's machine, the dwarf's whip,
Mr. Beaver's tail; swimming / baking / tried, fatter, hiking, fried), and no two films open the same way.
NO RECORDINGS (Bethany, Nov 14 2026): films are built silent with captions; scripts stay written to the budget.

    python tools/g3sparkle/teach_wk28.py
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
1: {"lookBtn": "Tap to learn about this old drawing of Santa Claus", "mods": [
 dict(WGRD, script="[warmly] Here's this week's reading tip. Some things in a story stand for a bigger idea. Watch for things that keep coming back, like the snow, or Aslan's name. " + LENS_END),
 dol("Lucy's coat wasn't warm enough, but she didn't complain about the cold. Lucy's shows belonging. Wasn't and didn't each join two words."),
 {"id": "morph", "find": "Morphology", "fold": [], "todo": "Think about the question. Tap See what was hiding. Type each whole word.",
  "script": "[curious] Look up at the night sky! Constellation. A constellation is a group of stars together in the sky. The front part, con, means with or together. Its twin, com, means the same thing. Read the four words, and tap See what was hiding. Then type each whole word."},
 {"id": "vocab", "find": "Vocabulary", "fold": VOCAB_FOLD, "todo": "Fill in each sentence from the word bank. Tap Check My Work. Then play the matching game.",
  "script": "Be a word detective with me. Uncombed. Here's the sentence. The children came out of the cave unbrushed and uncombed. One, read the sentence: they just woke up. Two, look for word parts: un, comb, e d. Three, check it. Uncombed means not combed. +how:vocabcloze"},
 {"id": "gram", "find": "Grammar", "fold": GRAM_FOLD, "todo": "Tap Now check your thinking. Then tap the five words that need an apostrophe.",
  "script": "[warmly] An apostrophe has two jobs. Job one: it joins two words. Can, plus not, makes can't. The apostrophe sits where the letters left. Job two: it shows belonging. The dog's bone is the bone that belongs to the dog. Tap Now check your thinking. Then find the five words that need an apostrophe."},
 {"id": "spell", "find": "Spelling", "fold": [], "todo": "Think about the questions. Tap Now name the pattern. Then sort all eight words.",
  "script": "Three spelling changes, coming up! Swim, swimming: the m doubles. Bake, baking: the e drops off. Try, tried: the y turns into i. Think about the questions, and tap Now name the pattern. Then sort the words."},
 {"id": "copia", "sel": ".spk-copia-card", "label": "Opti shows you how", "fold": [], "todo": "Write the sentence three new ways, one box at a time.",
  "script": "[warmly] Here's copia: one idea, said many ways. Let me try a different sentence first. Peter smiled. Box one, change the opener: In the cold morning, Peter smiled. Box two, a stronger verb: Peter beamed. Box three, add a detail: Peter smiled at his shining new shield. Now it's your turn, one box at a time. If you get stuck, tap Show one way."},
 dict(READ, todo="Read Chapter 10 in your book. Then try the Truth Watch below.",
  script="Read Chapter 10 in your book, with your lens in mind. Listen for the jingling bells, and watch who arrives. Then try the Truth Watch and the three questions."),
 dict(CHQ, script="Three questions, in full sentences, with details from the book. One, what Father Christmas's arrival stands for. Two, why each child gets a different kind of gift. Three, what Aslan seems to stand for so far."),
 dict(WRITE, todo="Write two or three sentences about one symbol from Chapter 10.",
  script="Today you write a symbol paragraph. Clara's first try just said Father Christmas came. Her new paragraph names the symbol, says what it stands for, and why it matters. Write yours the same way."),
], "cards": {},
 "virtue": [
  {"t": "Mrs. Beaver tells the children plainly that they cannot reach the Stone Table before the Witch, but they still have a hope.", "ok": True, "why": "She tells the hard truth, and the hopeful part too."},
  {"t": "Father Christmas tells Peter that his presents are tools, not toys.", "ok": True, "why": "He is honest about what the sword and shield are for."},
  {"t": "Lucy says she is not sure, but she thinks she could be brave enough.", "ok": True, "why": "She says how she really feels, even the part she is not sure about."}]},
2: {"lookBtn": "Tap to learn about this painting of melting snow", "mods": [
 dict(WGRD, script="[warmly] Here's today's reading tip. Snow has been in every chapter so far. Watch what happens to it in Chapter 11, and what that might mean. " + LENS_END),
 dol("The Witch's wand turned the feasting creatures to stone, and the dwarf's whip couldn't make the reindeer go any faster. Witch's and dwarf's show belonging. Couldn't joins two words."),
 {"id": "poem", "find": "Poetry", "fold": [":scope > .callout"], "todo": "Read the limerick out loud. Check it against A, A, B, B, A.",
  "script": "[curious] Here's a limerick by Edward Lear, the man who made them famous. Read it out loud, and listen to the last word of each line. Does it follow the pattern A, A, B, B, A? Answer out loud."},
 {"id": "morph", "find": "Morphology", "fold": [":scope > .callout:not(:has(+ .match-game))", ":scope > .key-concept"], "todo": "Tap a word, then tap what it means. Match all four words.",
  "script": "Watch one match first. Companion. Find the front part: com. It means with. A companion is a friend who goes along with you. That's my match! +how:morph2"},
 {"id": "vocab", "find": "Vocabulary", "fold": [], "todo": "Tap a word, then tap its meaning. Match all four words.",
  "script": "Ever seen a grin that made you want to look away? Repulsive. The dwarf grins at Edmund in a repulsive way. Repulsive means so nasty you want to turn away. Now tap a word, then tap its meaning. Match all four."},
 {"id": "gram", "find": "Grammar", "fold": GRAM_FOLD, "todo": "Find what each apostrophe does. Tap Now check your thinking. Then tap every word that is wrong.",
  "script": "Spot the apostrophe. Mrs. Beaver's sewing machine was too heavy to bring. Beaver's, with an apostrophe s, shows belonging. Find the apostrophes in each of the four sentences, and tap Now check your thinking. Then fix the paragraph."},
 {"id": "spell", "find": "Spelling", "fold": [], "foldText": ["The Rule:"], "todo": "Read the rule. In each row, tap the word that matches.",
  "script": "Detective question! Which of these doubled its last letter: fatter, or faster? Fatter! Fat has a short vowel and one t, so the t doubles. Read the rule. Then in each row, tap the one word that matches what the row asks for."},
 dict(READ, todo="Read Chapter 11 in your book. Then try the Truth Watch below.",
  script="Read Chapter 11 in your book, with your lens in mind. Then try the Truth Watch, and watch my video in the Read Like a Writer box before you write."),
 {"id": "rwm", "sel": ".rwm-box", "after": ":scope > .rwm-header", "label": "Opti shows you how", "fold": [],
  "script": "Let's try all three parts with a sentence from Chapter 11. The snow was again falling as they came into the courtyard, but she took no notice of that and made Edmund sit beside her on the sledge. Part one, read like a reader. The Witch doesn't care about the snow. Part two, read like a writer. Weather first, then but turns to the story. Part three, mimic. Here's mine: The rain was pouring as we left school, but Mom took no notice and made us run to the car. Now it's your turn with the sentence about the snow and the moon. Write one sentence in each box."},
 dict(CHQ, script="Three questions, in full sentences. One, how the Witch acts when the snow melts. Two, one thing that keeps coming back, and what it stands for. Three, how Edmund has changed by the end of Chapter 11."),
 dict(WRITE, todo="Make one vague phrase in your symbol paragraph more precise.",
  script="Today you make it precise. Clara swapped things are getting better for hope overcoming despair. Find one vague phrase in yours, and make it sharper."),
], "cards": {},
 "virtue": [
  {"t": "The Witch gives Edmund dry bread instead of the Turkish Delight she promised him.", "ok": False, "why": "She does not keep her promise."},
  {"t": "A little squirrel says Father Christmas really did come, even when the Witch says to call it a lie.", "ok": True, "why": "He tells the truth, even though the Witch is angry."},
  {"t": "Edmund starts to see that the things he told himself about the Witch being good sound silly now.", "ok": True, "why": "He is finally being honest with himself."}]},
3: {"lookBtn": "Tap to learn about this painting of a knight", "mods": [
 dict(WGRD, script="[warmly] Here's today's reading tip. Father Christmas gave Peter a sword. In Chapter 12, watch when Peter uses it, and what that shows about him. " + LENS_END),
 dol("Susan's horn rang out, and Peter ran to help, but Aslan's order meant the others didn't join the fight. Susan's and Aslan's show belonging. Didn't joins two words."),
 {"id": "morph", "find": "Morphology", "fold": [":scope > .callout:not(:has(+ .fillin-game))", ":scope > .key-concept"], "todo": "Say the parts out loud. Type the whole word in each box. Tap Check My Answers.",
  "script": "Snap the parts together. Con. Tact. Contact! When two things are in contact, they touch together. +how:morph3"},
 {"id": "vocab", "find": "Vocabulary", "fold": [], "todo": "Read each sentence. Pick the word that fits.",
  "script": "Try each word in the blank, and keep the one that makes sense. Here's my sentence. After a long nap, my grandpa felt blank. Herald? Hmm, no. Renewed? Yes! Now pick the word that fits each sentence."},
 {"id": "gram", "find": "Grammar", "fold": GRAM_FOLD, "todo": "Read the before and after. Put the apostrophes in the gray sentence.",
  "script": "Let's be the editor. The dwarfs whip wasnt kind to the reindeer. Dwarf's needs an apostrophe: the whip belongs to the dwarf. Wasn't needs one too: was, plus not. Read the before and after, and tap Check yourself. Then fix the sentence in the gray box."},
 {"id": "spell", "find": "Spelling", "fold": [], "foldText": ["The Rule:"], "todo": "Read the rule. Tap each card to build the new word.",
  "script": "Let's build one. Hike, plus i n g. Hike ends in a silent e, so the e drops off. Hiking! Read the rule. Decide which change each word needs. Then tap the card to build the new word."},
 dict(READ, todo="Read Chapter 12 in your book. Then try the Truth Watch below.",
  script="Read Chapter 12 in your book, with your lens in mind. Part of it is a scary fight with a wolf. Peter is brave, and he is not hurt. Then try the Truth Watch and the three questions."),
 dict(CHQ, script="Three questions, in full sentences. One, what Peter does in his first battle. Two, what Aslan does next, and what it might mean. Three, how this connects to the four thrones."),
 dict(WRITE, todo="Add your symbol paragraph to your response, with a joining phrase.",
  script="Today you put it together. Clara used a joining phrase, in addition to, to add her symbol paragraph to her response. Add yours the same way."),
], "cards": {},
 "virtue": [
  {"t": "Peter tells Aslan that Edmund going wrong was partly his own fault, because he was angry with him.", "ok": True, "why": "He owns up to his part, even in front of Aslan."},
  {"t": "Mr. Beaver tells Aslan plainly that Edmund has joined the White Witch.", "ok": True, "why": "He tells the truth, even though it is sad news."},
  {"t": "Aslan tells Lucy that saving Edmund may be harder than she thinks.", "ok": True, "why": "He does not pretend it will be easy."}]},
4: {"lookBtn": "Tap to learn about this painting of blossoms", "mods": [
 dict(WGRD, script="[warmly] Here's today's reading tip. Look back at the things Lewis kept bringing back this week. Pick the one you think matters most. " + LENS_END),
 dol("It's Susan's horn, and Peter doesn't stop to think. It's means it is. Susan's shows belonging."),
 {"id": "poem", "find": "Poetry", "fold": [":scope > .callout"], "todo": "Make up your own limerick. Say it out loud.",
  "script": "Your turn to be the poet. Start with: There once was a. Lines one, two and five rhyme. Lines three and four are short, and they rhyme with each other. Say your limerick out loud."},
 {"id": "morph", "find": "Morphology", "fold": [":scope > .key-concept"], "foldText": ["Before you roll"], "todo": "Tap Roll the Dice. Say what the word means. Tap Check My Thinking. Roll all six words.",
  "script": "Quick question: what do com and con mean? With, or together! Here's a word that's not on the dice. Community. A community is people who live together. Now tap Roll the Dice. Say what each word means, and tap Check My Thinking. Roll all six."},
 {"id": "vocab", "find": "Vocabulary", "fold": [], "todo": "Choose one word. Write one sentence about Chapters 10 to 12.",
  "script": "Here's how I'd use a word about the story. Solemn. Peter was silent and solemn when Father Christmas handed him a sword. One word, one moment. Now choose one of your words and write your own sentence about Chapters 10 to 12."},
 {"id": "gram", "find": "Grammar", "fold": GRAM_FOLD, "todo": "Tap Check yourself. Tap every word that needs fixing. Then tap See the answers.",
  "script": "Two passes, like an editor. mr beavers tail was the last thing lucy saw. Pass one, capitals: Mr., Beaver and Lucy. Pass two, apostrophes: Beaver's tail. Now do your passes, and tap every word that needs fixing."},
 {"id": "spell", "find": "Spelling", "fold": [], "foldText": ["The Rule:"], "todo": "Tap Roll the dice. Decide which change the word needs. Tap Check my answer.",
  "script": "Here's my roll. Fry, plus e d. Fry ends in y after a consonant, so the y turns into i. Fried! Tap Roll the dice, decide which change the word needs, or none, and tap Check my answer."},
 dict(READ, todo="Look back at Chapters 10 to 12. Then try the Truth Watch below.",
  script="No new chapters today. Look back at Chapters 10 to 12, and find the thing Lewis keeps bringing back. Then try the Truth Watch and the three questions."),
 dict(CHQ, script="Three questions to finish the week, in full sentences. One, your symbol and what it stands for. Two, why showing the thaw is stronger than just saying it. Three, a detail Lewis keeps bringing back, and why."),
 dict(WRITE, todo="Polish your response. Add a closing sentence about what the symbols do.",
  script="Last step: polish. Clara ended with what the symbols do for the reader. Read your whole response, and add your own closing sentence."),
], "cards": {},
 "virtue": [
  {"t": "The dwarf tells the Witch the truth: this is no thaw, this is Spring, and it is Aslan's doing.", "ok": True, "why": "He tells her the truth, even though she will not like it."},
  {"t": "The Witch tells the Fox he will be forgiven if he says he has been lying.", "ok": False, "why": "She wants him to call the truth a lie."},
  {"t": "Aslan tells Peter he has forgotten to clean his sword, and Peter blushes because it is true.", "ok": True, "why": "Peter does not make excuses. He fixes it."}]},
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
        if m['id'] in ids: m['video'] = 'g3ela-28-%d-teach-%s' % (d, m['id'])

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
                out['g3ela-28-%d-teach-%s' % (d, m['id'])] = t
        for w, t in cfg['cards'].items(): out['g3ela-28-%d-say-%s' % (d, w)] = t
    return out

if __name__ == '__main__':
    import sys
    for d, cfg in L.items():
        p = 'data/lesson-28-%d.json' % d
        j = json.load(io.open(p, encoding='utf-8'))
        if 'plate' in j: j['plate']['lookBtn'] = cfg['lookBtn']
        j['teach'] = {"dropTurnNotes": True, "mods": cfg['mods'], "cards": cfg['cards']}
        j['virtue'] = {"name": "honesty", "title": VTITLE, "items": cfg['virtue']}
        io.open(p, 'w', encoding='utf-8').write(json.dumps(j, ensure_ascii=False, indent=1))
        write_page('lesson-28-%d-lww.html' % d, j)
    rec = recorded(); tot = 0
    for k, t in rec.items():
        n = len(t); tot += n; print('%-32s %4d' % (k, n))
    print('recorded this week: %d / 6260 credits (%.0f%%)' % (tot, 100.0 * tot / 6260))
    io.open('/tmp/wk28_rec.json', 'w', encoding='utf-8').write(json.dumps(rec, ensure_ascii=False, indent=1))
