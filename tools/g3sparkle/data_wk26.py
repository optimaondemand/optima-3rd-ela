#!/usr/bin/env python3
"""Week 26 DATA (The Lion, the Witch and the Wardrobe, Ch. 4-6): 26.1-26.4 + fluency.
Every book line checked against Planning docs/lww_text.txt (nothing past Ch. 6). Turkish Delight Box items use only this
week's word study (beats in long school words; verb tense) and none is an answer elsewhere on the week's pages
(compare evidence information explain character education detail summary conversation predict important sequence
imagination form uniform reform transform inform formation deform) or a film example (see teach_wk26.py)."""
import json, io, os
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'data')
S = "<strong>"; E = "</strong>"
def C(x): return S + x + E
def dol(a_raw, a_fixed, a_why, b_raw, b_fixed, b_why):
    return {"a": {"raw": a_raw, "fixed": a_fixed, "why": a_why}, "b": {"raw": b_raw, "fixed": b_fixed, "why": b_why}}
GLOSS = [
 {"w": "consequence", "m": "what happens because of a choice", "key": True},
 {"w": "tense", "m": "the time a verb tells about: past (walked) or present (walks)", "key": True},
 {"w": "verb", "m": "an action word, like ate, walks or said"},
 {"w": "syllable", "m": "one beat in a word. Ev-i-dence has three syllables."},
 {"w": "Turkish Delight", "cs": True, "m": "a real soft, sweet candy, often dusted with powdered sugar"},
 {"w": "literary response", "m": "writing that tells what you think about a book and proves it with details from the book"},
 {"w": "honesty", "m": "telling the truth, even when it is hard", "key": True},
]
NOTES_COMMON = {
 "wordParts": "The root form means shape. uniform = one shape for everyone. transform = to change shape.",
 "grammar": "Keep your verbs in the same time. If a story starts in the past (walked, ate), every verb stays in the past.",
 "spelling": "Every beat in a word has one vowel sound. Count the sounds, not the letters: de-tail has two beats."
}
VOC = [["enchanted", "under a magic spell; bewitched"], ["dominions", "the lands ruled by someone"], ["wretched", "very unhappy or miserable"]]
BEAT = {n: {"id": str(n), "label": "%d beats" % n, "ic": "👏" * min(n, 3) + ("+" if n > 3 else "")} for n in (2, 3, 4, 5)}
TENSE = {"stays": {"id": "stays", "label": "Stays in one time", "ic": "✅"}, "slips": {"id": "slips", "label": "A verb slips", "ic": "🌀"}}
def it_beat(w, n, split, bins):
    return {"t": w, "bin": str(n), "why": "%s: %d beats." % (split, n),
            "miss": {str(b): "Clap it again, slowly. Count one clap for each vowel sound you hear." for b in bins if b != n}}
def it_tense(t, ok, why):
    right = "stays" if ok else "slips"
    return {"t": t, "bin": right, "why": why,
            "miss": {("slips" if ok else "stays"): ("Look at every verb. Are they all in the same time?" if ok else "Find each verb. Is one of them in a different time from the others?")}}
GAME = {"type": "delight", "title": "The Turkish Delight Box",
        "sub": "Every right answer puts a sweet in the Queen's box.",
        "todo": "Read what is on the sweet. Tap the right answer. A right answer adds a sweet to the box.",
        "win": "Today's 8 sweets are in the box. Come back next lesson to fill more.",
        "winWeek": "The box is full! Unlike Edmund, you earned every sweet."}
LOOK1 = ("This week's game is a box of Turkish Delight, like the one the Queen gives Edmund in Chapter 4. "
         "Each sweet comes with a long school word. Clap it and count the beats, then tap how many beats it has. "
         "Each right answer puts one sweet in the box. Over four days you fill the whole box.")
LOOK2 = ("Today each sweet comes with a sentence. Read every verb. If all the verbs stay in the same time, tap Stays in one time. "
         "If one verb slips into a different time, tap A verb slips. The sweets from earlier days are still in the box.")
LOOK3 = ("Clap each word on the sweet and count the beats. Today some words have five! Each right answer adds a sweet to the box.")
def note(title, text, before="Read:|Look Back"):
    return [{"id": "world", "kind": "info", "tab": "reading", "after": before, "before": True, "icon": "🌍",
             "title": "World Notes: " + title, "sub": "A real thing behind the story",
             "todo": "Read the note. Then read the chapter with your lens in mind.", "text": text}]
L = {}
L["26-1"] = {
 "connector": "What is the most delicious thing you have ever tasted? Today Edmund tastes something he can't stop eating, and it changes his choices. Watch for each choice Edmund makes in Chapter 4, and what it leads to.",
 "writingFocus": "literary response",
 "dol": dol("the queen gives edmund a hot drink and he feels warm",
   C("T")+"he "+C("Q")+"ueen gives "+C("E")+"dmund a hot drink"+C(",")+" and he feels warm"+C("."),
   "The starts the sentence. Queen is used as her name, and Edmund is a name. A comma goes before and. Gives and feels are both present tense.",
   "edmund eats the turkish delight and he wants more",
   C("E")+"dmund eats the "+C("T")+"urkish "+C("D")+"elight"+C(",")+" and he wants more"+C("."),
   "Edmund is a name. Turkish Delight is the name of a sweet. A comma goes before and. Eats and wants are both present tense."),
 "hints": {
  "mfill1": {"h1": "The meaning says one shape. Type the root that means shape.", "why": "uni + form = uniform: one shape for everyone."},
  "mfill2": {"h1": "To shape again. Which root means shape?", "why": "re + form = reform: to shape again."},
  "mfill3": {"h1": "To change across. Look at the table for the root.", "why": "trans + form = transform: to change shape."},
  "mfill4": {"h1": "Every word in the table hides the same root.", "why": "in + form = inform: to shape what someone knows."},
  "vcloze1": {"h1": "The Turkish Delight had magic in it. Find the word for under a spell.", "why": "Enchanted means under a magic spell."},
  "vcloze2": {"h1": "The Queen means the lands she rules. Find that word.", "why": "Dominions are the lands someone rules."},
  "vcloze3": {"h1": "Lucy was very unhappy. Find the word for very unhappy.", "why": "Wretched means very unhappy."}
 },
 "miss": {"match": {
   "enchanted": "Enchanted is about magic. Look for the meaning with a spell.",
   "dominions": "Dominions are places. Look for the meaning about lands.",
   "wretched": "Wretched is a feeling. Look for the unhappy meaning."}},
 "flags": {"journal-q1": {"quote": False, "count": 1}, "journal-q2": {"quote": False, "count": 1}, "journal-q3": {"quote": False, "count": 2}},
 "copia": {"look": "One plain sentence from Chapter 4, and three empty boxes. Each box asks you to say the same idea in a new way.",
   "todo": "Rewrite the sentence three ways, one box at a time. Tap Show one way if you get stuck.",
   "seed": "Edmund <b>ate</b> the Turkish Delight.",
   "eg": ["On the Queen's sledge, Edmund ate the Turkish Delight.",
          "Edmund <i>gobbled</i> the Turkish Delight.",
          "Edmund ate the sweet, soft Turkish Delight."]},
 "wordgame": dict(GAME, look=LOOK1, stepTitle="How many beats?", bins=[BEAT[n] for n in (2, 3, 4)], items=[
   it_beat("topic", 2, "top·ic", (2, 3, 4)), it_beat("example", 3, "ex·am·ple", (2, 3, 4)), it_beat("punctuation", 4, "punc·tu·a·tion", (2, 3, 4)),
   it_beat("reason", 2, "rea·son", (2, 3, 4)), it_beat("paragraph", 3, "par·a·graph", (2, 3, 4)), it_beat("observation", 4, "ob·ser·va·tion", (2, 3, 4)),
   it_beat("opinion", 3, "o·pin·ion", (2, 3, 4)), it_beat("question", 2, "ques·tion", (2, 3, 4))]),
 "glossary": GLOSS, "sayWords": [],
 "cards": note("Turkish Delight", [
   "Turkish delight is a real candy. It is soft and chewy, made with sugar and starch, and often dusted with powdered sugar.",
   "It comes from Turkey, where people have made it for hundreds of years.",
   "In the story, the Queen's Turkish Delight is enchanted. Real Turkish delight is just a sweet treat."]),
 "transcripts": {"welcome": "Hi, it's Opti. Edmund tastes something he can't stop eating. Watch each choice he makes in Chapter 4, and what it leads to.",
  "guide1": "Word work first: a root that means shape, verbs that stay in one time, and beats in long words.",
  "guide2": "Read Chapter 4 with your lens. Then answer three questions.",
  "guide3": "Today you draft a paragraph about a character's choice."},
 "notes": dict(NOTES_COMMON, wgrd="Name the choice, follow what happens because of it, and ask what the character knew when he chose.", vocab=VOC)
}
L["26-2"] = {
 "connector": "Lucy and Edmund are back, and this time Edmund has been to Narnia too. Will he tell the truth? In Chapter 5, watch the choice he makes when Peter asks him, and what it costs Lucy.",
 "writingFocus": "literary response",
 "dol": dol("edmund gave lucy a superior look but he said nothing kind",
   C("E")+"dmund gave "+C("L")+"ucy a superior look"+C(",")+" but he said nothing kind"+C("."),
   "Edmund and Lucy are names. A comma goes before but, because it joins two complete thoughts. Gave and said are both past tense.",
   "peter went to the professor and he told him the whole story",
   C("P")+"eter went to the "+C("P")+"rofessor"+C(",")+" and he told him the whole story"+C("."),
   "Peter is a name, and the Professor is used as his name. A comma goes before and. Went and told are both past tense."),
 "hints": {},
 "miss": {"match": {
   "enchanted": "Enchanted is about magic. Look for the meaning with a spell.",
   "dominions": "Dominions are places. Look for the meaning about lands.",
   "wretched": "Wretched is a feeling. Look for the unhappy meaning.",
   "treachery": "Treachery is about trust. Look for the meaning about betraying someone."}},
 "flags": {"journal-q1": {"quote": False, "count": 1}, "journal-q2": {"quote": False, "count": 1}, "journal-q3": {"quote": False, "count": 1}},
 "wordgame": dict(GAME, look=LOOK2, stepTitle="Stays, or slips?", bins=[TENSE["stays"], TENSE["slips"]], items=[
   it_tense("The Queen gave Edmund a box, and he opened it.", True, "gave, opened: both past."),
   it_tense("Edmund ate the Turkish Delight and wants more.", False, "ate is past, but wants is now. It should be wanted."),
   it_tense("Lucy gave Edmund one look and rushed out of the room.", True, "gave, rushed: both past."),
   it_tense("Peter turned on Edmund and tells him to shut up.", False, "turned is past, but tells is now. It should be told."),
   it_tense("The Professor listens and asked them a question.", False, "listens is now, but asked is past."),
   it_tense("The children put on the coats and walked into the forest.", True, "put, walked: both past."),
   it_tense("Susan wanted to go home, but Lucy says they must help.", False, "wanted is past, but says is now. It should be said."),
   it_tense("The robin flew from tree to tree, and the children followed it.", True, "flew, followed: both past.")]),
 "glossary": GLOSS, "sayWords": [],
 "cards": note("Old Country Houses", [
   "The Professor's house is a big, old country house. In England, some very old houses are so famous that people come to see them.",
   "In Chapter 5, the housekeeper, Mrs. Macready, shows groups of visitors around the house.",
   "That is why the children have to hide when the visitors come, and why they end up in the wardrobe!"]),
 "transcripts": {"welcome": "Hi, it's Opti. Edmund has been to Narnia too. Will he tell the truth? Watch his choice in Chapter 5.",
  "guide1": "Word work: match form words, fix verbs that slip, and hear the beats.",
  "guide2": "Read Chapter 5. Then try my video in Read Like a Writer.",
  "guide3": "Today you make the link between a choice and what it causes clearer."},
 "notes": dict(NOTES_COMMON, wgrd="A choice can cost someone else. Edmund's lie made Lucy look like she was not telling the truth.", vocab=VOC + [["treachery", "betraying someone's trust in a serious way"]])
}
L["26-3"] = {
 "connector": "All four children step into Narnia together. Then they find Mr. Tumnus's cave broken and empty. In Chapter 6, watch what they choose to do, and who wants to turn back.",
 "writingFocus": "literary response",
 "dol": dol("when the children reached the cave they saw that the door was broken",
   C("W")+"hen the children reached the cave"+C(",")+" they saw that the door was broken"+C("."),
   "When starts the part that cannot stand alone, so a comma goes after cave. Reached and saw are both past tense.",
   "when lucy saw the robin she asked it where mr tumnus was",
   C("W")+"hen "+C("L")+"ucy saw the robin"+C(",")+" she asked it where "+C("M")+"r"+C(".")+" "+C("T")+"umnus was"+C("."),
   "When starts the part that cannot stand alone, so a comma goes after robin. Lucy and Mr. Tumnus are names. Saw and asked are both past tense."),
 "hints": {
  "mfill1": {"h1": "Just the root itself. Which root means shape?", "why": "form: a shape or structure."},
  "mfill2": {"h1": "uni, then form. Push them together.", "why": "uni + form = uniform."},
  "mfill3": {"h1": "re, then form. Push them together.", "why": "re + form = reform."},
  "mfill4": {"h1": "trans, then form. Push them together.", "why": "trans + form = transform."}
 },
 "flags": {"journal-q1": {"quote": False, "count": 3}, "journal-q2": {"quote": False, "count": 1}, "journal-q3": {"quote": False, "count": 1}},
 "wordgame": dict(GAME, look=LOOK3, stepTitle="How many beats?", bins=[BEAT[n] for n in (2, 3, 4, 5)], items=[
   it_beat("author", 2, "au·thor", (2, 3, 4, 5)), it_beat("dialogue", 3, "di·a·logue", (2, 3, 4, 5)), it_beat("definition", 4, "def·i·ni·tion", (2, 3, 4, 5)),
   it_beat("vocabulary", 5, "vo·cab·u·lar·y", (2, 3, 4, 5)), it_beat("pronoun", 2, "pro·noun", (2, 3, 4, 5)), it_beat("syllable", 3, "syl·la·ble", (2, 3, 4, 5)),
   it_beat("illustration", 4, "il·lus·tra·tion", (2, 3, 4, 5)), it_beat("investigation", 5, "in·ves·ti·ga·tion", (2, 3, 4, 5))]),
 "glossary": GLOSS, "sayWords": [],
 "cards": note("Robins in Winter", [
   "The robin in Narnia is a European robin: a small brown bird with an orange-red breast.",
   "In Britain, robins stay all winter and sing even in the cold, so people often see them in the snow.",
   "That is one reason robins are on so many British Christmas cards."]),
 "transcripts": {"welcome": "Hi, it's Opti. All four children are in Narnia now. Watch what they choose when they find Mr. Tumnus's cave.",
  "guide1": "Word work: build form words, keep every verb in the past, and split long words into beats.",
  "guide2": "Read Chapter 6. Then answer three questions.",
  "guide3": "Today you put your whole paragraph together."},
 "notes": dict(NOTES_COMMON, wgrd="Some choices are brave. Lucy chooses to help Mr. Tumnus because he got into trouble for helping her.", vocab=VOC)
}
L["26-4"] = {
 "connector": "No new chapters today. Look back at Chapters 4 to 6 and follow Edmund's choice to the trouble it causes. Today you finish your paragraph about a character's choice.",
 "writingFocus": "literary response",
 "dol": dol("edmund said he was all right but he was feeling very sick",
   C("E")+"dmund said he was all right"+C(",")+" but he was feeling very sick"+C("."),
   "Edmund is a name. A comma goes before but, because it joins two complete thoughts. Said and was are both past tense.",
   "lucy led the way and she found the faun's cave",
   C("L")+"ucy led the way"+C(",")+" and she found the "+C("F")+"aun's cave"+C("."),
   "Lucy is a name, and the Faun is used as his name. A comma goes before and. Led and found are both past tense."),
 "hints": {},
 "flags": {"journal-q1": {"quote": False, "count": 1}, "journal-q2": {"quote": False, "count": 1}, "journal-q3": {"quote": False, "count": 1}},
 "wordgame": dict(GAME, look=LOOK2, stepTitle="Stays, or slips?", bins=[TENSE["stays"], TENSE["slips"]], items=[
   it_tense("I opened the box and see a sweet.", False, "opened is past, but see is now. It should be saw."),
   it_tense("We walked to the park and played.", True, "walked, played: both past."),
   it_tense("She reads a book and writes a note.", True, "reads, writes: both now. That stays in one time too."),
   it_tense("The dog runs outside and barked.", False, "runs is now, but barked is past."),
   it_tense("My brother wakes up early and eats toast.", True, "wakes, eats: both now."),
   it_tense("It snowed all night, and the trees look white.", False, "snowed is past, but look is now. It should be looked."),
   it_tense("Dad cooked dinner and we ate together.", True, "cooked, ate: both past."),
   it_tense("The bell rings and everyone hurried in.", False, "rings is now, but hurried is past.")]),
 "glossary": GLOSS, "sayWords": [],
 "cards": note("Arctic Explorers", [
   "In Chapter 6, Lucy says they can pretend to be Arctic explorers.",
   "The Arctic is the icy land and sea around the North Pole.",
   "Explorers who went there wore thick fur clothes, a lot like the fur coats the children borrow from the wardrobe."], before="Look Back"),
 "transcripts": {"welcome": "Hi, it's Opti. Look back at Chapters 4 to 6 and follow Edmund's choice to the trouble it causes.",
  "guide1": "Word work: roll form words, fix a passage in passes, and roll for beats.",
  "guide2": "Look back at Chapters 4 to 6 for your best evidence.",
  "guide3": "Today you polish your paragraph with a stronger word."},
 "notes": dict(NOTES_COMMON, wgrd="A choice leads to a consequence. Edmund chose to keep his secret, and it put his whole family in danger.", vocab=VOC)
}
FLU = {"connector": "This week's passage is from Chapter 4: Edmund eating Turkish Delight on the Queen's sledge. Read it three times. The last time, read the long sentence in one smooth run.",
 "howto": True,
 "transcripts": {"welcome": "Hi, it's Opti. This week's passage is Edmund on the Queen's sledge. Read it three times. First, get every word right. Next, make it smooth. Then read the long sentence in one smooth run, the way Edmund keeps on eating."}}
if __name__ == '__main__':
    import sys
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    try:
        from plates_wk26 import PLATES as P
        for k, p in P.items(): L[k]["plate"] = p
    except ImportError: print('no plates yet')
    for k, v in L.items():
        io.open(os.path.join(OUT, 'lesson-%s.json' % k), 'w', encoding='utf-8').write(json.dumps(v, ensure_ascii=False, indent=1)); print(k)
    io.open(os.path.join(OUT, 'lesson-26-fluency.json'), 'w', encoding='utf-8').write(json.dumps(FLU, ensure_ascii=False, indent=1))
