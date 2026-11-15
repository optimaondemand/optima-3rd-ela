#!/usr/bin/env python3
"""Week 29 DATA (The Lion, the Witch and the Wardrobe, Ch. 13-15): 29.1-29.4 + fluency.
Every book line checked against Planning docs/lww_text.txt (nothing past Ch. 15; each day's lines from that day's chapter or
earlier: Day 1 = Ch. 13 only, Day 2 = Ch. 14, Day 3 = Ch. 15). Hard content kept gentle for 8-year-olds (Bethany, Nov 15).
Skipping Stones items use only this week's word study (ject = throw with re-, in-, e-, pro-; roots ject, script/scribe, spect,
port) and are not answers elsewhere on the week's pages (reject inject eject project projector objection; unexpected
enchanted disobeyed bewildered unbelievable reappeared describe manuscript inscription prescription). Days 1-2 use
inflected ject words in new sentences ("which way is it thrown?"). Film examples are kept out of the game
(projectile, interject, object, trajectory; see teach_wk29.py)."""
import json, io, os
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'data')
S = "<strong>"; E = "</strong>"
def C(x): return S + x + E
Q = '"'
def dol(a_raw, a_fixed, a_why, b_raw, b_fixed, b_why):
    return {"a": {"raw": a_raw, "fixed": a_fixed, "why": a_why}, "b": {"raw": b_raw, "fixed": b_fixed, "why": b_why}}
GLOSS = [
 {"w": "theme", "m": "the big lesson a story teaches, said as a full sentence", "key": True},
 {"w": "topic", "m": "what a story is about, in a word or two, like loyalty or winter"},
 {"w": "dialogue", "m": "the words characters say out loud in a story", "key": True},
 {"w": "quotation marks", "m": "the marks “ and ” that go around the exact words someone says", "key": True},
 {"w": "dialogue tag", "m": "the part that tells who is talking, like said Lucy"},
 {"w": "root", "m": "the main part of a word that holds its meaning, like ject, which means throw", "key": True},
 {"w": "affix", "m": "a part added to the front or the end of a word, like un- or -ed"},
 {"w": "honesty", "m": "telling the truth, even when it is hard", "key": True},
]
NOTES_COMMON = {
 "wordParts": "The root ject means throw. reject = throw back. inject = throw into. eject = throw out. project = throw forward.",
 "grammar": "Quotation marks go around the exact words someone says. The first word gets a capital. The comma or period goes inside the closing mark: “Let him approach,” said Aslan.",
 "spelling": "A long word is often a root with parts added. Find the root first: un + expect + ed = unexpected."
}
VOC = [["traitor", "someone who betrays the trust of their own side"], ["atone", "to make up for a wrong you have done"], ["sacrifice", "giving up something precious for something or someone more important"]]
VOC4 = VOC + [["resurrection", "coming back to life after death"]]
WAY = {"back": {"id": "back", "label": "Thrown back", "ic": "👆"}, "into": {"id": "into", "label": "Thrown into", "ic": "👆"},
       "out": {"id": "out", "label": "Thrown out", "ic": "👆"}, "fwd": {"id": "fwd", "label": "Thrown forward", "ic": "👆"}}
WAYS = [WAY["back"], WAY["into"], WAY["out"], WAY["fwd"]]
PRE = {"back": "re", "into": "in", "out": "e", "fwd": "pro"}
WMISS = "Look at the part in front of ject. What does that front part mean?"
def it_way(sent, word, way):
    return {"t": sent, "bin": way, "why": "%s: %s- means %s." % (word, PRE[way], {"back": "back", "into": "into", "out": "out", "fwd": "forward"}[way]),
            "miss": {w: WMISS for w in PRE if w != way}}
ROOT = {"ject": {"id": "ject", "label": "ject (throw)", "ic": "👆"}, "script": {"id": "script", "label": "script or scribe (write)", "ic": "👆"},
        "spect": {"id": "spect", "label": "spect (look)", "ic": "👆"}, "port": {"id": "port", "label": "port (carry)", "ic": "👆"}}
ROOTS = [ROOT["ject"], ROOT["script"], ROOT["spect"], ROOT["port"]]
RMISS = "Cover the front and the end of the word. Which letters are left in the middle?"
def it_root(word, root, parts):
    return {"t": word, "bin": root, "why": "%s: %s." % (word, parts), "miss": {r: RMISS for r in ROOT if r != root}}
GAME = {"type": "skip", "title": "Skipping Stones",
        "sub": "Every right answer throws a stone into the river.",
        "todo": "Read the word on the stone. Tap the right answer. A right answer skips the stone across the river.",
        "win": "Today's 8 stones are in the river. Come back next lesson to throw more.",
        "winWeek": "The stepping stones reach all the way across the river!"}
LOOK1 = ("This week's game is a river at a shallow crossing, called a ford. Each stone has a sentence with a ject word in it. "
         "Remember: ject means throw. Tap which way something is thrown: back, into, out or forward. "
         "Each right answer skips a stone into the river. Over four days you build a path of stepping stones across.")
LOOK2 = ("Eight new stones with eight new sentences. Look at the part in front of ject, and tap which way something is thrown. "
         "The stones from Day 1 are still in the river.")
LOOK3 = ("Today each stone has a long word. Find its root in the middle: ject (throw), script or scribe (write), spect (look) or port (carry). "
         "The stones from earlier days are still in the river.")
LOOK4 = ("Eight more stones with eight more long words. Cover the front and the end, and find the root. "
         "Throw these and the path reaches all the way across.")
def note(title, text, before="Read:|Look Back"):
    return [{"id": "world", "kind": "info", "tab": "reading", "after": before, "before": True, "icon": "🌍",
             "title": "World Notes: " + title, "sub": "A real thing behind the story",
             "todo": "Read the note. Then read the chapter with your lens in mind.", "text": text}]
MATCH = {"traitor": "A traitor turns against his own side. Look for the meaning about trust.",
         "atone": "Atone is about making up for a wrong. Look for that meaning.",
         "sacrifice": "A sacrifice means giving something up. Look for the meaning about giving up."}
FILLH = {"h1": "Look at the table of four words. Which four letters are in every one?", "why": "The root is ject."}
L = {}
L["29-1"] = {
 "connector": "Has anyone ever said to you, “Let’s not talk about it anymore”? In Chapter 13, Edmund is rescued, and Aslan tells his family there is no need to talk about what is past. Watch for big ideas forming: forgiveness, loyalty, and what is fair.",
 "writingFocus": "literary response",
 "dol": dol(Q + "here is your brother" + Q + " said aslan",
   Q + C("H") + "ere is your brother" + C(",") + Q + " said " + C("A") + "slan" + C("."),
   "Here starts the spoken words, so it gets a capital. The comma goes inside the quotation mark. Aslan is a name.",
   Q + "im sorry" + Q + " said edmund",
   Q + C("I") + C("’") + "m sorry" + C(",") + Q + " said " + C("E") + "dmund" + C("."),
   "I’m starts the spoken words and joins I and am. The comma goes inside the quotation mark. Edmund is a name."),
 "hints": {"fill1": FILLH, "fill2": FILLH, "fill3": FILLH, "fill4": FILLH,
  "vcloze1": {"h1": "The Witch says Edmund turned against his own side. Look back at the word Opti figured out with you.", "why": "A traitor betrays the trust of their own side."},
  "vcloze2": {"h1": "This word is about making up for a wrong. Look at the meanings in the matching game.", "why": "To atone is to make up for a wrong you have done."},
  "vcloze3": {"h1": "Mom gave up her free day to help others. Find the word about giving something up.", "why": "A sacrifice is giving up something precious for something more important."}},
 "miss": {"match": MATCH},
 "flags": {"journal-q1": {"quote": False, "count": 1}, "journal-q2": {"quote": False, "count": 1}, "journal-q3": {"quote": False, "count": 1}},
 "copia": {"look": "One plain sentence from Chapter 13, and three empty boxes. Each box asks you to say the same idea in a new way.",
   "todo": "Rewrite the sentence three ways, one box at a time. Tap Show one way if you get stuck.",
   "seed": "Edmund <b>looked</b> at Aslan.",
   "eg": ["In the bright sunshine, Edmund looked at Aslan.",
          "Edmund <i>gazed</i> at Aslan.",
          "Edmund looked at Aslan’s golden face and did not look away."]},
 "wordgame": dict(GAME, look=LOOK1, stepTitle="Which way is it thrown?", bins=WAYS, items=[
   it_way("The goalie rejected the shot and sent it flying back.", "rejected", "back"),
   it_way("The pilot ejected from the plane and floated down with a parachute.", "ejected", "out"),
   it_way("The nurse injected the medicine with a tiny needle.", "injected", "into"),
   it_way("The movie was projected onto the big screen.", "projected", "fwd"),
   it_way("The printer ejected the jammed paper.", "ejected", "out"),
   it_way("The store rejected the broken toy and sent it back to the maker.", "rejected", "back"),
   it_way("The teacher projected her voice to the back of the room.", "projected", "fwd"),
   it_way("The vet injected the puppy’s shot.", "injected", "into")]),
 "glossary": GLOSS, "sayWords": [],
 "cards": note("A Lion’s Roar", [
   "A real lion’s roar is one of the loudest sounds any animal makes. On a quiet night it can be heard about five miles away.",
   "Lions roar to tell other lions, This is our land. They also roar to call their family group, called a pride, back together.",
   "In Chapter 13, Aslan gives a great roar, and the Witch runs for her life."]),
 "transcripts": {"welcome": "Hi, it's Opti. In Chapter 13, Edmund is rescued, and the Witch comes to talk with Aslan. Watch for big ideas forming.",
  "guide1": "Word work first: the root ject, the marks around spoken words, and long words built from parts.",
  "guide2": "Read Chapter 13 with your lens. Then answer three questions.",
  "guide3": "Today you brainstorm possible themes."},
 "notes": dict(NOTES_COMMON, wgrd="A topic is one word, like loyalty. A theme is a full sentence about it: The story shows that forgiveness can give someone a fresh start.", vocab=VOC)
}
L["29-2"] = {
 "connector": "Chapter 14 is the saddest chapter in the book. Lucy and Susan cannot sleep, so they follow Aslan into the moonlight. Read it slowly. Notice what Aslan chooses to do, and what it might show about the story’s big lesson. The story is not over yet.",
 "writingFocus": "literary response",
 "dol": dol(Q + "cant you get to sleep either" + Q + " said susan",
   Q + C("C") + "an" + C("’") + "t you get to sleep either" + C("?") + Q + " said " + C("S") + "usan" + C("."),
   "Can’t starts the spoken words and joins can and not. The question mark goes inside the quotation mark. Susan is a name.",
   Q + "we will" + Q + " said the two girls",
   Q + C("W") + "e will" + C(",") + Q + " said the two girls" + C("."),
   "We starts the spoken words. The comma goes inside the quotation mark. The tag ends with a period."),
 "hints": {},
 "miss": {"match": MATCH},
 "flags": {"journal-q1": {"quote": False, "count": 2}, "journal-q2": {"quote": False, "count": 1}, "journal-q3": {"quote": False, "count": 1}},
 "wordgame": dict(GAME, look=LOOK2, stepTitle="Which way is it thrown?", bins=WAYS, items=[
   it_way("The DVD player ejected the disc.", "ejected", "out"),
   it_way("The doctor injected a little medicine into Grandpa’s arm.", "injected", "into"),
   it_way("The coach rejected my first plan, so I had to think again.", "rejected", "back"),
   it_way("The class projected the map onto the wall.", "projected", "fwd"),
   it_way("The volcano ejected hot ash into the sky.", "ejected", "out"),
   it_way("The chef injected juice into the turkey.", "injected", "into"),
   it_way("The library rejected my late form and handed it back.", "rejected", "back"),
   it_way("The singer projected her voice all the way to the last row.", "projected", "fwd")]),
 "glossary": GLOSS, "sayWords": [],
 "cards": note("Stone Tables", [
   "Long ago, people in Ireland, Britain, France and many other places built real stone tables called dolmens.",
   "A dolmen is a big flat stone set on top of standing stones. Many were built more than 5,000 years ago, and some are still standing.",
   "Nobody knows exactly how such heavy stones were lifted. In the story, the Stone Table is very old, too, and the Deep Magic is written on it."]),
 "transcripts": {"welcome": "Hi, it's Opti. Chapter 14 is the saddest chapter in the book. Read it slowly, and notice what Aslan chooses to do.",
  "guide1": "Word work: match ject words, fix dialogue mistakes, and find long words built from parts.",
  "guide2": "Read Chapter 14. Then watch my video in Read Like a Writer.",
  "guide3": "Today you draft your response on theme."},
 "notes": dict(NOTES_COMMON, wgrd="Aslan gives his own life so that Edmund can go free. This is strong proof for a theme about love or sacrifice.", vocab=VOC)
}
L["29-3"] = {
 "connector": "Chapter 15 begins on the saddest night of the story and ends with the sun coming up. Watch what Lucy and Susan see at sunrise, and listen to what Aslan explains. Ask yourself how it changes the big lesson you have been building.",
 "writingFocus": "literary response",
 "dol": dol(Q + "whats that" + Q + " said lucy",
   Q + C("W") + "hat" + C("’") + "s that" + C("?") + Q + " said " + C("L") + "ucy" + C("."),
   "What’s starts the spoken words and joins what and is. The question mark goes inside the quotation mark. Lucy is a name.",
   Q + "do i look it" + Q + " he said",
   Q + C("D") + "o " + C("I") + " look it" + C("?") + Q + " he said" + C("."),
   "Do starts the spoken words. I is always a capital. The question mark goes inside. He stays lowercase in the tag."),
 "hints": {
  "mfill1": {"h1": "Say the two parts out loud, then push them together.", "why": "re + ject = reject."},
  "mfill2": {"h1": "Say the two parts out loud, then push them together.", "why": "in + ject = inject."},
  "mfill3": {"h1": "Keep both parts. Do not drop any letters.", "why": "e + ject = eject."},
  "mfill4": {"h1": "Keep both parts. Do not drop any letters.", "why": "pro + ject = project."}},
 "flags": {"journal-q1": {"quote": False, "count": 1}, "journal-q2": {"quote": False, "count": 1}, "journal-q3": {"quote": False, "count": 1}},
 "wordgame": dict(GAME, look=LOOK3, stepTitle="Which root is in the middle?", bins=ROOTS, items=[
   it_root("dejected", "ject", "de + ject + ed"), it_root("spectator", "spect", "spect + ator"),
   it_root("portable", "port", "port + able"), it_root("subscription", "script", "sub + script + ion"),
   it_root("subject", "ject", "sub + ject"), it_root("spectacles", "spect", "spect + acles"),
   it_root("import", "port", "im + port"), it_root("postscript", "script", "post + script")]),
 "glossary": GLOSS, "sayWords": [],
 "cards": note("Field Mice and the Morning Star", [
   "Field mice have sharp front teeth that never stop growing. Gnawing keeps them short, and mice can chew right through rope and string.",
   "Just before sunrise, you can sometimes see one very bright star low in the east. Often it is not a star at all. It is the planet Venus, called the morning star.",
   "In Chapter 15, Lucy and Susan see both: little mice, and one big star low in the east as the night ends."]),
 "transcripts": {"welcome": "Hi, it's Opti. Chapter 15 begins on a sad night and ends at sunrise. Watch what Lucy and Susan see.",
  "guide1": "Word work: build ject words, fix a line of dialogue, and spell long words from the root.",
  "guide2": "Read Chapter 15. Then answer three questions.",
  "guide3": "Today you add proof from Chapter 15 to your response."},
 "notes": dict(NOTES_COMMON, wgrd="The Deeper Magic means a willing, innocent life given for a traitor makes death work backwards. It makes the theme stronger: love is stronger than the Witch's law.", vocab=VOC4)
}
L["29-4"] = {
 "connector": "No new chapters today. Look back at the whole book so far, from Edmund and the Turkish Delight to the Stone Table at sunrise. Today you pick your strongest proof and finish your literary response on theme.",
 "writingFocus": "literary response",
 "dol": dol(Q + "peace beaver" + Q + " said aslan",
   Q + C("P") + "eace" + C(",") + " " + C("B") + "eaver" + C(",") + Q + " said " + C("A") + "slan" + C("."),
   "Peace starts the spoken words. A comma sets off Beaver, the one being spoken to, and another goes inside the quotation mark.",
   Q + "so am i" + Q + " said susan",
   Q + C("S") + "o am " + C("I") + C(",") + Q + " said " + C("S") + "usan" + C("."),
   "So starts the spoken words. I is always a capital. The comma goes inside the quotation mark. Susan is a name."),
 "hints": {},
 "flags": {"journal-q1": {"quote": False, "count": 1}, "journal-q2": {"quote": False, "count": 3}, "journal-q3": {"quote": False, "count": 1}},
 "wordgame": dict(GAME, look=LOOK4, stepTitle="Which root is in the middle?", bins=ROOTS, items=[
   it_root("adjective", "ject", "ad + ject + ive"), it_root("respect", "spect", "re + spect"),
   it_root("transport", "port", "trans + port"), it_root("subscribe", "script", "sub + scribe"),
   it_root("spectacular", "spect", "spect + acular"), it_root("export", "port", "ex + port"),
   it_root("scripted", "script", "script + ed"), it_root("inspector", "spect", "in + spect + or")]),
 "glossary": GLOSS, "sayWords": [],
 "cards": note("A Lion’s Mane", [
   "Only grown male lions have a mane, the thick ring of hair around the head and neck.",
   "A big mane makes a lion look larger. Scientists think a darker, fuller mane can also show other lions that he is strong and healthy.",
   "A mane takes years to grow. In the story, Aslan’s golden mane is part of what makes him look so royal."], before="Look Back"),
 "transcripts": {"welcome": "Hi, it's Opti. Look back at the whole book so far. Pick your strongest proof, and finish your response on theme.",
  "guide1": "Word work: roll ject words, fix a passage in passes, and roll long words.",
  "guide2": "Look back at Chapters 13 to 15 for your best details.",
  "guide3": "Today you finish your literary response."},
 "notes": dict(NOTES_COMMON, wgrd="A theme needs proof from the beginning, the middle and the end. Edmund betrays his family, he is forgiven, and Aslan gives his life for him.", vocab=VOC4)
}
FLU = {"connector": "This week's passage is from Chapter 14: Lucy and Susan walk beside Aslan in the moonlight. Read it three times. The last time, slow down at every period, and let the girls' questions sound worried.",
 "howto": True,
 "transcripts": {"welcome": "Hi, it's Opti. This week's passage is the quiet walk in Chapter 14. Read it three times. First, get every word right. Next, make it smooth. Then slow down and let the questions sound worried."}}
if __name__ == '__main__':
    import sys
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from plates_wk29 import PLATES as P
    for k, p in P.items(): L[k]["plate"] = p
    for k, v in L.items():
        io.open(os.path.join(OUT, 'lesson-%s.json' % k), 'w', encoding='utf-8').write(json.dumps(v, ensure_ascii=False, indent=1)); print(k)
    io.open(os.path.join(OUT, 'lesson-29-fluency.json'), 'w', encoding='utf-8').write(json.dumps(FLU, ensure_ascii=False, indent=1))
