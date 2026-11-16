#!/usr/bin/env python3
"""Week 32 DATA (Year-End Culmination: The 7 Pillars of Virtue; extension pages lesson-32-*-ext.html): 32.1-32.4, no fluency.
Every book moment (Pillar Watch, Bookshelf Awards, Reading Road) is checked in Planning docs (flat_stanley_text.txt book 1,
whipping_boy_ocr.txt, despereaux_ocr.txt, lww_text.txt). World Notes facts: Wikipedia "The Flat Stanley Project" (1995,
Dale Hubert, London, Ontario); Wikipedia "Barnaby Fitzpatrick" (closest companion of Prince Edward; historian Leanda de
Lisle: no evidence from the time that he was a whipping boy); OUP blog (courtesy < Old French curtesie, from court);
Wheaton College Wade Center (wardrobe hand-made by Richard Lewis, C.S. Lewis's grandfather, in the 1800s; Little Lea,
Belfast, then The Kilns). Raise the 7 Pillars items use only this year's word parts and spelling rules, and none is an
answer elsewhere on the week's pages (helpful careless redo unfair darkness uncover truthful rewrite brightness unlucky
reheat fearful untie restless wonderful recheck; hoping hopping cried boxes making running ponies wishes baking swimming
tried glasses skipped pennies riding buses)."""
import json, io, os
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'data')
S = "<strong>"; E = "</strong>"
def C(x): return S + x + E
def dol(a_raw, a_fixed, a_why, b_raw, b_fixed, b_why):
    return {"a": {"raw": a_raw, "fixed": a_fixed, "why": a_why}, "b": {"raw": b_raw, "fixed": b_fixed, "why": b_why}}
GLOSS = [
 {"w": "pillar", "m": "a tall post that holds up a building. The 7 pillars hold up good character.", "key": True},
 {"w": "virtue", "m": "a quality that shows good character, like honesty or courage", "key": True},
 {"w": "courtesy", "m": "being polite and kind with your words and actions"},
 {"w": "prefix", "m": "a word part added to the front of a word, like un- in unkind", "key": True},
 {"w": "suffix", "m": "a word part added to the end of a word, like -ful in hopeful", "key": True},
 {"w": "base word", "m": "the main word before a prefix or suffix is added. Hope is the base word in hopeful."},
 {"w": "claim", "m": "the main idea you want to prove in your writing", "key": True},
 {"w": "body paragraph", "m": "a paragraph in the middle of your writing that gives one reason and an example"},
]
NOTES_COMMON = {
 "wordParts": "Word parts I know: -y and -ness mean being something, -ous means full of, -ful means full of, -less means without, un- means not, re- means again.",
 "grammar": "Editing checklist: capitals on names and the first word, apostrophes for belonging and joined words, a comma before and/but/so when it joins two complete thoughts, and the right past form, like went.",
 "spelling": "Find the base word first. Then check what was added: drop the silent e (hope, hoping), double the last letter (hop, hopping), change y to i (cry, cried), or add -es (box, boxes)."
}
VOC = [["integrity", "doing the right thing even when no one is watching"], ["empathy", "understanding and sharing the feelings of another person"],
       ["resilience", "the ability to keep going after something hard"]]
VOC4 = VOC + [["perseverance", "continuing to try even when things are hard"]]
PMISS = "Find the prefix or suffix. What does that part mean?"
def it_mean(n, w, right, wrong):
    bins = [{"id": "r", "label": right, "ic": "👆"}, {"id": "w", "label": wrong, "ic": "👆"}]
    if n % 2: bins.reverse()
    return {"t": w, "bin": "r", "bins": bins, "why": "%s: %s." % (w, right), "miss": {"w": PMISS}}
RULES = [("e", "Drop the silent e"), ("d", "Double the last letter"), ("y", "Change y to i"), ("es", "Add -es")]
RMISS = {"e": "Look at the base word. Does it end in a silent e?", "d": "Look at the base word. Is it short, with one vowel and one last consonant?",
         "y": "Look at the base word. Does it end in y?", "es": "Look at the base word. Does it end in s, x, sh or ch?"}
def it_rule(n, word, base, rule):
    ids = [r[0] for r in RULES]; k = n % 4; ids = ids[k:] + ids[:k]
    lab = dict(RULES)
    return {"t": word, "bin": rule, "bins": [{"id": i, "label": lab[i], "ic": "👆"} for i in ids],
            "why": "%s comes from %s: %s." % (word, base, lab[rule].lower()), "miss": {i: RMISS[i] for i in ids if i != rule}}
NAMES = ["Honesty", "Respect", "Courtesy", "Responsibility", "Courage", "Service", "Perseverance"]
GAME = {"type": "pillars", "title": "Raise the 7 Pillars", "names": NAMES,
        "sub": "Every right answer raises the temple a little more.",
        "todo": "Read the word on the temple. Tap the right answer. Each right answer raises the pillars.",
        "win": "Today's 8 are done. Come back next lesson to raise the pillars higher.",
        "winWeek": "All 7 pillars stand, and the roof is on. Your year of words built this!"}
LOOK = {1: "Seven stone pillars, one for each pillar of good character. Each word has a prefix or a suffix. Tap what the word means, and the pillars rise.",
        2: "Eight more words with prefixes and suffixes. Tap what each word means. The pillars start where you left them.",
        3: "Today each word has an ending added. Find the base word. Then tap the spelling rule that was used.",
        4: "Eight more words. Tap the spelling rule for each one. Finish the temple today and the roof goes on."}
def note(title, text, sub):
    return {"id": "world", "kind": "info", "tab": "reading", "after": "Read:|Look Back", "before": True, "icon": "🌍",
            "title": "World Notes: " + title, "sub": sub, "todo": "Read the note. Then read with your lens in mind.", "text": text}
MATCH = {"integrity": "Integrity is about doing right when no one sees. Look for that meaning.",
         "empathy": "Empathy is about feeling what someone else feels. Look for that meaning.",
         "resilience": "Resilience is about bouncing back after something hard. Look for that meaning.",
         "perseverance": "Perseverance is about not giving up. Look for that meaning."}
AWARDS = {"id": "awards", "kind": "awards", "tab": "reading", "after": "Q3 —", "title": "Bookshelf Awards",
  "sub": "Give a ribbon to a character from this year's books",
  "todo": "Read the ribbon. Tap the character you would give it to. Then read what they did.",
  "win": "Every ribbon has a winner! Your awards are saved in your work.",
  "ribbons": [
   {"id": "brave", "name": "Bravest", "ic": "🦁", "q": "Who was the bravest?", "opts": [
     {"who": "Despereaux", "book": "The Tale of Despereaux", "moment": "He went down into the dark dungeon to save the princess."},
     {"who": "Jemmy", "book": "The Whipping Boy", "moment": "He told the outlaws, &ldquo;Lay down the whip,&rdquo; to stop them from whipping the prince."},
     {"who": "Edmund", "book": "The Lion, the Witch and the Wardrobe", "moment": "In the battle, he fought his way to the Witch and smashed her wand."}]},
   {"id": "honest", "name": "Most Honest", "ic": "💎", "q": "Who was the most honest?", "opts": [
     {"who": "Lucy", "book": "The Lion, the Witch and the Wardrobe", "moment": "She kept saying Narnia was real, even when no one believed her."},
     {"who": "Edmund", "book": "The Lion, the Witch and the Wardrobe", "moment": "After his talk with Aslan, he said &ldquo;I&rsquo;m sorry&rdquo; to each of his brother and sisters."}]},
   {"id": "kind", "name": "Kindest", "ic": "💛", "q": "Who was the kindest?", "opts": [
     {"who": "The Princess Pea", "book": "The Tale of Despereaux", "moment": "She asked Roscuro, &ldquo;Would you like some soup?&rdquo; even after all he had done."},
     {"who": "Mrs. Lambchop", "book": "Flat Stanley", "moment": "She told Stanley, &ldquo;It is wrong to dislike people for their shapes.&rdquo;"},
     {"who": "Stanley", "book": "Flat Stanley", "moment": "He stayed in a picture frame all night to help catch the sneak thieves."}]},
   {"id": "change", "name": "Biggest Change", "ic": "🌱", "q": "Who changed the most?", "opts": [
     {"who": "Prince Brat", "book": "The Whipping Boy", "moment": "He began the book calling Jemmy a rascal, and by the end he wanted Jemmy as his friend."},
     {"who": "Edmund", "book": "The Lion, the Witch and the Wardrobe", "moment": "He began by helping the Witch, and ended as King Edmund the Just."}]}]}
LOOKBACK = {"id": "lookback", "kind": "lookback", "tab": "reading", "after": "Q1 —", "title": "The Reading Road: Look Back",
  "sub": "Your whole year, one stop at a time",
  "todo": "Tap each stop on the road to see what you learned there. Then tap your favorite book.",
  "win": "What a year of reading!",
  "stops": [
   {"book": "Flat Stanley", "ic": "✉️", "color": "#2A9BC0", "learned": "You learned to find the characters, the setting and the problem, and how events change a character."},
   {"book": "The Tale of Despereaux", "ic": "🐭", "color": "#C7922C", "learned": "You learned that different characters see things in different ways, and that a small character can be very brave."},
   {"book": "The Whipping Boy", "ic": "🏰", "color": "#7B2E3B", "learned": "You learned how two characters can change each other, and how to compare them."},
   {"book": "The Lion, the Witch and the Wardrobe", "ic": "🦁", "color": "#1B7A4E", "learned": "You learned about symbols and themes: what a story teaches, and how a character like Edmund can change."}]}
CERT = {"id": "cert", "kind": "cert", "tab": "assignment", "title": "Your 3rd Grade Certificate", "sub": "From Opti, for a whole year of reading",
  "todo": "Tap the pillar you will take to 4th grade. Check your name. Then save your certificate.",
  "head": "Story Map Explorer", "line": "who walked the whole Reading Road: four books in 3rd grade ELA.", "pillars": NAMES}

L = {}
L["32-1"] = {
 "connector": "Which character from our books would you want as a friend? This week you pick one character and show the good character inside them. First, meet the 7 pillars.",
 "writingFocus": "culmination response",
 "dol": dol("honesty means telling the truth even when its difficult and thats one of the hardest things a person can do",
   C("H") + "onesty means telling the truth even when it" + C("’") + "s difficult" + C(",") + " and that" + C("’") + "s one of the hardest things a person can do" + C("."),
   "Honesty starts the sentence. It’s and that’s are joined words. A comma goes before and.",
   "lucy told the truth about narnia but her brothers and sister didnt believe her",
   C("L") + "ucy told the truth about " + C("N") + "arnia" + C(",") + " but her brothers and sister didn" + C("’") + "t believe her" + C("."),
   "Lucy and Narnia are names. A comma goes before but. Didn’t joins did and not."),
 "hints": {
  "fill1": {"h1": "Honest is the base word. Which ending means being honest?", "why": "honest + y = honesty."},
  "fill2": {"h1": "Which ending means full of?", "why": "courage + ous = courageous."},
  "fill3": {"h1": "Look at the table at the top for the ending on perseverance.", "why": "persevere + ance = perseverance (the e drops)."},
  "fill4": {"h1": "Re- is the front part. What comes after it in respect?", "why": "re + spect = respect."},
  "vcloze1": {"h1": "Look back at the word Opti figured out with you.", "why": "Integrity means doing right even when no one is watching."},
  "vcloze2": {"h1": "Which word means feeling what other people feel?", "why": "Empathy means understanding and sharing someone's feelings."},
  "vcloze3": {"h1": "Which word means bouncing back and keeping going?", "why": "Resilience means you keep going after something hard."}},
 "miss": {"match": MATCH},
 "flags": {"journal-q1": {"quote": False, "count": 1}, "journal-q2": {"quote": False, "count": 2}, "journal-q3": {"quote": False, "count": 1}},
 "copia": {"look": "One plain sentence about a pillar, and three empty boxes. Each box asks you to say the same idea in a new way.",
   "todo": "Rewrite the sentence three ways, one box at a time. Tap Show one way if you get stuck.",
   "seed": "Courage <b>means</b> acting even when you are afraid.",
   "eg": ["Even when you are afraid, courage means acting anyway.",
          "Courage <i>is</i> doing the right thing while your knees shake.",
          "Courage means acting even when you are afraid, because something matters more than your fear."]},
 "wordgame": dict(GAME, look=LOOK[1], stepTitle="What does it mean?", bins=[], items=[
   it_mean(0, "helpful", "full of help", "without any help"),
   it_mean(1, "careless", "without care", "full of care"),
   it_mean(2, "redo", "to do again", "to never do"),
   it_mean(3, "unfair", "not fair", "very fair"),
   it_mean(4, "darkness", "being dark", "getting lighter"),
   it_mean(5, "uncover", "to take the cover off", "to cover it more"),
   it_mean(6, "truthful", "full of truth", "without the truth"),
   it_mean(7, "rewrite", "to write again", "to stop writing")]),
 "glossary": GLOSS, "sayWords": [],
 "cards": [note("The Real Flat Stanley Project", [
   "In 1995, a 3rd grade teacher in Canada named Dale Hubert had an idea. His class read <i>Flat Stanley</i>. Then each student colored a paper Stanley and mailed him to a friend or family member far away.",
   "The person who got the paper Stanley took a picture with him and wrote back about his adventures.",
   "Today, kids all over the world still mail paper Stanleys, just like Stanley traveled in an envelope in the book."],
   "A real thing behind one of our books")],
 "transcripts": {"welcome": "Hi, it's Opti. This is our last week together. You pick one character and show the good character inside them.",
  "guide1": "Word work first: word parts from the year, three big words, and one last editing job.",
  "guide2": "Read about the 7 pillars. Then choose your character.",
  "guide3": "Today you plan: your character and two pillars."},
 "notes": dict(NOTES_COMMON, wgrd="The 7 pillars of good character are honesty, respect, courtesy, responsibility, courage, service and perseverance. Our books show all of them.", vocab=VOC)
}
L["32-2"] = {
 "connector": "What does a good paragraph about a character need? A pillar, a real example from the book, and a sentence that says what it shows. Today you write two of them.",
 "writingFocus": "culmination response",
 "dol": dol("jemmys courage grew slowly throughout the whipping boy and by the end he had become someone even he didnt recognize",
   C("J") + "emmy" + C("’") + "s courage grew slowly throughout " + C("<i>The Whipping Boy</i>") + C(",") + " and by the end he had become someone even he didn" + C("’") + "t recognize" + C("."),
   "Jemmy’s shows belonging. A book title gets capitals. A comma goes before and. Didn’t joins did and not.",
   "despereauxs courage grew in the dark and by the end he had saved the princess",
   C("D") + "espereaux" + C("’") + "s courage grew in the dark" + C(",") + " and by the end he had saved the princess" + C("."),
   "Despereaux’s shows belonging, so it gets a capital and an apostrophe. A comma goes before and."),
 "hints": {},
 "miss": {"match": MATCH},
 "flags": {"journal-q1": {"quote": False, "count": 1}, "journal-q2": {"quote": False, "count": 2}},
 "wordgame": dict(GAME, look=LOOK[2], stepTitle="What does it mean?", bins=[], items=[
   it_mean(0, "brightness", "being bright", "getting darker"),
   it_mean(1, "unlucky", "not lucky", "very lucky"),
   it_mean(2, "reheat", "to heat again", "to cool down"),
   it_mean(3, "fearful", "full of fear", "without fear"),
   it_mean(4, "untie", "to undo a knot", "to tie it tighter"),
   it_mean(5, "restless", "without rest", "full of rest"),
   it_mean(6, "wonderful", "full of wonder", "without wonder"),
   it_mean(7, "recheck", "to check again", "to never check")]),
 "glossary": GLOSS, "sayWords": [],
 "cards": [note("Real Whipping Boys?", [
   "<i>The Whipping Boy</i> is a made-up story, but it grew from an old idea: a boy who was punished when a prince misbehaved.",
   "Prince Edward of England, who later became King Edward VI, grew up with a best friend named Barnaby Fitzpatrick. Stories say Barnaby was Edward&rsquo;s whipping boy.",
   "Historians today say there is no proof from that time that Barnaby was ever whipped for the prince. But he really was the prince&rsquo;s closest friend, a little like Jemmy and Prince Brat at the end of the book."],
   "A real thing behind one of our books")],
 "transcripts": {"welcome": "Hi, it's Opti. Today you write your opening and two body paragraphs.",
  "guide1": "Word work: match word parts, name kinds of sentences, and pick the spelling rule.",
  "guide2": "Write your opening and two paragraphs. Then watch my video in Read Like a Writer.",
  "guide3": "Your draft lives on the Reading tab today."},
 "notes": dict(NOTES_COMMON, wgrd="A body paragraph names one pillar, gives a real example from the book, and says what the example shows about the character.", vocab=VOC4)
}
L["32-3"] = {
 "connector": "What makes an ending stick in your head? Today you make your writing stronger and write your closing. Then you give out some awards.",
 "writingFocus": "culmination response",
 "dol": dol("by the end of their stories each character we read about had grown in ways that surprised even themselves",
   C("B") + "y the end of their stories" + C(",") + " each character we read about had grown in ways that surprised even themselves" + C("."),
   "By starts the sentence. A comma comes after the opening part.",
   "after his talk with aslan edmund said he was sorry",
   C("A") + "fter his talk with " + C("A") + "slan" + C(",") + " " + C("E") + "dmund said he was sorry" + C("."),
   "After starts the sentence. Aslan and Edmund are names. A comma comes after the opening part."),
 "hints": {
  "mfill1": {"h1": "Say the two parts out loud, then push them together.", "why": "honest + y = honesty."},
  "mfill2": {"h1": "Say re, then spect, then push them together.", "why": "re + spect = respect."},
  "mfill3": {"h1": "Keep the e in courage before -ous.", "why": "courage + ous = courageous."},
  "mfill4": {"h1": "The silent e at the end of persevere drops before -ance.", "why": "persevere + ance = perseverance."}},
 "flags": {"journal-q1": {"quote": False, "count": 1}, "journal-q2": {"quote": False, "count": 1}, "journal-q3": {"quote": False, "count": 1}},
 "wordgame": dict(GAME, look=LOOK[3], stepTitle="Which spelling rule?", bins=[], items=[
   it_rule(0, "hoping", "hope", "e"), it_rule(1, "hopping", "hop", "d"), it_rule(2, "cried", "cry", "y"), it_rule(3, "boxes", "box", "es"),
   it_rule(4, "making", "make", "e"), it_rule(5, "running", "run", "d"), it_rule(6, "ponies", "pony", "y"), it_rule(7, "wishes", "wish", "es")]),
 "glossary": GLOSS, "sayWords": [],
 "cards": [note("Knights and Courtesy", [
   "The word <i>courtesy</i> comes from the word <i>court</i>, the place where a king or queen lived. Long ago, people at court were expected to have good manners.",
   "Old stories about knights say a good knight was brave and polite: he bowed, kept his promises, and helped people in need.",
   "Despereaux learned to say &ldquo;I honor you&rdquo; from a book of stories like these. That is courtesy, knight style."],
   "A real thing behind one of our books"), AWARDS],
 "transcripts": {"welcome": "Hi, it's Opti. Today you make your writing stronger, and you get to give out some awards.",
  "guide1": "Word work: build words, fix a sentence out loud, and find spelling mistakes.",
  "guide2": "Revise your opening and one paragraph. Write your closing. Then give out the Bookshelf Awards.",
  "guide3": "Write your notes for sharing out loud."},
 "notes": dict(NOTES_COMMON, wgrd="A strong closing says your claim in a new way and tells what the character teaches us about good character.", vocab=VOC)
}
L["32-4"] = {
 "connector": "You read four whole books this year. Today you share what you wrote, look back down the Reading Road, and get a certificate from me.",
 "writingFocus": "culmination response",
 "dol": dol("the four novels we read this year taught us about courage honesty perseverance and what it means to grow up",
   C("T") + "he four novels we read this year taught us about courage" + C(",") + " honesty" + C(",") + " perseverance" + C(",") + " and what it means to grow up" + C("."),
   "The starts the sentence. Commas go between things in a list.",
   "this year we met a flat boy a brave mouse a whipping boy and four children in narnia",
   C("T") + "his year we met a flat boy" + C(",") + " a brave mouse" + C(",") + " a whipping boy" + C(",") + " and four children in " + C("N") + "arnia" + C("."),
   "This starts the sentence. Commas go between things in a list. Narnia is a name."),
 "hints": {},
 "flags": {"journal-q1": {"quote": False, "count": 2}, "journal-q2": {"quote": False, "count": 1}, "journal-q3": {"quote": False, "count": 1}},
 "wordgame": dict(GAME, look=LOOK[4], stepTitle="Which spelling rule?", bins=[], items=[
   it_rule(0, "baking", "bake", "e"), it_rule(1, "swimming", "swim", "d"), it_rule(2, "tried", "try", "y"), it_rule(3, "glasses", "glass", "es"),
   it_rule(4, "riding", "ride", "e"), it_rule(5, "skipped", "skip", "d"), it_rule(6, "pennies", "penny", "y"), it_rule(7, "buses", "bus", "es")]),
 "glossary": GLOSS, "sayWords": [],
 "cards": [note("The Real Wardrobe", [
   "In <i>The Lion, the Witch and the Wardrobe</i>, the way into Narnia is a wardrobe.",
   "C.S. Lewis really grew up with a big wooden wardrobe. His grandfather, Richard Lewis, made it by hand in the 1800s. It stood in the family&rsquo;s house in Belfast, and later in Lewis&rsquo;s home in England.",
   "Today it is in a museum at Wheaton College, in Illinois. Some people think it helped give Lewis the idea for the wardrobe in Narnia."],
   "A real thing behind one of our books"), LOOKBACK, CERT],
 "transcripts": {"welcome": "Hi, it's Opti. Last day! Share your writing, look back at the year, and get your certificate.",
  "guide1": "Word work: roll word-part words, one last editing pass, and roll spelling words.",
  "guide2": "Finish your response, look back down the Reading Road, and write to a new 3rd grader.",
  "guide3": "Give your response a title and share it out loud. Then get your certificate."},
 "notes": dict(NOTES_COMMON, wgrd="Good readers look back at how they have grown. Name one skill that was hard in the fall and is easy for you now.", vocab=VOC)
}
if __name__ == '__main__':
    import sys
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from plates_wk32 import PLATES as P
    for k, p in P.items(): L[k]["plate"] = p
    for k, v in L.items():
        io.open(os.path.join(OUT, 'lesson-%s.json' % k), 'w', encoding='utf-8').write(json.dumps(v, ensure_ascii=False, indent=1)); print(k)
