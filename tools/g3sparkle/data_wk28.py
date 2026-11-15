#!/usr/bin/env python3
"""Week 28 DATA (The Lion, the Witch and the Wardrobe, Ch. 10-12): 28.1-28.4 + fluency.
Every book line checked against Planning docs/lww_text.txt (nothing past Ch. 12; each day's lines from that day's chapter or
earlier). The Great Thaw items use only this week's word study (com-/con- = with, together; endings that double, drop the e,
or change y to i) and none is an answer elsewhere on the week's pages (combine connect company conversation compare construct;
stopped nodding shining named hurried cried wrapped waved smiled carried walked running hoping crying jumping biggest nicest
happiest longest writer winner owner helper sitter happier shopping smiling jumped bravest babies) or a film example
(constellation companion contact community; swimming baking tried fatter hiking fried; see teach_wk28.py)."""
import json, io, os
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'data')
S = "<strong>"; E = "</strong>"
def C(x): return S + x + E
def dol(a_raw, a_fixed, a_why, b_raw, b_fixed, b_why):
    return {"a": {"raw": a_raw, "fixed": a_fixed, "why": a_why}, "b": {"raw": b_raw, "fixed": b_fixed, "why": b_why}}
GLOSS = [
 {"w": "symbol", "m": "a thing in a story that stands for a bigger idea, like snow standing for the Witch's cold power", "key": True},
 {"w": "contraction", "m": "two words joined into one, with an apostrophe where letters were left out, like didn't", "key": True},
 {"w": "possessive", "m": "a word that shows who something belongs to, like Lucy's bottle", "key": True},
 {"w": "apostrophe", "m": "the little mark ’ that joins two words or shows belonging"},
 {"w": "base word", "m": "a word that can stand on its own before an ending is added. Hope is the base word in hoping."},
 {"w": "limerick", "m": "a funny poem with five lines and a bouncy beat"},
 {"w": "honesty", "m": "telling the truth, even when it is hard", "key": True},
]
NOTES_COMMON = {
 "wordParts": "The word parts com- and con- both mean with or together. combine = to join together. connect = to tie together.",
 "grammar": "An apostrophe has two jobs. It joins two words: did + not = didn’t. It shows belonging: Lucy’s bottle is the bottle that belongs to Lucy.",
 "spelling": "Some endings change the base word. Double the last letter: run → running. Drop the silent e: hope → hoping. Change y to i: carry → carried."
}
VOC = [["renewed", "made new again; restored to a fresh state"], ["herald", "a person or thing that announces something important is coming"], ["solemn", "serious, formal, and sincere"]]
VOC2 = VOC + [["jovial", "cheerful and friendly; in high spirits"]]
TOG = "Remember: com- and con- mean with or together. Which meaning has that idea?"
def it_mean(n, w, right, wrong):
    bins = [{"id": "r", "label": right, "ic": "👆"}, {"id": "w", "label": wrong, "ic": "👆"}]
    if n % 2: bins.reverse()
    return {"t": w, "bin": "r", "bins": bins, "why": "%s: %s." % (w, right), "miss": {"w": TOG}}
BIN = {"dbl": {"id": "dbl", "label": "Double the last letter", "ic": "✌️"}, "dropE": {"id": "dropE", "label": "Drop the silent e", "ic": "✂️"},
       "yi": {"id": "yi", "label": "Change y to i", "ic": "🔁"}, "none": {"id": "none", "label": "No change", "ic": "✔️"}}
MISS = {"dbl": "Look at the end of the base word. How many vowels, and how many consonants?",
        "dropE": "Look at the last letter of the base word. Do you hear it when you say the word?",
        "yi": "Look at the last letter of the base word, and the letter just before it.",
        "none": "Look at the end of the base word. Is there a short vowel and one consonant, a silent e, or a y? If not, think again."}
def it_end(base, end, rule, made, choices):
    return {"t": "%s + %s" % (base, end), "bin": rule, "why": "%s + %s = %s." % (base, end, made),
            "miss": {c: MISS[rule] for c in choices if c != rule}}
GAME = {"type": "thaw", "title": "The Great Thaw",
        "sub": "Every right answer melts a snow patch.",
        "todo": "Read the word on the snow patch. Tap the right answer. A right answer melts the snow, and a flower comes up.",
        "win": "Today's 8 snow patches have melted. Come back next lesson to melt more.",
        "winWeek": "The whole glade has thawed. Spring has come to Narnia!"}
LOOK1 = ("This week's game is a snowy glade in Narnia. Each snow patch has a word that starts with com- or con-. "
         "Tap what the word means. Remember: com- and con- mean with or together. "
         "Each right answer melts a patch, and a spring flower comes up. Over four days you thaw the whole glade.")
LOOK2 = ("Eight new snow patches with eight new words. Tap what each word means. Remember what com- and con- mean. "
         "The flowers from Day 1 are still blooming.")
LOOK3 = ("Today each snow patch has a base word and an ending. What does the base word need before the ending goes on: "
         "double the last letter, drop the silent e, or change y to i? The flowers from earlier days are still blooming.")
LOOK4 = ("Eight more patches. This time some base words need no change at all. Look at the end of each base word before you tap. "
         "Melt these and the whole glade has thawed.")
def note(title, text, before="Read:|Look Back"):
    return [{"id": "world", "kind": "info", "tab": "reading", "after": before, "before": True, "icon": "🌍",
             "title": "World Notes: " + title, "sub": "A real thing behind the story",
             "todo": "Read the note. Then read the chapter with your lens in mind.", "text": text}]
MATCH = {"renewed": "Renewed is about something made fresh again. Look for the meaning about new.",
         "herald": "A herald tells that something is coming. Look for the meaning about announcing.",
         "solemn": "Solemn is about being serious. Look for that meaning."}
L = {}
L["28-1"] = {
 "connector": "Have you ever seen a sign that something good was coming? In Chapter 10, the children hear jingling bells in the morning. Is it the Witch, or something better? Watch for signs that the long winter is starting to end.",
 "writingFocus": "literary response",
 "dol": dol("mrs beavers sewing machine couldnt come with them",
   C("M")+"rs"+C(".")+" "+C("B")+"eaver"+C("’")+"s sewing machine couldn"+C("’")+"t come with them"+C("."),
   "Mrs. Beaver is a title and a name. Beaver’s shows the machine belongs to her. Couldn’t joins could and not.",
   "peter didnt say a word when he got his shield and sword",
   C("P")+"eter didn"+C("’")+"t say a word when he got his shield and sword"+C("."),
   "Peter is a name. Didn’t joins did and not, and the apostrophe sits where the o was."),
 "hints": {
  "mfill1": {"h1": "Say the two parts out loud, then push them together.", "why": "com + bine = combine."},
  "mfill2": {"h1": "Say the two parts out loud, then push them together.", "why": "con + nect = connect."},
  "mfill3": {"h1": "Keep both parts. Do not drop any letters.", "why": "com + pany = company."},
  "mfill4": {"h1": "Keep both parts. Do not drop any letters.", "why": "con + versation = conversation."},
  "vcloze1": {"h1": "They slept and woke up fresh. Look at the meaning in the matching game about new.", "why": "Renewed means made fresh and new again."},
  "vcloze2": {"h1": "The robin was like a sign that good news was coming. Find the word for that.", "why": "A herald announces that something important is coming."},
  "vcloze3": {"h1": "Glad, but also very serious. Find the word for serious.", "why": "Solemn means serious and sincere."}
 },
 "miss": {"match": MATCH},
 "flags": {"journal-q1": {"quote": False, "count": 1}, "journal-q2": {"quote": False, "count": 2}, "journal-q3": {"quote": False, "count": 1}},
 "copia": {"look": "One plain sentence from Chapter 10, and three empty boxes. Each box asks you to say the same idea in a new way.",
   "todo": "Rewrite the sentence three ways, one box at a time. Tap Show one way if you get stuck.",
   "seed": "Father Christmas <b>gave</b> the children presents.",
   "eg": ["In the snowy morning, Father Christmas gave the children presents.",
          "Father Christmas <i>handed</i> the children presents.",
          "Father Christmas gave the three children very special presents."]},
 "wordgame": dict(GAME, look=LOOK1, stepTitle="What does it mean?", bins=[], items=[
   it_mean(0, "concert", "music played by people together", "music one person hums alone"),
   it_mean(1, "compound", "something made of parts put together", "something with only one part"),
   it_mean(2, "compress", "to press things together into a smaller space", "to pull things far apart"),
   it_mean(3, "convoy", "cars or ships traveling together", "one car driving alone"),
   it_mean(4, "conference", "a meeting where people talk together", "quiet time by yourself"),
   it_mean(5, "compose", "to put words or music together", "to erase words"),
   it_mean(6, "confluence", "the place where two rivers flow together", "the start of one small stream"),
   it_mean(7, "compact", "packed tightly together", "spread far apart")]),
 "glossary": GLOSS, "sayWords": [],
 "cards": note("Father Christmas", [
   "Father Christmas is an old English name for the spirit of Christmas. Stories say he brings gifts in the middle of winter.",
   "Old English pictures often show him in a long robe with a crown of holly. In America, a figure like him is called Santa Claus.",
   "In Narnia, the Witch made it always winter and never Christmas. So when Father Christmas gets in, it is big news."]),
 "transcripts": {"welcome": "Hi, it's Opti. In Chapter 10, the children hear jingling bells. Watch for signs that the long winter is starting to end.",
  "guide1": "Word work first: two word parts that mean together, two jobs for an apostrophe, and endings that change a word.",
  "guide2": "Read Chapter 10 with your lens. Then answer three questions.",
  "guide3": "Today you write a paragraph about one symbol."},
 "notes": dict(NOTES_COMMON, wgrd="A symbol is a thing in a story that stands for a bigger idea. Father Christmas getting into Narnia is a sign that the Witch's winter is weakening.", vocab=VOC)
}
L["28-2"] = {
 "connector": "In Chapter 11, the story follows Edmund on the Witch's sledge. It is a long, cold ride. Then he hears a sound he has not heard in Narnia before: running water. Watch what happens to the snow, and what it might stand for.",
 "writingFocus": "literary response",
 "dol": dol("the witchs dwarf couldnt make the sledge move",
   C("T")+"he "+C("W")+"itch"+C("’")+"s dwarf couldn"+C("’")+"t make the sledge move"+C("."),
   "The begins the sentence. Witch’s shows the dwarf works for her. Couldn’t joins could and not.",
   "edmund didnt want the dry bread but he ate it",
   C("E")+"dmund didn"+C("’")+"t want the dry bread"+C(",")+" but he ate it"+C("."),
   "Edmund is a name. Didn’t joins did and not. A comma goes before but."),
 "hints": {},
 "miss": {"match": dict(MATCH, jovial="Jovial is about being cheerful. Look for the happy meaning.")},
 "flags": {"journal-q1": {"quote": False, "count": 1}, "journal-q2": {"quote": False, "count": 1}, "journal-q3": {"quote": False, "count": 1}},
 "wordgame": dict(GAME, look=LOOK2, stepTitle="What does it mean?", bins=[], items=[
   it_mean(0, "compile", "to gather things together in one place", "to throw things away"),
   it_mean(1, "congregate", "to gather together in a crowd", "to scatter in every direction"),
   it_mean(2, "commotion", "noise and rushing about all together", "perfect quiet"),
   it_mean(3, "convention", "a big meeting where people come together", "a walk all by yourself"),
   it_mean(4, "conjoin", "to join together", "to split in two"),
   it_mean(5, "combat", "a fight with an enemy", "a nap after lunch"),
   it_mean(6, "convene", "to come together for a meeting", "to leave a meeting early"),
   it_mean(7, "comrade", "a friend who works or fights with you", "a stranger you never meet")]),
 "glossary": GLOSS, "sayWords": [],
 "cards": note("Spring Flowers", [
   "Snowdrops are often the first flowers of the year. They can push up while snow is still on the ground.",
   "Celandines are small yellow flowers. They open in sunshine and close up when it turns cloudy.",
   "Crocuses come up in late winter and early spring, in purple, white and gold. Edmund sees all three as the snow melts."]),
 "transcripts": {"welcome": "Hi, it's Opti. Edmund rides with the Witch, and then he hears running water. Watch what happens to the snow in Chapter 11.",
  "guide1": "Word work: match together words, find what each apostrophe does, and spot endings that change a word.",
  "guide2": "Read Chapter 11. Then watch my video in Read Like a Writer.",
  "guide3": "Today you make your symbol paragraph more precise."},
 "notes": dict(NOTES_COMMON, wgrd="The snow has been in every chapter. In Chapter 11 it melts. The thaw stands for the Witch's power breaking.", vocab=VOC2)
}
L["28-3"] = {
 "connector": "In Chapter 12, the children finally reach the Stone Table and meet Aslan. Then Susan's horn rings out, and Peter has to be brave even though he is scared. Watch what Peter does, and what Aslan does next.",
 "writingFocus": "literary response",
 "dol": dol("peters sword wasnt clean so aslan told him to wipe it",
   C("P")+"eter"+C("’")+"s sword wasn"+C("’")+"t clean"+C(",")+" so "+C("A")+"slan told him to wipe it"+C("."),
   "Peter’s shows the sword belongs to Peter. Wasn’t joins was and not. A comma goes before so.",
   "lucy didnt stop running until she reached peter",
   C("L")+"ucy didn"+C("’")+"t stop running until she reached "+C("P")+"eter"+C("."),
   "Lucy and Peter are names. Didn’t joins did and not."),
 "hints": {
  "mfill1": {"h1": "Say the two parts out loud, then push them together.", "why": "com + bine = combine."},
  "mfill2": {"h1": "Say the two parts out loud, then push them together.", "why": "con + nect = connect."},
  "mfill3": {"h1": "Keep both parts. Do not drop any letters.", "why": "com + pany = company."},
  "mfill4": {"h1": "Keep both parts. Do not drop any letters.", "why": "con + versation = conversation."}
 },
 "flags": {"journal-q1": {"quote": False, "count": 2}, "journal-q2": {"quote": False, "count": 1}, "journal-q3": {"quote": False, "count": 1}},
 "wordgame": dict(GAME, look=LOOK3, stepTitle="Which change does it need?", bins=[BIN["dbl"], BIN["dropE"], BIN["yi"]], items=[
   it_end("drip", "ing", "dbl", "dripping", ["dbl", "dropE", "yi"]), it_end("freeze", "ing", "dropE", "freezing", ["dbl", "dropE", "yi"]),
   it_end("sunny", "er", "yi", "sunnier", ["dbl", "dropE", "yi"]), it_end("hop", "ed", "dbl", "hopped", ["dbl", "dropE", "yi"]),
   it_end("skate", "ing", "dropE", "skating", ["dbl", "dropE", "yi"]), it_end("bury", "ed", "yi", "buried", ["dbl", "dropE", "yi"]),
   it_end("slip", "ing", "dbl", "slipping", ["dbl", "dropE", "yi"]), it_end("chase", "ed", "dropE", "chased", ["dbl", "dropE", "yi"])]),
 "glossary": GLOSS, "sayWords": [],
 "cards": note("How Knights Were Made", [
   "Long ago in Europe, a king or queen could make a brave person a knight.",
   "The new knight knelt, and the ruler touched his shoulder with the flat side of a sword. This is called an accolade.",
   "Then he was called Sir. The king of the United Kingdom still makes knights today, with a touch of a sword on each shoulder."]),
 "transcripts": {"welcome": "Hi, it's Opti. The children meet Aslan, and Peter has to be brave. Watch what Peter does in Chapter 12.",
  "guide1": "Word work: build together words, put apostrophes in place, and build words with endings.",
  "guide2": "Read Chapter 12. Then answer three questions.",
  "guide3": "Today you add your symbol paragraph to your response."},
 "notes": dict(NOTES_COMMON, wgrd="Peter uses the sword Father Christmas gave him. Aslan makes him a knight. The gift was a sign of what Peter would need to do.", vocab=VOC)
}
L["28-4"] = {
 "connector": "No new chapters today. Look back at Chapters 10 to 12. Father Christmas, the melting snow, the flowers, Peter's sword: Lewis keeps bringing back signs of hope. Today you pick one symbol and finish your literary response.",
 "writingFocus": "literary response",
 "dol": dol("its spring in narnia and the witchs winter is over",
   C("I")+"t"+C("’")+"s spring in "+C("N")+"arnia"+C(",")+" and the "+C("W")+"itch"+C("’")+"s winter is over"+C("."),
   "It’s means it is. Narnia is a place name. Witch’s shows the winter was hers. A comma goes before and.",
   "mr beaver couldnt say a word when he heard about his dam",
   C("M")+"r"+C(".")+" "+C("B")+"eaver couldn"+C("’")+"t say a word when he heard about his dam"+C("."),
   "Mr. Beaver is a title and a name. Couldn’t joins could and not."),
 "hints": {},
 "flags": {"journal-q1": {"quote": False, "count": 1}, "journal-q2": {"quote": False, "count": 1}, "journal-q3": {"quote": False, "count": 1}},
 "wordgame": dict(GAME, look=LOOK4, stepTitle="Which change, or none?", bins=[BIN["dbl"], BIN["dropE"], BIN["yi"], BIN["none"]], items=[
   it_end("melt", "ing", "none", "melting", ["dbl", "dropE", "yi", "none"]), it_end("tidy", "ed", "yi", "tidied", ["dbl", "dropE", "yi", "none"]),
   it_end("trot", "ing", "dbl", "trotting", ["dbl", "dropE", "yi", "none"]), it_end("race", "ing", "dropE", "racing", ["dbl", "dropE", "yi", "none"]),
   it_end("bloom", "ed", "none", "bloomed", ["dbl", "dropE", "yi", "none"]), it_end("muddy", "er", "yi", "muddier", ["dbl", "dropE", "yi", "none"]),
   it_end("skip", "ed", "dbl", "skipped", ["dbl", "dropE", "yi", "none"]), it_end("glide", "ing", "dropE", "gliding", ["dbl", "dropE", "yi", "none"])]),
 "glossary": GLOSS, "sayWords": [],
 "cards": note("Real Wolves", [
   "Real gray wolves live in family groups called packs. They are shy and usually stay far away from people.",
   "Old fairy tales often made wolves the villains, like the wolf in Little Red Riding Hood.",
   "In the story, Maugrim is a made-up wolf who works for the Witch. Real wolves are not like him."], before="Look Back"),
 "transcripts": {"welcome": "Hi, it's Opti. Look back at Chapters 10 to 12. Lewis keeps bringing back signs of hope. Pick the one that matters most to you.",
  "guide1": "Word work: roll together words, fix a passage in passes, and roll words with endings.",
  "guide2": "Look back at Chapters 10 to 12 for your best details.",
  "guide3": "Today you polish your literary response."},
 "notes": dict(NOTES_COMMON, wgrd="Lewis keeps bringing back signs of hope: Father Christmas, the thaw, the spring flowers. A symbol lets the reader feel the idea, not just hear it.", vocab=VOC2)
}
FLU = {"connector": "This week's passage is from Chapter 11: the thaw, seen through Edmund's eyes. Read it three times. The last time, let the two Every moment sentences speed up, like the snow melting faster and faster.",
 "howto": True,
 "transcripts": {"welcome": "Hi, it's Opti. This week's passage is the thaw in Chapter 11. Read it three times. First, get every word right. Next, make it smooth. Then let the Every moment sentences speed up, like the thaw."}}
if __name__ == '__main__':
    import sys
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from plates_wk28 import PLATES as P
    for k, p in P.items(): L[k]["plate"] = p
    for k, v in L.items():
        io.open(os.path.join(OUT, 'lesson-%s.json' % k), 'w', encoding='utf-8').write(json.dumps(v, ensure_ascii=False, indent=1)); print(k)
    io.open(os.path.join(OUT, 'lesson-28-fluency.json'), 'w', encoding='utf-8').write(json.dumps(FLU, ensure_ascii=False, indent=1))
