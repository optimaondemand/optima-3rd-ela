#!/usr/bin/env python3
"""Week 19 DATA (The Whipping Boy, Ch. 6-11): 19.1-19.4 and the fluency page.
Every plot line checked against Planning docs/whipping_boy_ocr.txt."""
import json, io, os
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'data')
S = "<strong>"; E = "</strong>"

def dol(a_raw, a_fixed, a_why, b_raw, b_fixed, b_why):
    return {"a": {"raw": a_raw, "fixed": a_fixed, "why": a_why}, "b": {"raw": b_raw, "fixed": b_fixed, "why": b_why}}

GLOSS = [
 {"w": "whipping boy", "cs": True, "m": "a boy kept in the castle to be punished whenever the prince does something wrong"},
 {"w": "ransom", "m": "money that kidnappers ask for before they let someone go"},
 {"w": "compound sentence", "m": "a sentence made of two complete thoughts joined by a word like and, but, or so"},
 {"w": "complete thought", "m": "a group of words that makes sense on its own, like The outlaw growled."},
 {"w": "root", "m": "the main part of a word. Other parts are added to the front or the end."},
 {"w": "syllable", "m": "one beat in a word. Can-dle has two."},
 {"w": "counterclaim", "m": "what someone who disagrees with you might say"},
 {"w": "conclusion", "m": "the last sentence of a paragraph. It says your big idea in a new way."},
]
NOTES_COMMON = {
 "wordParts": "The root port means “carry.” transport = carry across, import = carry in, export = carry out, report = carry back, portable = able to be carried.",
 "grammar": "A compound sentence joins two complete thoughts with a comma and a joining word: Jemmy wrote the note, and Billy watched.",
 "spelling": "When a word ends in a consonant + le, that consonant goes with the le to make the last syllable: ta·ble, can·dle, sim·ple."
}

# ── Fill the Wagon (Ch. 8: "A wagonload of gold at the very least. And jewels mixed in.")
WAGON = {
 "type": "wagon", "title": "Fill the Wagon",
 "sub": "Billy wants a wagonload of gold and jewels. Every right answer adds one.",
 "look": "This is the outlaws’ wagon. In Chapter 8, Jemmy tells Billy to ask the king for a whole wagonload of gold and jewels. Each sack has a label. You get one thing to sort at a time. Every right answer drops a gold coin or a jewel into the wagon. You add 8 each day this week. On Day 4 the wagon is full.",
 "todo": "Read the words on the card. Tap the sack where they belong. A right answer adds gold to the wagon.",
 "win": "Today’s 8 are in the wagon. Come back next lesson to add more.",
 "winWeek": "A wagonload of gold, with jewels mixed in! The wagon is full."
}
def it(t, b, why, miss):
    return {"t": t, "bin": b, "why": why, "miss": miss}

L = {}
# ───────────────────────────── 19.1 · Ch. 6–7
L["19-1"] = {
 "connector": "Last time, the outlaws grabbed the boys in the fog and saw the king’s crest on the saddle. Today they take the boys to their hideout. Watch for something golden in the prince’s basket, and watch what happens when the outlaws need someone to write.",
 "writingFocus": "counter",
 "plate": {"src": "art/wb/wb-forest-hut.jpg", "alt": "A painting of a small log hut in a clearing among tall pine trees",
   "credit": "Hut in the Forest · Ivan Shishkin, second half of the 1800s · Public domain",
   "look": "A small hut deep in a pine forest, painted by Ivan Shishkin more than 100 years ago. In Chapter 6, the outlaws lead the boys through thick pines to their hideout, a rickety hut with a moldy roof."},
 "dol": dol("thats your ransom your royal highness billy said grinning",
   S+"“T"+E+"hat"+S+"’"+E+"s your ransom"+S+", Y"+E+"our "+S+"R"+E+"oyal "+S+"H"+E+"ighness"+S+",”"+E+" "+S+"B"+E+"illy said"+S+","+E+" grinning"+S+"."+E,
   "Quotation marks go around Billy’s exact words. That’s needs an apostrophe for the missing i. Your Royal Highness is a title, so each word gets a capital, and a comma comes before it. A comma goes inside the closing quotation mark. Billy is a name. A comma comes before grinning, and a period ends the sentence.",
   "heres your supper your young majesty cutwater said laughing",
   S+"“H"+E+"ere"+S+"’"+E+"s your supper"+S+", Y"+E+"our "+S+"Y"+E+"oung "+S+"M"+E+"ajesty"+S+",”"+E+" "+S+"C"+E+"utwater said"+S+","+E+" laughing"+S+"."+E,
   "Quotation marks go around Cutwater’s exact words. Here’s needs an apostrophe for the missing i. Your Young Majesty is a title, so each word gets a capital, and a comma comes before it. A comma goes inside the closing quotation mark. Cutwater is a name. A comma comes before laughing, and a period ends the sentence."),
 "hints": {
  "fill1": {"h1": "Look at the word bank. Which word part means carry?", "why": "trans + port: to carry across."},
  "fill2": {"h1": "Something is carried in. Which bank word means carry?", "why": "im + port: to carry in."},
  "fill3": {"h1": "Something is carried out. Which bank word means carry?", "why": "ex + port: to carry out."},
  "fill4": {"h1": "News is carried back. Which bank word means carry?", "why": "re + port: to carry back."}
 },
 "miss": {"match": {
   "scheme": "A scheme is something you think up. Look for the meaning about a plan.",
   "ransom": "A ransom is about money. Look for the meaning about a prisoner.",
   "flummox": "Flummox is something you do to someone’s brain. Look for the meaning about confusing.",
   "amiss": "Amiss is how things are when something is off. Look for the meaning that says wrong."}},
 "flags": {"journal-q1": {"quote": False, "count": 1}, "journal-q2": {"quote": False, "count": 1}, "journal-q3": {"quote": True, "count": 1}},
 "scholar": {"journal-q1": "… and tell what Billy says he can be even richer than.",
   "journal-q2": "… and tell how the prince acts when it happens.",
   "journal-q3": "… and explain how Jemmy plays along when Billy decides he is the prince."},
 "copia": {"look": "One plain sentence about today’s chapters, and three empty boxes. Each box asks you to say the same idea in a new way.",
   "todo": "Rewrite the sentence three ways, one box at a time. Tap Show one way if you get stuck.",
   "seed": "Billy <b>lifted</b> a golden crown out of the basket.",
   "eg": ["In the gloom of the hut, Billy lifted a golden crown out of the basket.",
          "Billy <i>pulled</i> a golden crown out of the basket.",
          "Billy lifted a golden crown out of the prince’s wicker basket."]},
 "wordgame": dict(WAGON,
   bins=[{"id": "in", "label": "Carry in"}, {"id": "out", "label": "Carry out"},
         {"id": "across", "label": "Carry across"}, {"id": "back", "label": "Carry back"}],
   stepTitle="Which way is it carried?",
   items=[
    it("Ships bring bananas <b>into</b> our country from far away.", "in", "Bananas come in from another place. That is import: carry in.",
       {"out": "The bananas are coming into our country, not leaving it.", "across": "Look at the word into. Where are the bananas going?", "back": "Nothing is being brought back here. Look at the word into."}),
    it("A farmer sends apples <b>out</b> to other countries.", "out", "The apples leave the country. That is export: carry out.",
       {"in": "The apples are leaving, not coming in. Look at the word out.", "across": "Look at the word out.", "back": "The apples are not coming back. They go out."}),
    it("A big cart carries the king’s food <b>across</b> the bridge.", "across", "From one side to the other. That is transport: carry across.",
       {"in": "Look at the word across.", "out": "Look at the word across.", "back": "The cart goes over the bridge to the other side. Look at the word across."}),
    it("A rider carries news <b>back</b> to the castle.", "back", "The news goes back to where it started. That is report: carry back.",
       {"in": "Look at the word back.", "out": "Look at the word back.", "across": "Look at the word back."}),
    it("A trader brings silk <b>into</b> the king’s land.", "in", "The silk comes in. Carry in, like import.",
       {"out": "Look at the word into. The silk is coming in.", "across": "Look at the word into.", "back": "Look at the word into."}),
    it("A ferryman rows people <b>across</b> the river.", "across", "From one bank to the other side. Carry across, like transport.",
       {"in": "Look at the word across.", "out": "Look at the word across.", "back": "Look at the word across."}),
    it("A spy carries a secret <b>back</b> to his captain.", "back", "The secret goes back to the captain. Carry back, like report.",
       {"in": "Look at the word back.", "out": "Look at the word back.", "across": "Look at the word back."}),
    it("The town sends wool <b>out</b> on a ship.", "out", "The wool leaves the town. Carry out, like export.",
       {"in": "The wool is leaving. Look at the word out.", "across": "Look at the word out.", "back": "Look at the word out."}),
   ]),
 "glossary": GLOSS,
 "sayWords": ["scheme", "ransom", "flummox", "amiss"],
 "transcripts": {
  "welcome": "Hi, it’s Opti. Last time, two outlaws grabbed the boys in the fog and found the king’s crest on the saddle. Today we visit the outlaws’ hideout. Here’s a puzzle to carry with you: who’s the prince now? Keep your eyes on the boy who can write, and the boy who can’t.",
  "guide1": "Word work first. Today you’ll meet a very old root that comes from Latin. Four words share it. See if you can figure out what it means before the page tells you. After that, you’ll sort word groups by how many complete thoughts they hold. Take it one step at a time.",
  "guide2": "Before you read: Chapter 6 takes you into the outlaws’ hut, deep in the pine forest. Look around it the way Jemmy does. Then, in Chapter 7, the outlaws need someone to write a message. Watch Jemmy closely when that happens. He’s thinking fast.",
  "guide3": "Your opinion is getting strong. Today, try something brave: think about the other side. What would someone who disagrees with you say? Write it down fairly. Then explain why you still think you’re right. Good writers aren’t scared of the other side. They answer it."
 },
 "notes": dict(NOTES_COMMON,
   wgrd="Good readers think about why characters do what they do: what each one wants, and what he does to get it.",
   vocab=[["scheme", "a clever secret plan, often tricky or sneaky"], ["ransom", "money demanded in exchange for a prisoner"], ["flummox", "to confuse or trick someone completely"], ["amiss", "wrong; not the way it should be"]])
}
# ───────────────────────────── 19.2 · Ch. 8–9
L["19-2"] = {
 "connector": "The outlaws think Jemmy is the prince, and Jemmy is going along with it. Today he writes the ransom note while Billy watches every word. Listen to how a street boy talks when he pretends to be a prince.",
 "writingFocus": "flow",
 "plate": {"src": "art/wb/wb-scribe.jpg", "alt": "An old painting of a man in a red robe writing in a big book at a wooden desk",
   "credit": "Jean Miélot at his desk · unknown painter, Brussels, 1400s · Public domain",
   "look": "A writer named Jean Miélot at his desk, painted by hand in a book more than 500 years ago. Long ago, few people could read or write, and writers like him used a feather pen called a quill. In Chapter 8, Jemmy writes the ransom note with a hawk’s feather and beet juice."},
 "dol": dol("sign your name here ordered hold-your-nose billy",
   S+"“S"+E+"ign your name here"+S+",”"+E+" ordered "+S+"H"+E+"old-"+S+"Y"+E+"our-"+S+"N"+E+"ose "+S+"B"+E+"illy"+S+"."+E,
   "Quotation marks go around Billy’s exact words, and Sign starts them with a capital. A comma goes inside the closing quotation mark. Hold-Your-Nose Billy is a name, so each part gets a capital. A period ends the sentence.",
   "eat your bread whispered jemmy",
   S+"“E"+E+"at your bread"+S+",”"+E+" whispered "+S+"J"+E+"emmy"+S+"."+E,
   "Quotation marks go around Jemmy’s exact words, and Eat starts them with a capital. A comma goes inside the closing quotation mark. Jemmy is a name, so it gets a capital. A period ends the sentence."),
 "miss": {"match": {
   "obliged": "Obliged is a feeling. Look for the meaning about being thankful.",
   "scoundrel": "A scoundrel is a kind of person, and not a good one. Look for the villain meaning.",
   "gallows": "Gallows is a thing made of wood. Look for the meaning about a frame.",
   "scribblement": "Scribblement is Cutwater’s made-up word. Look for the meaning about writing."}},
 "flags": {"journal-q1": {"quote": False, "count": 1}, "journal-q2": {"quote": False, "count": 1}, "journal-q3": {"quote": True, "count": 1}},
 "scholar": {"journal-q1": "… and tell what the prince says about Jemmy’s letters.",
   "journal-q2": "… and tell how Jemmy signs the note.",
   "journal-q3": "… and explain why Jemmy might want the whipping boy to carry it."},
 "wordgame": dict(WAGON,
   bins=[{"id": "yes", "label": "Compound sentence"}, {"id": "no", "label": "Not compound"}],
   stepTitle="Compound or not?",
   items=[
    it("Billy wanted gold, but Jemmy wanted more.", "yes", "Two complete thoughts joined by a comma and but.",
       {"no": "Cover the word but. Billy wanted gold. Jemmy wanted more. Both sides make sense alone."}),
    it("Jemmy dipped the quill in beet juice.", "no", "One complete thought. There is no joining word.",
       {"yes": "Look for a joining word like and, but, or so. This sentence has only one thought."}),
    it("Cutwater gnawed on a pheasant, and Billy paced the hut.", "yes", "Two thoughts joined by a comma and and.",
       {"no": "Cover the word and. Can each side stand alone as a sentence?"}),
    it("The prince sat on the moldy straw.", "no", "One complete thought.",
       {"yes": "There is only one thought here, and no joining word."}),
    it("Billy could not read, so he tested Jemmy.", "yes", "Two thoughts joined by a comma and so.",
       {"no": "Cover the word so. Billy could not read. He tested Jemmy. Two sentences!"}),
    it("Jemmy read the note backward.", "no", "One complete thought.",
       {"yes": "Look for a joining word with a whole thought on each side. It is not here."}),
    it("The prince was hungry, so he nibbled the stale bread.", "yes", "Two thoughts joined by a comma and so.",
       {"no": "Cover the word so. Does each side make sense on its own?"}),
    it("Jemmy signed the note with a flourish.", "no", "One complete thought.",
       {"yes": "This sentence has one thought and no joining word."}),
   ]),
 "cards": [{
   "id": "backward", "kind": "backward", "tab": "reading", "after": "^\\W*Read: Ch",
   "title": "Read It Backward", "sub": "Try Billy’s test from Chapter 9",
   "look": "In Chapter 9, Billy wants to check the ransom note. He makes Jemmy read it backward, from the last word to the first. The real note ends with “Your Obedient Son,” so Jemmy starts with “Son Obedient Your.” Below are three short notes, already written backward.",
   "todo": "Read each note out loud from the last word to the first. Then tap the words in the right order. Last, answer the question.",
   "stepText": "Read the note out loud, starting with the last word. Then tap the words in the right order.",
   "notes": [
     {"title": "Note 1", "back": ["hungry.", "am", "I"], "done": "I am hungry. That is what the prince keeps saying!"},
     {"title": "Note 2", "back": ["herring.", "and", "bread", "Eat"], "done": "Eat bread and herring. That is the outlaws’ breakfast."},
     {"title": "Note 3", "back": ["garlic.", "like", "smells", "Billy"], "done": "Billy smells like garlic. He really does!"}
   ],
   "q": {"title": "Why read it backward?", "text": "Why does Billy make Jemmy read the note backward?",
     "opts": ["Billy can’t read. If Jemmy had made up the words, he would trip over them backward.",
              "Billy thinks the note sounds funnier backward.",
              "The king can only read notes that are written backward."],
     "a": 0,
     "why": "Billy can’t check the words himself. Reading backward is hard to fake, so if Jemmy reads it smoothly, the words must really be on the paper.",
     "miss": {"1": "Billy is not trying to be funny. He wants to know if the note says what Jemmy told him.",
              "2": "The king reads notes the normal way. This test is for Jemmy."}},
   "finish": "Jemmy read the real note backward twice before Billy was satisfied."}],
 "glossary": GLOSS,
 "sayWords": ["obliged", "scoundrel", "gallows", "scribblement"],
 "transcripts": {
  "welcome": "Welcome back, it’s Opti. The outlaws think Jemmy is the prince, and Jemmy is going along with it. Now he has to write a ransom note while two outlaws watch. As you read, think about this: how does a street boy act like a prince? And keep an eye on the real prince. He is not happy.",
  "guide1": "Word study time. You’ll match more words that share the root that means carry. Then you’ll find the two complete thoughts hiding inside long sentences. Here’s a tip: cover the joining word with your finger. If both sides still make sense on their own, you found them.",
  "guide2": "Before you read: Chapter 8 is all about the ransom note. Listen to how Jemmy talks when he pretends to be the prince. Then, in Chapter 9, Billy gives Jemmy a strange test. Watch closely, and ask yourself why Billy would think of it.",
  "guide3": "Today you’re a listener. Read your paragraph out loud, slowly, like you’re reading it to a friend. Your ears will catch things your eyes miss. Is there a spot where the sentences bump? A transition word can smooth it right out.",
  "card-backward": "Billy and Cutwater can’t read the note Jemmy wrote. So in Chapter 9, Billy makes Jemmy read it backward, from the last word to the first. Now you try it. Turn each note around. Then think about why Billy wanted it read that way."
 },
 "notes": dict(NOTES_COMMON,
   wgrd="Good readers notice when a character does something unexpected, like being kind to someone who has not been kind to him.",
   vocab=[["obliged", "grateful; thankful for a favor done"], ["scoundrel", "a dishonest or wicked person; a villain"], ["gallows", "a wooden frame used to hang criminals as punishment"], ["scribblement", "Cutwater’s word for writing"]])
}
# ───────────────────────────── 19.3 · Ch. 10–11
L["19-3"] = {
 "connector": "The ransom note is written. Now someone has to carry it to the castle, and nobody wants that job. Today the outlaws argue, Jemmy bosses them like a prince, and the real prince makes a choice that leaves Jemmy struck dumb.",
 "writingFocus": "conclusion",
 "plate": {"src": "art/wb/wb-horse.jpg", "alt": "A painting of a red-brown horse rearing up on its back legs against a plain background",
   "credit": "Whistlejacket (detail) · George Stubbs, about 1762 · Public domain",
   "look": "A real racehorse named Whistlejacket, painted by George Stubbs about 260 years ago. He was painted life-size. The boys rode out of the castle on one of the king’s own horses."},
 "dol": dol("the prince was furious for a long time",
   S+"T"+E+"he prince was furious for a long time"+S+"."+E,
   "The starts the sentence, so it gets a capital T. A period ends it. Nobody is talking, so there are no quotation marks.",
   "jemmy stared at the prince in surprise",
   S+"J"+E+"emmy stared at the prince in surprise"+S+"."+E,
   "Jemmy starts the sentence and is a name, so it gets a capital J. A period ends it. Nobody is talking, so there are no quotation marks."),
 "hints": {
  "mfill1": {"h1": "Say the two parts out loud, one right after the other.", "why": "trans + port: to carry across."},
  "mfill2": {"h1": "Put the first part right in front of port. No space.", "why": "im + port: to carry in."},
  "mfill3": {"h1": "Put the first part right in front of port. No space.", "why": "ex + port: to carry out."},
  "mfill4": {"h1": "This time the root comes first. Add the ending after it.", "why": "port + able: able to be carried."},
  "vcloze1": {"h1": "The prince will not budge, like a stubborn mule. Which bank word has mule in it?", "why": "mulishness means being stubborn like a mule."},
  "vcloze2": {"h1": "The boy refuses boldly. Which bank word means boldly refusing to obey?", "why": "defiant means boldly refusing to obey."},
  "vcloze3": {"h1": "It is a private talk to work something out. Which bank word means that?", "why": "a parley is a talk between two sides."},
  "vcloze4": {"h1": "He always does the opposite. Which bank word means that?", "why": "contrary means always doing the opposite."},
  "gfill1": {"h1": "Read until you have a whole thought. Stop before the joining word.", "why": "Jemmy ran, and the outlaw followed."},
  "gfill2": {"h1": "Find the joining word. The comma goes right before it.", "why": "It was cold, so they lit a fire."},
  "gfill3": {"h1": "Find the joining word. Which word comes just before it?", "why": "He was tired, but he kept going."},
  "gfill4": {"h1": "Find the joining word. Which word comes just before it?", "why": "The prince shouted, and Jemmy turned."}
 },
 "miss": {"match": {
   "mulishness": "Mulishness has the word mule in it. Look for the stubborn meaning.",
   "defiant": "Defiant means standing up and saying no. Look for the meaning about boldly refusing.",
   "parley": "A parley is a kind of talk. Look for the meaning about a conversation.",
   "contrary": "Contrary means doing the opposite. Look for that meaning."}},
 "flags": {"journal-q1": {"quote": False, "count": 1}, "journal-q2": {"quote": True, "count": 1}, "journal-q3": {"quote": False, "count": 2}},
 "scholar": {"journal-q1": "… and tell what Jemmy wanted the prince to do instead.",
   "journal-q2": "… and tell what Jemmy says back to him.",
   "journal-q3": "… and tell what the outlaws offer the prince when they come back."},
 "wordgame": dict(WAGON,
   bins=[{"id": "cle", "label": "Ends in consonant-le"}, {"id": "other", "label": "Other ending"}],
   stepTitle="Which ending?",
   items=[
    it("saddle", "cle", "sad · dle: the d goes with the le.", {"other": "Look at the last three letters: d, l, e. A consonant, then le."}),
    it("wagon", "other", "wagon ends in on, not le.", {"cle": "Look at the last two letters. Are they l then e?"}),
    it("cradle", "cle", "cra · dle: the d goes with the le.", {"other": "Look at the last three letters: d, l, e."}),
    it("garlic", "other", "garlic ends in ic, not le.", {"cle": "Look at the last two letters. They are i and c."}),
    it("tumble", "cle", "tum · ble: the b goes with the le.", {"other": "Look at the last three letters: b, l, e."}),
    it("jewel", "other", "jewel ends in e then l. Consonant-le ends in l then e.", {"cle": "Look closely: jewel ends in e-l. Consonant-le words end in l-e."}),
    it("pebble", "cle", "peb · ble: the b goes with the le.", {"other": "Look at the last three letters: b, l, e."}),
    it("herring", "other", "herring ends in ing, not le.", {"cle": "Look at the last two letters. They are n and g."}),
   ]),
 "glossary": GLOSS,
 "sayWords": ["mulishness", "defiant", "parley", "contrary"],
 "transcripts": {
  "welcome": "Hi, it’s Opti. The ransom note is written. Now somebody has to carry it to the castle, and nobody wants that job. These two chapters are loud. People shout and stomp, and one boy makes a choice that leaves Jemmy speechless. As you read, ask yourself: why would he choose that?",
  "guide1": "Word work. You’ll build words that share the root that means carry, and you’ll find where the comma goes in a compound sentence. Here’s the trick: the comma sits right in front of the joining word, like a little doorstop. Then you’ll snap word parts together, one tile at a time.",
  "guide2": "Before you read: Chapter 10 is a battle of words. Jemmy uses big, bossy prince talk on the outlaws. Listen to how they react. In Chapter 11, the prince gets a chance most kids would grab. Watch what he does with it, and watch Jemmy’s face.",
  "guide3": "Every paragraph needs a good ending. A conclusion is your last word, the sentence a reader carries away. Don’t just copy your first sentence. Say your big idea in a fresh way, and make it sound finished, like closing a door."
 },
 "notes": dict(NOTES_COMMON,
   wgrd="Good readers notice when a character changes, even a little, and they ask why.",
   vocab=[["mulishness", "stubborn refusal to obey; acting like a mule"], ["defiant", "boldly refusing to obey"], ["parley", "a private talk between two sides, often enemies"], ["contrary", "always doing the opposite; hard to deal with"]])
}
# ───────────────────────────── 19.4 · look back, Ch. 6–11
L["19-4"] = {
 "connector": "No new chapters today. Look back at Chapters 6 to 11: the hut, the quill, the ransom note, and all that shouting. Who held the power in that hut? Today you put your whole opinion paragraph together.",
 "writingFocus": "paragraph",
 "plate": {"src": "art/wb/wb-crown.jpg", "alt": "An old painting of a golden crown covered in jewels, sitting on a red cushion",
   "credit": "The Imperial Crown · Johann Adam Delsenbach, 1751 · Public domain",
   "look": "A real emperor’s crown, made of gold and covered in jewels, drawn and painted by Johann Adam Delsenbach about 275 years ago. In this week’s chapters, the prince’s golden crown ends up in the outlaws’ hands."},
 "dol": dol("its not you they're looking for said the prince",
   S+"“I"+E+"t"+S+"’"+E+"s not you they’re looking for"+S+",”"+E+" said the prince"+S+"."+E,
   "Quotation marks go around the prince’s exact words, and It’s starts them with a capital. It’s needs an apostrophe because it means it is. A comma goes inside the closing quotation mark. A period ends the sentence.",
   "well send the whipping boy said billy",
   S+"“W"+E+"e"+S+"’"+E+"ll send the whipping boy"+S+",”"+E+" said "+S+"B"+E+"illy"+S+"."+E,
   "Quotation marks go around Billy’s exact words, and We’ll starts them with a capital. We’ll needs an apostrophe because it means we will. A comma goes inside the closing quotation mark. Billy is a name. A period ends the sentence."),
 "hints": {
  "vcloze1": {"h1": "Jemmy cannot understand it. Which bank word means to understand something deep?", "why": "fathom means to understand something deep."},
  "vcloze2": {"h1": "The outlaws get all mixed up. Which bank word means to confuse someone?", "why": "flummox means to confuse someone completely."},
  "vcloze3": {"h1": "The two outlaws step outside to talk. Which bank word is a talk between two sides?", "why": "parley means to talk things over."},
  "vcloze4": {"h1": "Cutwater thinks the prince is fishing for something. Which bank word means that?", "why": "angling means trying to get something in a clever way."}
 },
 "miss": {"match": {
   "fathom": "Fathom is about understanding. Look for that meaning.",
   "flummox": "Flummox is about confusing someone. Look for that meaning.",
   "parley": "A parley is a talk. Look for the meaning about two sides talking.",
   "angling": "Angling is like fishing for something. Look for that meaning."}},
 "flags": {"journal-q1": {"quote": False, "count": 2}, "journal-q2": {"quote": True, "count": 1}, "journal-q3": {"quote": False, "count": 2}},
 "scholar": {"journal-q1": "… and say whether you think it was a good choice.",
   "journal-q2": "… and explain what it might show about the prince.",
   "journal-q3": "… and say which kind of clever you think matters more."},
 "wordgame": dict(WAGON,
   bins=[{"id": "port", "label": "Has the root port (carry)"}, {"id": "comp", "label": "Compound sentence"}, {"id": "cle", "label": "Ends in consonant-le"}],
   stepTitle="Which sack?",
   items=[
    it("support", "port", "sup + port: to carry from under, like holding something up.", {"comp": "This is one word, not a sentence.", "cle": "support ends in ort. Find the root."}),
    it("The outlaws went outside, and the boys argued.", "comp", "Two complete thoughts joined by a comma and and.", {"port": "Look for a comma and a joining word.", "cle": "This is a sentence, not one word."}),
    it("needle", "cle", "nee · dle: the d goes with the le.", {"port": "Look at the last three letters: d, l, e.", "comp": "This is one word, not a sentence."}),
    it("export", "port", "ex + port: to carry out.", {"comp": "This is one word, not a sentence.", "cle": "export ends in ort. Find the root."}),
    it("The prince was offered gold, but he said no.", "comp", "Two complete thoughts joined by a comma and but.", {"port": "Look for a comma and a joining word.", "cle": "This is a sentence, not one word."}),
    it("bottle", "cle", "bot · tle: the t goes with the le.", {"port": "Look at the last three letters: t, l, e.", "comp": "This is one word, not a sentence."}),
    it("Jemmy wanted to slip away, but the prince would not leave.", "comp", "Two complete thoughts joined by a comma and but.", {"port": "Look for a comma and a joining word.", "cle": "This is a sentence, not one word."}),
    it("beetle", "cle", "bee · tle: the t goes with the le.", {"port": "Look at the last three letters: t, l, e.", "comp": "This is one word, not a sentence."}),
   ]),
 "glossary": GLOSS,
 "sayWords": ["fathom", "flummox", "parley", "angling"],
 "transcripts": {
  "welcome": "Welcome back, it’s Opti. No new chapters today. Instead, let’s look back at Chapters 6 through 11. A lot happened in that hut. Think about who held the quill, who gave the orders, and who surprised you. Today you’ll put your whole opinion paragraph together, all five parts.",
  "guide1": "Review day. You’ll roll the dice for words that share the root that means carry, and you’ll hunt for mistakes in compound sentences. Not every sentence has a mistake, so read each one carefully before you tap. Then fill the last sacks in the wagon.",
  "guide2": "No new reading today. Flip back through Chapters 6 to 11 and find the moments that stuck with you. Was there a time Jemmy surprised you? A time the prince did? Keep those pages in mind. They’ll help you answer the questions.",
  "guide3": "This is the big one. Today you put all five parts together: your claim, your reason, your example, the other side, and your conclusion. Read Clara’s paragraph first, and notice how each part leads to the next. Then build yours, one sentence at a time."
 },
 "notes": dict(NOTES_COMMON,
   wgrd="Good readers look back at the whole section and ask how each character has changed since the start.",
   vocab=[["fathom", "to understand something very deep or hard"], ["flummox", "to completely confuse someone"], ["parley", "a talk between two sides who disagree"], ["angling", "trying in a clever way to get something"]])
}
# ───────────────────────────── fluency
L["19-fluency"] = {
 "connector": "This week’s passage is the start of Chapter 11, where everybody is shouting. Read it three times, and give each person a voice.",
 "media": {"welcome": {"path": "guide/opti/g3ela-19-fluency-welcome", "label": "Opti’s welcome"}},
 "transcripts": {
  "welcome": "Hi, it’s Opti. This week’s passage is the start of Chapter 11, where everybody is shouting. Read it three times. First, get every word right. Next, make it smooth. Then give each person a voice: Jemmy amazed, the prince cold, and Billy loud. Have fun with it."
 }
}
if __name__ == '__main__':
    for k, v in L.items():
        io.open(os.path.join(OUT, 'lesson-%s.json' % k), 'w', encoding='utf-8').write(json.dumps(v, ensure_ascii=False, indent=1))
        print(k, len(json.dumps(v, ensure_ascii=False).encode()))
