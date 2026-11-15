#!/usr/bin/env python3
"""Week 27 DATA (The Lion, the Witch and the Wardrobe, Ch. 7-9): 27.1-27.4 + fluency.
Every book line checked against Planning docs/lww_text.txt (nothing past Ch. 9). Mr. Beaver's Ice Hole items use only this
week's word study (in-/im- = not; prefix + base word) and none is an answer elsewhere on the week's pages
(possible correct patient visible informal perfect reform untrue transport recall form true act wise transform inform perform
rebuild unpack disappeared preheat misplaced unhappy unkind misread unfair disappear remake disobey) or a film example
(inactive impolite incomplete immature indirect replay preview rewind unsafe misbehave; see teach_wk27.py)."""
import json, io, os
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'data')
S = "<strong>"; E = "</strong>"
def C(x): return S + x + E
def dol(a_raw, a_fixed, a_why, b_raw, b_fixed, b_why):
    return {"a": {"raw": a_raw, "fixed": a_fixed, "why": a_why}, "b": {"raw": b_raw, "fixed": b_fixed, "why": b_why}}
GLOSS = [
 {"w": "perspective", "m": "how one character sees and feels about what happens", "key": True},
 {"w": "prefix", "m": "a word part added to the front of a word that changes its meaning", "key": True},
 {"w": "base word", "m": "a word that can stand on its own before a prefix is added. Happy is the base word in unhappy."},
 {"w": "irregular verb", "m": "a verb that does not add -ed for the past, like go and went", "key": True},
 {"w": "limerick", "m": "a funny poem with five lines and a bouncy beat"},
 {"w": "honesty", "m": "telling the truth, even when it is hard", "key": True},
]
NOTES_COMMON = {
 "wordParts": "The word parts in- and im- both mean not. inactive = not active. impolite = not polite. Use im- before words that start with m or p.",
 "grammar": "An irregular verb does not add -ed for the past. You learn each one: say → said, see → saw, sit → sat.",
 "spelling": "A prefix goes on the front of a base word, and the base word keeps its spelling. Peel the prefix off to read the base: un + happy."
}
VOC = [["authority", "the right or power to give orders and make decisions"], ["prophecy", "a statement that something will happen in the future"], ["betray", "to be disloyal to someone who trusted you"]]
VOC2 = VOC + [["treachery", "betraying someone's trust in a very serious way"]]
BIN = {"in": {"id": "in", "label": "in- (not)", "ic": "🪣"}, "im": {"id": "im", "label": "im- (not)", "ic": "🪣"},
       "keep": {"id": "keep", "label": "Keep it: prefix + base word", "ic": "🪣"}, "back": {"id": "back", "label": "Throw it back: no prefix", "ic": "🌊"}}
def it_pre(base, p, mean):
    other = "im" if p == "in" else "in"
    miss = ("Look at the first letter of the word. Is it m or p?" if p == "im" else
            "Look at the first letter of the word. The other word part only goes before m or p.")
    return {"t": base, "bin": p, "why": "%s + %s = %s%s: %s." % (p, base, p, base, mean), "miss": {other: miss}}
def it_keep(w, ok, why):
    right = "keep" if ok else "back"
    miss = ("Cover the first part. Is what's left a real word?" if ok else "Cover the first part. Is what's left really a word?")
    return {"t": w, "bin": right, "why": why, "miss": {("back" if ok else "keep"): miss}}
GAME = {"type": "icehole", "title": "Mr. Beaver’s Ice Hole",
        "sub": "Every right answer lands a fish on the ice.",
        "todo": "Read the word on the fish. Tap the right answer. A right answer lands the fish on the ice.",
        "win": "Today's 8 fish are on the ice. Come back next lesson to catch more.",
        "winWeek": "A fine catch! Mrs. Beaver will have the frying pan ready."}
LOOK1 = ("This week's game is Mr. Beaver's fishing hole. In Chapter 7 he keeps a hole open in the ice and pulls out fish for dinner. "
         "Each fish comes with a word. Which word part makes it mean not: in- or im-? Look at the first letter. "
         "Each right answer lays a fish on the ice. Over four days you land the whole catch.")
LOOK2 = ("Eight new fish with eight new words. Which word part makes each one mean not: in- or im-? "
         "Remember: im- goes before m or p. The fish from Day 1 are still on the ice.")
LOOK3 = ("Today Mr. Beaver keeps only the fish whose word has a prefix. Cover the first part of the word. "
         "If what's left is a real word, tap Keep it. If not, tap Throw it back. The fish from earlier days are still on the ice.")
def note(title, text, before="Read:|Look Back"):
    return [{"id": "world", "kind": "info", "tab": "reading", "after": before, "before": True, "icon": "🌍",
             "title": "World Notes: " + title, "sub": "A real thing behind the story",
             "todo": "Read the note. Then read the chapter with your lens in mind.", "text": text}]
L = {}
L["27-1"] = {
 "connector": "Has a name ever made you feel something, before you even knew what it meant? In Chapter 7, Mr. Beaver whispers one name, and each of the four children feels something different. Watch how each one feels, and think about why.",
 "writingFocus": "literary response",
 "dol": dol("mr beaver led the children over the dam and they went into his house",
   C("M")+"r"+C(".")+" "+C("B")+"eaver led the children over the dam"+C(",")+" and they went into his house"+C("."),
   "Mr. Beaver is a title and a name, and Mr. ends with a period. A comma goes before and. Led and went are irregular past verbs.",
   "mrs beaver was at her sewing machine and she got up to meet them",
   C("M")+"rs"+C(".")+" "+C("B")+"eaver was at her sewing machine"+C(",")+" and she got up to meet them"+C("."),
   "Mrs. Beaver is a title and a name. A comma goes before and. Was and got are irregular past verbs."),
 "hints": {
  "fill1": {"h1": "Cover the first two letters. What word is left?", "why": "im + possible: the base word is possible."},
  "fill2": {"h1": "Cover the first two letters. What word is left?", "why": "in + correct: the base word is correct."},
  "fill3": {"h1": "Cover the word part that means not. What is left?", "why": "im + patient: the base word is patient."},
  "fill4": {"h1": "Cover the word part that means not. What is left?", "why": "in + visible: the base word is visible."},
  "vcloze1": {"h1": "Even the Witch feared it. Find the word about the power to rule.", "why": "Authority means the right or power to be in charge."},
  "vcloze2": {"h1": "It said what would happen in the future. Find that word.", "why": "A prophecy says something will happen."},
  "vcloze3": {"h1": "Edmund was being disloyal to his family. Find that word.", "why": "To betray is to be disloyal to someone who trusted you."}
 },
 "miss": {"match": {
   "authority": "Authority is about being in charge. Look for the meaning about power.",
   "prophecy": "A prophecy is about the future. Look for that meaning.",
   "betray": "Betray is about trust. Look for the meaning about being disloyal."}},
 "flags": {"journal-q1": {"quote": False, "count": 2}, "journal-q2": {"quote": False, "count": 1}, "journal-q3": {"quote": False, "count": 1}},
 "copia": {"look": "One plain sentence from Chapter 7, and three empty boxes. Each box asks you to say the same idea in a new way.",
   "todo": "Rewrite the sentence three ways, one box at a time. Tap Show one way if you get stuck.",
   "seed": "Mr. Beaver <b>caught</b> a fish.",
   "eg": ["Through the hole in the ice, Mr. Beaver caught a fish.",
          "Mr. Beaver <i>whisked out</i> a fish.",
          "Mr. Beaver caught a beautiful, wriggling trout."]},
 "wordgame": dict(GAME, look=LOOK1, stepTitle="in- or im-?", bins=[BIN["in"], BIN["im"]], items=[
   it_pre("capable", "in", "not capable"), it_pre("proper", "im", "not proper"), it_pre("expensive", "in", "not expensive"),
   it_pre("pure", "im", "not pure"), it_pre("accurate", "in", "not accurate"), it_pre("mobile", "im", "not able to move"),
   it_pre("edible", "in", "not safe to eat"), it_pre("movable", "im", "not able to be moved")]),
 "glossary": GLOSS, "sayWords": [],
 "cards": note("Real Beavers", [
   "Real beavers build dams across streams with sticks, mud and stones.",
   "The dam holds back the water and makes a pond. Beavers live in a home of sticks and mud called a lodge.",
   "Their strong front teeth never stop growing, so chewing wood keeps them the right size."]),
 "transcripts": {"welcome": "Hi, it's Opti. Mr. Beaver whispers one name, and each child feels something different. Watch how each one feels in Chapter 7.",
  "guide1": "Word work first: two word parts that mean not, verbs that skip -ed, and prefixes.",
  "guide2": "Read Chapter 7 with your lens. Then answer three questions.",
  "guide3": "Today you plan a response that compares two characters."},
 "notes": dict(NOTES_COMMON, wgrd="Two characters can see the same moment in different ways. Ask what each one wants, fears or knows.", vocab=VOC)
}
L["27-2"] = {
 "connector": "After dinner at the Beavers' house, Mr. Beaver tells the children about Aslan. But someone at the table is not listening the way the others are. In Chapter 8, look for clues about what Edmund is thinking.",
 "writingFocus": "literary response",
 "dol": dol("lucy saw that edmund was gone and she told the others",
   C("L")+"ucy saw that "+C("E")+"dmund was gone"+C(",")+" and she told the others"+C("."),
   "Lucy and Edmund are names. A comma goes before and. Saw and told are irregular past verbs.",
   "peter wanted to look for edmund but mr beaver said there was no use",
   C("P")+"eter wanted to look for "+C("E")+"dmund"+C(",")+" but "+C("M")+"r"+C(".")+" "+C("B")+"eaver said there was no use"+C("."),
   "Peter, Edmund and Mr. Beaver are names. A comma goes before but. Said is an irregular past verb."),
 "hints": {},
 "miss": {"match": {
   "authority": "Authority is about being in charge. Look for the meaning about power.",
   "prophecy": "A prophecy is about the future. Look for that meaning.",
   "betray": "Betray is about trust. Look for the meaning about being disloyal.",
   "treachery": "Treachery is a very serious kind of betraying. Look for the meaning that says very serious."}},
 "flags": {"journal-q1": {"quote": False, "count": 1}, "journal-q2": {"quote": False, "count": 1}, "journal-q3": {"quote": False, "count": 1}},
 "wordgame": dict(GAME, look=LOOK2, stepTitle="in- or im-?", bins=[BIN["in"], BIN["im"]], items=[
   it_pre("measurable", "im", "too big to measure"), it_pre("dependent", "in", "not depending on others"), it_pre("practical", "im", "not practical"),
   it_pre("secure", "in", "not feeling safe"), it_pre("mortal", "im", "living forever"), it_pre("justice", "in", "something unfair"),
   it_pre("personal", "im", "not personal"), it_pre("flexible", "in", "not able to bend")]),
 "glossary": GLOSS, "sayWords": [],
 "cards": note("Ice Fishing", [
   "In very cold places, people fish through a hole they cut in thick ice.",
   "Mr. Beaver keeps his hole open every day with his hatchet, so it does not freeze over.",
   "Thick ice can hold a person, but thin ice cannot. Never walk on ice unless a grown-up says it is safe."]),
 "transcripts": {"welcome": "Hi, it's Opti. After dinner, Mr. Beaver tells about Aslan. Look for clues about what Edmund is thinking in Chapter 8.",
  "guide1": "Word work: match not words, fix wrong verbs, and hunt for prefixes.",
  "guide2": "Read Chapter 8. Then watch my video in Read Like a Writer.",
  "guide3": "Today you draft your comparison."},
 "notes": dict(NOTES_COMMON, wgrd="Lewis shows what Edmund is thinking through what he does. He slips away while the others are listening.", vocab=VOC2)
}
L["27-3"] = {
 "connector": "Today the story follows Edmund, alone in the snow. You see the night through his eyes. In Chapter 9, watch what he tells himself, and what he really knows deep down.",
 "writingFocus": "literary response",
 "dol": dol("when edmund saw the lion he stood very still",
   C("W")+"hen "+C("E")+"dmund saw the lion"+C(",")+" he stood very still"+C("."),
   "When starts the part that cannot stand alone, so a comma goes after lion. Saw and stood are irregular past verbs.",
   "when the wolf stood up edmund began to tremble",
   C("W")+"hen the wolf stood up"+C(",")+" "+C("E")+"dmund began to tremble"+C("."),
   "When starts the part that cannot stand alone, so a comma goes after up. Edmund is a name. Stood and began are irregular past verbs."),
 "hints": {
  "mfill1": {"h1": "Say the two parts out loud, then push them together.", "why": "im + possible = impossible."},
  "mfill2": {"h1": "Say the two parts out loud, then push them together.", "why": "in + correct = incorrect."},
  "mfill3": {"h1": "Keep both parts. Do not drop any letters.", "why": "im + patient = impatient."},
  "mfill4": {"h1": "Keep both parts. Do not drop any letters.", "why": "in + visible = invisible."}
 },
 "flags": {"journal-q1": {"quote": False, "count": 2}, "journal-q2": {"quote": False, "count": 1}, "journal-q3": {"quote": False, "count": 1}},
 "wordgame": dict(GAME, look=LOOK3, stepTitle="Keep it, or throw it back?", bins=[BIN["keep"], BIN["back"]], items=[
   it_keep("unlock", True, "un + lock: lock is a real word."), it_keep("uncle", False, "Cover the first part: cle is not a word. No prefix."),
   it_keep("refill", True, "re + fill: fill is a real word."), it_keep("real", False, "Cover the first part: al is not a word. No prefix."),
   it_keep("preschool", True, "pre + school: school is a real word."), it_keep("pretty", False, "Cover the first part: tty is not a word. No prefix."),
   it_keep("dislike", True, "dis + like: like is a real word."), it_keep("dish", False, "Cover the first part: h is not a word. No prefix.")]),
 "glossary": GLOSS, "sayWords": [],
 "cards": note("Stone Statues", [
   "Real statues are carved by artists from stone, like marble or granite.",
   "Some old castles and gardens have courtyards full of statues of people and animals.",
   "In the story, the Witch's statues were once living creatures. That part is only in the story."]),
 "transcripts": {"welcome": "Hi, it's Opti. Edmund is alone in the snow. Watch what he tells himself in Chapter 9, and what he really knows.",
  "guide1": "Word work: build not words, fix a sentence's verbs, and proofread prefix words.",
  "guide2": "Read Chapter 9. Then answer three questions.",
  "guide3": "Today you make your comparison more precise."},
 "notes": dict(NOTES_COMMON, wgrd="Edmund tells himself the Witch is the rightful Queen, but deep down he knows she is bad and cruel.", vocab=VOC2)
}
L["27-4"] = {
 "connector": "No new chapters today. Look back at Chapters 7 to 9. Edmund and Lucy heard the same name and felt opposite things. Today you finish your response comparing two characters.",
 "writingFocus": "literary response",
 "dol": dol("mr beaver caught some fish and mrs beaver fried them",
   C("M")+"r"+C(".")+" "+C("B")+"eaver caught some fish"+C(",")+" and "+C("M")+"rs"+C(".")+" "+C("B")+"eaver fried them"+C("."),
   "Mr. Beaver and Mrs. Beaver are titles and names. A comma goes before and. Caught is an irregular past verb.",
   "edmund crossed the river on the ice and he walked up to the house",
   C("E")+"dmund crossed the river on the ice"+C(",")+" and he walked up to the house"+C("."),
   "Edmund is a name. A comma goes before and, because it joins two complete thoughts. Crossed and walked are regular past verbs."),
 "hints": {},
 "flags": {"journal-q1": {"quote": False, "count": 1}, "journal-q2": {"quote": False, "count": 1}, "journal-q3": {"quote": False, "count": 1}},
 "wordgame": dict(GAME, look=LOOK3, stepTitle="Keep it, or throw it back?", bins=[BIN["keep"], BIN["back"]], items=[
   it_keep("misspell", True, "mis + spell: spell is a real word."), it_keep("mister", False, "Cover the first part: ter is not a word. No prefix."),
   it_keep("untie", True, "un + tie: tie is a real word."), it_keep("reach", False, "Cover the first part: ach is not a word. No prefix."),
   it_keep("reheat", True, "re + heat: heat is a real word."), it_keep("press", False, "Cover the first part: ss is not a word. No prefix."),
   it_keep("prepay", True, "pre + pay: pay is a real word."), it_keep("price", False, "Cover the first part: ce is not a word. No prefix.")]),
 "glossary": GLOSS, "sayWords": [],
 "cards": note("The Full Moon", [
   "The moon does not make its own light. It shines with light from the sun.",
   "Snow bounces light back, so a full moon on snow can make a night look almost bright.",
   "In Chapter 9, the full moon comes out and helps Edmund find his way."], before="Look Back"),
 "transcripts": {"welcome": "Hi, it's Opti. Look back at Chapters 7 to 9. Edmund and Lucy heard the same name and felt opposite things.",
  "guide1": "Word work: roll not words, fix a passage in passes, and roll prefix words.",
  "guide2": "Look back at Chapters 7 to 9 for your best details.",
  "guide3": "Today you publish your comparison."},
 "notes": dict(NOTES_COMMON, wgrd="Lucy felt joy at Aslan's name and Edmund felt horror. What each one chose before changed what each one felt.", vocab=VOC2)
}
FLU = {"connector": "This week's passage is from Chapter 7: the moment Mr. Beaver says Aslan's name. Read it three times. The last time, give each child's feeling its own voice.",
 "howto": True,
 "transcripts": {"welcome": "Hi, it's Opti. This week's passage is the moment the children hear Aslan's name. Read it three times. First, get every word right. Next, make it smooth. Then give each child's feeling its own voice."}}
if __name__ == '__main__':
    import sys
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from plates_wk27 import PLATES as P
    for k, p in P.items(): L[k]["plate"] = p
    for k, v in L.items():
        io.open(os.path.join(OUT, 'lesson-%s.json' % k), 'w', encoding='utf-8').write(json.dumps(v, ensure_ascii=False, indent=1)); print(k)
    io.open(os.path.join(OUT, 'lesson-27-fluency.json'), 'w', encoding='utf-8').write(json.dumps(FLU, ensure_ascii=False, indent=1))
