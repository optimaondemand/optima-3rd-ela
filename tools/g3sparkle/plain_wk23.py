#!/usr/bin/env python3
"""Week 23 plain-language pass (Medieval Nonfiction, part 1: four short articles, no novel).

Same rules as plain_wk18-22 (Bethany, Nov 8 2026). Reads ~/g3w23/pristine-orig
(the week 23 files after acc_wk23.py), writes ~/g3w23/pristine. Every
replacement is asserted. Re-runnable. No fluency page this week (Bethany, Nov 14)."""
import io, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC, DST = os.path.expanduser('~/g3w23/pristine-orig'), os.path.expanduser('~/g3w23/pristine')
DAYS = ['lesson-23-1-med.html', 'lesson-23-2-med.html', 'lesson-23-3-med.html', 'lesson-23-4-med.html']

OLD = {}
for w in (18, 19, 20, 21, 22):
    for k, v in json.load(io.open(os.path.join(HERE, 'how_wk%d.json' % w), encoding='utf-8')).items(): OLD.setdefault(k, v)
NEW = {
 'morph-trans1': 'Read the three words and their parts. Think about the three questions. Then tap See if you cracked it. Last, type the missing part of each word and tap Check My Work.',
 'gram-cap1':    'Read the two sentences and tap Now check your thinking. Then tap each name, and tap its column: a person, a place, or a title. Last, answer the question in the box.',
 'gram-cap2':    'Read the Remember box. Then tap every word that needs a capital letter. A name can be more than one word. Last, answer the question in the box.',
 'gram-cap3':    'Read the Remember box. Count the words in each sentence that need a capital, and type the number. Tap Check My Answers. Last, answer the question in the box.',
 'spell-vccv1':  'Say the words in Group A and Group B out loud. Think about the three questions, then tap See the Rule. Last, tap each of the eight words, and tap the group it belongs in.',
 'spell-vccv2':  'Read the rule. Then in each row, tap the one word with two consonants in the middle.',
 'spell-vccv3':  'Read the rule. Find the two consonants in the middle of each word. Then tap the word to split it.',
 'poem-hyper1':  'Read the poem out loud. Then think: how is this poem different from a lie? Say your answer out loud.',
 'poem-hyper2':  'Read the poem out loud again. Then make up one sentence of hyperbole about how long a school day feels. Say it out loud. You do not need to write it.',
 'read-art':     'Read the two Pause and Think questions first. Then read today’s article below. Think about your answers as you read. You do not write these answers.',
 'article':      'Read each question. Answer in full sentences. Use details from the article.',
 'rwm-art':      'Read the sentence from the article. Then do the three parts in order. Write one sentence in each box.',
 'ww-topic':     'Read how Clara made her topic smaller. Then write your own topic in the box: one thing about medieval life you want to explain.',
 'ww-notes':     'Read Clara’s notes. Write your research question. Then write two notes from today’s article and two from another article this week, with each article’s title.',
 'ww-plan':      'Read Clara’s plan. Then plan your paragraph in the box: a topic sentence, two details, and a closing sentence.',
 'ww-draft':     'Read Clara’s opening. Then write your topic sentence and at least one detail sentence in the box. Use your plan from Day 3.',
 'illuminate':   'Read the question. Tap the answer you think is right. A right answer paints the next part of the page.',
}
for k in NEW: assert k not in OLD, k
DO = dict(OLD); DO.update(NEW)
USED = set()
def do_line(slug):
    USED.add(slug)
    return '<p class="g3-do" data-say="%s"><b>What to do:</b> %s</p>' % (slug, DO[slug])

def must(h, old, new, f, n=1):
    c = h.count(old)
    if c != n: sys.exit('%s: expected %d of %r, found %d' % (f, n, old[:100], c))
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

ART = {1: 'Life in a Medieval Castle', 2: 'Servants and Apprentices', 3: 'Royal Courts: Power and Protocol', 4: 'What Did Medieval People Eat?'}
VOCSUB = {1: 'Four words from the castle article', 2: 'Four words about learning a trade', 3: 'Four words about royal courts', 4: 'Four words about medieval food'}

def common(h, f, day):
    h = must(h, '<div class="thinking-stop">💭 Think about this as you read today — you don\'t need to write anything here.</div>', '', f)
    h = head(h, '📚 What Good Readers Do', f, sub='What to watch for while you read', slug='readers')
    h = head(h, '✏️ Daily Oral Language', f, sub='Study the model. Then fix a sentence.', slug='dol')
    h = resub(h, r'\s*<p>The first sentence is <strong>correct</strong>\. Tap the parts you notice.*?</p>', '', f)
    h = must(h, 'Now that your mind is warmed up, let&rsquo;s sharpen your words and skills.', 'Next: word study.', f)
    h = must(h, 'Your words and skills are sharp. Time to open the book.', 'Next: reading.', f)
    h = must(h, 'You&rsquo;ve read the article and thought carefully. Now let&rsquo;s put your thinking into writing.', 'Next: answer the questions and turn in your work.', f)
    # reading tab
    h = must(h, '<p><strong>Novel Connection:</strong> You just finished reading <em>The Whipping Boy</em>, which is set in a medieval kingdom. This week we zoom OUT — instead of a story, we read informational texts about what life in the Middle Ages was actually like.</p>',
               '<p><strong>From story to facts:</strong> <em>The Whipping Boy</em> is a made-up story set long ago. This week you read true articles about real life in the Middle Ages.</p>', f)
    h = head(h, 'Pause &amp; Think', f, sub='Think about these while you read.', slug='read-art')
    h = must(h, '<div class="activity-title">%s</div>' % ART[day], '<div class="activity-title">📰 Read: %s</div>' % ART[day], f)
    # assignment
    h = head(h, '📰 Article Thinking', f, sub='Answer in full sentences. Use details from the article.', slug='article')
    h = must(h, '<div class="activity-title">🔤 Word Study Connection (Morphology)</div><div class="activity-sub">Your morphology response from the Word Study tab.</div>',
               '<div class="activity-title">🔤 Word Study Check</div><div class="activity-sub">The word part work on the Word Study tab</div>', f)
    h = must(h, 'Your morphology answer was saved on the Word Study tab. It will appear in your gathered work below.',
               'Finish the word part work on the Word Study tab. It shows in your work below.', f)
    h = h.replace('{ title: \'🔤 WORD STUDY CONNECTION (MORPHOLOGY)\'', '{ title: \'🔤 WORD STUDY CHECK\'')
    # Writer's Workshop
    h = must(h, 'Meet Today, our example writer', 'Meet Clara, our example writer', f)
    h = re.sub(r'(<strong>Today&rsquo;s focus:</strong> )Today: ', r'\1', h)
    h = re.sub(r'\s*<p style="font-size:14px;"><em>Today: [^<]*</em></p>', '', h)
    h = resub(h, r'\s*<div class="callout callout-info" style="background:#E8F1E8;border-color:#A8C8A8;margin:0 0 10px 0;padding:10px 14px;"><span class="callout-icon">📝</span><p style="font-size:14px;"><strong>Now you try\.</strong>.*?</p></div>', '', f)
    h = head(h, 'Writer&rsquo;s Workshop', f, slug=['ww-topic', 'ww-notes', 'ww-plan', 'ww-draft'][day - 1])
    # vocabulary
    h = head(h, '🔤 Vocabulary', f, slug='vocabcloze')
    h = must(h, '<div class="activity-sub">Words from this week\'s articles.</div>', '<div class="activity-sub">%s</div>' % VOCSUB[day], f)
    return h

def rwm(h, f):
    h = must(h, '<div class="rwm-header">📖 RWM &mdash; Read like a Reader, Read like a Writer, Mimic</div>',
               '<div class="rwm-header">📖 Read Like a Writer</div>\n' + do_line('rwm-art'), f)
    h = h.replace("{ title: '📖 RWM — READ LIKE A READER / WRITER / MIMIC'", "{ title: '📖 READ LIKE A WRITER'")
    h = h.replace('data-label="RWM &mdash; Read like a Reader"', 'data-label="Read like a reader"')
    h = h.replace('data-label="RWM &mdash; Read like a Writer"', 'data-label="Read like a writer"')
    h = h.replace('data-label="RWM &mdash; Mimic"', 'data-label="Write your own"')
    return h

LI_OLD = ('      <li><strong>Read the whole article first:</strong> The central idea is built across the page, not stated in the first line.</li>\n'
          '      <li><strong>Find what the article keeps returning to:</strong> That repeated point is the central idea.</li>\n'
          '      <li><strong>Collect the facts that support it:</strong> Write down two or three details that prove the big idea.</li>')
def lis(*xs): return '\n'.join('      <li><strong>%s</strong> %s</li>' % x for x in xs)
FACTS = ('Collect the facts:', 'Find two details that prove the big idea.')
LI = {
 1: lis(('Read the whole article first:', 'The big idea is spread across the page, not only in the first line.'),
        ('Find what it keeps coming back to:', 'The point the article repeats is the central idea.'), FACTS),
 2: lis(('Look at each paragraph:', 'Ask what each paragraph is mostly about.'),
        ('Put them together:', 'Say one big idea that fits both paragraphs.'), FACTS),
 3: lis(('Use the clues:', 'When a word is new, read the sentences around it.'),
        ('Find the big point:', 'Ask what the author most wants you to know about royal courts.'), FACTS),
 4: lis(('Find the two sides:', 'Look for words like most and very differently that split rich from poor.'),
        ('Find the big point:', 'Ask what the two sides show about food in the Middle Ages.'), FACTS),
}
WG = {
 1: ("<p>Good readers of nonfiction look for the central idea — the most important point the author is making. As you read today, ask: what is the ONE big idea this article keeps coming back to?</p>",
     '<p class="socratic-q">As you read about life in a medieval castle, ask: <strong>what is the ONE big idea this article keeps coming back to? Which facts point to it?</strong></p>',
     'The <strong>central idea</strong> is the most important point an author makes. A <strong>detail</strong> is one fact that helps prove it.',
     'What big idea does this article keep coming back to?'),
 2: ("<p>Good readers of nonfiction look for how the author organizes information. Today's article is organized by comparing two groups of people. Watch for how each paragraph has its own focus.</p>",
     '<p class="socratic-q">Taking notes from informational text</p>',
     'Today&rsquo;s article has two paragraphs. Each one has its own focus.',
     'What is each paragraph mostly about? What big idea fits both?'),
 3: ("<p>Good readers use context clues to figure out unfamiliar words. Today's article has some challenging vocabulary. When you hit a word you don't know, look at the sentences around it for clues.</p>",
     '<p class="socratic-q">Taking notes from informational text</p>',
     'When you meet a new word, the sentences around it often explain it.',
     'What does the author most want you to know about royal courts?'),
 4: ("<p>Good readers notice how authors organize contrast — showing two different sides of a topic. As you read today, watch for how the author separates the rich from the poor.</p>",
     '<p class="socratic-q">Taking notes from informational text</p>',
     'Today&rsquo;s article shows two sides: what rich people ate and what poor people ate.',
     'What do the two sides show about food in the Middle Ages?'),
}
def wg(h, f, d):
    op, oq, p, q = WG[d]
    h = must(h, op, '<p>%s</p>' % p, f)
    h = must(h, oq, '<p class="socratic-q"><strong>%s</strong></p>' % q, f)
    return must(h, LI_OLD, LI[d], f)

REMEMBER = ('<div class="key-concept"><div class="key-concept-label">&#x1F4CC; Remember</div>\n'
            '<p>A capital letter starts every sentence. Names get capitals too: people (<em>Queen Eleanor</em>), places (<em>Tower of London</em>) and titles (<em>The Sword in the Stone</em>). '
            'Every important word in a name gets one. Small words like <em>the</em>, <em>of</em> and <em>in</em> stay small, unless they come first in a title.</p></div>')
NOTICE = r'<!-- grammar-notice-first -->.*?<div class="dol-answer" id="gramNotice">.*?</div>'
SPELL_DUP = r'\s*<p>(?:Find the VCCV|Apply the VCCV|Divide all these)[^<]*</p>.*?<div class="dol-answer" id="spell(?:Rule)?Reveal">.*?</div>'
SPELL_BYS = '<div class="callout callout-info" style="margin-bottom:14px;"><span class="callout-icon">&#x1F440;</span><p>Before you start: find the two middle consonants and split between them.</p></div>'
MORPH_T = '🌱 Morphology: trans-'

def day1(h, f):
    h = common(h, f, 1); h = wg(h, f, 1)
    h = head(h, '🌱 Morphology: Prefix trans- means across', f, sub='A word part that means <em>across</em>', slug='morph-trans1')
    h = must(h, '<div class="activity-title">🌱 Morphology: Prefix trans- means across</div>', '<div class="activity-title">' + MORPH_T + '</div>', f)
    h = must(h, '<p>Fill in the missing part after the prefix to build the word.</p>', '<p>Type the missing part after <strong>trans</strong> to build each word.</p>', f)
    h = head(h, '✏️ Grammar: Capitalization of Titles, Names, and Places', f, sub='Names of people, places and titles get capital letters.', slug='gram-cap1')
    h = must(h, '<strong>Your turn.</strong> Nine names, three kinds. Every one of them is capitalized &mdash; sort them by what they name.', '<strong>Your turn.</strong> Tap a name, then tap what it names.', f)
    h = head(h, '🔠 Spelling: VCCV Syllable Division', f, sub='Split between two consonants.', slug='spell-vccv1')
    h = resub(h, r'(<div class="dol-answer" id="spellReveal"><p><strong>The Rule:</strong>.*?</p>)<p>The <strong>VCCV pattern</strong>.*?</div>', r'\1</div>', f)
    h = must(h, '<strong>Practice:</strong> Sort these words using the pattern you discovered.', '<strong>Sort the words!</strong>', f)
    return h

def day2(h, f):
    h = common(h, f, 2); h = wg(h, f, 2)
    h = head(h, '🪶 Poetry', f, sub='Hyperbole: stretching the truth on purpose', slug='poem-hyper1')
    h = head(h, MORPH_T, f, sub='Match each word to its meaning.', slug='morph2')
    h = must(h, '<p>Before you start: find the word part, then read what is left.</p>', '<p>Find <strong>trans</strong> in each word. Then look at what is left.</p>', f)
    h = must(h, '<strong>Practice: Match the Word to Its Meaning!</strong> Tap a word, then tap what it means.', '<strong>Match the Word to Its Meaning!</strong>', f)
    h = head(h, '✏️ Grammar: Capitalization: Titles, Names, Places', f, sub='Find every word that needs a capital.', slug='gram-cap2')
    h = resub(h, NOTICE, REMEMBER, f)
    h = resub(h, r'<strong>Your turn\.</strong> Tap <strong>every</strong> word that needs a capital letter\..*?</p>', '<strong>Your turn.</strong> Tap every word that needs a capital letter. Every word in a name counts.</p>', f)
    h = head(h, '🔠 Spelling: VCCV Syllable Division', f, sub='Find the word that splits between two consonants.', slug='spell-vccv2')
    h = must(h, SPELL_BYS, '', f); h = resub(h, SPELL_DUP, '', f)
    h = must(h, '<strong>Sound Detective!</strong> Only one word in each row has two consonants standing between its vowels.', '<strong>Sound Detective!</strong>', f)
    h = rwm(h, f)
    return h

def day3(h, f):
    h = common(h, f, 3); h = wg(h, f, 3)
    h = head(h, MORPH_T, f, sub='Build four new words.', slug='morph3')
    h = must(h, '<p>Before you start: read the parts aloud, push them together, then write the word.</p>', '<p>Say each part out loud. Then say them together as one word.</p>', f)
    h = must(h, '<strong>Build the word.</strong> Put the parts together and type what they make.', '<strong>Build the word.</strong>', f)
    h = head(h, '✏️ Grammar: Capitalization: Count the Capitals', f, sub='Count the capitals each sentence needs.', slug='gram-cap3')
    h = resub(h, NOTICE, REMEMBER, f)
    h = resub(h, r'<strong>Your turn\.</strong> Count every word that needs a capital.*?</p>', '<strong>Your turn.</strong> Count the words that need a capital. The first word counts too.</p>', f)
    h = head(h, '🔠 Spelling: VCCV Syllable Division', f, sub='Split each word.', slug='spell-vccv3')
    h = must(h, SPELL_BYS, '', f); h = resub(h, SPELL_DUP, '', f)
    h = must(h, '<strong>VCCV Splitter!</strong> Find the two consonants in the middle, then tap to split between them.', '<strong>VCCV Splitter!</strong>', f)
    h = rwm(h, f)
    return h

def day4(h, f):
    h = common(h, f, 4); h = wg(h, f, 4)
    h = head(h, '🪶 Poetry', f, sub='Make up your own hyperbole.', slug='poem-hyper2')
    h = must(h, '<p class="socratic-q">Write one sentence of hyperbole about how long a school day feels. Stretch it until it is obviously not true.</p>',
               '<p class="socratic-q">Make up one sentence of hyperbole about how long a school day feels. Stretch it until nobody could believe it. Say it out loud.</p>', f)
    h = head(h, MORPH_T, f, sub='Roll a word and tell what it means.', slug='morph-dice')
    h = must(h, '<p>Before you start: say what the word part does from memory, then roll.</p>', '<p>Before you roll, say out loud what <strong>trans</strong> means.</p>', f)
    h = must(h, '<strong>Dice Roll Challenge!</strong> Roll a word, then say out loud what it means and how the word part changed it. Tap to check yourself.', '<strong>Dice Roll Challenge!</strong>', f)
    h = head(h, '✏️ Grammar: Capitalization Review', f, sub='Find the mistake. Not every sentence has one.', slug='gram-hunt')
    h = resub(h, NOTICE, REMEMBER, f)
    h = resub(h, r'<strong>Your turn\.</strong> Each sentence either has one mistake.*?</p>', '<strong>Your turn.</strong> Each sentence has one mistake or no mistake.</p>', f)
    h = head(h, '🔠 Spelling: VCCV Syllable Division', f, sub='Roll a word and split it.', slug='spell4')
    h = must(h, SPELL_BYS, '', f); h = resub(h, SPELL_DUP, '', f)
    h = must(h, '<strong>VCCV Dice!</strong> Roll a word, say it out loud, decide &mdash; then tap to check yourself.', '<strong>VCCV Dice!</strong>', f)
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
    how['illuminate'] = DO['illuminate']
    io.open(os.path.join(HERE, 'how_wk23.json'), 'w', encoding='utf-8').write(json.dumps(how, ensure_ascii=False, indent=1))
    print('reused:', sorted(k for k in USED if k in OLD))
    print('new lines:', sorted(how))
