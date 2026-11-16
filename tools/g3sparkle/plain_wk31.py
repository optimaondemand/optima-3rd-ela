#!/usr/bin/env python3
"""Week 31 plain-language pass (Paired Texts: The Courage to Act; extension pages lesson-31-*-ext.html).

Same rules as plain_wk18-30 (Bethany, Nov 8 2026). Reads ~/g3w31/pristine-orig (the week 31 files after
acc_wk31.py), writes ~/g3w31/pristine. Every replacement is asserted. Re-runnable. No fluency page this week."""
import io, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC, DST = os.path.expanduser('~/g3w31/pristine-orig'), os.path.expanduser('~/g3w31/pristine')
DAYS = ['lesson-31-%d-ext.html' % d for d in (1, 2, 3, 4)]

OLD = {}
for w in range(18, 31):
    for k, v in json.load(io.open(os.path.join(HERE, 'how_wk%d.json' % w), encoding='utf-8')).items(): OLD.setdefault(k, v)
NEW = {
 'read-t1':     'Read Text 1 below. Keep your lens in mind. Then answer the three questions.',
 'read-t2':     'Read Text 2 below. It is a made-up story. Keep your lens in mind. Then answer the three questions.',
 'look-texts':  'There is no new text today. Read both texts again. Then answer the questions below.',
 'qtext':       'Answer the question in full sentences. Use details from the text.',
 'qboth':       'Answer the question in full sentences. Use details from both texts.',
 'talk':        'Ask someone at home the question. Listen all the way to the end and ask one question. Then write what you learned in the box.',
 'rwm-text':    'Read the sentence from the text. Then do the three parts in order. Write one sentence in each box.',
 'morph-ps1':   'Read the word parts and their examples. Think about the three questions, then tap See what was hiding. Last, type the missing part of each word and tap Check My Work.',
 'gram-spiral1': 'Read the sentence in The Rule box. Think about the questions, then tap Now check your thinking. Then tap all six words in the passage that need fixing. For a missing comma, tap the word before it. Last, answer the question in the box.',
 'spell-ps1':   'Think about the questions, then tap Now name the pattern. Last, tap each of the eight words, and tap its column: prefix at the front or suffix at the end.',
 'poem-moon':   'Read the poem out loud. What are the fish-ponds compared to? Then make up a short poem of your own and say it out loud. You do not need to write it.',
 'gram-types2': 'Read the four sentences and think about the questions, then tap Now check your thinking. Then tap the four words in the passage that are wrong. For a missing comma, tap the word before it. Last, answer the question in the box.',
 'spell-split2': 'Read the rule. Tap every word with three or more syllables. Then read how each word splits into its parts.',
 'poem-name':   'Read the poem again. Make up a poem of your own and say it out loud. Then say which form you chose and one figure of speech you used.',
 'vsentence-yr': 'Choose one word. Write one sentence that uses it to tell about a moment from a book you read this year.',
 'ww-c1':       'Read Clara’s before and after. Then plan in the box: what Text 1 says courage is, a character who shows it, and your claim.',
 'ww-c2':       'Read Clara’s opening. Then write your opening: name both texts, say what they agree on, and say how they are different.',
 'ww-c3':       'Read Clara’s draft. Then write one paragraph about each text, and one sentence that connects them.',
 'ww-c4':       'Read Clara’s closing. Then write your whole comparison in the box: opening, two paragraphs and a closing. Check your capitals and end marks.',
 'row':         'Read the word on the boat. Tap the right answer. Each right answer is one pull on the oars.',
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

LI_OLD = ('<li><strong>Name the shared topic:</strong> Both texts are about the same thing &mdash; say what it is.</li>',
          '<li><strong>Note what each author chose to show:</strong> Two writers pick different moments, facts, and people.</li>',
          '<li><strong>Explain what makes the messages alike or different:</strong> Same topic does not always mean same message.</li>')
LI_NEW = ('<li><strong>Name the shared topic:</strong> Both texts are about the same thing. Say what it is.</li>',
          '<li><strong>Notice what each author shows:</strong> Each writer picks different moments, facts and people.</li>',
          '<li><strong>Say what is alike and different:</strong> Two texts can share a topic and still say different things about it.</li>')
READT = {1: ('📖 Read: Text 1', 'What Is Courage?', 'read-t1',
             'Read Text 1 below. Ask: What does this author say courage is? What examples does the author give?'),
         2: ('📖 Read: Text 2', 'The Choice at the Bridge', 'read-t2',
             'Read Text 2 below. It is a made-up story. Ask: How does the author show that Mira is brave without using the word brave? How does that fit what Text 1 said?'),
         3: ('📖 Look Back: both texts', 'No new text today', 'look-texts',
             'There is no new text today. Read both texts again and collect details for your comparison.'),
         4: ('📖 Look Back: both texts', 'No new text today', 'look-texts',
             'There is no new text today. Read both texts again. Then finish your comparison.')}
QS = {1: ['qtext', 'qtext', 'qbook'], 2: ['qtext', 'qboth', 'qboth'], 3: ['qtext', 'qboth', 'qbook'], 4: ['qboth', 'qboth', 'qbook']}
WW = {1: 'ww-c1', 2: 'ww-c2', 3: 'ww-c3', 4: 'ww-c4'}
RCALL = r'(<div class="callout callout-info"><span class="callout-icon">📖</span><p style="white-space:pre-line;">)(Today you .*?)(</p></div>)'

def common(h, f, d):
    h = head(h, '📚 What Good Readers Do', f, sub='What to watch for while you read', slug='readers')
    for a, b in zip(LI_OLD, LI_NEW): h = must(h, a, b, f)
    h = must(h, '<p>Good readers <strong>compare how two authors present the same topic</strong>. Two writers can tell you about courage and still leave you with very different ideas about what it means.</p>',
               '<p>Good readers <strong>compare how two authors write about the same topic</strong>. Two writers can both write about courage and still leave you with different ideas about it.</p>', f)
    h = must(h, '<p class="socratic-q"><strong>Compare how two authors present the same topic or theme.</strong></p>',
               '<p class="socratic-q"><strong>Compare how two authors write about the same topic.</strong></p>', f)
    h = h.replace('<p class="socratic-q">As you read today, ask yourself: ', '<p class="socratic-q">Ask yourself: ')
    h = must(h, "<div class=\"thinking-stop\">💭 Keep this question in your mind as you read — you'll answer it in the Reading tab.</div>", '', f)
    h = head(h, '✏️ Daily Oral Language', f, sub='Study the model. Then fix a sentence.', slug='dol')
    h = must(h, '<p>The first sentence is <strong>correct</strong>. Tap the highlighted words to see what is done right. Then use the model to fix the second sentence.</p>', '', f)
    h = must(h, 'Your mind is warmed up. Let&rsquo;s sharpen your words and skills.', 'Next: word study.', f)
    h = must(h, 'Words and skills sharpened. Time to open the book.', 'Next: reading.', f)
    h = must(h, 'Great reading work! Now bring your thinking to the assignment.', 'Next: turn in your work.', f)
    t, sub, slug, intro = READT[d]
    h = head(h, 'Reading: Week 31', f, sub=sub, slug=slug, newtitle=t)
    h = resub(h, RCALL, lambda m: m.group(1) + intro + m.group(3), f)
    for e in ('Use details from the text in your answer.', 'Use details from both texts in your answer.', 'Use one detail from the book you choose.'):
        h = h.replace('<div class="textbox-prompt">%s</div>' % e, '')
    qs = re.findall(r'activity-title">(Q[123] — [^<]*)<', h); assert len(qs) == 3, (f, qs)
    for q, s in zip(qs, QS[d]): h = head(h, q, f, slug=s)
    if d == 4: h = head(h, 'Q4 — Talk It Over', f, slug='talk')
    h = must(h, '<div class="activity-title">📖 Chapter Thinking</div><div class="activity-sub">Your reading responses are saved from the Reading tab.</div>',
               '<div class="activity-title">📖 Reading Answers</div><div class="activity-sub">Your answers from the Reading tab</div>', f)
    h = must(h, 'Your chapter answers were saved on the Reading tab. They will appear in your gathered work below.',
               'Your answers on the Reading tab show in your work below.', f)
    h = must(h, '<div class="activity-title">🔤 Word Study Connection</div><div class="activity-sub">Your morphology response from the Word Study tab.</div>',
               '<div class="activity-title">🔤 Word Study Check</div><div class="activity-sub">The word part work on the Word Study tab</div>', f)
    h = must(h, 'Your morphology answer was saved on the Word Study tab. It will appear in your gathered work below.',
               'Finish the word part work on the Word Study tab. It shows in your work below.', f)
    h = resub(h, r'\s*<div class="callout callout-info" style="background:#E8F1E8;border-color:#A8C8A8;margin-bottom:10px;padding:10px 14px;"><span class="callout-icon">📝</span><p style="font-size:14px;"><strong>Now you try\.</strong>.*?</p></div>', '', f)
    h = head(h, 'Writer&rsquo;s Workshop', f, slug=WW[d])
    return h

def rwm(h, f):
    h = resub(h, r'<div class="rwm-header">📖 RWM (?:&mdash;|—) Read like a Reader, Read like a Writer, Mimic</div>',
               '<div class="rwm-header">📖 Read Like a Writer</div>\n' + do_line('rwm-text'), f)
    h = h.replace("{ title: '📖 RWM — READ LIKE A READER / WRITER / MIMIC'", "{ title: '📖 READ LIKE A WRITER'")
    for a, b in (('Read like a Reader', 'Read like a reader'), ('Read like a Writer', 'Read like a writer'), ('Mimic', 'Write your own')):
        h = h.replace('data-label="RWM &mdash; %s"' % a, 'data-label="%s"' % b).replace('data-label="RWM — %s"' % a, 'data-label="%s"' % b)
    return h

GRAM = '✏️ Grammar: Grammar spiral review'
SPELL = '🔠 Spelling: Multisyllabic decoding review'
MORPH = '🌱 Morphology: prefixes and suffixes'
BEFORE_SP = '<div class="callout callout-info" style="margin-bottom:14px;"><span class="callout-icon">&#x1F5C2;&#xFE0F;</span><p>Before you start: split, then spell one beat at a time.</p></div>'
LOWELL_NOTE = 'You have four forms to choose from and three tools to use inside them. Lowell&rsquo;s poem is free verse using one big metaphor &mdash; the fish-ponds have <strong>backs</strong> and <strong>dragon scales</strong>. That is the combination you are aiming for: a shape, plus at least one figure of speech.'

def day1(h, f):
    h = common(h, f, 1)
    h = head(h, '🌱 Morphology: Morphology review: prefixes and suffixes', f, sub='Word parts from the whole year', slug='morph-ps1', newtitle='🌱 Morphology: prefixes and suffixes')
    h = must(h, '<p>Prefixes at the front, suffixes at the end, base words in between.</p>', '<p>A prefix goes at the front. A suffix goes at the end. The base word is in the middle.</p>', f)
    h = must(h, '<p>Fill in the missing part after the prefix to build the word.</p>', '<p>Type the missing part to build each word.</p>', f)
    h = head(h, '🔤 Vocabulary: Decode &amp; Discover', f, sub='Three words about courage', slug='vocabcloze', newtitle='🔤 Vocabulary')
    h = head(h, GRAM, f, sub='Mistakes from the whole year', slug='gram-spiral1', newtitle='✏️ Grammar: Year review')
    h = must(h, '<strong>Your turn.</strong> Tap <strong>every</strong> word in the passage that needs fixing. The passage only finishes when you have found them all &mdash; count first, then start tapping. Everything you learned this year is in play here.',
               '<strong>Your turn.</strong> Six words need fixing. Tap all six.', f)
    h = head(h, SPELL, f, sub='Prefix or suffix?', slug='spell-ps1', newtitle='🔠 Spelling: Long words')
    h = must(h, '<p>Sort each word: does it have a prefix at the front or a suffix at the end?</p>', '<p><strong>Sort the Words!</strong></p>', f)
    return h

def day2(h, f):
    h = common(h, f, 2)
    h = head(h, '🪶 Poetry', f, sub='Find the metaphor', slug='poem-moon')
    h = must(h, LOWELL_NOTE, 'Lowell&rsquo;s poem is <strong>free verse</strong> (no set rhyme or line length) with one big <strong>metaphor</strong>: the fish-ponds have <strong>backs</strong> and <strong>dragon scales</strong>.', f, n=1)
    h = must(h, 'Before you write: which form will you choose, and why that one?', 'What would you write a poem about? Which form would fit it best?', f)
    h = head(h, MORPH, f, sub='Match each word to its meaning.', slug='morph2')
    h = must(h, '<p>Before you start: find the word part, then read what is left.</p>', '<p>Find the prefix or suffix in each word. Then read what is left.</p>', f)
    h = must(h, '<strong>Practice: Match the Word to Its Meaning!</strong> Tap a word, then tap what it means.', '<strong>Match the Word to Its Meaning!</strong>', f)
    h = head(h, '🔤 Vocabulary: Identify &amp; Match', f, sub='Four words about courage', slug='vmatch', newtitle='🔤 Vocabulary')
    h = resub(h, callout('🎯', r'<strong>Vocabulary Match:</strong> Tap a word, then tap its meaning\. Use what you know from your reading\.'), '', f)
    h = head(h, GRAM, f, sub='Three kinds of sentences', slug='gram-types2', newtitle='✏️ Grammar: Year review')
    h = must(h, '<p>Identify the key word or pattern in each sentence. Think: what rule does it follow?</p>', '<p>Is each sentence simple, compound or complex? Look for <em>and</em>, <em>although</em> and <em>because</em>.</p>', f)
    h = must(h, '<strong>Your turn.</strong> Same job, but the mistakes are not all the same kind this time. Tap <strong>every</strong> word that is wrong.',
               '<strong>Your turn.</strong> Tap the four words that are wrong.', f)
    h = head(h, SPELL, f, sub='Split long words', slug='spell-split2', newtitle='🔠 Spelling: Long words')
    h = must(h, BEFORE_SP, '', f)
    h = rwm(h, f)
    return h

def day3(h, f):
    h = common(h, f, 3)
    h = head(h, MORPH, f, sub='Build four words.', slug='morph3')
    h = must(h, '<p>Before you start: read the parts aloud, push them together, then write the word.</p>', '<p>Say each part out loud. Then say them together as one word.</p>', f)
    h = must(h, '<strong>Build the word.</strong> Put the parts together and type what they make.', '<strong>Build the word.</strong>', f)
    h = head(h, '🔤 Vocabulary: Use the Words', f, sub='Pick the word that fits.', slug='vselect', newtitle='🔤 Vocabulary')
    h = resub(h, callout('🎯', r'Choose the vocabulary word that best fits each sentence\.'), '', f)
    h = head(h, GRAM, f, sub='Fix a sentence like an editor.', slug='gram-edit3', newtitle='✏️ Grammar: Year review')
    h = must(h, '<strong>Now you.</strong> Fix everything. Count the changes as you go &mdash; there are more than five.',
               '<strong>Now you.</strong> Write this sentence the right way in the box. There are six changes to make.', f)
    h = head(h, SPELL, f, sub='Build long words one beat at a time.', slug='spell-tiles', newtitle='🔠 Spelling: Long words')
    h = must(h, BEFORE_SP, '', f)
    h = must(h, '<strong>Syllable Tiles!</strong> Four beats each &mdash; the longest words of the year. Tap the chunks <strong>in order</strong> to build the word. A chunk in the wrong place will not stick.',
               '<strong>Syllable Tiles!</strong> Four beats in each word.', f)
    h = rwm(h, f)
    return h

def day4(h, f):
    h = common(h, f, 4)
    h = head(h, '🪶 Poetry', f, sub='Make a poem and name its parts', slug='poem-name')
    h = must(h, LOWELL_NOTE, 'Lowell&rsquo;s poem is <strong>free verse</strong> (no set rhyme or line length) with one big <strong>metaphor</strong>: the fish-ponds have <strong>backs</strong> and <strong>dragon scales</strong>.', f, n=1)
    h = must(h, 'Write your poem in your journal. Then write one sentence underneath naming the form you chose and the figurative language you used.',
               'Make up your poem and say it out loud. Which form did you choose? Which figure of speech did you use?', f)
    h = head(h, MORPH, f, sub='Roll a word and tell what it means.', slug='morph-dice')
    h = must(h, '<p>Before you start: say what the word part does from memory, then roll.</p>', '<p>Before you roll, say out loud what one prefix or suffix from this year means.</p>', f)
    h = must(h, '<strong>Dice Roll Challenge!</strong> Roll a word, then say out loud what it means and how the word part changed it. Tap to check yourself.', '<strong>Dice Roll Challenge!</strong>', f)
    h = head(h, '🔤 Vocabulary: Justify Your Choice', f, sub='Use a word to tell about a book.', slug='vsentence-yr', newtitle='🔤 Vocabulary')
    h = resub(h, callout('🎯', r'Choose one word\. Write a sentence connecting it to a specific moment from one of the novels we read this year\.'), '', f)
    h = head(h, GRAM, f, sub='Fix it in passes.', slug='gram-pass', newtitle='✏️ Grammar: Year review')
    h = must(h, '<strong>Your turn.</strong> A full editing pass. Tap <strong>every</strong> word that needs fixing &mdash; capitals, apostrophes, commas, verb forms, anything from this year.',
               '<strong>Your turn.</strong> Tap all seven words that need fixing. For a missing comma, tap the word before it.', f)
    h = head(h, SPELL, f, sub='Roll a long word and split it.', slug='spell-beats4', newtitle='🔠 Spelling: Long words')
    h = must(h, BEFORE_SP, '', f)
    h = must(h, '<strong>Long Word Dice!</strong> Roll a word, say it out loud, decide &mdash; then tap to check yourself.', '<strong>Long Word Dice!</strong>', f)
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
    how = {k: DO[k] for k in sorted(USED) if k not in OLD}
    how['row'] = DO['row']
    io.open(os.path.join(HERE, 'how_wk31.json'), 'w', encoding='utf-8').write(json.dumps(how, ensure_ascii=False, indent=1))
    print('reused:', sorted(k for k in USED if k in OLD))
    print('new lines:', sorted(how))
