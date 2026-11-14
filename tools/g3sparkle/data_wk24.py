#!/usr/bin/env python3
"""Week 24 DATA (Medieval Nonfiction, part 2): 24.1-24.4. No fluency page this week.
History lines checked against standard sources (claude/g3-ela-wk24-audit.md); every article quote is the article's own
words after acc_wk24.py. Market Day items use only this week's word study (script/scribe = write; -ful, -less, -ness, -ly)
and none is an answer elsewhere on the week's pages (script describe manuscript inscription prescription prescribe scribble
scribe; hopeful hopeless fearful fearless kindness quickly powerful endless darkness peaceful harmless bravely restless
graceful sadness slowly brightness joyful worthless gently careful greatness quietly illness careless quickness kindly darkly)
or a film example (postscript, thankless; see teach_wk24.py)."""
import json, io, os
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'data')
S = "<strong>"; E = "</strong>"
def C(x): return S + x + E

def dol(a_raw, a_fixed, a_why, b_raw, b_fixed, b_why):
    return {"a": {"raw": a_raw, "fixed": a_fixed, "why": a_why}, "b": {"raw": b_raw, "fixed": b_fixed, "why": b_why}}

GLOSS = [
 {"w": "main idea", "m": "what a whole paragraph is mostly about. It is often in the first sentence.", "key": True},
 {"w": "topic sentence", "m": "the sentence that tells the main idea of a paragraph, often the first one"},
 {"w": "detail", "m": "one fact that helps prove the main idea"},
 {"w": "off the topic", "m": "a sentence that does not help the main idea, so it does not belong in that paragraph"},
 {"w": "cause", "m": "why something happens"},
 {"w": "effect", "m": "what happens because of a cause"},
 {"w": "Middle Ages", "cs": True, "m": "a time in history about 500 to 1,500 years ago, when there were castles, knights and kings in Europe"},
 {"w": "medieval", "m": "from the Middle Ages", "key": True},
 {"w": "base word", "m": "the main word before an ending is added. Hope is the base word in hopeful."},
 {"w": "expository", "m": "writing that explains or teaches facts about a topic"},
 {"w": "diligence", "m": "working hard and carefully, and not giving up", "key": True},
]
NOTES_COMMON = {
 "wordParts": "The root script or scribe means write. describe = to write about something. manuscript = written by hand. One root, two spellings.",
 "grammar": "A paragraph has one main idea, often in the first sentence (the topic sentence). The other sentences are details that support it. A sentence that does not support it is off the topic.",
 "spelling": "-ful means full of (hopeful). -less means without (hopeless). -ness turns a describing word into a thing (kindness). -ly tells how something was done (quickly)."
}
BIN = {"script": {"id": "script", "label": "script (write)", "ic": "📜"}, "scribe": {"id": "scribe", "label": "scribe (write)", "ic": "🪶"},
       "ful": {"id": "ful", "label": "-ful (full of)", "ic": "🍎"}, "less": {"id": "less", "label": "-less (without)", "ic": "🧺"},
       "ness": {"id": "ness", "label": "-ness (names a thing)", "ic": "🧀"}, "ly": {"id": "ly", "label": "-ly (tells how)", "ic": "🥖"}}
END = {"ful": "-ful", "less": "-less", "ness": "-ness", "ly": "-ly"}
def miss_for(right, bins, sentence=False):
    m = {}
    for b in bins:
        if b == right: continue
        if b in ("script", "scribe"):
            m[b] = "Look closely at the root. Is it spelled s c r i p t, or s c r i b e?" if right in ("script", "scribe") else "This word has no script or scribe in it. Look at its ending."
        elif sentence:
            m[b] = "Read the sentence again. Does the word need to tell how, name a thing, mean full of, or mean without?"
        elif right in ("script", "scribe"):
            m[b] = "Look for the root that means write. Which spelling do you see?"
        else:
            m[b] = "That stall sells words ending in %s. Cover the base word. What ending is left?" % END[b]
    return m
def it(t, right, why, bins, sentence=False):
    return {"t": t, "bin": right, "why": why, "miss": miss_for(right, bins, sentence)}
B1 = ["script", "scribe", "ful", "less"]; B4 = ["ful", "less", "ness", "ly"]
GAME = {"type": "market", "title": "Market Day",
        "sub": "Every right answer brings a customer to the medieval market.",
        "todo": "Read the word on the basket. Tap the stall that sells it. A right answer brings a customer to the market.",
        "stepTitle": "Which stall sells it?",
        "win": "Today’s 8 customers are at the market. Come back next lesson for more.",
        "winWeek": "The market square is full. Every stall did good business this week!"}
LOOK1 = ("This week’s game is a market square in a medieval town, like the one in Thursday’s article. "
         "Each stall sells one kind of word. The sign on the stall tells you which. "
         "Read the word on the basket, then tap the stall that sells it. Each right answer brings one customer. "
         "Today the stalls sell words with the root script, the root scribe, the ending -ful and the ending -less.")
LOOK = ("Each stall sells words with one ending: -ful, -less, -ness or -ly. Read the word on the basket, then tap the stall that sells it. "
        "Each right answer brings one more customer. The customers from earlier days are still shopping.")

def job(title, text):
    return [{"id": "job", "kind": "info", "tab": "reading", "after": "Pause", "before": True, "icon": "⭐",
             "title": "Job Spotlight: " + title, "sub": "A real job in the Middle Ages",
             "todo": "Read about this real job. Then read the two questions and the article.", "text": text}]

L = {}
# ───────────────────────────── 24.1 · How Castles Were Built
L["24-1"] = {
 "connector": "Last week you read about who lived in a castle. Today: how a castle was built, stone by stone. Every wall, ditch and bridge had a reason. Look for the cause, why it was built that way, and the effect, what it did.",
 "writingFocus": "inform",
 "dol": dol("the masons at conwy castle worked for king edward",
   C("T")+"he masons at "+C("C")+"onwy "+C("C")+"astle worked for "+C("K")+"ing "+C("E")+"dward"+C("."),
   "The starts the sentence. Conwy Castle is the name of one castle, so both words get capitals. King is a title right before his name, Edward. A period ends the sentence.",
   "workers carried stone to dover castle in wooden carts",
   C("W")+"orkers carried stone to "+C("D")+"over "+C("C")+"astle in wooden carts"+C("."),
   "Workers starts the sentence, so it gets a capital W. Dover Castle is the name of one castle. A period ends the sentence."),
 "hints": {
  "fill1": {"h1": "Look at the table above. Find the word that starts with de.", "why": "de + scribe = describe: to write down details about something."},
  "fill2": {"h1": "Look at the table above. Find the word that starts with manu.", "why": "manu + script = manuscript: written by hand."},
  "fill3": {"h1": "Look at the table above. Find the word that starts with in. Type everything after in.", "why": "in + scription = inscription: writing carved into something."},
  "fill4": {"h1": "It ends just like the in word above it.", "why": "pre + scription = prescription: a written order for medicine."},
  "vcloze1": {"h1": "Find the word for a deep ditch full of water.", "why": "A moat is a deep ditch filled with water around a castle."},
  "vcloze2": {"h1": "This worker cuts and places stone. Look for stone inside the word.", "why": "A stonemason is a skilled worker who builds with stone."},
  "vcloze3": {"h1": "This bridge could be pulled up. Look for bridge inside the word.", "why": "A drawbridge could be raised so no one could cross the moat."},
  "vcloze4": {"h1": "Find the word for the strongest tower in the middle of the castle.", "why": "The keep was the strongest inner tower, the last place to defend."}
 },
 "miss": {"match": {
   "moat": "A moat is a ditch. Look for the meaning about water around the castle.",
   "stonemason": "A stonemason is a person. Look for the meaning about a worker.",
   "drawbridge": "A drawbridge is a bridge. Look for the meaning about raising it.",
   "keep": "The keep is a tower. Look for the meaning about the last defense."}},
 "flags": {"journal-q1": {"quote": False, "count": 0}, "journal-q2": {"quote": False, "count": 1}, "journal-q3": {"quote": False, "count": 2}},
 "copia": {"look": "One plain sentence from the castle article, and three empty boxes. Each box asks you to say the same idea in a new way.",
   "todo": "Rewrite the sentence three ways, one box at a time. Tap Show one way if you get stuck.",
   "seed": "A drawbridge could be <b>raised</b> to block the entrance.",
   "eg": ["To block the entrance, a drawbridge could be raised.",
          "A drawbridge could be <i>pulled up</i> to block the entrance.",
          "A heavy wooden drawbridge could be raised to block the castle entrance."]},
 "wordgame": dict(GAME, look=LOOK1, bins=[BIN[b] for b in B1], items=[
   it("subscribe", "scribe", "sub + scribe: you write your name to sign up for something.", B1),
   it("thankful", "ful", "thank + ful: full of thanks.", B1),
   it("scripture", "script", "script + ure: holy writing, like the books scribes copied.", B1),
   it("spotless", "less", "spot + less: without a single spot.", B1),
   it("inscribe", "scribe", "in + scribe: to write or carve words into something.", B1),
   it("cheerful", "ful", "cheer + ful: full of cheer.", B1),
   it("helpless", "less", "help + less: without help.", B1),
   it("colorful", "ful", "color + ful: full of color.", B1),
 ]),
 "glossary": GLOSS, "sayWords": [],
 "cards": job("The Stonemason", [
   "A stonemason cut big blocks of stone and fit them together to build walls and towers.",
   "Masons learned the trade as apprentices, over many years.",
   "Many masons carved their own mark into the stones they shaped. You can still find these marks in old castles and churches."]),
 "transcripts": {
  "welcome": "Hi, it’s Opti. Last week you read about who lived in a castle. Today: how a castle was built. Look for the reason behind every wall and ditch.",
  "guide1": "Word work first. A root that means write, main ideas and details, and four endings you know.",
  "guide2": "Read how castles were built. Find one thing the builders did, and why.",
  "guide3": "Today you write your whole paragraph."
 },
 "notes": dict(NOTES_COMMON,
   wgrd="A cause is why something happens. The effect is what happens. Castles had thick walls because enemies attacked.",
   vocab=[["moat", "a deep ditch, often filled with water, around a castle"], ["stonemason", "a skilled worker who cuts and builds with stone"], ["drawbridge", "a bridge over a moat that can be raised to block the way in"], ["keep", "the strongest inner tower of a castle, used as a last defense"]])
}
# ───────────────────────────── 24.2 · Knights
L["24-2"] = {
 "connector": "Knights in stories always seem brave and perfect. Today’s article tells how a boy really became a knight, one step at a time, and what knights were supposed to be like. Look for why each step came before the next.",
 "writingFocus": "inform",
 "dol": dol("sir henry trained as a squire in kent",
   C("S")+"ir "+C("H")+"enry trained as a squire in "+C("K")+"ent"+C("."),
   "Sir is a title right before his name, Henry, so both get capitals. Kent is the name of a place. Squire is not a name, so it stays small. A period ends the sentence.",
   "the young page served lady margaret at windsor castle",
   C("T")+"he young page served "+C("L")+"ady "+C("M")+"argaret at "+C("W")+"indsor "+C("C")+"astle"+C("."),
   "The starts the sentence. Lady is a title right before her name, Margaret. Windsor Castle is the name of one castle. A period ends the sentence."),
 "hints": {
  "vcloze1": {"h1": "Find the word for the code of rules knights were supposed to follow.", "why": "Chivalry was the code: be brave, loyal and kind to the weak."},
  "vcloze2": {"h1": "This young helper polished armor and cared for the horse.", "why": "A squire served a knight while training to become one."},
  "vcloze3": {"h1": "Find the word for being made a knight with a tap of the sword.", "why": "To be dubbed is to be made a knight in a ceremony."},
  "vcloze4": {"h1": "Find the word for a contest where knights showed their skill.", "why": "A tournament was a contest of knights before a crowd."}
 },
 "miss": {"match": {
   "chivalry": "Chivalry is a set of rules. Look for the meaning about a code.",
   "squire": "A squire is a person. Look for the meaning about helping a knight.",
   "dubbed": "Dubbed is something that happens to you. Look for the meaning about the sword on the shoulder.",
   "tournament": "A tournament is an event. Look for the meaning about a contest."}},
 "flags": {"journal-q1": {"quote": False, "count": 0}, "journal-q2": {"quote": False, "count": 3}, "journal-q3": {"quote": False, "count": 1}},
 "wordgame": dict(GAME, look=LOOK, bins=[BIN[b] for b in B4], items=[
   it("playful", "ful", "play + ful: full of play.", B4),
   it("softness", "ness", "soft + ness: names the soft feeling as a thing.", B4),
   it("loudly", "ly", "loud + ly: tells how something was done.", B4),
   it("sleepless", "less", "sleep + less: without sleep.", B4),
   it("goodness", "ness", "good + ness: names being good as a thing.", B4),
   it("wishful", "ful", "wish + ful: full of wishing.", B4),
   it("proudly", "ly", "proud + ly: tells how. The squire stood proudly.", B4),
   it("cloudless", "less", "cloud + less: a sky without clouds.", B4),
 ]),
 "glossary": GLOSS, "sayWords": [],
 "cards": job("The Squire", [
   "A squire was a teenage boy training to be a knight, often from about age fourteen.",
   "He cleaned his knight’s armor, cared for his horses, and helped him dress for battle.",
   "He practiced with sword, shield and lance almost every day, often for several years."]),
 "transcripts": {
  "welcome": "Welcome back, it’s Opti. How did a boy become a knight? Not overnight! Today’s article tells the steps, in order.",
  "guide1": "Word study. Match script and scribe words, find main ideas, and hunt for endings.",
  "guide2": "Read about knights. Then watch my video in the Read Like a Writer box.",
  "guide3": "Today you fix your paragraph so every sentence fits your topic."
 },
 "notes": dict(NOTES_COMMON,
   wgrd="Look for why each step happens. A boy became a page, then a squire, then a knight. Each step got him ready for the next.",
   vocab=[["chivalry", "the code of honorable behavior for knights"], ["squire", "a young man serving a knight while training to become one"], ["dubbed", "made a knight in a ceremony, with the tap of a sword on the shoulder"], ["tournament", "a contest where knights competed to show their skill"]])
}
# ───────────────────────────── 24.3 · Medieval Towns
L["24-3"] = {
 "connector": "Close your eyes and picture a busy market: people shouting, animals in the street, bread in the oven. Today’s article takes you to a medieval town. Look for what made it so loud, so busy, and so smelly.",
 "writingFocus": "inform",
 "dol": dol("in the town of york merchants sold wool every week",
   C("I")+"n the town of "+C("Y")+"ork"+C(",")+" merchants sold wool every week"+C("."),
   "In starts the sentence. York is the name of a place. A comma comes after the opening part, In the town of York. A period ends the sentence.",
   "in old london bakers sold bread near the river thames",
   C("I")+"n old "+C("L")+"ondon"+C(",")+" bakers sold bread near the "+C("R")+"iver "+C("T")+"hames"+C("."),
   "In starts the sentence. London is a place. A comma comes after the opening part. River Thames is the name of one river, so both words get capitals. A period ends the sentence."),
 "hints": {
  "mfill1": {"h1": "There is only one part. Type it just as it is.", "why": "script: the written words of a play."},
  "mfill2": {"h1": "Say the two parts out loud, then say them fast as one word.", "why": "de + scribe = describe."},
  "mfill3": {"h1": "Say the two parts out loud, then say them fast as one word.", "why": "manu + script = manuscript: written by hand."},
  "mfill4": {"h1": "Say all three parts out loud. The last part makes the word a thing.", "why": "in + script + ion = inscription."},
  "gfill1": {"h1": "All three details are about young people learning a trade. Find that word in the bank.", "why": "The details are all about apprentices."},
  "gfill2": {"h1": "A cook, a stablehand and a guard. What did each one have in the castle?", "why": "The details are all about castle jobs."},
  "gfill3": {"h1": "Carts, roads and rivers: think about getting from place to place.", "why": "The details are all about travel."},
  "gfill4": {"h1": "Look at the first word of each detail.", "why": "The details are all about guilds."},
  "vcloze1": {"h1": "Find the word for a group of workers in the same trade.", "why": "A guild was a group of craftsmen in one trade."},
  "vcloze2": {"h1": "This person buys goods in one place and sells them in another.", "why": "A merchant buys and sells goods."},
  "vcloze3": {"h1": "These routes were for buying and selling goods.", "why": "Trade routes were roads for buying and selling."},
  "vcloze4": {"h1": "Find the word for a very big, important church.", "why": "A cathedral is a large, important church."}
 },
 "miss": {"match": {
   "guild": "A guild is a group. Look for the meaning about craftsmen in the same trade.",
   "merchant": "A merchant is a person. Look for the meaning about buying and selling for profit.",
   "trade": "Trade is something people do. Look for the meaning about buying and selling goods.",
   "cathedral": "A cathedral is a building. Look for the meaning about a church."}},
 "flags": {"journal-q1": {"quote": False, "count": 0}, "journal-q2": {"quote": False, "count": 3}, "journal-q3": {"quote": False, "count": 1}, "journal-q4": {"quote": False, "count": 2}},
 "wordgame": dict(GAME, look=LOOK, bins=[BIN[b] for b in B4], items=[
   it("weakness", "ness", "weak + ness: names being weak as a thing.", B4),
   it("neatly", "ly", "neat + ly: tells how something was done.", B4),
   it("freshness", "ness", "fresh + ness: the baker’s bread had freshness.", B4),
   it("sweetly", "ly", "sweet + ly: tells how. The minstrel sang sweetly.", B4),
   it("fairness", "ness", "fair + ness: names being fair as a thing.", B4),
   it("firmly", "ly", "firm + ly: tells how. He shook hands firmly.", B4),
   it("useless", "less", "use + less: without any use.", B4),
   it("handful", "ful", "hand + ful: as much as a hand is full of.", B4),
 ]),
 "glossary": GLOSS, "sayWords": [],
 "cards": job("The Barber-Surgeon", [
   "A barber in a medieval town did more than cut hair and shave beards.",
   "Barbers also pulled bad teeth and treated cuts and wounds.",
   "Stories say the red and white stripes on a barber pole are a reminder of that old job."]),
 "transcripts": {
  "welcome": "Hi, it’s Opti. Can you smell that? Today we visit a medieval town. It was loud, busy, and often smelly. Let’s find out why.",
  "guide1": "Word study. Build script and scribe words, name what details are about, and break words apart.",
  "guide2": "Read about medieval towns. Look for what you could see, hear and smell.",
  "guide3": "Today you check your paragraph for capitals and periods."
 },
 "notes": dict(NOTES_COMMON,
   wgrd="Details you can see, hear and smell help you picture a place. Ask what caused each one.",
   vocab=[["guild", "a group of craftsmen or merchants in the same trade"], ["merchant", "a person who buys and sells goods for profit"], ["trade", "the buying and selling of goods"], ["cathedral", "a large, important church"]])
}
# ───────────────────────────── 24.4 · Real vs. Imagined
L["24-4"] = {
 "connector": "You have read The Whipping Boy and two weeks of true articles. Now be a history detective. Which parts of the stories match real life long ago, and which parts did storytellers change? And why would they change them?",
 "writingFocus": "inform",
 "dol": dol("historians study old books from england and france",
   C("H")+"istorians study old books from "+C("E")+"ngland and "+C("F")+"rance"+C("."),
   "Historians starts the sentence. England and France are names of places. A period ends the sentence.",
   "scholars read stories about king arthur and his knights",
   C("S")+"cholars read stories about "+C("K")+"ing "+C("A")+"rthur and his knights"+C("."),
   "Scholars starts the sentence. King is a title right before his name, Arthur. Knights is not a name, so it stays small. A period ends the sentence."),
 "hints": {
  "vcloze1": {"h1": "Find the word for a person who studies the past.", "why": "A historian studies old records to learn about the past."},
  "vcloze2": {"h1": "Find the word that means true to the facts.", "why": "Accurate means correct and true to the facts."},
  "vcloze3": {"h1": "Find the word for making something seem more perfect than it was.", "why": "To idealize is to make something seem better than it really was."},
  "vcloze4": {"h1": "Find the word for facts that support a claim.", "why": "Evidence is the facts that support a claim."}
 },
 "miss": {"match": {
   "historian": "A historian is a person. Look for the meaning about someone who studies history.",
   "accurate": "Accurate describes something. Look for the meaning about being true.",
   "idealize": "Idealize is something you do. Look for the meaning about making it seem better.",
   "evidence": "Evidence is information. Look for the meaning about supporting a claim."}},
 "flags": {"journal-q1": {"quote": False, "count": 0}, "journal-q2": {"quote": False, "count": 3}, "journal-q3": {"quote": False, "count": 1}},
 "wordgame": dict(GAME, look=LOOK, stepTitle="Which ending fits?", bins=[BIN[b] for b in B4], items=[
   it("The knight rode <b>bold___</b> into the tournament.", "ly", "boldly: tells how he rode.", B4, True),
   it("The bakery was full of <b>sweet___</b>.", "ness", "sweetness: names the sweet smell as a thing.", B4, True),
   it("A good squire was <b>use___</b> to his knight.", "ful", "useful: full of use.", B4, True),
   it("Arguing with the king was <b>point___</b>.", "less", "pointless: without a point.", B4, True),
   it("The herald spoke <b>clear___</b> so the crowd could hear.", "ly", "clearly: tells how he spoke.", B4, True),
   it("The <b>damp___</b> of the old tower turned the stones green.", "ness", "dampness: names being damp as a thing.", B4, True),
   it("The merchant was <b>help___</b> to every customer.", "ful", "helpful: full of help.", B4, True),
   it("The page tried to walk <b>silent___</b> past the guards.", "ly", "silently: tells how he walked.", B4, True),
 ]),
 "glossary": GLOSS, "sayWords": [],
 "cards": job("The Scribe", [
   "A scribe was a person whose job was writing. The root scribe means write!",
   "Before there were printing presses, scribes copied every book by hand, letter by letter.",
   "Scribes also wrote down laws, letters and records. Much of what historians know about the Middle Ages comes from what scribes wrote."]),
 "transcripts": {
  "welcome": "Hi, it’s Opti. Today you get to be a history detective. Stories borrow from real life, and then they change things. Let’s find out what is real.",
  "guide1": "Word study review. Roll script and scribe words, find the sentence that wandered off, and pick endings.",
  "guide2": "Read the last article. Sort what is real from what stories made up.",
  "guide3": "Today you publish your paragraph."
 },
 "notes": dict(NOTES_COMMON,
   wgrd="Stories borrow from history but add imagination. Ask what is real, what was changed, and why a storyteller changed it.",
   vocab=[["historian", "a person who studies and writes about history using evidence"], ["accurate", "correct; true to the facts"], ["idealize", "to make something seem better or more perfect than it really is"], ["evidence", "facts used to support a claim"]])
}

if __name__ == '__main__':
    import sys
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    try:
        from plates_wk24 import PLATES as P
        for k, p in P.items(): L[k]["plate"] = p
    except ImportError: print('no plates yet')
    for k, v in L.items():
        io.open(os.path.join(OUT, 'lesson-%s.json' % k), 'w', encoding='utf-8').write(json.dumps(v, ensure_ascii=False, indent=1))
        print(k, len(json.dumps(v, ensure_ascii=False).encode()))
