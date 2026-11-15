#!/usr/bin/env python3
"""Week 29 (LWW Ch. 13-15): the Nov 10 2026 pilot fixes, as on weeks 18-28, for the Narnia page template.
Writes DATA.teach, plate.lookBtn and DATA.virtue (Truth Watch: honesty, the Narnia unit's trait; 3 moments a day from
that day's chapter, Day 4 from the whole week, checked against Planning docs/lww_text.txt) into data/lesson-29-N.json
AND the page's oao-data block. Word Study scripts are written for the Opti films: Day 1 teaches each idea; Days 2-4 show
that day's activity with an example that is not an answer anywhere in the week (projectile, interject, object,
trajectory; earnestly, stern, my brother's cup, Edmund the traitor; We're home / come here / where are my boots /
its snowing; unbreakable, unlocked, replanted, uncovered), and no two films open the same way.
Hard content (Ch. 13 the Witch and Edmund; Ch. 14 Aslan's death) is named gently, never in detail (Bethany, Nov 15 2026).
NO RECORDINGS (Bethany, Nov 14 2026): films are built silent with captions; scripts stay written to the budget.

    python tools/g3sparkle/teach_wk29.py
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
1: {"lookBtn": "Tap to learn about this painting of an old stone table", "mods": [
 dict(WGRD, script="[warmly] Here's this week's reading tip. A topic is one word, like loyalty. A theme is the big lesson, said as a full sentence. Watch for big ideas in Chapter 13. " + LENS_END),
 dol("Let him approach, said Aslan. The words Aslan says sit inside the quotation marks. Let starts with a capital, and the comma goes inside, before the closing mark."),
 {"id": "morph", "find": "Morphology", "fold": [], "todo": "Think about the question. Tap See if you were right. Type the missing part in each box.",
  "script": "[curious] A throw is hiding inside this word. Projectile. Pro means forward. Ject means throw. A projectile is something thrown forward, like a snowball. Read the four words and their parts, and tap See if you were right. Then type the missing part in each box."},
 {"id": "vocab", "find": "Vocabulary", "fold": VOCAB_FOLD, "todo": "Fill in each sentence from the word bank. Tap Check My Work. Then play the matching game.",
  "script": "Be a word detective with me. Earnestly. Here's the sentence. The Lion and the Witch talked earnestly together in low voices. One, read the sentence: everyone is waiting, and worried. Two, look for word parts: earnest, l y. Three, check it. Earnestly means in a very serious way. +how:vocabcloze"},
 {"id": "gram", "find": "Grammar", "fold": GRAM_FOLD, "todo": "Tap Now check your thinking. Then tap the three words with a dialogue mistake.",
  "script": "[warmly] When someone talks in a story, their words get a little house. We're home, said Mom. Quotation marks go around We're home. We're gets a capital. The comma goes inside, before the closing mark. Tap Now check your thinking. Then find the three dialogue mistakes."},
 {"id": "spell", "find": "Spelling", "fold": [], "todo": "Think about the questions. Tap Now name the pattern. Then sort all eight words.",
  "script": "Big words come apart! Unbreakable. Find the root first: break. The front part is un. The end part is able. Un, break, able. Think about the questions, and tap Now name the pattern. Then sort the words."},
 {"id": "copia", "sel": ".spk-copia-card", "label": "Opti shows you how", "fold": [], "todo": "Write the sentence three new ways, one box at a time.",
  "script": "[warmly] Here's copia: one idea, said many ways. Let me try a different sentence first. Lucy cried. Box one, change the opener: On the quiet hilltop, Lucy cried. Box two, a stronger verb: Lucy sobbed. Box three, add a detail: Lucy cried for her brother Edmund. Now it's your turn, one box at a time. If you get stuck, tap Show one way."},
 dict(READ, todo="Read Chapter 13 in your book. Then try the Truth Watch below.",
  script="Read Chapter 13 in your book, with your lens in mind. At the start, the Witch tries to hurt Edmund, but Aslan's friends rescue him in time. Then try the Truth Watch and the three questions."),
 dict(CHQ, script="Three questions, in full sentences, with details from the book. One, what the Deep Magic is, in your own words. Two, what you think Aslan offered the Witch, and why. Three, a big idea you see forming."),
 dict(WRITE, todo="Write two or three possible themes, each as a full sentence.",
  script="Today you brainstorm themes. Clara's first try was just: being good. Her new list says each theme as a full sentence that starts, The story shows that. Write two or three of your own."),
], "cards": {},
 "virtue": [
  {"t": "Edmund says “I’m sorry” to each of his brother and sisters.", "ok": True, "why": "He tells the truth about what he did wrong."},
  {"t": "Aslan says the Witch is right about the Deep Magic, even though it is bad news.", "ok": True, "why": "He does not pretend, even when the truth is hard."},
  {"t": "The Witch makes herself look like a big rock so the rescuers will not find her.", "ok": False, "why": "She tricks them by making things look like what they are not."}]},
2: {"lookBtn": "Tap to learn about this painting of a moonlit sea", "mods": [
 dict(WGRD, script="[warmly] Here's today's reading tip. In Chapter 14, notice what Aslan chooses to do. A choice like that can be strong proof for a theme. " + LENS_END),
 dol("We couldn't sleep, said Lucy. We starts with a capital. The comma goes inside the quotation mark, and the tag, said Lucy, ends with a period."),
 {"id": "poem", "find": "Poetry", "fold": [":scope > .callout"], "todo": "Read the poem out loud. Say which kind it is, and two reasons why.",
  "script": "[curious] Here's a short poem by Emily Dickinson. Read it out loud. Count the lines, and listen to the ends of the lines. Is it free verse, rhymed verse, a haiku, or a limerick? Answer out loud."},
 {"id": "morph", "find": "Morphology", "fold": [":scope > .callout:not(:has(+ .match-game))", ":scope > .key-concept"], "todo": "Tap a word, then tap what it means. Match all four words.",
  "script": "Watch one match first. Interject. Inter means between, and ject means throw. To interject is to throw your words in while someone else is talking. That's my match! +how:morph2"},
 {"id": "vocab", "find": "Vocabulary", "fold": [], "todo": "Tap a word, then tap its meaning. Match all three words.",
  "script": "Ever seen a face so serious that nobody dared to ask a question? Stern. Aslan's face was stern. Stern means very serious, and a little strict. Now tap a word, then tap its meaning. Match all three."},
 {"id": "gram", "find": "Grammar", "fold": GRAM_FOLD, "todo": "Find each mistake. Tap Now check your thinking. Then tap every word that is wrong.",
  "script": "Find the two mistakes. come here. said Dad. Come needs a capital, because it starts the spoken words. And that period should be a comma, inside the quotation mark. Read the four sentences, and tap Now check your thinking. Then fix the paragraph."},
 {"id": "spell", "find": "Spelling", "fold": [], "foldText": ["The Rule:"], "todo": "Read the rule. Tap every word built from a root with parts added.",
  "script": "Root hunt! Lucy unlocked the door. Unlocked: un, lock, e d. Lock is the root, with parts on both ends. That one gets a tap! Read the rule. Then tap every word in the two sentences that is built from a root with parts added."},
 dict(READ, todo="Read Chapter 14 in your book. Then try the Truth Watch below.",
  script="Read Chapter 14 in your book, with your lens in mind. It is the saddest chapter in the book, and something very sad happens to Aslan. Read it slowly, and take a break if you need one. It is okay to feel sad. The story is not over yet. Then try the Truth Watch, and watch my video in the Read Like a Writer box."),
 {"id": "rwm", "sel": ".rwm-box", "after": ":scope > .rwm-header", "label": "Opti shows you how", "fold": [],
  "script": "Let's try all three parts with part of a sentence from Chapter 14. They kissed his mane and his nose and his paws and his great, sad eyes. Part one, read like a reader. Lucy and Susan love Aslan, and they are saying goodbye. Part two, read like a writer. It's a list joined by and. The last one, his great, sad eyes, is the longest, so the list ends slowly. Part three, mimic. Here's mine: I hugged my dog's ears and his nose and his paws and his warm, sleepy head. Now it's your turn with the Witch's list of names. Write one sentence in each box."},
 dict(CHQ, script="Three questions, in full sentences. One, what happens at the Stone Table, in order. Two, how Lucy and Susan show they are loyal. Three, how Chapter 14 is proof for your theme."),
 dict(WRITE, todo="Draft your response: your theme, and proof from two parts of the story.",
  script="Today you draft. Clara said her theme as a full sentence. Then she gave proof from the beginning and the middle of the story. Write your draft the same way."),
], "cards": {},
 "virtue": [
  {"t": "When Peter says Aslan will be at the battle, Aslan says, “I can give you no promise of that.”", "ok": True, "why": "He will not make a promise he may not keep."},
  {"t": "Lucy tells Susan she has a horrible feeling, and Susan says she has the same feeling.", "ok": True, "why": "They both say how they really feel."},
  {"t": "When the girls ask what is wrong, Aslan tells them, “I am sad and lonely.”", "ok": True, "why": "He tells them the truth about his feelings."}]},
3: {"lookBtn": "Tap to learn about this painting of a sunrise", "mods": [
 dict(WGRD, script="[warmly] Here's today's reading tip. In Chapter 15, listen closely to what Aslan explains. Ask how it changes the big lesson you have been building. " + LENS_END),
 dol("And now, said Aslan presently, to business. The tag sits in the middle. A comma comes after presently, and to stays small, because it is the same sentence."),
 {"id": "morph", "find": "Morphology", "fold": [":scope > .callout:not(:has(+ .fillin-game))", ":scope > .key-concept"], "todo": "Say the parts out loud. Type the whole word in each box. Tap Check My Answers.",
  "script": "Snap the parts together. Ob. Ject. Object! When you object, you throw a no against an idea. +how:morph3"},
 {"id": "vocab", "find": "Vocabulary", "fold": [], "todo": "Read each sentence. Pick the word that fits.",
  "script": "Try each word in the blank, and keep the one that makes sense. Here's my sentence. My brother broke my cup, so he cleaned up the mess to blank. Traitor? Hmm, no. Atone? Yes! Now pick the word that fits each sentence."},
 {"id": "gram", "find": "Grammar", "fold": GRAM_FOLD, "todo": "Read the before and after. Fix the line in the gray box.",
  "script": "Be the editor. where are my boots, asked Peter. Where needs a capital, because it starts the spoken words. It's a question, so a question mark goes inside the closing mark. Read the before and after, and tap Check yourself. Then fix the line in the gray box."},
 {"id": "spell", "find": "Spelling", "fold": [], "foldText": ["The Rule:"], "todo": "Read the rule. Cover each word, write it, then tap to check.",
  "script": "Let's spell one from the root. Replanted. The root is plant. Re goes on the front, and e d goes on the end. Re, plant, e d. Replanted! Read the rule. Look hard at each word, cover it, and write it. Then tap the card to check."},
 dict(READ, todo="Read Chapter 15 in your book. Then try the Truth Watch below.",
  script="Read Chapter 15 in your book, with your lens in mind. It starts on a sad, quiet night. Keep going to the sunrise. Then try the Truth Watch and the three questions."),
 dict(CHQ, script="Three questions, in full sentences. One, the Deeper Magic in your own words. Two, how Lucy and Susan feel at sunrise, and what that shows. Three, the new proof Chapter 15 gives your theme."),
 dict(WRITE, todo="Add two sentences of proof from Chapter 15 to your response.",
  script="Today you revise. Clara added proof from Chapter 15 with a joining phrase: goes even deeper. Add two sentences of Chapter 15 proof to yours."),
], "cards": {},
 "virtue": [
  {"t": "Susan tells Lucy, “I feel afraid to turn round.”", "ok": True, "why": "She says how she really feels, even though she is scared."},
  {"t": "When Lucy asks if he is dead, Aslan answers her truthfully: “Not now.”", "ok": True, "why": "He gives her a true answer to her question."},
  {"t": "When Susan asks what it all means, Aslan explains the Deeper Magic plainly.", "ok": True, "why": "He tells them the whole truth, so they understand."}]},
4: {"lookBtn": "Tap to learn about this painting of a lion", "mods": [
 dict(WGRD, script="[warmly] Here's today's reading tip. A theme needs proof from the start, the middle and the end of a book. Look back and choose your strongest three. " + LENS_END),
 dol("Fall back, all of you, said Aslan, and I will talk to the Witch alone. The tag sits in the middle, and the second part, and I will talk, stays small."),
 {"id": "poem", "find": "Poetry", "fold": [":scope > .callout"], "todo": "Think of the poems you read this year. Put each one in a column on paper.",
  "script": "Your turn to sort! Think of every poem you read this year: haiku, limericks, poems that rhyme, and poems that don't. Put each one in a column on paper."},
 {"id": "morph", "find": "Morphology", "fold": [], "todo": "Say what ject means. Roll the dice. Say what each word means, then check.",
  "script": "Quick question: what does ject mean? Throw! Here's a word that's not on the dice. Trajectory. It's the path something takes when you throw it, like the curve of a ball. +how:morph-dice"},
 {"id": "vocab", "find": "Vocabulary", "fold": [], "todo": "Choose one word. Write one sentence about the theme.",
  "script": "One word can carry a big idea. Traitor. At first, Edmund acts like a traitor, but in Chapter 13 his family forgives him. One word, one big idea. Now choose your word, and write your own sentence about the theme."},
 {"id": "gram", "find": "Grammar", "fold": GRAM_FOLD, "todo": "Fix it in passes. Then tap every word that needs fixing.",
  "script": "Two passes, like an editor. its snowing, said peter. Pass one, capitals: It's and Peter. Pass two, apostrophes: it's means it is. The comma is already inside. Now do your passes, and tap every word that needs fixing."},
 {"id": "spell", "find": "Spelling", "fold": [], "foldText": ["The Rule:"], "todo": "Roll the dice. Name the root and the parts. Then check.",
  "script": "Dice roll: uncovered! Cover the front and the end. What's left? Cover! That's the root, and the parts are un and e d. Tap Roll the dice, say the root and the parts, and tap Check my answer."},
 dict(READ, todo="Look back at Chapters 13 to 15. Then try the Truth Watch below.",
  script="No new chapters today. Look back at the whole book so far, and find your strongest proof from the start, the middle and the end. Then try the Truth Watch and the three questions."),
 dict(CHQ, script="Three questions to finish the week, in full sentences. One, your theme as a full sentence. Two, three moments from different chapters, with chapter numbers. Three, why proof from more than one chapter matters."),
 dict(WRITE, todo="Write your whole response: theme, proof from three chapters, and a closing.",
  script="Last step: put it all together. Clara put her proof in order, earliest first and strongest last. Write your whole response, with a closing sentence."),
], "cards": {},
 "virtue": [
  {"t": "Mr. Beaver says the Witch is not really the Queen of Narnia.", "ok": True, "why": "He tells the truth about her, even in front of her messenger."},
  {"t": "The Witch’s messenger calls her “the Queen of Narnia.”", "ok": False, "why": "That title is not really hers."},
  {"t": "Aslan keeps his promise to the Witch, even though it costs him so much.", "ok": True, "why": "He does exactly what he said he would do."}]},
}

HOW = {'morph3': 'Say each pair of parts out loud. Type the whole word in the box. Then tap Check My Answers.',
       'morph2': 'Read the Remember box. Then tap a word, and tap what it means. Match all four words.',
       'morph-dice': 'Say what the word part means. Then tap Roll the Dice. Say what the word means, and tap Check My Thinking. Roll all six words.',
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
        if m['id'] in ids: m['video'] = 'g3ela-29-%d-teach-%s' % (d, m['id'])

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
    """What gets voiced this week: the 17 film clips (minus any shared ending)."""
    out = {}
    for d, cfg in L.items():
        for m in cfg['mods']:
            if 'video' in m:
                t = m['script']
                if (d, m['id']) in SPLICE: t = t[:len(t) - len(HOW[SPLICE[(d, m['id'])][len('g3ela-how-'):]])].rstrip()
                out['g3ela-29-%d-teach-%s' % (d, m['id'])] = t
        for w, t in cfg['cards'].items(): out['g3ela-29-%d-say-%s' % (d, w)] = t
    return out

if __name__ == '__main__':
    import sys
    if '--count' not in sys.argv:
        for d, cfg in L.items():
            p = 'data/lesson-29-%d.json' % d
            j = json.load(io.open(p, encoding='utf-8'))
            if 'plate' in j: j['plate']['lookBtn'] = cfg['lookBtn']
            j['teach'] = {"dropTurnNotes": True, "mods": cfg['mods'], "cards": cfg['cards']}
            j['virtue'] = {"name": "honesty", "title": VTITLE, "items": cfg['virtue']}
            io.open(p, 'w', encoding='utf-8').write(json.dumps(j, ensure_ascii=False, indent=1))
            write_page('lesson-29-%d-lww.html' % d, j)
    rec = recorded(); tot = 0
    for k, t in rec.items():
        n = len(t); tot += n; print('%-32s %4d' % (k, n))
    print('recorded this week: %d / 6260 credits (%.0f%%)' % (tot, 100.0 * tot / 6260))
    io.open('/tmp/wk29_rec.json', 'w', encoding='utf-8').write(json.dumps(rec, ensure_ascii=False, indent=1))
