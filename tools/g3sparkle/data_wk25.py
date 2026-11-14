#!/usr/bin/env python3
"""Week 25 DATA (The Lion, the Witch and the Wardrobe, Ch. 1-3): 25.1-25.4 + fluency.
Every book line checked against Planning docs/lww_text.txt (Ch. 1-3 only; nothing later). Through the Wardrobe items use
only this week's spelling (the schwa) and none is an answer elsewhere on the week's pages (about problem afraid moment along
season await forgotten open lesson pencil circus banana alone button family travel wagon animal) or a film example
(Narnia, Edmund, Susan, apart, lion, Tumnus; see teach_wk25.py)."""
import json, io, os
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'data')
S = "<strong>"; E = "</strong>"
def C(x): return S + x + E
def dol(a_raw, a_fixed, a_why, b_raw, b_fixed, b_why):
    return {"a": {"raw": a_raw, "fixed": a_fixed, "why": a_why}, "b": {"raw": b_raw, "fixed": b_fixed, "why": b_why}}

GLOSS = [
 {"w": "setting", "m": "where and when a story happens", "key": True},
 {"w": "fantasy", "m": "a story with magic or things that could not happen in real life"},
 {"w": "schwa", "m": "the lazy uh sound in a quiet beat of a long word. Any vowel letter can make it.", "key": True},
 {"w": "syllable", "m": "one beat in a word. Lem-on has two syllables."},
 {"w": "complex sentence", "m": "a sentence with a main idea and a part that cannot stand alone, joined by a word like when, because or although", "key": True},
 {"w": "dependent", "m": "needs another part to make sense. A dependent part cannot stand alone as a sentence."},
 {"w": "personification", "m": "talking about something that is not a person as if it were a person", "key": True},
 {"w": "Faun", "cs": True, "m": "a creature from very old stories. Stories say a faun is half person and half goat."},
 {"w": "literary response", "m": "writing that tells what you think about a book and proves it with details from the book"},
 {"w": "honesty", "m": "telling the truth, even when it is hard", "key": True},
]
NOTES_COMMON = {
 "wordParts": "The word part tele means far. telephone = sound from far away. telescope = a tool for looking far away.",
 "grammar": "A complex sentence has a main idea and a part that cannot stand alone, joined by a word like when, because or although. When that part comes first, put a comma after it.",
 "spelling": "The schwa is a lazy uh sound in a quiet beat of a long word. Any vowel can make it: the a in sofa, the e in seven, the o in lemon."
}
VOC = [["inquisitive", "eager to find out; very curious"], ["melancholy", "a deep feeling of sadness or gloom"], ["peculiar", "strange or unusual in a hard-to-explain way"]]
BIN = {v: {"id": v, "label": "%s says uh" % v, "ic": v} for v in "aeiou"}
def miss_for(right, bins, sentence=False):
    m = {}
    for b in bins:
        if b == right: continue
        m[b] = ("Say the word with the missing letter out loud. Which letter would make that lazy uh?" if sentence else
                "Say the word slowly and clap it. Find the quiet, lazy beat. Which vowel letter is in that beat?")
    return m
def it(t, right, why, bins, sentence=False):
    return {"t": t, "bin": right, "why": why, "miss": miss_for(right, bins, sentence)}
B1 = ["a", "e", "o"]; B2 = ["a", "e", "o", "i"]; B3 = ["a", "o", "i", "u"]; B4 = ["a", "e", "o", "u"]
GAME = {"type": "wardrobe", "title": "Through the Wardrobe",
        "sub": "Every right answer pushes a fur coat aside. What is behind them?",
        "todo": "Read the word on the coat. Tap the vowel that makes its lazy schwa sound. A right answer pushes the coat aside.",
        "stepTitle": "Which vowel says uh?",
        "win": "All the coats are pushed aside, and the lamp-post is shining. Come back next lesson; more snow is falling.",
        "winWeek": "You made it all the way through the wardrobe. The lamp-post is shining as bright as it can!"}
LOOK1 = ("This week’s game is the inside of a big old wardrobe, full of fur coats, like the one Lucy steps into. "
         "Each coat has a word on it. Every word has one quiet, lazy beat that says uh: that is the schwa. "
         "Say the word, find the lazy beat, then tap the vowel letter that makes it. Each right answer pushes one coat aside. "
         "Push all of them aside to see what is behind.")
LOOK = ("Each coat has a word with a lazy uh beat. Say the word, then tap the vowel that makes the uh. "
        "Each right answer pushes one coat aside. The snow from earlier days is still falling behind the coats.")
LOOK4 = ("Today each coat has a sentence with one letter missing. The missing letter makes the lazy uh sound. "
         "Say the word out loud, then tap the vowel that belongs in the blank. Each right answer pushes one coat aside.")
def note(title, text, before="Read:|Look Back"):
    return [{"id": "world", "kind": "info", "tab": "reading", "after": before, "before": True, "icon": "🌍",
             "title": "World Notes: " + title, "sub": "A real thing behind the story",
             "todo": "Read the note. Then read the chapters with your lens in mind.", "text": text}]

L = {}
L["25-1"] = {
 "connector": "What’s at the back of your closet? A wall, right? Today a girl named Lucy opens an old wardrobe, walks in, and keeps walking. Lewis builds a whole new world in one chapter. Look for the details that make it feel real.",
 "writingFocus": "literary response",
 "dol": dol("lucy looked back at the wardrobe and she could still see the empty room",
   C("L")+"ucy looked back at the wardrobe"+C(",")+" and she could still see the empty room"+C("."),
   "Lucy is a name and starts the sentence. A comma goes before and, because and joins two complete thoughts. A period ends it.",
   "the faun had a red muffler and his skin was rather reddish too",
   C("T")+"he "+C("F")+"aun had a red muffler"+C(",")+" and his skin was rather reddish too"+C("."),
   "The starts the sentence. Faun gets a capital because the Faun is used as his name. A comma goes before and. A period ends it."),
 "hints": {
  "mfill1": {"h1": "Say tele, then phone. Now say them fast as one word.", "why": "tele + phone = telephone: sound from far away."},
  "mfill2": {"h1": "Say tele, then vision. Push them together.", "why": "tele + vision = television: seeing from far away."},
  "mfill3": {"h1": "Say tele, then scope. Type them as one word.", "why": "tele + scope = telescope: a tool for looking far away."},
  "mfill4": {"h1": "Say tele, then gram. Push them together.", "why": "tele + gram = telegram: a message written from far away."},
  "vcloze1": {"h1": "Lucy wants to find out more. Find the word that means very curious.", "why": "Inquisitive means eager to find out."},
  "vcloze2": {"h1": "His voice sounds sad. Find the word for a deep, sad feeling.", "why": "Melancholy is a deep feeling of sadness."},
  "vcloze3": {"h1": "A lamp-post in a forest is strange. Find the word for strange.", "why": "Peculiar means strange or unusual."}
 },
 "miss": {"match": {
   "inquisitive": "Inquisitive is about wanting to know more. Look for the meaning about finding out.",
   "melancholy": "Melancholy is a feeling. Which meaning is a feeling?",
   "peculiar": "Peculiar describes a thing that seems odd. Look for the meaning about strange things."}},
 "flags": {"journal-q1": {"quote": False, "count": 2}, "journal-q2": {"quote": False, "count": 2}, "journal-q3": {"quote": False, "count": 1}},
 "copia": {"look": "One plain sentence from Chapter 1, and three empty boxes. Each box asks you to say the same idea in a new way.",
   "todo": "Rewrite the sentence three ways, one box at a time. Tap Show one way if you get stuck.",
   "seed": "She began to <b>walk</b> forward over the snow.",
   "eg": ["Through the dark wood, she began to walk forward over the snow.",
          "She began to <i>crunch</i> forward over the snow.",
          "She began to walk forward over the cold, crunchy snow."]},
 "wordgame": dict(GAME, look=LOOK1, bins=[BIN[b] for b in B1], items=[
   it("sofa", "a", "so·fa: the a in the last beat says uh.", B1),
   it("chicken", "e", "chick·en: the e in the last beat says uh.", B1),
   it("lemon", "o", "lem·on: the o in the last beat says uh.", B1),
   it("zebra", "a", "ze·bra: the a at the end says uh.", B1),
   it("kitten", "e", "kit·ten: the e says uh.", B1),
   it("bacon", "o", "ba·con: the o says uh.", B1),
   it("pizza", "a", "piz·za: the a at the end says uh.", B1),
   it("seven", "e", "sev·en: the e in the last beat says uh.", B1),
 ]),
 "glossary": GLOSS, "sayWords": [],
 "cards": note("Sent Away from London", [
   "The story begins during a real war, World War II.",
   "In 1939, many children in Britain were sent away from big cities like London to stay in the country, where they were safer from air raids. An air raid is an attack by planes dropping bombs.",
   "That is why Peter, Susan, Edmund and Lucy go to stay at the old Professor’s house."]),
 "transcripts": {
  "welcome": "Hi, it’s Opti. A new book starts today! Lucy opens a wardrobe and keeps on walking. Look for the details that make her new world feel real.",
  "guide1": "Word work first: a word part that means far, a new kind of sentence, and a lazy vowel sound.",
  "guide2": "Read Chapter 1 with your lens. Then answer three questions.",
  "guide3": "Today you brainstorm details about Narnia for your writing."
 },
 "notes": dict(NOTES_COMMON, wgrd="In a fantasy story, slow down and notice how the author builds the world: the weather, the light, and what could never happen at home.", vocab=VOC)
}
L["25-2"] = {
 "connector": "Lucy had tea with a Faun! But when she comes back, the others don’t believe her. Today you read Chapters 2 and 3. Notice how Narnia feels inside Mr. Tumnus’s warm cave, and how different it feels when Edmund steps through.",
 "writingFocus": "literary response",
 "dol": dol("the dwarf cracked his whip and the bells on the sledge jingled",
   C("T")+"he dwarf cracked his whip"+C(",")+" and the bells on the sledge jingled"+C("."),
   "The starts the sentence. A comma goes before and, because and joins two complete thoughts. A period ends it.",
   "the queen wore a golden crown and she held a long golden wand",
   C("T")+"he "+C("Q")+"ueen wore a golden crown"+C(",")+" and she held a long golden wand"+C("."),
   "The starts the sentence. Queen gets a capital because it is used as her name. A comma goes before and. A period ends it."),
 "hints": {},
 "miss": {"match": {
   "inquisitive": "Inquisitive is about wanting to know more. Look for the meaning about finding out.",
   "melancholy": "Melancholy is a feeling. Which meaning is a sad feeling?",
   "peculiar": "Peculiar describes a thing that seems odd. Look for the meaning about strange things.",
   "betray": "To betray is something a person does to someone who trusted them. Look for that meaning."}},
 "flags": {"journal-q1": {"quote": False, "count": 2}, "journal-q2": {"quote": False, "count": 2}, "journal-q3": {"quote": False, "count": 1}},
 "wordgame": dict(GAME, look=LOOK, bins=[BIN[b] for b in B2], items=[
   it("ago", "a", "a·go: the a in the first beat says uh.", B2),
   it("broken", "e", "bro·ken: the e says uh.", B2),
   it("cotton", "o", "cot·ton: the o in the last beat says uh.", B2),
   it("pupil", "i", "pu·pil: the i says uh.", B2),
   it("balloon", "a", "bal·loon: the a in the first beat says uh.", B2),
   it("happen", "e", "hap·pen: the e says uh.", B2),
   it("carrot", "o", "car·rot: the o says uh.", B2),
   it("April", "i", "A·pril: the i says uh.", B2),
 ]),
 "glossary": GLOSS, "sayWords": [],
 "cards": note("Fauns in Old Stories", [
   "Fauns come from very old stories told in ancient Rome, about 2,000 years ago.",
   "Stories say a faun is half person and half goat, with goat legs and small horns, and lives in the woods.",
   "Lewis borrowed the faun from those old stories and made Mr. Tumnus."]),
 "transcripts": {
  "welcome": "Hi, it’s Opti. Lucy is back, and nobody believes her. Today, notice how Narnia feels in a warm cave, and in a cold, quiet wood.",
  "guide1": "Word work: match tele words, find connecting words, and spot the lazy uh.",
  "guide2": "Read Chapters 2 and 3. Then try my video in Read Like a Writer.",
  "guide3": "Today you write the opening sentence of your literary response."
 },
 "notes": dict(NOTES_COMMON, wgrd="A setting can change with the mood: Mr. Tumnus’s cave feels warm and cozy, and the empty wood feels cold and still.", vocab=VOC + [["betray", "to be disloyal to someone who trusted you"]])
}
L["25-3"] = {
 "connector": "No new chapters today. You get to be the detective. Find the exact words Lewis uses for what Lucy feels and hears, and the strange lamp-post glowing in the wood. Those words are your evidence.",
 "writingFocus": "literary response",
 "dol": dol("when lucy reached the lamp-post she heard a pitter patter of feet",
   C("W")+"hen "+C("L")+"ucy reached the lamp-post"+C(",")+" she heard a pitter patter of feet"+C("."),
   "When starts the part that cannot stand alone. A comma goes after it, before the main idea. Lucy is a name. A period ends it.",
   "when lucy was tired of eating the faun began to talk",
   C("W")+"hen "+C("L")+"ucy was tired of eating"+C(",")+" the "+C("F")+"aun began to talk"+C("."),
   "When starts the part that cannot stand alone, so a comma goes after eating. Lucy is a name, and the Faun is used as his name."),
 "hints": {
  "mfill1": {"h1": "Read the meaning beside it: sound from far away. Say tele, then phone.", "why": "tele + phone = telephone."},
  "mfill2": {"h1": "Read the meaning: seeing from far away. Say tele, then vision.", "why": "tele + vision = television."},
  "mfill3": {"h1": "Read the meaning: a tool for looking far away. Say tele, then scope.", "why": "tele + scope = telescope."},
  "mfill4": {"h1": "Read the meaning: a message written from far away. Say tele, then gram.", "why": "tele + gram = telegram."}
 },
 "flags": {"journal-q1": {"quote": True, "count": 2}, "journal-q2": {"quote": False, "count": 1}, "journal-q3": {"quote": False, "count": 2}},
 "wordgame": dict(GAME, look=LOOK, bins=[BIN[b] for b in B3], items=[
   it("parade", "a", "pa·rade: the a in the first beat says uh.", B3),
   it("melon", "o", "mel·on: the o says uh.", B3),
   it("walrus", "u", "wal·rus: the u says uh.", B3),
   it("fossil", "i", "fos·sil: the i says uh.", B3),
   it("comma", "a", "com·ma: the a at the end says uh.", B3),
   it("gallon", "o", "gal·lon: the o says uh.", B3),
   it("bonus", "u", "bo·nus: the u says uh.", B3),
   it("stencil", "i", "sten·cil: the i says uh.", B3),
 ]),
 "glossary": GLOSS, "sayWords": [],
 "cards": note("Lamp-Posts and Lamplighters", [
   "Long ago, before electric lights, many streets in London were lit by gas lamps on tall posts.",
   "Each evening a lamplighter walked from post to post to light them, and each morning he put them out.",
   "A lamp-post on a city street was ordinary. A lamp-post alone in a snowy wood is very strange!"], before="Look Back"),
 "transcripts": {
  "welcome": "Hi, it’s Opti. Detective day! Find the exact words Lewis uses to make Narnia feel real.",
  "guide1": "Word work: build tele words, join two sentences, and find which vowel blurred.",
  "guide2": "Look back at Chapters 1 to 3 for the exact words you need.",
  "guide3": "Today you write two evidence sentences with short quotes."
 },
 "notes": dict(NOTES_COMMON, wgrd="Point to the exact words. Lewis tells what Lucy feels and hears: snow that is soft and powdery and extremely cold, and something crunching under her feet.", vocab=VOC)
}
L["25-4"] = {
 "connector": "How does a made-up world start to feel real? Today you put it all together: a claim about Narnia, the one detail that proves it best, and a closing sentence for your writing.",
 "writingFocus": "literary response",
 "dol": dol("although susan looked inside she saw only an ordinary wardrobe",
   C("A")+"lthough "+C("S")+"usan looked inside"+C(",")+" she saw only an ordinary wardrobe"+C("."),
   "Although starts the part that cannot stand alone, so a comma goes after inside. Susan is a name. A period ends it.",
   "because lucy was a truthful girl she would not say it was a story",
   C("B")+"ecause "+C("L")+"ucy was a truthful girl"+C(",")+" she would not say it was a story"+C("."),
   "Because starts the part that cannot stand alone, so a comma goes after girl. Lucy is a name. A period ends it."),
 "hints": {},
 "flags": {"journal-q1": {"quote": False, "count": 1}, "journal-q2": {"quote": False, "count": 1}, "journal-q3": {"quote": False, "count": 1}},
 "wordgame": dict(GAME, look=LOOK4, bins=[BIN[b] for b in B4], items=[
   it("Snow fell softly on the gard<b>_</b>n.", "e", "garden: the e says uh.", B4, True),
   it("The cact<b>_</b>s grew in the hot desert.", "u", "cactus: the u says uh.", B4, True),
   it("It is snowing t<b>_</b>day.", "o", "today: the o says uh.", B4, True),
   it("The pand<b>_</b> ate bamboo.", "a", "panda: the a at the end says uh.", B4, True),
   it("Five min<b>_</b>s two is three.", "u", "minus: the u says uh.", B4, True),
   it("The bread was hot from the ov<b>_</b>n.", "e", "oven: the e says uh.", B4, True),
   it("The children ran <b>_</b>round the tree.", "a", "around: the a says uh.", B4, True),
   it("Wait just one sec<b>_</b>nd!", "o", "second: the o says uh.", B4, True),
 ]),
 "glossary": GLOSS, "sayWords": [],
 "cards": note("Reindeer and Sledges", [
   "Reindeer live in the cold far north, in places like Norway, Sweden and Finland.",
   "For a very long time, people there have trained reindeer to pull sledges over the snow. A sledge is a sled.",
   "In Chapter 3, the Queen’s sledge is pulled by two white reindeer with bells on their harness."], before="Look Back"),
 "transcripts": {
  "welcome": "Hi, it’s Opti. Last day of the week. Put it all together: what makes Narnia feel real, and how do you know?",
  "guide1": "Word work: roll tele words, edit in passes, and roll for the lazy uh.",
  "guide2": "Look back at Chapters 1 to 3 and pick your best detail.",
  "guide3": "Today you finish your literary response with a closing sentence."
 },
 "notes": dict(NOTES_COMMON, wgrd="A reader believes a fantasy world when the details feel real: what you can see, hear and touch.", vocab=VOC)
}
FLU = {
 "connector": "This week’s passage is from Chapter 1: the moment Lucy finds out the wardrobe never ends. Read it three times. The last time, slow down where Lucy is surprised.",
 "howto": True,
 "transcripts": {"welcome": "Hi, it’s Opti. This week’s passage is the moment Lucy finds Narnia. Read it three times. First, get every word right. Next, make it smooth. Then slow down where Lucy is surprised, and let your voice sound amazed."}
}

if __name__ == '__main__':
    import sys
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    try:
        from plates_wk25 import PLATES as P
        for k, p in P.items(): L[k]["plate"] = p
    except ImportError: print('no plates yet')
    for k, v in L.items():
        io.open(os.path.join(OUT, 'lesson-%s.json' % k), 'w', encoding='utf-8').write(json.dumps(v, ensure_ascii=False, indent=1))
        print(k, len(json.dumps(v, ensure_ascii=False).encode()))
    io.open(os.path.join(OUT, 'lesson-25-fluency.json'), 'w', encoding='utf-8').write(json.dumps(FLU, ensure_ascii=False, indent=1))
