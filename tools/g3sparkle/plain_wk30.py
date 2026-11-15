#!/usr/bin/env python3
"""Week 30 plain-language pass (The Lion, the Witch and the Wardrobe, Ch. 16-17 + synthesis; Narnia page template, as weeks 25-28).

Same rules as plain_wk18-28 (Bethany, Nov 8 2026). Reads ~/g3w30/pristine-orig (the week 30 files after
acc_wk30.py), writes ~/g3w30/pristine. Every replacement is asserted. Re-runnable."""
import io, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC, DST = os.path.expanduser('~/g3w30/pristine-orig'), os.path.expanduser('~/g3w30/pristine')
DAYS = ['lesson-30-1-lww.html', 'lesson-30-2-lww.html', 'lesson-30-3-lww.html', 'lesson-30-4-lww.html']
FLU = 'lesson-30-fluency.html'

OLD = {}
for w in range(18, 30):
    for k, v in json.load(io.open(os.path.join(HERE, 'how_wk%d.json' % w), encoding='utf-8')).items(): OLD.setdefault(k, v)
NEW = {
 'morph-rev1':    'Read the word parts and their examples. Think about the three questions, then tap See if you cracked it. Last, type the missing part of each word and tap Check My Work.',
 'gram-cap5':     'Read the sentence in the Look box. Think about the questions, then tap Now check your thinking. Then tap the five words that need a capital letter. Last, answer the question in the box.',
 'spell-rev1':    'Think about the questions, then tap Now name the pattern. Last, tap each of the nine words, and tap its column: magic-e, vowel team, or prefix + base word.',
 'poem-3tools':   'Read the poem out loud. Find the fire that sings, and say what kind of figurative language it is. You do not need to write it.',
 'gram-4rules':   'Read the sentence and think about the four questions, then tap Check yourself. Tap every word that is wrong. For the missing comma, tap the word before it. Last, answer the question in the box.',
 'spell-syl2':    'Read the rule. Then tap every word in the two sentences that has a silent-e, vowel-team or r-controlled syllable.',
 'gram-edit3':    'Read the before and after, then tap Check yourself. Fix the sentence in the gray box. Write it in the answer box, and say what you changed.',
 'poem-label':    'Read the poem out loud. Find one metaphor, one personification and one hyperbole, and say each one out loud. You do not need to write it.',
 'vsentence-end': 'Choose one word. Write one sentence that tells how it connects to the ending and the theme.',
 'gram-pass6':    'Think about the questions, then tap Check yourself. Tap all five words that need fixing: capitals, apostrophes and a missing comma. Last, answer the question in the box.',
 'spell-syl4':    'Tap Roll the dice. Say the word out loud, split it, and name its syllable types. Then tap Check my answer. Roll all six words.',
 'look-book':     'There are no new chapters today. Look back through the whole book. Then answer the questions below.',
 'ww-fin1':       'Read Clara’s before and after. Then add two sentences to your response with proof from Chapter 16 or 17 that shows how the ending completes your theme.',
 'ww-fin2':       'Read Clara’s edit. Then check your response for capitals, apostrophes and commas, read it out loud once, and write the fixed version in the box.',
 'ww-fin3':       'Read Clara’s final changes. Then give your response a title, read it start to finish, and make one last improvement.',
 'ww-fin4':       'Read Clara’s last step. Then write your finished response in the box: a title, your theme, proof from three different chapters, and a closing.',
 'statues':       'Read the word on the statue. Tap the right answer. A right answer breathes life into the statue, and it fills with color.',
}
for k in NEW: assert k not in OLD, k
DO = dict(OLD); DO.update(NEW)
USED = set()
def do_line(slug):
    USED.add(slug)
    return '<p class="g3-do" data-say="%s"><b>What to do:</b> %s</p>' % (slug, DO[slug])

def must(h, old, new, f, n=1):
    c = h.count(old)
    if c != n: sys.exit('%s: expected %d of %r, found %d' % (f, n, old[:110], c))
    return h.replace(old, new)
def resub(h, pat, new, f, n=1, flags=re.S):
    h2, c = re.subn(pat, new, h, count=n, flags=flags)
    if c != n: sys.exit('%s: pattern %r matched %d' % (f, pat[:90], c))
    return h2
def head(h, title, f, sub=None, slug=None, newtitle=None):
    i = h.find('activity-title">' + title)
    if i < 0: sys.exit('%s: no activity %r' % (f, title))
    if sub is not None:
        m = re.compile(r'(<div class="activity-sub">)(.*?)(</div>|<script>)', re.S).search(h, i)
        h = h[:m.start(2)] + sub + h[m.end(2):]
    if newtitle:
        h = h[:i] + 'activity-title">' + newtitle + h[i + len('activity-title">' + title):]
    if slug:
        j = h.find('<div class="activity-body"', i)
        k = h.find('>', j) + 1
        h = h[:k] + '\n' + do_line(slug) + h[k:]
    return h
def callout(icon_re, text_re):
    return r'\s*<div class="callout callout-info"[^>]*><span class="callout-icon">' + icon_re + r'</span><p>' + text_re + r'</p></div>'

LI_OLD = ('    <li><strong>Reread the ending:</strong> Go back over the last pages slowly &mdash; endings are written carefully.</li>\n'
          '    <li><strong>Ask what the ending settles:</strong> What question from the beginning of the book finally gets answered?</li>\n'
          '    <li><strong>Connect it back to the start:</strong> The theme is usually the line between how the book opened and how it closed.</li>')
LI_NEW = ('    <li><strong>Reread the ending:</strong> Read the last pages again, slowly.</li>\n'
          '    <li><strong>Ask what the ending settles:</strong> What question from the start of the book finally gets an answer?</li>\n'
          '    <li><strong>Connect it back to the start:</strong> How is the end different from the beginning? That change points to the theme.</li>')
READT = {1: ('📖 Read: Ch. 16–17', 'What Happened About the Statues; The Hunting of the White Stag', 'read-ch'), 2: ('📖 Look Back: the whole book', 'No new chapters today', 'look-book'),
         3: ('📖 Look Back: the whole book', 'No new chapters today', 'look-book'), 4: ('📖 Look Back: the whole book', 'No new chapters today', 'look-book')}
WW = {1: 'ww-fin1', 2: 'ww-fin2', 3: 'ww-fin3', 4: 'ww-fin4'}
CHECK = {1: ('I answered all 3 reading questions using evidence from Ch. 16–17.', 'I answered all 3 chapter questions with details from the book.'), 2: None, 3: None, 4: None}

def common(h, f, d):
    h = head(h, '📚 What Good Readers Do', f, sub='What to watch for while you read', slug='readers')
    h = must(h, LI_OLD, LI_NEW, f)
    h = must(h, '<p>Good readers pay attention to <strong>how the ending reveals the theme</strong>. The last chapter answers a question the first chapter asked, and that answer is usually the lesson.</p>',
               '<p>Good readers pay attention to <strong>how the ending reveals the theme</strong>. The end of a book often answers a question the beginning asked, and that answer is the big lesson.</p>', f)
    h = must(h, '<p class="socratic-q"><strong>Explain how the ending reveals theme.</strong></p>', '<p class="socratic-q"><strong>Look at how the ending shows the big lesson.</strong></p>', f)
    h = h.replace('<p class="socratic-q">As you read today, ask yourself: ', '<p class="socratic-q">Ask yourself: ')
    h = must(h, "<div class=\"thinking-stop\">💭 Keep this question in your mind as you read — you'll answer it in the Reading tab.</div>", '', f)
    h = head(h, '✏️ Daily Oral Language', f, sub='Study the model. Then fix a sentence.', slug='dol')
    h = must(h, '<p>The first sentence is <strong>correct</strong>. Tap the highlighted words to see what is done right. Then use the model to fix the second sentence.</p>', '', f)
    h = must(h, 'Your mind is warmed up. Let&rsquo;s sharpen your words and skills.', 'Next: word study.', f)
    h = must(h, 'Words and skills sharpened. Time to open the book.', 'Next: reading.', f)
    h = must(h, 'Great reading work! Now bring your thinking to the assignment.', 'Next: turn in your work.', f)
    t, sub, slug = READT[d]
    h = head(h, 'Reading: Ch. 16–17 + Synthesis', f, sub=sub, slug=slug, newtitle=t)
    n = h.count('<div class="textbox-prompt">Use evidence from the book in your answer.</div>'); assert n >= 3, (f, n)
    h = h.replace('<div class="textbox-prompt">Use evidence from the book in your answer.</div>', '')
    for q in ('Q1 —', 'Q2 —', 'Q3 —') + (('Q4 —',) if d == 3 else ()): h = head(h, q, f, slug='qbook')
    h = must(h, '<div class="activity-title">📖 Chapter Thinking</div><div class="activity-sub">Your reading responses are saved from the Reading tab.</div>',
               '<div class="activity-title">📖 Chapter Thinking</div><div class="activity-sub">Your answers from the Reading tab</div>', f)
    h = must(h, 'Your chapter answers were saved on the Reading tab. They will appear in your gathered work below.',
               'Your answers on the Reading tab show in your work below.', f)
    h = must(h, '<div class="activity-title">🔤 Word Study Connection</div><div class="activity-sub">Your morphology response from the Word Study tab.</div>',
               '<div class="activity-title">🔤 Word Study Check</div><div class="activity-sub">The word part work on the Word Study tab</div>', f)
    h = must(h, 'Your morphology answer was saved on the Word Study tab. It will appear in your gathered work below.',
               'Finish the word part work on the Word Study tab. It shows in your work below.', f)
    if CHECK[d]: h = must(h, CHECK[d][0], CHECK[d][1], f)
    h = resub(h, r'\s*<div class="callout callout-info" style="background:#E8F1E8;border-color:#A8C8A8;margin-bottom:10px;padding:10px 14px;"><span class="callout-icon">📝</span><p style="font-size:14px;"><strong>Now you try\.</strong>.*?</p></div>', '', f)
    h = head(h, 'Writer&rsquo;s Workshop', f, slug=WW[d])
    return h

def rwm(h, f):
    h = resub(h, r'<div class="rwm-header">📖 RWM (?:&mdash;|—) Read like a Reader, Read like a Writer, Mimic</div>',
               '<div class="rwm-header">📖 Read Like a Writer</div>\n' + do_line('rwm'), f)
    h = h.replace("{ title: '📖 RWM — READ LIKE A READER / WRITER / MIMIC'", "{ title: '📖 READ LIKE A WRITER'")
    for a, b in (('Read like a Reader', 'Read like a reader'), ('Read like a Writer', 'Read like a writer'), ('Mimic', 'Write your own')):
        h = h.replace('data-label="RWM &mdash; %s"' % a, 'data-label="%s"' % b).replace('data-label="RWM — %s"' % a, 'data-label="%s"' % b)
    return h

GRAM = '✏️ Grammar: Editing for punctuation and capitalization'
SPELL = '🔠 Spelling: Cumulative spelling pattern review'
MORPH = '🌱 Morphology: roots and bases from the year'
BEFORE_SP = '<div class="callout callout-info" style="margin-bottom:14px;"><span class="callout-icon">&#x1F5C2;&#xFE0F;</span><p>Before you start: name the pattern before you spell the word.</p></div>'
WIDER = '<p>Review: use word-part knowledge to decode and spell unfamiliar words. Ask: What syllable type is this — closed, open, magic-e, vowel team, r-controlled? Then add prefixes and roots on top.</p>'

def spell_common(h, f):
    h = must(h, BEFORE_SP, '', f)
    return h

def day1(h, f):
    h = common(h, f, 1)
    h = head(h, '🌱 Morphology: Review roots and bases from the year', f, sub='Word parts from the whole year', slug='morph-rev1', newtitle='🌱 Morphology: roots from the year')
    h = head(h, '🔤 Vocabulary: Decode &amp; Discover', f, sub='Three words from Ch. 16–17', slug='vocabcloze', newtitle='🔤 Vocabulary')
    h = head(h, GRAM, f, sub='Which words need a capital letter?', slug='gram-cap5', newtitle='✏️ Grammar: Editing')
    h = must(h, '<p>Read this passage the way the person who has to fix it would read it &mdash; hunting, not following the story.</p>', '<p>Read it like an editor: hunt for the mistakes.</p>', f)
    h = must(h, '<strong>Your turn.</strong> Tap <strong>every</strong> word in the passage that needs a capital letter. The passage only finishes when you have found them all.',
               '<strong>Your turn.</strong> Five words need a capital letter. Tap all five.', f)
    h = head(h, SPELL, f, sub='Every spelling pattern from the year', slug='spell-rev1', newtitle='🔠 Spelling: Patterns from the year')
    h = must(h, WIDER, '', f)
    h = must(h, '<p>Sort these words into the correct spelling pattern group.</p>', '<p><strong>Sort the Words!</strong></p>', f)
    return h

def day2(h, f):
    h = common(h, f, 2)
    h = head(h, '🪶 Poetry', f, sub='Three tools in one poem', slug='poem-3tools')
    h = head(h, MORPH, f, sub='Match each word to its meaning.', slug='morph2', newtitle='🌱 Morphology: roots from the year')
    h = must(h, '<p>Before you start: find the word part, then read what is left.</p>', '<p>Find the root in each word. Then look at the part in front of it.</p>', f)
    h = must(h, '<strong>Practice: Match the Word to Its Meaning!</strong> Tap a word, then tap what it means.', '<strong>Match the Word to Its Meaning!</strong>', f)
    h = head(h, '🔤 Vocabulary: Identify &amp; Match', f, sub='Four words from Ch. 16–17', slug='vmatch', newtitle='🔤 Vocabulary')
    h = resub(h, callout('🎯', r'<strong>Vocabulary Match:</strong> Tap a word, then tap its meaning\. Use what you know from your reading\.'), '', f)
    h = head(h, GRAM, f, sub='Four mistakes, four different rules', slug='gram-4rules', newtitle='✏️ Grammar: Editing')
    h = must(h, '<strong>Your turn.</strong> Four mistakes, four different rules. Tap <strong>every</strong> word that is wrong &mdash; for the missing comma, tap the word it should come after.',
               '<strong>Your turn.</strong> Tap <strong>every</strong> word that is wrong. For the missing comma, tap the word before it.', f)
    h = head(h, SPELL, f, sub='Find the syllable types.', slug='spell-syl2', newtitle='🔠 Spelling: Patterns from the year')
    h = spell_common(h, f)
    h = must(h, '<p>For each word, identify the spelling pattern: magic-e, vowel team, or prefix + base.</p>', '<p>Here is the pattern in each word.</p>', f)
    h = rwm(h, f)
    return h

def day3(h, f):
    h = common(h, f, 3)
    h = head(h, MORPH, f, sub='Build four words.', slug='morph3', newtitle='🌱 Morphology: roots from the year')
    h = must(h, '<p>Before you start: read the parts aloud, push them together, then write the word.</p>', '<p>Say each part out loud. Then say them together as one word.</p>', f)
    h = must(h, '<strong>Build the word.</strong> Put the parts together and type what they make.', '<strong>Build the word.</strong>', f)
    h = head(h, '🔤 Vocabulary: Use the Words', f, sub='Pick the word that fits.', slug='vselect', newtitle='🔤 Vocabulary')
    h = resub(h, callout('🎯', r'Choose the vocabulary word that best fits each sentence\.'), '', f)
    h = head(h, GRAM, f, sub='Fix a sentence like an editor.', slug='gram-edit3', newtitle='✏️ Grammar: Editing')
    h = must(h, '<strong>Now you.</strong> Nobody has touched this one. Copy it into the box and write it out correctly &mdash; every capital, every apostrophe, every comma.',
               '<strong>Now you.</strong> Write this sentence the right way in the box: every capital, apostrophe and comma.', f)
    h = head(h, SPELL, f, sub='Spell words from memory.', slug='spell-root3', newtitle='🔠 Spelling: Patterns from the year')
    h = spell_common(h, f)
    h = must(h, '<strong>Cover, Write, Check!</strong> Every syllable type from the year. Look hard at the word, cover it with your hand, write it in your notebook, <em>then</em> tap to check every letter.', '<strong>Cover, Write, Check!</strong>', f)
    h = rwm(h, f)
    return h

def day4(h, f):
    h = common(h, f, 4)
    h = head(h, '🪶 Poetry', f, sub='Find all three tools', slug='poem-label')
    h = must(h, 'Copy the six lines into your journal. Label every place Teasdale uses metaphor, personification, or hyperbole. Some lines may have more than one.',
               'Which line is a metaphor? Which is personification? Which is hyperbole? Say each one out loud.', f)
    h = head(h, MORPH, f, sub='Roll a word and tell what it means.', slug='morph-dice', newtitle='🌱 Morphology: roots from the year')
    h = must(h, '<p>Before you start: say what the word part does from memory, then roll.</p>', '<p>Before you roll, say out loud what one root from this year means.</p>', f)
    h = must(h, '<strong>Dice Roll Challenge!</strong> Roll a word, then say out loud what it means and how the word part changed it. Tap to check yourself.', '<strong>Dice Roll Challenge!</strong>', f)
    h = head(h, '🔤 Vocabulary: Justify Your Choice', f, sub='Use a word to tell about the ending.', slug='vsentence-end', newtitle='🔤 Vocabulary')
    h = resub(h, callout('🎯', r'Choose one word\. Write a sentence explaining how it connects to the novel\'s ending and its theme\.'), '', f)
    h = head(h, GRAM, f, sub='Fix it in passes.', slug='gram-pass6', newtitle='✏️ Grammar: Editing')
    h = must(h, '<strong>Your turn.</strong> A full editing pass. Tap <strong>every</strong> word that needs fixing &mdash; there are five, and for the missing comma tap the word it should come after.',
               '<strong>Your turn.</strong> Tap all five words that need fixing. For the missing comma, tap the word before it.', f)
    h = head(h, SPELL, f, sub='Roll a word and split it.', slug='spell-syl4', newtitle='🔠 Spelling: Patterns from the year')
    h = spell_common(h, f)
    h = must(h, '<strong>Syllable Review Dice!</strong> Roll a word, say it out loud, decide &mdash; then tap to check yourself.', '<strong>Syllable Review Dice!</strong>', f)
    h = rwm(h, f)
    return h

FIX = {DAYS[0]: day1, DAYS[1]: day2, DAYS[2]: day3, DAYS[3]: day4}
if __name__ == '__main__':
    os.makedirs(DST, exist_ok=True)
    for f, fn in FIX.items():
        h = io.open(os.path.join(SRC, f), encoding='utf-8').read()
        o = h.count('<div') - h.count('</div')
        h = fn(h, f)
        assert h.count('<div') - h.count('</div') == o, (f, o, h.count('<div') - h.count('</div'))
        io.open(os.path.join(DST, f), 'w', encoding='utf-8').write(h)
        print('ok', f)
    h = io.open(os.path.join(SRC, FLU), encoding='utf-8').read()
    o = h.count('<div') - h.count('</div')
    h = must(h, '<div class="activity-title">The 5-Step Fluency Routine</div><div class="activity-sub">Work through these in order every time.</div>',
               '<div class="activity-title">🎯 The 4 Steps</div><div class="activity-sub">Do these in order.</div>', FLU)
    h = head(h, '🎯 The 4 Steps', FLU, slug='flu')
    h = must(h, '📖 5 Steps', '📖 4 Steps', FLU, 2)
    h = must(h, 'Words ready. Now walk through the 5-step routine.', 'Next: the 4 steps.', FLU)
    assert h.count('<div') - h.count('</div') == o
    io.open(os.path.join(DST, FLU), 'w', encoding='utf-8').write(h)
    how = {k: DO[k] for k in sorted(USED) if k not in OLD}
    how['statues'] = DO['statues']
    io.open(os.path.join(HERE, 'how_wk30.json'), 'w', encoding='utf-8').write(json.dumps(how, ensure_ascii=False, indent=1))
    print('reused:', sorted(k for k in USED if k in OLD))
    print('new lines:', sorted(how))
