#!/usr/bin/env python3
"""Week 18 plain-language pass (Nov 8 2026, Bethany: "direct instruction,
nothing left up to interpretation, valuable words only").

Reads pristine-orig/, writes pristine/ (the build input). Wording only:
same meaning, same answers. Every activity gets one "What to do:" line that
Opti reads (data-say = the clip slug, shared across days when the words are
the same). Re-runnable."""
import io, os, re, sys

SRC, DST = '/home/claude/g3/pristine-orig', '/home/claude/g3/pristine'
DAYS = ['lesson-18-1-wb.html', 'lesson-18-2-wb.html', 'lesson-18-3-wb.html', 'lesson-18-4-wb.html']
FLU = 'lesson-18-fluency.html'

# ── Opti's "What to do" lines: slug -> words (the clip says exactly this) ──
DO = {
 'readers': 'Read the tip. Think about it while you read today. You do not write anything here.',
 'dol':     'Tap the highlighted parts of the correct sentence to see why they are right. Then choose Sentence A or Sentence B, and type it the right way in the box.',
 'poem2':   'Read the three haiku out loud. Then clap the syllables in the first one. You should count 5, then 7, then 5.',
 'poem4':   'Choose one of the three haiku. Say out loud the one picture it puts in your head. You do not need to write it.',
 'morph1':  'Read the four words and their parts. Think about the three questions. Then tap See what each part means. Last, type each whole word and tap Check My Answers.',
 'morph2':  'Read the Remember box. Then tap a word, and tap what it means. Match all four words.',
 'morph3':  'Say each pair of parts out loud. Type the whole word in the box. Then tap Check My Answers.',
 'morph4':  'Say what inter and sub mean. Then tap Roll the Dice. Say what the word means, and tap Check My Thinking. Roll all six words.',
 'vocabflip':  'Read how we figured out the first word. Then read each sentence from the book, guess what the word means, and tap the card to check. Last, play the matching game.',
 'vocabcloze': 'Read how we figured out the first word. Then fill in each sentence with a word from the word bank, and tap Check My Work. Last, play the matching game.',
 'gram1':   'Find the joining word in the sentence. Then tap each of the nine sentences, and tap the box it belongs in: and, but, or so. Last, write one sentence for each word.',
 'gram2':   'For each sentence, tap the joining word first. Then tap the part of the sentence that comes after it. Last, answer the question in the box.',
 'gram3':   'Type and, but, or so in each blank. Tap Check My Answers. Then write your own sentence that uses but.',
 'gram4':   'Read each sentence. Tap the joining word that is wrong, or tap No mistake. Then answer the question in the box.',
 'spell1':  'Say each word out loud and clap the beats. Then tap Now name the pattern. Last, tap each of the eight words, and tap the group it belongs in.',
 'spell2':  'Read the rule. Then tap every word in the two sentences that has a vowel team.',
 'spell3':  'Find the vowel team in each word. Then tap the word to split it into syllables.',
 'spell4':  'Tap Roll the dice. Say the word out loud and split it into syllables. Then tap Check my answer. Roll all six words.',
 'read':    'Read the two Pause and Think questions first. Then read today’s chapters in your book. When you get to each question, stop and think of your answer. You do not write these answers.',
 'readrev': 'There are no new chapters today. Read the two Pause and Think questions. Then look back through Chapters 1 to 5 in your book to find your answers. You do not write these answers.',
 'rwm':     'Read the sentence from the book. Then do the three parts in order. Write one sentence in each box.',
 'chapter': 'Choose Explorer or Scholar. Then answer the three questions in full sentences. Use details from the book.',
 'ww1':     'Read how Clara wrote her claim. Then write your own claim in the box: name a character, say what you think of him, and give a reason. Copy it into your own document.',
 'ww2':     'Read how Clara added a reason. Copy your claim from Day 1 into the box. Then write one reason under it. Copy it into your own document.',
 'ww3':     'Read how Clara added an example. Then write one example from the book. Start with: For example, in Chapter. Copy it into your own document.',
 'ww4':     'Read how Clara checked her writing. Read your claim, your reason and your example. Then write one thing you will add or fix.',
 'flu':     'Do the four steps in order. Read the passage out loud three times. Then record your best reading in Canvas.',
}

def do_line(slug):
    return '<p class="g3-do" data-say="%s"><b>What to do:</b> %s</p>' % (slug, DO[slug])

def must(h, old, new, f, n=1):
    c = h.count(old)
    if c != n:
        sys.exit('%s: expected %d of %r, found %d' % (f, n, old[:90], c))
    return h.replace(old, new)

def head(h, title, f, sub=None, slug=None, nth=1):
    """retitle the activity's sub line and put Opti's What to do line at the top of its body"""
    i = -1
    for _ in range(nth):
        i = h.find('activity-title">' + title, i + 1)
    if i < 0: sys.exit('%s: no activity %r' % (f, title))
    if sub is not None:
        m = re.compile(r'(<div class="activity-sub">)(.*?)(</div>)').search(h, i)
        h = h[:m.start(2)] + sub + h[m.end(2):]
    if slug:
        j = h.find('<div class="activity-body"', i)
        k = h.find('>', j) + 1
        h = h[:k] + '\n' + do_line(slug) + h[k:]
    return h

def common(h, f, day):
    # warm-up: the reading tip (paragraph + "watch for" said the same thing twice on days 2-4)
    h = must(h, '<li><strong>Watch who gives the orders:</strong> Notice who decides and who has to obey.</li>',
               '<li><strong>Who gives the orders?</strong> Notice who decides and who has to obey.</li>', f)
    h = must(h, '<li><strong>Notice how each one is treated:</strong> Look at what each character is given, allowed, and punished for.</li>',
               '<li><strong>Who gets what?</strong> Notice what each boy is given, what he is allowed to do, and what he is punished for.</li>', f)
    h = must(h, '<li><strong>Ask what would change:</strong> If the power flipped, what would each character do differently?</li>',
               '<li><strong>Who pays?</strong> Notice who gets punished when the prince does something wrong.</li>', f)
    h = must(h, '<div class="thinking-stop">💭 Think about this as you read today — you don\'t need to write anything here.</div>', '', f)
    h = head(h, '📚 What Good Readers Do', f, sub='What to watch for while you read', slug='readers')
    # DOL: the do line says it; the old paragraph said it longer
    h = head(h, '✏️ Daily Oral Language', f, sub='Fix a sentence from the story.', slug='dol')
    h, n = re.subn(r'\s*<p>The first sentence is <strong>correct</strong>\. Tap the parts you notice.*?</p>', '', h, count=1)
    if n != 1: sys.exit(f + ': DOL paragraph')
    h = head(h, 'Writer&rsquo;s Workshop', f, slug='ww%d' % day)
    # transitions
    h = must(h, 'Now that your mind is warmed up, let&rsquo;s sharpen your words and skills.', 'Next: word study.', f)
    h = must(h, 'Your words and skills are sharp. Time to open the book.', 'Next: reading.', f)
    h = must(h, 'You&rsquo;ve read and noticed. Now answer the questions and submit your work.', 'Next: answer the questions and turn in your work.', f)
    # reading tab
    h = must(h, '<div class="thinking-stop">💭 Think: How will your character help someone in your story?</div>', '', f)
    h = re.sub(r'<div class="callout callout-info" style="margin-bottom:14px;"><span class="callout-icon">&#x23F8;&#xFE0F;</span><p><strong>Read these first\.</strong>.*?</p></div>', '', h, count=1)
    h = h.replace('<div class="thinking-stop">💭 Pause and think about this — no need to write.</div>', '')
    # assignment
    h = head(h, '📖 Chapter Thinking', f, sub='Answer in full sentences. Use details from the book.', slug='chapter')
    h = must(h, '<div class="activity-title">🔤 Word Study Connection (Morphology)</div><div class="activity-sub">Your morphology response from the Word Study tab.</div>',
               '<div class="activity-title">🔤 Word Study Check</div><div class="activity-sub">The word part game on the Word Study tab</div>', f)
    h = must(h, 'Your morphology answer was saved on the Word Study tab. It will appear in your gathered work below.',
               'Finish the word part game on the Word Study tab. It shows in your work below.', f)
    h = must(h, 'I completed my Morphology response.', 'I finished the word part game on the Word Study tab.', f)
    h = re.sub(r'(I answered all 3 (?:chapter|review) questions) with evidence(?: from the book)?\.', r'\1 with details from the book.', h)
    h = re.sub(r'(<strong>Today&rsquo;s focus:</strong> )Today: ', r'\1', h)
    h = h.replace('{ title: \'🔤 WORD STUDY CONNECTION (MORPHOLOGY)\'', '{ title: \'🔤 WORD STUDY CHECK\'')
    # Character Spotlight repeated the warm-up's reading tip word for word
    h, n = re.subn(r'\s*<div class="key-concept" style="background:#F0E8FF;border-color:#D8CCF0;margin-bottom:14px;">\s*<div class="key-concept-label" style="color:#6B4FB0;">💎 As you read, notice:</div>\s*<p>.*?</p>\s*</div>', '', h, count=1, flags=re.S)
    if n != 1: sys.exit(f + ': spotlight tip')
    # the open book already says which chapters; the callout under it said it again
    h, n = re.subn(r'\s*<div class="callout callout-info" style="margin-bottom:14px;">\s*<span class="callout-icon">📕</span>\s*<p><strong>Open your novel to .*?</p>\s*</div>', '', h, count=1, flags=re.S)
    if n != 1: sys.exit(f + ': open-book callout')
    # Writer's Workshop: say the box's instruction once, in plain words
    h, n = re.subn(r'\s*<div class="callout callout-info" style="background:#E8F1E8;border-color:#A8C8A8;margin:0 0 10px 0;padding:10px 14px;"><span class="callout-icon">📝</span><p style="font-size:14px;"><strong>Now you try\.</strong>.*?</p></div>', '', h, count=1)
    if n != 1: sys.exit(f + ': now you try')
    h = re.sub(r'\s*<p style="font-size:14px;"><em>Today: [^<]*</em></p>', '', h, count=1)
    h = h.replace('🟡 Makes a judgment', '🟡 Says what you think').replace('🔴 Gives a reason hint', '🔴 Gives a reason')
    h = h.replace('Name a character, make a judgment, and give a reason hint.', 'Name a character, say what you think of him, and give a reason.')
    # vocabulary: the do line already says how the cards work
    h = re.sub(r'<div class="callout callout-info" style="margin-top:16px;"><span class="callout-icon">🎯</span><p><strong>Your turn!</strong> Each word below has its actual sentence from the book above it\..*?</p></div>', '', h, count=1)
    return h

def rwm(h, f):
    h = must(h, '<div class="rwm-header">📖 RWM &mdash; Read like a Reader, Read like a Writer, Mimic</div>',
               '<div class="rwm-header">📖 Read Like a Writer</div>\n' + do_line('rwm'), f)
    h = h.replace("{ title: '📖 RWM — READ LIKE A READER / WRITER / MIMIC'", "{ title: '📖 READ LIKE A WRITER'")
    h = h.replace('data-label="RWM &mdash; Read like a Reader"', 'data-label="Read like a reader"')
    h = h.replace('data-label="RWM &mdash; Read like a Writer"', 'data-label="Read like a writer"')
    h = h.replace('data-label="RWM &mdash; Mimic"', 'data-label="Write your own"')
    return h

def read_card(h, f, chap_open, chap_text):
    return h   # the callout is removed in common(); the open book names the chapters
    h = must(h, '<strong>Open your novel to %s.</strong> Read at your own pace. The Pause &amp; Think prompts are above &mdash; look them over first, then stop at each one as you read.' % chap_open,
               chap_text, f)
    return h

def day1(h, f):
    h = common(h, f, 1)
    h = must(h, '<p>Good readers notice who has power over whom at the start of a story. Pay attention to how Jemmy and the prince are different — their feelings, their choices, and the way they treat each other.</p>',
               '<p>Good readers notice who is in charge in a story. Today, watch how Jemmy and the prince are different: how they feel, what they choose, and how they treat each other.</p>', f)
    h = must(h, 'Jemmy takes the punishment every time the prince misbehaves. <strong>What does that arrangement tell you about who has power in the castle &mdash; and how does each boy feel about it?</strong>',
               'Jemmy is punished every time the prince does something wrong. <strong>Who has more power in the castle? How does each boy feel about that?</strong>', f)
    h = head(h, '🌱 Morphology: inter- and sub-', f, sub='Learn what inter- and sub- mean.', slug='morph1')
    h = must(h, '&#x1F331; See what was hiding', '&#x1F331; See what each part means', f)
    h = must(h, '<p>inter- and sub- means <strong>between, and under</strong>.</p>', '<p><strong>inter-</strong> means <strong>between</strong>. <strong>sub-</strong> means <strong>under</strong>.</p>', f)
    h = head(h, '🔤 Vocabulary', f, sub='Four words from this week’s chapters', slug='vocabflip')
    h = head(h, '✏️ Grammar: Conjunctions: and, but, so', f, sub='and, but and so join two ideas.', slug='gram1')
    h = must(h, '<p>This sentence is really two thoughts joined together. Find the joint.</p>', '<p>This sentence is two ideas joined by one word. Find the joining word.</p>', f)
    h = must(h, '<li>What word sits at the joint?</li>', '<li>Which word joins the two ideas?</li>', f)
    h = must(h, '<strong>Your turn.</strong> Nine sentences with the joining word taken out. Sort each one under the word that belongs in the gap.',
               '<strong>Your turn.</strong> Each sentence is missing its joining word. Tap a sentence, then tap and, but, or so.', f)
    # two "and" items could also take "so" — now only "and" fits
    h = must(h, '>Jemmy ran ___ he hid</span>', '>The king shouted ___ he stamped his foot</span>', f)
    h = must(h, '>They walked ___ they waited</span>', '>Jemmy swept the floor ___ he fed the rats</span>', f)
    h = must(h, '>The lantern came ___ they ran</span>', '>The lantern came closer ___ they ran</span>', f)
    h = must(h, 'What job does each of the three words do? Give one sentence for each.',
               'Write three sentences about the story: one with <strong>and</strong>, one with <strong>but</strong> and one with <strong>so</strong>.', f)
    h = head(h, '🔠 Spelling: Vowel team syllables', f, sub='Two vowels can work as a team to make one sound.', slug='spell1')
    h = must(h, '<li>Say each word. How many beats?</li>', '<li>How many beats does each word have?</li>', f)
    h = must(h, '<strong>ex-</strong> can mean <em>thoroughly</em>, <strong>asper</strong> means <em>rough</em>, and <strong>-ation</strong> turns a word into a thing. So <em>exasperation</em> is a rough, worn-out, fed-u',
               '<strong>asper</strong> means <em>rough</em>, and <strong>-ation</strong> turns a word into a thing. So <em>exasperation</em> is a rough, fed-u', f)
    h = must(h, '<li>Which beat holds two vowels side by side?</li>', '<li>Which beat has two vowels next to each other?</li>', f)
    h = must(h, '<strong>Look at the words below, then work through these:</strong>', '<strong>Say each word below. Then answer these in your head:</strong>', f)
    h = head(h, '📕 Read: Ch. 1–2', f, slug='read')
    h = read_card(h, f, 'Ch. 1–2', '<strong>Open your book to Chapter 1.</strong> Read Chapters 1 and 2.')
    h = must(h, '<div class="socratic-label">&#x1F451; Service nobody asked for:</div>', '<div class="socratic-label">&#x1F451; A job nobody asked for:</div>', f)
    h = must(h, 'Jemmy is fetched out of the north tower and takes twenty whacks for a prank he did not play &mdash; and he refuses to make a sound, because bawling is exactly what the prince wants to hear. It is service, but nobody ever asked him whether he wanted to give it.',
               'Jemmy is taken from the north tower and gets twenty whacks for a prank he did not play. He does not make a sound, because crying is what the prince wants. Nobody ever asked Jemmy if he wanted this job.', f)
    return h

def day2(h, f):
    h = common(h, f, 2)
    t = "Good readers notice when characters make bad decisions. Watch how the prince's choice to run away leads to trouble — and ask: who is responsible?"
    h = must(h, '<p>%s</p>' % t, '<p>Good readers notice when a character makes a bad choice. Today the prince decides to run away. Watch what trouble that choice causes.</p>', f)
    h = must(h, '<p class="socratic-q">%s</p>' % t, '<p class="socratic-q"><strong>The prince runs away, and Jemmy has to go too. Whose fault is the trouble they get into?</strong></p>', f)
    h = head(h, '🪶 Poetry', f, sub='A haiku has 3 lines: 5 syllables, then 7, then 5.', slug='poem2')
    h = head(h, '🌱 Morphology: inter- and sub-', f, sub='Match each word to its meaning.', slug='morph2')
    h = h.replace('<p>Before you start: find the word part, then read what is left.</p>', '<p>First find inter- or sub- in the word. Then read the rest of the word.</p>')
    h = must(h, '<p><strong>inter- and sub-</strong> means <strong>between, and under</strong>.</p>', '<p><strong>inter-</strong> means <strong>between</strong>. <strong>sub-</strong> means <strong>under</strong>.</p>', f)
    h = head(h, '🔤 Vocabulary', f, sub='Four words from this week’s chapters', slug='vocabflip')
    h = head(h, '✏️ Grammar: Conjunctions: and, but, so', f, sub='Find the joining word and the part it joins.', slug='gram2')
    h = must(h, '<strong>Your turn.</strong> Tap the joining word <strong>and</strong> the whole half it brings with it. Two taps each &mdash; one small, one large.',
               '<strong>Your turn.</strong> For each sentence, tap two things: first the joining word, then the part of the sentence that comes after it.', f)
    h = must(h, 'Take one sentence and swap its joining word for a different one. What happens to the meaning?',
               'Choose one sentence above. Write it again with a different joining word. Then write how the meaning changed.', f)
    h = head(h, '🔠 Spelling: Vowel team syllables', f, sub='Find the vowel teams in a story.', slug='spell2')
    h = h.replace('<p>Before you start: find the beat where two vowels share one sound.</p>', '<p>Look for two vowels that make one sound.</p>')
    h = must(h, '<p>Tap every word that keeps a <strong>vowel team</strong> together in one syllable.</p>', '<p>Tap every word that has a <strong>vowel team</strong>.</p>', f)
    h = head(h, '📕 Read: Ch. 3–4', f, slug='read')
    h = read_card(h, f, 'Ch. 3–4', '<strong>Open your book to Chapter 3.</strong> Read Chapters 3 and 4.')
    h = rwm(h, f)
    h = must(h, 'Three troubles, one after another, joined by commas: the fog, the wrong road, the trees. Fleischman stacks them up so the situation gets worse as the sentence goes on. The last one &mdash; <strong>trees had closed in</strong> &mdash; makes the wood sound alive.',
               'Fleischman puts three troubles in one sentence: the fog, the wrong road, and the trees. Each one makes things worse. The last one, <strong>trees had closed in</strong>, makes the woods sound alive.', f)
    # accuracy: the prince never laughs at a whipping (Ch. 15: Jemmy has "never before heard Prince Brat laugh")
    h = must(h, 'One reason is that Prince Brat enjoys watching Jemmy get whipped for things he didn\'t do — he laughs instead of feeling bad.',
               'One reason is that Prince Brat wants Jemmy whipped hard for things the prince did.', f)
    return h

def day3(h, f):
    h = common(h, f, 3)
    t = 'Good readers notice how characters handle pressure. Watch Jemmy carefully in Chapter 5 — does he fight, trick, or stay silent? Why?'
    h = must(h, '<p>%s</p>' % t, '<p>Good readers notice what a character does when he is in danger. In Chapter 5, watch what Jemmy does when the outlaws grab him.</p>', f)
    h = must(h, '<p class="socratic-q">%s</p>' % t, '<p class="socratic-q"><strong>Does Jemmy fight, trick the outlaws, or stay quiet? Why?</strong></p>', f)
    h = head(h, '🌱 Morphology: inter- and sub-', f, sub='Build words with inter- and sub-.', slug='morph3')
    h = h.replace('<p>Before you start: read the parts aloud, push them together, then write the word.</p>', '<p>Say each part out loud. Then say them together as one word.</p>')
    h = must(h, '<p><strong>inter- and sub-</strong> means <strong>between, and under</strong>.</p>', '<p><strong>inter-</strong> means <strong>between</strong>. <strong>sub-</strong> means <strong>under</strong>.</p>', f)
    h = head(h, '🔤 Vocabulary', f, sub='Four words from this week’s chapters', slug='vocabcloze')
    h = head(h, '✏️ Grammar: Conjunctions', f, sub='Join two sentences with and, but or so.', slug='gram3')
    h = head(h, '🔠 Spelling: Vowel team syllables', f, sub='Split words into syllables without breaking the vowel team.', slug='spell3')
    h = h.replace('<p>Before you start: find the beat where two vowels share one sound.</p>', '<p>Look for two vowels that make one sound.</p>')
    h = must(h, '<strong>Vowel Team Splitter!</strong> Find the vowel team first, then tap &mdash; the split never goes through it.',
               '<strong>Vowel Team Splitter!</strong> Find the vowel team, then tap the word. The split never goes through the vowel team.', f)
    h = head(h, '📕 Read: Ch. 5', f, slug='read')
    h = read_card(h, f, 'Ch. 5', '<strong>Open your book to Chapter 5.</strong> Read Chapter 5.')
    h = rwm(h, f)
    h = must(h, 'Fleischman does not write &ldquo;Jemmy was afraid the prince would give them away.&rdquo; He gives you the <strong>elbow</strong>, then tells you its purpose: <em>to keep his mouth shut</em>. An action plus its reason, in one sentence.',
               'Fleischman does not say Jemmy was afraid. He shows what Jemmy did (a jab with his <strong>elbow</strong>) and why he did it (<em>to keep his mouth shut</em>).', f)
    h = must(h, 'Write 1 sentence: what does the elbow tell you that the word <em>afraid</em> would not?', 'Write 1 sentence: what does the elbow jab show you about Jemmy?', f)
    h = must(h, 'He watches without feeling sorry.', 'He wants Jemmy hurt for the prince’s own mistake.', f)
    return h

def day4(h, f):
    h = common(h, f, 4)
    t = 'Good readers step back and think about the whole section. Who suffers more? Does either character deserve sympathy?'
    h = must(h, '<p>%s</p>' % t, '<p>Good readers look back at everything they have read so far. Today, think about both boys in Chapters 1 to 5.</p>', f)
    h = must(h, '<p class="socratic-q">%s</p>' % t, '<p class="socratic-q"><strong>Which boy has the harder life? Do you feel sorry for either one? Why?</strong></p>', f)
    h = head(h, '🪶 Poetry', f, sub='One haiku, one picture', slug='poem4')
    h = must(h, 'Choose one of the three haiku. In your journal, write the one picture it puts in your head &mdash; just the picture, no explaining.',
               'Choose one of the three haiku. Say out loud the one picture it puts in your head.', f)
    h = head(h, '🌱 Morphology: inter- and sub-', f, sub='Roll a word and tell what it means.', slug='morph4')
    h = h.replace('<p>Before you start: say what the word part does from memory, then roll.</p>', '<p>Before you roll, say out loud what inter- and sub- mean.</p>')
    h = must(h, '<p><strong>inter- and sub-</strong> means <strong>between, and under</strong>.</p>', '<p><strong>inter-</strong> means <strong>between</strong>. <strong>sub-</strong> means <strong>under</strong>.</p>', f)
    h = must(h, '<strong>Dice Roll Challenge!</strong> Roll a word, then say out loud what it means and how the word part changed it. Tap to check yourself.',
               '<strong>Dice Roll Challenge!</strong> Tap Roll the Dice. Say out loud what the word means. Then tap Check My Thinking.', f)
    h = head(h, '🔤 Vocabulary', f, sub='Review four words from this week', slug='vocabcloze')
    h = head(h, '✏️ Grammar: Conjunctions', f, sub='Find the wrong joining word. Not every sentence has one.', slug='gram4')
    h = must(h, 'One sentence was fine. Which, and how did you decide to leave it alone?', 'One sentence had no mistake. Which one was it? How did you know it was right?', f)
    h = head(h, '🔠 Spelling: Vowel team syllables', f, sub='Roll a word and split it into syllables.', slug='spell4')
    h = h.replace('<p>Before you start: find the beat where two vowels share one sound.</p>', '<p>Look for two vowels that make one sound.</p>')
    h = must(h, '<strong>Vowel Team Dice!</strong> Roll a word, say it out loud, decide &mdash; then tap to check yourself.',
               '<strong>Vowel Team Dice!</strong> Tap Roll the dice. Say the word and split it into syllables. Then tap Check my answer.', f)
    h = must(h, '<div class="activity-title">📕 Read: Ch. 1–5 Review</div><div class="activity-sub">Review and Writing Response</div>',
               '<div class="activity-title">📕 Look Back: Ch. 1–5</div><div class="activity-sub">No new chapters today</div>', f)
    h = head(h, '📕 Look Back: Ch. 1–5', f, slug='readrev')
    h = must(h, 'Open your novel to Ch. 1–5 Review.</div>', 'Look back at Chapters 1–5.</div>', f)
    h = read_card(h, f, 'Ch. 1–5 Review', '<strong>No new chapters today.</strong> Use your book to look back at Chapters 1 to 5.')
    h = rwm(h, f)
    h = must(h, 'Notice Fleischman does not call him Prince Brat here. He calls him <strong>the heir to the throne</strong> &mdash; the grandest name in the book &mdash; right as he is about to do something foolish. Choosing which name to use is a way of raising an eyebrow at a character.',
               'Here Fleischman calls the prince <strong>the heir to the throne</strong>. That is a very grand name. He uses it right before the prince does something foolish, and that makes the foolish thing funny.', f)
    h = must(h, 'Write 1 sentence: why use <em>the heir to the throne</em> instead of just <em>the prince</em>?', 'Write 1 sentence: why does the grand name make this part funny?', f)
    h = must(h, "Prince Brat is the most unfair character. One reason is that he watches Jemmy get whipped. For example...",
               "Prince Brat is the most unfair character. One reason is that he wants Jemmy whipped hard. For example...", f)
    h = must(h, "One thing to add: explain HOW watching shows Prince Brat doesn't care about others.",
               "One thing to add: explain how this shows Prince Brat doesn't care about others.", f)
    return h

def flu(h, f):
    h = must(h, '<div class="activity-sub">From Chapter 1 — Ch. 1–5</div>', '<div class="activity-sub">From Chapter 1</div>', f)
    h = must(h, 'This passage sets up the mischief! Read the first two sentences with a mysterious, storytelling voice. When you get to the part about the wigs flying off, let your voice rise with surprise and humor.',
               '<strong>How to read it:</strong> Read the first two sentences like you are telling a story. When the wigs fly off, make your voice sound surprised and funny.', f)
    h = must(h, '<strong>Read with expression.</strong> Read it a third time. Let your voice show the feeling — this passage sets up the mischief! Read the first two sentences with a mysterious, storytelling voice.',
               '<strong>Read with expression.</strong> Read it a third time. Use the voice from <em>How to read it</em>.', f)
    h = must(h, 'Did my voice change to show the building excitement — and then the funny surprise at the end?',
               'Did I sound like I was telling a story, and then surprised and funny when the wigs flew off?', f)
    h = head(h, '🎯 The 4 Steps', f, sub='Do these in order.', slug='flu')
    return h

FIX = {DAYS[0]: day1, DAYS[1]: day2, DAYS[2]: day3, DAYS[3]: day4, FLU: flu}
for f, fn in FIX.items():
    h = io.open(os.path.join(SRC, f), encoding='utf-8').read()
    h = fn(h, f)
    io.open(os.path.join(DST, f), 'w', encoding='utf-8').write(h)
    print('ok', f)
