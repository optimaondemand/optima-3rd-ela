#!/usr/bin/env python3
"""Week 19 (The Whipping Boy, Ch. 6-11): the Nov 10 2026 pilot fixes, as on week 18.
Writes DATA.teach (Opti teaches before each activity; turns on one-step + Start here),
plate.lookBtn (notice first, reveal after) and DATA.virtue (Courage Watch, Nov 12)
into data/lesson-19-N.json AND the page's oao-data block.
Scripts use only what is on the page; book quotes checked against
Planning docs/whipping_boy_ocr.txt (that edition prints "!" for "?").

    python tools/g3sparkle/teach_wk19.py
"""
import io, json, re

GRAM_FOLD = [":scope > .callout:not(:has(+ .spotter-game)):not(:has(+ .fillin-game)):not(:has(+ .sort-game)):not(:has(+ .dol-check-btn))"]
WGRD = {"id": "wgrd", "find": "What Good Readers", "fold": [":scope > p:not(.g3-do)", ":scope > .key-concept", ":scope > .socratic-box"],
        "todo": "Listen to Opti. Then tap the lens you will use today."}
VOCAB_FOLD = [":scope > .g3-model-h", ":scope > .decode-steps"]
SPELL_FOLDTEXT = ["^\\s*👂", "^\\s*This week:", "The Rule:", "Remember: it.s always at the END", "^\\s*Sort and explain"]
WRITE = {"id": "write", "find": "Writer.s Workshop", "fold": [":scope > .callout"], "foldText": ["watch how", "today.s tool"]}
DOL_TODO = "Tap the yellow parts. Then pick Sentence A or B and type it the right way."
CHQ_TODO = "Pick Explorer or Scholar. Answer the three questions in full sentences."
VTITLE = "Courage Watch: Did they show courage?"

L = {
1: {"lookBtn": "Tap to learn about this forest hut painting", "mods": [
 dict(WGRD, script="[warmly] Here's today's reading tip. Good readers ask why characters do what they do. In Chapters 6 and 7, the outlaws take the boys to their hideout in the forest. Ask yourself: what does Jemmy want right now? And what does the prince want? Below are two lenses. Tap the one you will use while you read. You don't need to write anything."),
 {"id": "dol", "find": "Daily Oral", "fold": [], "todo": DOL_TODO,
  "script": "Let's fix a sentence. Look at the correct one first. Billy is talking, so his words go inside quotation marks. There's has an apostrophe, because it's short for there is. Your Young Majesty gets capital letters, because it's a title, like a name. And a comma goes before the closing quotation mark, because the sentence keeps going: he said, chuckling. Tap the yellow parts to see each rule. Then pick Sentence A or Sentence B, and type it the right way."},
 {"id": "morph", "find": "Morphology", "fold": [":scope > .callout:not(:has(+ .fillin-game)):not(:has(+ .dol-check-btn))"],
  "todo": "Say the four words. Tap See if you cracked it. Then type the missing root in each box and tap Check My Work.",
  "script": "Let's crack a word part. Here are four words: transport, import, export, report. Say them out loud. What part do all four words share? Now think about each word. In every one, something is being moved from one place to another. So what do you think that shared part means? Think of your answer. Then tap See if you cracked it to check. After that, type the missing root in each box, and tap Check My Work."},
 {"id": "vocab", "find": "Vocabulary", "fold": VOCAB_FOLD, "todo": "Listen to each card. Guess the meaning, then flip the card. Then play the matching game.",
  "script": "Let's be word detectives. Here's scheme. Read the sentence: A scheme had leaped into his head. Jemmy just thought of something, all of a sudden. Scheme has no prefix or suffix, so the sentence does the work. Something that leaps into your head when you're in trouble is probably a plan. A scheme is a clever plan, often a sneaky one. Now tap Opti reads it on each card. Guess the meaning, then flip the card to check. Then play the matching game."},
 {"id": "gram", "find": "Grammar", "fold": GRAM_FOLD, "todo": "Tap Now check your thinking. Then sort each word group. Last, answer the question in the box.",
  "script": "This week's sentences are compound sentences. A compound sentence is two complete thoughts, glued together with a comma and a joining word, like and, but, or so. Read the sentence from the book in the box. Could each half stand alone as its own sentence? Think about it, then tap Now check your thinking. Next, sort the word groups. Some are one thought. Some are two thoughts joined. And some are not sentences at all, because they leave you hanging. Tap a word group, then tap its column."},
 {"id": "spell", "find": "Spelling", "fold": [], "todo": "Say the words in Group A and B. Tap See the Rule. Then sort the eight words.",
  "script": "Say these words out loud: table, little, candle, simple. Listen to the last beat of each word. Now look at the last three letters, and look where the dot goes. What do you notice? Tap See the Rule to check your idea. Then tap each of the eight words, and tap the group it belongs in. Watch out! Not every word ends the same way."},
 {"id": "copia", "sel": ".spk-copia-card", "label": "Opti shows you how", "fold": [], "todo": "Write Billy’s sentence three new ways, one box at a time.",
  "script": "[warmly] Remember copia? It means saying one idea in many ways. Watch me try one first, with a different sentence. Jemmy ate the bread. Box one, change the opener: In the gloomy hut, Jemmy ate the bread. Box two, swap the verb for a stronger one: Jemmy gobbled the bread. Box three, add a detail: Jemmy ate the stale bread with a herring on top. Same idea, three new ways. Now it's your turn with Billy's sentence, one box at a time. If you get stuck, tap Show one way."},
 {"id": "spotlight", "find": "Character Spotlight", "fold": [":scope > .socratic-box"],
  "script": "Here's something to think about. In Chapter 7, the outlaws want the prince to write a note to the king. But the prince can't write, and Jemmy can. So Jemmy offers to write it. Is he being kind to the prince? Or does he have a plan of his own? From the outside, helping someone and using someone can look the same. Watch what Jemmy really wants."},
 {"id": "read", "find": "^\\s*\\S*\\s*Read:", "fold": [], "todo": "Read the two questions. Then read Ch. 6–7 in your book.",
  "script": "Time to read Chapters 6 and 7 in your book. First, read the two Pause and Think questions below, so you know where to stop. In Chapter 6, the outlaws open the prince's basket and find something that makes them very excited. In Chapter 7, the outlaws need someone to write a note to the king. Watch who can write and who can't, and what the outlaws decide because of it. Stop at each question, think of your answer, and keep reading."},
 {"id": "chq", "find": "Chapter Thinking", "fold": [], "todo": CHQ_TODO,
  "script": "Now show what you understood. Answer in full sentences, with details from the book. One, what valuable thing do the outlaws find in the basket, and why are they so excited? Two, the prince can't write his own name. How does that give Jemmy power, for once? Three, what scheme leaps into Jemmy's head? Want a challenge? Pick Scholar, and add one more detail to each answer."},
 dict(WRITE, todo="Write one sentence: Some people might think ___, but I believe ___ because ___.",
  script="Strong writers think about the other side. That means, what would someone who disagrees with you say? Listen to Clara. Her opinion is, Prince Brat is the most unfair character. Then she thought, someone might say Jemmy is more unfair, because he tricked the outlaws. But she still thinks she's right, because Prince Brat started everything by running away. Now you try. Write one sentence. Start with, Some people might think. Then add, but I believe, and tell why."),
], "cards": {
 "scheme": "Scheme. A scheme had leaped into his head. A scheme is a clever plan, often a sneaky one. Jemmy has a plan to trick the outlaws.",
 "ransom": "Ransom. The outlaws want the king to pay gold to get his son back. That gold is a ransom. A ransom is money people demand before they will set a prisoner free.",
 "flummox": "Flummox. I'm thinking these lads have mixed themselves up to flummox us. To flummox someone means to confuse them completely.",
 "amiss": "Amiss. Something's amiss here. Amiss means wrong, not the way it should be. Billy can tell something doesn't add up."},
 "virtue": [
  {"t": "The outlaws take the prince’s basket. He cries, “That’s mine!”", "ok": False, "why": "Shouting about your things is not courage."},
  {"t": "Jemmy takes the hawk’s feather and offers to write the outlaws’ note himself.", "ok": True, "why": "He is in danger, but he steps up with a plan. That takes courage."},
  {"t": "The outlaws decide Jemmy is the prince, and Jemmy plays along.", "ok": True, "why": "If the outlaws find out, he will be in big trouble. He does it anyway."}]},
2: {"lookBtn": "Tap to learn about this old painting of a writer", "mods": [
 dict(WGRD, script="[warmly] Here's today's reading tip. Good readers notice when a character does something they didn't expect. Today, watch for a moment when Jemmy does something kind for the prince, even though the prince has not been kind to him. Then tap one of the two lenses below, and use it while you read. You don't need to write anything."),
 {"id": "dol", "find": "Daily Oral", "fold": [], "todo": DOL_TODO,
  "script": "Let's fix a sentence. Look at the correct one first. Billy is giving an order, so his words go inside quotation marks, and a comma goes before the closing quotation mark. Hold-Your-Nose Billy is his name, so every part of it gets a capital letter, even with the little dashes in between. Tap the yellow parts to see each rule. Then pick Sentence A or Sentence B, and type it the right way."},
 {"id": "poem", "find": "Poetry", "fold": [":scope > .callout", ":scope > .socratic-box"], "todo": "Read the two haiku out loud. Clap the beats: 5, then 7, then 5. Find where each one changes.",
  "script": "Here are two haiku about a cold morning. Remember, a haiku has three lines. Five beats, then seven, then five. Read both out loud, and clap the beats in each line. Five, steps, to, the, gate. That's five! Then look at the last line of each haiku. A haiku often saves its surprise for the end. Find the word where each one changes direction."},
 {"id": "morph", "find": "Morphology", "fold": [":scope > .callout:not(:has(+ .match-game))", ":scope > .key-concept"], "todo": "Tap a word, then tap what it means. Match all four words.",
  "script": "Remember the root port? It means carry. Now look at the part in front of it. Trans means across. Im means in. Ex means out. And able at the end means you can do it. Put the parts together, and you'll know each word. Tap a word, then tap what it means. Match all four words."},
 {"id": "vocab", "find": "Vocabulary", "fold": VOCAB_FOLD, "todo": "Listen to each card. Guess the meaning, then flip the card. Then play the matching game.",
  "script": "Let's be word detectives. Here's obliged. Read the sentence: He'll be ever so much obliged to know you're safe and hearty. Billy is talking about the king, the prince's father. Now look at the parts: oblige, plus e d. To oblige someone is to do them a favor. So obliged means thankful for a favor. Billy doesn't really care, though. He just wants the gold! Now tap Opti reads it on each card. Guess the meaning, then flip the card to check. Then play the matching game."},
 {"id": "gram", "find": "Grammar", "fold": GRAM_FOLD, "todo": "Tap Now check your thinking. Then tap the two complete thoughts in each sentence. Skip the joining word.",
  "script": "Today you'll take compound sentences apart. Remember, a compound sentence is two complete thoughts glued together with a joining word, like and, but, or so. Look at the sentence in the box, and tap Now check your thinking. Then, in each sentence below, tap the first complete thought, and then the second one. Don't tap the joining word. It's the glue, not part of either thought. Last, answer the question in the box."},
 {"id": "spell", "find": "Spelling", "fold": [":scope > .socratic-box"], "foldText": SPELL_FOLDTEXT, "todo": "In each row, tap the one word that ends in a consonant-le syllable.",
  "script": "Remember consonant l e? A word like table ends with a consonant plus l, e, and those three letters make the last beat together. Ta, ble. In each row, only one word ends that way. Say every word out loud, and listen to the last beat. Then tap the word that ends in a consonant l e syllable."},
 {"id": "spotlight", "find": "Character Spotlight", "fold": [":scope > .socratic-box"],
  "script": "Think about this before you read. Jemmy is writing the ransom note, and the outlaws think he is the prince. The real prince has to sit and watch. Jemmy's plan could set the prince free. It could also get Jemmy rid of the prince for good. Can helping someone and using someone look the same? Watch what Jemmy does, and think about why."},
 {"id": "backward", "sel": "#g3card-backward", "fold": [],
  "script": "Here's Billy's test from Chapter 9. Billy makes Jemmy read the ransom note backward, from the last word to the first. Now you try it! Each note below is written backward. Read it out loud, starting with the last word. Then tap the words in the right order to fix it. Last, answer the question. Why does Billy want the note read backward?"},
 {"id": "read", "find": "^\\s*\\S*\\s*Read:", "fold": [], "todo": "Read the two questions. Then read Ch. 8–9 in your book.",
  "script": "Time to read Chapters 8 and 9 in your book. First, read the two Pause and Think questions below. In Chapter 8, Jemmy writes the ransom note. Billy wants to ask the king for the prince's weight in gold. Watch what Jemmy asks for instead, and why. In Chapter 9, Billy gives Jemmy a tricky test. Stop at each question, think of your answer, and keep reading. Then do the Read Like a Writer box, and try Read It Backward."},
 {"id": "rwm", "sel": ".rwm-box", "after": ":scope > .rwm-header", "label": "Opti shows you how", "fold": [], "script": "[warmly] Read Like a Writer has three parts. Let me show you with a different sentence from Chapter 9. Cutwater yanked Jemmy to his feet. Part one, read like a reader. What is happening? Cutwater is angry, so he pulls Jemmy up, hard. Part two, read like a writer. Which word does the work? Yanked. The author could have said pulled, but yanked is stronger, so we feel how rough Cutwater is. Part three, mimic. Now I write my own: My little brother yanked the blanket off my bed. Now it's your turn with the prince's sentence. Write one sentence in each box."},
 {"id": "chq", "find": "Chapter Thinking", "fold": [], "todo": CHQ_TODO,
  "script": "Now answer in full sentences, with details from the book. One, how does Jemmy get the outlaws to let him write the ransom note? Two, Jemmy signs the note Prince Horace, not Prince Brat. Why use the real name? Think about who will read the note. Three, at the end of Chapter 9, how does Jemmy say the note should get to the castle? And who would really go free? For a challenge, pick Scholar, and add one more detail to each answer."},
 dict(WRITE, todo="Read your writing out loud. Write one sentence again with a transition word, like For example.",
  script="Today, read your opinion out loud, like a real writer. Your ears catch things your eyes miss. Clara read hers out loud. She noticed that her sentences all started with He. She also noticed her example needed a transition word in front of it. Transition words help a reader follow you, like One reason is, Another reason is, and For example. Read your writing out loud. Then pick one sentence and write it again with a transition word."),
], "cards": {
 "obliged": "Obliged. He'll be ever so much obliged to know you're safe and hearty. Obliged means thankful for a favor.",
 "scoundrel": "Scoundrel. Our captors are loyal subjects, but scoundrels by trade. A scoundrel is a dishonest, wicked person. Jemmy writes this about the outlaws, right in front of them!",
 "gallows": "Gallows. Warn him we fear no gallows! A gallows is a wooden frame that was used long ago to punish criminals. Billy is bragging that he is not afraid.",
 "scribblement": "Scribblement. But how are we going to do the scribblement? We can't write. Scribblement is Cutwater's own word for writing. He makes it up because he can't write."},
 "virtue": [
  {"t": "Jemmy tells the outlaws a prince is worth a whole wagonload of gold.", "ok": True, "why": "He talks back to two outlaws to make his trick work. That is brave."},
  {"t": "The prince hears he might get whipped, so he calls the outlaw “sir.”", "ok": False, "why": "He is only trying to save himself."},
  {"t": "Billy makes Jemmy read the note backward. Jemmy stays calm and reads it all.", "ok": True, "why": "One slip could ruin his plan. He keeps calm and does it."}]},
3: {"lookBtn": "Tap to learn about this horse painting", "mods": [
 dict(WGRD, script="[warmly] Here's today's reading tip. Good readers notice when a character changes, even a little. In Chapter 11, the prince makes a choice that surprises Jemmy. Watch for it, and ask yourself: why would he choose that? Then tap one of the two lenses below to use while you read. You don't need to write anything."),
 {"id": "dol", "find": "Daily Oral", "fold": [], "todo": DOL_TODO,
  "script": "Let's fix a sentence. Today's model is short: Jemmy was struck dumb. That means he was so surprised he couldn't speak. Nobody is talking in this sentence. The storyteller is telling us what happened, so there are no quotation marks. It needs a capital letter at the start and a period at the end. Tap the yellow parts to see each rule. Then pick Sentence A or Sentence B, and type it the right way."},
 {"id": "morph", "find": "Morphology", "fold": [":scope > .callout:not(:has(+ .fillin-game))", ":scope > .key-concept"], "todo": "Say the parts out loud. Type the whole word in each box. Tap Check My Answers.",
  "script": "Let's build words with port. Remember, port means carry. Say each pair of parts out loud, then push them together into one word. Trans, port. Transport! Hear how the parts snap together? Type the whole word in each box. Then tap Check My Answers. The meaning next to each word tells you what you built."},
 {"id": "vocab", "find": "Vocabulary", "fold": VOCAB_FOLD, "todo": "Fill in each sentence with a word from the word bank. Tap Check My Work. Then play the matching game.",
  "script": "Here's a funny word from Chapter 11: mulishness. Cutwater shouts, I'll whip the mulishness out of him! Look at the parts. Mule, ish, ness. A mule is an animal famous for being stubborn. Ish means like. And ness turns it into a thing. So mulishness means being stubborn, like a mule. Now the other words. Defiant means boldly refusing to obey. A parley is a private talk to work something out. And contrary means always doing the opposite. Fill in each sentence from the word bank, and tap Check My Work. Then play the matching game."},
 {"id": "gram", "find": "Grammar", "fold": GRAM_FOLD, "todo": "Tap Now check your thinking. Type the word the comma goes after. Tap Check My Answers. Then write your own.",
  "script": "Today you're the comma finder. Look at the sentence in the box. Where is the comma? Tap Now check your thinking. In a compound sentence, the comma goes right before the joining word. The sentences below have lost their commas. Find the end of the first complete thought. That's the word just before and, but, or so. Type that word, and tap Check My Answers. Last, write your own compound sentence."},
 {"id": "spell", "find": "Spelling", "fold": [":scope > .socratic-box"], "foldText": SPELL_FOLDTEXT, "todo": "Tap the word parts in order to build each word.",
  "script": "Let's build consonant l e words. Remember, the consonant always stays with the l, e. Can, dle. Candle. Each word is cut into tiles. Say each part out loud, and tap the tiles in order to build the word. If a tile is in the wrong place, it won't stick, so just try the other one."},
 {"id": "spotlight", "find": "Character Spotlight", "fold": [":scope > .socratic-box"],
  "script": "Think about the prince today. He gets a chance to go home, and he says no. Jemmy can't understand it. Is the prince just being a brat again? Or is something else going on inside him? Watch closely. Sometimes people do things for reasons they don't say out loud."},
 {"id": "read", "find": "^\\s*\\S*\\s*Read:", "fold": [], "todo": "Read the two questions. Then read Ch. 10–11 in your book.",
  "script": "Time to read Chapters 10 and 11 in your book. First, read the two Pause and Think questions below. Remember, the outlaws think the real prince is the whipping boy! In Chapter 10, they decide to send him to the castle with the note. Watch what the prince says. In Chapter 11, Billy pulls off his belt. Watch what Jemmy does. Stop at each question, think of your answer, and keep reading. After you read, do the Read Like a Writer box."},
 {"id": "chq", "find": "Chapter Thinking", "fold": [], "todo": CHQ_TODO,
  "script": "Now answer in full sentences, with details from the book. One, Chapter 11 asks if the prince has sand for brains. What does the prince do that makes Jemmy think that? Two, why might the prince not want to go home? Look at what he says about his father. Three, when the outlaws step outside, what do Jemmy and the prince argue about, and what does the prince decide? For a challenge, pick Scholar, and add one more detail to each answer."},
 dict(WRITE, todo="Write one conclusion sentence. Say your big idea in a new way.",
  script="Every opinion needs an ending. It's called a conclusion. A good conclusion doesn't just repeat your first sentence. It says your big idea in a fresh way, and it gives your reader something to think about. Listen to the end of Clara's: A true prince would learn to use his power to protect, not to punish. Doesn't that sound like an ending? Now write a conclusion sentence for your own paragraph. Don't copy your first sentence word for word."),
], "cards": {},
 "virtue": [
  {"t": "The prince tosses away his herring and shows no care for what happens to Jemmy.", "ok": False, "why": "Not caring about someone in danger is not courage."},
  {"t": "Jemmy keeps up his trick so the outlaws will send the prince home.", "ok": True, "why": "He could be caught any minute, but he keeps trying to help."},
  {"t": "Billy grabs his belt to whip the prince. Jemmy speaks up with a new idea: send the horse.", "ok": True, "why": "He speaks up to two angry outlaws to stop a whipping. That takes courage."}]},
4: {"lookBtn": "Tap to learn about this golden crown painting", "mods": [
 dict(WGRD, script="[warmly] There are no new chapters today. Instead, good readers look back at everything they've read so far. Think about Jemmy and the prince in Chapter 1, back at the castle. Now think about them in the outlaws' hut. How has each boy changed? Then tap one of the two lenses below to use while you look back. You don't need to write anything."),
 {"id": "dol", "find": "Daily Oral", "fold": [], "todo": DOL_TODO,
  "script": "Let's fix a sentence. Look at the correct one first. The prince is talking, so his words go inside quotation marks. Doesn't has an apostrophe, because it's short for does not. And a comma goes before the closing quotation mark, because the sentence keeps going: Prince Brat said coldly. Tap the yellow parts to see each rule. Then pick Sentence A or Sentence B, and type it the right way. Watch out, the sentence you fix needs two apostrophes!"},
 {"id": "poem", "find": "Poetry", "fold": [":scope > .callout", ":scope > .socratic-box"], "todo": "Make up a haiku about something outside your window. Count 5, 7, 5. Say it out loud.",
  "script": "Here are the two cold-morning haiku again. Today, you'll make up your own. Look out your window. What do you see? A bird, a car, the rain, a tree? Make up three lines about it, and count the beats on your fingers. Five, then seven, then five. Try to save a little surprise for the last line. Say your haiku out loud. You don't need to write it."},
 {"id": "morph", "find": "Morphology", "fold": [":scope > .key-concept"], "foldText": ["Before you roll"], "todo": "Tap Roll the Dice. Say what the word means. Tap Check My Thinking. Roll all six words.",
  "script": "Let's roll some port words. Before you roll, say it out loud: port means carry. Tap Roll the Dice. When a word comes up, look at the part in front of port, and say what the whole word means. Then tap Check My Thinking to see if you were right. Keep rolling until you've done all six words."},
 {"id": "vocab", "find": "Vocabulary", "fold": VOCAB_FOLD, "todo": "Fill in each sentence with a word from the word bank. Tap Check My Work. Then play the matching game.",
  "script": "Let's review four words. Start with fathom. He couldn't fathom what was stirring in the prince's mind. Jemmy can't figure out what the prince is thinking. Long ago, sailors used a fathom to measure how deep the water was. So to fathom something is to get to the bottom of it, to understand it. Now the others. Flummox means to confuse someone completely. A parley is a private talk. And angling means trying to get something in a sneaky way, like fishing for it. Fill in each sentence from the word bank, and tap Check My Work."},
 {"id": "gram", "find": "Grammar", "fold": GRAM_FOLD, "todo": "Tap the word where the mistake is, or tap No mistake. Then tap See the answers and answer the question in the box.",
  "script": "Today you're the teacher, checking compound sentences. Remember: two complete thoughts, a comma, and then the joining word. Look at the sentence in the box, and tap Now check your thinking. Then read each sentence below out loud. Look at the comma and the joining word together. If you find a mistake, tap the word where it is. If the sentence is right, tap No mistake. Then tap See the answers, and answer the question in the box."},
 {"id": "spell", "find": "Spelling", "fold": [":scope > .socratic-box", ":scope > .dol-check-btn", "#spellRuleReveal"], "foldText": SPELL_FOLDTEXT, "todo": "Tap Roll the dice. Say the word and split it. Tap Check my answer. Roll all six words.",
  "script": "Let's roll some consonant l e words. Tap Roll the dice. Say the word out loud and clap its beats. Then split it. Remember, count back three letters from the end, and that's your last syllable. Bub, ble. Then tap Check my answer. Keep rolling until you've done all six words."},
 {"id": "spotlight", "find": "Character Spotlight", "fold": [":scope > .socratic-box"],
  "script": "Look back at the whole week. Jemmy wrote the ransom note, played the prince, and tricked two outlaws. Was he helping the prince, or helping himself? Maybe both! Now think about the prince. He could have gone home, and he said no. What do you think he really wants?"},
 {"id": "read", "find": "Look Back", "fold": [], "todo": "Read the two questions. Then look back through Ch. 6–11 in your book.",
  "script": "There are no new chapters today. Instead, look back through Chapters 6 to 11 in your book. First, read the two Pause and Think questions below. One is about something Jemmy says to the prince: It's not me you think you're protecting, is it? The other asks if the prince has really changed. Flip back through the pages to find clues. Then do the Read Like a Writer box."},
 {"id": "chq", "find": "Chapter Thinking", "fold": [], "todo": CHQ_TODO,
  "script": "Now look back and answer in full sentences, with details from the book. One, Jemmy signs the note as the prince. How does that help him, and how could it hurt him? Two, describe one moment in Chapter 11 when the prince does something unexpected. Three, who is cleverer in Chapters 6 to 11, Jemmy or the prince? Give one example for each boy. For a challenge, pick Scholar, and add one more detail to each answer."},
 dict(WRITE, todo="Write your paragraph with all five parts: claim, reason, example, the other side, and conclusion.",
  script="Today you put it all together. Clara had five pieces: her claim, a reason, an example, the other side, and a conclusion. Then she put them in order to make one paragraph. Read hers and listen to how it flows. It starts with her claim, gives a reason, proves it with an example from Chapter 2, answers the other side, and ends with a conclusion. Now write your own paragraph in the box, with all five parts. Use your work from this week to help."),
], "cards": {},
 "virtue": [
  {"t": "Jemmy writes the ransom note and signs it with the prince’s name.", "ok": True, "why": "He takes a big risk to trick the outlaws."},
  {"t": "The prince gobbles an apple tart and says he will go back “when I choose.”", "ok": False, "why": "Doing what he wants is not the same as courage."},
  {"t": "Billy pulls off his belt. Jemmy speaks up with the horse idea.", "ok": True, "why": "He is scared, but he speaks up to stop it."}]},
}

# Opti videos (Nov 13 2026 pilot): Day 1 Word Study + Day 2 Read Like a Writer.
# Same recorded clip as the button; film in assets/video/g3ela-19-D-teach-<id>.mp4 (+ .jpg).
# Days 2-4 Word Study scripts rewritten for the videos (Bethany, Nov 13 2026):
# short, show that day's activity with a non-answer example, never re-teach Day 1.
# "+how:" marks a shared direction clip joined on the end (only the part before it is recorded).
WS2 = {
 2: {"morph": "Watch this. Support. Find port at the end. Now look at the part in front: sup, which means under. So to support something is to carry it from underneath, like holding up a heavy box. Use the same trick on each word. Tap a word, then tap what it means.",
     "vocab": "Here's a word Billy uses: obliged. He tells the prince his father will be ever so much obliged. Billy is pretending to be polite. Obliged means thankful. The cards work just like last time: listen, guess, then flip. Then match all four.",
     "gram": "Here's one to take apart. The fog rolled in, and the boys got lost. First thought: the fog rolled in. Second thought: the boys got lost. The word and is just the glue, so skip it. In each sentence, tap the first thought, then the second.",
     "spell": "Quick test. Cattle, kitten, carpet. Which one ends with a consonant and l, e? Say them. Cat, tle. That's the one. In each row, only one word ends that way. Say every word, listen to the last beat, and tap it."},
 3: {"morph": "Let's build a silly one first. Tele means far. Tele, plus port. Teleport! To carry something far away in a flash. Now you build the real ones. Say each pair of parts out loud. Type the whole word in the box. Then tap Check My Answers.",
     "vocab": "Cutwater shouts, I'll whip the mulishness out of him! Mule, ish, ness: stubborn like a mule. Defiant, parley and contrary are in the word bank too. Read each sentence, try each word in the blank, and keep the one that makes sense. Then tap Check My Work.",
     "gram": "These sentences lost their commas. Listen. The horse was fast, but the outlaws were faster. Hear the little pause after fast? The comma goes there, right before but. Find that spot in each sentence and type the word that comes just before it.",
     "spell": "Two tiles, one word. Pud, dle. Puddle! The d sticks with the l, e. Build each word the same way. Tap the first part, then the last part. If a tile is in the wrong spot, it won't stick, so try the other one."},
 4: {"morph": "Roll it, then crack it. Every word on the dice has port in it, so you already know half the meaning. Look at the part in front of port. That part is your clue. Say what the whole word means out loud, then tap Check My Thinking. Do all six.",
     "vocab": "Last chance with this week's words: fathom, flummox, parley, and angling. Here's a trick. Read each sentence out loud with the word in the blank. If it sounds right and makes sense, keep it. Then tap Check My Work.",
     "gram": "Can you spot what's wrong? The fog was thick but, they kept going. The comma jumped to the wrong side of but! It belongs right before it. Read each sentence. Tap the word where the mistake is, or tap No mistake if it's right.",
     "spell": "Here's how to split one. Bottle. Count back three letters from the end: t, l, e. Bot, tle. That's the split. Tap Roll the dice. Say the word out loud and split it into syllables. Then tap Check my answer. Roll all six words."},
}
# shared direction clip joined on the end (clip-log: same voice, same words)
SPLICE = {(3, 'morph'): 'g3ela-how-morph3', (4, 'spell'): 'g3ela-how-spell4'}
for d, scr in WS2.items():
    for m in L[d]['mods']:
        if m['id'] in scr: m['script'] = scr[m['id']]
VIDEO = {1: ['morph', 'vocab', 'gram', 'spell'], 2: ['morph', 'vocab', 'gram', 'spell', 'rwm'],
         3: ['morph', 'vocab', 'gram', 'spell'], 4: ['morph', 'vocab', 'gram', 'spell']}
for d, ids in VIDEO.items():
    for m in L[d]['mods']:
        if m['id'] in ids: m['video'] = 'g3ela-19-%d-teach-%s' % (d, m['id'])

def write_page(f, D):
    html = io.open(f, encoding='utf-8', newline='').read()
    m = re.search(r'(<script type="application/json" id="oao-data">)(.*?)(</script>)', html, re.S)
    old = m.group(2)
    if '\n' not in old.strip(): body = json.dumps(D, ensure_ascii=False, separators=(',', ':'))
    else: body = json.dumps(D, ensure_ascii=False, indent=1)
    body = body.replace('</script', '<\\/script')
    lead = old[:len(old) - len(old.lstrip())]; tail = old[len(old.rstrip()):]
    io.open(f, 'w', encoding='utf-8', newline='').write(html[:m.start(2)] + lead + body + tail + html[m.end(2):])

for d, cfg in L.items():
    p = 'data/lesson-19-%d.json' % d
    j = json.load(io.open(p, encoding='utf-8'))
    j['plate']['lookBtn'] = cfg['lookBtn']
    j['teach'] = {"dropTurnNotes": True, "mods": cfg['mods'], "cards": cfg['cards']}
    j['virtue'] = {"name": "courage", "title": VTITLE, "items": cfg['virtue']}
    io.open(p, 'w', encoding='utf-8').write(json.dumps(j, ensure_ascii=False, indent=1))
    write_page('lesson-19-%d-wb.html' % d, j)
    n = sum(len(re.sub(r'\[[^\]]*\]\s*', '', x.get('script', ''))) for x in cfg['mods']) + sum(len(v) for v in cfg['cards'].values())
    print('19.%d teach credits %d' % (d, n))
