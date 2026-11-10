#!/usr/bin/env python3
"""Opti-teaches DATA for week 18 lessons 18.2-18.4 (18.1 was hand-built).
Writes DATA.teach + plate.lookBtn into data/lesson-18-N.json and the page's
oao-data block. Scripts use only what is on the page (book quotes as printed)."""
import io, json, re

GRAM_FOLD = [":scope > .callout:not(:has(+ .spotter-game)):not(:has(+ .fillin-game)):not(:has(+ .sort-game)):not(:has(+ .dol-check-btn))"]
WGRD = {"id":"wgrd","find":"What Good Readers","fold":[":scope > p:not(.g3-do)",":scope > .key-concept",":scope > .socratic-box"],
        "todo":"Listen to Opti. Keep his question in your head while you read."}
VOCAB_FOLD = [":scope > .g3-model-h",":scope > .decode-steps"]
SPELL_FOLDTEXT = ["^\\s*👂", "^\\s*This week:", "The Rule:"]
WRITE = {"id":"write","find":"Writer.s Workshop","fold":[":scope > .callout"],"foldText":["watch how","today.s tool"]}

L = {
2: {"lookBtn":"Tap to learn about this foggy forest painting", "mods":[
 dict(WGRD, script="[warmly] Here's today's reading tip. Good readers notice when a character makes a bad choice, and then watch what that choice causes. Today the prince decides to run away, and Jemmy has to go with him. As you read, ask yourself: whose idea was this, and whose fault is the trouble that follows? Keep that question in your head. You don't need to write anything."),
 {"id":"dol","find":"Daily Oral","fold":[],"todo":"Tap the yellow parts. Then pick Sentence A or B and type it the right way.",
  "script":"Let's fix a sentence. Look at the correct one first. The prince is talking, so his words go inside quotation marks. A comma goes before the closing quotation mark, because the sentence keeps going: the prince announced to Jemmy. Tap the yellow parts to see each rule. Then pick Sentence A or Sentence B. Add the quotation marks, the comma, and the capital letters, and type it the right way."},
 {"id":"poem","find":"Poetry","fold":[":scope > .callout",":scope > .socratic-box"],"todo":"Read the three haiku out loud. Clap the beats in the first one: 5, then 7, then 5.",
  "script":"This is a haiku, a tiny poem with a fixed shape. The first line has five beats, the second has seven, and the last has five again. A haiku holds one picture and doesn't explain it. Read all three out loud. Then go back to the first one and clap each beat. Snow, on, the, court, yard. That's five! Keep clapping, and check that you get five, seven, five."},
 {"id":"morph","find":"Morphology","fold":[":scope > .callout:not(:has(+ .match-game))",":scope > .key-concept"],"todo":"Tap a word, then tap what it means. Match all four words.",
  "script":"You already know two word parts. Inter means between, like the internet connecting computers. Sub means under, like a subway under the city. When you see a long word, find the part at the start first, then read the rest. Tap a word in the game, then tap what it means. If you're stuck, look at the first part of the word. It gives you a big clue."},
 {"id":"vocab","find":"Vocabulary","fold":VOCAB_FOLD,"todo":"Listen to each card. Guess the meaning, then flip the card. Then play the matching game.",
  "script":"Let's be word detectives again. Here's astonishment. Read the sentence: Jemmy stared at him with dreadful astonishment. Jemmy just heard something he never expected. Now look at the parts. Astonish means to surprise, and ment turns it into a thing. So astonishment is a feeling of great surprise. Now tap Opti reads it on each card, guess the meaning, and flip the card to check. Then play the matching game."},
 {"id":"gram","find":"Grammar","fold":GRAM_FOLD,"todo":"Tap the joining word, then the part after it. Then write one sentence with a new joining word.",
  "script":"Joining words are back, and today you're a joining-word spotter. Remember: and adds an idea, but shows a difference, and so shows what happens next. In each sentence, first tap the joining word. Then tap the part of the sentence that comes after it. That part is the new idea the joining word brings in. Last, pick one sentence and write it again with a different joining word. Notice how the meaning changes."},
 {"id":"spell","find":"Spelling","fold":[],"foldText":SPELL_FOLDTEXT,"todo":"Tap every word in the two sentences that has a vowel team.",
  "script":"Let's go hunting for vowel teams. A vowel team is two vowels side by side that make one sound, like the o and a in coach, or the e and a in feast. The team always stays together. Read the two sentences slowly. Every time you see two vowels working together, tap that word. There's more than one, so keep looking until the game says you found them all."},
 {"id":"spotlight","find":"Character Spotlight","fold":[":scope > .socratic-box"],
  "script":"Here's something to think about. The prince runs away for one reason: he's bored. Jemmy doesn't get a choice. He has to come along and carry the basket. But out in the fog, there are no guards and no castle walls. Watch Jemmy closely. He may see a chance of his own. Who do you think is really in charge out there?"},
 {"id":"read","find":"^\\s*\\S*\\s*Read:","fold":[],"todo":"Read the two questions. Then read Ch. 3–4 in your book.",
  "script":"Time to read Chapters 3 and 4 in your book. First, read the two Pause and Think questions below, so you know where to stop. In Chapter 3, look for the prince's real reason for running away. In Chapter 4, a thick fog rolls in and two strangers appear. Ask yourself who Jemmy thinks they are, and why he's so scared. Stop at each question, think of your answer, and keep reading."},
 {"id":"chq","find":"Chapter Thinking","fold":[],"todo":"Pick Explorer or Scholar. Answer the three questions in full sentences.",
  "script":"Now show what you understood. Remember, a good answer is a full sentence with a detail from the book. One, what is Jemmy's plan to escape in the fog, and what stops it? Two, when the strangers grab the boys, what does Jemmy think they are, and why is he scared? Three, why does the prince pick Jemmy to run away with? Use a detail from Chapter 3. Want a challenge? Pick Scholar, and add one more detail to each answer."},
 dict(WRITE, todo="Copy your claim from Day 1. Write one reason under it.",
  script="On Day 1 you wrote a claim. Today you'll give it a reason. A reason tells why your claim is true. Listen to Clara. Her claim was, Prince Brat is the most unfair character. Then she added, One reason is that Prince Brat wants Jemmy whipped hard for things the prince did. See how the reason backs up the claim? Copy your claim from Day 1 into the box. Then write one reason under it. You can start with, One reason is that."),
], "cards": {
 "astonishment":"Astonishment. Jemmy stared at him with dreadful astonishment. Astonishment means a feeling of great surprise or shock.",
 "gallows":"Gallows. More likely I'll be hung from the gallows. A gallows is a wooden frame that was used long ago to punish people by hanging. Jemmy is afraid of a terrible punishment.",
 "strayed":"Strayed. A thick fog had swirled in, they'd strayed from the road, and trees had closed in on them. Strayed means wandered off the path by mistake.",
 "cutthroat":"Cutthroat. A cutthroat! he thought. A cutthroat is a dangerous criminal who would do anything for money."}},
3: {"lookBtn":"Tap to learn about this highwayman drawing", "mods":[
 dict(WGRD, script="[warmly] Here's today's reading tip. Good readers notice what a character does when he's in danger. In Chapter 5, two outlaws grab the boys. Watch Jemmy. Does he fight, does he try to trick them, or does he stay quiet? And think about why he makes that choice. You don't need to write anything. Just watch Jemmy closely while you read."),
 {"id":"dol","find":"Daily Oral","fold":[],"todo":"Tap the yellow parts. Then pick Sentence A or B and type it the right way.",
  "script":"Let's fix a sentence about the outlaws. Look at the correct one first. Billy gets a capital letter, because it's a name. Commas go around the describing part in the middle: raw as a skinned ox. And a comma goes before and, because and joins two ideas. Tap the yellow parts to see each rule. Then pick Sentence A or B, and type it with capitals, commas, and a period."},
 {"id":"morph","find":"Morphology","fold":[":scope > .callout:not(:has(+ .fillin-game))",":scope > .key-concept"],"todo":"Type the whole word in each box. Then tap Check My Answers.",
  "script":"Today you'll build words from their parts. Remember, inter means between, and sub means under. Say each pair of parts out loud, then say them together as one word. Inter, rupt: interrupt. Hear how the parts snap together? Type the whole word in each box, then tap Check My Answers. Look at the little meaning next to each one. It tells you what you just built."},
 {"id":"vocab","find":"Vocabulary","fold":VOCAB_FOLD,"todo":"Fill in each sentence with a word from the word bank. Tap Check My Work. Then play the matching game.",
  "script":"Here's a word from Chapter 5: ruffian. The prince calls Billy a clod and a ruffian. He's insulting him, so a ruffian must be someone rough and rude. Ruffian has no parts to help, so the sentence does the work. A ruffian is a rough, violent person, a bully. Now the other words in the word bank. An exploit is a bold, daring act. An heir is the person who will be king one day. And a ransom is money demanded to set a prisoner free. Fill in each sentence, then tap Check My Work."},
 {"id":"gram","find":"Grammar","fold":GRAM_FOLD,"todo":"Type and, but, or so in each blank. Tap Check My Answers. Then write a sentence that uses but.",
  "script":"Today you'll do the joining yourself. Each pair has two short sentences. Glue them into one with and, but, or so. Ask yourself: am I adding an idea? Use and. Are the two ideas different, or surprising? Use but. Does the first thing cause the second? Use so. Read each one out loud with the word you picked. Then tap Check My Answers, and write your own sentence about Chapter 5 that uses but."},
 {"id":"spell","find":"Spelling","fold":[],"foldText":SPELL_FOLDTEXT,"todo":"Find the vowel team in each word. Then tap the word to split it.",
  "script":"Remember vowel teams? Two vowels side by side making one sound. Here's today's rule: when you split a word into syllables, never split the team. The team always stays together. Rain, bow. Sea, son. Look at each word, find the vowel team, and think about where the split goes. Then tap the word to check. The split goes between the syllables, never through the team."},
 {"id":"spotlight","find":"Character Spotlight","fold":[":scope > .socratic-box"],
  "script":"Think about this before you read. When two outlaws grab the boys, the prince keeps telling them who he is. Jemmy tries to stop him without saying a word. Why would Jemmy want the prince to stay quiet? What might happen if outlaws find out they have a prince? Watch who keeps his head, and who keeps talking."},
 {"id":"read","find":"^\\s*\\S*\\s*Read:","fold":[],"todo":"Read the two questions. Then read Ch. 5 in your book.",
  "script":"Time to read Chapter 5. First, read the two Pause and Think questions below. In this chapter, Jemmy jabs the prince with his elbow. Ask yourself why. Then watch the outlaw named Cutwater. He notices something on the saddle that changes everything. Stop at each question, think of your answer, and keep reading. After you read, try the King's Crest to see what Cutwater saw."},
 {"id":"chq","find":"Chapter Thinking","fold":[],"todo":"Pick Explorer or Scholar. Answer the three questions in full sentences.",
  "script":"Now show what you understood, in full sentences with details from the book. One, how does Jemmy know who Hold-Your-Nose Billy is, and what does that tell us about how famous Billy is? Two, when the prince says who he is, the outlaws don't bow. What do they do instead? Three, Jemmy jabbed the prince to keep him quiet. Was that the right thing to do? Use a detail to back up your answer. For a challenge, pick Scholar and add one more detail."},
 dict(WRITE, todo="Write one example from the book. Start with: For example, in Chapter.",
  script="You have a claim and a reason. Today you'll prove your reason with an example from the book. Clara's reason was, Prince Brat enjoys watching Jemmy get whipped. To prove it, she found a real moment. For example, in Chapter 2, the prince tells the tutor, ten whacks at least. Always name the chapter, so your reader can find it. Now write one example of your own. Start with, For example, in Chapter. Then copy it into your document."),
], "cards": {}},
4: {"lookBtn":"Tap to learn about this castle tower painting", "mods":[
 dict(WGRD, script="[warmly] There are no new chapters today. Instead, good readers look back over everything they've read. Think about both boys in Chapters 1 to 5. The prince has velvet clothes and a king for a father. Jemmy has rags, and he gets whipped for the prince's pranks. Which boy has the harder life? Do you feel sorry for either one? Think about why. You don't need to write anything."),
 {"id":"dol","find":"Daily Oral","fold":[],"todo":"Tap the yellow parts. Then pick Sentence A or B and type it the right way.",
  "script":"Let's fix a sentence. Look at the correct one. The prince says one word: Boring. That word goes inside quotation marks, and it starts with a capital letter. A comma comes right before the opening quotation mark, after the word said. And the period goes inside the closing quotation mark. Tap the yellow parts to see each rule. Then pick Sentence A or B, and type it the right way."},
 {"id":"poem","find":"Poetry","fold":[":scope > .callout",":scope > .socratic-box"],"todo":"Pick one haiku. Say out loud the picture it puts in your head.",
  "script":"Here are the three haiku again. Remember, a haiku holds one small picture and doesn't explain it. Today, you get to choose. Read all three out loud, and pick the one you like best. Then close your eyes and see the picture it puts in your head. Is it the snow, the rat with the candles, or the soup that no one eats? Say your picture out loud. You don't need to write it."},
 {"id":"morph","find":"Morphology","fold":[":scope > .key-concept"],"foldText":["Before you roll"],"todo":"Tap Roll the Dice. Say what the word means. Tap Check My Thinking. Roll all six words.",
  "script":"Let's play with inter and sub one more time. Before you roll, say it out loud: inter means between, sub means under. Tap Roll the Dice. When a word comes up, find its first part, and say what the whole word means. Then tap Check My Thinking to see if you were right. Keep rolling until you've done all six words."},
 {"id":"vocab","find":"Vocabulary","fold":VOCAB_FOLD,"todo":"Fill in each sentence with a word from the word bank. Tap Check My Work. Then play the matching game.",
  "script":"This week you met lots of new words. Today you'll use four of them. Let's start with contrite. The prince lowered his head so as to appear humbled and contrite. He's trying to look sorry. So contrite means truly sorry for something you did wrong. Now the others. Astonishment means great surprise. A ruffian is a rough, mean bully. And exasperation is a fed-up feeling that keeps building. Fill in each sentence from the word bank, then tap Check My Work."},
 {"id":"gram","find":"Grammar","fold":GRAM_FOLD,"todo":"Tap the wrong joining word, or tap No mistake. Then answer the question in the box.",
  "script":"Today you're the teacher, checking someone else's work. Some of these sentences use the wrong joining word. Remember: and adds an idea, but shows a difference, and so shows what happens because of something. Read each sentence out loud. If the joining word doesn't match the meaning, tap it. If the sentence is right, tap No mistake. Then tell which sentence had no mistake, and how you knew."},
 {"id":"spell","find":"Spelling","fold":[],"foldText":SPELL_FOLDTEXT,"todo":"Tap Roll the dice. Say the word and split it. Tap Check my answer. Roll all six words.",
  "script":"Let's roll some vowel team words. Tap Roll the dice. When a word comes up, say it out loud and clap the syllables. Find the vowel team, and remember, the team never splits. Meadow: mead, ow. Then tap Check my answer to see if you split it the right way. Keep rolling until you've done all six words."},
 {"id":"spotlight","find":"Character Spotlight","fold":[":scope > .socratic-box"],
  "script":"Think about the two boys side by side. One has velvet clothes, a tutor, and a king for a father. The other has rags and a rat-catcher's know-how. But Jemmy also learned all the lessons the prince never did. Now they're both stuck with the same outlaws. Which boy do you think will be better at getting out of trouble?"},
 {"id":"read","find":"Look Back","fold":[],"todo":"Read the two questions. Then look back through Ch. 1–5 in your book.",
  "script":"There are no new chapters today. Instead, look back through Chapters 1 to 5 in your book. First, read the two Pause and Think questions below. One asks about the biggest conflict: which characters are against each other, and over what? The other asks you to predict. What will the outlaws do with a real prince? Flip back through the pages to find clues. You don't need to write these answers."},
 {"id":"chq","find":"Chapter Thinking","fold":[],"todo":"Pick Explorer or Scholar. Answer the three questions in full sentences.",
  "script":"Now look back and answer in full sentences, with details from the book. One, describe Jemmy's life at the castle. What is good about it, and what is hard? Two, what are two pranks the prince has pulled, and why does no one ever punish him? Three, both boys are captives now. Who is more responsible for that? Use one detail. For a challenge, pick Scholar, and add one more detail to each answer."},
 dict(WRITE, todo="Read your claim, reason and example. Write one thing you will add or fix.",
  script="This week you wrote a claim, a reason, and an example. Today you'll check your work, like a real writer. Clara read her draft and asked three questions. Is my claim clear? Does my reason tell why? Is my example from the book? Then she found one thing to add. Now read your own claim, reason, and example. Ask the same three questions. Then write one thing you'll add or fix to make your opinion stronger."),
], "cards": {}},
}
for d, cfg in L.items():
    p = 'data/lesson-18-%d.json' % d
    j = json.load(io.open(p, encoding='utf-8'))
    j['plate']['lookBtn'] = cfg['lookBtn']
    j['teach'] = {"dropTurnNotes": True, "mods": cfg['mods'], "cards": cfg['cards']}
    io.open(p, 'w', encoding='utf-8').write(json.dumps(j, ensure_ascii=False, indent=1))
    f = 'lesson-18-%d-wb.html' % d
    h = io.open(f, encoding='utf-8').read()
    m = re.search(r'(id="oao-data">\s*)(\{.*?\})(\s*</script>)', h, re.S)
    h = h[:m.start(2)] + json.dumps(j, ensure_ascii=False) + h[m.end(2):]
    io.open(f, 'w', encoding='utf-8').write(h)
    n = sum(len(x.get('script', '')) for x in cfg['mods']) + sum(len(v) for v in cfg['cards'].values())
    print(f, 'teach credits', n)
