#!/usr/bin/env python3
"""Week 32 (Year-End Culmination: The 7 Pillars of Virtue; extension pages): the Nov 10 2026 pilot fixes, as on weeks 18-31.
Writes DATA.teach, plate.lookBtn and DATA.virtue (Pillar Watch, Bethany Nov 16 2026; every moment checked in the novel
texts in Planning docs) into data/lesson-32-N.json AND the page's oao-data block. Word Study scripts are written for the
Opti films: Day 1 teaches each idea; Days 2-4 show that day's activity with an example that is not an answer anywhere in
the week (kindness, joyous, generous, maya and leo, unhappy/thankful; joyous, fair, when the bell rang, raking; joyful,
courtesy, my dogs bowl, puddel; restart, respect, my sisters cat, hiking), and no two films open the same way.
Day 2 Read Like a Writer works a different real line ("Nothing." in The Tale of Despereaux), never Mrs. Lambchop's.
NO RECORDINGS (Bethany, Nov 14 2026): films are built silent with captions; scripts stay written to the budget.

    python tools/g3sparkle/teach_wk32.py [--count]
"""
import io, json, re

GRAM_FOLD = [":scope > .callout:not(:has(+ .spotter-game)):not(:has(+ .fillin-game)):not(:has(+ .sort-game)):not(:has(+ .dol-check-btn))"]
WGRD = {"id": "wgrd", "find": "What Good Readers", "fold": [":scope > p:not(.g3-do)", ":scope > .key-concept", ":scope > .socratic-box"],
        "todo": "Listen to Opti. Then tap the lens you will use today."}
VOCAB_FOLD = [":scope > .g3-model-h", ":scope > .decode-steps", ":scope > .key-concept"]
WRITE = {"id": "write", "find": "Writer.s Workshop", "fold": [":scope > .callout"], "foldText": ["watch how", "today.s tool"]}
DOL_TODO = "Tap the yellow parts. Then pick Sentence A or B and type it the right way."
VTITLE = "Pillar Watch: Does it show a pillar?"
LENS_END = "Then tap one of the two lenses below to use while you read. You don't need to write anything."
READ = {"id": "read", "find": "^\\W*(Read:|Look Back)", "fold": []}
def chq(todo, script): return {"id": "chq", "find": "Q1 —", "fold": [], "todo": todo, "script": script}
def dol(script): return {"id": "dol", "find": "Daily Oral", "fold": [], "todo": DOL_TODO, "script": "Let's fix a sentence. The correct one first. " + script + " Tap the yellow parts. Then pick Sentence A or Sentence B, and type it the right way."}
L = {
1: {"lookBtn": "Tap to learn about this painting of an old temple", "mods": [
 dict(WGRD, script="[warmly] Here's this week's reading tip. Look back at how your reading has grown. Think about all four books, and one skill that is easy for you now. " + LENS_END),
 dol("Kindness costs nothing, and it's the one thing everybody remembers. It's joins it and is. A comma goes before and, because and joins two complete thoughts."),
 {"id": "morph", "find": "Morphology", "fold": [], "todo": "Think about the questions. Tap See if you were right. Type the missing part in each box.",
  "script": "[curious] Every word part this year was a tool. Kindness. Kind, plus ness: being kind. Joyous. Joy, plus ous: full of joy. Find the base word first, then the part. Read the words and their parts, tap See if you were right, then type the missing part of each word."},
 {"id": "vocab", "find": "Vocabulary", "fold": VOCAB_FOLD, "todo": "Fill in each sentence from the word bank. Tap Check My Work. Then play the matching game.",
  "script": "Be a word detective with me. Generous. Here's my sentence. Maya gave half her lunch to a new friend; she was generous. One, read the sentence: she shared. Two, look for word parts: ous means full of. Three, check it. Generous means happy to give and share. Now fill in each sentence from the word bank, and play the matching game."},
 {"id": "gram", "find": "Grammar", "fold": GRAM_FOLD, "todo": "Tap Now check your thinking. Then tap all seven words that need fixing.",
  "script": "[warmly] One sentence, four fixes. maya and leo goed to the library on monday. Maya and Leo are names: capitals. Monday is a day: capital M. And goed should be went. Read The Rule box, and tap Now check your thinking. Then tap all seven words in the passage that need fixing."},
 {"id": "spell", "find": "Spelling", "fold": [], "todo": "Think about the questions. Tap Now name the pattern. Then sort all eight words.",
  "script": "Front or back? Unhappy: the part un is at the front, so it's a prefix. Thankful: the part ful is at the end, so it's a suffix. Think about the questions, and tap Now name the pattern. Then sort the words: prefix at the front, or suffix at the end."},
 {"id": "copia", "sel": ".spk-copia-card", "label": "Opti shows you how", "fold": [], "todo": "Write the sentence three new ways, one box at a time.",
  "script": "[warmly] Here's copia: one idea, said many ways. Let me try a different sentence first. Lucy told the truth. Box one, change the opener: Even when no one believed her, Lucy told the truth. Box two, a stronger verb: Lucy insisted it was true. Box three, add a detail: Lucy told the truth about the lamp-post in the snowy wood. Now you try it with the sentence about courage."},
 dict(READ, todo="Read about the 7 pillars. Then try the Pillar Watch below.",
  script="Read about the 7 pillars with your lens in mind. Each one has a real example from a book we read. Then try the Pillar Watch and the three questions."),
 chq("Answer each question in full sentences. Use a detail from your character's book.",
  "Three questions, in full sentences. One, your character, and why you chose them. Two, two pillars your character shows, with an example for each. Three, the one pillar that matters most for your character."),
 dict(WRITE, todo="Read Clara's plan. Your plan is your answers on the Reading tab.",
  script="Clara chose Edmund and two pillars. Your plan is your answers on the Reading tab, so there's nothing more to write here."),
], "cards": {},
 "virtue": [
  {"t": "Lucy keeps saying Narnia is real, even when the others think she is making it up. (The Lion, the Witch and the Wardrobe)", "ok": True, "why": "Honesty: she tells the truth even when it is hard."},
  {"t": "Edmund tells Peter and Susan that he and Lucy were only pretending about Narnia. (The Lion, the Witch and the Wardrobe)", "ok": False, "why": "That was a lie, so it is not honesty. Edmund changes later in the book."},
  {"t": "Stanley stays in a picture frame all night to help catch the sneak thieves. (Flat Stanley)", "ok": True, "why": "Service: he helps the museum and asks for nothing back."}]},
2: {"lookBtn": "Tap to learn about this painting of a little prince", "mods": [
 dict(WGRD, script="[warmly] Here's today's reading tip. Look back: what can you do now that was hard in the fall? Keep it in mind as you write. " + LENS_END),
 dol("Edmund's choices in The Lion, the Witch and the Wardrobe weren't easy to forgive. Edmund's shows belonging. A book title gets capitals. Weren't joins were and not."),
 {"id": "poem", "find": "Poetry", "fold": [":scope > .callout"], "todo": "Read the first four lines two times: slowly, then fast. Which one sounds like a train?",
  "script": "[curious] Here's a poem by Robert Louis Stevenson about riding on a train. Read the first four lines slowly. Now read them fast. Which one sounds like a train?"},
 {"id": "morph", "find": "Morphology", "fold": [":scope > .callout:not(:has(+ .match-game))", ":scope > .key-concept"], "todo": "Tap a word, then tap what it means. Match all four words.",
  "script": "Watch one match first. Joyous. Find the ending: ous. It means full of. So joyous means full of joy. That's my match! +how:morph2"},
 {"id": "vocab", "find": "Vocabulary", "fold": [], "todo": "Tap a word, then tap its meaning. Match all four words.",
  "script": "Here's a good-character word that isn't in the game. Fair. Being fair means everyone plays by the same rules. Now tap a word, then tap its meaning. Match all four."},
 {"id": "gram", "find": "Grammar", "fold": GRAM_FOLD, "todo": "Read the four sentences. Tap Now check your thinking. Then tap the five words that are wrong.",
  "script": "Simple, compound or complex? When the bell rang, we lined up. When starts a part that can't stand alone: complex. I read, and my sister drew. Two complete thoughts joined by and: compound. Name each sentence, and tap Now check your thinking. Then tap the five words that are wrong."},
 {"id": "spell", "find": "Spelling", "fold": [], "foldText": ["The Rule:"], "todo": "Read each question. Tap the one word in the row that fits.",
  "script": "Rule detective! Which word dropped a silent e? Raking. Rake, drop the e, add i n g. Read the rule. Then read each question, and tap the one word in the row that fits."},
 dict(READ, todo="Write your opening and two paragraphs. Then try the Pillar Watch below.",
  script="Today you write. Look back at your character's book and the 7 pillars. Then try the Pillar Watch, write your opening and two body paragraphs, and watch my video in the Read Like a Writer box."),
 {"id": "rwm", "sel": ".rwm-box", "after": ":scope > .rwm-header", "label": "Opti shows you how", "fold": [],
  "script": "Let's try all three parts with a different sentence, from The Tale of Despereaux. Nothing is sweeter in this sad world than the sound of someone you love calling your name. Nothing. Part one, read like a reader. The princess calls Despereaux's name, and it means everything to him. Part two, read like a writer. The author stops, then adds one more word: Nothing. The add-on makes us stop and feel it. Part three, write your own. My turn: Pizza night is the best night of the week. The best. Now it's your turn with Mrs. Lambchop's sentence. Write one sentence in each box."},
 chq("Answer each question in full sentences. Use a detail from your character's book.",
  "Two questions today, in full sentences. One, your opening: your character, the book, and your most important pillar. Two, two body paragraphs, one for each pillar."),
 dict(WRITE, todo="Read Clara's two paragraphs. Your draft is your answers on the Reading tab.",
  script="Clara wrote two paragraphs about Edmund: a pillar, an example, and what it shows. Your draft is on the Reading tab, so there's nothing more to write here."),
], "cards": {},
 "virtue": [
  {"t": "Jemmy orders the outlaws, “Lay down the whip,” to stop them from whipping the prince. (The Whipping Boy)", "ok": True, "why": "Courage: he speaks up even though the outlaws are dangerous."},
  {"t": "When the outlaws whip Prince Brat, he sets his jaw and does not make a sound. (The Whipping Boy)", "ok": True, "why": "Courage: he is brave, just the way Jemmy always was."},
  {"t": "People make fun of Stanley and call him names because he is flat. (Flat Stanley)", "ok": False, "why": "Calling names is not respect. Mrs. Lambchop says it is wrong to dislike people for their shapes."}]},
3: {"lookBtn": "Tap to learn about this painting of a knight and a lady", "mods": [
 dict(WGRD, script="[warmly] Here's today's reading tip. Give your proof: remember a time this year when you used a reading skill all on your own. " + LENS_END),
 dol("By the last page of the novel, every character had changed in some way. By the last page of the novel is the opening part, so a comma closes it."),
 {"id": "morph", "find": "Morphology", "fold": [":scope > .callout:not(:has(+ .fillin-game))", ":scope > .key-concept"], "todo": "Say the parts out loud. Type the whole word in each box. Tap Check My Answers.",
  "script": "Snap the parts together. Joy. Ful. Joyful! Full of joy. +how:morph3"},
 {"id": "vocab", "find": "Vocabulary", "fold": [], "todo": "Read each sentence. Pick the word that fits.",
  "script": "Try each word in the blank, and keep the one that makes sense. Mia said thank you and held the door. That shows blank. Courage? Hmm, not quite. Courtesy? Yes! Now pick the word that fits each sentence."},
 {"id": "gram", "find": "Grammar", "fold": GRAM_FOLD, "todo": "Read the before and after. Say the gray sentence the right way. Tap Check your sentence.",
  "script": "Be the editor. my dogs bowl was empty and he looked sad. My gets a capital. Dog's gets an apostrophe: the bowl belongs to the dog. A comma goes before and. Read the before and after, and tap Check yourself. Then say the gray sentence the right way, out loud, and tap Check your sentence."},
 {"id": "spell", "find": "Spelling", "fold": [], "foldText": ["The Rule:"], "todo": "Tap the misspelled words. Find all six.",
  "script": "Spot the mistake. She jumped in the puddel. Puddle ends in l e, so puddel is wrong. Read the rule. Each sentence has two misspelled words. Tap a word to check it, and find all six."},
 dict(READ, todo="Read your draft and the checklist. Then try the Pillar Watch below.",
  script="No new reading today. Read your draft and the checklist. Then try the Pillar Watch, make your writing stronger, write your closing, and give out the Bookshelf Awards."),
 chq("Answer each question in full sentences. Use a detail from your character's book.",
  "Three questions. One, fix your opening so it has your character, the book and your claim. Two, make your weakest paragraph stronger. Three, write your closing."),
 dict(WRITE, todo="Read Clara's closing. Write 3 notes for sharing out loud, and the one thing you will show.",
  script="Clara wrote a closing people remember. Your closing is on the Reading tab. Here, write three short notes for sharing out loud, and the one thing you'll show."),
], "cards": {},
 "virtue": [
  {"t": "Despereaux tells the princess, “I honor you.” (The Tale of Despereaux)", "ok": True, "why": "Courtesy: these are the polite words of a knight."},
  {"t": "After his talk with Aslan, Edmund says “I'm sorry” to each of the others. (The Lion, the Witch and the Wardrobe)", "ok": True, "why": "Responsibility: he owns what he did."},
  {"t": "Roscuro takes the princess down to the dungeon. (The Tale of Despereaux)", "ok": False, "why": "That is not a pillar. Taking someone away is cruel."}]},
4: {"lookBtn": "Tap to learn about this painting of a girl reading", "mods": [
 dict(WGRD, script="[warmly] Last reading tip of the year. You read four whole books. Think about how much your reading has grown. " + LENS_END),
 dol("This year we read about mice, rats, lions, and one very brave whipping boy. Commas go between the things in a list, even before and."),
 {"id": "poem", "find": "Poetry", "fold": [":scope > .callout"], "todo": "Choose a poem from this year. Read it out loud to someone.",
  "script": "Last poem of the year. Pick any poem you liked, and read it out loud to someone. Make your voice fit the poem: fast or slow, soft or loud."},
 {"id": "morph", "find": "Morphology", "fold": [], "todo": "Say what one part means. Roll the dice. Say what each word means, then check.",
  "script": "Quick question: what does re mean? Again! Here's a word that isn't on the dice. Restart. To start again. +how:morph-dice"},
 {"id": "vocab", "find": "Vocabulary", "fold": [], "todo": "Choose one word. Write one sentence about your character and you.",
  "script": "Watch me connect a word to a book and to me. Respect. Mrs. Lambchop and I both show respect: she stands up for Stanley, and I listen to my friends. Now choose your word, and write one sentence about your character and you."},
 {"id": "gram", "find": "Grammar", "fold": GRAM_FOLD, "todo": "Fix it in passes. Then tap all seven words that need fixing.",
  "script": "Three passes, like an editor. my sisters cat runned under the bed. Pass one, capitals: My. Pass two, apostrophes: sister's. Pass three, verbs: runned should be ran. Now do your passes, and tap all seven words that need fixing."},
 {"id": "spell", "find": "Spelling", "fold": [], "foldText": ["The Rule:"], "todo": "Roll the dice. Say the word and think of its rule. Then check.",
  "script": "Dice roll: hiking! The base word is hike. It ended in a silent e, so the e dropped. Tap Roll the dice, say the word, and think: which rule is at work? Then tap Check my answer."},
 dict(READ, todo="Read how to share. Then try the Pillar Watch below.",
  script="Today you share. Read how to share your response. Then try the Pillar Watch, look back down the Reading Road, and answer the questions."),
 chq("Answer each question in full sentences.",
  "Three questions today. One, your finished response. Two, the reading skill that grew the most for you. Three, a short letter to a new 3rd grader."),
 dict(WRITE, todo="Read Clara's title. Type your title. Then share your response out loud.",
  script="Clara gave her response a title that tells her big idea. Give yours a title, then share it out loud. Then save your certificate."),
], "cards": {},
 "virtue": [
  {"t": "Despereaux goes down into the dark dungeon to save the princess. (The Tale of Despereaux)", "ok": True, "why": "Courage and perseverance: he keeps going in the dark."},
  {"t": "The Princess Pea asks Roscuro, “Would you like some soup?” (The Tale of Despereaux)", "ok": True, "why": "Courtesy: she is kind to someone who hurt her."},
  {"t": "At the start of the book, Prince Brat calls Jemmy a rascal. (The Whipping Boy)", "ok": False, "why": "Calling names is not respect. The prince changes by the end."}]},
}

HOW = {'morph3': 'Say each pair of parts out loud. Type the whole word in the box. Then tap Check My Answers.',
       'morph2': 'Read the Remember box. Then tap a word, and tap what it means. Match all four words.',
       'morph-dice': 'Say what the word part means. Then tap Roll the Dice. Say what the word means, and tap Check My Thinking. Roll all six words.'}
for d, cfg in L.items():
    for m in cfg['mods']:
        t = m.get('script', '')
        if '+how:' in t:
            new, slug = t.split(' +how:')
            m['script'] = new + ' ' + HOW[slug]
VIDEO = {1: ['morph', 'vocab', 'gram', 'spell'], 2: ['morph', 'vocab', 'gram', 'spell', 'rwm'],
         3: ['morph', 'vocab', 'gram', 'spell'], 4: ['morph', 'vocab', 'gram', 'spell']}
for d, ids in VIDEO.items():
    for m in L[d]['mods']:
        if m['id'] in ids: m['video'] = 'g3ela-32-%d-teach-%s' % (d, m['id'])

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
    out = {}
    for d, cfg in L.items():
        for m in cfg['mods']:
            if 'video' in m: out['g3ela-32-%d-teach-%s' % (d, m['id'])] = m['script']
    return out

if __name__ == '__main__':
    import sys
    if '--count' not in sys.argv:
        for d, cfg in L.items():
            p = 'data/lesson-32-%d.json' % d
            j = json.load(io.open(p, encoding='utf-8'))
            if 'plate' in j: j['plate']['lookBtn'] = cfg['lookBtn']
            j['teach'] = {"dropTurnNotes": True, "mods": cfg['mods'], "cards": cfg['cards']}
            j['virtue'] = {"name": "pillars", "title": VTITLE, "items": cfg['virtue']}
            io.open(p, 'w', encoding='utf-8').write(json.dumps(j, ensure_ascii=False, indent=1))
            write_page('lesson-32-%d-ext.html' % d, j)
    rec = recorded(); tot = 0
    for k, t in rec.items():
        n = len(t); tot += n; print('%-32s %4d' % (k, n))
    print('film scripts this week: %d / 6260 credits (%.0f%%)' % (tot, 100.0 * tot / 6260))
    io.open('tools/g3sparkle/video/scripts_wk32.json', 'w', encoding='utf-8').write(json.dumps(rec, ensure_ascii=False, indent=1))
