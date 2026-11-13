#!/usr/bin/env python3
"""Week 20 DATA (The Whipping Boy, Ch. 11-15): 20.1-20.4 and the fluency page.
Every plot line checked against Planning docs/whipping_boy_ocr.txt (that edition prints "!" for "?")."""
import json, io, os
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'data')
S = "<strong>"; E = "</strong>"

def dol(a_raw, a_fixed, a_why, b_raw, b_fixed, b_why):
    return {"a": {"raw": a_raw, "fixed": a_fixed, "why": a_why}, "b": {"raw": b_raw, "fixed": b_fixed, "why": b_why}}

GLOSS = [
 {"w": "whipping boy", "cs": True, "m": "a boy kept in the castle to be punished whenever the prince does something wrong"},
 {"w": "ransom", "m": "money that kidnappers ask for before they let someone go"},
 {"w": "preposition", "m": "a small word in front of a noun that tells where, when, or how, like under, after, or with"},
 {"w": "root", "m": "the main part of a word. Other parts are added to the front or the end."},
 {"w": "syllable", "m": "one beat in a word. Im-por-tant has three."},
 {"w": "conclusion", "m": "the last sentence of a paragraph. It says your big idea in a new way."},
 {"w": "claim", "m": "the opinion your paragraph sets out to prove"},
]
NOTES_COMMON = {
 "wordParts": "The root spect means “look.” inspect = look closely into, spectator = one who looks on, respect = look again with care, inspector = one whose job is to look.",
 "grammar": "A preposition sits in front of a noun and ties it to the sentence. It can tell where (under the straw), when (after the storm), or how (with great care).",
 "spelling": "To read a long word, find the vowels, split between them, read each beat, then push the beats together: im·por·tant."
}

CHASE = {
 "type": "chase", "title": "The Chase",
 "sub": "Every right answer moves Jemmy one step closer to the hollow tree.",
 "todo": "Read the question. Tap the answer you think is right. A right answer moves Jemmy one step closer to the hollow tree.",
 "win": "Today’s 8 steps are done. Come back next lesson to keep running.",
 "winWeek": "Jemmy dove into the hollow tree. Cutwater ran right past!"
}
LOOK1 = "This week’s game is a chase through the forest. Who runs, and who chases? You’ll find out in Chapter 13. The stones are the path. Every right answer moves the runner one stone. You run 8 stones each day this week. On Day 4 you reach the hollow tree."
LOOK = "In Chapter 13, Jemmy runs through the forest with Cutwater close behind. The stones are the path. Every right answer moves Jemmy one stone, and Cutwater stays three stones back. You run 8 stones each day this week. On Day 4 Jemmy reaches the hollow tree."
WHERE = ["where", "when", "how"]
def q(title, qq, opts, a, why, miss):
    return {"title": title, "q": qq, "opts": opts, "a": a, "why": why, "miss": {str(k): v for k, v in miss.items()}}

L = {}
# ───────────────────────────── 20.1 · Ch. 11–12
L["20-1"] = {
 "connector": "You met the start of Chapter 11 last week, so skim it again to remember. Then read Chapter 12 closely. One outlaw rides off with the ransom note, and the other comes back to tie the boys up. Watch what the prince says when Cutwater asks a question.",
 "writingFocus": "evidence",
 "plate": {"src": "art/wb/wb-straw.jpg", "alt": "An old black-and-white print of a stable with horses and piles of straw on the floor", "credit": "Stable Interior · print after George Morland (1763–1804) · Smithsonian American Art Museum · CC0", "look": "An old print of a stable, made from a painting by George Morland, who lived more than 200 years ago. Straw covers the floor. In Chapter 12, the outlaws’ hut has a pile of moldy bed straw, and Jemmy finds a use for it."},
 "dol": dol("jemmy crept to the wooden door and pressed his ear against the cold oak",
   S+"J"+E+"emmy crept to the wooden door and pressed his ear against the cold oak"+S+"."+E,
   "Jemmy starts the sentence and is a name, so it gets a capital J. A period ends it. Nobody is talking, so there are no quotation marks.",
   "the owl sat on the branch and watched the hut",
   S+"T"+E+"he owl sat on the branch and watched the hut"+S+"."+E,
   "The starts the sentence, so it gets a capital T. A period ends it. Nobody is talking, so there are no quotation marks."),
 "hints": {
  "fill1": {"h1": "Look at the word bank. Which word part means look?", "why": "in + spect: to look into."},
  "fill2": {"h1": "The word starts with spect. Which ending makes a person who watches?", "why": "spect + ator: one who watches."},
  "fill3": {"h1": "Say suspect out loud. Is there an s sound twice? Look at the word bank again.", "why": "sus + pect: the s is shared, so only pect is left."},
  "fill4": {"h1": "Say expect out loud. The x already makes the s sound. Look at the word bank again.", "why": "ex + pect: the x hides the s."}
 },
 "miss": {"match": {
   "bewildered": "Bewildered is how Billy feels when he can’t understand what is happening. Look for the confused meaning.",
   "trifle": "A trifle is not worth much. Look for the meaning about a small thing.",
   "truss": "Cutwater wants to truss the boys like a Christmas goose. Look for the meaning about tying.",
   "ransom": "A ransom is about money. Look for the meaning about a prisoner."}},
 "flags": {"journal-q1": {"quote": True, "count": 1}, "journal-q2": {"quote": False, "count": 1}, "journal-q3": {"quote": False, "count": 1}},
 "scholar": {"journal-q1": "… and tell what Jemmy had asked the prince to say instead.",
   "journal-q2": "… and tell what Jemmy said he would do to the outlaws’ plan.",
   "journal-q3": "… and tell how the prince sounds when he says it."},
 "copia": {"look": "One plain sentence about today’s chapters, and three empty boxes. Each box asks you to say the same idea in a new way.",
   "todo": "Rewrite the sentence three ways, one box at a time. Tap Show one way if you get stuck.",
   "seed": "Jemmy <b>hid</b> under the straw.",
   "eg": ["In the dark hut, Jemmy hid under the straw.",
          "Jemmy <i>burrowed</i> under the straw.",
          "Jemmy hid under the moldy straw."]},
 "wordgame": dict(CHASE, look=LOOK1, items=[
   q("Where, when, or how?", "The fox hid <b>behind</b> the log. What does <b>behind the log</b> tell you?", WHERE, 0,
     "Behind the log is a place. It tells where.", {1: "Is behind the log a time? Think about a place.", 2: "Is it the way the fox hid? Think about a place."}),
   q("Where, when, or how?", "The owl hooted <b>at midnight</b>. What does <b>at midnight</b> tell you?", WHERE, 1,
     "Midnight is a time. It tells when.", {0: "Can you stand at midnight? It is a time, not a place.", 2: "It is not the way the owl hooted. Midnight is a time."}),
   q("Where, when, or how?", "Jemmy spoke <b>in a whisper</b>. What does <b>in a whisper</b> tell you?", WHERE, 2,
     "In a whisper is the way he spoke. It tells how.", {0: "A whisper is not a place. It is the way he spoke.", 1: "A whisper is not a time. It is the way he spoke."}),
   q("Find the preposition", "Which word is the preposition? <i>The boys waited until dark.</i>", ["boys", "waited", "until"], 2,
     "Until sits in front of dark and tells when.", {0: "Boys is a noun. Look for the small word in front of dark.", 1: "Waited is what the boys did. Look for the small word in front of dark."}),
   q("The root spect", "A <b>spectacle</b> is something big and amazing, like a parade. What do people do at a spectacle?", ["They look at it.", "They carry it.", "They write it down."], 0,
     "Spect means look. People stop and look at a spectacle.", {1: "Carry is the root port, from last week. Find spect in spectacle.", 2: "Find spect in spectacle. What does spect mean?"}),
   q("The root spect", "<b>Spectacular</b> fireworks are…", ["amazing to look at", "heavy to carry", "hard to hear"], 0,
     "Spect means look. Spectacular fireworks are amazing to look at.", {1: "Find spect in spectacular. It is about looking.", 2: "Find spect in spectacular. It is about your eyes, not your ears."}),
   q("Count the beats", "Clap it: <b>butterfly</b>. How many beats?", ["2", "3", "4"], 1,
     "but · ter · fly: three beats.", {0: "Clap again: but, ter, fly.", 2: "Clap again: but, ter, fly."}),
   q("Count the beats", "Clap it: <b>elephant</b>. How many beats?", ["2", "3", "4"], 1,
     "el · e · phant: three beats.", {0: "Clap again: el, e, phant.", 2: "Clap again: el, e, phant."}),
 ]),
 "glossary": GLOSS,
 "sayWords": ["bewildered", "trifle", "truss", "ransom"],
 "virtue": None,
 "transcripts": {
  "welcome": "Hi, it’s Opti. Last week the prince said no to going home, and Jemmy talked the outlaws into sending the horse instead. Today, one outlaw rides away, and the boys are left with Cutwater. Jemmy has a plan. Will the prince help him, or not?",
  "guide1": "Word work first. Today you’ll meet a very old root. Three words share it. See if you can figure out what it means before the page tells you. Then you’ll learn the little words that tell where, when, and how.",
  "guide2": "Before you read: skim Chapter 11 again, since you met it last week. Then slow down for Chapter 12. Jemmy makes a plan to escape, and he needs the prince to say one thing. Watch what the prince says instead.",
  "guide3": "Good writers prove what they say. Today, check your examples. Does each one name a chapter and tell exactly what happened? If not, add the chapter and the detail."
 },
 "notes": dict(NOTES_COMMON,
   wgrd="Good readers read between the lines. When a character does not say how he feels, what he does shows it.",
   vocab=[["bewildered", "completely confused"], ["trifle", "a small thing that is not worth much"], ["truss", "to tie someone up tightly"], ["ransom", "money demanded to set a prisoner free"]])
}
# ───────────────────────────── 20.2 · Ch. 13–14
L["20-2"] = {
 "connector": "At the end of Chapter 12, the prince told Cutwater where Jemmy was hiding. Today Jemmy runs for it. Watch what Jemmy and the prince say to each other when the chase is over, and listen for a voice in the forest.",
 "writingFocus": "conclusion",
 "plate": {"src": "art/wb/wb-pine-forest.jpg", "alt": "A painting of bear cubs climbing a broken, fallen pine tree in a misty forest", "credit": "Morning in a Pine Forest · Ivan Shishkin and Konstantin Savitsky, 1889 · Public domain", "look": "Bear cubs on a fallen pine tree, painted in 1889. Ivan Shishkin painted the forest, and Konstantin Savitsky painted the bears. In Chapter 13, Jemmy runs through a forest like this one and finds something by an upturned tree."},
 "dol": dol("the prince stumbled through the dark tangled undergrowth",
   S+"T"+E+"he prince stumbled through the dark"+S+","+E+" tangled undergrowth"+S+"."+E,
   "The starts the sentence, so it gets a capital T. Dark and tangled both describe the undergrowth, so a comma goes between them. A period ends it.",
   "jemmy pushed through the thick thorny brambles",
   S+"J"+E+"emmy pushed through the thick"+S+","+E+" thorny brambles"+S+"."+E,
   "Jemmy starts the sentence and is a name, so it gets a capital J. Thick and thorny both describe the brambles, so a comma goes between them. A period ends it."),
 "miss": {"match": {
   "instinct": "Instinct is acting without stopping to think. Look for that meaning.",
   "foliage": "Foliage is something you find in a forest. Look for the meaning about leaves.",
   "tilt": "Jemmy ran at full tilt. Look for the meaning about going fast.",
   "bramble": "Brambles tear the boys’ clothes. Look for the meaning about a thorny bush."}},
 "flags": {"journal-q1": {"quote": False, "count": 3}, "journal-q2": {"quote": True, "count": 1}, "journal-q3": {"quote": False, "count": 2}},
 "scholar": {"journal-q1": "… and tell what animal Jemmy meets in the clearing.",
   "journal-q2": "… and tell what Jemmy says back to the prince.",
   "journal-q3": "… and tell who Petunia is."},
 "wordgame": dict(CHASE, look=LOOK, items=[
   q("Where, when, or how?", "Jemmy ran <b>through the tangle</b>. What does <b>through the tangle</b> tell you?", WHERE, 0,
     "The tangle is a place in the forest. It tells where.", {1: "Is the tangle a time? It is a place.", 2: "It is not the way he ran. It is a place."}),
   q("How many?", "How many prepositions? <i>Betsy came from the woods with a coil of rope.</i>", ["1", "2", "3"], 2,
     "From the woods, with a coil, of rope: three.", {0: "Look again. Find from, with, and one more small word.", 1: "Look again. There is one more small word after coil."}),
   q("Find the preposition", "Which word is the preposition? <i>The prince followed Jemmy into the brambles.</i>", ["followed", "into", "brambles"], 1,
     "Into sits in front of the brambles and tells where.", {0: "Followed is what the prince did. Look for the small word in front of the brambles.", 2: "Brambles is a noun. Look for the small word in front of it."}),
   q("Where, when, or how?", "The soldiers rode <b>along the river road</b>. What does it tell you?", WHERE, 0,
     "The river road is a place. It tells where.", {1: "Is the river road a time? It is a place.", 2: "It is not the way they rode. It is a place."}),
   q("The root spect", "A <b>prospector</b> searches rivers and hills for gold. Which part of the word tells you he looks?", ["pro", "spect", "or"], 1,
     "Spect means look. A prospector looks for gold.", {0: "Pro is at the front. Find the root that means look.", 2: "Or means a person who. Find the root that means look."}),
   q("Soft or hard?", "Say <b>cent</b>. Is the c soft or hard?", ["soft, like s", "hard, like k"], 0,
     "The next letter is e, so the c is soft. Cent sounds like sent.", {1: "Look at the letter after the c. It is e."}),
   q("Soft or hard?", "Say <b>goose</b>. Is the g soft or hard?", ["soft, like j", "hard, like g in go"], 1,
     "The next letter is o, so the g stays hard.", {0: "Look at the letter after the g. It is o, not e, i, or y."}),
   q("Count the beats", "Which word has three beats?", ["forest", "banana", "outlaw"], 1,
     "ba · na · na: three beats.", {0: "Clap it: for, est. Two beats.", 2: "Clap it: out, law. Two beats."}),
 ]),
 "glossary": GLOSS,
 "sayWords": ["instinct", "foliage", "tilt", "bramble"],
 "transcripts": {
  "welcome": "Welcome back, it’s Opti. The prince just gave away Jemmy’s hiding place. Now Jemmy has one chance, and he takes it. Today there’s a chase, a big surprise in a clearing, and an argument. As you read, ask yourself: does the prince have a point?",
  "guide1": "Word study. You’ll match more words with the root that means look, and you’ll hunt for prepositions. Most sentences have more than one. There’s a bonus too: c and g can make two different sounds.",
  "guide2": "Before you read: Chapter 13 moves fast, so hang on. After the chase, the boys argue. Listen to both sides. Then in Chapter 14, a girl comes through the woods calling for someone named Petunia.",
  "guide3": "A strong ending gives your reader something to think about. Today, try ending with a question, or a challenge. Make it sound finished."
 },
 "notes": dict(NOTES_COMMON,
   spelling="To read a long word, split it into beats: im·por·tant. The letters c and g go soft before e, i, or y: city, giant. Before other letters they stay hard: cave, goat.",
   wgrd="Good readers notice what characters say and how they say it. When two characters argue, each one may have a point.",
   vocab=[["instinct", "a natural way of acting without stopping to think"], ["foliage", "thick leaves and branches"], ["tilt", "at full tilt means as fast as you can go"], ["bramble", "a prickly, thorny bush"]])
}
# ───────────────────────────── 20.3 · Ch. 15
L["20-3"] = {
 "connector": "Jemmy and the prince have reached the river. Today they follow it toward the city, and Jemmy plans to give the prince the slip. Watch what the prince does on the mud flat, and what Jemmy does when he gets a ride.",
 "writingFocus": "edit",
 "plate": {"src": "art/wb/wb-mudflat.jpg", "alt": "A painting of a sailboat resting on wet sand and shallow water at low tide, under a gray sky", "credit": "Trouville at Low Tide · Eugène Boudin, between 1888 and 1895 · Yale University Art Gallery · Public domain", "look": "A harbor in France at low tide, painted by Eugène Boudin more than 125 years ago. When the tide goes out, the water drops and leaves wide, wet mud behind. In Chapter 15, Jemmy and the prince walk along a river mud flat at low tide."},
 "dol": dol("she whistled a sharp note and pointed toward the road",
   S+"S"+E+"he whistled a sharp note and pointed toward the road"+S+"."+E,
   "She starts the sentence, so it gets a capital S. A period ends it. Two actions joined by and need no comma.",
   "the old man cracked his whip and called to his horses",
   S+"T"+E+"he old man cracked his whip and called to his horses"+S+"."+E,
   "The starts the sentence, so it gets a capital T. A period ends it. Two actions joined by and need no comma."),
 "hints": {
  "mfill1": {"h1": "Say the two parts out loud, one right after the other.", "why": "in + spect: to look closely into."},
  "mfill2": {"h1": "Put the ending right after spect. No space.", "why": "spect + ator: one who looks on."},
  "mfill3": {"h1": "Put the first part right in front of spect. No space.", "why": "re + spect: to look again, with care."},
  "mfill4": {"h1": "This one has three parts. Push all three together.", "why": "in + spect + or: one whose job is to look."},
  "vcloze1": {"h1": "Read the vocabulary box. What does Jemmy call searching the mud?", "why": "mudlarking means searching river mud for things to sell."},
  "vcloze2": {"h1": "The boys walk below a raised bank beside the river. Which bank word means that?", "why": "an embankment is a raised bank beside a river."},
  "vcloze3": {"h1": "The birdcage is bent and old. Which bank word means beaten and worn out?", "why": "battered means beaten and damaged."},
  "vcloze4": {"h1": "Jemmy wants to sell it as firewood. Which bank word is wood from the river?", "why": "driftwood is wood washed up by the river."},
  "gfill1": {"h1": "It tells where. They go from one side of the stream to the other.", "why": "They waded across the shallow stream."},
  "gfill2": {"h1": "It tells where. The footsteps are farther away than the trees.", "why": "Footsteps came from beyond the trees."},
  "gfill3": {"h1": "It tells when. They got there while it was still light.", "why": "They reached the hut before nightfall."},
  "gfill4": {"h1": "It tells how. Nobody heard him go.", "why": "Jemmy slipped away without a sound."}
 },
 "miss": {"match": {
   "mudlarking": "Mudlarking is what Jemmy does on the mud flat. Look for the meaning about searching river mud.",
   "embankment": "An embankment is a place by the river. Look for the meaning about a raised bank.",
   "battered": "Battered describes something old and beaten up. Look for the meaning about worn out.",
   "driftwood": "Driftwood is wood. Look for the meaning about pieces the river washes up."}},
 "flags": {"journal-q1": {"quote": False, "count": 2}, "journal-q2": {"quote": False, "count": 1}, "journal-q3": {"quote": True, "count": 1}},
 "scholar": {"journal-q1": "… and tell what Jemmy hopes to sell.",
   "journal-q2": "… and tell what the prince called Jemmy’s mudlarking at first.",
   "journal-q3": "… and tell what Jemmy calls the prince when he shouts to Captain Nips."},
 "wordgame": dict(CHASE, look=LOOK, items=[
   q("Pick the preposition", "Jemmy rode ___ the coach with the potatoes.", ["inside", "under", "beyond"], 0,
     "Jemmy sat in the coach with the potatoes and the kettle. Inside fits.", {1: "Under the coach is in the mud! Where did Jemmy sit?", 2: "Beyond the coach is past it. Where did Jemmy sit?"}),
   q("Pick the preposition", "The coach was stuck ___ a mud hole.", ["in", "over", "after"], 0,
     "The wheels sank in the mud hole.", {1: "Over would mean above it. The coach is stuck.", 2: "After tells when. This sentence needs where."}),
   q("Pick the preposition", "The boys walked ___ the river toward the city.", ["along", "into", "under"], 0,
     "They followed the river, walking beside it. Along fits.", {1: "Into the river would get them wet! They walk beside it.", 2: "Under the river? They walk beside it."}),
   q("Pick the preposition", "The prince pulled a chair leg ___ the mud.", ["from", "into", "behind"], 0,
     "He picked it up out of the mud. From fits.", {1: "Into would push it down. He picks it up.", 2: "Behind tells a place next to something. He picks it up out of the mud."}),
   q("Build a spect word", "<b>spect</b> + <b>acle</b> makes which word?", ["spectacle", "speckle", "spectator"], 0,
     "spect + acle = spectacle, something big to look at.", {1: "Speckle has no spect in it. Push spect and acle together.", 2: "Spectator ends in ator. This one ends in acle."}),
   q("Split it", "Which way splits <b>pumpkin</b> into beats?", ["pum · pkin", "pump · kin", "pu · mpkin"], 1,
     "pump · kin: the vowels are u and i, and the split goes between p and k.", {0: "Say it slowly: pump, kin.", 2: "Say it slowly: pump, kin."}),
   q("Split it", "Which way splits <b>sandwich</b> into beats?", ["sand · wich", "sa · ndwich", "sandw · ich"], 0,
     "sand · wich: two beats, and each one is easy to read.", {1: "Say it slowly: sand, wich.", 2: "Say it slowly: sand, wich."}),
   q("Soft or hard?", "Say <b>giraffe</b>. Is the g soft or hard?", ["soft, like j", "hard, like g in go"], 0,
     "The next letter is i, so the g is soft.", {1: "Look at the letter after the g. It is i."}),
 ]),
 "glossary": GLOSS,
 "sayWords": [],
 "transcripts": {
  "welcome": "Hi, it’s Opti. The boys made it to the river. Jemmy says he’ll give the prince the slip as soon as he can. But the river has treasure in its mud, and a rickety old coach is stuck nearby. As you read, keep your eye on the prince. He does something small, and it matters.",
  "guide1": "Word work. Today you’ll build words with the root that means look, and you’ll pick the preposition that makes each sentence say what you mean. Then you’ll put long words back together, one beat at a time.",
  "guide2": "Before you read: Chapter 15 starts on a mud flat by the river. Watch what Jemmy picks up, and what the prince picks up. Then a coach comes along. Watch Jemmy when it drives away.",
  "guide3": "Real writers check their work before anyone else sees it. Today you’re the editor. Go through the checklist, one line at a time, and fix what you find."
 },
 "notes": dict(NOTES_COMMON,
   wgrd="Good readers figure out what a character is like from the small things he does.",
   vocab=[["mudlarking", "searching river mud for things to sell"], ["embankment", "a raised bank of earth beside a river"], ["battered", "beaten and damaged; worn out"], ["driftwood", "pieces of wood washed up by the river"]])
}
# ───────────────────────────── 20.4 · Ch. 11–15 review
L["20-4"] = {
 "connector": "No new chapters today. Look back at Chapters 11 to 15: the straw, the chase, Betsy, the mud flat, and the coach. In Chapter 12 the prince gave Jemmy away. In Chapter 15 Jemmy went back for him. Today you finish your opinion paragraph.",
 "writingFocus": "check",
 "plate": {"src": "art/wb/wb-coach.jpg", "alt": "A painting of a red and black coach full of passengers, pulled by four white horses along a dirt road", "credit": "The London–Faringdon Coach passing Buckland House · James Pollard, 1835 · Public domain", "look": "A real coach that carried people from London to Faringdon, painted by James Pollard in 1835. Horses pulled coaches like this along the roads. In Chapter 15, the boys ride in a rickety old coach that belongs to Captain Nips."},
 "dol": dol("betsy thought she heard a shout echo through the princes forest",
   S+"B"+E+"etsy thought she heard a shout echo through the prince"+S+"’"+E+"s forest"+S+"."+E,
   "Betsy starts the sentence and is a name, so it gets a capital B. The forest belongs to the prince, so prince’s needs an apostrophe. A period ends it.",
   "jemmy saw a smile on the princes face",
   S+"J"+E+"emmy saw a smile on the prince"+S+"’"+E+"s face"+S+"."+E,
   "Jemmy starts the sentence and is a name, so it gets a capital J. The face belongs to the prince, so prince’s needs an apostrophe. A period ends it."),
 "hints": {
  "vcloze1": {"h1": "The prince sticks to Jemmy like a little sea creature on a ship. Which bank word is that?", "why": "a barnacle sticks tight to rocks and ships."},
  "vcloze2": {"h1": "Jemmy knows danger is coming before he thinks about it. Which bank word means that?", "why": "instinct is acting without stopping to think."},
  "vcloze3": {"h1": "The boys hide beside a raised bank by the river. Which bank word means that?", "why": "an embankment is a raised bank beside a river."},
  "vcloze4": {"h1": "Jemmy has searched river mud for years. Which bank word means that?", "why": "mudlarking means searching river mud for things to sell."}
 },
 "miss": {"match": {
   "barnacle": "A barnacle sticks to things. Look for the meaning about a sea creature.",
   "instinct": "Instinct happens without thinking. Look for that meaning.",
   "embankment": "An embankment is beside a river. Look for the meaning about a raised wall of earth.",
   "mudlarking": "Mudlarking happens in the mud. Look for the meaning about searching river mud."}},
 "flags": {"journal-q1": {"quote": False, "count": 2}, "journal-q2": {"quote": False, "count": 1}, "journal-q3": {"quote": True, "count": 1}},
 "scholar": {"journal-q1": "… and tell what Jemmy calls the prince in Chapter 15.",
   "journal-q2": "… and tell what the boys see on the river road.",
   "journal-q3": "… and tell what Jemmy hears, and whose voice it is."},
 "wordgame": dict(CHASE, look=LOOK, items=[
   q("Which is right?", "Which sentence uses the right preposition?", ["The prince stood in the middle of the road.", "The prince stood at the middle on the road.", "The prince stood under the middle of the road."], 0,
     "In the middle of the road: that is where the prince stood.", {1: "Read it out loud. At the middle on the road sounds wrong.", 2: "Under the road? He would be in the dirt!"}),
   q("Find the preposition", "Which word is the preposition? <i>Captain Nips cracked his whip in the air.</i>", ["cracked", "in", "whip"], 1,
     "In sits in front of the air and tells where.", {0: "Cracked is what he did. Look for the small word in front of the air.", 2: "Whip is a noun. Look for the small word in front of the air."}),
   q("Where, when, or how?", "The coach stopped <b>with a jolt</b>. What does <b>with a jolt</b> tell you?", WHERE, 2,
     "With a jolt is the way it stopped. It tells how.", {0: "A jolt is not a place. It is the way the coach stopped.", 1: "A jolt is not a time. It is the way the coach stopped."}),
   q("Where, when, or how?", "The coach stopped <b>after a few minutes</b>. What does it tell you?", WHERE, 1,
     "A few minutes is time. It tells when.", {0: "Minutes are not a place. They are time.", 2: "It is not the way it stopped. Minutes are time."}),
   q("The root spect", "<b>spectacle</b>, <b>prospector</b>, <b>spectacular</b>. What do all three have to do with?", ["looking", "carrying", "writing"], 0,
     "They all have spect, and spect means look.", {1: "Carrying is the root port, from last week. These words have spect.", 2: "Find the part all three share. What does it mean?"}),
   q("Count the beats", "Clap it: <b>watermelon</b>. How many beats?", ["3", "4", "5"], 1,
     "wa · ter · mel · on: four beats.", {0: "Clap again: wa, ter, mel, on.", 2: "Clap again: wa, ter, mel, on."}),
   q("Count the beats", "Clap it: <b>dinosaur</b>. How many beats?", ["2", "3", "4"], 1,
     "di · no · saur: three beats.", {0: "Clap again: di, no, saur.", 2: "Clap again: di, no, saur."}),
   q("Soft or hard?", "Say <b>cabbage</b>. Listen to the first letter. Is the c soft or hard?", ["soft, like s", "hard, like k"], 1,
     "The next letter is a, so the c stays hard.", {0: "Look at the letter after the c. It is a, not e, i, or y."}),
 ]),
 "glossary": GLOSS,
 "sayWords": [],
 "transcripts": {
  "welcome": "Hi, it’s Opti. No new chapters today. Instead, think back over Chapters 11 to 15. In Chapter 12, the prince gave Jemmy away. In Chapter 15, Jemmy went back for him. What changed in between? That’s what we’ll look for today.",
  "guide1": "Word study review. You’ll roll words with the root that means look, fix prepositions that are doing the wrong job, and roll long words to split into beats.",
  "guide2": "No new chapters today. Flip back through Chapters 11 to 15 and find the moment you think changed the story most. Then do the Read Like a Writer box.",
  "guide3": "Today you finish. Check that your paragraph has all five parts: a claim, a reason, an example with a chapter, the other side, and a conclusion. Then say what you are proud of."
 },
 "notes": dict(NOTES_COMMON,
   wgrd="Good readers look back and find the moment that changed the story the most.",
   vocab=[["barnacle", "a sea creature that sticks tight to rocks and ships"], ["instinct", "a natural way of acting without stopping to think"], ["embankment", "a raised bank of earth beside a river"], ["mudlarking", "searching river mud for things to sell"]])
}
# ───────────────────────────── fluency
L["20-fluency"] = {
 "connector": "This week’s passage is the start of Chapter 13, where Jemmy runs for it. Read it three times. The last time, read it fast, like a chase.",
 "howto": True,
 "transcripts": {
  "welcome": "Hi, it’s Opti. This week’s passage is the start of Chapter 13. Jemmy bursts out of the straw and runs. Read it three times. First, get every word right. Next, make it smooth. Then read it fast and sharp, like your heart is pounding."
 }
}
for k in ('20-1', '20-2', '20-3', '20-4'):
    if L[k].get('virtue') is None: L[k].pop('virtue', None)

if __name__ == '__main__':
    for k, v in L.items():
        io.open(os.path.join(OUT, 'lesson-%s.json' % k), 'w', encoding='utf-8').write(json.dumps(v, ensure_ascii=False, indent=1))
        print(k, len(json.dumps(v, ensure_ascii=False).encode()))
