#!/usr/bin/env python3
"""Week 22 DATA (The Whipping Boy wrap-up, no new chapters): 22.1-22.4 and the fluency page.
Every plot line checked against Planning docs/whipping_boy_ocr.txt (that edition prints "!" for "?").
Game items use only this week's word study (the root struct; compound words; pronoun jobs) and
none is an answer or film example elsewhere in the week (construct, structure, instruct, destruct,
construction, instruction, destruction, obstruct, reconstruct, instructor, restructure; mailbox,
postcard, landmark, notebook, birthday, sidewalk, airplane, sunset, railroad, daylight, classroom,
rainbow, cupcake, doghouse, football, toothbrush stay out)."""
import json, io, os
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'data')
S = "<strong>"; E = "</strong>"

def dol(a_raw, a_fixed, a_why, b_raw, b_fixed, b_why):
    return {"a": {"raw": a_raw, "fixed": a_fixed, "why": a_why}, "b": {"raw": b_raw, "fixed": b_fixed, "why": b_why}}

GLOSS = [
 {"w": "whipping boy", "cs": True, "m": "a boy kept in the castle to be punished whenever the prince does something wrong"},
 {"w": "theme", "m": "the big lesson a story teaches. You can say it in one sentence."},
 {"w": "root", "m": "the main part of a word that holds its meaning, like struct in construct"},
 {"w": "compound word", "m": "two small words joined into one word, like rain + bow = rainbow"},
 {"w": "pronoun", "m": "a small word that takes the place of a name, like he, him, or his"},
 {"w": "personification", "m": "writing about a thing as if it were a person, like a cricket that is cheerful"},
 {"w": "Reader’s Theater", "cs": True, "m": "reading a scene out loud like a play, with a voice for each character"},
]
NOTES_COMMON = {
 "wordParts": "The root struct means build. construct = to build together. structure = something built. instruct = to build knowledge in someone.",
 "grammar": "A pronoun takes the place of a noun. Doing the action: I, he, she, we, they. Getting the action: me, him, her, us, them. Showing whose: my, his, her, their.",
 "spelling": "A compound word is two small words joined into one: rain + bow = rainbow. Read each part on its own, then blend them. A long word is not always a compound word."
}
PLATES = {}

CASTLE = {
 "type": "castle", "title": "Build the Castle",
 "sub": "Every right answer lays a stone in the castle wall.",
 "todo": "Read the question. Tap the answer you think is right. A right answer lays the next stone in the castle.",
 "win": "Today’s 8 stones are laid. Come back next lesson to keep building.",
 "winWeek": "The castle is built, from the ground to the flag!"
}
LOOK1 = "This week’s game is a castle that is not built yet. The root struct means build, so this week you build! The dashed boxes show where each stone goes. Each right answer lays one stone, from the bottom row up. You lay 8 stones each day. On Day 4 the castle gets its towers, its gate and its flag."
LOOK = "Each right answer lays one stone in the castle wall, from the bottom row up. You lay 8 stones each day. On Day 4 the castle gets its towers, its gate and its flag."
def q(title, qq, opts, a, why, miss):
    return {"title": title, "q": qq, "opts": opts, "a": a, "why": why, "miss": {str(k): v for k, v in miss.items()}}
SIDE = {"22-1": [1, 0, 1, 0, 0, 1, 1, 0], "22-2": [2, 1, 0, 1, 1, 0, 0, 1], "22-3": [1, 0, 0, 1, 1, 0, 1, 2], "22-4": [1, 0, 1, 0, 1, 1, 0, 1]}
def sides(k, items):
    """Right answer is written first; this moves it to SIDE's position so the place is no clue."""
    for it, s in zip(items, SIDE[k]):
        s = s % len(it["opts"])
        order = [i for i in range(len(it["opts"])) if i != it["a"]]
        order.insert(s, it["a"])
        newpos = {old: new for new, old in enumerate(order)}
        it["opts"] = [it["opts"][i] for i in order]
        it["miss"] = {str(newpos[int(k2)]): v for k2, v in it["miss"].items()}
        it["a"] = s
    return items
ST, CW, PR = "Build words with struct", "Compound words", "Pronoun jobs"
NOT2 = "Long is not the same as compound. Look for two real words."

L = {}
# ───────────────────────────── 22.1 · How two characters changed
L["22-1"] = {
 "connector": "You finished The Whipping Boy! This week there are no new chapters. Today, think about Jemmy and the prince on the first pages and on the last pages. Which boy changed more? Keep your book close so you can look back.",
 "writingFocus": "compare",
 "dol": dol("then follow me said the prince",
   "“"+S+"T"+E+"hen follow me"+S+",”"+E+" said the prince"+S+"."+E,
   "The words the prince says go inside quotation marks. Then starts what he says, so it gets a capital T. A comma goes inside the closing quotation mark. A period ends the sentence.",
   "rein in your beast the prince whispered",
   "“"+S+"R"+E+"ein in your beast"+S+",”"+E+" the prince whispered"+S+"."+E,
   "The words the prince says go inside quotation marks. Rein starts what he says, so it gets a capital R. A comma goes inside the closing quotation mark. A period ends the sentence."),
 "hints": {
  "fill1": {"h1": "Look at the word list above. Which six letters are in every word?", "why": "con + struct = construct: to build something."},
  "fill2": {"h1": "It is the same root as the first box.", "why": "de + struct = destruct: to tear a structure apart."},
  "fill3": {"h1": "Look at how structure is built in the word list. What comes after struct?", "why": "struct + ure = structure: something that has been built."},
  "fill4": {"h1": "Look at instruct in the word list. What comes after in?", "why": "in + struct = instruct: to build knowledge; to teach."}
 },
 "miss": {"match": {
   "transform": "Transform has form, which means shape. Look for the meaning about changing completely.",
   "compare": "When you compare, you look at two things side by side. Look for sameness and difference.",
   "contrast": "Contrast is only about what is different. Look for that meaning.",
   "develop": "Develop is about growing over time. Look for that meaning."}},
 "flags": {"journal-q1": {"quote": False, "count": 2}, "journal-q2": {"quote": False, "count": 2}, "journal-q3": {"quote": False, "count": 1}},
 "scholar": {"journal-q1": "… and tell which chapter shows the biggest change.",
   "journal-q2": "… and tell one thing about the prince that stayed the same.",
   "journal-q3": "… and tell how that likeness helped them get home."},
 "copia": {"look": "One plain sentence from the end of the book, and three empty boxes. Each box asks you to say the same idea in a new way.",
   "todo": "Rewrite the sentence three ways, one box at a time. Tap Show one way if you get stuck.",
   "seed": "Jemmy <b>walked</b> toward the golden doors.",
   "eg": ["Beside the prince, Jemmy walked toward the golden doors.",
          "Jemmy <i>strode</i> toward the golden doors.",
          "A happy Jemmy walked toward the tall golden doors."]},
 "wordgame": dict(CASTLE, look=LOOK1, items=[
   q(ST, "Which word has the root <b>struct</b> in it?", ["destructive", "distract"], 0,
     "de + struct + ive. Distract has s t r, but not all of struct.", {1: "Look for all six letters: s t r u c t."}),
   q(ST, "A storm can be <b>destructive</b>. What does destructive mean?", ["it tears things down", "it builds things up"], 0,
     "de means down, and struct means build. Destructive things tear down what was built.", {1: "Look at the front part, de. It means down or apart."}),
   q(CW, "Which word is a compound word?", ["outlaw", "ransom"], 0,
     "out + law = outlaw. Two real words.", {1: "Can you split ransom into two real words? Try the other one."}),
   q(CW, "Which word is a compound word?", ["riverbank", "important"], 0,
     "river + bank = riverbank.", {1: NOT2}),
   q(CW, "Which word is a compound word?", ["greyhound", "kettle"], 0,
     "grey + hound = greyhound, a very fast dog.", {1: "Can you split kettle into two real words?"}),
   q(PR, "Jemmy and ___ ran down the road.", ["he", "him"], 0,
     "Cover Jemmy: he ran. He does the action.", {1: "Cover Jemmy and say it. Him ran? Try the other one."}),
   q(PR, "Betsy waved at Jemmy and ___.", ["him", "he"], 0,
     "Cover Jemmy: waved at him. Him gets the action.", {1: "Cover Jemmy. Waved at he? Say it out loud."}),
   q(ST, "Which word has the root <b>struct</b> in it?", ["instructive", "instrument"], 0,
     "in + struct + ive. Instrument has s t r, but not struct.", {1: "Look for all six letters: s t r u c t."}),
 ]),
 "glossary": GLOSS,
 "sayWords": ["transform", "compare", "contrast", "develop"],
 "transcripts": {
  "welcome": "Hi, it’s Opti. You finished The Whipping Boy! This week there are no new chapters. Today, look back at Jemmy and the prince on the very first pages, and on the very last. Which boy changed more?",
  "guide1": "Word work first. You’ll meet a root that means build, sort pronouns by their jobs, and find compound words.",
  "guide2": "No new chapters today. Look back through the whole book for the moments that changed each boy.",
  "guide3": "Today you make one vague sentence in your comparison specific. Add a chapter number."
 },
 "notes": dict(NOTES_COMMON,
   wgrd="Good readers look back at a whole book and see how the characters grew.",
   vocab=[["transform", "to change completely"], ["compare", "to look at two things side by side for sameness and difference"], ["contrast", "to point out the differences between two things"], ["develop", "to grow and change over time"]])
}
# ───────────────────────────── 22.2 · Theme
L["22-2"] = {
 "connector": "Yesterday you looked at how the boys changed. Today, think about what the whole story teaches. That lesson is the theme. Find one moment early in the book and one late that show it.",
 "writingFocus": "compare",
 "dol": dol("the prince didnt make a sound",
   S+"T"+E+"he prince didn"+S+"’"+E+"t make a sound"+S+"."+E,
   "The starts the sentence, so it gets a capital T. Didn’t is did not squeezed together, so it needs an apostrophe. A period ends it.",
   "jemmy wasnt sure he trusted the prince",
   S+"J"+E+"emmy wasn"+S+"’"+E+"t sure he trusted the prince"+S+"."+E,
   "Jemmy starts the sentence and is a name, so it gets a capital J. Wasn’t is was not squeezed together, so it needs an apostrophe. A period ends it."),
 "miss": {"match": {
   "theme": "The theme is the big lesson. Look for the meaning about a message.",
   "evidence": "Evidence is a detail that proves an idea. Look for that meaning.",
   "resolution": "The resolution comes at the end. Look for the meaning about a problem being settled.",
   "character development": "Development is growing. Look for the meaning about a character changing."}},
 "flags": {"journal-q1": {"quote": False, "count": 0}, "journal-q2": {"quote": False, "count": 1}, "journal-q3": {"quote": False, "count": 1}},
 "scholar": {"journal-q1": "… and say it so it fits any person, not only Jemmy.",
   "journal-q2": "… and tell which chapter it comes from.",
   "journal-q3": "… and tell how this moment is different from your early one."},
 "wordgame": dict(CASTLE, look=LOOK, items=[
   q(ST, "The root <b>struct</b> means…", ["build", "carry", "look"], 0,
     "struct means build. port means carry, and spect means look.", {1: "Carry goes with port. Which one goes with struct?", 2: "Look goes with spect. Which one goes with struct?"}),
   q(ST, "A <b>structured</b> day has a plan, the way a building has a frame. Which part means build?", ["struct", "ed"], 0,
     "struct means build. ed is an ending.", {1: "ed is an ending. Find the six letters that mean build."}),
   q(CW, "Which word is a compound word?", ["birdcage", "castle"], 0,
     "bird + cage = birdcage.", {1: "Can you split castle into two real words?"}),
   q(CW, "<b>Fairground</b> is made of which two words?", ["fair + ground", "fa + irground"], 0,
     "fair + ground. Both are real words.", {1: "Is irground a real word? Split it into two words you know."}),
   q(CW, "Which word is a compound word?", ["cowboy", "champion"], 0,
     "cow + boy = cowboy.", {1: NOT2}),
   q(PR, "___ and Betsy walked to the fair.", ["She", "Her"], 0,
     "Cover Betsy: She walked. She does the action.", {1: "Cover Betsy. Her walked? Try the other one."}),
   q(PR, "Petunia sniffed ___ boots.", ["his", "him"], 0,
     "his shows whose boots they are.", {1: "Him boots? The boots belong to him. Use the word that shows whose."}),
   q(ST, "In <b>destructive</b>, which part means build?", ["struct", "de"], 0,
     "struct means build. de means down or apart.", {1: "de means down or apart. Find the six letters that mean build."}),
 ]),
 "glossary": GLOSS,
 "sayWords": ["theme", "evidence", "resolution", "character development"],
 "transcripts": {
  "welcome": "Welcome back, it’s Opti. Today’s question is a big one. What is The Whipping Boy really about? Not what happened, but what it teaches. That lesson is called the theme.",
  "guide1": "Word study. You’ll match struct words to their meanings, find every pronoun in a sentence, and pick out the compound words by ear.",
  "guide2": "No new chapters today. Think of one moment early in the book and one moment late that show the same lesson.",
  "guide3": "Today you add a sentence to your conclusion that says what the story teaches."
 },
 "notes": dict(NOTES_COMMON,
   wgrd="The lesson a story teaches is called its theme. Say it so it fits any person, not only the characters.",
   vocab=[["theme", "the big message or lesson of a story"], ["evidence", "a detail from the book that proves your idea"], ["resolution", "how the problem is settled at the end"], ["character development", "how a character grows and changes"]])
}
# ───────────────────────────── 22.3 · Reader's Theater
L["22-3"] = {
 "connector": "Today the book becomes a play. You pick a scene and read it out loud, with a voice for each character. Is the prince bossy or scared? Is Betsy calm or loud? Let the punctuation tell your voice what to do.",
 "writingFocus": "compare",
 "dol": dol("does everyone hate me the prince asked",
   "“"+S+"D"+E+"oes everyone hate me"+S+"?”"+E+" the prince asked"+S+"."+E,
   "The prince asks a question, so a question mark goes inside the closing quotation mark. Does gets a capital D. The word the stays small, because the sentence keeps going. A period ends it.",
   "what about you the prince asked",
   "“"+S+"W"+E+"hat about you"+S+"?”"+E+" the prince asked"+S+"."+E,
   "The prince asks a question, so a question mark goes inside the closing quotation mark. What gets a capital W. The word the stays small. A period ends it."),
 "hints": {
  "mfill1": {"h1": "Say con, then struct, then ion. Push them together.", "why": "con + struct + ion = construction: the work of building."},
  "mfill2": {"h1": "Say in, then struct, then ion. Push them together.", "why": "in + struct + ion = instruction: teaching, or steps that tell you how."},
  "mfill3": {"h1": "Say de, then struct, then ion. Push them together.", "why": "de + struct + ion = destruction: tearing something down."},
  "mfill4": {"h1": "Say ob, then struct. Push them together.", "why": "ob + struct = obstruct: to block the way."},
  "vcloze1": {"h1": "This one is about showing feelings with your voice and face.", "why": "expression means showing feeling."},
  "vcloze2": {"h1": "This one is the words the characters say to each other.", "why": "dialogue is the words characters say."},
  "vcloze3": {"h1": "This one is about reading smoothly, not choppy.", "why": "fluency means reading smoothly at the right speed."},
  "vcloze4": {"h1": "This one is the hardest word: rhythm, speed and stress.", "why": "prosody is the rhythm and stress of your voice."},
  "gfill1": {"h1": "The prince gets the map. Which word from the bank gets the action?", "why": "Jemmy gave the map to him."},
  "gfill2": {"h1": "Two people ran. Which bank word stands for both of them?", "why": "They ran."},
  "gfill3": {"h1": "The coach belongs to Captain Nips. Which bank word shows whose?", "why": "It was his coach."},
  "gfill4": {"h1": "Jemmy told someone. Which bank word gets the action?", "why": "Jemmy told him about the bear."}
 },
 "miss": {"match": {
   "expression": "Expression is showing feelings. Look for the meaning about voice, face, or body.",
   "dialogue": "Dialogue is what characters say. Look for the meaning about spoken words.",
   "fluency": "Fluency is about reading smoothly. Look for the meaning about pace.",
   "prosody": "Prosody is the music of your voice. Look for the meaning about rhythm and stress."}},
 "flags": {"journal-q1": {"quote": False, "count": 1}, "journal-q2": {"quote": False, "count": 1}, "journal-q3": {"quote": False, "count": 2}},
 "scholar": {"journal-q1": "… and copy one line of dialogue from the scene.",
   "journal-q2": "… and tell one place where you changed your voice on purpose.",
   "journal-q3": "… and tell which punctuation mark helped you most."},
 "wordgame": dict(CASTLE, look=LOOK, items=[
   q(ST, "Which word has the root <b>struct</b> in it?", ["constructive", "consonant"], 0,
     "con + struct + ive. Consonant starts with con too, but it has no struct.", {1: "Look for all six letters: s t r u c t."}),
   q(ST, "Kind, <b>constructive</b> words help a friend build a better story. What does constructive mean?", ["helping to build something better", "tearing something down"], 0,
     "con + struct: to build together. Constructive words help build.", {1: "Tearing down would be destructive. Constructive starts with con, not de."}),
   q(CW, "Which word is a compound word?", ["sunshine", "sewer"], 0,
     "sun + shine = sunshine.", {1: "Can you split sewer into two real words?"}),
   q(CW, "Put <b>night</b> and <b>gown</b> together. What word do you get?", ["nightgown", "nitegown"], 0,
     "night + gown = nightgown. Both words keep their spelling.", {1: "Look at night. Did it keep its spelling?"}),
   q(CW, "Which word is a compound word?", ["footprint", "elephant"], 0,
     "foot + print = footprint.", {1: NOT2}),
   q(PR, "The king smiled at ___.", ["them", "they"], 0,
     "them gets the action: smiled at them.", {1: "Smiled at they? Say it out loud."}),
   q(PR, "___ and I found a map.", ["He", "Him"], 0,
     "Cover and I: He found a map. He does the action.", {1: "Cover and I. Him found a map? Try the other one."}),
   q(ST, "In <b>instructive</b>, which part means build?", ["struct", "in", "ive"], 0,
     "struct means build.", {1: "in is the front part. Find the six letters that mean build.", 2: "ive is the ending. Find the six letters that mean build."}),
 ]),
 "glossary": GLOSS,
 "sayWords": [],
 "transcripts": {
  "welcome": "Hi, it’s Opti. Today the book turns into a play! You pick a scene and read it out loud, with a voice for each character. Is the prince bossy? Is Betsy loud? Let the marks on the page tell your voice what to do.",
  "guide1": "Word work. You’ll build four new struct words, use pronouns so a name isn’t said twice, and join small words into compound words.",
  "guide2": "No new chapters today. Pick the scene you would most like to read out loud. Think about how each character sounds.",
  "guide3": "Today you check the pronouns in your comparison paragraph."
 },
 "notes": dict(NOTES_COMMON,
   wgrd="Good readers hear each character’s voice. The marks on the page tell your voice when to rise, ask, or pause.",
   vocab=[["expression", "showing feelings with your voice, face, or body"], ["dialogue", "the words characters say"], ["fluency", "reading smoothly at the right speed"], ["prosody", "the rhythm and stress of your voice"]])
}
# ───────────────────────────── 22.4 · Publish + celebrate
L["22-4"] = {
 "connector": "This is the last day with The Whipping Boy. Today you share your comparison paragraph out loud, and you look back at the whole book. What moment will you remember most?",
 "writingFocus": "compare",
 "dol": dol("betsy bowed low to the king",
   S+"B"+E+"etsy bowed low to the king"+S+"."+E,
   "Betsy starts the sentence and is a name, so it gets a capital B. A period ends the sentence.",
   "the boys walked toward the golden doors",
   S+"T"+E+"he boys walked toward the golden doors"+S+"."+E,
   "The starts the sentence, so it gets a capital T. A period ends the sentence."),
 "hints": {
  "vcloze1": {"h1": "This sentence asks you to think back. Which bank word means that?", "why": "reflect means to think carefully about something that happened."},
  "vcloze2": {"h1": "Finishing a book is a reason for a party. Which bank word fits?", "why": "celebrate means to mark something with joy."},
  "vcloze3": {"h1": "The Whipping Boy is a long story with chapters. Which bank word names that?", "why": "a novel is a long story with characters, plot and theme."},
  "vcloze4": {"h1": "This one means worth remembering.", "why": "memorable means worth remembering."}
 },
 "miss": {"match": {
   "reflect": "Reflect is about thinking back. Look for that meaning.",
   "celebrate": "Celebrate is about joy. Look for the meaning about honoring something.",
   "novel": "A novel is a kind of book. Look for the meaning about a long story.",
   "memorable": "Memorable has memory inside it. Look for the meaning about remembering."}},
 "flags": {"journal-q1": {"quote": False, "count": 1}, "journal-q2": {"quote": True, "count": 1}, "journal-q3": {"quote": False, "count": 1}},
 "scholar": {"journal-q1": "… and tell which chapter made you sure.",
   "journal-q2": "… and tell how you could make another sentence that strong.",
   "journal-q3": "… and tell what that moment shows about one of the boys."},
 "wordgame": dict(CASTLE, look=LOOK, items=[
   q(ST, "Which word part means build?", ["struct", "port", "spect"], 0,
     "struct = build. port = carry. spect = look.", {1: "port means carry. Which part means build?", 2: "spect means look. Which part means build?"}),
   q(ST, "Which word has the root <b>struct</b> in it?", ["structured", "stretched"], 0,
     "struct + ed. Stretched has s t r, but not struct.", {1: "Look for all six letters: s t r u c t."}),
   q(ST, "An <b>instructive</b> book…", ["teaches you something", "knocks down a wall"], 0,
     "in + struct: to build knowledge in someone. An instructive book teaches you.", {1: "Knocking down would be destructive. Look at the front part, in."}),
   q(CW, "Which word is a compound word?", ["snowball", "adventure"], 0,
     "snow + ball = snowball.", {1: NOT2}),
   q(CW, "Which word is a compound word?", ["hilltop", "convict"], 0,
     "hill + top = hilltop.", {1: "Can you split convict into two real words?"}),
   q(CW, "<b>Sunflower</b> is made of which two words?", ["sun + flower", "sunf + lower"], 0,
     "sun + flower. Both are real words.", {1: "Is sunf a word? Split it into two words you know."}),
   q(PR, "The outlaws chased Jemmy and ___.", ["me", "I"], 0,
     "Cover Jemmy: chased me. Me gets the action.", {1: "Cover Jemmy. Chased I? Say it out loud."}),
   q(PR, "Which pronoun shows belonging?", ["their", "they"], 0,
     "their shows whose: their coach.", {1: "They does the action. Which word shows whose?"}),
 ]),
 "glossary": GLOSS,
 "sayWords": [],
 "transcripts": {
  "welcome": "Hi, it’s Opti. This is our last day with The Whipping Boy. Today you read your comparison paragraph out loud, and you look back at the whole book. What moment will you remember most?",
  "guide1": "Word study review. Roll struct words, hunt for pronouns in the wrong job, and roll compound words.",
  "guide2": "No new chapters today. Think about which boy changed the most, and what you would tell the author.",
  "guide3": "Today you read your comparison paragraph out loud. Then write what you noticed."
 },
 "notes": dict(NOTES_COMMON,
   wgrd="Good readers remember a book after they close it. Think about where the characters started and where they ended.",
   vocab=[["reflect", "to think carefully about something that happened"], ["celebrate", "to mark something with joy"], ["novel", "a long story with characters, plot and theme"], ["memorable", "worth remembering"]])
}
# ───────────────────────────── fluency
L["22-fluency"] = {
 "connector": "This week’s passage is the very end of the book, from Chapter 20. Read it three times. The last time, read the boys quietly, like two friends, and the king warm, like a big smile.",
 "howto": True,
 "transcripts": {
  "welcome": "Hi, it’s Opti. This week’s passage is the very end of the book. Read it three times. First, get every word right. Next, make it smooth. Then read the boys quietly, like two friends, and read the king’s last line warm, like a big smile."
 }
}
for k in ("22-1", "22-2", "22-3", "22-4"): sides(k, L[k]["wordgame"]["items"])

if __name__ == '__main__':
    import sys
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    try:
        from plates_wk22 import PLATES as P
        for k, p in P.items(): L[k]["plate"] = p
    except ImportError: pass
    for k, v in L.items():
        io.open(os.path.join(OUT, 'lesson-%s.json' % k), 'w', encoding='utf-8').write(json.dumps(v, ensure_ascii=False, indent=1))
        print(k, len(json.dumps(v, ensure_ascii=False).encode()))
