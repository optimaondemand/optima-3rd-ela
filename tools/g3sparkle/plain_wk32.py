#!/usr/bin/env python3
"""Week 32 plain-language pass (Year-End Culmination: The 7 Pillars of Virtue; lesson-32-*-ext.html).

Same rules as plain_wk18-31 (Bethany, Nov 8 2026): a "What to do:" line on every activity, plain subs, no repeats.
Also the Reading tab in a clear order (week 31 rule): Day 1's 7 Pillars card sits INSIDE the Read box, so the
Pillar Watch ("After you read") comes after it; Days 2-4 get a "See the 7 pillars again" fold in the Look Back box.
Runs in place on the repo files after acc_wk32.py + light_wk32.py:  python tools/g3sparkle/plain_wk32.py"""
import io, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
DAYS = ['lesson-32-%d-ext.html' % d for d in (1, 2, 3, 4)]
OLD = {}
for w in range(18, 32):
    for k, v in json.load(io.open(os.path.join(HERE, 'how_wk%d.json' % w), encoding='utf-8')).items(): OLD.setdefault(k, v)
NEW = {
 'read-pillars': 'Read about the 7 pillars below. Each one has a real example from a book we read. Keep your lens in mind. Then answer the three questions.',
 'look-draft':   'There is nothing new to read today. Look back at your character’s book and the 7 pillars. Then answer the two questions.',
 'look-revise':  'There is nothing new to read today. Read your draft and the checklist. Then answer the three questions.',
 'look-share':   'Read how to share your response. Then answer the three questions.',
 'qchar':        'Answer the question in full sentences. Use a detail from your character’s book.',
 'qfinal':       'Type or paste your finished response in the box: opening, two body paragraphs and a closing.',
 'qreflect':     'Think back over your year of reading. Answer in full sentences.',
 'qletter':      'Write a short letter to a new 3rd grader: 3 to 5 sentences.',
 'poem-train':   'Read the first four lines out loud two times: once slowly, once fast. Which one sounds like a train?',
 'poem-perform': 'Choose any poem from this year and read it out loud to someone. Then think: what did you do with your voice to make it sound right? You do not need to write it.',
 'morph-yr1':    'Read the six words and their parts. Think about the three questions, then tap See if you were right. Last, type the missing part of each word and tap Check My Work.',
 'vsentence-me': 'Choose one word. Write one sentence that connects it to your character and to you.',
 'gram-yr1':     'Read the sentence in The Rule box. Think about the questions, then tap Now check your thinking. Then tap all seven words in the passage that need fixing.',
 'gram-yr2':     'Read the four sentences. Is each one simple, compound or complex? Tap Now check your thinking. Then tap the five words in the passage that are wrong.',
 'gram-yr3':     'Read the before and after, then tap Check yourself. Say the sentence in the gray box the right way, out loud. Then tap Check your sentence.',
 'gram-yr4':     'Think about the questions, then tap Check yourself. Tap all seven words that need fixing: capitals, then apostrophes, then verbs. Then tap See the answers, and answer the question in the box.',
 'spell-rules2': 'Read the rule. In each row, read the question, then tap the one word that fits.',
 'spell-dice-rule': 'Tap Roll the dice. Say the word out loud and think: which rule is at work? Then tap Check my answer. Roll all six words.',
 'ww-p1':        'Read Clara’s plan. Your plan is your answers to Q1 to Q3 on the Reading tab, so there is nothing to write here.',
 'ww-p2':        'Read Clara’s two paragraphs. Your draft is your answers to Q1 and Q2 on the Reading tab, so there is nothing to write here.',
 'ww-p3':        'Read Clara’s closing. Then write 3 short notes for sharing out loud, and the one thing you will show.',
 'ww-p4':        'Read Clara’s title. Type your title in the box. Then share your response out loud.',
 'pillars':      'Read the word on the temple. Tap the right answer. Each right answer raises the pillars.',
 'awards':       'Read the ribbon. Tap the character you would give it to. Then read what they did.',
 'lookback':     'Tap each stop on the road to see what you learned there. Then tap your favorite book.',
 'cert':         'Tap the pillar you will take to 4th grade. Check your name. Then save your certificate.',
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
        m = re.compile(r'(<div class="activity-sub">)(.*?)(</div>)', re.S).search(h, i)
        h = h[:m.start(2)] + sub + h[m.end(2):]
    if newtitle:
        h = h[:i] + 'activity-title">' + newtitle + h[i + len('activity-title">' + title):]
    if slug:
        j = h.find('<div class="activity-body"', i)
        k = h.find('>', j) + 1
        h = h[:k] + '\n' + do_line(slug) + h[k:]
    return h
def yourturn(h, f, text):
    return resub(h, r'(<span class="callout-icon">🎯</span><p><strong>Your turn\.</strong>).*?(</p>)', lambda m: m.group(1) + ' ' + text + m.group(2), f)

LI_RE = r'<li><strong>Look back across the year\'s books:</strong>.*?</li>\s*<li><strong>Name a skill you now use without thinking:</strong>.*?</li>\s*<li><strong>Give your proof:</strong>.*?</li>'
LI_NEW = ('<li><strong>Look back:</strong> Think about the books you read this year, from <em>Flat Stanley</em> to Narnia.</li>\n'
          '    <li><strong>Name a skill:</strong> Pick one thing that was hard in the fall and is easy for you now.</li>\n'
          '    <li><strong>Give your proof:</strong> Remember a time this year when you used that skill on your own.</li>')
KC = '\n      <div class="key-concept"><div class="key-concept-label">🌟 Reading–Writing–Meaning Connection</div><p>Speaking and writing with a clear, confident voice.</p></div>'
RCALL = r'(<div class="callout callout-info"><span class="callout-icon">📖</span><p style="white-space:pre-line;">)(.*?)(</p></div>)'
INTRO = {1: 'This week you will write about one character from our books and the 7 pillars of good character. Then you will share it out loud.\n\n'
            'Read each pillar below. Each one has a real example from a book we read.',
         2: 'Today you write the first part of your response.\n\n'
            '• Opening: name your character, the book, and your most important pillar.\n'
            '• Two body paragraphs: one for each pillar. Give the pillar, a real example from the book, and one sentence that says what it shows.\n\n'
            'You will write your closing tomorrow. Clara&rsquo;s model on the Turn In tab shows how it looks.'}
PILLAR_FOLD = ('\n      <details class="g3-reread" style="margin-top:8px;"><summary style="cursor:pointer;font-weight:800;color:#1B7A4E;padding:8px 12px;'
               'border:2px solid #B8E0C8;border-radius:10px;background:#EAF4EE;display:inline-block;">👆 See the 7 pillars again</summary>\n'
               '      <ul style="margin:8px 0 4px 20px;font-size:14px;color:#3A4A6B;line-height:1.7;">'
               '<li><strong>Honesty:</strong> telling the truth</li><li><strong>Respect:</strong> treating every person well</li>'
               '<li><strong>Courtesy:</strong> being polite and kind with words</li><li><strong>Responsibility:</strong> owning your choices</li>'
               '<li><strong>Courage:</strong> acting even when you are afraid</li><li><strong>Service:</strong> helping others without a reward</li>'
               '<li><strong>Perseverance:</strong> trying again when things are hard</li></ul>\n      </details>')
READT = {1: ('📖 Read: The 7 Pillars', 'Good character, with examples from our books', 'read-pillars'),
         2: ('📖 Look Back: your character', 'Draft your response', 'look-draft'),
         3: ('📖 Look Back: your draft', 'Revise your response', 'look-revise'),
         4: ('📖 Look Back: your whole year', 'Share your response', 'look-share')}
QS = {1: ['qchar'] * 3, 2: ['qchar'] * 2, 3: ['qchar'] * 3, 4: ['qfinal', 'qreflect', 'qletter']}
WW = {1: 'ww-p1', 2: 'ww-p2', 3: 'ww-p3', 4: 'ww-p4'}
PILLAR_CARD = re.compile(r'\n<div class="activity bl-gold" style="margin-bottom:18px;">\n  <div class="activity-head"><div class="activity-num" style="background:#D4AF37;">⭐</div>\n    <div><div class="activity-title">The 7 Pillars of Virtue</div>.*?\n</div></div>\n</div>\n', re.S)

def common(h, f, d):
    h = head(h, '📚 What Good Readers Do', f, sub='What to watch for while you read', slug='readers')
    h = resub(h, LI_RE, LI_NEW, f)
    h = must(h, '<p>Good readers <strong>look back at how their own reading has grown</strong>. The skills you practiced all year are the ones you now use without being told to.</p>',
               '<p>Good readers <strong>look back at how their reading has grown</strong>. The skills you practiced all year are the ones you now use on your own.</p>', f)
    h = must(h, '<p class="socratic-q"><strong>Reflect on how reading skills have grown.</strong></p>', '<p class="socratic-q"><strong>Look back at how your reading has grown.</strong></p>', f)
    h = h.replace('<p class="socratic-q">As you read today, ask yourself: ', '<p class="socratic-q">Ask yourself: ')
    h = must(h, "<div class=\"thinking-stop\">💭 Keep this question in your mind as you read — you'll answer it in the Reading tab.</div>", '', f)
    h = head(h, '✏️ Daily Oral Language', f, sub='Study the model. Then fix a sentence.', slug='dol')
    h = must(h, '<p>The first sentence is <strong>correct</strong>. Tap the highlighted words to see what is done right. Then use the model to fix the second sentence.</p>', '', f)
    h = must(h, 'Your mind is warmed up. Let&rsquo;s sharpen your words and skills.', 'Next: word study.', f)
    h = must(h, 'Words and skills sharpened. Time to open the book.', 'Next: reading.', f)
    h = must(h, 'Great reading work! Now bring your thinking to the assignment.', 'Next: turn in your work.', f)
    t, sub, slug = READT[d]
    h = head(h, 'Reading: Week 32', f, sub=sub, slug=slug, newtitle=t)
    h = must(h, KC, '', f)
    i = h.find('activity-title">' + t)
    m = re.compile(RCALL, re.S).search(h, i)
    body = INTRO.get(d, m.group(2))
    extra = PILLAR_FOLD if d > 1 else ''
    h = h[:m.start(2)] + body + h[m.end(2):m.end()] + extra + h[m.end():]
    if d == 1:   # the 7 Pillars card moves INSIDE the Read box, after the intro
        pc = PILLAR_CARD.search(h); assert pc, (f, 'pillar card')
        card = pc.group(0)
        inner = re.search(r'<div class="activity-body">\n(.*)\n</div></div>\n</div>\n$', card, re.S); assert inner, (f, 'card body')
        h = h[:pc.start()] + '\n' + h[pc.end():]
        box = ('\n      <div class="g3-text-in" style="border:2px solid #E8D28A;border-radius:14px;padding:12px 14px;margin-top:14px;background:#FFFDF6;">\n'
               '      <div style="font-weight:800;color:#0E1C42;margin-bottom:8px;">⭐ The 7 Pillars of Virtue</div>\n' + inner.group(1) + '\n</div>\n      </div>')
        i = h.find('activity-title">' + t); m = re.compile(RCALL, re.S).search(h, i)
        h = h[:m.end()] + box + h[m.end():]
    h = h.replace('<div class="textbox-prompt">Use a detail from your character&rsquo;s book.</div>', '')
    h = h.replace('<div class="textbox-prompt">Think about your own reading this year.</div>', '').replace('<div class="textbox-prompt">Write to a new 3rd grader.</div>', '')
    qs = re.findall(r'activity-title">(Q[123] — [^<]*)<', h); assert len(qs) == len(QS[d]), (f, qs)
    for q, s in zip(qs, QS[d]): h = head(h, q, f, slug=s)
    h = must(h, '<div class="activity-title">📖 Chapter Thinking</div><div class="activity-sub">Your reading responses are saved from the Reading tab.</div>',
               '<div class="activity-title">📖 Reading Answers</div><div class="activity-sub">Your answers from the Reading tab</div>', f)
    h = must(h, 'Your chapter answers were saved on the Reading tab. They will appear in your gathered work below.', 'Your answers on the Reading tab show in your work below.', f)
    h = must(h, '<div class="activity-title">🔤 Word Study Connection</div><div class="activity-sub">Your morphology response from the Word Study tab.</div>',
               '<div class="activity-title">🔤 Word Study Check</div><div class="activity-sub">The word part work on the Word Study tab</div>', f)
    h = must(h, 'Your morphology answer was saved on the Word Study tab. It will appear in your gathered work below.', 'Finish the word part work on the Word Study tab.', f)
    h = resub(h, r'\s*<div class="callout callout-info" style="background:#E8F1E8;border-color:#A8C8A8;margin-bottom:10px;padding:10px 14px;"><span class="callout-icon">📝</span><p style="font-size:14px;"><strong>Now you try\.</strong>.*?</p></div>', '', f)
    if d < 3: h = resub(h, r'\s*<div class="textbox-prompt">Write your response below\. Use complete sentences\.</div>', '', f)
    h = head(h, 'Writer&rsquo;s Workshop', f, slug=WW[d])
    return h

def rwm(h, f):
    h = resub(h, r'<div class="rwm-header">📖 RWM (?:&mdash;|—) Read like a Reader, Read like a Writer, Mimic</div>',
               '<div class="rwm-header">📖 Read Like a Writer</div>\n' + do_line('rwm'), f)
    for a, b in (('Read like a Reader', 'Read like a reader'), ('Read like a Writer', 'Read like a writer'), ('Mimic', 'Write your own')):
        h = h.replace('data-label="RWM &mdash; %s"' % a, 'data-label="%s"' % b)
    return h

BEFORE_SP = '<div class="callout callout-info" style="margin-bottom:14px;"><span class="callout-icon">&#x1F440;</span><p>Before you start: decide what you check first when a word looks wrong.</p></div>'
MORPH = '🌱 Morphology: word parts I know'
GRAM = '✏️ Grammar: Final editing review'
SPELL = '🔠 Spelling: Final spelling and conventions review'
TRAIN = 'This poem gallops. Long lines, hard rhymes, and a rhythm that copies wheels on a track. Reading it aloud at the right speed is not showing off &mdash; it is how you show you understood it.'

def day1(h, f):
    h = common(h, f, 1)
    h = head(h, '🌱 Morphology: Morphology reflection: word parts I know', f, sub='Word parts from the whole year', slug='morph-yr1', newtitle='🌱 Morphology: word parts I know')
    h = head(h, '🔤 Vocabulary: Decode &amp; Discover', f, sub='Three words about good character', slug='vocabcloze', newtitle='🔤 Vocabulary')
    h = head(h, GRAM, f, sub='Mistakes from the whole year', slug='gram-yr1', newtitle='✏️ Grammar: Year review')
    h = yourturn(h, f, 'Seven words need fixing. Tap all seven.')
    h = head(h, SPELL, f, sub='Prefix or suffix?', slug='spell-ps1', newtitle='🔠 Spelling: Year review')
    h = must(h, '<p>Sort each word: does it have a prefix at the front or a suffix at the end?</p>', '<p><strong>Sort the Words!</strong></p>', f)
    return h

def day2(h, f):
    h = common(h, f, 2)
    h = head(h, '🪶 Poetry', f, sub='Make it sound like a train', slug='poem-train')
    h = head(h, MORPH, f, sub='Match each word to its meaning.', slug='morph2')
    h = must(h, '<p>Before you start: find the word part, then read what is left.</p>', '<p>Find the word part in each word. Then read what is left.</p>', f)
    h = head(h, '🔤 Vocabulary: Identify &amp; Match', f, sub='Four words about good character', slug='vmatch', newtitle='🔤 Vocabulary')
    h = head(h, GRAM, f, sub='Three kinds of sentences', slug='gram-yr2', newtitle='✏️ Grammar: Year review')
    h = must(h, '<p>Identify the key word or pattern in each sentence. Think: what rule does it follow?</p>', '<p>Is each sentence simple, compound or complex? Look for <em>and</em>, <em>when</em> and <em>although</em>.</p>', f)
    h = yourturn(h, f, 'Tap the five words that are wrong.')
    h = head(h, SPELL, f, sub='Which rule is it?', slug='spell-rules2', newtitle='🔠 Spelling: Year review')
    h = must(h, BEFORE_SP, '', f)
    h = rwm(h, f)
    return h

def day3(h, f):
    h = common(h, f, 3)
    h = head(h, MORPH, f, sub='Build four words.', slug='morph3')
    h = must(h, '<p>Before you start: read the parts aloud, push them together, then write the word.</p>', '<p>Say each part out loud. Then say them together as one word.</p>', f)
    h = head(h, '🔤 Vocabulary: Use the Words', f, sub='Pick the word that fits.', slug='vselect', newtitle='🔤 Vocabulary')
    h = head(h, GRAM, f, sub='Fix a sentence like an editor.', slug='gram-yr3', newtitle='✏️ Grammar: Year review')
    h = head(h, SPELL, f, sub='Find the misspelled words.', slug='spell-pre3', newtitle='🔠 Spelling: Year review')
    h = must(h, BEFORE_SP, '', f)
    h = rwm(h, f)
    return h

def day4(h, f):
    h = common(h, f, 4)
    h = head(h, '🪶 Poetry', f, sub='Perform a poem from the year', slug='poem-perform')
    h = must(h, 'Choose any poem from this year and read it aloud to someone. Then write one sentence in your journal: what did you have to do with your voice to make it sound right?',
               'What did you have to do with your voice to make it sound right?', f)
    h = head(h, MORPH, f, sub='Roll a word and tell what it means.', slug='morph-dice')
    h = must(h, '<p>Before you start: say what the word part does from memory, then roll.</p>', '<p>Before you roll, say out loud what one word part from this year means.</p>', f)
    h = head(h, '🔤 Vocabulary: Justify Your Choice', f, sub='Use a word to tell about your character and you.', slug='vsentence-me', newtitle='🔤 Vocabulary')
    h = head(h, GRAM, f, sub='Fix it in passes.', slug='gram-yr4', newtitle='✏️ Grammar: Year review')
    h = yourturn(h, f, 'Tap all seven words that need fixing.')
    h = head(h, SPELL, f, sub='Roll a word and name its rule.', slug='spell-dice-rule', newtitle='🔠 Spelling: Year review')
    h = must(h, BEFORE_SP, '', f)
    h = rwm(h, f)
    return h

FIX = {DAYS[0]: day1, DAYS[1]: day2, DAYS[2]: day3, DAYS[3]: day4}
if __name__ == '__main__':
    apply = '--apply' in sys.argv
    for f, fn in FIX.items():
        h = io.open(f, encoding='utf-8', newline='').read()
        assert 'class="g3-do"' not in h, (f, 'already done')
        o = h.count('<div') - h.count('</div')
        h = fn(h, f)
        assert h.count('<div') - h.count('</div') == o, (f, o, h.count('<div') - h.count('</div'))
        if apply: io.open(f, 'w', encoding='utf-8', newline='').write(h)
        print('ok', f)
    how = {k: DO[k] for k in sorted(USED) if k not in OLD}
    for k in ('pillars', 'awards', 'lookback', 'cert'): how[k] = DO[k]
    if apply: io.open(os.path.join(HERE, 'how_wk32.json'), 'w', encoding='utf-8').write(json.dumps(how, ensure_ascii=False, indent=1))
    print('reused:', sorted(k for k in USED if k in OLD))
    print('new lines:', sorted(how))
