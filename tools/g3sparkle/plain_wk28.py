#!/usr/bin/env python3
"""Week 28 plain-language pass (The Lion, the Witch and the Wardrobe, Ch. 10-12; Narnia page template, as weeks 25-27).

Same rules as plain_wk18-27 (Bethany, Nov 8 2026). Reads ~/g3w28/pristine-orig (the week 28 files after
acc_wk28.py), writes ~/g3w28/pristine. Every replacement is asserted. Re-runnable."""
import io, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC, DST = os.path.expanduser('~/g3w28/pristine-orig'), os.path.expanduser('~/g3w28/pristine')
DAYS = ['lesson-28-1-lww.html', 'lesson-28-2-lww.html', 'lesson-28-3-lww.html', 'lesson-28-4-lww.html']
FLU = 'lesson-28-fluency.html'

OLD = {}
for w in range(18, 28):
    for k, v in json.load(io.open(os.path.join(HERE, 'how_wk%d.json' % w), encoding='utf-8')).items(): OLD.setdefault(k, v)
NEW = {
 'vsentence1012': 'Choose one word. Write one sentence that uses it to tell about something in Chapters 10 to 12.',
 'gram-apos1':   'Read The Rule box. Think about the question, then tap Now check your thinking. Then tap the five words in the passage that are missing an apostrophe. Last, answer the question in the box.',
 'gram-apos2':   'Read the four sentences and find what each apostrophe does. Tap Now check your thinking. Next, tap every word in the paragraph that is wrong. Last, answer the question in the box.',
 'gram-apos3':   'Read the before and after, then tap Check yourself. Put the apostrophes into the sentence in the gray box. Write it in the answer box, and label each apostrophe joined or belonging.',
 'gram-pass4':   'Think about the question, then tap Check yourself. Tap every word that needs fixing: capitals and apostrophes. Then tap See the answers, and answer the question in the box.',
 'spell-end1':   'Think about the questions, then tap Now name the pattern. Last, tap each of the eight words, and tap its column: doubled, dropped the e, or y to i.',
 'spell-end3':   'Read the rule. Decide which change each word needs. Then tap the card to build the new word.',
 'spell-end4':   'Tap Roll the dice. Say the word out loud, and decide which change it needs, or none. Then tap Check my answer. Roll all six words.',
 'poem-lim3':    'Read the limerick out loud. Check each line against the pattern A, A, B, B, A. Say your answer out loud. You do not need to write it.',
 'poem-limw':    'Make up your own limerick: five lines, where lines 1, 2 and 5 rhyme and lines 3 and 4 are short and rhyme. Say it out loud. You do not need to write it.',
 'look-ch1012':  'There are no new chapters today. Look back through Chapters 10 to 12 in your book. Then answer the three questions below.',
 'ww-sym1':      'Read Clara’s before and after. Then write two or three sentences about one symbol from Chapter 10: name it, say what it stands for, and why it matters.',
 'ww-sym2':      'Read Clara’s revision. Find one vague phrase in your symbol paragraph. Write it again with a precise idea and a word like represents, suggests or symbolizes.',
 'ww-sym3':      'Read Clara’s new sentence. Then add your symbol paragraph to your literary response, with a joining phrase like In addition or Lewis also uses.',
 'ww-sym4':      'Read Clara’s last sentence. Then polish your literary response, and add one closing sentence that says what the symbols do for the reader.',
 'thaw':         'Read the word on the snow patch. Tap the right answer. A right answer melts the snow, and a flower comes up.',
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

LI_OLD = ('    <li><strong>Notice what keeps coming back:</strong> An object, an image, or a word the author repeats on purpose.</li>\n'
          '    <li><strong>Ask what it stands for:</strong> A repeated thing usually points to a bigger idea &mdash; safety, hope, fear, or power.</li>\n'
          '    <li><strong>Check it against the story:</strong> Test your idea: does it hold up every time that thing appears?</li>')
LI_NEW = ('    <li><strong>Look for what comes back:</strong> Notice a thing or a word the author uses again and again.</li>\n'
          '    <li><strong>Ask what it stands for:</strong> What bigger idea could it be about, like hope or fear?</li>\n'
          '    <li><strong>Check it:</strong> Does your idea fit every time it shows up?</li>')
READT = {1: ('📖 Read: Ch. 10', 'The Spell Begins to Break', 'read-ch'), 2: ('📖 Read: Ch. 11', 'Aslan Is Nearer', 'read-ch'),
         3: ('📖 Read: Ch. 12', 'Peter’s First Battle', 'read-ch'), 4: ('📖 Look Back: Ch. 10–12', 'No new chapters today', 'look-ch1012')}
WW = {1: 'ww-sym1', 2: 'ww-sym2', 3: 'ww-sym3', 4: 'ww-sym4'}
CHECK = {1: ('I answered all 3 reading questions about symbols.', 'I answered all 3 chapter questions with details from the book.'),
         2: ('I answered all 3 reading questions with evidence.', 'I answered all 3 chapter questions with details from the book.'),
         3: ('I answered all 3 reading questions with text evidence.', 'I answered all 3 chapter questions with details from the book.'),
         4: None}

def common(h, f, d):
    h = head(h, '📚 What Good Readers Do', f, sub='What to watch for while you read', slug='readers')
    h = must(h, LI_OLD, LI_NEW, f)
    h = must(h, '<p>Good readers <strong>notice symbolism and repeated ideas</strong>. When an author brings the same object or image back again and again, it has started to stand for something bigger.</p>',
               '<p>Good readers <strong>notice symbols and repeated ideas</strong>. A <em>symbol</em> is a thing in a story that stands for a bigger idea.</p>', f)
    h = must(h, '<p class="socratic-q"><strong>Notice symbolism and repeated ideas.</strong></p>', '<p class="socratic-q"><strong>Look for things that stand for bigger ideas.</strong></p>', f)
    h = h.replace('<p class="socratic-q">As you read today, ask yourself: ', '<p class="socratic-q">Ask yourself: ')
    h = must(h, "<div class=\"thinking-stop\">💭 Keep this question in your mind as you read — you'll answer it in the Reading tab.</div>", '', f)
    h = head(h, '✏️ Daily Oral Language', f, sub='Study the model. Then fix a sentence.', slug='dol')
    h = must(h, '<p>The first sentence is <strong>correct</strong>. Tap the highlighted words to see what is done right. Then use the model to fix the second sentence.</p>', '', f)
    h = must(h, 'Your mind is warmed up. Let&rsquo;s sharpen your words and skills.', 'Next: word study.', f)
    h = must(h, 'Words and skills sharpened. Time to open the book.', 'Next: reading.', f)
    h = must(h, 'Great reading work! Now bring your thinking to the assignment.', 'Next: turn in your work.', f)
    t, sub, slug = READT[d]
    h = head(h, 'Reading: Ch. 10–12', f, sub=sub, slug=slug, newtitle=t)
    h = must(h, '<div class="textbox-prompt">Use evidence from the book in your answer.</div>', '', f, 3)
    for q in ('Q1 —', 'Q2 —', 'Q3 —'): h = head(h, q, f, slug='qbook')
    h = must(h, '<div class="activity-title">📖 Chapter Thinking</div><div class="activity-sub">Your reading responses are saved from the Reading tab.</div>',
               '<div class="activity-title">📖 Chapter Thinking</div><div class="activity-sub">Your answers from the Reading tab</div>', f)
    h = must(h, 'Your chapter answers were saved on the Reading tab. They will appear in your gathered work below.',
               'Your answers to Q1, Q2 and Q3 on the Reading tab show in your work below.', f)
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

GRAM = '✏️ Grammar: Apostrophes in contractions and possessives'
SPELL = '🔠 Spelling: Suffixes that change meaning'
MORPH = '🌱 Morphology: com- / con-'
BEFORE_SP = '<div class="callout callout-info" style="margin-bottom:14px;"><span class="callout-icon">&#x1F440;</span><p>Before you start: name the change each base word made.</p></div>'
SAME = '<p>Same rule as Day 1 &mdash; review: endings that change the base. This time, as you work, notice <em>why</em> each word follows the rule.</p>'
THREE = '<p>Three rules change the base word before the ending goes on: <strong>double</strong> the consonant, <strong>drop</strong> the silent e, or change <strong>y to i</strong>.</p>'
SORTL = '<p>Sort each word by which rule was used to build it.</p>'
def spell_common(h, f):
    h = must(h, BEFORE_SP, '', f)
    h = resub(h, r'\s*' + re.escape(SAME), '', f)
    return h
LIM_NOTE = ' You have met this poem before &mdash; it is the one from the hyperbole lesson. Now the shape has a name: a <strong>limerick</strong>.'
def day1(h, f):
    h = common(h, f, 1)
    h = head(h, MORPH, f, sub='Two word parts that both mean together', slug='morph-tele1')
    h = must(h, '<strong>Build the word.</strong> Put the parts together and type what they make.', '<strong>Build the word.</strong>', f)
    h = head(h, '🔤 Vocabulary: Decode &amp; Discover', f, sub='Three words from Ch. 10–12', slug='vocabcloze', newtitle='🔤 Vocabulary')
    h = head(h, GRAM, f, sub='An apostrophe has two jobs', slug='gram-apos1')
    h = must(h, "It's Aslan's roar that shakes the Witch's walls.", "It's Peter's sword, and the Witch's magic is weakening.", f)
    h = must(h, "It's = contraction (it is). Aslan's = possessive (roar of Aslan). Witch's = possessive (walls of the Witch).",
               "<em>It's</em> = it is: two words joined. <em>Peter's</em> = the sword belongs to Peter. <em>Witch's</em> = the magic belongs to the Witch.", f)
    h = resub(h, r'<strong>Your turn\.</strong> Tap <strong>every</strong> word in the passage that needs fixing\. The passage only finishes when you have found them all &mdash; count first, then start tapping\. Five words here are missing an apostrophe\.[^<]*',
               '<strong>Your turn.</strong> Five words in this passage are missing an apostrophe. Tap all five.', f)
    h = head(h, SPELL, f, sub='Three ways a base word changes before an ending', slug='spell-end1')
    h = must(h, '\n' + THREE + '\n' + SORTL, '', f)
    h = must(h, '<strong>Practice: Sort the words.</strong> Tap a word, then tap the column it belongs in.', '<strong>Sort the Words!</strong>', f)
    h = must(h, '<div class="activity-title">Q2 — Father Christmas</div>', '<div class="activity-title">Q2 — The Gifts</div>', f)
    return h

def day2(h, f):
    h = common(h, f, 2)
    h = head(h, '🪶 Poetry', f, sub='A funny poem with five lines', slug='poem-lim3')
    h = must(h, 'Does this fit the A&ndash;A&ndash;B&ndash;B&ndash;A pattern you wrote down last week? Check each line.', 'Does this fit the A&ndash;A&ndash;B&ndash;B&ndash;A pattern from last week? Check each line.', f)
    h = head(h, MORPH, f, sub='Match each word to its meaning.', slug='morph2')
    h = must(h, '<p>Before you start: find the word part, then read what is left.</p>', '<p>Find <strong>com-</strong> or <strong>con-</strong> in each word. Then look at what is left.</p>', f)
    h = must(h, '<strong>Practice: Match the Word to Its Meaning!</strong> Tap a word, then tap what it means.', '<strong>Match the Word to Its Meaning!</strong>', f)
    h = head(h, '🔤 Vocabulary: Identify &amp; Match', f, sub='Four words from Ch. 10–12', slug='vmatch', newtitle='🔤 Vocabulary')
    h = resub(h, callout('🎯', r'<strong>Vocabulary Match:</strong> Tap a word, then tap its meaning\. Use what you know from your reading\.'), '', f)
    h = head(h, GRAM, f, sub='Find what each apostrophe does. Then fix a paragraph.', slug='gram-apos2')
    h = must(h, '<p>Identify the key word or pattern in each sentence. Think: what rule does it follow?</p>', '<p>Find the apostrophes in each sentence. Does each one join two words, or show belonging?</p>', f)
    h = must(h, '<strong>Your turn.</strong> Same job, but the mistakes are not all the same kind this time. Tap <strong>every</strong> word that is wrong.',
               '<strong>Your turn.</strong> Tap <strong>every</strong> word that is wrong.', f)
    h = head(h, SPELL, f, slug='spell-beats2')
    h = spell_common(h, f)
    h = must(h, '<strong>Sound Detective!</strong> Each row names one change. Find the word it happened to.', '<strong>Change Detective!</strong>', f)
    h = rwm(h, f)
    return h

def day3(h, f):
    h = common(h, f, 3)
    h = head(h, MORPH, f, sub='Build four words.', slug='morph3')
    h = must(h, '<p>Before you start: read the parts aloud, push them together, then write the word.</p>', '<p>Say each part out loud. Then say them together as one word.</p>', f)
    h = must(h, '<strong>Build the word.</strong> Put the parts together and type what they make.', '<strong>Build the word.</strong>', f)
    h = head(h, '🔤 Vocabulary: Use the Words', f, sub='Pick the word that fits.', slug='vselect', newtitle='🔤 Vocabulary')
    h = resub(h, callout('🎯', r'Choose the vocabulary word that best fits each sentence\.'), '', f)
    h = head(h, GRAM, f, sub='Put the apostrophes in a sentence.', slug='gram-apos3')
    h = must(h, '<p>Someone has already edited the first one. Read the before and the after side by side before you touch the second.</p>', '<p>Read the before and the after.</p>', f)
    h = must(h, '<li>Did the editor change any of the writer&rsquo;s actual words?</li>', '<li>Which ones show belonging?</li>', f)
    h = must(h, '<p>Editing changes how the words are <em>presented</em> &mdash; never which words the writer chose. Every original word is still there.</p>',
               '<p>The editor added three apostrophes and changed no words. <em>Didn&rsquo;t</em> joins two words. <em>Lucy&rsquo;s</em> and <em>faun&rsquo;s</em> show belonging.</p>', f)
    h = must(h, '<p style="margin-top:10px;font-size:13px;color:#3A4A6B;"><strong>Notice:</strong> three apostrophes, doing two different jobs. <em>didn&rsquo;t</em> is two words joined; the other two show belonging.</p>', '', f)
    h = must(h, '<strong>Now you.</strong> Put the apostrophes where they belong, and say which job each one is doing.', '<strong>Now you.</strong> Fix this sentence.', f)
    h = head(h, SPELL, f, sub='Build the words.', slug='spell-end3')
    h = spell_common(h, f)
    h = must(h, '<strong>Change It Builder!</strong> Decide which of the three changes this word needs, then tap.', '<strong>Change It Builder!</strong>', f)
    h = rwm(h, f)
    return h

def day4(h, f):
    h = common(h, f, 4)
    h = head(h, '🪶 Poetry', f, sub='Make up your own limerick', slug='poem-limw')
    h = must(h, 'Write your own limerick. Five lines. Lines 1, 2 and 5 rhyme; lines 3 and 4 rhyme and are shorter. Start with &ldquo;There once was a ___.&rdquo;',
               'Start with &ldquo;There once was a ___.&rdquo; Say your limerick out loud.', f)
    h = head(h, MORPH, f, sub='Roll a word and tell what it means.', slug='morph-dice')
    h = must(h, '<p>Before you start: say what the word part does from memory, then roll.</p>', '<p>Before you roll, say out loud what <strong>com-</strong> and <strong>con-</strong> mean.</p>', f)
    h = must(h, '<strong>Dice Roll Challenge!</strong> Roll a word, then say out loud what it means and how the word part changed it. Tap to check yourself.', '<strong>Dice Roll Challenge!</strong>', f)
    h = head(h, '🔤 Vocabulary: Justify Your Choice', f, sub='Use a word to tell about the story.', slug='vsentence1012', newtitle='🔤 Vocabulary')
    h = resub(h, callout('🎯', r'Choose one word\. Write a sentence explaining how it connects to a specific moment in Ch\. 10–12\.'), '', f)
    h = head(h, GRAM, f, sub='Fix it in passes.', slug='gram-pass4')
    h = must(h, '<p>Everything you have learned this year is fair game in this passage. Read it like the person who has to fix it, not the person who wrote it.</p>',
               '<p>This passage needs capitals and apostrophes. Fix it like an editor.</p>', f)
    h = must(h, '<li>Now everything else &mdash; commas, verb forms, endings.</li>', '<li>Last, read it again to check.</li>', f)
    h = must(h, '<p>Work in passes, not all at once: capitals, then apostrophes, then the rest. Three quick trips through a passage beat one slow one &mdash; that is how an editor actually reads.</p>',
               '<p>Work in passes, not all at once: capitals first, then apostrophes. That is how an editor reads.</p>', f)
    h = must(h, '<strong>Your turn.</strong> A full editing pass. Tap <strong>every</strong> word that needs fixing &mdash; capitals, apostrophes, commas, verb forms, anything from this year.',
               '<strong>Your turn.</strong> Tap <strong>every</strong> word that needs fixing.', f)
    h = head(h, SPELL, f, sub='Roll a word and decide.', slug='spell-end4')
    h = must(h, BEFORE_SP, '', f)
    h = must(h, '\n' + THREE.replace('<p>', '      <p>') + '\n        ' + SORTL, '', f) if ('      ' + THREE) in h else must(h, THREE, '', f)
    if SORTL in h: h = must(h, SORTL, '', f)
    h = must(h, '<strong>Which Change Dice!</strong> Roll a word, say it out loud, decide &mdash; then tap to check yourself.', '<strong>Which Change Dice!</strong>', f)
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
    how['thaw'] = DO['thaw']
    io.open(os.path.join(HERE, 'how_wk28.json'), 'w', encoding='utf-8').write(json.dumps(how, ensure_ascii=False, indent=1))
    print('reused:', sorted(k for k in USED if k in OLD))
    print('new lines:', sorted(how))
