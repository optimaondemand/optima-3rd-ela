#!/usr/bin/env python3
"""Week 31 (Paired Texts: The Courage to Act; extension pages): the Nov 10 2026 pilot fixes, as on weeks 18-30.
Writes DATA.teach, plate.lookBtn and DATA.virtue (Courage Watch, as week 18; each day's moments from that day's text,
Days 3-4 from both texts) into data/lesson-31-N.json AND the page's oao-data block. Word Study scripts are written for the
Opti films: Day 1 teaches each idea; Days 2-4 show that day's activity with an example that is not an answer anywhere in
the week (replay, painless, daring, grace telled; unsafe, loyal, rowed/although, wonderful; repaint, integrity, the boats
oars, everyone; unbroken, integrity-Lucy, the keepers daughter, rescue-boat), and no two films open the same way.
NO RECORDINGS (Bethany, Nov 14 2026): films are built silent with captions; scripts stay written to the budget.

    python tools/g3sparkle/teach_wk31.py [--count]
"""
import io, json, re

GRAM_FOLD = [":scope > .callout:not(:has(+ .spotter-game)):not(:has(+ .fillin-game)):not(:has(+ .sort-game)):not(:has(+ .dol-check-btn))"]
WGRD = {"id": "wgrd", "find": "What Good Readers", "fold": [":scope > p:not(.g3-do)", ":scope > .key-concept", ":scope > .socratic-box"],
        "todo": "Listen to Opti. Then tap the lens you will use today."}
VOCAB_FOLD = [":scope > .g3-model-h", ":scope > .decode-steps", ":scope > .key-concept"]
WRITE = {"id": "write", "find": "Writer.s Workshop", "fold": [":scope > .callout"], "foldText": ["watch how", "today.s tool"]}
DOL_TODO = "Tap the yellow parts. Then pick Sentence A or B and type it the right way."
VTITLE = "Courage Watch: Is someone being brave?"
LENS_END = "Then tap one of the two lenses below to use while you read. You don't need to write anything."
READ = {"id": "read", "find": "^\\W*(Read:|Look Back)", "fold": []}
def chq(todo, script): return {"id": "chq", "find": "Q1 —", "fold": [], "todo": todo, "script": script}
def dol(script): return {"id": "dol", "find": "Daily Oral", "fold": [], "todo": DOL_TODO, "script": "Let's fix a sentence. The correct one first. " + script + " Tap the yellow parts. Then pick Sentence A or Sentence B, and type it the right way."}
L = {
1: {"lookBtn": "Tap to learn about this painting of a young woman", "mods": [
 dict(WGRD, script="[warmly] Here's this week's reading tip. Two authors can write about the same topic and still say different things about it. This week the topic is courage. " + LENS_END),
 dol("Bravery isn't the absence of fear; it's choosing to act anyway. Isn't joins is and not. It's joins it and is. The mark in the middle, a semicolon, joins two complete thoughts that belong together."),
 {"id": "morph", "find": "Morphology", "fold": [], "todo": "Think about the questions. Tap See what was hiding. Type the missing part in each box.",
  "script": "[curious] What happens when you add a part to a word? Replay. Re is a prefix at the front. It means again. Replay means play again. Painless. Less is a suffix at the end. It means without. Painless means without pain. Every part on this page is one you already know. Read the parts, tap See what was hiding, then type the missing part of each word."},
 {"id": "vocab", "find": "Vocabulary", "fold": VOCAB_FOLD, "todo": "Fill in each sentence from the word bank. Tap Check My Work. Then play the matching game.",
  "script": "Be a word detective with me. Daring. Here's my sentence. Grace made a daring trip across the stormy sea. One, read the sentence: she went, even though it was dangerous. Two, look for word parts: dare, plus i n g. Three, check it. Daring means brave enough to take a risk. Now fill in each sentence from the word bank, and play the matching game."},
 {"id": "gram", "find": "Grammar", "fold": GRAM_FOLD, "todo": "Tap Now check your thinking. Then tap all six words that need fixing.",
  "script": "[warmly] A whole year of rules, in one sentence. when grace saw the wreck she telled her father. When starts the sentence: capital W. Grace is a name: capital G. A comma goes after wreck, to close the opening part. And telled should be told. Tap Now check your thinking. Then tap all six words in the passage that need fixing."},
 {"id": "spell", "find": "Spelling", "fold": [], "todo": "Think about the questions. Tap Now name the pattern. Then sort all eight words.",
  "script": "Front or back? Replay: the part re is at the front, so it's a prefix. Painless: the part less is at the end, so it's a suffix. Think about the questions, and tap Now name the pattern. Then sort the words: prefix at the front, or suffix at the end."},
 {"id": "copia", "sel": ".spk-copia-card", "label": "Opti shows you how", "fold": [], "todo": "Write the sentence three new ways, one box at a time.",
  "script": "[warmly] Here's copia: one idea, said many ways. Let me try a different sentence first. Grace rowed. Box one, change the opener: Through the storm, Grace rowed. Box two, a stronger verb: Grace pulled hard on the oars. Box three, add a detail: Grace rowed toward the wreck as the waves crashed. Now you try it with the sentence from Text 1."},
 dict(READ, todo="Read Text 1. Then try the Courage Watch below.",
  script="Read Text 1, What Is Courage?, with your lens in mind. Ask: what does this author say courage is, and what is it not? Then try the Courage Watch and the three questions."),
 chq("Answer each question in full sentences. Use details from the text.",
  "Three questions, in full sentences. One, what Text 1 says courage is, in your own words. Two, one big moment and one quiet moment of courage from the text. Three, a character from this year's books who fits."),
 dict(WRITE, todo="Plan in the box: what Text 1 says, a character, and your claim.",
  script="Today you plan. Clara wrote down what Text 1 says courage is, a character who shows it, and her claim. Plan yours in the box."),
], "cards": {},
 "virtue": [
  {"t": "Someone tells the truth when it would be easier to lie.", "ok": True, "why": "Text 1 calls this a quiet kind of courage."},
  {"t": "Someone stands up for a person who is being treated unfairly.", "ok": True, "why": "Text 1 says this takes courage, even though it is not a battle."},
  {"t": "Someone is never scared of anything at all.", "ok": False, "why": "Text 1 says courage is not the same as having no fear. Brave people feel afraid and act anyway."}]},
2: {"lookBtn": "Tap to learn about this painting of an old bridge", "mods": [
 dict(WGRD, script="[warmly] Here's today's reading tip. A story often shows courage instead of telling it. Look for what a character does, thinks and says. " + LENS_END),
 dol("Although Mira was afraid, she walked onto the bridge. Although starts the opening part. A comma closes the opening part, and Mira is a name."),
 {"id": "poem", "find": "Poetry", "fold": [":scope > .callout"], "todo": "Read the poem out loud. Find the metaphor. Make up your own short poem.",
  "script": "[curious] Here's a poem by Amy Lowell about the moon. Read it out loud. What are the fish-ponds compared to? That's a metaphor. Then make up a short poem of your own, and say it out loud."},
 {"id": "morph", "find": "Morphology", "fold": [":scope > .callout:not(:has(+ .match-game))", ":scope > .key-concept"], "todo": "Tap a word, then tap what it means. Match all four words.",
  "script": "Watch one match first. Unsafe. Find the prefix: un. It means not. So unsafe means not safe. That's my match! +how:morph2"},
 {"id": "vocab", "find": "Vocabulary", "fold": [], "todo": "Tap a word, then tap its meaning. Match all four words.",
  "script": "Here's a good-character word that isn't in the game. Loyal. A loyal friend sticks by you, even when things get hard. Now tap a word, then tap its meaning. Match all four."},
 {"id": "gram", "find": "Grammar", "fold": GRAM_FOLD, "todo": "Think about the questions. Tap Now check your thinking. Then tap the four words that are wrong.",
  "script": "Simple, compound or complex? Grace rowed, and her father helped. Two complete thoughts joined by and: compound. Although the sea was rough, they rowed on. Although starts a part that can't stand alone: complex. Name each sentence, and tap Now check your thinking. Then tap the four words that are wrong."},
 {"id": "spell", "find": "Spelling", "fold": [], "foldText": ["The Rule:"], "todo": "Read the rule. Tap every word with three or more syllables.",
  "script": "Clap it with me. Wonderful. Won, der, ful. Three beats, so I'd tap it. Brave? Just one beat, so no tap. Read the rule. Then tap every word in the sentences with three or more beats."},
 dict(READ, todo="Read Text 2. Then try the Courage Watch below.",
  script="Read Text 2, The Choice at the Bridge. It's a made-up story. The author never uses the word brave. Watch how the story shows it. Then try the Courage Watch, and watch my video in the Read Like a Writer box."),
 {"id": "rwm", "sel": ".rwm-box", "after": ":scope > .rwm-header", "label": "Opti shows you how", "fold": [],
  "script": "Let's try all three parts with a different sentence from Text 2. Mira's heart hammered. Part one, read like a reader. Mira is very scared. Part two, read like a writer. The author never says scared. She shows it with the body: a heart that hammers like a hammer on wood. Part three, write your own. My turn: Sam's hands shook on the rope. Now it's your turn with the author's sentence. Write one sentence in each box."},
 chq("Answer each question in full sentences. Use details from the texts.",
  "Three questions, in full sentences. One, two details that show Mira's courage. Two, how Mira fits what Text 1 says. Three, which way of showing courage you think is stronger, and why."),
 dict(WRITE, todo="Write your opening: name both texts, what they agree on, and how they differ.",
  script="Today you write your opening. Clara named both texts, said what they agree on, and said how they are different. Write yours."),
], "cards": {},
 "virtue": [
  {"t": "For weeks, Mira finds a reason to walk the other way when the big boys take things.", "ok": False, "why": "Walking away is not courage yet. Mira changes later in the story."},
  {"t": "Mira walks onto the bridge, even though her feet want to turn around.", "ok": True, "why": "She is scared, and she acts anyway."},
  {"t": "When the small boy asks, Mira says she was very afraid.", "ok": True, "why": "It takes courage to admit you were scared."}]},
3: {"lookBtn": "Tap to learn about this painting of a lighthouse", "mods": [
 dict(WGRD, script="[warmly] Here's today's reading tip. Same topic, different message? Check what each author chose to show you, and how the two texts fit together. " + LENS_END),
 dol("The author of Text 1 defines courage, and the story in Text 2 shows it in action. Text 1 and Text 2 are the names of the texts, so they get capitals. A comma goes before and."),
 {"id": "morph", "find": "Morphology", "fold": [":scope > .callout:not(:has(+ .fillin-game))", ":scope > .key-concept"], "todo": "Say the parts out loud. Type the whole word in each box. Tap Check My Answers.",
  "script": "Snap the parts together. Re. Paint. Repaint! To paint it again. +how:morph3"},
 {"id": "vocab", "find": "Vocabulary", "fold": [], "todo": "Read each sentence. Pick the word that fits.",
  "script": "Try each word in the blank, and keep the one that makes sense. Nobody was watching, but Leo gave back the extra change. That shows blank. Courageous? Hmm, not quite. Integrity? Yes! Now pick the word that fits each sentence."},
 {"id": "gram", "find": "Grammar", "fold": GRAM_FOLD, "todo": "Read the before and after. Fix the sentence in the gray box.",
  "script": "Be the editor. the boats oars were heavy and grace was tired. The gets a capital. Boat's gets an apostrophe: the oars belong to the boat. A comma goes before and. Grace is a name. Read the before and after, and tap Check yourself. Then fix the sentence in the gray box."},
 {"id": "spell", "find": "Spelling", "fold": [], "foldText": ["The Rule:"], "todo": "Tap the chunks in order to build each word.",
  "script": "Build it one beat at a time. Ev. Er. Y. One. Everyone! Four beats, in order. A chunk in the wrong place won't stick. Now tap the chunks in order to build each word."},
 dict(READ, todo="Read both texts again. Then try the Courage Watch below.",
  script="No new text today. Read both texts again, slowly, and collect your best details: one from Text 1 and one from Text 2. Then try the Courage Watch and the three questions."),
 chq("Answer each question in full sentences. Use details from the texts.",
  "Three questions, in full sentences. One, the idea from Text 1 you want to use. Two, the detail from Mira's story that proves it. Three, a character from this year who shows the same courage."),
 dict(WRITE, todo="Write one paragraph for each text, and one sentence that connects them.",
  script="Today you write the middle. Clara wrote one paragraph about Text 1 and one about Text 2, then showed how they connect. Write yours."),
], "cards": {},
 "virtue": [
  {"t": "Mira says, “Leave him alone,” and her voice comes out steadier than she expected.", "ok": True, "why": "She speaks up for someone smaller, even while she is afraid."},
  {"t": "The three big boys take younger children's things for weeks.", "ok": False, "why": "Picking on smaller kids is not courage."},
  {"t": "Text 1 says courage is something you practice, one choice at a time.", "ok": True, "why": "Every brave choice makes the next one easier."}]},
4: {"lookBtn": "Tap to learn about this painting of a rescue at sea", "mods": [
 dict(WGRD, script="[warmly] Here's today's reading tip. Before you finish, say what is alike and what is different about the two texts, in one sentence each. " + LENS_END),
 dol("After thinking about all four novels, I decided that courage looks different every time. After starts the opening part, and a comma closes it. I is always a capital."),
 {"id": "poem", "find": "Poetry", "fold": [":scope > .callout"], "todo": "Make up a poem and say it out loud. Name its form and one figure of speech.",
  "script": "Your last poem job this week: make up a poem of your own and say it out loud. Then name it, like a poet. Which form did you choose? Which figure of speech did you use?"},
 {"id": "morph", "find": "Morphology", "fold": [], "todo": "Say what one part means. Roll the dice. Say what each word means, then check.",
  "script": "Quick question: what does un mean? Not! Here's a word that's not on the dice. Unbroken. Not broken. The boat came home unbroken. +how:morph-dice"},
 {"id": "vocab", "find": "Vocabulary", "fold": [], "todo": "Choose one word. Write one sentence about a moment from a book.",
  "script": "Watch me use a word about a book from this year. Integrity. Lucy showed integrity: she kept telling the truth about Narnia, even when nobody believed her. Now choose your word, and write your own sentence about a book."},
 {"id": "gram", "find": "Grammar", "fold": GRAM_FOLD, "todo": "Fix it in passes. Then tap all seven words that need fixing.",
  "script": "Two passes, like an editor. the keepers daughter was brave and she rowed hard. Pass one, capitals: The. Pass two, apostrophes and commas: keeper's, and a comma before and. Now do your passes, and tap every word that needs fixing."},
 {"id": "spell", "find": "Spelling", "fold": [], "foldText": ["The Rule:"], "todo": "Roll the dice. Count the beats and say where they split. Then check.",
  "script": "Dice roll: rescue boat! Rescue: res, cue. Two beats. Boat: one beat. Tap Roll the dice, say the word, count its beats and say where they split. Then tap Check my answer."},
 dict(READ, todo="Read both texts one more time. Then try the Courage Watch below.",
  script="No new text today. Read both texts one last time, and pick your strongest detail for your closing. Then try the Courage Watch and the questions."),
 chq("Answer each question in full sentences. Use details from the texts and the books.",
  "Four questions today. One, your closing paragraph. Two, your best piece of evidence and why it works. Three, the character from this year who showed the most courage. Four, talk it over with someone at home."),
 dict(WRITE, todo="Write your whole comparison: opening, two paragraphs and a closing.",
  script="Last step: finish. Clara wrote a closing that says her claim in a new way. Put your whole comparison together, and check your capitals and end marks."),
], "cards": {},
 "virtue": [
  {"t": "Mira decides that the small boy matters more than her fear.", "ok": True, "why": "That is just what Text 1 says courage is."},
  {"t": "One of the three boys laughs at Mira.", "ok": False, "why": "Laughing at someone is not brave."},
  {"t": "Text 1 says courage can mean trying again after a big failure.", "ok": True, "why": "Trying again when you might fail takes courage too."}]},
}

HOW = {'morph3': 'Say each pair of parts out loud. Type the whole word in the box. Then tap Check My Answers.',
       'morph2': 'Read the Remember box. Then tap a word, and tap what it means. Match all four words.',
       'morph-dice': 'Say what the word part means. Then tap Roll the Dice. Say what the word means, and tap Check My Thinking. Roll all six words.'}
SPLICE = {}
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
        if m['id'] in ids: m['video'] = 'g3ela-31-%d-teach-%s' % (d, m['id'])

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
            if 'video' in m: out['g3ela-31-%d-teach-%s' % (d, m['id'])] = m['script']
    return out

if __name__ == '__main__':
    import sys
    if '--count' not in sys.argv:
        for d, cfg in L.items():
            p = 'data/lesson-31-%d.json' % d
            j = json.load(io.open(p, encoding='utf-8'))
            if 'plate' in j: j['plate']['lookBtn'] = cfg['lookBtn']
            j['teach'] = {"dropTurnNotes": True, "mods": cfg['mods'], "cards": cfg['cards']}
            j['virtue'] = {"name": "courage", "title": VTITLE, "items": cfg['virtue']}
            io.open(p, 'w', encoding='utf-8').write(json.dumps(j, ensure_ascii=False, indent=1))
            write_page('lesson-31-%d-ext.html' % d, j)
    rec = recorded(); tot = 0
    for k, t in rec.items():
        n = len(re.sub(r'\[[a-z ]+\]\s*', '', t)); tot += n; print('%-32s %4d' % (k, n))
    print('recorded this week: %d / 6260 credits (%.0f%%)' % (tot, 100.0 * tot / 6260))
    io.open('/tmp/wk31_rec.json', 'w', encoding='utf-8').write(json.dumps(rec, ensure_ascii=False, indent=1))
