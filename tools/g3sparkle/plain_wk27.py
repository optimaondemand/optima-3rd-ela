#!/usr/bin/env python3
"""Week 27 plain-language pass (The Lion, the Witch and the Wardrobe, Ch. 7-9; Narnia page template, as weeks 25-26).

Same rules as plain_wk18-24 (Bethany, Nov 8 2026). Reads ~/g3w27/pristine-orig (the week 27 files after
acc_wk27.py), writes ~/g3w27/pristine. Every replacement is asserted. Re-runnable."""
import io, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC, DST = os.path.expanduser('~/g3w27/pristine-orig'), os.path.expanduser('~/g3w27/pristine')
DAYS = ['lesson-27-1-lww.html', 'lesson-27-2-lww.html', 'lesson-27-3-lww.html', 'lesson-27-4-lww.html']
FLU = 'lesson-27-fluency.html'

OLD = {}
for w in range(18, 27):
    for k, v in json.load(io.open(os.path.join(HERE, 'how_wk%d.json' % w), encoding='utf-8')).items(): OLD.setdefault(k, v)
NEW = {
 'morph-in1':    'Read the four words. Think about the question, then tap See if you were right. Last, type the base word hiding in each one and tap Check My Words.',
 'vsentence79':  'Choose one word. Write one sentence that uses it to tell about something in Chapters 7 to 9.',
 'gram-irr1':    'Read The Rule box. Think about the question, then tap Now check your thinking. Then tap the four verbs in the passage that should not end in -ed. Last, answer the question in the box.',
 'gram-irr2':    'Read the four sentences and find the verbs that are wrong. Tap Now check your thinking. Next, tap every word in the paragraph that is wrong. Last, answer the question in the box.',
 'gram-irr3':    'Read the before and after, then tap Check yourself. Fix the sentence in the gray box. Write it in the answer box, and list three more verbs that do not take -ed.',
 'gram-pass3':   'Think about the question, then tap Check yourself. Tap every word that needs fixing: capitals, the apostrophe, the verbs, and the word before a missing comma. Then tap See the answers, and answer the question in the box.',
 'spell-pre1':   'Think about the questions, then tap Now name the pattern. Last, tap each of the eight words, and tap its group: prefix + base word, or base word only.',
 'spell-pre2':   'Read the rule. Then tap every word in the two sentences that is built from a prefix and a base word.',
 'spell-pre3':   'Read the rule. Each sentence has two misspelled words. Tap a word to check it. Find all six.',
 'spell-pre4':   'Tap Roll the dice. Say the word out loud, and name its prefix and its base word. Then tap Check my answer. Roll all six words.',
 'poem-lim1':    'Read the first limerick out loud. Then answer the question out loud: which three lines rhyme, and which two? You do not need to write it.',
 'poem-lim2':    'Read both limericks out loud. Say the rhyme pattern as letters: A, A, B, B, A. Does the second limerick fit it? Say your answer out loud.',
 'look-ch79':    'There are no new chapters today. Look back through Chapters 7 to 9 in your book. Then answer the three questions below.',
 'ww-cplan':     'Read Clara’s before and after. Then plan your response in the box: two characters, how each one sees Aslan or Narnia, and the big difference between them.',
 'ww-cdraft':    'Read Clara’s draft. Then write your comparison in full sentences. Use a word like shows or reveals.',
 'ww-precise':   'Read Clara’s revision. Find one vague phrase in your response. Write your response again with more precise words, like shows, reveals or suggests.',
 'ww-cpublish':  'Read Clara’s closing. Then write your final response: two characters, how each one sees things, details from the book, and what the difference shows.',
 'icehole':      'Read the word on the fish. Tap the right answer. A right answer lands the fish on the ice.',
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

LI_OLD = ('    <li><strong>Pick the event they all share:</strong> Choose a scene more than one character is part of.</li>\n'
          '    <li><strong>Retell it from each side:</strong> Say what each character would tell you happened.</li>\n'
          '    <li><strong>Explain what makes them differ:</strong> Different wants, different fears, and different information change what a character sees.</li>')
LI_NEW = ('    <li><strong>Pick one moment:</strong> Find a scene with two or more characters in it.</li>\n'
          '    <li><strong>See it from each side:</strong> What would each character say happened?</li>\n'
          '    <li><strong>Ask why they differ:</strong> What does each one want, fear, or know?</li>')
READT = {1: ('📖 Read: Ch. 7', 'A Day with the Beavers', 'read-ch'), 2: ('📖 Read: Ch. 8', 'What Happened after Dinner', 'read-ch'),
         3: ('📖 Read: Ch. 9', 'In the Witch’s House', 'read-ch'), 4: ('📖 Look Back: Ch. 7–9', 'No new chapters today', 'look-ch79')}
WW = {1: 'ww-cplan', 2: 'ww-cdraft', 3: 'ww-precise', 4: 'ww-cpublish'}
CHECK = {1: ('I answered all 3 reading questions with evidence.', 'I answered all 3 chapter questions with details from the book.'),
         2: ('I answered all 3 reading questions with evidence.', 'I answered all 3 chapter questions with details from the book.'),
         3: ('I answered all 3 reading questions with text evidence.', 'I answered all 3 chapter questions with details from the book.'),
         4: ('I answered all 3 questions with clear evidence and explanation.', 'I answered all 3 questions with details from the book.')}

def common(h, f, d):
    h = head(h, '📚 What Good Readers Do', f, sub='What to watch for while you read', slug='readers')
    h = must(h, LI_OLD, LI_NEW, f)
    h = must(h, '<p>Good readers <strong>explain different characters&rsquo; perspectives</strong>. Everyone in a scene sees it through their own wants, fears, and what they happen to know.</p>',
               '<p>Good readers <strong>explain how different characters see the same thing</strong>. That is called a character&rsquo;s <em>perspective</em>.</p>', f)
    h = must(h, '<p class="socratic-q"><strong>Explain different character perspectives.</strong></p>', '<p class="socratic-q"><strong>See the story through each character&rsquo;s eyes.</strong></p>', f)
    h = h.replace('<p class="socratic-q">As you read today, ask yourself: ', '<p class="socratic-q">Ask yourself: ')
    h = must(h, "<div class=\"thinking-stop\">💭 Keep this question in your mind as you read — you'll answer it in the Reading tab.</div>", '', f)
    h = head(h, '✏️ Daily Oral Language', f, sub='Study the model. Then fix a sentence.', slug='dol')
    h = must(h, '<p>The first sentence is <strong>correct</strong>. Tap the highlighted words to see what is done right. Then use the model to fix the second sentence.</p>', '', f)
    h = must(h, 'Your mind is warmed up. Let&rsquo;s sharpen your words and skills.', 'Next: word study.', f)
    h = must(h, 'Words and skills sharpened. Time to open the book.', 'Next: reading.', f)
    h = must(h, 'Great reading work! Now bring your thinking to the assignment.', 'Next: turn in your work.', f)
    t, sub, slug = READT[d]
    h = head(h, 'Reading: Ch. 7–9', f, sub=sub, slug=slug, newtitle=t)
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
    h = must(h, CHECK[d][0], CHECK[d][1], f)
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

GRAM = '✏️ Grammar: Irregular verbs'
SPELL = '🔠 Spelling: Prefix + base word decoding'
MORPH = '🌱 Morphology: in- / im-'
RULE_PRE = '<p><strong>This week:</strong> Prefix + base word decoding</p>'
BEFORE_PRE = '<div class="callout callout-info" style="margin-bottom:14px;"><span class="callout-icon">&#x1F440;</span><p>Before you start: separate the front chunk from the base word.</p></div>'
def spell_common(h, f):
    h = must(h, BEFORE_PRE, '', f)
    h = resub(h, r'\s*' + re.escape(RULE_PRE), '', f)
    return h
def day1(h, f):
    h = common(h, f, 1)
    h = head(h, MORPH, f, sub='Two word parts that both mean not', slug='morph-in1')
    h = must(h, '<strong>Practice: Build it.</strong> Type the base word hiding inside each one.', '<strong>Find the base word.</strong>', f)
    h = head(h, '🔤 Vocabulary: Decode &amp; Discover', f, sub='Three words from Ch. 7–9', slug='vocabcloze', newtitle='🔤 Vocabulary')
    h = head(h, GRAM, f, sub='Verbs that do not use -ed for the past', slug='gram-irr1')
    h = must(h, '<p style="margin-top:8px;font-size:15px;color:#3A4A6B;">Said is the irregular past tense of say — not sayed. Came is the irregular past tense of come — not comed.</p>',
               '<p style="margin-top:8px;font-size:15px;color:#3A4A6B;"><em>Said</em> is the past tense of <em>say</em>. It is not <em>sayed</em>. A verb like this is called an <strong>irregular verb</strong>.</p>', f)
    h = resub(h, r'<strong>Your turn\.</strong> Tap <strong>every</strong> word in the passage that needs fixing\. The passage only finishes when you have found them all &mdash; count first, then start tapping\. Four verbs here took <em>-ed</em> when they should not have\.',
               '<strong>Your turn.</strong> Four verbs in this passage end in <em>-ed</em> when they should not. Tap all four.', f)
    h = head(h, SPELL, f, sub='Peel off the prefix to find the base word', slug='spell-pre1')
    h = must(h, '<div class="callout callout-info"><span class="callout-icon">🎮</span><p>Sort these words into the correct spelling pattern group.</p></div>',
               '<div class="callout callout-info"><span class="callout-icon">🎮</span><p><strong>Sort the Words!</strong></p></div>', f)
    return h

def day2(h, f):
    h = common(h, f, 2)
    h = head(h, '🪶 Poetry', f, sub='A funny poem with five lines', slug='poem-lim1')
    h = head(h, MORPH, f, sub='Match each word to its meaning.', slug='morph2')
    h = must(h, '<p>Before you start: find the word part, then read what is left.</p>', '<p>Find <strong>in-</strong> or <strong>im-</strong> in each word. Then look at what is left.</p>', f)
    h = must(h, '<strong>Practice: Match the Word to Its Meaning!</strong> Tap a word, then tap what it means.', '<strong>Match the Word to Its Meaning!</strong>', f)
    h = head(h, '🔤 Vocabulary: Identify &amp; Match', f, sub='Four words from Ch. 7–9', slug='vmatch', newtitle='🔤 Vocabulary')
    h = resub(h, callout('🎯', r'<strong>Vocabulary Match:</strong> Tap a word, then tap its meaning\. Use what you know from your reading\.'), '', f)
    h = head(h, GRAM, f, sub='Find the wrong verbs. Then fix a paragraph.', slug='gram-irr2')
    h = must(h, '<p>Identify the key word or pattern in each sentence. Think: what rule does it follow?</p>', '<p>Look at the verb in each sentence. Is it the right past-tense form?</p>', f)
    h = must(h, '<strong>Your turn.</strong> Same job, but the mistakes are not all the same kind this time. Tap <strong>every</strong> word that is wrong.',
               '<strong>Your turn.</strong> The mistakes in this paragraph are not all the same kind. Tap <strong>every</strong> word that is wrong.', f)
    h = head(h, SPELL, f, sub='Find the words with a prefix', slug='spell-pre2')
    h = spell_common(h, f)
    h = must(h, '<p>Tap every word built from a <strong>prefix + base word</strong>.</p>', '<p><strong>Prefix Hunt!</strong></p>', f)
    h = rwm(h, f)
    return h

def day3(h, f):
    h = common(h, f, 3)
    h = head(h, MORPH, f, sub='Build four words.', slug='morph3')
    h = must(h, '<p>Before you start: read the parts aloud, push them together, then write the word.</p>', '<p>Say each part out loud. Then say them together as one word.</p>', f)
    h = must(h, '<strong>Build the word.</strong> Put the parts together and type what they make.', '<strong>Build the word.</strong>', f)
    h = head(h, '🔤 Vocabulary: Use the Words', f, sub='Pick the word that fits.', slug='vselect', newtitle='🔤 Vocabulary')
    h = resub(h, callout('🎯', r'Choose the vocabulary word that best fits each sentence\.'), '', f)
    h = head(h, GRAM, f, sub='Fix the verbs in a sentence.', slug='gram-irr3')
    h = must(h, '<p>Someone has already edited the first one. Read the before and the after side by side before you touch the second.</p>', '<p>Read the before and the after.</p>', f)
    h = must(h, '<li>List the changes. How many are capitals? How many are punctuation?</li>\n<li>Did the editor change any of the writer&rsquo;s actual words?</li>',
               '<li>Which verbs changed?</li>\n<li>What did each one become?</li>', f)
    h = must(h, '<p>Editing changes how the words are <em>presented</em> &mdash; never which words the writer chose. Every original word is still there.</p>',
               '<p><em>Goed</em> became <em>went</em> and <em>finded</em> became <em>found</em>. Irregular verbs change the whole word for the past, not just the ending.</p>', f)
    h = must(h, '<p style="margin-top:10px;font-size:13px;color:#3A4A6B;"><strong>Notice:</strong> neither verb takes <em>-ed</em>. They change their whole middle instead.</p>', '', f)
    h = must(h, '<strong>Now you.</strong> Rewrite this with the correct past forms.', '<strong>Now you.</strong> Fix this sentence.', f)
    h = head(h, SPELL, f, sub='Find the misspelled words.', slug='spell-pre3')
    h = spell_common(h, f)
    h = must(h, '<strong>Proofreader!</strong> A prefix never changes the base word &mdash; so spell the base first, then stick the prefix on. Each sentence has <strong>two</strong> misspelled words. Tap any word you want to check.',
               '<strong>Proofreader!</strong> A prefix never changes the base word. Spell the base word first, then add the prefix.', f)
    h = rwm(h, f)
    return h

def day4(h, f):
    h = common(h, f, 4)
    h = head(h, '🪶 Poetry', f, sub='The limerick pattern', slug='poem-lim2')
    h = must(h, 'Copy the rhyme pattern into your journal as letters: A, A, B, B, A. Then check the second limerick against it. Does it fit?',
               'Say the rhyme pattern as letters: A, A, B, B, A. Then check the second limerick against it. Does it fit?', f)
    h = head(h, MORPH, f, sub='Roll a word and tell what it means.', slug='morph-dice')
    h = must(h, '<p>Before you start: say what the word part does from memory, then roll.</p>', '<p>Before you roll, say out loud what <strong>in-</strong> and <strong>im-</strong> mean.</p>', f)
    h = must(h, '<strong>Dice Roll Challenge!</strong> Roll a word, then say out loud what it means and how the word part changed it. Tap to check yourself.', '<strong>Dice Roll Challenge!</strong>', f)
    h = head(h, '🔤 Vocabulary: Justify Your Choice', f, sub='Use a word to tell about the story.', slug='vsentence79', newtitle='🔤 Vocabulary')
    h = resub(h, callout('🎯', r'Choose one word\. Write a sentence explaining how it connects to a moment in Ch\. 7–9\.'), '', f, flags=re.S)
    h = head(h, GRAM, f, sub='Fix it in passes.', slug='gram-pass3')
    h = must(h, '<p>Everything you have learned this year is fair game in this passage. Read it like the person who has to fix it, not the person who wrote it.</p>',
               '<p>This passage has mistakes from things you learned this year. Fix it like an editor.</p>', f)
    h = must(h, '<li>Now everything else &mdash; commas, verb forms, endings.</li>', '<li>Now verbs and commas. Is every verb the right past form? Does a comma join two complete thoughts?</li>', f)
    h = must(h, '<p>Work in passes, not all at once: capitals, then apostrophes, then the rest. Three quick trips through a passage beat one slow one &mdash; that is how an editor actually reads.</p>',
               '<p>Work in passes, not all at once: capitals, then apostrophes, then verbs and commas. That is how an editor reads.</p>', f)
    h = must(h, '<strong>Your turn.</strong> A full editing pass. Tap <strong>every</strong> word that needs fixing &mdash; capitals, apostrophes, commas, verb forms, anything from this year.',
               '<strong>Your turn.</strong> Tap <strong>every</strong> word that needs fixing.', f)
    h = must(h, '<p>These verbs change their middles for the past instead of taking an ending. There is no rule for them &mdash; you learn them one at a time.</p>',
               '<p>These verbs change the whole word for the past instead of adding <em>-ed</em>. You learn them one at a time.</p>', f)
    h = head(h, SPELL, f, sub='Roll a word and split it.', slug='spell-pre4')
    h = spell_common(h, f)
    h = must(h, '<strong>Prefix Dice!</strong> Roll a word, say it out loud, decide &mdash; then tap to check yourself.', '<strong>Prefix Dice!</strong>', f)
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
    how['icehole'] = DO['icehole']
    io.open(os.path.join(HERE, 'how_wk27.json'), 'w', encoding='utf-8').write(json.dumps(how, ensure_ascii=False, indent=1))
    print('reused:', sorted(k for k in USED if k in OLD))
    print('new lines:', sorted(how))
