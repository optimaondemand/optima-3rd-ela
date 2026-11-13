#!/usr/bin/env python3
"""Week 20 plain-language pass (The Whipping Boy, Ch. 11-15).

Same rules as plain_wk18.py (Bethany, Nov 8 2026): direct instruction,
nothing left to interpretation, valuable words only, each fact once, a
sort item has exactly one right answer. Every activity gets one
"What to do:" line that Opti reads (data-say = the clip slug; a slug that
already exists in how_wk18.json reuses that clip, so its words must match
exactly).

Reads pristine-orig/ (the week 20 files after acc_wk20.py), writes
pristine/ (the build input). Every replacement is asserted. Re-runnable."""
import io, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC, DST = os.path.expanduser('~/g3w20/pristine-orig'), os.path.expanduser('~/g3w20/pristine')
DAYS = ['lesson-20-1-wb.html', 'lesson-20-2-wb.html', 'lesson-20-3-wb.html', 'lesson-20-4-wb.html']
FLU = 'lesson-20-fluency.html'

# ── Opti's "What to do" lines. Week 18 slugs keep their exact words. ──
WK18 = json.load(io.open(os.path.join(HERE, 'how_wk18.json'), encoding='utf-8'))
WK19 = json.load(io.open(os.path.join(HERE, 'how_wk19.json'), encoding='utf-8'))
for k, v in WK19.items(): WK18.setdefault(k, v)
NEW = {
 'poem-haiku':  'Read the poem out loud and count its lines. Then answer the question: give two reasons it is not a haiku.',
 'poem-redo':   'Read the turtle poem again. Make up a haiku about the turtle: 3 lines, 5, then 7, then 5 syllables, and no rhyme. Say it out loud. Then think: what did you leave out?',
 'morph-spect1':'Read the three words. Think about the three questions. Then tap See if you were right. Type the missing word part in each box and tap Check My Work. Last, answer the question in the box.',
 'gram-prep1':  'Read the two sentences and tap Now check your thinking. Then tap each phrase, and tap the column it belongs in: where, when, or how. Last, answer the question in the box.',
 'gram-prep2':  'Read the sentence in the box and tap Check yourself. Then tap every preposition in each sentence. There is more than one. Last, answer the question in the box.',
 'gram-prep3':  'Read the three sentences in the box and tap Check yourself. Then type a word from the word bank in each blank, and tap Check My Answers. Last, answer the question in the box.',
 'spell-sort6': 'Say each word in Group A and Group B, and clap the beats. Tap See the Rule. Then tap each of the six words, and tap the group it belongs in.',
 'spell-beats': 'Say each word out loud and clap its beats. In each row, tap the one word with three syllables.',
 'spell-softcg':'Say the eight words in the sort out loud. Think about the three questions, then tap Now name the pattern. Last, tap each word, and tap the column it belongs in.',
 'ww-anchor':   'Read Clara’s weak and strong examples. Then find one example in your paragraph that needs a chapter number. Write it again with the chapter in it.',
 'ww-ending':   'Read Clara’s two conclusions. Then write your conclusion again. End with a question or a challenge.',
 'ww-edit':     'Check your paragraph with the editing checklist. Then write one mistake you fixed: what it was before, and what it is now.',
 'ww-check':    'Label each part of your paragraph: claim, reason, example, the other side, and conclusion. Then write one thing you are proud of and one thing you would make better.',
 'vocabflip2':  'Read how we figured out the first word. Then guess what each word means, and tap the card to check. Last, play the matching game.',
 'chase':       'Read the question. Tap the answer you think is right. A right answer moves Jemmy one step closer to the hollow tree.',
}
for k in NEW: assert k not in WK18, k
DO = dict(WK18); DO.update(NEW)
USED = set()

def do_line(slug):
    USED.add(slug)
    return '<p class="g3-do" data-say="%s"><b>What to do:</b> %s</p>' % (slug, DO[slug])

def must(h, old, new, f, n=1):
    c = h.count(old)
    if c != n:
        sys.exit('%s: expected %d of %r, found %d' % (f, n, old[:100], c))
    return h.replace(old, new)

def resub(h, pat, new, f, n=1, flags=re.S):
    h2, c = re.subn(pat, new, h, count=n, flags=flags)
    if c != n: sys.exit('%s: pattern %r matched %d' % (f, pat[:90], c))
    return h2

def head(h, title, f, sub=None, slug=None):
    i = h.find('activity-title">' + title)
    if i < 0: sys.exit('%s: no activity %r' % (f, title))
    if sub is not None:
        m = re.compile(r'(<div class="activity-sub">)(.*?)(</div>|<script>)', re.S).search(h, i)
        h = h[:m.start(2)] + sub + h[m.end(2):]
    if slug:
        j = h.find('<div class="activity-body"', i)
        k = h.find('>', j) + 1
        h = h[:k] + '\n' + do_line(slug) + h[k:]
    return h

LI = [('<li><strong>Watch the action, not the explanation:</strong> When a character will not say how they feel, their choices say it for them.</li>',
       '<li><strong>What does he do?</strong> When a character does not say how he feels, what he does shows it.</li>'),
      ('<li><strong>Ask what feeling fits:</strong> What would someone have to be feeling to do that?</li>',
       '<li><strong>What feeling fits?</strong> Ask: how would someone have to feel to do that?</li>'),
      ('<li><strong>Back it up with the book:</strong> Point to the line or moment that made you think so.</li>',
       '<li><strong>Where in the book?</strong> Find the line that made you think so.</li>')]

def common(h, f, day):
    for a, b in LI: h = must(h, a, b, f)
    h = must(h, '<div class="thinking-stop">💭 Think about this as you read today — you don\'t need to write anything here.</div>', '', f)
    h = head(h, '📚 What Good Readers Do', f, sub='What to watch for while you read', slug='readers')
    h = head(h, '✏️ Daily Oral Language', f, sub='Fix a sentence from the story.', slug='dol')
    h = resub(h, r'\s*<p>The first sentence is <strong>correct</strong>\. Tap the parts you notice.*?</p>', '', f)
    # transitions
    h = must(h, 'Now that your mind is warmed up, let&rsquo;s sharpen your words and skills.', 'Next: word study.', f)
    h = must(h, 'Your words and skills are sharp. Time to open the book.', 'Next: reading.', f)
    h = must(h, 'You&rsquo;ve read and noticed. Now answer the questions and submit your work.', 'Next: answer the questions and turn in your work.', f)
    # reading tab
    h = must(h, '<div class="thinking-stop">💭 Think: How will your character help someone in your story?</div>', '', f)
    h = resub(h, r'<div class="callout callout-info" style="margin-bottom:14px;"><span class="callout-icon">&#x23F8;&#xFE0F;</span><p><strong>Read these first\.</strong>.*?</p></div>', '', f)
    h = h.replace('<div class="thinking-stop">💭 Pause and think about this — no need to write.</div>', '')
    h = resub(h, r'\s*<div class="key-concept" style="background:#F0E8FF;border-color:#D8CCF0;margin-bottom:14px;">\s*<div class="key-concept-label" style="color:#6B4FB0;">💎 As you read, notice:</div>\s*<p>.*?</p>\s*</div>', '', f)
    h = resub(h, r'\s*<div class="callout callout-info" style="margin-bottom:14px;">\s*<span class="callout-icon">📕</span>\s*<p><strong>Open your novel to .*?</p>\s*</div>', '', f)
    # assignment
    h = head(h, '📖 Chapter Thinking', f, sub='Answer in full sentences. Use details from the book.', slug='chapter')
    h = must(h, '<div class="activity-title">🔤 Word Study Connection (Morphology)</div><div class="activity-sub">Your morphology response from the Word Study tab.</div>',
               '<div class="activity-title">🔤 Word Study Check</div><div class="activity-sub">The word part work on the Word Study tab</div>', f)
    h = must(h, 'Your morphology answer was saved on the Word Study tab. It will appear in your gathered work below.',
               'Finish the word part work on the Word Study tab. It shows in your work below.', f)
    h = must(h, 'I completed my Morphology response.', 'I finished the word part work on the Word Study tab.', f)
    h = re.sub(r'(I answered all 3 (?:chapter|review) questions) with evidence(?: from the book)?\.', r'\1 with details from the book.', h)
    h = h.replace('{ title: \'🔤 WORD STUDY CONNECTION (MORPHOLOGY)\'', '{ title: \'🔤 WORD STUDY CHECK\'')
    # Writer's Workshop
    h = must(h, 'Meet Today, our example writer', 'Meet Clara, our example writer', f)
    h = re.sub(r'(<strong>Today&rsquo;s focus:</strong> )Today: ', r'\1', h)
    h = resub(h, r'\s*<p style="font-size:14px;"><em>Today: [^<]*</em></p>', '', f)
    h = resub(h, r'\s*<div class="callout callout-info" style="background:#E8F1E8;border-color:#A8C8A8;margin:0 0 10px 0;padding:10px 14px;"><span class="callout-icon">📝</span><p style="font-size:14px;"><strong>Now you try\.</strong>.*?</p></div>', '', f)
    h = head(h, 'Writer&rsquo;s Workshop', f, slug=['ww-anchor', 'ww-ending', 'ww-edit', 'ww-check'][day - 1])
    # vocabulary: the do line says how the cards work
    h = re.sub(r'<div class="callout callout-info" style="margin-top:16px;"><span class="callout-icon">🎯</span><p><strong>Your turn!</strong> Each word below has its actual sentence from the book above it\..*?</p></div>', '', h, count=1)
    # spelling: a See the Rule button that opens an empty box
    if 'id="spellReveal"></div>' in h:
        h = resub(h, r'\s*<button class="dol-check-btn"[^>]*spellReveal[^>]*>🔍 See the Rule</button>\s*<div class="dol-answer" id="spellReveal"></div>', '', f)
    return h

def rwm(h, f):
    h = must(h, '<div class="rwm-header">📖 RWM &mdash; Read like a Reader, Read like a Writer, Mimic</div>',
               '<div class="rwm-header">📖 Read Like a Writer</div>\n' + do_line('rwm'), f)
    h = h.replace("{ title: '📖 RWM — READ LIKE A READER / WRITER / MIMIC'", "{ title: '📖 READ LIKE A WRITER'")
    h = h.replace('data-label="RWM &mdash; Read like a Reader"', 'data-label="Read like a reader"')
    h = h.replace('data-label="RWM &mdash; Read like a Writer"', 'data-label="Read like a writer"')
    h = h.replace('data-label="RWM &mdash; Mimic"', 'data-label="Write your own"')
    return h

def wgrd(h, f, old, p, q):
    h = must(h, '<p>%s</p>' % old, '<p>%s</p>' % p, f)
    h = must(h, '<p class="socratic-q">%s</p>' % old, '<p class="socratic-q"><strong>%s</strong></p>' % q, f)
    return h

def spell_rule_boxes(h, f):
    h = must(h, '<p class="socratic-q">Look at the last three letters of each word. What two of them are always the same?</p>',
               '<p class="socratic-q">Look at the last three letters of each word. Which two letters are always the same?</p>', f)
    h = must(h, '<p class="socratic-q">Count back three letters from the end of each word. Where does the dot land?</p>',
               '<p class="socratic-q">Count back three letters from the end of each word. Is that where the dot is?</p>', f)
    return h


BEFORE = '<p>Before you start: split each word into beats, then read the pieces.</p>'
def spell_common(h, f):
    h = must(h, BEFORE, '<p>Say each word out loud. Clap the beats.</p>', f)
    return h

def day1(h, f):
    h = common(h, f, 1)
    h = must(h, "<p>Good readers read between the lines. When a character doesn't explain their feelings, look at their ACTIONS. Watch what the prince DOES — not just what he says.</p>",
               '<p>Good readers read between the lines. When a character does not say how he feels, look at what he does. Today, watch what the prince does, not just what he says.</p>', f)
    h = must(h, 'In Chapter 12, Jemmy hides under the straw. He never stops to explain how he feels. <strong>What do his actions tell you that his words do not?</strong>',
               'In Chapter 12, Jemmy hides under the straw. He never says how he feels. <strong>What do his actions tell you?</strong>', f)
    h = head(h, '🌱 Morphology: Root/base: spect means look', f, sub='Figure out what the root spect means.', slug='morph-spect1')
    h = must(h, '<p>This chunk is not a word on its own &mdash; it is an old root that shows up inside other words.</p>',
               '<p>A <strong>root</strong> is the main part of a word. These three words all have the same root.</p>', f)
    h = must(h, '<li>Think about what the words have in common. Eyes, or ears, or hands?</li>', '<li>Do these words have to do with eyes, ears, or hands?</li>', f)
    h = must(h, '<p style="font-size:13px;color:#7A88A8;margin-top:4px;">Every answer below comes from this list. Some may be used more than once.</p>',
               '<p style="font-size:13px;color:#7A88A8;margin-top:4px;">Every answer comes from this list. You can use a word part more than once.</p>', f)
    h = head(h, '🔤 Vocabulary', f, sub='Four words from The Whipping Boy', slug='vocabflip2')
    h = head(h, '✏️ Grammar: Prepositions', f, sub='A preposition can tell where, when, or how.', slug='gram-prep1')
    h = must(h, '<p>Two sentences about the same moment. The second one tells you more, and it is one small word doing it.</p>',
               '<p>Two sentences about the same moment. The second one tells you more. Look for the small word that starts the new part.</p>', f)
    h = must(h, '<strong>Your turn.</strong> Nine phrases, three columns. Each phrase starts with a preposition &mdash; sort it by the question that preposition answers.',
               '<strong>Your turn.</strong> Each phrase starts with a preposition. Tap a phrase, then tap the question it answers.', f)
    h = head(h, '🔠 Spelling: Multisyllabic Decoding', f, sub='Split long words into beats.', slug='spell-sort6')
    h = must(h, '<strong>Practice:</strong> Sort these words using the pattern you discovered.', '<strong>Practice:</strong> Tap a word, then tap the group it belongs in.', f)
    h = head(h, '📕 Read: Ch. 11–12', f, slug='read')
    return h

def day2(h, f):
    h = common(h, f, 2)
    h = wgrd(h, f, 'Good readers look for clues in what characters say AND how they say it. When two characters argue, both sides have a point. Look for both.',
             'Good readers notice what characters say and how they say it. Today Jemmy and the prince argue. Each boy has a point. Look for both.',
             'What is Jemmy’s side? What is the prince’s side?')
    h = head(h, '🪶 Poetry', f, sub='A haiku has 3 lines: 5 syllables, then 7, then 5. It does not rhyme.', slug='poem-haiku')
    h = head(h, '🌱 Morphology: spect', f, sub='Match each word to its meaning.', slug='morph2')
    h = must(h, '<p>Before you start: find the word part, then read what is left.</p>', '<p>Find spect in each word. Then look at the parts around it.</p>', f)
    h = must(h, '<strong>Practice: Match the Word to Its Meaning!</strong> Tap a word, then tap what it means.', '<strong>Match the Word to Its Meaning!</strong>', f)
    h = head(h, '🔤 Vocabulary', f, sub='Four words from this week’s chapters', slug='vocabflip2')
    h = head(h, '✏️ Grammar: Prepositions', f, sub='Find every preposition in a sentence.', slug='gram-prep2')
    h = must(h, '<strong>Your turn.</strong> Tap <strong>every</strong> preposition in each sentence &mdash; there is more than one. The sentence only finishes when you have found them all.',
               '<strong>Your turn.</strong> Each sentence has more than one preposition. Find them all.', f)
    h = head(h, '🔠 Spelling: Multisyllabic Decoding', f, sub='Hear the beats in long words.', slug='spell-beats')
    h = spell_common(h, f)
    h = must(h, '<p>Divide these words into syllables using what you know. Say each syllable out loud.</p>', '', f)
    h = must(h, '<strong>Sound Detective!</strong> Clap each word as you say it. One in every row has an extra beat.', '<strong>Sound Detective!</strong>', f)
    h = head(h, '🔠 Spelling Bonus: Soft c and soft g', f, sub='Hear when c and g make a soft sound.', slug='spell-softcg')
    h = must(h, '<p>Say these aloud. The same letters are not making the same sound.</p>',
               '<p>Look at the eight words in the sort below. Say them out loud. The letters c and g do not always make the same sound.</p>', f)
    h = must(h, '<p><strong>c</strong> and <strong>g</strong> go soft &mdash; /s/ and /j/ &mdash; when the very next letter is <strong>e</strong>, <strong>i</strong> or <strong>y</strong>: <em>mice</em>, <em>magic</em>.</p>', '', f)
    h = h.replace('Before any other letter they stay hard: <em>cave</em>, <em>goat</em>.</p>', 'Before any other letter they stay hard: <em>cave</em>, <em>goat</em>.</p>', 1)
    h = head(h, '📕 Read: Ch. 13–14', f, slug='read')
    h = rwm(h, f)
    return h

def day3(h, f):
    h = common(h, f, 3)
    h = wgrd(h, f, 'Good readers infer character traits from small details. Watch Jemmy and the prince working together on the riverbank — what can you infer about each of them from their actions?',
             'Good readers figure out what a character is like from the small things he does. Today Jemmy and the prince work together on the riverbank.',
             'What do their actions show about each boy?')
    h = head(h, '🌱 Morphology: spect', f, sub='Build words with spect.', slug='morph3')
    h = must(h, '<p>Before you start: read the parts aloud, push them together, then write the word.</p>', '<p>Say each part out loud. Then say them together as one word.</p>', f)
    h = head(h, '🔤 Vocabulary', f, sub='Four words from Chapter 15', slug='vocabcloze')
    h = head(h, '✏️ Grammar: Prepositions', f, sub='Pick the preposition that fits.', slug='gram-prep3')
    h = must(h, '<p>Same sentence, different preposition. Read all three aloud and watch the picture change.</p>',
               '<p>Same sentence, three different prepositions. Read all three out loud. Picture where the coach is each time.</p>', f)
    h = must(h, '<strong>Your turn.</strong> Each bank word fits exactly one sentence. Type it in.', '<strong>Your turn.</strong> Each word in the bank fits one sentence.', f)
    h = head(h, '🔠 Spelling: Multisyllabic Decoding', f, sub='Build long words from their beats.', slug='spell-tiles')
    h = spell_common(h, f)
    h = must(h, '<p>Divide these words and say them quickly and smoothly. Fluency practice!</p>', '', f)
    h = must(h, '<strong>Syllable Tiles!</strong> Three beats each. Clap the word before you start. Tap the chunks <strong>in order</strong> to build the word. A chunk in the wrong place will not stick.',
               '<strong>Syllable Tiles!</strong> Three beats each. Clap the word before you start.', f)
    h = head(h, '📕 Read: Ch. 15', f, slug='read')
    h = rwm(h, f)
    return h

def day4(h, f):
    h = common(h, f, 4)
    h = wgrd(h, f, 'Good readers look back at a section and find the single most important turning point. Which moment in Chapters 11–15 changed the story the most?',
             'Good readers look back and find the moment that changed the story the most. Today, look back at Chapters 11–15.',
             'Which moment changed the story the most?')
    h = head(h, '🪶 Poetry', f, sub='Turn a rhyme into a haiku.', slug='poem-redo')
    h = must(h, 'Rewrite the turtle poem as a real haiku: three lines, 5&ndash;7&ndash;5, no rhyme. You will have to leave things out. What did you cut?',
               'Turn the turtle poem into a haiku: 3 lines, 5&ndash;7&ndash;5, no rhyme. You will have to leave things out. What did you leave out?', f)
    h = head(h, '🌱 Morphology: spect', f, sub='Roll a word and tell what it means.', slug='morph-dice')
    h = must(h, '<p>Before you start: say what the word part does from memory, then roll.</p>', '<p>Before you roll, say out loud what spect means.</p>', f)
    h = must(h, '<strong>Dice Roll Challenge!</strong> Roll a word, then say out loud what it means and how the word part changed it. Tap to check yourself.', '<strong>Dice Roll Challenge!</strong>', f)
    h = head(h, '🔤 Vocabulary', f, sub='Review four words from this week', slug='vocabcloze')
    h = head(h, '✏️ Grammar: Prepositions', f, sub='Find the mistake. Not every sentence has one.', slug='gram-hunt')
    h = must(h, '<p>Start with this one. In the four sentences below, some have a preposition doing the wrong job &mdash; and at least one is perfectly fine.</p>',
               '<p>Some sentences below use the wrong preposition. At least one has no mistake.</p>', f)
    h = must(h, '<strong>Your turn.</strong> Each sentence either has one preposition doing the wrong job, or nothing wrong at all. Tap the word that is wrong &mdash; or tap <strong>No mistake</strong>.',
               '<strong>Your turn.</strong> Each sentence has one wrong preposition or no mistake.', f)
    h = must(h, '🔠 Spelling: Multisyllabic Decoding — Unit Celebration Sort</div>', '🔠 Spelling: Multisyllabic Decoding</div>', f)
    h = head(h, '🔠 Spelling: Multisyllabic Decoding', f, sub='Roll a long word and split it into beats.', slug='spell4')
    h = spell_common(h, f)
    h = must(h, '<p>Decode these vocabulary words from The Whipping Boy. Divide the syllables and read them aloud.</p>', '', f)
    h = must(h, '<strong>Long Word Dice!</strong> Roll a word, say it out loud, decide &mdash; then tap to check yourself.', '<strong>Long Word Dice!</strong>', f)
    h = must(h, '<div class="activity-title">📕 Read: Ch. 11–15 Review</div><div class="activity-sub">Review, Response, and Writing Workshop</div>',
               '<div class="activity-title">📕 Look Back: Ch. 11–15</div><div class="activity-sub">No new chapters today</div>', f)
    h = head(h, '📕 Look Back: Ch. 11–15', f, slug='readrev-week')
    h = must(h, 'Open your novel to Ch. 11–15 Review.</div>', 'Look back at Chapters 11–15.</div>', f)
    h = must(h, '<div class="info-detail">Review, Response, and Writing Workshop</div>', '<div class="info-detail">No new chapters today</div>', f)
    h = rwm(h, f)
    return h

def flu(h, f):
    h = must(h, '<div class="activity-sub">From Chapter 13 — Ch. 11–15</div>', '<div class="activity-sub">From Chapter 13</div>', f)
    h = must(h, 'This is an escape! Read it fast and urgent. Short sentences need short, punchy delivery. The last three lines should feel like rapid heartbeats — one beat each.',
               '<strong>How to read it:</strong> This is an escape! Read it fast. Read each short sentence short and sharp. Read the last three lines like quick heartbeats.', f)
    h = must(h, '<strong>Read with expression.</strong> Read it a third time. Let your voice show the feeling — this is an escape! Read it fast and urgent.',
               '<strong>Read with expression.</strong> Read it a third time. Read it the way <em>How to read it</em> says.', f)
    h = must(h, 'Did my pace pick up to match the excitement of the chase?', 'Did I read faster to match the chase?', f)
    h = head(h, '🎯 The 4 Steps', f, sub='Do these in order.', slug='flu')
    return h

FIX = {DAYS[0]: day1, DAYS[1]: day2, DAYS[2]: day3, DAYS[3]: day4, FLU: flu}
if __name__ == '__main__':
    os.makedirs(DST, exist_ok=True)
    for f, fn in FIX.items():
        h = io.open(os.path.join(SRC, f), encoding='utf-8').read()
        h = fn(h, f)
        io.open(os.path.join(DST, f), 'w', encoding='utf-8').write(h)
        print('ok', f)
    how = {k: DO[k] for k in sorted(USED) if k not in WK18}
    io.open(os.path.join(HERE, 'how_wk20.json'), 'w', encoding='utf-8').write(json.dumps(how, ensure_ascii=False, indent=1))
    print('reused:', sorted(k for k in USED if k in WK18))
    print('new clips:', sorted(how))
