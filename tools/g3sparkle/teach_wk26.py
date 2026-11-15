#!/usr/bin/env python3
"""Week 26 (LWW Ch. 4-6): the Nov 10 2026 pilot fixes, as on weeks 18-24, for the new Narnia page template.
Writes DATA.teach, plate.lookBtn and DATA.virtue (Truth Watch: honesty, the Narnia unit's trait; 3 moments a day from
Ch. 4-6, checked against Planning docs/lww_text.txt) into data/lesson-25-N.json AND the page's oao-data block.
Word Study scripts are written for the Opti films: Day 1 teaches each idea; Days 2-4 show that day's activity with an
example that is not an answer anywhere in the week (platform, formless, format, landform; superior, beastly;
dangerous, beautiful, wardrobe, Professor, inquisitive), and no two films open the same way. NO RECORDINGS (Bethany, Nov 14 2026):
films are built silent with captions; scripts stay written to the budget for later.

    python tools/g3sparkle/teach_wk26.py
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
1: {"lookBtn": "Tap to learn about this painting of skaters on the ice", "mods": [
 dict(WGRD, script="[warmly] Here's this week's reading tip. In a story, almost nothing goes wrong by accident. Someone decides something first. Find the moment a character chooses, then follow what happens because of it. " + LENS_END),
 dol("The Queen smiles at Edmund, and she gives him a box of Turkish Delight. Smiles and gives are both happening now. Keep them in the same time."),
 {"id": "morph", "find": "Morphology", "fold": [":scope > .callout:not(:has(+ .dol-check-btn)):not(:has(+ .fillin-game))", ":scope > .key-concept:not(:has(+ .fillin-game))"],
  "todo": "Think about the question. Tap See what was hiding. Type the missing part of each word.",
  "script": "[curious] Some word parts tell you about shape. Form means shape. Here's a word that's not on your list. Platform. Plat means flat. So a platform is a flat shape you stand on, like at a train station. Flat shape: platform! Read the four words and their parts. Then tap See what was hiding, and type the missing parts."},
 {"id": "vocab", "find": "Vocabulary", "fold": VOCAB_FOLD, "todo": "Fill in each sentence from the word bank. Tap Check My Work. Then play the matching game.",
  "script": "Be a word detective with me. Superior. Here's the sentence. Edmund gave a very superior look, as if he were far older than Lucy. One, read the sentence: he's acting older and better. Two, look for word parts: super means above. Three, check it. Superior means acting as if you're above someone. +how:vocabcloze"},
 {"id": "gram", "find": "Grammar", "fold": GRAM_FOLD, "todo": "Tap Now check your thinking. Then tap every verb that slipped out of the past.",
  "script": "[warmly] A story can happen in the past, or right now. Once you pick a time, the verbs stay there. Listen. Edmund climbed onto the sledge and sits down. Climbed is past. Sits is now! It slipped. It should be sat. Read The Rule box, and tap Now check your thinking. Then find every verb that slipped."},
 {"id": "spell", "find": "Spelling", "fold": [], "todo": "Clap the words. Tap See the Rule. Then sort all nine words by beats.",
  "script": "Clap with me. Dan, ger, ous. Dangerous. Three claps! Each beat has one vowel sound. Now try beautiful. Beau, ti, ful. Beau has two vowel letters, but only one sound, so it's one beat. Count the sounds, not the letters. Clap the words in Group A and Group B, and tap See the Rule. Then sort the words."},
 {"id": "copia", "sel": ".spk-copia-card", "label": "Opti shows you how", "fold": [], "todo": "Write the sentence three new ways, one box at a time.",
  "script": "[warmly] Here's copia: one idea, said many ways. Let me try a different sentence first. The dwarf bowed. Box one, change the opener: On the sledge, the dwarf bowed. Box two, a stronger verb: The dwarf bent low. Box three, add a detail: The fat dwarf bowed with a smile. Now it's your turn, one box at a time. If you get stuck, tap Show one way."},
 dict(READ, todo="Read Chapter 4 in your book. Then try the Truth Watch below.",
  script="Read Chapter 4 in your book, with your lens in mind. Watch for each choice Edmund makes on the Queen's sledge. Then try the Truth Watch right after this box, and answer the three questions."),
 dict(CHQ, script="Three questions, in full sentences, with details from the book. One, what Edmund chooses, and what the narrator tells us about the Turkish Delight. Two, why the Witch wants all four children. Three, two effects of the enchanted sweets."),
 dict(WRITE, todo="Name a character's choice, the reason, and what happened because of it.",
  script="Today you draft a paragraph about a choice. Clara's first try just said Edmund made a bad choice. Her draft names the choice, gives the reason, and tells what happened next. Choice, reason, consequence. Write yours."),
], "cards": {},
 "virtue": [
  {"t": "Lucy tells Edmund all about the White Witch.", "ok": True, "why": "She tells him the truth about what she knows."},
  {"t": "Edmund says, “I'm all right,” but the book says this was not true.", "ok": False, "why": "He was feeling very sick, and he hid it."},
  {"t": "Edmund keeps it a secret that he has met the Queen.", "ok": False, "why": "Hiding what happened is not being honest."}]},
2: {"lookBtn": "Tap to learn about this painting of a country house", "mods": [
 dict(WGRD, script="[warmly] Here's today's reading tip. A choice can cost someone else. Watch what Edmund says when Peter asks him about Narnia, and who pays for it. " + LENS_END),
 dol("Edmund had been to Narnia, but he told Peter and Susan it was only a game. Been and told both point to the past, so the sentence never slips."),
 {"id": "poem", "find": "Poetry", "fold": [":scope > .callout"], "todo": "Read the poem out loud. Then answer the question.",
  "script": "[curious] Here's a poem by Robert Louis Stevenson. Read it out loud. Who is riding by, all night long, in the dark and wet? You never see him. Then answer the question."},
 {"id": "morph", "find": "Morphology", "fold": [":scope > .callout:not(:has(+ .match-game))", ":scope > .key-concept"], "todo": "Tap a word, then tap what it means. Match all four words.",
  "script": "Watch one match first. Find form, and remember: it means shape. Formless. Form, plus less, without. Formless means without a shape, like a cloud of fog. That's my match! +how:morph2"},
 {"id": "vocab", "find": "Vocabulary", "fold": [], "todo": "Tap a word, then tap its meaning. Match all four words.",
  "script": "Here's a strong word from Chapter 5. Beastly. Peter says Edmund has been perfectly beastly to Lu. Acting like a beast? Very mean! Now tap a word, then tap its meaning. Match all four."},
 {"id": "gram", "find": "Grammar", "fold": GRAM_FOLD, "todo": "Find the verb that slipped. Tap Now check your thinking. Then tap every word that is wrong.",
  "script": "Which verb slipped? Susan looked inside and sees only coats. Looked is past. Sees is now. Sees slipped! It should be saw. Find the slipped verb in each sentence, and tap Now check your thinking. Then fix the paragraph."},
 {"id": "spell", "find": "Spelling", "fold": [], "foldText": ["The Rule:"], "todo": "Read the rule. In each row, tap the word that matches.",
  "script": "Beat detective time! Which word has two beats? Wardrobe. Lamp. Enchanted. Clap them. Ward, robe: two! Lamp: one. En, chant, ed: three. Wardrobe it is. Read the rule. Then in each row, tap the one word that matches."},
 dict(READ, todo="Read Chapter 5 in your book. Then try the Truth Watch below.",
  script="Read Chapter 5 in your book, with your lens in mind. Then try the Truth Watch, and watch my video in the Read Like a Writer box before you write."),
 {"id": "rwm", "sel": ".rwm-box", "after": ":scope > .rwm-header", "label": "Opti shows you how", "fold": [],
  "script": "[warmly] Let's try all three parts with a different sentence from Chapter 5. Edmund, who was becoming a nastier person every minute, thought that he had scored a great success. Part one, read like a reader. Edmund thinks he won, but he hurt Lucy. Part two, read like a writer. Lewis tucks a fact about Edmund into the middle, with who. Part three, mimic. Here's mine: Opti, who was getting sleepier every minute, thought that one more chapter would do. Now it's your turn with the sentence about Edmund being tired. Write one sentence in each box."},
 dict(CHQ, script="Three questions, in full sentences. One, what Edmund says, and what it does to Lucy. Two, how Peter answers him. Three, the Professor's main argument about Lucy's story."),
 dict(WRITE, todo="Add one connecting word, like because or as a result.",
  script="Today you make the link clearer. Clara's draft was three short sentences. Her revision joins the choice to what it causes, with words like because. Add one connecting word to your paragraph."),
], "cards": {},
 "virtue": [
  {"t": "Edmund says he and Lucy were only pretending.", "ok": False, "why": "That was a lie. He had been to Narnia too."},
  {"t": "Peter and Susan tell the Professor the whole story.", "ok": True, "why": "They are honest about what has been happening."},
  {"t": "Peter says that, until now, he would always have said Lucy was the more truthful one.", "ok": True, "why": "He tells the truth about Lucy, even after an argument."}]},
3: {"lookBtn": "Tap to learn about this picture of robins", "mods": [
 dict(WGRD, script="[warmly] Here's today's reading tip. Some choices are brave. When the children find Mr. Tumnus's cave, they have to choose: go on, or go home? Watch who wants what. " + LENS_END),
 dol("When the children climbed into the wardrobe, they pushed past the coats and stepped into the snow. Climbed, pushed and stepped all stay in the past."),
 {"id": "morph", "find": "Morphology", "fold": [":scope > .callout:not(:has(+ .fillin-game))", ":scope > .key-concept"], "todo": "Say the parts out loud. Type the whole word in each box. Tap Check My Answers.",
  "script": "Snap the parts together. Form. At. Format! The format of a page is its shape: where the title goes, and where the words go. +how:morph3"},
 {"id": "vocab", "find": "Vocabulary", "fold": [], "todo": "Read each sentence. Pick the word that fits.",
  "script": "Try each word in the blank, and keep the one that makes sense. Here's my sentence. Edmund gave Lucy a blank look, as if he were much older. Beastly? Hmm, no. Superior? Yes! Now pick the word that fits each sentence."},
 {"id": "gram", "find": "Grammar", "fold": GRAM_FOLD, "todo": "Read the before and after. Rewrite the sentences in the past tense.",
  "script": "Let's move a sentence into the past. The children run upstairs and hide in the wardrobe. Run becomes ran. Hide becomes hid. The children ran upstairs and hid in the wardrobe. Read the before and after. Then rewrite the two sentences so every verb is in the past."},
 {"id": "spell", "find": "Spelling", "fold": [], "foldText": ["The Rule:"], "todo": "Read the rule. Say each word in chunks. Tap the card to see the beats.",
  "script": "Let's split a long word into chunks. Professor. Pro, fes, sor. Three chunks! Say each chunk, then push them back together: Professor. Read the rule. Then say each word in chunks, and tap the card to check."},
 dict(READ, todo="Read Chapter 6 in your book. Then try the Truth Watch below.",
  script="Read Chapter 6 in your book, with your lens in mind. Watch what the children choose at Mr. Tumnus's cave. Then try the Truth Watch and the three questions."),
 dict(CHQ, script="Three questions, in full sentences. One, three details about Mr. Tumnus's cave. Two, Lucy's reason for helping him, and whether it convinces you. Three, why Lewis might choose a robin as a guide."),
 dict(WRITE, todo="Put your opening, evidence and closing together into one paragraph.",
  script="Today you put it all together. Clara had three separate pieces. She joined them into one paragraph with words like because and as a result. Put yours together the same way."),
], "cards": {},
 "virtue": [
  {"t": "Edmund pretends he has never been in the wood before.", "ok": False, "why": "He had been there. Pretending is not honest."},
  {"t": "Peter says out loud that Edmund made out Lucy was telling lies.", "ok": True, "why": "He tells the truth about what Edmund did."},
  {"t": "Lucy says the Faun is in trouble because he helped her, so they must try to rescue him.", "ok": True, "why": "She owns up to her part, even though it means danger."}]},
4: {"lookBtn": "Tap to learn about this painting of a snowy pine tree", "mods": [
 dict(WGRD, script="[warmly] Here's today's reading tip. Look back and connect the dots. One choice on the Queen's sledge leads to trouble chapters later. Follow it all the way. " + LENS_END),
 dol("The Witch spoke kindly and promised Edmund a crown, but Lucy said she was a terrible person. Spoke, promised and said all stay in the past."),
 {"id": "poem", "find": "Poetry", "fold": [":scope > .callout"], "todo": "Read the poem again. Then answer the question out loud.",
  "script": "Here's Stevenson's poem again. He never says the word wind after the second line. So how do you know the rider is the wind? Read it out loud again, and answer out loud."},
 {"id": "morph", "find": "Morphology", "fold": [":scope > .key-concept"], "foldText": ["Before you roll"], "todo": "Tap Roll the Dice. Say what the word means. Tap Check My Thinking. Roll all six words.",
  "script": "Quick! What does form mean? Shape! Here's a word that's not on the dice. Landform. A landform is a shape of the land, like a hill or a valley. Now tap Roll the Dice. Say what each word means, and tap Check My Thinking. Roll all six."},
 {"id": "vocab", "find": "Vocabulary", "fold": [], "todo": "Choose one word. Write one sentence about Chapters 4 to 6.",
  "script": "Here's how I'd use a word about the story. Superior. Edmund gave Lucy a superior look when he said they were only pretending. One word, one moment. Now choose one of your words and write your own sentence about Chapters 4 to 6."},
 {"id": "gram", "find": "Grammar", "fold": GRAM_FOLD, "todo": "Tap Check yourself. Tap every word that needs fixing. Then tap See the answers.",
  "script": "Three passes, like an editor. Lucy said the queen was terrible and edmund feels sick. Pass one, capitals: Queen and Edmund. Pass two, verbs: feels slipped, so it becomes felt. Pass three, a comma before and. Now do your passes, and tap every word that needs fixing."},
 {"id": "spell", "find": "Spelling", "fold": [], "foldText": ["The Rule:"], "todo": "Tap Roll the dice. Split the word and say how you knew. Tap Check my answer.",
  "script": "Here's my roll. Inquisitive. In, quis, i, tive. Four beats! How did I know? Four vowel sounds. Tap Roll the dice, split the word out loud, and say how you knew. Then tap Check my answer."},
 dict(READ, todo="Look back at Chapters 4 to 6. Then try the Truth Watch below.",
  script="No new chapters today. Look back at Chapters 4 to 6, and follow Edmund's choice to the trouble it causes. Then try the Truth Watch and the three questions."),
 dict(CHQ, script="Three questions to finish the week, in full sentences. One, what Edmund's choice shows. Two, the most important consequence, and why it matters. Three, one example of how Lewis makes the choice and consequence easy to see."),
 dict(WRITE, todo="Swap one weak word for a stronger one. Write your final version.",
  script="Last step: polish. Clara found one weak word, bad, and changed it to dangerous. Find one weak word in your paragraph, and choose a stronger one."),
], "cards": {},
 "virtue": [
  {"t": "Edmund says, “You can't always believe what Fauns say.”", "ok": False, "why": "He says it to cover up that he has met the Queen."},
  {"t": "Susan says she has a horrid feeling that Lu is right.", "ok": True, "why": "She says what she really thinks, even though she wants to go home."},
  {"t": "The Professor says this is a very strange house, and even he knows very little about it.", "ok": True, "why": "He admits what he does not know."}]},
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
        if m['id'] in ids: m['video'] = 'g3ela-26-%d-teach-%s' % (d, m['id'])

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
                out['g3ela-26-%d-teach-%s' % (d, m['id'])] = t
        for w, t in cfg['cards'].items(): out['g3ela-26-%d-say-%s' % (d, w)] = t
    return out

if __name__ == '__main__':
    import sys
    for d, cfg in L.items():
        p = 'data/lesson-26-%d.json' % d
        j = json.load(io.open(p, encoding='utf-8'))
        if 'plate' in j: j['plate']['lookBtn'] = cfg['lookBtn']
        j['teach'] = {"dropTurnNotes": True, "mods": cfg['mods'], "cards": cfg['cards']}
        j['virtue'] = {"name": "honesty", "title": VTITLE, "items": cfg['virtue']}
        io.open(p, 'w', encoding='utf-8').write(json.dumps(j, ensure_ascii=False, indent=1))
        write_page('lesson-26-%d-lww.html' % d, j)
    rec = recorded(); tot = 0
    for k, t in rec.items():
        n = len(t); tot += n; print('%-32s %4d' % (k, n))
    print('recorded this week: %d / 6260 credits (%.0f%%)' % (tot, 100.0 * tot / 6260))
    io.open('/tmp/wk26_rec.json', 'w', encoding='utf-8').write(json.dumps(rec, ensure_ascii=False, indent=1))
