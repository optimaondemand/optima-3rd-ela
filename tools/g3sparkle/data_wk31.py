#!/usr/bin/env python3
"""Week 31 DATA (Paired Texts: The Courage to Act; extension pages lesson-31-*-ext.html): 31.1-31.4, no fluency page.
Text 1 "What Is Courage?" and Text 2 "The Choice at the Bridge" are written for the course (Bethany kept them, Nov 16 2026).
World Notes are about Grace Darling's real rescue (Sept. 7, 1838), the world of the Row to the Wreck game; facts checked
against Royal Museums Greenwich (date, age 22, nine saved, nearly a mile, Longstone Lighthouse, St Aidan's Bamburgh) and
James Baldwin's "Grace Darling" (1896, the monument with an oar). Row to the Wreck items use only this year's prefixes and
suffixes (re-, un-, trans-, inter-, -ful, -less) and syllable counts, and none is an answer elsewhere on the week's pages
(rebuild reread reform unfair unkind uncertain unafraid unhelpful transport transform translate interact interrupt
international careful hopeful faithful fearless hopeless careless endless kindness slowly courageous; invitation
ordinary discovery particular; electricity celebration temperature information vegetable photograph)."""
import json, io, os
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'data')
S = "<strong>"; E = "</strong>"
def C(x): return S + x + E
def dol(a_raw, a_fixed, a_why, b_raw, b_fixed, b_why):
    return {"a": {"raw": a_raw, "fixed": a_fixed, "why": a_why}, "b": {"raw": b_raw, "fixed": b_fixed, "why": b_why}}
GLOSS = [
 {"w": "courage", "m": "being brave enough to do something hard or scary because it matters", "key": True},
 {"w": "prefix", "m": "a word part added to the front of a word, like re- in rebuild", "key": True},
 {"w": "suffix", "m": "a word part added to the end of a word, like -less in fearless", "key": True},
 {"w": "syllable", "m": "a part of a word with one vowel sound. Rescue has two: res and cue.", "key": True},
 {"w": "informational text", "m": "writing that gives facts and explains a topic"},
 {"w": "fiction", "m": "a made-up story"},
 {"w": "claim", "m": "the main idea you want to prove in your writing", "key": True},
]
NOTES_COMMON = {
 "wordParts": "Prefixes and suffixes from this year: re- = again, un- = not, trans- = across, inter- = between, -ful = full of, -less = without.",
 "grammar": "Year review: capitals for names and the first word, a comma after an opening part, apostrophes for belonging and joined words, and irregular past forms like went and took.",
 "spelling": "Long words: find the vowels, split between them, read each chunk, then push the chunks together. Rescue = res + cue."
}
VOC = [["courageous", "having or showing courage; willing to act even when afraid"], ["perseverance", "continuing to try even when things are hard"], ["virtue", "a quality that shows good character"]]
VOC4 = VOC + [["integrity", "doing the right thing even when no one is watching"]]
PMISS = "Find the prefix or suffix. What does that part mean?"
def it_mean(n, w, right, wrong):
    bins = [{"id": "r", "label": right, "ic": "👆"}, {"id": "w", "label": wrong, "ic": "👆"}]
    if n % 2: bins.reverse()
    return {"t": w, "bin": "r", "bins": bins, "why": "%s: %s." % (w, right), "miss": {"w": PMISS}}
BMISS = "Say the word slowly and clap each beat. Count the vowel sounds."
def it_beats(n, word, split):
    k = len(split.split('-')); ids = ["2", "3", "4"]; ids = ids[n % 3:] + ids[:n % 3]
    return {"t": word, "bin": str(k), "bins": [{"id": i, "label": i + " beats", "ic": "👆"} for i in ids],
            "why": "%s = %s: %d beats." % (word, split, k), "miss": {i: BMISS for i in ids if i != str(k)}}
GAME = {"type": "row", "title": "Row to the Wreck",
        "sub": "Every right answer is one pull on the oars.",
        "todo": "Read the word on the boat. Tap the right answer. Each right answer is one pull on the oars.",
        "win": "Today's 8 pulls are done. Come back next lesson to row closer.",
        "winWeek": "You reached the wreck. Nine people saved!"}
LOOK1 = ("This week's game is a real rescue from 1838. Grace Darling and her father row their boat from the lighthouse to a wrecked ship in a storm. "
         "Each word on the boat has a prefix or a suffix. Tap what the word means. Each right answer is one pull on the oars. Over four days you row all the way to the wreck.")
LOOK2 = "Eight more words with prefixes and suffixes. Tap what each word means. The boat starts where you left it last time."
LOOK3 = "Today each word is a long word. Say it slowly and clap: how many beats (syllables) does it have? The storm is calming, and the boat keeps going."
LOOK4 = "Eight more long words. Count the beats in each one. Reach the wreck today and bring everyone home."
def note(title, text, before="Read:|Look Back"):
    return [{"id": "world", "kind": "info", "tab": "reading", "after": before, "before": True, "icon": "🌍",
             "title": "World Notes: " + title, "sub": "A real person and place behind this week's game",
             "todo": "Read the note. Then read with your lens in mind.", "text": text}]
MATCH = {"courageous": "Courageous ends in -ous, full of. Look for the meaning about acting even when afraid.",
         "perseverance": "Perseverance is about not giving up. Look for that meaning.",
         "virtue": "A virtue is part of good character. Look for that meaning."}
MMATCH = {"rebuild": "Re- means again. Look for the meaning with again.", "unkind": "Un- means not. Look for the meaning with not.",
          "hopeful": "-ful means full of. Look for full of.", "endless": "-less means without. Look for without."}
L = {}
L["31-1"] = {
 "connector": "Have you ever done something brave while you were scared? This week you read two texts about courage. Text 1 explains what courage is. Watch for what the author says courage is, and what it is not.",
 "writingFocus": "comparison response",
 "dol": dol("courage isnt the same as having no fear",
   C("C") + "ourage isn" + C("’") + "t the same as having no fear" + C("."),
   "Courage starts the sentence. Isn’t joins is and not. A period ends it.",
   "mira didnt feel brave but she walked onto the bridge",
   C("M") + "ira didn" + C("’") + "t feel brave" + C(",") + " but she walked onto the bridge" + C("."),
   "Mira is a name. Didn’t joins did and not. A comma goes before but."),
 "hints": {
  "fill1": {"h1": "Re- means again. What do you do again to rebuild?", "why": "re + build = rebuild."},
  "fill2": {"h1": "Un- means not. Not what?", "why": "un + afraid = unafraid."},
  "fill3": {"h1": "Trans- means across. Change the shape: what word means shape?", "why": "trans + form = transform."},
  "fill4": {"h1": "Look at the suffix that means without in the table.", "why": "fear + less = fearless."},
  "vcloze1": {"h1": "Look back at the word Opti figured out with you.", "why": "A courageous choice is a brave one."},
  "vcloze2": {"h1": "He kept going and did not give up. Which word means that?", "why": "Perseverance means keeping on, even when it is hard."},
  "vcloze3": {"h1": "Text 1 calls courage one of these. Look at the meanings in the matching game.", "why": "A virtue is a quality of good character."}},
 "miss": {"match": MATCH},
 "flags": {"journal-q1": {"quote": False, "count": 1}, "journal-q2": {"quote": False, "count": 2}, "journal-q3": {"quote": False, "count": 1}},
 "copia": {"look": "One plain sentence from Text 1, and three empty boxes. Each box asks you to say the same idea in a new way.",
   "todo": "Rewrite the sentence three ways, one box at a time. Tap Show one way if you get stuck.",
   "seed": "Courage <b>shows up</b> in many different forms.",
   "eg": ["In stories and in real life, courage shows up in many different forms.",
          "Courage <i>appears</i> in many different forms.",
          "Courage shows up in big, loud moments and in small, quiet ones."]},
 "wordgame": dict(GAME, look=LOOK1, stepTitle="What does it mean?", bins=[], items=[
   it_mean(0, "refill", "to fill again", "to spill out"),
   it_mean(1, "unlock", "to open a lock", "to lock it twice"),
   it_mean(2, "playful", "full of play", "without any play"),
   it_mean(3, "spotless", "without a spot", "full of spots"),
   it_mean(4, "retell", "to tell again", "to keep a secret"),
   it_mean(5, "unpack", "to take things out of a bag", "to put more things in"),
   it_mean(6, "thankful", "full of thanks", "without any thanks"),
   it_mean(7, "sleepless", "without sleep", "full of sleep")]),
 "glossary": GLOSS, "sayWords": [],
 "cards": note("Grace Darling, a Real Rescue", [
   "On September 7, 1838, a steamship called the Forfarshire hit the rocks off the Farne Islands, in England, during a terrible storm. Some of the people on board were left clinging to a rock.",
   "Grace Darling, who was 22, lived in the Longstone Lighthouse with her family. At dawn she saw the people on the rock.",
   "Grace and her father, William, rowed their heavy boat nearly a mile through the waves and saved nine people. This week's game follows their boat."]),
 "transcripts": {"welcome": "Hi, it's Opti. This week is all about courage. Text 1 explains what courage is. Read to find out.",
  "guide1": "Word work first: prefixes and suffixes, a year of grammar, and long words.",
  "guide2": "Read Text 1 with your lens. Then answer three questions.",
  "guide3": "Today you plan your comparison and write your claim."},
 "notes": dict(NOTES_COMMON, wgrd="Text 1 says courage is not having no fear. It is choosing to act anyway, because it matters, one choice at a time.", vocab=VOC)
}
L["31-2"] = {
 "connector": "Can a made-up story teach something true? Text 2 is a made-up story about a girl named Mira and an old, narrow bridge. The author never says Mira is brave. Watch how the story shows it.",
 "writingFocus": "comparison response",
 "dol": dol("when mira spoke the three boys stared at her",
   C("W") + "hen " + C("M") + "ira spoke" + C(",") + " the three boys stared at her" + C("."),
   "When starts the sentence. Mira is a name. A comma comes after the opening part.",
   "although her heart hammered mira took a breath",
   C("A") + "lthough her heart hammered" + C(",") + " " + C("M") + "ira took a breath" + C("."),
   "Although starts the sentence. A comma comes after the opening part. Mira is a name."),
 "hints": {},
 "miss": {"match": dict(MATCH, integrity="Integrity is about doing right even when no one sees. Look for that meaning.", **MMATCH)},
 "flags": {"journal-q1": {"quote": False, "count": 2}, "journal-q2": {"quote": False, "count": 1}, "journal-q3": {"quote": False, "count": 1}},
 "wordgame": dict(GAME, look=LOOK2, stepTitle="What does it mean?", bins=[], items=[
   it_mean(0, "reopen", "to open again", "to close for good"),
   it_mean(1, "unwrap", "to take the wrapping off", "to wrap it up tight"),
   it_mean(2, "joyful", "full of joy", "without any joy"),
   it_mean(3, "harmless", "without harm", "full of harm"),
   it_mean(4, "untrue", "not true", "very true"),
   it_mean(5, "intercity", "a train that goes between cities", "a train inside one city"),
   it_mean(6, "colorful", "full of color", "without color"),
   it_mean(7, "rewind", "to wind back again", "to stop for good")]),
 "glossary": GLOSS, "sayWords": [],
 "cards": note("How a Lighthouse Works", [
   "A lighthouse is a tall tower with a bright light at the top. At night, the light warns ships away from rocks.",
   "Each lighthouse flashes in its own pattern, so sailors can tell which one they are looking at.",
   "Grace Darling's family moved into the new Longstone Lighthouse in 1826, when she was 10. It still stands on its rocky island today."]),
 "transcripts": {"welcome": "Hi, it's Opti. Text 2 is a made-up story. The author never says Mira is brave. Watch how the story shows it.",
  "guide1": "Word work: match word parts, name kinds of sentences, and split long words.",
  "guide2": "Read Text 2. Then watch my video in Read Like a Writer.",
  "guide3": "Today you draft the opening of your comparison."},
 "notes": dict(NOTES_COMMON, wgrd="Text 2 shows courage instead of telling it. Mira’s heart hammers and her feet want to turn around, but she walks onto the bridge.", vocab=VOC4)
}
L["31-3"] = {
 "connector": "Today you are a collector. You go back to both texts and pick the details that prove your claim. One detail from Text 1, one from Text 2, and a sentence that ties them together.",
 "writingFocus": "comparison response",
 "dol": dol("text 1 explains courage and text 2 shows it",
   C("T") + "ext 1 explains courage" + C(",") + " and " + C("T") + "ext 2 shows it" + C("."),
   "Text 1 and Text 2 are names of texts, so they get capitals. A comma goes before and.",
   "mira was afraid but she did not run",
   C("M") + "ira was afraid" + C(",") + " but she did not run" + C("."),
   "Mira is a name. A comma goes before but when it joins two complete thoughts."),
 "hints": {
  "mfill1": {"h1": "Say the two parts out loud, then push them together.", "why": "re + build = rebuild."},
  "mfill2": {"h1": "Say the two parts out loud, then push them together.", "why": "un + kind = unkind."},
  "mfill3": {"h1": "Keep both parts. Do not drop any letters.", "why": "hope + ful = hopeful."},
  "mfill4": {"h1": "Keep both parts. Do not drop any letters.", "why": "end + less = endless."}},
 "flags": {"journal-q1": {"quote": False, "count": 1}, "journal-q2": {"quote": False, "count": 1}, "journal-q3": {"quote": False, "count": 1}},
 "wordgame": dict(GAME, look=LOOK3, stepTitle="How many beats?", bins=[], items=[
   it_beats(0, "rescue", "res-cue"), it_beats(1, "September", "Sep-tem-ber"), it_beats(2, "watermelon", "wa-ter-mel-on"),
   it_beats(3, "lighthouse", "light-house"), it_beats(4, "adventure", "ad-ven-ture"), it_beats(5, "helicopter", "hel-i-cop-ter"),
   it_beats(6, "terrible", "ter-ri-ble"), it_beats(7, "January", "Jan-u-ar-y")]),
 "glossary": GLOSS, "sayWords": [],
 "cards": note("Rowing Through Rough Water", [
   "A rowing boat moves when people pull long oars through the water. In big waves, it takes strength and good timing to keep the boat steady.",
   "Grace and her father rowed a coble, a heavy wooden boat built for the rough North Sea. The real boat is kept today at the Grace Darling Museum in Bamburgh, England.",
   "When they reached the rock, her father climbed out to help the people, and Grace held the boat steady by herself."], before="Look Back"),
 "transcripts": {"welcome": "Hi, it's Opti. Today you collect your best details from both texts.",
  "guide1": "Word work: build words, fix a sentence like an editor, and build long words.",
  "guide2": "Read both texts again. Then answer the questions.",
  "guide3": "Today you write one paragraph for each text."},
 "notes": dict(NOTES_COMMON, wgrd="A comparison needs a detail from each text, and a sentence that shows how they connect. Mira’s words echo Text 1’s idea of courage.", vocab=VOC)
}
L["31-4"] = {
 "connector": "After a whole year of reading, what do you think courage really means? Today you finish your comparison. Then you think back over every book you read this year.",
 "writingFocus": "comparison response",
 "dol": dol("after thinking about both texts i chose my claim",
   C("A") + "fter thinking about both texts" + C(",") + " " + C("I") + " chose my claim" + C("."),
   "After starts the sentence. A comma closes the opening part. I is always a capital.",
   "before i wrote my closing i read both texts again",
   C("B") + "efore " + C("I") + " wrote my closing" + C(",") + " " + C("I") + " read both texts again" + C("."),
   "Before starts the sentence. I is always a capital. A comma closes the opening part."),
 "hints": {},
 "flags": {"journal-q1": {"quote": False, "count": 1}, "journal-q2": {"quote": False, "count": 1}, "journal-q3": {"quote": False, "count": 1}},
 "wordgame": dict(GAME, look=LOOK4, stepTitle="How many beats?", bins=[], items=[
   it_beats(0, "island", "is-land"), it_beats(1, "hurricane", "hur-ri-cane"), it_beats(2, "alligator", "al-li-ga-tor"),
   it_beats(3, "thunder", "thun-der"), it_beats(4, "umbrella", "um-brel-la"), it_beats(5, "caterpillar", "cat-er-pil-lar"),
   it_beats(6, "anchor", "an-chor"), it_beats(7, "fisherman", "fish-er-man")]),
 "glossary": GLOSS, "sayWords": [],
 "cards": note("Remembered in Stone", [
   "Grace Darling became famous all over Britain. People wrote songs and poems about her, and painters came to paint her picture.",
   "She died young, in 1842, and was buried in the churchyard of St Aidan's Church in Bamburgh, near the sea.",
   "A stone monument there shows Grace lying at rest, holding an oar in her hand, so no one forgets the morning she rowed into the storm."], before="Look Back"),
 "transcripts": {"welcome": "Hi, it's Opti. Today you finish your comparison, and think back over the whole year of reading.",
  "guide1": "Word work: roll word-part words, edit in passes, and roll long words.",
  "guide2": "Read both texts one more time. Then answer the questions.",
  "guide3": "Today you finish your comparison."},
 "notes": dict(NOTES_COMMON, wgrd="Both texts say courage means acting even when you are afraid. A strong closing says your claim in a new way and tells why it matters.", vocab=VOC)
}
if __name__ == '__main__':
    import sys
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from plates_wk31 import PLATES as P
    for k, p in P.items(): L[k]["plate"] = p
    for k, v in L.items():
        io.open(os.path.join(OUT, 'lesson-%s.json' % k), 'w', encoding='utf-8').write(json.dumps(v, ensure_ascii=False, indent=1)); print(k)
