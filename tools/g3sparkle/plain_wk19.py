#!/usr/bin/env python3
"""Week 19 plain-language pass (The Whipping Boy, Ch. 6-11).

Same rules as plain_wk18.py (Bethany, Nov 8 2026): direct instruction,
nothing left to interpretation, valuable words only, each fact once, a
sort item has exactly one right answer. Every activity gets one
"What to do:" line that Opti reads (data-say = the clip slug; a slug that
already exists in how_wk18.json reuses that clip, so its words must match
exactly).

Reads pristine-orig/ (the week 19 files after the accuracy commit), writes
pristine/ (the build input). Every replacement is asserted. Re-runnable."""
import io, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC, DST = '/home/claude/g3/pristine-orig', '/home/claude/g3/pristine'
DAYS = ['lesson-19-1-wb.html', 'lesson-19-2-wb.html', 'lesson-19-3-wb.html', 'lesson-19-4-wb.html']
FLU = 'lesson-19-fluency.html'

# ── Opti's "What to do" lines. Week 18 slugs keep their exact words. ──
WK18 = json.load(io.open(os.path.join(HERE, 'how_wk18.json'), encoding='utf-8'))
NEW = {
 'poem-turn':     'Read the two haiku out loud. Clap the syllables in each line: 5, then 7, then 5. Then find the word where each haiku changes direction.',
 'poem-make':     'Make up your own haiku about something outside your window. Count the syllables on your fingers: 5, then 7, then 5. Say it out loud. You do not need to write it.',
 'morph-root1':   'Read the four words. Think about the three questions. Then tap See if you cracked it. Type the missing root in each box and tap Check My Work. Last, answer the question in the box.',
 'morph-dice':    'Say what the word part means. Then tap Roll the Dice. Say what the word means, and tap Check My Thinking. Roll all six words.',
 'gram-sort3':    'Read the sentence in the box and tap Now check your thinking. Then tap each word group, and tap the column it belongs in. Last, answer the question in the box.',
 'gram-halves':   'In each sentence, tap the two complete thoughts. Do not tap the joining word. Then answer the question in the box.',
 'gram-comma':    'Find the last word of the first complete thought. Type it in the box, and tap Check My Answers. Then write your own compound sentence.',
 'gram-hunt':     'Read each sentence. Tap the word where the mistake is, or tap No mistake. Then tap See the answers, and answer the question in the box.',
 'spell-sort':    'Say each word in Group A and Group B. Think about the three questions, then tap See the Rule. Last, tap each of the eight words, and tap the group it belongs in.',
 'spell-find':    'Read the rule. Then in each row, tap the one word that ends in a consonant-le syllable.',
 'spell-tiles':   'Tap the word parts in order to build each word. A part in the wrong place will not stick.',
 'readrev-week':  'There are no new chapters today. Read the two Pause and Think questions. Then look back through this week’s chapters in your book to find your answers. You do not write these answers.',
 'ww-counter':    'Read how Clara thought about the other side. Then write one sentence that says what someone who disagrees might think, and why you still think you are right.',
 'ww-transition': 'Read your opinion paragraph out loud. Then write one of your sentences again with a transition word, like For example or Another reason is.',
 'ww-conclusion': 'Read Clara’s conclusion. Then write a conclusion sentence for your paragraph. Do not copy your first sentence word for word.',
 'ww-full':       'Read Clara’s whole paragraph. Then write your own paragraph in the box with all five parts: claim, reason, example, the other side, and conclusion.',
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

LI = [('<li><strong>Name what each character wants:</strong> Ask it separately for each one &mdash; right now, in this chapter.</li>',
       '<li><strong>What does each boy want?</strong> Ask it for Jemmy. Then ask it for the prince.</li>'),
      ('<li><strong>Find the action that proves it:</strong> Characters show what they want by what they do, not by announcing it.</li>',
       '<li><strong>What does he do to get it?</strong> What a character does shows what he wants.</li>'),
      ('<li><strong>Ask whether the wants collide:</strong> When two characters want opposite things, that is where the trouble comes from.</li>',
       '<li><strong>Do their wants clash?</strong> When two characters want opposite things, trouble starts.</li>')]

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
    h = head(h, 'Writer&rsquo;s Workshop', f, slug=['ww-counter', 'ww-transition', 'ww-conclusion', 'ww-full'][day - 1])
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

def day1(h, f):
    h = common(h, f, 1)
    h = must(h, '<p>Good readers think about WHY characters act the way they do. Ask yourself: what does Jemmy want right now? What does the prince want? Are those the same things?</p>',
               '<p>Good readers think about why characters do what they do. Today, ask: what does Jemmy want right now? What does the prince want?</p>', f)
    h = must(h, 'The prince chose to run away. Jemmy has been waiting for a chance to escape. <strong>Why would two boys leave the same castle for completely different reasons?</strong>',
               'The prince chose to run away. Jemmy has been waiting for a chance to escape. <strong>Why does each boy want to get away from the castle?</strong>', f)
    # morphology
    h = head(h, '🌱 Morphology: Root/base: port means carry', f, sub='Figure out what the root port means.', slug='morph-root1')
    h = must(h, '<p>One old root this time. Four words, and they all carry it.</p>', '<p>A <strong>root</strong> is the main part of a word. These four words all have the same root.</p>', f)
    h = must(h, '<li>What is being moved in each one &mdash; and where to?</li>', '<li>In each word, where is something being moved to?</li>', f)
    h = must(h, 'Type the missing <strong>prefix</strong> at the start of each word.', 'Type the missing <strong>root</strong> at the end of each word.', f)
    h = must(h, '<p style="font-size:13px;color:#7A88A8;margin-top:4px;">Every answer below comes from this list. Some may be used more than once.</p>',
               '<p style="font-size:13px;color:#7A88A8;margin-top:4px;">Every answer comes from this list. You can use a word more than once.</p>', f)
    h = must(h, '<div class="textbox-prompt">Use the prefix and its meaning.</div>', '<div class="textbox-prompt">Use the first part of each word and the root port.</div>', f)
    # vocabulary
    h = head(h, '🔤 Vocabulary', f, sub='Four words from this week’s chapters', slug='vocabflip')
    # grammar
    h = head(h, '✏️ Grammar: Compound Sentences', f, sub='A compound sentence joins two complete thoughts.', slug='gram-sort3')
    h = must(h, '<p>Look at the two halves of this sentence and what holds them together.</p>', '<p>Look at the two parts of this sentence and the word that joins them.</p>', f)
    h = must(h, '<p>A compound sentence: two complete thoughts joined by a comma and <strong>but</strong>. The <strong>but</strong> tells you the second half goes against the first.</p>',
               '<p>In this sentence, a comma and <strong>but</strong> join the two thoughts. <strong>but</strong> tells you the second part goes against the first.</p>', f)
    h = must(h, '<strong>Your turn.</strong> Nine word groups, three columns. Read each one aloud and decide how many complete thoughts it holds.',
               '<strong>Your turn.</strong> Read each word group out loud. Tap it, then tap the column it belongs in.', f)
    # spelling: "table" was filed under Other ending, but it is the rule's own example
    h = head(h, '🔠 Spelling: Consonant-le Syllables', f, sub='Find the last syllable in words that end in -le.', slug='spell-sort')
    h = spell_rule_boxes(h, f)
    h = must(h, '<span class="sort-chip" data-group="b" onclick="pickSortChip(this)">table</span>', '<span class="sort-chip" data-group="b" onclick="pickSortChip(this)">basket</span>', f)
    h = must(h, '<strong>Practice:</strong> Sort these words using the pattern you discovered.', '<strong>Practice:</strong> Tap a word, then tap the group it belongs in.', f)
    # reading
    h = head(h, '📕 Read: Ch. 6–7', f, slug='read')
    return h

def day2(h, f):
    h = common(h, f, 2)
    h = wgrd(h, f, "Good readers look for moments when a character does something unexpected. Watch for a moment where Jemmy does something surprising for someone who hasn't deserved it.",
             'Good readers notice when a character does something they did not expect. Today, watch for a moment when Jemmy does something kind for the prince, even though the prince has not been kind to him.',
             'What does Jemmy do for the prince? Why might he do it?')
    h = head(h, '🪶 Poetry', f, sub='A haiku has 3 lines: 5 syllables, then 7, then 5.', slug='poem-turn')
    h = must(h, '<p class="socratic-q">Count the syllables in each line of both haiku. Then find the word in each one where things change.</p>',
               '<p class="socratic-q">Which word in each haiku is where things change?</p>', f)
    h = head(h, '🌱 Morphology: port', f, sub='Match each word to its meaning.', slug='morph2')
    h = must(h, '<p>Before you start: find the word part, then read what is left.</p>', '<p>Find port in each word. Then look at the part in front of it.</p>', f)
    h = must(h, '<strong>Practice: Match the Word to Its Meaning!</strong> Tap a word, then tap what it means.', '<strong>Match the Word to Its Meaning!</strong>', f)
    h = head(h, '🔤 Vocabulary', f, sub='Four words from this week’s chapters', slug='vocabflip')
    h = must(h, 'To <strong>oblige</strong> someone is to do them a favor, and <strong>-ed</strong> tells how someone feels. So being <em>obliged</em> means feeling you owe someone thanks.',
               'To <strong>oblige</strong> someone is to do them a favor. When someone does you a favor, you feel <em>obliged</em>: you owe them thanks.', f)
    h = head(h, '✏️ Grammar: Compound Sentences', f, sub='Find the two complete thoughts in a sentence.', slug='gram-halves')
    h = must(h, '<p>Today we decide whether a sentence is <em>compound</em> (two complete thoughts joined by a conjunction) or <em>simple</em> (one thought).</p>',
               '<p>A <em>compound</em> sentence has two complete thoughts joined by a joining word. Today you find the two thoughts.</p>', f)
    h = must(h, '<strong>Your turn.</strong> Tap <strong>both</strong> complete thoughts in each sentence &mdash; the joining word in the middle is not one of them.',
               '<strong>Your turn.</strong> Tap <strong>both</strong> complete thoughts in each sentence. The joining word is not part of either one.', f)
    h = must(h, 'Pick one sentence and write out its two halves as two separate sentences. Which version reads better, and why?',
               'Choose one sentence above. Write its two thoughts as two separate sentences. Then write which way sounds better, and why.', f)
    h = head(h, '🔠 Spelling: Consonant-le Syllables', f, sub='Find the word that ends in consonant-le.', slug='spell-find')
    h = spell_rule_boxes(h, f)
    h = must(h, '<p>Before you start: listen to the last beat and notice how quiet it is.</p>', '<p>Say each word out loud. Listen to the last beat.</p>', f)
    h = head(h, '📕 Read: Ch. 8–9', f, slug='read')
    h = rwm(h, f)
    return h

def day3(h, f):
    h = common(h, f, 3)
    h = wgrd(h, f, 'Good readers notice when a character changes — even slightly. Watch Prince Brat in Chapter 11. He makes a surprising choice. Why?',
             'Good readers notice when a character changes, even a little. In Chapter 11, the prince makes a choice that surprises Jemmy.',
             'What does the prince choose? Why might he choose it?')
    h = head(h, '🌱 Morphology: port', f, sub='Build words with port.', slug='morph3')
    h = must(h, '<p>Before you start: read the parts aloud, push them together, then write the word.</p>', '<p>Say each part out loud. Then say them together as one word.</p>', f)
    h = head(h, '🔤 Vocabulary', f, sub='Four words from this week’s chapters', slug='vocabcloze')
    h = head(h, '✏️ Grammar: Compound Sentences', f, sub='Find where the comma goes.', slug='gram-comma')
    h = must(h, '<p>Today you write your own compound sentences about Chapters 10–11.</p>',
               '<p>In a compound sentence, the comma goes right before the joining word.</p>', f)
    h = must(h, '<strong>Your turn.</strong> Nobody has punctuated these. Type the word the comma belongs after &mdash; it is always the last word of the first complete thought.',
               '<strong>Your turn.</strong> These sentences have no commas. Type the word the comma goes after. It is the last word of the first complete thought.', f)
    h = must(h, 'Write a compound sentence of your own about Chapter 10 or 11, comma and all.',
               'Write your own compound sentence about Chapter 10 or 11. Put the comma before the joining word.', f)
    h = head(h, '🔠 Spelling: Consonant-le Syllables', f, sub='Build words that end in consonant-le.', slug='spell-tiles')
    h = spell_rule_boxes(h, f)
    h = must(h, '<p>Before you start: listen to the last beat and notice how quiet it is.</p>', '<p>Say each word out loud. Listen to the last beat.</p>', f)
    h = must(h, '<p>Today we divide words with consonant-le syllables and practice reading them smoothly.</p>', '', f)
    h = must(h, '<strong>Syllable Tiles!</strong> Notice that the consonant always travels with the <em>-le</em>. Tap the chunks <strong>in order</strong> to build the word. A chunk in the wrong place will not stick.',
               '<strong>Syllable Tiles!</strong> The consonant always stays with the <em>-le</em>.', f)
    h = head(h, '📕 Read: Ch. 10–11', f, slug='read')
    h = rwm(h, f)
    return h

def day4(h, f):
    h = common(h, f, 4)
    h = wgrd(h, f, 'Good readers return to the whole section and ask: how has each character changed since Chapter 1? Compare who they were at the start to who they are now.',
             'Good readers look back at everything they have read so far. Today, think about how Jemmy and the prince have changed since Chapter 1.',
             'How is each boy different now from how he was in Chapter 1?')
    h = head(h, '🪶 Poetry', f, sub='Make up your own haiku.', slug='poem-make')
    h = must(h, '<p class="socratic-q">Write your own haiku about something that happens outside your window. Count on your fingers: 5, then 7, then 5.</p>',
               '<p class="socratic-q">What could your haiku be about? A bird, a car, the rain, a tree?</p>', f)
    h = head(h, '🌱 Morphology: port', f, sub='Roll a word and tell what it means.', slug='morph-dice')
    h = must(h, '<p>Before you start: say what the word part does from memory, then roll.</p>', '<p>Before you roll, say out loud what port means.</p>', f)
    h = must(h, '<strong>Dice Roll Challenge!</strong> Roll a word, then say out loud what it means and how the word part changed it. Tap to check yourself.',
               '<strong>Dice Roll Challenge!</strong>', f)
    h = head(h, '🔤 Vocabulary', f, sub='Review four words from this week', slug='vocabcloze')
    h = head(h, '✏️ Grammar: Compound Sentences', f, sub='Find the mistake. Not every sentence has one.', slug='gram-hunt')
    h = must(h, '<p>Today you will write three compound sentences — one for each conjunction — about Chapters 6–11.</p>',
               '<p>Today you check compound sentences for mistakes. Look at the comma and the joining word together.</p>', f)
    h = must(h, '<strong>Your turn.</strong> Each sentence either has one mistake or nothing wrong at all. Tap the word that is wrong, or tap <strong>No mistake</strong>. Look at the commas and the joining words together.',
               '<strong>Your turn.</strong> Each sentence has one mistake or no mistake.', f)
    h = head(h, '🔠 Spelling: Consonant-le Syllables', f, sub='Roll a word and split it into syllables.', slug='spell4')
    h = spell_rule_boxes(h, f)
    h = must(h, '<p>Before you start: listen to the last beat and notice how quiet it is.</p>', '<p>Say each word out loud. Listen to the last beat.</p>', f)
    h = must(h, '<strong>Consonant-le Dice!</strong> Roll a word, say it out loud, decide &mdash; then tap to check yourself.',
               '<strong>Consonant-le Dice!</strong>', f)
    h = must(h, '<div class="activity-title">📕 Read: Ch. 6–11 Review</div><div class="activity-sub">Review, Response, and Writing Workshop</div>',
               '<div class="activity-title">📕 Look Back: Ch. 6–11</div><div class="activity-sub">No new chapters today</div>', f)
    h = head(h, '📕 Look Back: Ch. 6–11', f, slug='readrev-week')
    h = must(h, 'Open your novel to Ch. 6–11 Review.</div>', 'Look back at Chapters 6–11.</div>', f)
    h = must(h, '<div class="info-detail">Review, Response, and Writing Workshop</div>', '<div class="info-detail">No new chapters today</div>', f)
    h = rwm(h, f)
    return h

def flu(h, f):
    h = must(h, '<div class="activity-sub">From Chapter 11 — Ch. 6–11</div>', '<div class="activity-sub">From Chapter 11</div>', f)
    h = must(h, "Read Jemmy's thoughts fast and amazed. The prince should sound cold and slow. Read Billy's voice loud and angry. Make the prince's last line calm and stubborn.",
               "<strong>How to read it:</strong> Read Jemmy's thoughts fast and amazed. Make the prince sound cold and slow. Read Billy loud and angry. Read the prince's last line calm and stubborn.", f)
    h = must(h, "<strong>Read with expression.</strong> Read it a third time. Let your voice show the feeling — read Billy's voice loud and angry.",
               '<strong>Read with expression.</strong> Read it a third time. Use the voices from <em>How to read it</em>.', f)
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
    io.open(os.path.join(HERE, 'how_wk19.json'), 'w', encoding='utf-8').write(json.dumps(how, ensure_ascii=False, indent=1))
    print('reused:', sorted(k for k in USED if k in WK18))
    print('new clips:', sorted(how))
