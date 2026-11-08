#!/usr/bin/env python3
"""Week 18 DATA for 18.2, 18.3, 18.4 and the fluency page (18.1 is hand-written JSON)."""
import json, io, os
OUT = '/home/claude/g3/repo/data'
CONJ = ["and", "but", "so"]
def tw(title, q, opts, a, why, miss):
    return {"title": title, "q": q, "opts": opts, "a": a, "why": why, "miss": {str(k): v for k, v in miss.items()}}
TOWER = {
 "type": "tower", "title": "Up the North Tower",
 "sub": "Jemmy’s little room is at the top. Every right answer lights a step.",
 "look": "This is the north tower of the castle, where Jemmy sleeps. Tiny stairs zig-zag up the stone wall. You light 8 steps each day this week. On Day 4 you reach Jemmy’s window at the top.",
 "todo": "Read the question. Tap the answer you think is right. A right answer lights the next step.",
 "win": "Today’s 8 steps are lit. Come back next lesson to climb higher.",
 "winWeek": "You reached Jemmy’s window at the top of the north tower!"
}
GLOSS = [
 {"w": "whipping boy", "cs": True, "m": "a boy kept in the castle to be punished whenever the prince does something wrong"},
 {"w": "conjunction", "m": "a joining word, like and, but, or so"},
 {"w": "vowel team", "m": "two vowels side by side that make one sound, like ai in rain"},
 {"w": "syllable", "m": "one beat in a word. Rain-bow has two."},
 {"w": "claim", "m": "what you think, said in one clear sentence"},
 {"w": "reason", "m": "the why behind your opinion"},
]
NOTES_COMMON = {
 "wordParts": "inter- means “between” (interrupt, interact, international). sub- means “under” (submarine).",
 "grammar": "A conjunction is a joining word. and adds an idea, but shows a difference, and so shows a result.",
 "spelling": "A vowel team is two vowels that make one sound, like ai in rain. A team stays together in one syllable: rain·bow, sea·son."
}
def dol(a_raw, a_fixed, a_why, b_raw, b_fixed, b_why):
    return {"a": {"raw": a_raw, "fixed": a_fixed, "why": a_why}, "b": {"raw": b_raw, "fixed": b_fixed, "why": b_why}}
S = "<strong>"; E = "</strong>"

L = {}
# ───────────────────────────── 18.2 · Ch. 3–4
L["18-2"] = {
 "connector": "Last time, Jemmy took his whacks without a sound, and the prince went back on his word. Today the prince sneaks into Jemmy’s room at night with a plan. Read to find out what he wants, and why Jemmy has to go along.",
 "writingFocus": "reason",
 "plate": {"src": "art/wb/wb-fog-forest.jpg", "alt": "A dark forest clearing with fog lying low over the grass",
   "credit": "Glade in a Forest. Fog · Arkhip Kuindzhi, 1898–1908 · Public domain",
   "look": "A forest clearing on a foggy morning, painted by Arkhip Kuindzhi more than 100 years ago. In Chapter 4, a thick fog swirls in and the boys lose the road."},
 "dol": dol("i am not afraid of you jemmy said to billy",
   S+"“I"+E+" am not afraid of you"+S+",”"+E+" "+S+"J"+E+"emmy said to "+S+"B"+E+"illy"+S+"."+E,
   "Quotation marks go around Jemmy’s exact words. I is always a capital. A comma goes inside the closing quotation mark. Jemmy and Billy are names, so they get capitals. A period ends the sentence.",
   "stay close to me jemmy said to the prince",
   S+"“S"+E+"tay close to me"+S+",”"+E+" "+S+"J"+E+"emmy said to the prince"+S+"."+E,
   "Quotation marks go around Jemmy’s exact words, and Stay starts them with a capital. A comma goes inside the closing quotation mark. Jemmy is a name, so it gets a capital. A period ends the sentence."),
 "miss": {"match": {
   "astonishment": "Astonishment is a feeling, a really big one. Look for the meaning about great surprise.",
   "gallows": "Gallows is a thing, not a feeling. Look for the meaning about a frame.",
   "strayed": "Strayed is something you do with your feet when you get lost. Look for the meaning about wandering off.",
   "cutthroat": "A cutthroat is a kind of person, and not a nice one. Look for the meaning about a dangerous criminal."}},
 "flags": {"journal-q1": {"quote": False, "count": 2}, "journal-q2": {"quote": True, "count": 1}, "journal-q3": {"quote": True, "count": 1}},
 "scholar": {"journal-q1": "… and tell why the sewers would be a good place for Jemmy to hide.",
   "journal-q2": "… and explain what Jemmy is afraid they will do.",
   "journal-q3": "… and tell what this shows about the prince."},
 "wordgame": dict(TOWER, items=[
   tw("Pick the joining word", "Jemmy was tired, ___ he still got out of bed.", CONJ, 1, "but: being tired and getting up anyway push against each other.", {0: "and just adds an idea. These two halves push against each other.", 2: "so shows a result. Did being tired make him get up?"}),
   tw("Pick the joining word", "The prince was bored, ___ he decided to run away.", CONJ, 2, "so: being bored is the reason he runs away.", {0: "and just adds an idea. Here one half causes the other.", 1: "but shows a difference. Does running away go against being bored?"}),
   tw("Pick the joining word", "The fog was thick, ___ the trees closed in.", CONJ, 0, "and: both halves add more trouble.", {1: "but shows a difference. Both halves here are bad news.", 2: "so shows a result. The fog didn’t make the trees move."}),
   tw("Pick the joining word", "The prince wore a black cloak, ___ he carried a big basket.", CONJ, 0, "and: it adds one more thing he had.", {1: "but shows a difference. Nothing here pushes against anything.", 2: "so shows a result. The cloak didn’t cause the basket."}),
   tw("Pick the joining word", "Jemmy wanted to slip away, ___ a lantern glowed in the fog.", CONJ, 1, "but: the lantern gets in the way of his plan.", {0: "and just adds an idea. The lantern ruins his plan.", 2: "so shows a result. Wanting to slip away didn’t make the lantern appear."}),
   tw("Pick the joining word", "They were lost in the forest, ___ Jemmy got down to lead the horse.", CONJ, 2, "so: being lost is why Jemmy has to lead the horse.", {0: "and just adds an idea. Here one half is the reason for the other.", 1: "but shows a difference. Leading the horse makes sense when you’re lost."}),
   tw("Pick the joining word", "It was night, ___ the moon was bright.", CONJ, 1, "but: night is dark, yet the moon made it bright.", {0: "and just adds. Dark night and a bright moon push against each other.", 2: "so shows a result. The night didn’t make the moon bright."}),
   tw("Think it through", "Which joining word shows a <b>result</b>?", CONJ, 2, "so shows a result: this happened, so that happened.", {0: "and adds another idea.", 1: "but shows a difference."}),
 ]),
 "glossary": GLOSS,
 "sayWords": ["astonishment", "gallows", "strayed", "cutthroat"],
 "transcripts": {
  "welcome": "Hi, it’s Opti. Last time you met a prince who never gets punished and a boy who always does. Today the prince has a big idea, and it isn’t a good one. As you read, ask yourself: is being bored a good enough reason to drag someone else into danger? Then you’ll give your opinion a reason to stand on.",
  "guide1": "Word work first. Today you’ll match some long words to what they mean, and you’ll go hunting for joining words inside sentences. A joining word never comes alone. It brings a whole chunk of the sentence along with it. See if you can catch the word and its chunk together.",
  "guide2": "Before you read: the castle is about to disappear behind you. Chapter 3 happens at night, and Chapter 4 happens in a thick fog. Watch Jemmy closely. He’s thinking hard the whole time, even when he’s quiet. And keep an eye out for a glowing light.",
  "guide3": "Yesterday you wrote a claim. Today you give it a reason, the because behind your opinion. A strong reason comes from something a character really did, not just how you feel. Look back at today’s chapters and pick the one moment that proves your point best."
 },
 "notes": dict(NOTES_COMMON,
   wgrd="Good readers notice when a character makes a bad choice, and they ask who is responsible for what happens next.",
   vocab=[["astonishment", "a feeling of great surprise or shock"], ["gallows", "a frame used for hanging; Jemmy fears this punishment"], ["strayed", "wandered off the path by mistake"], ["cutthroat", "a dangerous criminal who would do anything for money"]])
}
# ───────────────────────────── 18.3 · Ch. 5
L["18-3"] = {
 "connector": "The boys are lost in the fog, and two strangers have grabbed them. Today you’ll meet those strangers up close. Listen for the names they call each other, and watch what happens every time the prince opens his mouth.",
 "writingFocus": "example",
 "plate": {"src": "art/wb/wb-highwayman.jpg", "alt": "An old black-and-white drawing of a man on horseback jumping a wooden gate",
   "credit": "Dick Turpin Jumping the Hornsey Tollgate · George Cruikshank, 1849 · Public domain",
   "look": "A drawing from an old storybook, printed in 1849. It shows a highwayman, a robber who stopped travelers on the road, jumping his horse over a gate. Hold-Your-Nose Billy in Chapter 5 is a highwayman too."},
 "dol": dol("cutwater was a thin man sharp as a knife blade and he moved like a shadow",
   S+"C"+E+"utwater was a thin man"+S+","+E+" sharp as a knife blade"+S+","+E+" and he moved like a shadow"+S+"."+E,
   "Cutwater is a name, so it gets a capital. Commas go around the describing part, sharp as a knife blade. And joins the last part. A period ends the sentence.",
   "billy was a big man loud as thunder and he smelled of garlic",
   S+"B"+E+"illy was a big man"+S+","+E+" loud as thunder"+S+","+E+" and he smelled of garlic"+S+"."+E,
   "Billy is a name, so it gets a capital. Commas go around the describing part, loud as thunder. And joins the last part. A period ends the sentence."),
 "hints": {
  "mfill1": {"h1": "Say the two parts out loud, one right after the other.", "why": "the part that means between, plus rupt (break): to break in between."},
  "mfill2": {"h1": "Put the first part in front of a word you already know.", "why": "the part that means between, plus act: to act between people."},
  "mfill3": {"h1": "The second part is a whole word. Stick the first part on the front.", "why": "the part that means between, plus national: between nations."},
  "mfill4": {"h1": "The second part has to do with the sea. Join them with no space.", "why": "the part that means under, plus marine (sea): a boat that goes under the sea."},
  "vcloze1": {"h1": "Which word in the bank names a rough, cruel person?", "why": "a ruffian is a rough, violent person, a bully."},
  "vcloze2": {"h1": "Ballad sellers sing about daring deeds. Which bank word means that?", "why": "an exploit is a bold, daring act."},
  "vcloze3": {"h1": "Who gets the throne after the king? Find that word in the bank.", "why": "the heir is the person who will get a throne or title."},
  "vcloze4": {"h1": "The outlaws want money in exchange for the prince. Which bank word is that?", "why": "a ransom is money paid to free a prisoner."},
  "gfill1": {"h1": "Cold and hungry are two troubles that go together. Which word adds one to the other?", "why": "and adds a second idea."},
  "gfill2": {"h1": "The lantern coming closer made them run. Which word shows a result?", "why": "so shows a result."},
  "gfill3": {"h1": "Being scared and walking anyway push against each other.", "why": "but shows a difference."},
  "gfill4": {"h1": "Shouting at someone usually gets an answer. Did it here?", "why": "but shows a difference: he shouted, yet Jemmy ignored him."}
 },
 "miss": {"match": {
   "ruffian": "A ruffian is a kind of person, a rough one. Look for the meaning about a bully or criminal.",
   "exploit": "An exploit is something someone does, the kind of thing people sing about. Look for the bold, daring act.",
   "heir": "An heir is the person next in line. Look for the meaning about getting a throne.",
   "ransom": "A ransom is money. Look for the meaning about paying to free a prisoner."}},
 "flags": {"journal-q1": {"quote": False, "count": 2}, "journal-q2": {"quote": True, "count": 1}, "journal-q3": {"quote": False, "count": 1}},
 "scholar": {"journal-q1": "… and explain why being famous might make Billy even more dangerous.",
   "journal-q2": "… and tell what this shows the outlaws care about most.",
   "journal-q3": "… and say what might have happened if the prince had stayed quiet."},
 "wordgame": dict(TOWER, items=[
   tw("Split the word", "Where does <b>rainbow</b> split into syllables?", ["rain · bow", "ra · inbow"], 0, "rain · bow keeps the ai team together.", {1: "That split pulls the a and i apart. A vowel team stays together."}),
   tw("Find the vowel team", "Which word has a vowel team?", ["trust", "feast", "melt"], 1, "feast: ea works as a team to make one sound.", {0: "trust has just one vowel, u.", 2: "melt has just one vowel, e."}),
   tw("Split the word", "Where does <b>season</b> split?", ["sea · son", "se · ason"], 0, "sea · son keeps the ea team together.", {1: "That split pulls the e and a apart. Keep the team in one syllable."}),
   tw("Find the vowel team", "Which word has a vowel team?", ["crisp", "damp", "gleam"], 2, "gleam: ea makes one long e sound.", {0: "crisp has just one vowel, i.", 1: "damp has just one vowel, a."}),
   tw("Split the word", "Where does <b>explain</b> split?", ["ex · plain", "expla · in"], 0, "ex · plain keeps the ai team together.", {1: "That split breaks the ai team. Find the team first."}),
   tw("Find the vowel team", "Which two letters make the vowel team in <b>road</b>?", ["oa", "ro"], 0, "oa makes the long o sound in road.", {1: "r is a consonant. Look for two vowels side by side."}),
   tw("Split the word", "Where does <b>peanut</b> split?", ["pea · nut", "pe · anut"], 0, "pea · nut keeps the ea team together.", {1: "That split pulls the e and a apart."}),
   tw("Split the word", "Where does <b>teacher</b> split?", ["tea · cher", "te · acher"], 0, "tea · cher keeps the ea team together.", {1: "That split breaks the ea team. Keep it in one beat."}),
 ]),
 "glossary": GLOSS + [{"w": "highwayman", "m": "a robber on horseback who stopped travelers on the road long ago"}],
 "sayWords": ["ruffian", "exploit", "heir", "ransom"],
 "cards": [{
   "id": "crest", "kind": "crest", "tab": "reading", "after": "^\\W*Read: Ch",
   "title": "The King’s Crest", "sub": "What Cutwater sees on the saddle",
   "look": "A dark night in the fog, and the saddle on the horse the boys rode from the castle. In Chapter 5, Cutwater holds his lantern up to the saddle and sees something important.",
   "todo": "Do Step 1 to see what Cutwater saw. Step 2 is just for fun.",
   "step1": "Look at the saddle", "step1p": "Tap the lantern to hold it up to the saddle, the way Cutwater does.",
   "art": {"file": "art/wb/wb-royal-standard.jpg", "alt": "Part of an old red and gold royal flag with lions and a crown", "title": "Royal Standard of Great Britain (detail)", "creator": "Unknown maker", "date": "1816–1837", "license": "Public domain"},
   "revealText": ["This is part of a real king’s flag, hand-painted about 200 years ago. The lions and the crown are the king’s family signs. A family’s special picture like this is called a <b>crest</b>.",
                  "The saddle in the story carries the king’s crest. That is how the outlaws figure out the horse came from the king’s own castle."],
   "step2": "Design your own crest", "step2p": "A crest tells people who your family is. Tap a color, tap a picture, and type one word that is true about you."
 }],
 "transcripts": {
  "welcome": "Hello, it’s Opti. Our runaways are in real trouble now. Two rough men have found them in the fog, and one of the boys can’t seem to stop talking. Today, think about this: when you’re in danger, is it smarter to stay quiet or to speak up? Watch what each boy chooses.",
  "guide1": "Today the word work asks you to use what you’ve learned. You’ll build words from their parts, fill in sentences with this week’s vocabulary, and join short sentences with the right joining word. Before you type, read each sentence in your head. Your ears often know the answer before your eyes do.",
  "guide2": "Before you read Chapter 5, a tip: notice the moment Jemmy uses his elbow instead of his voice. Authors often show what a character is thinking through what they do. And when the lantern comes close to the saddle, slow down. One small thing changes everything.",
  "guide3": "Today your opinion gets proof. A text example is a moment from the book that shows your reason is true, and you always say which chapter it came from. Go back to a chapter, find the moment, and tell what happened in your own words.",
  "card-crest": "Look closely at a king’s things, and you’ll often find his family’s signs, like lions and crowns. When the outlaws spot the king’s crest on the saddle, they know where that horse came from. Now it’s your turn. Design a crest that tells the world something about you."
 },
 "notes": dict(NOTES_COMMON,
   wgrd="Good readers notice how characters handle pressure: who keeps calm, who keeps talking, and why.",
   vocab=[["ruffian", "a rough, violent person; a bully or criminal"], ["exploit", "a bold, daring act, often sung about by ballad sellers"], ["heir", "the person who will inherit a throne or title"], ["ransom", "money paid or demanded to free a prisoner"]])
}
# ───────────────────────────── 18.4 · Ch. 1–5 review
L["18-4"] = {
 "connector": "You’ve read five chapters. Today there’s nothing new to read, so you get to look back like a detective. Who has the harder life, Jemmy or the prince? Gather your clues from the whole story, then check your opinion one last time.",
 "writingFocus": "revise",
 "plate": {"src": "art/wb/wb-tower.jpg", "alt": "A painting of a lonely stone tower on a hill under a cloudy sky",
   "credit": "Dolbadarn Castle (detail) · J. M. W. Turner, 1799–1800 · Public domain",
   "look": "A real castle tower in Wales, painted by J. M. W. Turner more than 200 years ago. It stands alone on a hill, a little like the north tower where Jemmy sleeps."},
 "dol": dol("the king crossed his arms and muttered disgusting",
   S+"T"+E+"he king crossed his arms and muttered"+S+", “D"+E+"isgusting"+S+".”"+E,
   "The starts the sentence, so it gets a capital T. A comma comes before the quotation. Quotation marks go around the word the king says, and it starts with a capital D. The period goes inside the closing quotation mark.",
   "the tutor shook his head and sighed hopeless",
   S+"T"+E+"he tutor shook his head and sighed"+S+", “H"+E+"opeless"+S+".”"+E,
   "The starts the sentence, so it gets a capital T. A comma comes before the quotation. Quotation marks go around the word the tutor says, and it starts with a capital H. The period goes inside the closing quotation mark."),
 "hints": {
  "vcloze1": {"h1": "The prince almost never feels sorry. Which bank word means truly sorry?", "why": "contrite means feeling truly sorry for something wrong."},
  "vcloze2": {"h1": "Jemmy can’t believe his ears. Which bank word means great surprise?", "why": "astonishment is great surprise."},
  "vcloze3": {"h1": "Billy grabs, threatens and sneers. Which bank word names that kind of person?", "why": "a ruffian is a rough, violent person."},
  "vcloze4": {"h1": "Jemmy is fed up with the prince. Which bank word means building frustration?", "why": "exasperation is frustration that keeps building."}
 },
 "miss": {"match": {
   "contrite": "Contrite is how you feel after doing wrong. Look for the meaning about feeling sorry.",
   "astonishment": "Astonishment is a big feeling of surprise. Look for that meaning.",
   "ruffian": "A ruffian is a kind of person, a rough one. Look for the bully meaning.",
   "exasperation": "Exasperation builds up when someone keeps bothering you. Look for the frustration meaning."}},
 "flags": {"journal-q1": {"quote": False, "count": 2}, "journal-q2": {"quote": False, "count": 2}, "journal-q3": {"quote": False, "count": 1}},
 "scholar": {"journal-q1": "… and say which part you think Jemmy minds the most.",
   "journal-q2": "… and explain how the whipping boy rule lets the pranks keep going.",
   "journal-q3": "… and explain whether the other boy is also a little bit responsible."},
 "wordgame": dict(TOWER, items=[
   tw("Word parts", "<b>interrupt</b> has the part that means…", ["between", "under"], 0, "inter- means between.", {1: "under is sub-. Look at how interrupt starts."}),
   tw("Pick the joining word", "Jemmy was scared, ___ he kept walking.", CONJ, 1, "but: scared and walking anyway push against each other.", {0: "and just adds. These halves push against each other.", 2: "so shows a result. Being scared doesn’t make you keep walking."}),
   tw("Split the word", "Where does <b>railroad</b> split?", ["rail · road", "ra · ilroad"], 0, "rail · road keeps both teams, ai and oa, together.", {1: "That split pulls the ai team apart."}),
   tw("Word parts", "A boat that goes under the sea is a…", ["submarine", "interact"], 0, "sub- (under) + marine (sea).", {1: "interact starts with the part that means between."}),
   tw("Pick the joining word", "The fog rolled in, ___ the boys got lost.", CONJ, 2, "so: the fog is why they got lost.", {0: "and just adds. Here one half causes the other.", 1: "but shows a difference. Getting lost in fog makes sense."}),
   tw("Find the vowel team", "Which word has a vowel team?", ["groan", "crisp"], 0, "groan: oa makes the long o sound.", {1: "crisp has just one vowel, i."}),
   tw("Think it through", "Which joining word <b>adds</b> an idea?", CONJ, 0, "and adds one more idea.", {1: "but shows a difference.", 2: "so shows a result."}),
   tw("Word parts", "A game played between many nations is…", ["international", "submarine"], 0, "inter- (between) + national.", {1: "submarine starts with the part that means under."}),
 ]),
 "glossary": GLOSS,
 "sayWords": ["contrite", "astonishment", "ruffian", "exasperation"],
 "transcripts": {
  "welcome": "Welcome back, it’s Opti. Today we look back at all five chapters. One boy has fine clothes and a king for a father. The other has rags and a lot of whacks. So here’s the big question: who really has the harder life? Hold on to your answer, because today you’ll check your whole opinion from top to bottom.",
  "guide1": "Word study review day. You’ll roll some dice, fix joining words that don’t fit, and fill in sentences with words from all week. When something feels tricky, think back to Day 1. The patterns haven’t changed. You’ve just gotten better at spotting them.",
  "guide2": "No new chapters today. Instead, think back over the whole story so far. Picture the feast, the tower, the fog, and the outlaws. Which moment tells you the most about the prince? Which one tells you the most about Jemmy? Keep those two moments in mind.",
  "guide3": "Time to be your own editor. Read your claim, your reason, and your example out loud. Does each part do its job? Does your example really prove your reason? Find one thing to make stronger. Even great writers fix their work before anyone else reads it."
 },
 "notes": dict(NOTES_COMMON,
   wgrd="Good readers step back and think about the whole section: who suffers more, and does either character deserve our sympathy?",
   vocab=[["contrite", "feeling truly sorry for something wrong you did"], ["astonishment", "complete surprise; unable to believe what you see"], ["ruffian", "a rough, violent person; a bully or criminal"], ["exasperation", "strong frustration that has been building up"]])
}
# ───────────────────────────── fluency
L["18-fluency"] = {
 "connector": "This week’s passage is the very first page of The Whipping Boy. Read it three times, and listen to your own voice get smoother each time.",
 "media": {"welcome": {"path": "guide/opti/g3ela-18-fluency-welcome", "label": "Opti’s welcome"}},
 "transcripts": {
  "welcome": "Hi, it’s Opti. This week’s passage is the very first page of The Whipping Boy. Read it three times. The first time, just get the words right. The second time, make it smooth. The third time, let your voice have fun with the prank. It really does get easier each time."
 }
}
for k, v in L.items():
    io.open(os.path.join(OUT, 'lesson-%s.json' % k), 'w', encoding='utf-8').write(json.dumps(v, ensure_ascii=False, indent=1))
    print(k, len(json.dumps(v, ensure_ascii=False).encode()))
