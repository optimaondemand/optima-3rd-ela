#!/usr/bin/env python3
"""Week 23 DATA (Medieval Nonfiction, part 1): 23.1-23.4. No fluency page this week.
History lines checked against standard sources (see claude/g3-ela-wk23-audit.md); every quote from an
article is the article's own words after acc_wk23.py. Game items use only this week's word study
(trans- = across; VCCV split; capital letters for names, places, titles) and none is an answer or film
example elsewhere in the week (transport, transform, translate, transfer, transparent, transplant,
transatlantic, and the films' transpacific, tranquil, transcontinental, transit, transcribe; rabbit garden basket sister tunnel hamper winter picnic turret mortar helmet napkin sudden
contest problem muffin dolphin button table noble bugle title tiger music robot paper bacon silent open
pilot final hotel lazy tulip; Prince Brat, Sir Geoffrey, Master Peck, Westminster, River Thames, London
Bridge, The Canterbury Tales, Windsor Castle, Spring stay out)."""
import json, io, os
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'data')
S = "<strong>"; E = "</strong>"

def dol(a_raw, a_fixed, a_why, b_raw, b_fixed, b_why):
    return {"a": {"raw": a_raw, "fixed": a_fixed, "why": a_why}, "b": {"raw": b_raw, "fixed": b_fixed, "why": b_why}}

GLOSS = [
 {"w": "central idea", "m": "the most important point an author makes. The whole article keeps coming back to it.", "key": True},
 {"w": "detail", "m": "one fact from the article that helps prove the central idea"},
 {"w": "Middle Ages", "cs": True, "m": "a time in history about 500 to 1,500 years ago, when there were castles, knights and kings in Europe"},
 {"w": "medieval", "m": "from the Middle Ages", "key": True},
 {"w": "VCCV", "cs": True, "m": "vowel, consonant, consonant, vowel. A word with this pattern splits between the two consonants, like nap · kin."},
 {"w": "syllable", "m": "one beat in a word. Basket has two: bas · ket."},
 {"w": "hyperbole", "m": "stretching the truth on purpose, so much that nobody believes it, like “I’m so hungry I could eat a horse.”", "key": True},
 {"w": "expository", "m": "writing that explains or teaches facts about a topic"},
 {"w": "research question", "m": "the question you want your notes to answer"},
 {"w": "diligence", "m": "working hard and carefully, and not giving up", "key": True},
]
NOTES_COMMON = {
 "wordParts": "The word part trans means across. transport = to carry across. translate = to carry words across into another language. Some words only start with t r a n, like tranquil (calm).",
 "grammar": "Capital letters start every sentence and every important word in a name: people (Queen Eleanor), places (Tower of London) and titles. Small words like the, of and in stay small inside a name or title, unless they come first.",
 "spelling": "VCCV means vowel, consonant, consonant, vowel. Split the word between the two consonants: bas · ket, tun · nel. Letters like ph and th stay together."
}

GAME = {
 "type": "illuminate", "title": "Illuminate the Page",
 "sub": "Every right answer paints part of a medieval book page.",
 "todo": "Read the question. Tap the answer you think is right. A right answer paints the next part of the page.",
 "win": "Today’s 8 parts are painted. Come back next lesson to keep painting.",
 "winWeek": "Your page is finished, from the gold letter to the last line!"
}
LOOK1 = ("This week’s game is a page from a medieval book, before it is painted. Long ago, books were written and painted by hand. "
         "A painted page is called illuminated, because the gold makes it shine. Each right answer paints one part. "
         "Day 1 paints the big gold capital letter. Day 2 paints the border, Day 3 the little picture, and Day 4 the lines of writing.")
LOOK = "Each right answer paints one part of the page. Day 1 painted the big letter. Day 2 paints the border, Day 3 the picture, and Day 4 the lines of writing."
def q(title, qq, opts, a, why, miss):
    return {"title": title, "q": qq, "opts": opts, "a": a, "why": why, "miss": {str(k): v for k, v in miss.items()}}
SIDE = {"23-1": [1, 0, 0, 1, 1, 0, 1, 0], "23-2": [0, 2, 1, 0, 1, 0, 1, 1], "23-3": [1, 0, 1, 0, 1, 0, 0, 1], "23-4": [1, 0, 1, 1, 2, 0, 1, 0]}
def sides(k, items):
    for it, s in zip(items, SIDE[k]):
        s = s % len(it["opts"])
        order = [i for i in range(len(it["opts"])) if i != it["a"]]
        order.insert(s, it["a"])
        newpos = {old: new for new, old in enumerate(order)}
        it["opts"] = [it["opts"][i] for i in order]
        it["miss"] = {str(newpos[int(k2)]): v for k2, v in it["miss"].items()}
        it["a"] = s
    return items
TR, VC, CP = "The word part trans", "Split the word", "Capital letters"
SPLIT = "Find the two consonants in the middle. Split between them."
TITLE = "When a title like this comes right before a name, it gets a capital too."

def job(title, text):
    return [{"id": "job", "kind": "info", "tab": "reading", "after": "Pause", "before": True, "icon": "⭐",
             "title": "Job Spotlight: " + title, "sub": "A real job in the Middle Ages",
             "todo": "Read about this real job. Then read the two questions and the article.", "text": text}]

L = {}
# ───────────────────────────── 23.1 · Life in a Medieval Castle
L["23-1"] = {
 "connector": "You just finished The Whipping Boy, a made-up story about a prince in a castle. This week you read true articles about real castles. Who lived there, and what did they do all day? Look for the one big idea the article keeps coming back to.",
 "writingFocus": "inform",
 "dol": dol("king john stayed at windsor castle",
   S+"K"+E+"ing "+S+"J"+E+"ohn stayed at "+S+"W"+E+"indsor "+S+"C"+E+"astle"+S+"."+E,
   "King is a title right before his name, so it gets a capital K. John is a name. Windsor Castle is the name of one place, so both words get capitals. A period ends the sentence.",
   "queen eleanor sailed to england",
   S+"Q"+E+"ueen "+S+"E"+E+"leanor sailed to "+S+"E"+E+"ngland"+S+"."+E,
   "Queen is a title right before her name, so it gets a capital Q. Eleanor is a name, and England is the name of a place. A period ends the sentence."),
 "hints": {
  "fill1": {"h1": "It means carry. You can find it in import and export.", "why": "trans + port = transport: to carry across."},
  "fill2": {"h1": "It means shape. A butterfly changes this.", "why": "trans + form = transform: to change into a new shape."},
  "fill3": {"h1": "Look at the word list above. It is the last word in the list.", "why": "trans + late = translate: to carry words across into another language."},
  "fill4": {"h1": "It is a six-letter word. Your mom or dad is one.", "why": "trans + parent = transparent: you can see across, or through, it."},
  "vcloze1": {"h1": "This place was built to keep enemies out. Look at the word with fort in it.", "why": "A fortress is a strong building built to keep enemies out."},
  "vcloze2": {"h1": "Find the word for the strongest tower inside the castle.", "why": "The keep is the strongest inner tower."},
  "vcloze3": {"h1": "These people cooked, cleaned and cared for the family.", "why": "Servants worked in someone else’s home."},
  "vcloze4": {"h1": "Find the word for a boy training to be a knight.", "why": "A page trained in a noble’s home to become a knight."}
 },
 "miss": {"match": {
   "fortress": "A fortress is a building. Look for the meaning about a strong building.",
   "keep": "The keep is one part of a castle. Look for the meaning about a tower.",
   "servant": "A servant is a person. Look for the meaning about working in someone’s home.",
   "page": "A page is a boy. Look for the meaning about training to be a knight."}},
 "flags": {"journal-q1": {"quote": False, "count": 0}, "journal-q2": {"quote": False, "count": 2}, "journal-q3": {"quote": False, "count": 1}},
 "copia": {"look": "One plain sentence from the castle article, and three empty boxes. Each box asks you to say the same idea in a new way.",
   "todo": "Rewrite the sentence three ways, one box at a time. Tap Show one way if you get stuck.",
   "seed": "Many people <b>worked</b> inside the castle walls every day.",
   "eg": ["Every day, many people worked inside the castle walls.",
          "Many people <i>labored</i> inside the castle walls every day.",
          "Many busy people worked inside the thick castle walls every day."]},
 "wordgame": dict(GAME, look=LOOK1, items=[
   q(TR, "Which word has the word part <b>trans</b>, meaning across?", ["transmit", "trance"], 0,
     "trans + mit: to send across. Trance starts with t r a n, but nothing goes across.", {1: "Trance starts with t r a n, but nothing goes across. Look for trans."}),
   q(TR, "Which word part means <b>across</b>?", ["trans", "un"], 0,
     "trans means across.", {1: "un means not. Which one means across?"}),
   q(VC, "Where does <b>lantern</b> split?", ["lan · tern", "la · ntern"], 0,
     "n and t sit between the vowels. Split between them: lan · tern.", {1: SPLIT}),
   q(VC, "Where does <b>market</b> split?", ["mar · ket", "ma · rket"], 0,
     "r and k sit between the vowels: mar · ket.", {1: SPLIT}),
   q(CP, "Which one is the name of one real place, so it gets capitals?", ["Dover Castle", "a big castle"], 0,
     "Dover Castle is the name of one real castle in England.", {1: "A big castle could be any castle. Which one is a name?"}),
   q(CP, "Which is written the right way?", ["Lady Anne", "lady Anne"], 0,
     "Lady is a title right before her name, so it gets a capital.", {1: TITLE}),
   q(VC, "Which word has two consonants in the middle?", ["velvet", "tiny"], 0,
     "vel · vet: l and v sit in the middle.", {1: "Tiny has only one consonant, n, in the middle. Look for two."}),
   q(TR, "A <b>transcript</b> is a talk written down. Which part means across?", ["trans", "script"], 0,
     "trans means across. The words move across, from talking to writing.", {1: "Script means writing. Which part means across?"}),
 ]),
 "glossary": GLOSS,
 "sayWords": [],
 "cards": job("The Page", [
   "A page was a boy from a noble family. At about seven years old, he went to live in a lord’s castle.",
   "He served at meals, carried messages, and learned to ride and to use a sword.",
   "At about fourteen, a page could become a squire, the next step toward being a knight."]),
 "transcripts": {
  "welcome": "Hi, it’s Opti. You just finished The Whipping Boy. This week you read true articles about real life long ago. Today: a castle. Who lived there, and what did they do all day?",
  "guide1": "Word work first. You’ll meet a word part that means across, sort names that get capital letters, and split words between two consonants.",
  "guide2": "Read the castle article. Look for the one big idea it keeps coming back to.",
  "guide3": "Today you pick your own topic about medieval life, one you will explain."
 },
 "notes": dict(NOTES_COMMON,
   wgrd="The central idea is the most important point an author makes. A detail is one fact that helps prove it.",
   vocab=[["fortress", "a large, strong building built to resist attack"], ["keep", "the strongest, innermost tower of a castle"], ["servant", "a person who works in someone else’s household"], ["page", "a young boy in training at a noble household, learning to become a knight"]])
}
# ───────────────────────────── 23.2 · Servants and Apprentices
L["23-2"] = {
 "connector": "Most children long ago did not go to school. So how did they learn? Today’s article has two paragraphs. Look for what each paragraph is about, and the one big idea that fits both.",
 "writingFocus": "inform",
 "dol": dol("in the town of york a baker hired an apprentice",
   S+"I"+E+"n the town of "+S+"Y"+E+"ork"+S+","+E+" a baker hired an apprentice"+S+"."+E,
   "In starts the sentence, so it gets a capital I. York is the name of a place. A comma comes after the opening part, In the town of York. A period ends the sentence.",
   "in old london master hugh taught his apprentice",
   S+"I"+E+"n old "+S+"L"+E+"ondon"+S+","+E+" "+S+"M"+E+"aster "+S+"H"+E+"ugh taught his apprentice"+S+"."+E,
   "In starts the sentence. London is a place. A comma comes after the opening part. Master is a title right before his name, Hugh. A period ends the sentence."),
 "hints": {
  "vcloze1": {"h1": "This young person is learning a trade from a master.", "why": "An apprentice learns a trade by working for an expert."},
  "vcloze2": {"h1": "This person already knows the trade and makes things by hand.", "why": "A craftsman is a skilled worker."},
  "vcloze3": {"h1": "This is a food: a thick soup.", "why": "Pottage is a thick soup of vegetables and grains."},
  "vcloze4": {"h1": "This one is something you do with a needle and thread.", "why": "To embroider is to sew pictures onto cloth."}
 },
 "miss": {"match": {
   "apprentice": "An apprentice is a person who is learning. Look for that meaning.",
   "craftsman": "A craftsman already has the skill. Look for the meaning about making things by hand.",
   "pottage": "Pottage is a food. Look for the meaning about soup.",
   "embroider": "Embroider is about sewing. Look for the meaning about needle and thread."}},
 "flags": {"journal-q1": {"quote": False, "count": 0}, "journal-q2": {"quote": False, "count": 2}, "journal-q3": {"quote": False, "count": 1}},
 "wordgame": dict(GAME, look=LOOK, items=[
   q(TR, "Which word has the word part <b>trans</b>?", ["transcript", "trumpet"], 0,
     "trans + script: words carried across, from talking to writing.", {1: "Trumpet starts with t r, but there is no trans in it."}),
   q(TR, "The word part <b>trans</b> means…", ["across", "again", "not"], 0,
     "trans means across.", {1: "Again goes with re. Which one goes with trans?", 2: "Not goes with un. Which one goes with trans?"}),
   q(VC, "Where does <b>hammer</b> split?", ["ham · mer", "hamm · er"], 0,
     "Two m’s in the middle. Split between them: ham · mer.", {1: "Split between the two consonants, not after them."}),
   q(VC, "Which word splits between two consonants?", ["kitten", "baby"], 0,
     "kit · ten.", {1: "Baby has one consonant, b, in the middle. Look for two."}),
   q(CP, "Which is written the right way?", ["the River Severn", "the river Severn"], 0,
     "River is part of the name, so it gets a capital. The small word the stays small.", {1: "River is part of this river’s name. Every important word in a name gets a capital."}),
   q(CP, "Which title is written the right way?", ["Beauty and the Beast", "Beauty And The Beast"], 0,
     "And and the are small words inside the title, so they stay small.", {1: "Look at And and The. Small words inside a title stay small."}),
   q(TR, "Radios <b>transmit</b> sound. Transmit means…", ["to send across", "to keep inside"], 0,
     "trans means across. A radio sends sound across the air.", {1: "Look at trans. It means across."}),
   q(VC, "Where does <b>harvest</b> split?", ["har · vest", "harv · est"], 0,
     "r and v sit in the middle: har · vest.", {1: SPLIT}),
 ]),
 "glossary": GLOSS,
 "sayWords": [],
 "cards": job("The Apprentice", [
   "An apprentice lived with a master and learned a trade, like baking or blacksmithing.",
   "Many started at about twelve to fourteen years old and stayed about seven years.",
   "To finish, some made a special piece of work to show the guild. That is where the word masterpiece comes from."]),
 "transcripts": {
  "welcome": "Welcome back, it’s Opti. Long ago, most children did not go to school. So how did they learn a job? Today’s article tells you, in two paragraphs.",
  "guide1": "Word study. Match trans words to their meanings, tap every word that needs a capital, and find the word that splits between two consonants.",
  "guide2": "Read about servants and apprentices. Then watch my video in the Read Like a Writer box.",
  "guide3": "Today you write a research question and take notes from two articles."
 },
 "notes": dict(NOTES_COMMON,
   wgrd="When an article has two paragraphs, ask what each one is mostly about. Then find one big idea that fits both.",
   vocab=[["apprentice", "a person learning a trade by working under an expert"], ["craftsman", "a skilled worker who makes things by hand"], ["pottage", "a thick soup of vegetables and grains"], ["embroider", "to decorate cloth with needle and thread"]])
}
# ───────────────────────────── 23.3 · Royal Courts
L["23-3"] = {
 "connector": "Imagine a dinner where your seat shows everyone how important you are. That was a royal court. Today’s article explains its rules. Ask: what does the author most want me to know?",
 "writingFocus": "inform",
 "dol": dol("lady anne of kent bowed before king henry",
   S+"L"+E+"ady "+S+"A"+E+"nne of "+S+"K"+E+"ent bowed before "+S+"K"+E+"ing "+S+"H"+E+"enry"+S+"."+E,
   "Lady and King are titles right before names, so they get capitals. Anne and Henry are names, and Kent is a place. The small word of stays small. A period ends the sentence.",
   "sir thomas knelt before queen isabella in london",
   S+"S"+E+"ir "+S+"T"+E+"homas knelt before "+S+"Q"+E+"ueen "+S+"I"+E+"sabella in "+S+"L"+E+"ondon"+S+"."+E,
   "Sir and Queen are titles right before names. Thomas and Isabella are names, and London is a place. A period ends the sentence."),
 "hints": {
  "mfill1": {"h1": "Say trans, then port. Push them together.", "why": "trans + port = transport: to carry across."},
  "mfill2": {"h1": "Say trans, then form. Push them together.", "why": "trans + form = transform: to change shape."},
  "mfill3": {"h1": "Say trans, then late. Push them together.", "why": "trans + late = translate: to carry meaning across languages."},
  "mfill4": {"h1": "Say trans, then fer. Push them together.", "why": "trans + fer = transfer: to move something to another place."},
  "vcloze1": {"h1": "Find the word for the court’s rules.", "why": "Protocol is the rules for how to behave at court."},
  "vcloze2": {"h1": "This word is a person’s level of importance.", "why": "Rank decided where a knight sat."},
  "vcloze3": {"h1": "This person has a high place, but is not a king or queen.", "why": "A noble is a person of high birth."},
  "vcloze4": {"h1": "This word means polite and kind.", "why": "Courteous means polite and respectful."},
  "gfill1": {"h1": "Start with the first word. Then count every word in a person’s name and a place’s name.", "why": "Prince, Brat, London, Bridge."},
  "gfill2": {"h1": "Count the first word. Then the words in his name and in the river’s name. Is the a name?", "why": "Sir, Geoffrey, River, Thames. The word the stays small."},
  "gfill3": {"h1": "Count the first word. Then every important word in the book’s title, starting with its first word.", "why": "Jemmy, The, Canterbury, Tales."},
  "gfill4": {"h1": "Count the first word. Then the words in a person’s name and a place’s name.", "why": "Master, Peck, Westminster."}
 },
 "miss": {"match": {
   "protocol": "Protocol is a set of rules. Look for the meaning about how to behave.",
   "rank": "Rank is about position. Look for the meaning about level or importance.",
   "noble": "A noble is a person. Look for the meaning about high birth.",
   "courteous": "Courteous describes manners. Look for the meaning about being polite."}},
 "flags": {"journal-q1": {"quote": False, "count": 0}, "journal-q2": {"quote": False, "count": 1}, "journal-q3": {"quote": False, "count": 1}, "journal-q4": {"quote": False, "count": 2}},
 "wordgame": dict(GAME, look=LOOK, items=[
   q(CP, "How many capitals does this need? <i>sir john lived in dover.</i>", ["3", "2", "4"], 0,
     "Sir, John, Dover. Sir starts the sentence and is part of his name.", {1: "Count the first word too.", 2: "Lived and in are not names."}),
   q(CP, "Which title is written the right way?", ["The Lion and the Mouse", "The Lion And The Mouse"], 0,
     "The first word, The, gets a capital. And and the inside the title stay small.", {1: "Look at And and the second The. Small words inside a title stay small."}),
   q(TR, "Which word does NOT have the word part trans?", ["trance", "transmit"], 0,
     "Trance is a word all on its own. It just starts with t r a n.", {1: "Transmit means to send across. It has trans."}),
   q(TR, "Put the parts together: <b>trans</b> + <b>script</b>", ["transcript", "tanscript"], 0,
     "trans + script = transcript.", {1: "Say trans, then script. Keep every letter of trans."}),
   q(VC, "Where does <b>pencil</b> split?", ["pen · cil", "pe · ncil"], 0,
     "n and c sit in the middle: pen · cil.", {1: SPLIT}),
   q(VC, "Which word splits between two consonants?", ["signal", "spider"], 0,
     "sig · nal: g and n sit in the middle.", {1: "Spider has one consonant, d, between i and e. Look for two."}),
   q(CP, "Which one is the name of a time in history, so it gets capitals?", ["the Middle Ages", "the old days"], 0,
     "The Middle Ages is the name of one time in history.", {1: "The old days could mean any time. Which one is a name?"}),
   q(VC, "Where does <b>cotton</b> split?", ["cot · ton", "co · tton"], 0,
     "Two t’s in the middle. Split between them: cot · ton.", {1: SPLIT}),
 ]),
 "glossary": GLOSS,
 "sayWords": [],
 "cards": job("The Herald", [
   "A herald worked for a king or a great lord.",
   "He carried important messages and announced guests and events in a loud, clear voice.",
   "Heralds knew every knight’s coat of arms, the pictures on their shields, so they could tell who was who."]),
 "transcripts": {
  "welcome": "Hi, it’s Opti. Picture a dinner where your seat tells everyone how important you are. That was a royal court. Today you find out its rules.",
  "guide1": "Word work. Build trans words, count the capitals a sentence needs, and split longer words.",
  "guide2": "Read about royal courts. Ask what the author most wants you to know.",
  "guide3": "Today you plan your paragraph: a topic sentence, two details, and a closing."
 },
 "notes": dict(NOTES_COMMON,
   wgrd="When a word is new, read the sentences around it. They often explain it. Then ask what the author most wants you to know.",
   vocab=[["protocol", "official rules for how to behave in formal situations"], ["rank", "a person’s position or level of importance"], ["noble", "a person of high birth, below a king or queen"], ["courteous", "polite, respectful and well-mannered"]])
}
# ───────────────────────────── 23.4 · Food
L["23-4"] = {
 "connector": "What did you eat today? Long ago, the answer depended on who you were. Today’s article shows two sides: the rich and the poor. Look for the words that split them apart.",
 "writingFocus": "inform",
 "dol": dol("at the great feast lord neville served roast swan",
   S+"A"+E+"t the great feast"+S+","+E+" "+S+"L"+E+"ord "+S+"N"+E+"eville served roast swan"+S+"."+E,
   "At starts the sentence, so it gets a capital A. A comma comes after the opening part. Lord is a title right before his name, Neville. A period ends the sentence.",
   "in the kitchens of dover castle the cooks baked pies",
   S+"I"+E+"n the kitchens of "+S+"D"+E+"over "+S+"C"+E+"astle"+S+","+E+" the cooks baked pies"+S+"."+E,
   "In starts the sentence. Dover Castle is the name of one place, so both words get capitals. A comma comes after the opening part. A period ends the sentence."),
 "hints": {
  "vcloze1": {"h1": "Poor families ate this thick soup.", "why": "Pottage is a thick soup of grain and vegetables."},
  "vcloze2": {"h1": "Find the word for a big, fancy meal.", "why": "A feast is a large meal for a celebration."},
  "vcloze3": {"h1": "This word means rough, not smooth.", "why": "Coarse bread was rough and dark."},
  "vcloze4": {"h1": "Find the word for a dull grey metal.", "why": "Pewter is a grey metal used for plates and cups."}
 },
 "miss": {"match": {
   "pottage": "Pottage is a food. Look for the meaning about soup.",
   "feast": "A feast is a meal. Look for the meaning about a big meal.",
   "coarse": "Coarse describes how something feels. Look for the meaning about rough.",
   "pewter": "Pewter is a metal. Look for the meaning about plates and cups."}},
 "flags": {"journal-q1": {"quote": False, "count": 0}, "journal-q2": {"quote": False, "count": 2}, "journal-q3": {"quote": False, "count": 1}},
 "wordgame": dict(GAME, look=LOOK, items=[
   q(TR, "Which word has the word part <b>trans</b>?", ["transmit", "trumpet"], 0,
     "trans + mit: to send across.", {1: "Trumpet starts with t r, but there is no trans in it."}),
   q(TR, "What does <b>trans</b> mean in <b>transcript</b>?", ["across", "under"], 0,
     "trans means across. The words move across, from talking to writing.", {1: "Under goes with sub. Which one goes with trans?"}),
   q(VC, "Where does <b>lumber</b> split?", ["lum · ber", "lu · mber"], 0,
     "m and b sit in the middle: lum · ber.", {1: SPLIT}),
   q(VC, "Which word splits between two consonants?", ["mitten", "river"], 0,
     "mit · ten.", {1: "River has one consonant, v, between the vowels. Look for two."}),
   q(CP, "Find the mistake: <i>We visited warwick Castle.</i>", ["warwick", "Castle", "No mistake"], 0,
     "Warwick is part of the castle’s name, so it needs a capital W.", {1: "Castle is part of the name, so its capital is right.", 2: "Look again at every word in the name."}),
   q(CP, "Find the mistake: <i>The feast was in the Winter.</i>", ["Winter", "feast", "No mistake"], 0,
     "Seasons stay small: winter.", {1: "Feast is not a name, so it stays small. That part is right.", 2: "Look at the season."}),
   q(CP, "Which is written the right way?", ["Duke William", "duke William"], 0,
     "Duke is a title right before his name, so it gets a capital.", {1: TITLE}),
   q(VC, "Where does <b>blanket</b> split?", ["blan · ket", "bla · nket"], 0,
     "n and k sit in the middle: blan · ket.", {1: SPLIT}),
 ]),
 "glossary": GLOSS,
 "sayWords": [],
 "cards": job("The Castle Cook", [
   "A big castle kitchen had a head cook and many helpers.",
   "They baked bread, stirred pottage, and roasted meat over a huge open fire.",
   "A kitchen boy sometimes had a hot job: turning the meat on a long spit, around and around, for hours."]),
 "transcripts": {
  "welcome": "Hi, it’s Opti. What did you eat today? Long ago, the answer depended on who you were. Today’s article shows two sides, the rich and the poor.",
  "guide1": "Word study review. Roll trans words, hunt for capital-letter mistakes, and roll VCCV words.",
  "guide2": "Read about medieval food. Look for the words that split the rich from the poor.",
  "guide3": "Today you start writing: your topic sentence and one detail."
 },
 "notes": dict(NOTES_COMMON,
   wgrd="Some articles show two sides. Words like most and very differently tell you the author is switching sides.",
   vocab=[["pottage", "a thick soup of vegetables and grains"], ["feast", "a large, fancy meal for a celebration"], ["coarse", "rough in texture"], ["pewter", "a dull grey metal used for plates and cups"]])
}
for k in ("23-1", "23-2", "23-3", "23-4"): sides(k, L[k]["wordgame"]["items"])

if __name__ == '__main__':
    import sys
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from plates_wk23 import PLATES as P
    for k, p in P.items(): L[k]["plate"] = p
    for k, v in L.items():
        io.open(os.path.join(OUT, 'lesson-%s.json' % k), 'w', encoding='utf-8').write(json.dumps(v, ensure_ascii=False, indent=1))
        print(k, len(json.dumps(v, ensure_ascii=False).encode()))
