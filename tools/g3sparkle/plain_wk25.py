#!/usr/bin/env python3
"""Week 25 plain-language pass (The Lion, the Witch and the Wardrobe, Ch. 1-3; the new Narnia page template).

Same rules as plain_wk18-24 (Bethany, Nov 8 2026). Reads ~/g3w25/pristine-orig (the week 25 files after
acc_wk25.py + acc2_wk25.py), writes ~/g3w25/pristine. Every replacement is asserted. Re-runnable."""
import io, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC, DST = os.path.expanduser('~/g3w25/pristine-orig'), os.path.expanduser('~/g3w25/pristine')
DAYS = ['lesson-25-1-lww.html', 'lesson-25-2-lww.html', 'lesson-25-3-lww.html', 'lesson-25-4-lww.html']
FLU = 'lesson-25-fluency.html'

OLD = {}
for w in range(18, 25):
    for k, v in json.load(io.open(os.path.join(HERE, 'how_wk%d.json' % w), encoding='utf-8')).items(): OLD.setdefault(k, v)
NEW = {
 'morph-tele1':  'Read the four words and their parts. Think about the question. Then tap See what was hiding. Last, type each whole word and tap Check My Answers.',
 'vmatch':       'Tap a word, then tap its meaning. Match all four words.',
 'vselect':      'Read each sentence. Pick the word that fits from the list.',
 'vsentence':    'Choose one word. Write one sentence that uses it to tell about something in Chapters 1 to 3.',
 'gram-cx1':     'Read The Rule box. Think about the question, then tap Now check your thinking. Then tap the word in each sentence that the missing comma goes after. Last, answer the question in the box.',
 'gram-cx2':     'Find the connecting word in each sentence, then tap Now check your thinking. Next, tap every word in the paragraph that is wrong. Last, answer the question in the box.',
 'gram-cx3':     'Read the before and after, then tap Check yourself. Join the two sentences into one complex sentence. Write it in the box, and say which joining word you chose.',
 'gram-pass':    'Think about the question, then tap Check yourself. Tap every word that needs fixing: capitals, then apostrophes, then commas. Then tap See the answers, and answer the question in the box.',
 'spell-schwa1': 'Say the eight words in the sort out loud. Think about the three questions, then tap Now name the pattern. Last, tap each word, and tap its column.',
 'spell-schwa2': 'Read the rule. Then tap every word in the sentences that has a lazy schwa beat.',
 'spell-schwa3': 'Read the rule. Say each word the lazy way. Then tap the card to see which vowel blurred.',
 'spell-schwa4': 'Tap Roll the dice. Say the word out loud and find the lazy beat. Then tap Check my answer. Roll all six words.',
 'poem-tyger1':  'Read the poem out loud. Then answer the question: what is Blake asking the tiger?',
 'poem-tyger2':  'Read the poem out loud again. Then answer the question about Mr. Tumnus out loud. You do not need to write it.',
 'read-ch':      'Read today’s chapters in your book. Keep your lens in mind. Then answer the three questions below.',
 'look-ch':      'There are no new chapters today. Look back through Chapters 1 to 3 in your book. Then answer the three questions below.',
 'qbook':        'Answer the question in full sentences. Use details from the book.',
 'ww-brain':     'Read Clara’s brainstorm. Then look back at Chapter 1, and write two or three details Lewis uses to describe Narnia.',
 'ww-litopen':   'Read Clara’s opening. Then write your opening sentence: name the book and the author, and say what you will show about the setting.',
 'ww-evid':      'Read Clara’s evidence. Then write two evidence sentences. Use a short quote from Chapters 1 to 3, and say what it shows.',
 'ww-close':     'Read Clara’s closing. Then write your closing sentence. Say your main idea in a new way, and why it matters.',
 'wardrobe':     'Read the word on the coat. Tap the vowel that makes its lazy schwa sound. A right answer pushes the coat aside.',
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

LI_OLD = ('    <li><strong>Collect the world details:</strong> Weather, light, time of day, and what is allowed or forbidden in this place.</li>\n'
          '    <li><strong>Compare it to our world:</strong> Note what is the same as home and what could never happen here.</li>\n'
          '    <li><strong>Ask how it makes you feel:</strong> A good fantasy setting gives you a feeling before it gives you a rule.</li>')
LI_NEW = ('    <li><strong>Collect world details:</strong> Look for the weather, the light and the time of day.</li>\n'
          '    <li><strong>Compare it to our world:</strong> What is the same as home? What could never happen here?</li>\n'
          '    <li><strong>Notice the feeling:</strong> How does this place make you feel?</li>')
READT = {1: ('📖 Read: Ch. 1', 'Lucy Looks into a Wardrobe', 'read-ch'), 2: ('📖 Read: Ch. 2–3', 'What Lucy Found There; Edmund and the Wardrobe', 'read-ch'),
         3: ('📖 Look Back: Ch. 1–3', 'No new chapters today', 'look-ch'), 4: ('📖 Look Back: Ch. 1–3', 'No new chapters today', 'look-ch')}
WW = {1: 'ww-brain', 2: 'ww-litopen', 3: 'ww-evid', 4: 'ww-close'}
CHECK = {1: ('I answered all 3 chapter questions with evidence from the book.', 'I answered all 3 chapter questions with details from the book.'),
         2: ('I answered all 3 chapter questions with evidence.', 'I answered all 3 chapter questions with details from the book.'),
         3: None, 4: None}

def common(h, f, d):
    # warm-up
    h = head(h, '📚 What Good Readers Do', f, sub='What to watch for while you read', slug='readers')
    h = must(h, '<p>Good readers in a fantasy story slow down and pay attention to <strong>how the author builds the world</strong>. Details of setting, character, and pattern all work together to create meaning.</p>',
               '<p>In a fantasy story, good readers slow down and notice <strong>how the author builds the world</strong>.</p>', f)
    h = must(h, LI_OLD, LI_NEW, f)
    h = must(h, '<p class="socratic-q"><strong>Orient yourself in fantasy settings.</strong></p>', '<p class="socratic-q"><strong>Find your way around a new world.</strong></p>', f)
    h = h.replace('<p class="socratic-q">As you read today, ask yourself: ', '<p class="socratic-q">Ask yourself: ')
    h = must(h, "<div class=\"thinking-stop\">💭 Keep this question in your mind as you read — you'll answer it in the Reading tab.</div>", '', f)
    h = head(h, '✏️ Daily Oral Language', f, sub='Study the model. Then fix a sentence.', slug='dol')
    h = must(h, '<p>The first sentence is <strong>correct</strong>. Tap the highlighted words to see what is done right. Then use the model to fix the second sentence.</p>', '', f)
    h = must(h, 'Your mind is warmed up. Let&rsquo;s sharpen your words and skills.', 'Next: word study.', f)
    h = must(h, 'Words and skills sharpened. Time to open the book.', 'Next: reading.', f)
    h = must(h, 'Great reading work! Now bring your thinking to the assignment.', 'Next: turn in your work.', f)
    # reading
    t, sub, slug = READT[d]
    h = head(h, 'Reading: Ch. 1–3', f, sub=sub, slug=slug, newtitle=t)
    h = must(h, '<div class="textbox-prompt">Use evidence from the book in your answer.</div>', '', f, 3)
    for q in ('Q1 —', 'Q2 —', 'Q3 —'): h = head(h, q, f, slug='qbook')
    # assignment
    h = must(h, '<div class="activity-title">📖 Chapter Thinking</div><div class="activity-sub">Your reading responses are saved from the Reading tab.</div>',
               '<div class="activity-title">📖 Chapter Thinking</div><div class="activity-sub">Your answers from the Reading tab</div>', f)
    h = must(h, 'Your chapter answers were saved on the Reading tab. They will appear in your gathered work below.',
               'Your answers to Q1, Q2 and Q3 on the Reading tab show in your work below.', f)
    h = must(h, '<div class="activity-title">🔤 Word Study Connection</div><div class="activity-sub">Your morphology response from the Word Study tab.</div>',
               '<div class="activity-title">🔤 Word Study Check</div><div class="activity-sub">The word part work on the Word Study tab</div>', f)
    h = must(h, 'Your morphology answer was saved on the Word Study tab. It will appear in your gathered work below.',
               'Finish the word part work on the Word Study tab. It shows in your work below.', f)
    if CHECK[d]: h = must(h, CHECK[d][0], CHECK[d][1], f)
    # writer's workshop: the do line replaces the Now you try callout
    h = resub(h, r'\s*<div class="callout callout-info" style="background:#E8F1E8;border-color:#A8C8A8;margin-bottom:10px;padding:10px 14px;"><span class="callout-icon">📝</span><p style="font-size:14px;"><strong>Now you try\.</strong>.*?</p></div>', '', f)
    h = head(h, 'Writer&rsquo;s Workshop', f, slug=WW[d])
    # spelling rule shown again on Days 2-4: one line, no "This week" label
    h = h.replace('<p><strong>This week:</strong> Schwa introduction in longer words</p>', '')
    h = re.sub(r'\s*<div class="callout callout-info" style="margin-bottom:14px;"><span class="callout-icon">&#x1F442;</span><p>Before you start: find the lazy beat, and notice its vowel is not what it looks like\.</p></div>', '', h)
    return h

def rwm(h, f):
    h = resub(h, r'<div class="rwm-header">📖 RWM (?:&mdash;|—) Read like a Reader, Read like a Writer, Mimic</div>',
               '<div class="rwm-header">📖 Read Like a Writer</div>\n' + do_line('rwm'), f)
    h = h.replace("{ title: '📖 RWM — READ LIKE A READER / WRITER / MIMIC'", "{ title: '📖 READ LIKE A WRITER'")
    for a, b in (('Read like a Reader', 'Read like a reader'), ('Read like a Writer', 'Read like a writer'), ('Mimic', 'Write your own')):
        h = h.replace('data-label="RWM &mdash; %s"' % a, 'data-label="%s"' % b).replace('data-label="RWM — %s"' % a, 'data-label="%s"' % b)
    return h

GRAM = '✏️ Grammar: Complex sentences intro'
SPELL = '🔠 Spelling: Schwa introduction in longer words'
MORPH = '🌱 Morphology: tele-'
def day1(h, f):
    h = common(h, f, 1)
    h = head(h, MORPH, f, sub='One word part in four words', slug='morph-tele1')
    h = head(h, '🔤 Vocabulary: Decode &amp; Discover', f, sub='Three words from Ch. 1–3', slug='vocabcloze', newtitle='🔤 Vocabulary')
    h = must(h, '<p><strong>Build the word.</strong> Put the parts together and type what they make.</p>', '<p><strong>Build the word.</strong></p>', f)
    h = head(h, GRAM, f, sub='Two parts and a comma', slug='gram-cx1')
    h = must(h, '<strong>Your turn.</strong> Tap <strong>every</strong> word in the passage that needs fixing. The passage only finishes when you have found them all &mdash; count first, then start tapping. Every sentence here starts with a dependent clause, and every one is missing the same mark.',
               '<strong>Your turn.</strong> Each sentence starts with the part that cannot stand alone, and each one is missing a comma. Tap the word the comma goes after.', f)
    h = head(h, SPELL, f, sub='A lazy vowel that sounds like uh', slug='spell-schwa1')
    h = must(h, "<p>The schwa is the most common vowel sound in English. It sounds like 'uh' and can be spelled with any vowel: a, e, i, o, or u. Example: about — the a sounds like 'uh.' You often need to memorize which letter spells the schwa.</p>", '', f)
    h = must(h, '<p>Sort these words into the correct spelling pattern group.</p>', '<p><strong>Sort the Words!</strong></p>', f)
    return h

def day2(h, f):
    h = common(h, f, 2)
    h = head(h, '🪶 Poetry', f, sub='A poem that talks to an animal', slug='poem-tyger1')
    h = head(h, MORPH, f, sub='Match each word to its meaning.', slug='morph2')
    h = must(h, '<p>Before you start: find the word part, then read what is left.</p>', '<p>Find <strong>tele</strong> in each word. Then look at what is left.</p>', f)
    h = must(h, '<strong>Practice: Match the Word to Its Meaning!</strong> Tap a word, then tap what it means.', '<strong>Match the Word to Its Meaning!</strong>', f)
    h = head(h, '🔤 Vocabulary: Identify &amp; Match', f, sub='Four words from Ch. 1–3', slug='vmatch', newtitle='🔤 Vocabulary')
    h = resub(h, callout('🎯', r'<strong>Vocabulary Match:</strong> Tap a word, then tap its meaning\. Use what you know from your reading\.'), '', f)
    h = head(h, GRAM, f, sub='Find the connecting word. Then fix a paragraph.', slug='gram-cx2')
    h = must(h, '<p>Identify the key word or pattern in each sentence. Think: what rule does it follow?</p>', '<p>Find the connecting word in each sentence.</p>', f)
    h = must(h, '<strong>Your turn.</strong> Same job, but the mistakes are not all the same kind this time. Tap <strong>every</strong> word that is wrong.',
               '<strong>Your turn.</strong> The mistakes in this paragraph are not all the same kind. Tap <strong>every</strong> word that is wrong.', f)
    h = head(h, SPELL, f, sub='Find the schwa.', slug='spell-schwa2')
    h = resub(h, callout('&#x1F50D;', r'Tap every word with a lazy <strong>schwa</strong> beat in it\.'), '', f)
    h = rwm(h, f)
    return h

def day3(h, f):
    h = common(h, f, 3)
    h = head(h, MORPH, f, sub='Build four words.', slug='morph-struct3')
    h = must(h, '<p>Before you start: read the parts aloud, push them together, then write the word.</p>', '<p>Say each part out loud. Then say them together as one word.</p>', f)
    h = must(h, '<strong>Build the word.</strong> Put the parts together and type what they make.', '<strong>Build the word.</strong>', f)
    h = head(h, '🔤 Vocabulary: Use the Words', f, sub='Pick the word that fits.', slug='vselect', newtitle='🔤 Vocabulary')
    h = resub(h, callout('🎯', r'Choose the vocabulary word that best fits each sentence\.'), '', f)
    h = head(h, GRAM, f, sub='Join two sentences into one.', slug='gram-cx3')
    h = must(h, '<p>Someone has already edited the first one. Read the before and the after side by side before you touch the second.</p>', '<p>Read the before and the after.</p>', f)
    h = must(h, '<li>List the changes. How many are capitals? How many are punctuation?</li>\n<li>Did the editor change any of the writer&rsquo;s actual words?</li>',
               '<li>What joining word went at the front?</li>\n<li>Where did the comma go?</li>', f)
    h = must(h, '<p>Editing changes how the words are <em>presented</em> &mdash; never which words the writer chose. Every original word is still there.</p>',
               '<p><em>Although</em> went at the front. The comma went where the first part ends, after <em>frightened</em>. The two sentences became one.</p>', f)
    h = must(h, '<strong>Now you.</strong> Join these two into one complex sentence. Use <em>although</em>, <em>when</em> or <em>because</em>, and do not forget the comma.',
               '<strong>Now you.</strong> Join these two sentences with <em>although</em>, <em>when</em> or <em>because</em>. Put the joining word first, and add the comma.', f)
    h = head(h, SPELL, f, sub='Which vowel blurred?', slug='spell-schwa3')
    h = must(h, '<strong>Find the Schwa!</strong> Say the word the lazy way you really say it, then tap to see which vowel blurred.', '<strong>Find the Schwa!</strong>', f)
    h = rwm(h, f)
    return h

def day4(h, f):
    h = common(h, f, 4)
    h = head(h, '🪶 Poetry', f, sub='A creature who acts like a person', slug='poem-tyger2')
    h = head(h, MORPH, f, sub='Roll a word and tell what it means.', slug='morph-dice')
    h = must(h, '<p>Before you start: say what the word part does from memory, then roll.</p>', '<p>Before you roll, say out loud what <strong>tele</strong> means.</p>', f)
    h = must(h, '<strong>Dice Roll Challenge!</strong> Roll a word, then say out loud what it means and how the word part changed it. Tap to check yourself.', '<strong>Dice Roll Challenge!</strong>', f)
    h = head(h, '🔤 Vocabulary: Justify Your Choice', f, sub='Use a word to tell about the story.', slug='vsentence', newtitle='🔤 Vocabulary')
    h = resub(h, callout('🎯', r'Choose one word\. Write a sentence connecting it to something that happens in Ch\. 1–3\.'), '', f)
    h = head(h, GRAM, f, sub='Fix it in three passes.', slug='gram-pass')
    h = must(h, '<p>Everything you have learned this year is fair game in this passage. Read it like the person who has to fix it, not the person who wrote it.</p>',
               '<p>This passage has mistakes from things you learned this year. Fix it like an editor.</p>', f)
    h = must(h, '<li>Now everything else &mdash; commas, verb forms, endings.</li>', '<li>Now commas. Does a comma join two complete thoughts?</li>', f)
    h = must(h, '<p>Work in passes, not all at once: capitals, then apostrophes, then the rest. Three quick trips through a passage beat one slow one &mdash; that is how an editor actually reads.</p>',
               '<p>Work in passes, not all at once: capitals, then apostrophes, then commas. That is how an editor reads.</p>', f)
    h = must(h, '<strong>Your turn.</strong> A full editing pass. Tap <strong>every</strong> word that needs fixing &mdash; capitals, apostrophes, commas, verb forms, anything from this year.',
               '<strong>Your turn.</strong> Tap <strong>every</strong> word that needs fixing.', f)
    h = head(h, SPELL, f, sub='Roll a word and find its schwa.', slug='spell-schwa4')
    h = must(h, '<strong>Schwa Dice!</strong> Roll a word, say it out loud, decide &mdash; then tap to check yourself.', '<strong>Schwa Dice!</strong>', f)
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
    how['wardrobe'] = DO['wardrobe']
    io.open(os.path.join(HERE, 'how_wk25.json'), 'w', encoding='utf-8').write(json.dumps(how, ensure_ascii=False, indent=1))
    print('reused:', sorted(k for k in USED if k in OLD))
    print('new lines:', sorted(how))
