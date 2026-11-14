#!/usr/bin/env python3
"""Week 24 plain-language pass (Medieval Nonfiction, part 2: four short articles, no novel).

Same rules as plain_wk18-22 (Bethany, Nov 8 2026). Reads ~/g3w24/pristine-orig
(the week 24 files after acc_wk24.py + acc2_wk24.py), writes ~/g3w24/pristine. Every
replacement is asserted. Re-runnable. No fluency page this week."""
import io, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC, DST = os.path.expanduser('~/g3w24/pristine-orig'), os.path.expanduser('~/g3w24/pristine')
DAYS = ['lesson-24-1-med.html', 'lesson-24-2-med.html', 'lesson-24-3-med.html', 'lesson-24-4-med.html']

OLD = {}
for w in (18, 19, 20, 21, 22, 23):
    for k, v in json.load(io.open(os.path.join(HERE, 'how_wk%d.json' % w), encoding='utf-8')).items(): OLD.setdefault(k, v)
NEW = {
 'morph-script1': 'Read the four words and their parts. Think about the three questions. Then tap See if you cracked it. Last, type the missing part of each word and tap Check My Work.',
 'gram-main1':    'Read the paragraph and tap Now check your thinking. Then tap each sentence, and tap its column: main idea, detail, or off the topic. Last, answer the question in the box.',
 'gram-main2':    'Read the Remember box. In each mixed-up paragraph, tap the one sentence that is the main idea. Last, answer the question in the box.',
 'gram-main3':    'Read the Remember box. Read each set of details, and type the one word they are all about. Tap Check My Answers. Last, write a main idea sentence in the box.',
 'gram-main4':    'Read the Remember box. In each paragraph, tap the sentence that is off the topic, or tap No mistake. Then tap See the answers, and answer the question in the box.',
 'spell-suf1':    'Say the words in Group A and Group B out loud. Think about the three questions, then tap See the Rule. Last, tap each of the eight words, and tap the ending it uses.',
 'spell-suf2':    'Read the rule. Then in each row, tap the one word that uses the ending named above it.',
 'spell-suf3':    'Read the rule. Say each word, and find where the base word stops. Then tap the card to break it apart.',
 'spell-suf4':    'Tap Roll the dice. Pick an ending for the word, and say why you picked it. Then tap Check my answer. Roll all six words.',
 'poem-jab1':     'Read the poem out loud. Find the real English words and the made-up ones. Then say how you can tell what a made-up word is doing.',
 'poem-jab2':     'Read the poem out loud again. Then make up two words of your own and use them in one sentence. Say it out loud. You do not need to write it.',
 'ww-draft2':     'Read Clara’s before and after. Then write your whole paragraph in the box: a topic sentence, two details, and a closing sentence.',
 'ww-revise':     'Read how Clara cut a sentence that did not fit. Read your paragraph out loud. Then write the sentence you cut or fixed, and how you changed it.',
 'ww-publish2':   'Read your paragraph with the final checklist and fix anything you find. Then write what you are most proud of, and one thing you would do differently.',
 'market':        'Read the word on the basket. Tap the stall that sells it. A right answer brings a customer to the market.',
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

ART = {1: 'How Castles Were Built', 2: 'Knights: Warriors and Gentlemen', 3: 'Medieval Towns: Busy, Smelly, and Alive', 4: 'Real vs. Imagined: The Middle Ages in Stories'}
VOCSUB = {1: 'Four words from the castle article', 2: 'Four words about knights', 3: 'Four words about medieval towns', 4: 'Four words about history and stories'}
WW = {1: 'ww-draft2', 2: 'ww-revise', 3: 'ww-edit', 4: 'ww-publish2'}

def common(h, f, day):
    h = must(h, '<div class="thinking-stop">💭 Think about this as you read today — you don\'t need to write anything here.</div>', '', f)
    h = head(h, '📚 What Good Readers Do', f, sub='What to watch for while you read', slug='readers')
    h = head(h, '✏️ Daily Oral Language', f, sub='Study the model. Then fix a sentence.', slug='dol')
    h = resub(h, r'\s*<p>The first sentence is <strong>correct</strong>\. Tap the parts you notice.*?</p>', '', f)
    h = must(h, 'Now that your mind is warmed up, let&rsquo;s sharpen your words and skills.', 'Next: word study.', f)
    h = must(h, 'Your words and skills are sharp. Time to open the book.', 'Next: reading.', f)
    h = must(h, 'You&rsquo;ve read the article and thought carefully. Now let&rsquo;s put your thinking into writing.', 'Next: answer the questions and turn in your work.', f)
    h = must(h, '<p><strong>Novel Connection:</strong> Last week you read about medieval life and chose a topic. This week we go deeper — reading about castles, knights, and towns — and you draft and publish your expository paragraph.</p>',
               '<p><strong>This week:</strong> more true articles about the Middle Ages: castles, knights, towns, and how stories change history. You write, fix and publish your own paragraph.</p>', f)
    h = head(h, 'Pause &amp; Think', f, sub='Think about these while you read.', slug='read-art')
    h = must(h, '<div class="activity-title">%s</div>' % ART[day], '<div class="activity-title">📰 Read: %s</div>' % ART[day], f)
    h = head(h, '📰 Article Thinking', f, sub='Answer in full sentences. Use details from the article.', slug='article')
    h = must(h, '<div class="activity-title">🔤 Word Study Connection (Morphology)</div><div class="activity-sub">Your morphology response from the Word Study tab.</div>',
               '<div class="activity-title">🔤 Word Study Check</div><div class="activity-sub">The word part work on the Word Study tab</div>', f)
    h = must(h, 'Your morphology answer was saved on the Word Study tab. It will appear in your gathered work below.',
               'Finish the word part work on the Word Study tab. It shows in your work below.', f)
    h = h.replace('{ title: \'🔤 WORD STUDY CONNECTION (MORPHOLOGY)\'', '{ title: \'🔤 WORD STUDY CHECK\'')
    h = must(h, 'Meet Today, our example writer', 'Meet Clara, our example writer', f)
    h = re.sub(r'(<strong>Today&rsquo;s focus:</strong> )Today: ', r'\1', h)
    h = re.sub(r'\s*<p style="font-size:14px;"><em>Today: [^<]*</em></p>', '', h)
    h = resub(h, r'\s*<div class="callout callout-info" style="background:#E8F1E8;border-color:#A8C8A8;margin:0 0 10px 0;padding:10px 14px;"><span class="callout-icon">📝</span><p style="font-size:14px;"><strong>Now you try\.</strong>.*?</p></div>', '', f)
    h = head(h, 'Writer&rsquo;s Workshop', f, slug=WW[day])
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

LI_OLD = ('      <li><strong>Find the design or the event:</strong> Start with something people built, changed, or decided.</li>\n'
          '      <li><strong>Ask WHY it was done that way:</strong> Nonfiction writers almost always explain the reason somewhere nearby.</li>\n'
          '      <li><strong>Say it as a <em>because</em> sentence:</strong> <em>Castles had thick walls because ___.</em></li>')
def lis(*xs): return '\n'.join('      <li><strong>%s</strong> %s</li>' % x for x in xs)
def bec(t): return ('Say it as a <em>because</em> sentence:', '<em>%s</em>' % t)
LI = {
 1: lis(('Find what the builders did:', 'Pick one thing about how a castle was built.'),
        ('Ask why:', 'The reason is usually close by. Look for because or so.'), bec('Castles had thick walls because ___.')),
 2: lis(('Find a step:', 'Pick one step on the way to becoming a knight.'),
        ('Ask why:', 'What did that step help a boy learn for the next one?'), bec('A squire cared for armor because ___.')),
 3: lis(('Find a sight, sound or smell:', 'Pick one thing you would notice in the town.'),
        ('Ask why:', 'What caused it? Think about animals, workshops and crowds.'), bec('The town was loud because ___.')),
 4: lis(('Find a change:', 'Pick one thing stories change from real life.'),
        ('Ask why:', 'Why would a storyteller change it?'), bec('Stories show perfect knights because ___.')),
}
WG = {
 1: ("<p>Good readers of nonfiction notice cause-and-effect relationships — when one thing causes another. Today's article is full of them. Ask: WHY was this designed this way?</p>",
     "<p class=\"socratic-q\">Pick one thing in today's article that castle builders did a certain way. <strong>WHY was it built like that?</strong></p>",
     'A <strong>cause</strong> is why something happens. The <strong>effect</strong> is what happens. Today&rsquo;s article is full of them.',
     'Why did castle builders build things the way they did?'),
 2: ("<p>Good readers notice when an author presents an ideal vs. the reality. Today's article tells you what knights were SUPPOSED to be like — and then hints at what they were actually like. Watch for that contrast.</p>",
     '<p class="socratic-q">Explaining facts in your own words</p>',
     'Today&rsquo;s article tells the steps to becoming a knight. Each step had a reason.',
     'Why did each step come before the next one?'),
 3: ("<p>Good readers use vivid details to build a mental picture. Today's article is full of sensory language. As you read, try to picture, hear, and even smell the medieval town the author is describing.</p>",
     '<p class="socratic-q">Explaining facts in your own words</p>',
     'Today&rsquo;s article helps you see, hear and smell a medieval town. Each busy sight or smell has a cause.',
     'What made a medieval town so loud and smelly?'),
 4: ("<p>Good readers think critically about what they read — including the stories they love. Today's article asks you to think like a historian: what is fact, and what is fiction?</p>",
     '<p class="socratic-q">Explaining facts in your own words</p>',
     'Today&rsquo;s article asks you to think like a historian: what is real, and what is made up? Stories change things for a reason.',
     'Why do stories change what really happened?'),
}
def wg(h, f, d):
    op, oq, p, q = WG[d]
    h = must(h, op, '<p>%s</p>' % p, f)
    h = must(h, oq, '<p class="socratic-q"><strong>%s</strong></p>' % q, f)
    return must(h, LI_OLD, LI[d], f)

REMEMBER = ('<div class="key-concept"><div class="key-concept-label">&#x1F4CC; Remember</div>\n'
            '<p>A paragraph has one <strong>main idea</strong>. It is often the first sentence, called the <strong>topic sentence</strong>. '
            'The other sentences are <strong>details</strong> that support it. A sentence that does not support it is <strong>off the topic</strong>.</p></div>')
NOTICE = r'<!-- grammar-notice-first -->.*?<div class="dol-answer" id="gramNotice">.*?</div>'
SPELL_RULE1 = r'<!-- spell-notice-first -->\s*<div class="callout callout-gold"[^>]*><span class="callout-icon">&#x1F4D6;</span><p[^>]*><strong>The Rule:</strong>.*?</p></div>'
MT = '🌱 Morphology: script / scribe'

def day1(h, f):
    h = common(h, f, 1); h = wg(h, f, 1)
    h = head(h, '🌱 Morphology: Root/base: script/scribe means write', f, sub='A word part that means <em>write</em>', slug='morph-script1')
    h = must(h, '<div class="activity-title">🌱 Morphology: Root/base: script/scribe means write</div>', '<div class="activity-title">' + MT + '</div>', f)
    h = must(h, '<p>Fill in the missing part after the prefix to build the word.</p>', '<p>Type the missing part to build each word.</p>', f)
    h = head(h, '✏️ Grammar: Main Idea and Details in Paragraphs', f, sub='Main idea, detail, or off the topic?', slug='gram-main1')
    h = must(h, '<strong>Your turn.</strong> Nine sentences, three columns. A main idea covers a whole paragraph; a detail supports one; an off-topic sentence does neither. The paragraphs are about guilds, castle jobs and travel.',
               '<strong>Your turn.</strong> These sentences come from paragraphs about guilds, castle jobs and travel. Tap a sentence, then tap its column.', f)
    h = head(h, '🔠 Spelling: Review suffixes -ful, -less, -ness, -ly', f, sub='Four endings, four jobs', slug='spell-suf1')
    h = resub(h, SPELL_RULE1, '<!-- spell-notice-first -->', f)
    h = must(h, '<strong>Practice: Sort the words.</strong> Tap a word, then tap the ending it uses.', '<strong>Sort the words!</strong>', f)
    return h

def day2(h, f):
    h = common(h, f, 2); h = wg(h, f, 2)
    h = head(h, '🪶 Poetry', f, sub='Made-up words you can still understand', slug='poem-jab1')
    h = head(h, MT, f, sub='Match each word to its meaning.', slug='morph2')
    h = must(h, '<p>Before you start: find the word part, then read what is left.</p>', '<p>Find <strong>script</strong> or <strong>scribe</strong> in each word.</p>', f)
    h = must(h, '<strong>Practice: Match the Word to Its Meaning!</strong> Tap a word, then tap what it means.', '<strong>Match the Word to Its Meaning!</strong>', f)
    h = head(h, '✏️ Grammar: Main Idea and Details', f, sub='Find the main idea sentence.', slug='gram-main2')
    h = resub(h, NOTICE, REMEMBER, f)
    h = must(h, '<strong>Your turn.</strong> Each group is a paragraph with its sentences shuffled. Tap the <strong>whole sentence</strong> that is the main idea &mdash; the one the other two are supporting.',
               '<strong>Your turn.</strong> Each group is a mixed-up paragraph. Tap the sentence that is the main idea.', f)
    h = head(h, '🔠 Spelling: Review suffixes -ful, -less, -ness, -ly', f, sub='Find the word with the named ending.', slug='spell-suf2')
    h = must(h, '<div class="callout callout-info" style="margin-bottom:14px;"><span class="callout-icon">&#x1F440;</span><p>Before you start: cover the ending with your finger and read the base word underneath.</p></div>', '', f)
    h = must(h, '<strong>Suffix Detective!</strong> Only one word in each row uses the ending named above it.', '<strong>Suffix Detective!</strong>', f)
    h = rwm(h, f)
    return h

def day3(h, f):
    h = common(h, f, 3); h = wg(h, f, 3)
    h = head(h, MT, f, sub='Build four words.', slug='morph-struct3')
    h = must(h, '<p>Before you start: read the parts aloud, push them together, then write the word.</p>', '<p>Say each part out loud. Then say them together as one word.</p>', f)
    h = must(h, '<strong>Build the word.</strong> Put the parts together and type what they make.', '<strong>Build the word.</strong>', f)
    h = head(h, '✏️ Grammar: Main Idea and Details', f, sub='Name what the details are about.', slug='gram-main3')
    h = resub(h, NOTICE, REMEMBER, f)
    h = must(h, '<strong>Your turn.</strong> Read the three details and type the one word they are all about. That word is the seed of the main idea.',
               '<strong>Your turn.</strong> Read the three details. Type the one word they are all about.', f)
    h = must(h, '<p style="font-size:13px;color:#7A88A8;margin-top:4px;">Every answer below comes from this list.</p>', '', f)
    h = head(h, '🔠 Spelling: Review suffixes -ful, -less, -ness, -ly', f, sub='Break each word apart.', slug='spell-suf3')
    h = must(h, '<div class="callout callout-info" style="margin-bottom:14px;"><span class="callout-icon">&#x1F440;</span><p>Before you start: find the base word, then name the job the ending is doing.</p></div>', '', f)
    h = resub(h, r'\s*<p>Say each word, decide where the base word stops, then tap to check yourself.</p>', '', f)
    h = must(h, '<strong>Break it apart!</strong> Tap each card to split the word and name what its ending does.', '<strong>Break it apart!</strong>', f)
    h = rwm(h, f)
    return h

def day4(h, f):
    h = common(h, f, 4); h = wg(h, f, 4)
    h = head(h, '🪶 Poetry', f, sub='Make up your own words.', slug='poem-jab2')
    h = must(h, '<p class="socratic-q">Invent two words of your own and use them in one sentence, so a reader can tell what they mean without being told.</p>',
               '<p class="socratic-q">Make up two words of your own and use them in one sentence, so a listener can tell what they mean. Say it out loud.</p>', f)
    h = head(h, MT, f, sub='Roll a word and tell what it means.', slug='morph-dice')
    h = must(h, '<p>Before you start: say what the word part does from memory, then roll.</p>', '<p>Before you roll, say out loud what <strong>script</strong> and <strong>scribe</strong> mean.</p>', f)
    h = must(h, '<strong>Dice Roll Challenge!</strong> Roll a word, then say out loud what it means and how the word part changed it. Tap to check yourself.', '<strong>Dice Roll Challenge!</strong>', f)
    h = head(h, '✏️ Grammar: Main Idea and Details', f, sub='Find the sentence that wandered off.', slug='gram-main4')
    h = resub(h, NOTICE, REMEMBER, f)
    h = must(h, '<strong>Your turn.</strong> Each sentence either has one mistake or nothing wrong at all. Tap the whole sentence that does not belong, or tap <strong>No mistake</strong>. Two of these paragraphs are tight and two have a sentence that wandered off.',
               '<strong>Your turn.</strong> In each paragraph, tap the sentence that is off the topic. If every sentence fits, tap <strong>No mistake</strong>.', f)
    h = head(h, '🔠 Spelling: Review suffixes -ful, -less, -ness, -ly', f, sub='Roll a word and pick its ending.', slug='spell-suf4')
    h = resub(h, r'\s*<p>Last day on these four\. Roll a base word.*?</p>', '', f)
    h = must(h, '<strong>Suffix Dice!</strong> Roll a base word, choose an ending, say why &mdash; then tap to check yourself.', '<strong>Suffix Dice!</strong>', f)
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
    how['market'] = DO['market']
    io.open(os.path.join(HERE, 'how_wk24.json'), 'w', encoding='utf-8').write(json.dumps(how, ensure_ascii=False, indent=1))
    print('reused:', sorted(k for k in USED if k in OLD))
    print('new lines:', sorted(how))
