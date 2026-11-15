#!/usr/bin/env python3
"""Week 27 (LWW Ch. 7-9): the Nov 10 2026 pilot fixes, as on weeks 18-24, for the new Narnia page template.
Writes DATA.teach, plate.lookBtn and DATA.virtue (Truth Watch: honesty, the Narnia unit's trait; 3 moments a day from
Ch. 7-9, checked against Planning docs/lww_text.txt) into data/lesson-27-N.json AND the page's oao-data block.
Word Study scripts are written for the Opti films: Day 1 teaches each idea; Days 2-4 show that day's activity with an
example that is not an answer anywhere in the week (inactive, impolite, incomplete, immature, indirect; sternly, snug, gloating;
catch/caught, drink/drank, keep/kept, make/made; replay, preview, rewind, unsafe, misbehave), and no two films open the same way. NO RECORDINGS (Bethany, Nov 14 2026):
films are built silent with captions; scripts stay written to the budget for later.

    python tools/g3sparkle/teach_wk27.py
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
1: {"lookBtn": "Tap to learn about this picture of beavers", "mods": [
 dict(WGRD, script="[warmly] Here's this week's reading tip. Two characters can stand in the same room and see it in different ways. Ask what each one wants, fears or knows. " + LENS_END),
 dol("Mr. Beaver led the children through the snow, and Mrs. Beaver put the kettle on. Led and put never add e d. And a comma comes before and."),
 {"id": "morph", "find": "Morphology", "fold": [], "todo": "Think about the question. Tap See if you were right. Type the base word in each box.",
  "script": "[curious] Two little word parts, one big job. The parts at the front of these words both mean not. Inactive means not active. Impolite means not polite. Here's the trick: im comes before words that start with m or p, like polite. Read the four words, and tap See if you were right. Then type the base word hiding in each one."},
 {"id": "vocab", "find": "Vocabulary", "fold": VOCAB_FOLD, "todo": "Fill in each sentence from the word bank. Tap Check My Work. Then play the matching game.",
  "script": "Be a word detective with me. Sternly. Here's the sentence. Aslan a man, said Mr. Beaver sternly. One, read the sentence: he sounds serious, maybe a little cross. Two, look for word parts: stern, plus l y. Three, check it. Sternly means in a strict, serious way. +how:vocabcloze"},
 {"id": "gram", "find": "Grammar", "fold": GRAM_FOLD, "todo": "Tap Now check your thinking. Then tap the four verbs that should not end in -ed.",
  "script": "[warmly] Most verbs add e d for the past. Walk, walked. But some verbs break the rule. Listen. Mr. Beaver catched a fish. Catched? No! It's caught. Verbs like that are called irregular. You learn them one at a time. Read The Rule box, and tap Now check your thinking. Then find the four verbs that should not end in e d."},
 {"id": "spell", "find": "Spelling", "fold": [], "todo": "Think about the questions. Tap Now name the pattern. Then sort all eight words.",
  "script": "Some long words are a short word with an extra part on the front. Replay. Cover the front part. What's left? Play! That front part means again, so replay means play again. Peel off the front, read the base word, then put it back. Tap Now name the pattern. Then sort the words."},
 {"id": "copia", "sel": ".spk-copia-card", "label": "Opti shows you how", "fold": [], "todo": "Write the sentence three new ways, one box at a time.",
  "script": "[warmly] Here's copia: one idea, said many ways. Let me try a different sentence first. Lucy smiled. Box one, change the opener: At the dam, Lucy smiled. Box two, a stronger verb: Lucy grinned. Box three, add a detail: Little Lucy smiled at the busy beaver. Now it's your turn, one box at a time. If you get stuck, tap Show one way."},
 dict(READ, todo="Read Chapter 7 in your book. Then try the Truth Watch below.",
  script="Read Chapter 7 in your book, with your lens in mind. When Mr. Beaver whispers a name, watch how each child feels. Then try the Truth Watch and the three questions."),
 dict(CHQ, script="Three questions, in full sentences, with details from the book. One, how two of the children feel at Aslan's name. Two, how the Beavers feel about Aslan. Three, how Edmund's feeling is different, and what that tells you."),
 dict(WRITE, todo="Plan your response: two characters, how each one sees Aslan or Narnia, and the big difference.",
  script="Today you plan a short response. Clara's first plan just said Edmund thinks one thing and Lucy thinks another. Her new plan says how each one feels, and why. Plan yours the same way."),
], "cards": {},
 "virtue": [
  {"t": "Mr. Beaver shows Lucy's handkerchief to prove he is Mr. Tumnus's friend.", "ok": True, "why": "He gives the children real proof of who he is."},
  {"t": "Peter tells Mr. Beaver plainly that they are strangers and have to be careful.", "ok": True, "why": "He says what he really thinks, politely."},
  {"t": "Edmund still does not tell anyone that he has met the White Witch.", "ok": False, "why": "He is keeping a secret that matters to everyone."}]},
2: {"lookBtn": "Tap to learn about this painting of a frozen river", "mods": [
 dict(WGRD, script="[warmly] Here's today's reading tip. Lewis doesn't always tell you what Edmund is thinking. Watch what Edmund does and says at dinner, and figure it out. " + LENS_END),
 dol("Mr. Beaver told the children about Aslan, and nobody saw Edmund go. Told and saw are past, with no e d."),
 {"id": "poem", "find": "Poetry", "fold": [":scope > .callout"], "todo": "Read the first limerick out loud. Then answer the question out loud.",
  "script": "[curious] Here's a limerick, a funny poem with five lines and a bouncy beat. Read the first one out loud, and listen to the last word of each line. Which lines rhyme together? Answer out loud."},
 {"id": "morph", "find": "Morphology", "fold": [":scope > .callout:not(:has(+ .match-game))", ":scope > .key-concept"], "todo": "Tap a word, then tap what it means. Match all four words.",
  "script": "Watch one match first. Incomplete. Find the word part at the front. It means not. What's left? Complete. So incomplete means not complete, like a puzzle with a missing piece. That's my match! +how:morph2"},
 {"id": "vocab", "find": "Vocabulary", "fold": [], "todo": "Tap a word, then tap its meaning. Match all four words.",
  "script": "Here's a cozy word from Chapter 7. Snug. Lucy thinks the Beavers have a very snug little home. Warm, cozy and safe! Now tap a word, then tap its meaning. Match all four."},
 {"id": "gram", "find": "Grammar", "fold": GRAM_FOLD, "todo": "Find the wrong verbs. Tap Now check your thinking. Then tap every word that is wrong.",
  "script": "Spot the wrong verb. The children drinked hot tea. Drinked? That's not a word! The past of drink is drank. The children drank hot tea. Check the verb in each of the four sentences, and tap Now check your thinking. Then fix the paragraph."},
 {"id": "spell", "find": "Spelling", "fold": [], "foldText": ["The Rule:"], "todo": "Read the rule. Tap every word built from a prefix and a base word.",
  "script": "Prefix hunt! Here's my sentence. Mom will preview the movie, then rewind the best part. Preview. Pre, plus view. Rewind. Re, plus wind. Two prefix words! Read the rule. Then tap every word built from a prefix and a base word."},
 dict(READ, todo="Read Chapter 8 in your book. Then try the Truth Watch below.",
  script="Read Chapter 8 in your book, with your lens in mind. Then try the Truth Watch, and watch my video in the Read Like a Writer box before you write."),
 {"id": "rwm", "sel": ".rwm-box", "after": ":scope > .rwm-header", "label": "Opti shows you how", "fold": [],
  "script": "[warmly] Let's try all three parts with a different sentence from Chapter 8. He is our brother after all, even if he is rather a little beast. Part one, read like a reader. Peter is cross with Edmund, but he still wants to find him. Part two, read like a writer. After all, and even if, let Peter hold two feelings in one sentence. Part three, mimic. Here's mine: She is my best friend after all, even if she eats the last cookie. Now it's your turn with the sentence about the whiskered face. Write one sentence in each box."},
 dict(CHQ, script="Three questions, in full sentences. One, what Edmund does near the end of Chapter 8, and when the others notice. Two, how the Beavers react. Three, one detail that shows Edmund's choice is a bad one."),
 dict(WRITE, todo="Write your comparison in full sentences.",
  script="Today you draft. Clara's first try said Lucy is good and Edmund is bad. Her draft says how each one feels, and uses the word reveals. Write your draft in full sentences."),
], "cards": {},
 "virtue": [
  {"t": "Mr. Beaver tells the children the hard truth: Aslan is not safe, but he is good.", "ok": True, "why": "He tells them what is true, even though it is a little scary."},
  {"t": "Lucy admits, almost in a whisper, that Edmund has been in Narnia alone before.", "ok": True, "why": "She tells the truth, even though it is about her own brother."},
  {"t": "Edmund slips out of the Beavers' house without telling anyone.", "ok": False, "why": "Sneaking away in secret is not being honest with his family."}]},
3: {"lookBtn": "Tap to learn about this old photograph of a castle", "mods": [
 dict(WGRD, script="[warmly] Here's today's reading tip. Today you see the night through Edmund's eyes. Notice what he tells himself, and what he really knows. " + LENS_END),
 dol("When Edmund came to the lion, he felt cold stone and knew that it was only a statue. A comma comes after the when part."),
 {"id": "morph", "find": "Morphology", "fold": [":scope > .callout:not(:has(+ .fillin-game))", ":scope > .key-concept"], "todo": "Say the parts out loud. Type the whole word in each box. Tap Check My Answers.",
  "script": "Snap the parts together. Im. Mature. Immature! Immature means not grown up yet, like a puppy chewing your shoes. +how:morph3"},
 {"id": "vocab", "find": "Vocabulary", "fold": [], "todo": "Read each sentence. Pick the word that fits.",
  "script": "Try each word in the blank, and keep the one that makes sense. Here's my sentence. The children ate dinner in the Beavers' blank little house. Treachery? Hmm, no. Snug? Yes! Now pick the word that fits each sentence."},
 {"id": "gram", "find": "Grammar", "fold": GRAM_FOLD, "todo": "Read the before and after. Fix the sentence and list three more verbs like these.",
  "script": "Let's fix a sentence the way the editor did. Mr. Beaver keeped a hole open in the ice. Keeped? The past of keep is kept. Mr. Beaver kept a hole open in the ice. Read the before and after, and tap Check yourself. Then fix the sentence, and list three more verbs like these."},
 {"id": "spell", "find": "Spelling", "fold": [], "foldText": ["The Rule:"], "todo": "Read the rule. Tap a word to check it. Find the two mistakes in each sentence.",
  "script": "Proofreader time! Here's a word with a mistake. Unsaif. Peel off the front part. What's left should be safe: s, a, f, e. The base word never changes, so it's unsafe. Read the rule. Then tap the words you think are spelled wrong."},
 dict(READ, todo="Read Chapter 9 in your book. Then try the Truth Watch below.",
  script="Read Chapter 9 in your book, with your lens in mind. Follow Edmund through the snow. Then try the Truth Watch and the three questions."),
 dict(CHQ, script="Three questions, in full sentences. One, two details about the Witch's castle. Two, whether Edmund's feelings about the Witch are changing. Three, who sees the truth more clearly, and why."),
 dict(WRITE, todo="Swap one vague phrase for more precise words.",
  script="Today you make it precise. Clara swapped a vague phrase for words that say exactly what Edmund's horror shows. Find one vague phrase in yours, and make it sharper."),
], "cards": {},
 "virtue": [
  {"t": "Edmund tells himself the Witch is the rightful Queen, but deep down he knows she is bad and cruel.", "ok": False, "why": "He is not being honest with himself."},
  {"t": "Edmund thinks more and more that he hates Peter, as if the cold and the snow were Peter's fault.", "ok": False, "why": "Blaming Peter for his own choice is not honest."},
  {"t": "Edmund tells the Witch that his brother and sisters are at the Beavers' house.", "ok": True, "why": "He tells the truth, but he uses it to help the Witch. Honest words can still hurt people."}]},
4: {"lookBtn": "Tap to learn about this painting of a snowy forest at night", "mods": [
 dict(WGRD, script="[warmly] Here's today's reading tip. Look back at one moment from two sides. Lucy and Edmund heard the same name. Why did they feel so differently? " + LENS_END),
 dol("The children came to the Beavers' house, and they ate fresh fish for dinner. Came and ate are past tense, with no e d."),
 {"id": "poem", "find": "Poetry", "fold": [":scope > .callout"], "todo": "Read both limericks. Say the rhyme pattern out loud. Does the second one fit?",
  "script": "Here are the limericks again. Say the pattern with letters: A, A, B, B, A. Then check the second limerick. Does it fit? Say it out loud."},
 {"id": "morph", "find": "Morphology", "fold": [":scope > .key-concept"], "foldText": ["Before you roll"], "todo": "Tap Roll the Dice. Say what the word means. Tap Check My Thinking. Roll all six words.",
  "script": "Quick! What do these two word parts mean? Not! Here's a word that's not on the dice. Indirect. A path that's not direct winds around, like Edmund's walk through the snow. Now tap Roll the Dice. Say what each word means, and tap Check My Thinking. Roll all six."},
 {"id": "vocab", "find": "Vocabulary", "fold": [], "todo": "Choose one word. Write one sentence about Chapters 7 to 9.",
  "script": "Here's how I'd use a word about the story. Gloating. Edmund stood gloating over the stone lion, because he thought the Witch had won. One word, one moment. Now choose one of your words and write your own sentence about Chapters 7 to 9."},
 {"id": "gram", "find": "Grammar", "fold": GRAM_FOLD, "todo": "Tap Check yourself. Tap every word that needs fixing. Then tap See the answers.",
  "script": "Three passes, like an editor. mrs beaver maked a marmalade roll and they ate it all. Pass one, capitals: Mrs. and Beaver. Pass two, verbs: maked becomes made. Pass three, a comma before and. Now do your passes, and tap every word that needs fixing."},
 {"id": "spell", "find": "Spelling", "fold": [], "foldText": ["The Rule:"], "todo": "Tap Roll the dice. Name the prefix and the base word. Tap Check my answer.",
  "script": "Here's my roll. Misbehave. Peel off the front part. The base word is behave. The front part means badly, so misbehave means behave badly. Tap Roll the dice, name the prefix and the base word, and tap Check my answer."},
 dict(READ, todo="Look back at Chapters 7 to 9. Then try the Truth Watch below.",
  script="No new chapters today. Look back at Chapters 7 to 9, and find a moment two characters see in different ways. Then try the Truth Watch and the three questions."),
 dict(CHQ, script="Three questions to finish the week, in full sentences. One, what Edmund's side of the story shows us. Two, the most important thing we learn from him. Three, why it helps to understand more than one character."),
 dict(WRITE, todo="Write your final response. End with what the difference shows.",
  script="Last step: publish. Clara ended with a big idea about choices. Write your final response, and end with what the difference between your two characters shows."),
], "cards": {},
 "virtue": [
  {"t": "Mrs. Beaver tells the children plainly that they cannot save Edmund by going to the Witch's House.", "ok": True, "why": "She tells them the hard truth to keep them safe."},
  {"t": "Lucy reminds the others that Edmund was there when they talked about Aslan.", "ok": True, "why": "She tells what she remembers, even though it is bad news."},
  {"t": "Edmund pretends to believe the Witch will not do anything very bad to the others.", "ok": False, "why": "Pretending to believe something is not being honest with yourself."}]},
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
        if m['id'] in ids: m['video'] = 'g3ela-27-%d-teach-%s' % (d, m['id'])

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
                out['g3ela-27-%d-teach-%s' % (d, m['id'])] = t
        for w, t in cfg['cards'].items(): out['g3ela-27-%d-say-%s' % (d, w)] = t
    return out

if __name__ == '__main__':
    import sys
    for d, cfg in L.items():
        p = 'data/lesson-27-%d.json' % d
        j = json.load(io.open(p, encoding='utf-8'))
        if 'plate' in j: j['plate']['lookBtn'] = cfg['lookBtn']
        j['teach'] = {"dropTurnNotes": True, "mods": cfg['mods'], "cards": cfg['cards']}
        j['virtue'] = {"name": "honesty", "title": VTITLE, "items": cfg['virtue']}
        io.open(p, 'w', encoding='utf-8').write(json.dumps(j, ensure_ascii=False, indent=1))
        write_page('lesson-27-%d-lww.html' % d, j)
    rec = recorded(); tot = 0
    for k, t in rec.items():
        n = len(t); tot += n; print('%-32s %4d' % (k, n))
    print('recorded this week: %d / 6260 credits (%.0f%%)' % (tot, 100.0 * tot / 6260))
    io.open('/tmp/wk27_rec.json', 'w', encoding='utf-8').write(json.dumps(rec, ensure_ascii=False, indent=1))
