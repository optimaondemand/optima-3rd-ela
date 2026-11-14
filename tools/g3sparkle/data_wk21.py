#!/usr/bin/env python3
"""Week 21 DATA (The Whipping Boy, Ch. 16-20): 21.1-21.4 and the fluency page.
Every plot line checked against Planning docs/whipping_boy_ocr.txt (that edition prints "!" for "?").
Game items use only this week's word study (front word parts re- un- pre- dis- mis-; to/two/too,
their/there/they're, its/it's, your/you're; prepositional phrases) and none is an answer elsewhere
on the week's pages (rebuild, unhappy, preview, disagree, misread, reread, unfair, preheat,
distrust, misspell, misplace, rewrite are page answers, so they stay out)."""
import json, io, os
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'data')
S = "<strong>"; E = "</strong>"

def dol(a_raw, a_fixed, a_why, b_raw, b_fixed, b_why):
    return {"a": {"raw": a_raw, "fixed": a_fixed, "why": a_why}, "b": {"raw": b_raw, "fixed": b_fixed, "why": b_why}}

GLOSS = [
 {"w": "whipping boy", "cs": True, "m": "a boy kept in the castle to be punished whenever the prince does something wrong"},
 {"w": "theme", "m": "the big lesson a story teaches. You can say it in one sentence."},
 {"w": "prefix", "m": "a word part at the front of a word that changes its meaning, like re in rebuild"},
 {"w": "homophones", "m": "words that sound the same but mean different things and are spelled differently, like to, two, and too"},
 {"w": "prepositional phrase", "m": "a group of words that starts with a preposition and ends on a noun, like under the straw"},
 {"w": "personification", "m": "writing about a thing as if it were a person, like a sea that crawls"},
 {"w": "conclusion", "m": "the last sentence of a paragraph. It says your big idea in a new way."},
]
NOTES_COMMON = {
 "wordParts": "These word parts go at the front of a word. re = again (rebuild), un = not (unhappy), pre = before (preview), dis = not (disagree), mis = wrong (misread).",
 "grammar": "A prepositional phrase starts with a preposition and ends on a noun: through the fog. It can tell where, when, or how.",
 "spelling": "Homophones sound the same but mean different things. to points (to the gate), two is the number 2, too means also or more than enough. their = belongs to them, there = a place, they’re = they are."
}
PLATES = {}   # filled in plates_wk21.py once the art is found (a missing plate hides its slot)

SEWER = {
 "type": "sewer", "title": "Out of the Sewer",
 "sub": "Every right tunnel moves Jemmy and the prince closer to daylight.",
 "todo": "Read the question. Tap the tunnel with the right answer. A right answer moves Jemmy and the prince closer to daylight.",
 "win": "Today’s 8 lamps are lit. Come back next lesson to keep going.",
 "winWeek": "Jemmy and the prince came out into the sunshine. The outlaws ran the wrong way!"
}
LOOK1 = "This week’s game is a map of an old city sewer: long brick tunnels under the streets. The little lamps are the way out. Each question is a fork with two tunnels. Tap the tunnel with the right answer, and the runners pass one lamp. You pass 8 lamps each day. On Day 4 you reach the daylight at the river."
LOOK = "In Chapter 19, Jemmy and the prince hide from the outlaws in the dark sewer. The little lamps are the way out. Each question is a fork with two tunnels. The right tunnel moves the boys one lamp closer to daylight. You pass 8 lamps each day. On Day 4 you reach the river."
def q(title, qq, opts, a, why, miss):
    return {"title": title, "q": qq, "opts": opts, "a": a, "why": why, "miss": {str(k): v for k, v in miss.items()}}
SIDE = {"21-1": [0, 1, 1, 0, 1, 0, 0, 1], "21-2": [1, 0, 0, 1, 1, 0, 1, 0], "21-3": [0, 1, 0, 1, 1, 0, 1, 0], "21-4": [1, 1, 0, 0, 1, 0, 1, 0]}
def sides(k, items):
    """Right answer is written first; this puts it in the left or right tunnel so the side is no clue."""
    for it, s in zip(items, SIDE[k]):
        if s != it["a"]:
            it["opts"] = it["opts"][::-1]; it["a"] = s
            it["miss"] = {str(1 - s): v for v in it["miss"].values()}
    return items
PF, HP, PP = "Front word parts", "Sound-alike words", "Prepositional phrases"

L = {}
# ───────────────────────────── 21.1 · Ch. 16–17
L["21-1"] = {
 "connector": "Last week Jemmy went back for the prince, and they rode off in Captain Nips’ potato coach. Today the coach is stopped on the river road. Jemmy hides. Watch what the prince says when the outlaws ask where the whipping boy went.",
 "writingFocus": "compare",
 "dol": dol("run now the prince ordered i wont wait for you",
   "“"+S+"R"+E+"un now"+S+"!”"+E+" the prince ordered. "+S+"“I"+E+" won"+S+"’"+E+"t wait for you"+S+"!”"+E,
   "Each thing the prince says gets its own quotation marks. Run and I start new sentences, so they get capitals. Won’t needs an apostrophe. The exclamation marks go inside the closing quotation marks.",
   "stop the coach jemmy shouted we left him behind",
   "“"+S+"S"+E+"top the coach"+S+"!”"+E+" Jemmy shouted. "+S+"“W"+E+"e left him behind"+S+"!”"+E,
   "Each thing Jemmy says gets its own quotation marks. Stop, Jemmy, and We get capitals. The exclamation marks go inside the closing quotation marks."),
 "hints": {
  "mfill1": {"h1": "Say re, then build. Push them together with no space.", "why": "re + build = rebuild: to build again."},
  "mfill2": {"h1": "Say un, then happy. Push them together.", "why": "un + happy = unhappy: not happy."},
  "mfill3": {"h1": "Say pre, then view. Push them together.", "why": "pre + view = preview: to view before."},
  "mfill4": {"h1": "Say dis, then agree. Push them together.", "why": "dis + agree = disagree: to not agree."},
  "mfill5": {"h1": "Say mis, then read. Push them together.", "why": "mis + read = misread: to read wrong."}
 },
 "miss": {"match": {
   "pluck": "Jemmy sees a cast-iron streak of it in the prince. Look for the meaning about courage.",
   "defiant": "Defiant is about standing firm. Look for the meaning about refusing to give in.",
   "girded": "The prince girded himself for the next blow. Look for the meaning about getting ready.",
   "snarling": "Snarling is a sound. Look for the meaning about a growl."}},
 "flags": {"journal-q1": {"quote": False, "count": 1}, "journal-q2": {"quote": True, "count": 1}, "journal-q3": {"quote": False, "count": 2}},
 "scholar": {"journal-q1": "… and tell what the prince says to Jemmy afterward about yelling.",
   "journal-q2": "… and tell what the prince does right after he gets up.",
   "journal-q3": "… and tell who calls the bear off, and how."},
 "copia": {"look": "One plain sentence about today’s chapters, and three empty boxes. Each box asks you to say the same idea in a new way.",
   "todo": "Rewrite the sentence three ways, one box at a time. Tap Show one way if you get stuck.",
   "seed": "The bear <b>ran</b> down the bank.",
   "eg": ["With a roar, the bear ran down the bank.",
          "The bear <i>charged</i> down the bank.",
          "The big, snarling bear ran down the bank."]},
 "wordgame": dict(SEWER, look=LOOK1, items=[
   q(PF, "Betsy slipped the rope back around the bear’s neck. She had to <b>retie</b> it. What does <b>retie</b> mean?", ["to tie again", "to not tie"], 0,
     "re means again. Retie means tie again.", {1: "That would be untie. Look for the meaning with again."}),
   q(PF, "The river road was <b>unsafe</b> with outlaws about. What does <b>unsafe</b> mean?", ["not safe", "safe before"], 0,
     "un means not. Unsafe means not safe.", {1: "Before would be pre. Which word part is at the front of unsafe?"}),
   q(PF, "A sign that points the wrong way can <b>mislead</b> you. What does <b>mislead</b> mean?", ["to lead the wrong way", "to lead again"], 0,
     "mis means wrong. Mislead means lead the wrong way.", {1: "Again would be re. Which word part is at the front of mislead?"}),
   q(HP, "Captain Nips had ___ horses pulling his coach.", ["two", "too"], 0,
     "two is the number 2.", {1: "too means also or more than enough. Here you need a number."}),
   q(HP, "The prince was whipped, and Jemmy was hurt ___. Which word means also?", ["too", "to"], 0,
     "too, with two o’s, can mean also.", {1: "to points somewhere. Here you need the word that means also."}),
   q(HP, "Hold-Your-Nose Billy ran ___ the river.", ["to", "two"], 0,
     "to points somewhere: to the river.", {1: "two is a number. Billy ran toward a place."}),
   q(PP, "Cutwater ran off <b>like a greyhound</b>. What does <b>like a greyhound</b> tell you?", ["how", "where"], 0,
     "like a greyhound tells how he ran: very fast.", {1: "A greyhound is not a place. It tells the way he ran."}),
   q(PP, "The rooster crowed <b>before dawn</b>. What does <b>before dawn</b> tell you?", ["when", "how"], 0,
     "Dawn is a time. Before dawn tells when.", {1: "It is not the way the rooster crowed. Dawn is a time."}),
 ]),
 "glossary": GLOSS,
 "sayWords": ["pluck", "defiant", "girded", "snarling"],
 "transcripts": {
  "welcome": "Hi, it’s Opti. Last week Jemmy went back for the prince. Now they’re riding in a coach full of potatoes, and somebody shouts, Stand and deliver! The outlaws are back. Today, watch the prince closely. He does something Jemmy never expected.",
  "guide1": "Word work first. You’ll meet five word parts that go at the front of a word. Then you’ll sort phrases that tell where, when, or how, and spell three words that sound exactly the same.",
  "guide2": "Before you read: Jemmy hides in Chapter 16, and the outlaws grab the prince. Watch what the prince says, and watch what he does not do. Then in Chapter 17, someone comes to help.",
  "guide3": "This week you compare Jemmy and the prince. Today, fill in the chart for each boy: how he started, how he ends, and what changed him."
 },
 "notes": dict(NOTES_COMMON,
   wgrd="In the last chapters of a book, good readers start to see its lesson. That lesson is called the theme.",
   vocab=[["pluck", "courage; being brave when things are hard"], ["defiant", "refusing to give in"], ["girded", "got ready for something hard"], ["snarling", "making a low, angry growl"]])
}
# ───────────────────────────── 21.2 · Ch. 18–19
L["21-2"] = {
 "connector": "Betsy and Petunia chased the outlaws off, and the coach rolled into the city. Today the boys walk through a busy fair. Then a news seller shouts something that makes Jemmy run. Watch where he runs, and who follows him.",
 "writingFocus": "compare",
 "dol": dol("the prince stumbled and grabbed jemmys sleeve",
   S+"T"+E+"he prince stumbled and grabbed "+S+"J"+E+"emmy"+S+"’"+E+"s sleeve"+S+"."+E,
   "The starts the sentence, so it gets a capital T. Jemmy is a name, so it gets a capital J. The sleeve belongs to Jemmy, so Jemmy’s needs an apostrophe. A period ends it.",
   "betsy laughed and patted petunias head",
   S+"B"+E+"etsy laughed and patted "+S+"P"+E+"etunia"+S+"’"+E+"s head"+S+"."+E,
   "Betsy starts the sentence and is a name, so it gets a capital B. Petunia is a name too. The head belongs to Petunia, so Petunia’s needs an apostrophe. A period ends it."),
 "miss": {"match": {
   "merriment": "Merriment is something Jemmy hears when the prince laughs. Look for the meaning about laughter.",
   "hubbub": "A hubbub is a noise. Look for the meaning about a busy crowd.",
   "broadside": "The news seller sells broadsides. Look for the meaning about a printed sheet.",
   "grain-fed": "The brewery rats eat the grain. Look for the meaning about being well fed."}},
 "flags": {"journal-q1": {"quote": True, "count": 1}, "journal-q2": {"quote": False, "count": 1}, "journal-q3": {"quote": False, "count": 2}},
 "scholar": {"journal-q1": "… and tell how Jemmy feels about fetching and carrying.",
   "journal-q2": "… and tell what Jemmy does right after he hears it.",
   "journal-q3": "… and tell what the prince says to Jemmy in the dark, just before."},
 "wordgame": dict(SEWER, look=LOOK, items=[
   q(PF, "Captain Nips could <b>reheat</b> the potatoes. What does <b>reheat</b> mean?", ["to heat again", "to not heat"], 0,
     "re means again. Reheat means heat again.", {1: "Look at the front part of reheat. Which meaning goes with re?"}),
   q(PF, "The cow lady said <b>unkind</b> things about Prince Brat. What does <b>unkind</b> mean?", ["not kind", "kind again"], 0,
     "un means not. Unkind means not kind.", {1: "Again would be re. Which word part is at the front of unkind?"}),
   q(HP, "The boys filled ___ kettle at the pump.", ["their", "there"], 0,
     "their means it belongs to them: their kettle.", {1: "there is a place. The kettle belongs to the boys."}),
   q(HP, "The big rats live down ___, by the brewery.", ["there", "their"], 0,
     "there is a place: down there.", {1: "their shows that something belongs to someone. Here you need a place."}),
   q(HP, "“___ coming!” Jemmy whispered.", ["They’re", "Their"], 0,
     "They’re means they are: They are coming.", {1: "Say they are in the blank. Does it fit? Pick the word with the apostrophe."}),
   q(HP, "Petunia balanced a hat on ___ nose.", ["its", "it’s"], 0,
     "its shows belonging, with no apostrophe: its nose.", {1: "it’s means it is. Say it is nose. Does that make sense?"}),
   q(HP, "“___ black as night in here!” said the prince.", ["It’s", "Its"], 0,
     "It’s means it is: It is black as night.", {1: "Say it is in the blank. It fits, so you need the apostrophe."}),
   q(PP, "They sloshed through the dark sewer. Which part is the prepositional phrase?", ["through the dark sewer", "They sloshed"], 0,
     "It starts with the preposition through and ends on the noun sewer.", {1: "A prepositional phrase starts with a word like through or under."}),
 ]),
 "glossary": GLOSS,
 "sayWords": ["merriment", "hubbub", "broadside", "grain-fed"],
 "transcripts": {
  "welcome": "Welcome back, it’s Opti. The coach made it to the city, and today there’s a fair, with jugglers, hot potatoes, and a dog-and-rat pit. But a news seller is shouting about the whipping boy. As you read, listen for one small word the prince uses.",
  "guide1": "Word study. You’ll match words with front word parts to their meanings. Then it’s a double spelling day: their, there, and they’re, plus its and it’s.",
  "guide2": "Before you read: at the fair, the prince carries something for the first time in his life. Then Jemmy runs for the sewers. Watch what the prince does in the dark.",
  "guide3": "Today you write the first sentence of your comparison. Name both boys, and say how each one started."
 },
 "notes": dict(NOTES_COMMON,
   wgrd="Good readers notice small moments that mean a lot, like when a character calls someone a friend.",
   spelling="their = belongs to them, there = a place, they’re = they are. its = belongs to it, it’s = it is. The apostrophe always stands for missing letters.",
   vocab=[["merriment", "happy laughing and fun"], ["hubbub", "a loud, busy noise from a crowd"], ["broadside", "a big printed news sheet sold in the street"], ["grain-fed", "fed well on grain"]])
}
# ───────────────────────────── 21.3 · Ch. 20
L["21-3"] = {
 "connector": "The boys got out of the sewer, and the outlaws met the brewery rats. Today is the last chapter. The prince says they are going back to the castle. Watch his face when he tells Betsy and Captain Nips to turn Jemmy in.",
 "writingFocus": "compare",
 "dol": dol("they're waiting for us at the gate said jemmy",
   "“"+S+"T"+E+"hey’re waiting for us at the gate"+S+",”"+E+" said "+S+"J"+E+"emmy"+S+"."+E,
   "The words Jemmy says go inside quotation marks. They’re starts the sentence, so it gets a capital T. A comma goes inside the closing quotation mark. Jemmy is a name, so it gets a capital J. A period ends it.",
   "the reward is yours said the king",
   "“"+S+"T"+E+"he reward is yours"+S+",”"+E+" said the king"+S+"."+E,
   "The words the king says go inside quotation marks. The starts the sentence, so it gets a capital T. A comma goes inside the closing quotation mark. A period ends it."),
 "hints": {
  "mfill1": {"h1": "Say re, then read. Push them together.", "why": "re + read = reread: to read again."},
  "mfill2": {"h1": "Say un, then fair. Push them together.", "why": "un + fair = unfair: not fair."},
  "mfill3": {"h1": "Say pre, then heat. Push them together.", "why": "pre + heat = preheat: to heat before."},
  "mfill4": {"h1": "Say dis, then trust. Push them together.", "why": "dis + trust = distrust: to not trust."},
  "mfill5": {"h1": "Say mis, then spell. Keep both s’s.", "why": "mis + spell = misspell: to spell wrong. It has two s’s."},
  "vcloze1": {"h1": "Jemmy is so shocked he can’t speak. Which bank word means that?", "why": "dumfounded means so surprised you can’t speak."},
  "vcloze2": {"h1": "Look for the bank word that means a prisoner.", "why": "a convict is a prisoner sent away for a crime."},
  "vcloze3": {"h1": "The prince sounds like a king giving an order. Which bank word is an official order?", "why": "a decree is an official order from a ruler."},
  "vcloze4": {"h1": "The prince will keep Jemmy safe. Which bank word means keeping someone safe?", "why": "protection means keeping someone safe."},
  "gfill1": {"h1": "Jemmy hid under something moldy in the outlaws’ hut. Check the word bank.", "why": "under the moldy straw."},
  "gfill2": {"h1": "Bed made of what? Check the word bank.", "why": "on a pile of bed straw."},
  "gfill3": {"h1": "Captain Nips drives it. Check the word bank.", "why": "inside the potato coach."},
  "gfill4": {"h1": "Betsy and the bear stood up high, beside the river. Check the word bank.", "why": "at the top of the bank."}
 },
 "miss": {"match": {
   "dumfounded": "Jemmy stood dumfounded. Look for the meaning about being too shocked to speak.",
   "convict": "A convict is a person. Look for the meaning about a prisoner.",
   "decree": "A decree comes from a ruler. Look for the meaning about an order.",
   "protection": "Protection keeps someone safe. Look for that meaning."}},
 "flags": {"journal-q1": {"quote": False, "count": 2}, "journal-q2": {"quote": True, "count": 1}, "journal-q3": {"quote": False, "count": 1}},
 "scholar": {"journal-q1": "… and tell where the prince says Jemmy would have to hide.",
   "journal-q2": "… and tell what Jemmy thinks when he hears the promise.",
   "journal-q3": "… and tell what the king said to Jemmy first."},
 "wordgame": dict(SEWER, look=LOOK, items=[
   q(PF, "Jemmy had to <b>rethink</b> what the prince was doing. What does <b>rethink</b> mean?", ["to think again", "to think before"], 0,
     "re means again. Rethink means think again.", {1: "Before would be pre. Which word part is at the front of rethink?"}),
   q(PF, "What does <b>dishonest</b> mean?", ["not honest", "honest again"], 0,
     "dis can mean not. Dishonest means not honest.", {1: "Again would be re. Which word part is at the front of dishonest?"}),
   q(PF, "Before a big test, a teacher may give a <b>pretest</b>. What is a pretest?", ["a test before", "a wrong test"], 0,
     "pre means before. A pretest comes before the real test.", {1: "Wrong would be mis. Which word part is at the front of pretest?"}),
   q(PF, "The prince promised not to <b>misbehave</b>. What does <b>misbehave</b> mean?", ["to behave badly", "to behave again"], 0,
     "mis means wrong or badly. Misbehave means behave badly.", {1: "Again would be re. Which word part is at the front of misbehave?"}),
   q(HP, "The king looked at the ___ boys.", ["two", "too"], 0,
     "two is the number 2: two boys.", {1: "too means also or more than enough. Here you need a number."}),
   q(HP, "Jemmy wanted ___ run.", ["to", "two"], 0,
     "to sits in front of a verb: to run.", {1: "two is a number. Here the word sits in front of run."}),
   q(HP, "The golden doors opened, and ___ sat the king.", ["there", "their"], 0,
     "there is a place.", {1: "their shows belonging. Here you need a place."}),
   q(PP, "The prince stood <b>beside Jemmy</b>. Which word is the preposition?", ["beside", "stood"], 0,
     "beside sits in front of Jemmy and tells where.", {1: "stood is what the prince did. Look for the word in front of Jemmy."}),
 ]),
 "glossary": GLOSS,
 "sayWords": [],
 "transcripts": {
  "welcome": "Hi, it’s Opti. This is it, the very last chapter. The boys are out of the sewer, and the prince says, We’re going back to the castle. Jemmy has a price on his head! As you read, watch the prince’s face very closely.",
  "guide1": "Word work. Today you’ll build five new words with front word parts, find the noun at the end of each phrase, and pick the right sound-alike word.",
  "guide2": "Before you read: the prince does something that looks like a betrayal. Keep reading. Then the boys stand before the king. Listen for the promise the prince made.",
  "guide3": "Today you write the middle of your comparison: one way the boys changed the same, and one way they changed differently."
 },
 "notes": dict(NOTES_COMMON,
   wgrd="The theme is the big lesson a story wants you to take away.",
   vocab=[["dumfounded", "so surprised you can’t speak"], ["convict", "a prisoner sent away for a crime"], ["decree", "an official order from a ruler"], ["protection", "keeping someone safe"]])
}
# ───────────────────────────── 21.4 · Ch. 16–20 review
L["21-4"] = {
 "connector": "You finished the book! No new chapters today. Look back at Chapters 16 to 20: the whipping on the embankment, the bear, the fair, the sewer, and the throne room. Today you finish your comparison and say what the story teaches.",
 "writingFocus": "compare",
 "dol": dol("you kept me safe through all of it the prince murmured",
   "“"+S+"Y"+E+"ou kept me safe through all of it"+S+",”"+E+" the prince murmured"+S+"."+E,
   "The words the prince says go inside quotation marks. You starts the sentence, so it gets a capital Y. A comma goes inside the closing quotation mark. A period ends it.",
   "ill do my lessons the prince promised",
   "“"+S+"I’"+E+"ll do my lessons"+S+",”"+E+" the prince promised"+S+"."+E,
   "The words the prince says go inside quotation marks. I’ll needs a capital I and an apostrophe. A comma goes inside the closing quotation mark. A period ends it."),
 "hints": {
  "vcloze1": {"h1": "The prince closes one eye at Jemmy. Which bank word is that?", "why": "a wink is a quick close of one eye."},
  "vcloze2": {"h1": "The prince thanks them for serving him well. Which bank word means in a fine, honorable way?", "why": "nobly means in a brave, honorable way."},
  "vcloze3": {"h1": "Jemmy sees courage in the prince. Which bank word means courage?", "why": "pluck means courage."},
  "vcloze4": {"h1": "The wink mixes Jemmy up for a moment. Which bank word means confused?", "why": "befuddled means confused."}
 },
 "miss": {"match": {
   "wink": "A wink is something you do with your eye. Look for that meaning.",
   "nobly": "Nobly is a way of acting. Look for the meaning about honor.",
   "pluck": "Pluck is something inside a person. Look for the meaning about courage.",
   "befuddled": "Befuddled is how Jemmy feels for an instant. Look for the meaning about being confused."}},
 "flags": {"journal-q1": {"quote": False, "count": 2}, "journal-q2": {"quote": False, "count": 1}, "journal-q3": {"quote": False, "count": 1}},
 "scholar": {"journal-q1": "… and tell what Jemmy says to Betsy to help the plan work.",
   "journal-q2": "… and tell what the prince says about yowling and bellowing.",
   "journal-q3": "… and tell how the story would be different if the boys never became friends."},
 "wordgame": dict(SEWER, look=LOOK, items=[
   q(PF, "What does <b>unlock</b> mean?", ["to open a lock", "to lock before"], 0,
     "un can mean undo. Unlock means undo the lock.", {1: "Before would be pre. Which word part is at the front of unlock?"}),
   q(PF, "What does <b>recount</b> mean?", ["to count again", "to count wrong"], 0,
     "re means again. Recount means count again.", {1: "Wrong would be mis. Which word part is at the front of recount?"}),
   q(PF, "What does <b>disobey</b> mean?", ["to not obey", "to obey again"], 0,
     "dis means not. Disobey means not obey.", {1: "Again would be re. Which word part is at the front of disobey?"}),
   q(PF, "At first Jemmy <b>misjudged</b> the prince. What does <b>misjudge</b> mean?", ["to judge wrong", "to judge before"], 0,
     "mis means wrong. Misjudge means judge wrong.", {1: "Before would be pre. Which word part is at the front of misjudge?"}),
   q(HP, "“Is that ___ birdcage, Jemmy?”", ["your", "you’re"], 0,
     "your shows belonging: your birdcage.", {1: "you’re means you are. Say you are birdcage. Does that make sense?"}),
   q(HP, "“___ my friend,” said the prince.", ["You’re", "Your"], 0,
     "You’re means you are: You are my friend.", {1: "Say you are in the blank. It fits, so you need the apostrophe."}),
   q(HP, "The ballad seller sang ___ loud.", ["too", "to"], 0,
     "too means more than enough: too loud.", {1: "to points somewhere. Here you need more than enough."}),
   q(PP, "Petunia danced <b>with great skill</b>. What does <b>with great skill</b> tell you?", ["how", "when"], 0,
     "with great skill tells how Petunia danced.", {1: "Skill is not a time. It tells the way she danced."}),
 ]),
 "glossary": GLOSS,
 "sayWords": [],
 "transcripts": {
  "welcome": "Hi, it’s Opti. You finished The Whipping Boy! No new chapters today. Think about where Jemmy and the prince started, and where they ended up. Today you finish your comparison, and you say what the whole story teaches.",
  "guide1": "Word study review. You’ll roll words with front word parts, hunt for broken prepositional phrases, and roll sound-alike words.",
  "guide2": "No new chapters today. Look back through Chapters 16 to 20 for the moments that showed each boy changing.",
  "guide3": "Today you finish. Write a conclusion for your comparison, then one sentence that says what the story teaches."
 },
 "notes": dict(NOTES_COMMON,
   wgrd="Good readers think about the whole book once they finish it. What was the story really about?",
   vocab=[["wink", "a quick close of one eye"], ["nobly", "in a brave, honorable way"], ["pluck", "courage"], ["befuddled", "confused"]])
}
# ───────────────────────────── fluency
L["21-fluency"] = {
 "connector": "This week’s passage is from Chapter 17, when Petunia charges the outlaws. Read it three times. The last time, read the bear slow and the outlaws fast.",
 "howto": True,
 "transcripts": {
  "welcome": "Hi, it’s Opti. This week’s passage is from Chapter 17. A bear comes down the embankment, and the outlaws run! Read it three times. First, get every word right. Next, make it smooth. Then read the bear slow and low, and the outlaws fast."
 }
}
for k, p in PLATES.items(): L[k]["plate"] = p
for k in ("21-1", "21-2", "21-3", "21-4"): sides(k, L[k]["wordgame"]["items"])

if __name__ == '__main__':
    import sys
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    try:
        from plates_wk21 import PLATES as P
        for k, p in P.items(): L[k]["plate"] = p
    except ImportError: pass
    for k, v in L.items():
        io.open(os.path.join(OUT, 'lesson-%s.json' % k), 'w', encoding='utf-8').write(json.dumps(v, ensure_ascii=False, indent=1))
        print(k, len(json.dumps(v, ensure_ascii=False).encode()))
