#!/usr/bin/env python3
"""Week 30 DATA (The Lion, the Witch and the Wardrobe, Ch. 16-17 + synthesis): 30.1-30.4 + fluency.
Day 1 reads Ch. 16-17 (the end of the book); Days 2-4 look back over the whole book. Every book line checked against
Planning docs/lww_text.txt. Statues Come Alive items use only this year's roots (inter, trans, form, ject, script/scribe,
port, struct) and syllable types, and none is an answer elsewhere on the week's pages (international transport reform
project interact transform translate uniform inform reject inject eject describe manuscript inscription inspect construct;
throne reign brave queen stone gleam compete rainbow garden candle napkin tiger harbor bacon simple explain invite basket)
or a film example (interview, transfer, report, transatlantic; liberated, remarkable; sunset, pilot; see teach_wk30.py)."""
import json, io, os
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'data')
S = "<strong>"; E = "</strong>"
def C(x): return S + x + E
def dol(a_raw, a_fixed, a_why, b_raw, b_fixed, b_why):
    return {"a": {"raw": a_raw, "fixed": a_fixed, "why": a_why}, "b": {"raw": b_raw, "fixed": b_fixed, "why": b_why}}
GLOSS = [
 {"w": "theme", "m": "the big lesson a story teaches, said as a full sentence", "key": True},
 {"w": "editor", "m": "a person who checks writing and fixes capitals, punctuation and spelling", "key": True},
 {"w": "proper noun", "m": "the name of one particular person, place or thing, like Lucy or Cair Paravel. It starts with a capital."},
 {"w": "syllable", "m": "a part of a word with one vowel sound. Garden has two: gar and den.", "key": True},
 {"w": "root", "m": "the main part of a word that holds its meaning, like port, which means carry", "key": True},
 {"w": "simile", "m": "a comparison that uses like or as"},
 {"w": "honesty", "m": "telling the truth, even when it is hard", "key": True},
]
NOTES_COMMON = {
 "wordParts": "Roots from this year: inter = between, trans = across, form = shape, ject = throw, script and scribe = write, port = carry, struct = build.",
 "grammar": "An editor checks in passes. Capitals for names and the first word. Apostrophes for belonging and joined words. A comma before and or but when it joins two complete thoughts.",
 "spelling": "Syllable types: closed (cat), open (go), silent-e (bake), vowel team (rain), r-controlled (car), consonant-le (table)."
}
VOC = [["sovereign", "the supreme ruler of a country or kingdom"], ["coronation", "the ceremony in which a ruler is officially crowned"], ["reconciled", "restored to friendship or peace after a conflict"]]
VOC4 = VOC + [["vanquished", "defeated completely in battle"]]
RMISS = "Find the root in the word. What does that root mean?"
def it_mean(n, w, right, wrong):
    bins = [{"id": "r", "label": right, "ic": "👆"}, {"id": "w", "label": wrong, "ic": "👆"}]
    if n % 2: bins.reverse()
    return {"t": w, "bin": "r", "bins": bins, "why": "%s: %s." % (w, right), "miss": {"w": RMISS}}
SYL = {"closed": "Closed (short vowel)", "open": "Open (long vowel)", "silent": "Silent-e", "team": "Vowel team", "r": "R-controlled", "le": "Consonant-le"}
SMISS = "Look at the vowel in the bold part, and the letter right after it."
def it_syl(n, word, part, kind, others):
    t = word.replace(part, '<b>' + part + '</b>', 1)
    ids = [kind] + others
    ids = ids[n % 3:] + ids[:n % 3]
    return {"t": t, "bin": kind, "bins": [{"id": i, "label": SYL[i], "ic": "👆"} for i in ids],
            "why": "%s: the bold part, %s, is %s." % (word, part, SYL[kind].split(' (')[0].lower()), "miss": {i: SMISS for i in others}}
GAME = {"type": "statues", "title": "Statues Come Alive",
        "sub": "Every right answer brings a statue to life.",
        "todo": "Read the word on the statue. Tap the right answer. A right answer breathes life into the statue, and it fills with color.",
        "win": "Today's 8 statues are alive. Come back next lesson to wake more.",
        "winWeek": "Every statue is alive. The courtyard looks more like a zoo!"}
LOOK1 = ("This week's game is the Witch's courtyard, full of stone statues. Each statue has a word built from a root you learned this year. "
         "Tap what the word means. Each right answer is like Aslan's breath: the statue turns from gray stone to full color. Over four days you wake the whole courtyard.")
LOOK2 = "Eight new statues with eight new words. Find the root, and tap what the word means. The statues from Day 1 are still alive."
LOOK3 = ("Today each statue has a word with one part in bold. Tap the syllable type of the bold part: closed, open, silent-e, vowel team, r-controlled or consonant-le. "
         "The statues from earlier days are still alive.")
LOOK4 = "Eight more statues. Name the syllable type of each bold part. Wake these and the whole courtyard is alive."
def note(title, text, before="Read:|Look Back"):
    return [{"id": "world", "kind": "info", "tab": "reading", "after": before, "before": True, "icon": "🌍",
             "title": "World Notes: " + title, "sub": "A real thing behind the story",
             "todo": "Read the note. Then read with your lens in mind.", "text": text}]
MATCH = {"sovereign": "A sovereign rules a whole land. Look for the meaning about a ruler.",
         "coronation": "A coronation is a ceremony. Look for the meaning about being crowned.",
         "reconciled": "Reconciled is about making peace. Look for that meaning."}
L = {}
L["30-1"] = {
 "connector": "What's the best ending to a story you've ever read? In Chapters 16 and 17, the last two chapters of the book, Aslan wakes the statues, the battle ends, and four children are crowned. Watch how the ending answers the questions the beginning asked.",
 "writingFocus": "literary response",
 "dol": dol("when the battle was over peter and aslan shook hands",
   C("W") + "hen the battle was over" + C(",") + " " + C("P") + "eter and " + C("A") + "slan shook hands" + C("."),
   "When starts the sentence. A comma closes the opening part. Peter and Aslan are names.",
   "when lucy found mr tumnus they danced round and round",
   C("W") + "hen " + C("L") + "ucy found " + C("M") + "r" + C(".") + " " + C("T") + "umnus" + C(",") + " they danced round and round" + C("."),
   "When starts the sentence. Lucy and Mr. Tumnus are names, and Mr. takes a period. A comma closes the opening part."),
 "hints": {
  "fill1": {"h1": "Look at the word part table. Which word means between nations?", "why": "inter + national = international."},
  "fill2": {"h1": "Look at the root that means carry in the table.", "why": "trans + port = transport."},
  "fill3": {"h1": "Look at the root that means shape.", "why": "re + form = reform."},
  "fill4": {"h1": "Look at the root that means throw.", "why": "pro + ject = project."},
  "vcloze1": {"h1": "They rule all of Narnia. Look back at the word Opti figured out with you.", "why": "A sovereign is the supreme ruler of a land."},
  "vcloze2": {"h1": "This sentence is about a ceremony with crowns. Look at the meanings in the matching game.", "why": "A coronation is the ceremony where a ruler is crowned."},
  "vcloze3": {"h1": "Edmund is at peace with his family again. Find the word about making peace.", "why": "Reconciled means back at peace after a fight."}},
 "miss": {"match": MATCH},
 "flags": {"journal-q1": {"quote": False, "count": 1}, "journal-q2": {"quote": False, "count": 1}, "journal-q3": {"quote": False, "count": 1}},
 "copia": {"look": "One plain sentence from Chapter 16, and three empty boxes. Each box asks you to say the same idea in a new way.",
   "todo": "Rewrite the sentence three ways, one box at a time. Tap Show one way if you get stuck.",
   "seed": "The statues <b>came</b> alive.",
   "eg": ["In the Witch’s courtyard, the statues came alive.",
          "The statues <i>sprang</i> alive.",
          "The statues came alive in a blaze of gold, red and green."]},
 "wordgame": dict(GAME, look=LOOK1, stepTitle="What does it mean?", bins=[], items=[
   it_mean(0, "interstate", "a road that goes between states", "a road inside one small town"),
   it_mean(1, "transplant", "to move a plant across to a new place", "to cut a plant down"),
   it_mean(2, "deform", "to spoil the shape of something", "to paint something a new color"),
   it_mean(3, "rejection", "a no that sends something back", "a big hug hello"),
   it_mean(4, "scribble", "to write fast and messy", "to whisper quietly"),
   it_mean(5, "porter", "a person who carries bags", "a person who sings songs"),
   it_mean(6, "structure", "something that is built, like a bridge", "something that melts, like ice"),
   it_mean(7, "intermission", "a short break between two parts of a show", "the very first song of a show")]),
 "glossary": GLOSS, "sayWords": [],
 "cards": note("Crowning a King or Queen", [
   "A coronation is the ceremony where a new king or queen is crowned. In England, it has been held in Westminster Abbey for hundreds of years.",
   "Queen Victoria was crowned there in 1838, when she was 19. The crown was set on her head, and the people shouted, God save the Queen!",
   "In Chapter 17, Aslan crowns the four children in the Great Hall of Cair Paravel, and everyone shouts, Long Live King Peter!"]),
 "transcripts": {"welcome": "Hi, it's Opti. These are the last two chapters of the book. Watch how the ending answers the questions the beginning asked.",
  "guide1": "Word work first: roots from the whole year, capital letters, and spelling patterns.",
  "guide2": "Read Chapters 16 and 17 with your lens. Then answer three questions.",
  "guide3": "Today you add proof from the ending to your response."},
 "notes": dict(NOTES_COMMON, wgrd="The ending answers the beginning. Edmund began as a traitor and ends as King Edmund the Just. The ending proves the theme.", vocab=VOC)
}
L["30-2"] = {
 "connector": "You have finished the whole book! Today you look back from the first chapter to the last. Which moments prove the big lesson best? Edmund's story is a good place to start: who was he at the beginning, and who is he at the end?",
 "writingFocus": "literary response",
 "dol": dol("the giant broke the gates and lucy laughed",
   C("T") + "he giant broke the gates" + C(",") + " and " + C("L") + "ucy laughed" + C("."),
   "The starts the sentence. A comma goes before and when it joins two complete thoughts. Lucy is a name.",
   "edmund fought bravely but he was badly hurt",
   C("E") + "dmund fought bravely" + C(",") + " but he was badly hurt" + C("."),
   "Edmund is a name. A comma goes before but when it joins two complete thoughts."),
 "hints": {},
 "miss": {"match": dict(MATCH, vanquished="Vanquished is about losing a battle. Look for that meaning.")},
 "flags": {"journal-q1": {"quote": False, "count": 3}, "journal-q2": {"quote": False, "count": 2}, "journal-q3": {"quote": False, "count": 1}},
 "wordgame": dict(GAME, look=LOOK2, stepTitle="What does it mean?", bins=[], items=[
   it_mean(0, "interlock", "to fit together between each other", "to come apart"),
   it_mean(1, "transit", "moving across from place to place", "staying in one spot"),
   it_mean(2, "format", "the shape or layout of a page", "the sound a page makes"),
   it_mean(3, "reporter", "a person who carries back the news", "a person who fixes cars"),
   it_mean(4, "construction", "building something", "taking a nap"),
   it_mean(5, "injection", "medicine pushed into the body with a needle", "a bandage on a cut"),
   it_mean(6, "scribe", "a person long ago who wrote things by hand", "a person who sails ships"),
   it_mean(7, "intercom", "a speaker for talking between rooms", "a lamp for one room")]),
 "glossary": GLOSS, "sayWords": [],
 "cards": note("Lions Made of Stone and Metal", [
   "People have carved statues of lions for thousands of years, from stone like marble and granite.",
   "The four giant lions in Trafalgar Square, London, look like stone, but they are made of bronze, a metal. They were put there in 1867.",
   "In Chapter 16, the Witch has turned a real lion to stone. Aslan breathes on him, and gold color creeps along his back until he is alive again."], before="Look Back"),
 "transcripts": {"welcome": "Hi, it's Opti. You finished the book! Today you look back from the first chapter to the last.",
  "guide1": "Word work: match root words, find four kinds of mistakes, and find syllable types.",
  "guide2": "Look back through the book. Then watch my video in Read Like a Writer.",
  "guide3": "Today you edit your response."},
 "notes": dict(NOTES_COMMON, wgrd="A theme needs proof from across the book. Edmund betrays his family, he is forgiven, and in the end he is crowned King Edmund the Just.", vocab=VOC4)
}
L["30-3"] = {
 "connector": "The book ends with the four kings and queens chasing the White Stag. They find a lamp-post, push through branches that turn into coats, and tumble out of the wardrobe, the same day and the same hour they left. Today you explain what the whole book is really about.",
 "writingFocus": "literary response",
 "dol": dol("the professor believed them and he didnt laugh",
   C("T") + "he " + C("P") + "rofessor believed them" + C(",") + " and he didn" + C("’") + "t laugh" + C("."),
   "The starts the sentence. The Professor is used as his name. A comma goes before and. Didn’t joins did and not.",
   "the four children ruled narnia and they made good laws",
   C("T") + "he four children ruled " + C("N") + "arnia" + C(",") + " and they made good laws" + C("."),
   "The starts the sentence. Narnia is a name. A comma goes before and."),
 "hints": {
  "mfill1": {"h1": "Say the two parts out loud, then push them together.", "why": "trans + port = transport."},
  "mfill2": {"h1": "Say the two parts out loud, then push them together.", "why": "in + spect = inspect."},
  "mfill3": {"h1": "Keep both parts. Do not drop any letters.", "why": "con + struct = construct."},
  "mfill4": {"h1": "Keep both parts. Do not drop any letters.", "why": "de + scribe = describe."}},
 "flags": {"journal-q1": {"quote": False, "count": 2}, "journal-q2": {"quote": False, "count": 1}, "journal-q3": {"quote": False, "count": 1}},
 "wordgame": dict(GAME, look=LOOK3, stepTitle="What kind of syllable is in bold?", bins=[], items=[
   it_syl(0, "robot", "ro", "open", ["closed", "silent"]), it_syl(1, "rabbit", "rab", "closed", ["open", "team"]),
   it_syl(2, "farmer", "far", "r", ["closed", "le"]), it_syl(3, "sailboat", "sail", "team", ["silent", "r"]),
   it_syl(4, "cupcake", "cake", "silent", ["team", "closed"]), it_syl(5, "marble", "ble", "le", ["open", "silent"]),
   it_syl(6, "music", "mu", "open", ["r", "closed"]), it_syl(7, "pumpkin", "pump", "closed", ["le", "team"])]),
 "glossary": GLOSS, "sayWords": [],
 "cards": note("Mermaids in Old Stories", [
   "For thousands of years, sailors have told stories about mermaids, sea people who are half human and half fish. Stories say they sing beautiful songs.",
   "Some scientists think sailors long ago saw real sea animals called manatees, swimming far off, and thought they were mermaids.",
   "In Chapter 17, mermen and mermaids sing outside the eastern door of Cair Paravel for the new kings and queens."], before="Look Back"),
 "transcripts": {"welcome": "Hi, it's Opti. The four kings and queens tumble out of the wardrobe. Today you explain what the whole book is really about.",
  "guide1": "Word work: build root words, fix a sentence like an editor, and spell by syllable types.",
  "guide2": "Look back through the book. Then answer the questions.",
  "guide3": "Today you give your response a title."},
 "notes": dict(NOTES_COMMON, wgrd="The book ends where it began, at the wardrobe. The children are ordinary again, but the Professor says, Once a King in Narnia, always a King in Narnia.", vocab=VOC)
}
L["30-4"] = {
 "connector": "This is the last day with The Lion, the Witch and the Wardrobe. You have read all 17 chapters, noticed symbols, and built a theme. Today you explain the whole book in your own words, and finish your literary response.",
 "writingFocus": "literary response",
 "dol": dol("the lion the witch and the wardrobe is my favorite book",
   C("T") + "he " + C("L") + "ion" + C(",") + " the " + C("W") + "itch and the " + C("W") + "ardrobe is my favorite book" + C("."),
   "Capitalize the important words in a book title. A comma goes after Lion in the title.",
   "c s lewis wrote seven books about narnia",
   C("C.S.") + " " + C("L") + "ewis wrote seven books about " + C("N") + "arnia" + C("."),
   "An author’s initials take capitals and periods. Lewis and Narnia are names."),
 "hints": {},
 "flags": {"journal-q1": {"quote": False, "count": 1}, "journal-q2": {"quote": False, "count": 1}, "journal-q3": {"quote": False, "count": 1}},
 "wordgame": dict(GAME, look=LOOK4, stepTitle="What kind of syllable is in bold?", bins=[], items=[
   it_syl(0, "bubble", "ble", "le", ["closed", "open"]), it_syl(1, "monster", "mon", "closed", ["silent", "r"]),
   it_syl(2, "sunshine", "shine", "silent", ["team", "open"]), it_syl(3, "raincoat", "rain", "team", ["closed", "le"]),
   it_syl(4, "moment", "mo", "open", ["closed", "team"]), it_syl(5, "stormy", "stor", "r", ["open", "silent"]),
   it_syl(6, "cactus", "cac", "closed", ["open", "r"]), it_syl(7, "reptile", "tile", "silent", ["team", "le"])]),
 "glossary": GLOSS, "sayWords": [],
 "cards": note("The White Stag", [
   "In old legends from Europe, a white stag or white deer is very hard to catch. When hunters chase one, it often leads them into a great adventure.",
   "Some stories about King Arthur begin with a white stag running through the forest.",
   "Real white deer do exist, but they are very rare. In Chapter 17, the White Stag leads the four rulers back to the lamp-post."], before="Look Back"),
 "transcripts": {"welcome": "Hi, it's Opti. This is the last day with the book. Explain it in your own words, and finish your response.",
  "guide1": "Word work: roll root words, fix a passage in passes, and split words by syllable.",
  "guide2": "Look back through the whole book for your best proof.",
  "guide3": "Today you publish your literary response."},
 "notes": dict(NOTES_COMMON, wgrd="A good theme statement works for the whole book: the beginning, the middle and the end. The ending is the strongest proof.", vocab=VOC)
}
FLU = {"connector": "This week's passage is from Chapter 17: the four children grow up as kings and queens of Narnia. Read it three times. The last time, read the four royal names with pride, like a herald announcing them.",
 "howto": True,
 "transcripts": {"welcome": "Hi, it's Opti. This week's passage is from the last chapter. Read it three times, and read the four royal names with pride."}}
if __name__ == '__main__':
    import sys
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from plates_wk30 import PLATES as P
    for k, p in P.items(): L[k]["plate"] = p
    for k, v in L.items():
        io.open(os.path.join(OUT, 'lesson-%s.json' % k), 'w', encoding='utf-8').write(json.dumps(v, ensure_ascii=False, indent=1)); print(k)
    io.open(os.path.join(OUT, 'lesson-30-fluency.json'), 'w', encoding='utf-8').write(json.dumps(FLU, ensure_ascii=False, indent=1))
