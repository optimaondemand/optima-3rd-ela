#!/usr/bin/env python3
"""Week 30 (LWW Ch. 16-17 + synthesis): the Nov 10 2026 pilot fixes, as on weeks 18-29, for the Narnia page template.
Writes DATA.teach, plate.lookBtn and DATA.virtue (Truth Watch: honesty, the Narnia unit's trait; Day 1 from Ch. 16-17,
Days 2-4 from the whole book, checked against Planning docs/lww_text.txt) into data/lesson-30-N.json AND the page's
oao-data block. Word Study scripts are written for the Opti films: Day 1 teaches each idea; Days 2-4 show that day's
activity with an example that is not an answer anywhere in the week (interview, transfer, report, transatlantic;
liberated, remarkable, the two friends, reconciled Edmund; lucy found mr. tumnus / the fauns scarf / the witchs sledge /
the professors house; cake-boat-rewrite, the goat and the lake, sunset, pilot), and no two films open the same way.
NO RECORDINGS (Bethany, Nov 14 2026): films are built silent with captions; scripts stay written to the budget.

    python tools/g3sparkle/teach_wk30.py
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
1: {"lookBtn": "Tap to learn about this painting of a young queen", "mods": [
 dict(WGRD, script="[warmly] Here's this week's reading tip. An ending often answers a question the beginning asked. Watch what Chapters 16 and 17 settle, and how that shows the big lesson. " + LENS_END),
 dol("When the four thrones were filled at Cair Paravel, the prophecy of Narnia came true. When starts the sentence with a capital. Cair Paravel and Narnia are names, so they get capitals, and a comma closes the opening part."),
 {"id": "morph", "find": "Morphology", "fold": [], "todo": "Think about the question. Tap See if you cracked it. Type the missing part in each box.",
  "script": "[curious] Can you crack this one? Interview. Inter means between. An interview is a talk between two people. Every root on this page is one you already know. Read the word parts, and tap See if you cracked it. Then type the missing part of each word."},
 {"id": "vocab", "find": "Vocabulary", "fold": VOCAB_FOLD, "todo": "Fill in each sentence from the word bank. Tap Check My Work. Then play the matching game.",
  "script": "Be a word detective with me. Liberated. Here's the sentence. The whole crowd of liberated statues surged back into the courtyard. One, read the sentence: the statues are alive again. Two, look for word parts: liber, ate, e d. Three, check it. Liberated means set free. +how:vocabcloze"},
 {"id": "gram", "find": "Grammar", "fold": GRAM_FOLD, "todo": "Tap Now check your thinking. Then tap the five words that need a capital.",
  "script": "[warmly] An editor hunts for capitals. lucy found mr. tumnus. Lucy is a name: capital L. Mr. Tumnus is a name too: capital M, capital T. Names get capitals wherever they are in a sentence. Tap Now check your thinking. Then tap the five words that need a capital."},
 {"id": "spell", "find": "Spelling", "fold": [], "todo": "Think about the questions. Tap Now name the pattern. Then sort all nine words.",
  "script": "Three patterns in one pile! Cake: a silent e at the end. Boat: two vowels make one sound, a vowel team. Rewrite: a prefix, re, plus a base word, write. Think about the questions, and tap Now name the pattern. Then sort the words."},
 {"id": "copia", "sel": ".spk-copia-card", "label": "Opti shows you how", "fold": [], "todo": "Write the sentence three new ways, one box at a time.",
  "script": "[warmly] Here's copia: one idea, said many ways. Let me try a different sentence first. Lucy laughed. Box one, change the opener: In the noisy courtyard, Lucy laughed. Box two, a stronger verb: Lucy giggled. Box three, add a detail: Lucy laughed at the giant's tiny handkerchief. Now it's your turn, one box at a time. If you get stuck, tap Show one way."},
 dict(READ, todo="Read Chapters 16 and 17 in your book. Then try the Truth Watch below.",
  script="Read Chapters 16 and 17, the last two chapters of the book, with your lens in mind. There is a battle, but it is short, and it ends well. Then try the Truth Watch and the three questions."),
 dict(CHQ, script="Three questions, in full sentences. One, how the statues coming alive connects to the winter and the stone. Two, how Edmund is different in the battle. Three, what the crowning shows about the theme. Start with: the ending shows that."),
 dict(WRITE, todo="Add two sentences from Chapter 16 or 17 to your response.",
  script="Today you revise with the ending. Clara added proof from the last chapter: Edmund, once a traitor, is crowned a king. Add two sentences from Chapter 16 or 17 to yours."),
], "cards": {},
 "virtue": [
  {"t": "Peter tells Aslan that winning the battle was all Edmund’s doing.", "ok": True, "why": "He gives Edmund the credit he really earned."},
  {"t": "Lucy is cross with Aslan, then says, “I’m sorry, Aslan,” and goes to help the others.", "ok": True, "why": "She owns up to being wrong right away."},
  {"t": "Giant Rumblebuffin picks up Lucy by mistake and says, “I beg your pardon, Missie.”", "ok": True, "why": "He says plainly that he made a mistake."}]},
2: {"lookBtn": "Tap to learn about this photo of lion statues", "mods": [
 dict(WGRD, script="[warmly] Here's today's reading tip. Look back from the first chapter to the last. What changed? That change points to the theme. " + LENS_END),
 dol("The battle was over in a few minutes, and Peter and Aslan shook hands. The starts with a capital. A comma comes before and, because it joins two complete thoughts. Peter and Aslan are names."),
 {"id": "poem", "find": "Poetry", "fold": [":scope > .callout"], "todo": "Read the poem out loud. Find the fire that sings, and name the tool.",
  "script": "[curious] Here's a poem by Sara Teasdale. Read it out loud. Find the fire that sways and sings. What kind of figurative language is that? Answer out loud."},
 {"id": "morph", "find": "Morphology", "fold": [":scope > .callout:not(:has(+ .match-game))", ":scope > .key-concept"], "todo": "Tap a word, then tap what it means. Match all four words.",
  "script": "Watch one match first. Transfer. Find the root: trans. It means across. To transfer is to move something across to a new place. That's my match! +how:morph2"},
 {"id": "vocab", "find": "Vocabulary", "fold": [], "todo": "Tap a word, then tap its meaning. Match all four words.",
  "script": "Ever met someone truly amazing? Remarkable. The book says the Professor was a very remarkable man. Remarkable means so unusual it's worth talking about. Now tap a word, then tap its meaning. Match all four."},
 {"id": "gram", "find": "Grammar", "fold": GRAM_FOLD, "todo": "Think about the four questions. Tap Check yourself. Then tap every word that is wrong.",
  "script": "Four rules, one sentence. the fauns scarf was red and lucy liked it. The needs a capital to start the sentence. Faun's needs an apostrophe: the scarf belongs to the faun. A comma goes before and. And Lucy is a name. Tap Check yourself. Then tap every word that is wrong."},
 {"id": "spell", "find": "Spelling", "fold": [], "foldText": ["The Rule:"], "todo": "Read the rule. Tap every silent-e, vowel-team or r-controlled word.",
  "script": "Pattern hunt! The goat ran to the lake. Goat: two vowels, one sound, a vowel team. Tap! Ran: short a, closed. No tap. Lake: silent e. Tap! Read the rule. Then tap every word in the two sentences with a silent-e, vowel-team or r-controlled syllable."},
 dict(READ, todo="Look back through the whole book. Then try the Truth Watch below.",
  script="No new chapters today. Look back through the whole book, from Lucy's first trip through the wardrobe to the crowning. Then try the Truth Watch, and watch my video in the Read Like a Writer box."),
 {"id": "rwm", "sel": ".rwm-box", "after": ":scope > .rwm-header", "label": "Opti shows you how", "fold": [],
  "script": "Let's try all three parts with a sentence from Chapter 16. Instead of all that deadly white the courtyard was now a blaze of colors. Part one, read like a reader. The statues are alive, and the courtyard is bright. Part two, read like a writer. Two pictures: deadly white, then a blaze of colors. Instead of flips one into the other. Part three, mimic. Here's mine: Instead of all that gray snow, the yard was now a carpet of green grass. Now it's your turn with the museum and the zoo. Write one sentence in each box."},
 dict(CHQ, script="Three questions, in full sentences. One, three moments from different chapters that prove the same theme. Two, Edmund at the beginning and at the end. Three, the one moment that proves your theme best."),
 dict(WRITE, todo="Edit your response for capitals, apostrophes and commas.",
  script="Today you edit. Check your capitals, your apostrophes and your commas, like an editor. Then read your response out loud once, and write the fixed version."),
], "cards": {},
 "virtue": [
  {"t": "In Chapter 5, Edmund says he was only pretending, and that he never went into Narnia.", "ok": False, "why": "He had been there. He lied to make Lucy look silly."},
  {"t": "Lucy keeps saying Narnia is real, even when the others laugh at her.", "ok": True, "why": "She tells the truth even when no one believes her."},
  {"t": "At the end, the children tell the Professor the whole story about the missing coats.", "ok": True, "why": "They explain what really happened, even though it sounds hard to believe."}]},
3: {"lookBtn": "Tap to learn about this painting of a castle by the sea", "mods": [
 dict(WGRD, script="[warmly] Here's today's reading tip. The book ends where it began, at the wardrobe. Think about why Lewis brings the children all the way back. " + LENS_END),
 dol("The four rulers hunted the White Stag one day, but they never caught it. White Stag is a name, so both words get capitals. A comma comes before but."),
 {"id": "morph", "find": "Morphology", "fold": [":scope > .callout:not(:has(+ .fillin-game))", ":scope > .key-concept"], "todo": "Say the parts out loud. Type the whole word in each box. Tap Check My Answers.",
  "script": "Snap the parts together. Re. Port. Report! When you report, you carry the news back. +how:morph3"},
 {"id": "vocab", "find": "Vocabulary", "fold": [], "todo": "Read each sentence. Pick the word that fits.",
  "script": "Try each word in the blank, and keep the one that makes sense. Here's my sentence. After their fight, the two friends were blank. Sovereign? Hmm, no. Reconciled? Yes! Now pick the word that fits each sentence."},
 {"id": "gram", "find": "Grammar", "fold": GRAM_FOLD, "todo": "Read the before and after. Fix the sentence in the gray box.",
  "script": "Be the editor. the witchs sledge was fast and edmund was cold. The gets a capital. Witch's gets an apostrophe. A comma goes before and. Edmund is a name. Read the before and after, and tap Check yourself. Then fix the sentence in the gray box."},
 {"id": "spell", "find": "Spelling", "fold": [], "foldText": ["The Rule:"], "todo": "Read the rule. Cover each word, write it, then tap to check.",
  "script": "Spell it by its syllables. Sunset. Sun: short u, a closed syllable. Set: short e, closed too. Sun, set. Read the rule. Look hard at each word, cover it, and write it. Then tap the card to check every letter."},
 dict(READ, todo="Look back through the whole book. Then try the Truth Watch below.",
  script="No new chapters today. Look back at the very last pages, when the kings and queens find the lamp-post. Then try the Truth Watch and the four questions."),
 dict(CHQ, script="Four questions today. One, a short paragraph about the whole book. Two, why the ending goes back through the wardrobe. Three, the reading skill that helped you most. Four, try a spelling and grammar checker on your writing."),
 dict(WRITE, todo="Give your response a title, and make one last improvement.",
  script="Today you get ready to publish. Clara changed one weak word and gave her response a title. Give yours a title, and make one last improvement."),
], "cards": {},
 "virtue": [
  {"t": "In Chapter 2, Mr. Tumnus tells Lucy he was going to hand her to the Witch, and says he is sorry.", "ok": True, "why": "He tells her the hard truth, even though it makes him look bad."},
  {"t": "In Chapter 4, the Witch tells Edmund she will make him a prince and then a king.", "ok": False, "why": "It is a trick. She only wants to trap him and his family."},
  {"t": "In Chapter 8, Mr. Beaver says plainly that Aslan is not safe, but he is good.", "ok": True, "why": "He tells the truth, not just what sounds nice."}]},
4: {"lookBtn": "Tap to learn about this painting of a white deer", "mods": [
 dict(WGRD, script="[warmly] Here's today's reading tip. A strong theme fits the beginning, the middle and the end of a book. Test yours one last time. " + LENS_END),
 dol("The Magician's Nephew was written by C.S. Lewis, and it tells how Narnia began. The important words in a book title get capitals. C.S. has a capital and a period for each letter."),
 {"id": "poem", "find": "Poetry", "fold": [":scope > .callout"], "todo": "Find a metaphor, a personification and a hyperbole. Say each one out loud.",
  "script": "Your last poem job: be a detective. Find a metaphor, a personification and a hyperbole in Teasdale's poem. Say each one out loud."},
 {"id": "morph", "find": "Morphology", "fold": [], "todo": "Say what one root means. Roll the dice. Say what each word means, then check.",
  "script": "Quick question: what does trans mean? Across! Here's a word that's not on the dice. Transatlantic. It means across the Atlantic Ocean, like a ship sailing from England to America. +how:morph-dice"},
 {"id": "vocab", "find": "Vocabulary", "fold": [], "todo": "Choose one word. Write one sentence about the ending and the theme.",
  "script": "Watch me use a word about the whole book. Reconciled. In the end, Edmund and his family are reconciled. One word, the whole story. Now choose your word, and write your own sentence about the ending."},
 {"id": "gram", "find": "Grammar", "fold": GRAM_FOLD, "todo": "Fix it in passes. Then tap all five words that need fixing.",
  "script": "Two passes, like an editor. the professors house was big and the children explored it. Pass one, capitals: The, and Professor, because it's his name. Pass two, apostrophes and commas: Professor's, and a comma before and. Now do your passes, and tap every word that needs fixing."},
 {"id": "spell", "find": "Spelling", "fold": [], "foldText": ["The Rule:"], "todo": "Roll the dice. Split the word and name its syllable types. Then check.",
  "script": "Dice roll: pilot! Split it after the vowel: pi, lot. Pi is open, so the i says its name. Lot is closed. Tap Roll the dice, split the word, name its syllable types, and tap Check my answer."},
 dict(READ, todo="Look back through the whole book. Then try the Truth Watch below.",
  script="No new chapters today. This is your last day with the book. Look back for your strongest proof from the beginning, the middle and the end. Then try the Truth Watch and the three questions."),
 dict(CHQ, script="Three questions to finish the book, in full sentences. One, your best theme statement. Two, the moment that mattered most to you. Three, why readers still love this book."),
 dict(WRITE, todo="Write your finished response: title, theme, proof from three chapters, closing.",
  script="Last step: publish. Clara read hers out loud one more time and changed one last word. Read yours, fix one thing, and write your finished response."),
], "cards": {},
 "virtue": [
  {"t": "In Chapter 5, the Professor asks who is more truthful, Lucy or Edmund, and Peter says, up till now, Lucy every time.", "ok": True, "why": "Peter is fair to Lucy, even though he doubts her story."},
  {"t": "Lucy tells the others about Narnia the very first time, even though they laugh.", "ok": True, "why": "She tells what really happened."},
  {"t": "In Chapter 12, Peter tells Aslan that his own anger helped Edmund go wrong.", "ok": True, "why": "He owns his part, instead of blaming only Edmund."}]},
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
        if m['id'] in ids: m['video'] = 'g3ela-30-%d-teach-%s' % (d, m['id'])

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
                out['g3ela-30-%d-teach-%s' % (d, m['id'])] = t
        for w, t in cfg['cards'].items(): out['g3ela-30-%d-say-%s' % (d, w)] = t
    return out

if __name__ == '__main__':
    import sys
    if '--count' not in sys.argv:
        for d, cfg in L.items():
            p = 'data/lesson-30-%d.json' % d
            j = json.load(io.open(p, encoding='utf-8'))
            if 'plate' in j: j['plate']['lookBtn'] = cfg['lookBtn']
            j['teach'] = {"dropTurnNotes": True, "mods": cfg['mods'], "cards": cfg['cards']}
            j['virtue'] = {"name": "honesty", "title": VTITLE, "items": cfg['virtue']}
            io.open(p, 'w', encoding='utf-8').write(json.dumps(j, ensure_ascii=False, indent=1))
            write_page('lesson-30-%d-lww.html' % d, j)
    rec = recorded(); tot = 0
    for k, t in rec.items():
        n = len(t); tot += n; print('%-32s %4d' % (k, n))
    print('recorded this week: %d / 6260 credits (%.0f%%)' % (tot, 100.0 * tot / 6260))
    io.open('/tmp/wk30_rec.json', 'w', encoding='utf-8').write(json.dumps(rec, ensure_ascii=False, indent=1))
