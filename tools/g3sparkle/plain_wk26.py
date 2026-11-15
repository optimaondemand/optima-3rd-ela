#!/usr/bin/env python3
"""Week 26 plain-language pass (The Lion, the Witch and the Wardrobe, Ch. 4-6; Narnia page template, as week 25).

Same rules as plain_wk18-24 (Bethany, Nov 8 2026). Reads ~/g3w26/pristine-orig (the week 25 files after
acc_wk26.py), writes ~/g3w26/pristine. Every replacement is asserted. Re-runnable."""
import io, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC, DST = os.path.expanduser('~/g3w26/pristine-orig'), os.path.expanduser('~/g3w26/pristine')
DAYS = ['lesson-26-1-lww.html', 'lesson-26-2-lww.html', 'lesson-26-3-lww.html', 'lesson-26-4-lww.html']
FLU = 'lesson-26-fluency.html'

OLD = {}
for w in range(18, 26):
    for k, v in json.load(io.open(os.path.join(HERE, 'how_wk%d.json' % w), encoding='utf-8')).items(): OLD.setdefault(k, v)
NEW = {
 'morph-form1':  'Read the four words and their parts. Think about the question. Then tap See what was hiding. Last, type the missing part of each word and tap Check My Work.',
 'vsentence46':  'Choose one word. Write one sentence that uses it to tell about something in Chapters 4 to 6.',
 'gram-tense1':  'Read The Rule box. Think about the question, then tap Now check your thinking. Then tap every verb in the passage that slipped out of the past tense. Last, answer the question in the box.',
 'gram-tense2':  'Read the four sentences and find the verb that slipped. Tap Now check your thinking. Next, tap every word in the paragraph that is wrong. Last, answer the question in the box.',
 'gram-tense3':  'Read the before and after, then tap Check yourself. Rewrite the two sentences so every verb is in the past tense. Write them in the box, and say how many verbs you changed.',
 'gram-pass2':   'Think about the question, then tap Check yourself. Tap every word that needs fixing: capitals, verbs that slipped, and the word before a missing comma. Then tap See the answers, and answer the question in the box.',
 'spell-beats1': 'Clap the words in Group A and Group B. Think about the questions, then tap See the Rule. Last, tap each of the nine words, and tap how many beats it has.',
 'spell-beats2': 'Read the rule. Then in each row, tap the one word that matches what the row asks for.',
 'spell-beats3': 'Read the rule. Say each word in chunks. Then tap the card to see the beats.',
 'spell-beats4': 'Tap Roll the dice. Split the word into beats out loud, and say how you knew. Then tap Check my answer. Roll all six words.',
 'poem-windy1':  'Read the poem out loud. Then answer the question: who is riding by?',
 'poem-windy2':  'Read the poem out loud again. Then answer the question: how do you know the rider is the wind? Say it out loud. You do not need to write it.',
 'look-ch46':    'There are no new chapters today. Look back through Chapters 4 to 6 in your book. Then answer the three questions below.',
 'ww-choice1':   'Read Clara’s before and after. Then write your paragraph about a character’s choice in Chapters 4 to 6: name the choice, give the reason, and tell what happened because of it.',
 'ww-connect':   'Read Clara’s revision. Then add one connecting word to your paragraph, like because or as a result, and write the new version in the box.',
 'ww-together':  'Read Clara’s complete draft. Then put your opening, your evidence and your closing together into one paragraph, with connecting words.',
 'ww-polish':    'Read Clara’s final change. Then find one weak word in your paragraph, like good or bad, and write your paragraph again with a stronger word.',
 'delight':      'Read what is on the sweet. Tap the right answer. A right answer adds a sweet to the box.',
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

LI_OLD = ('    <li><strong>Name the choice:</strong> Point to the moment a character decides something.</li>\n'
          '    <li><strong>Follow what happens because of it:</strong> Consequences can arrive pages later &mdash; keep watching.</li>\n'
          '    <li><strong>Ask what they knew when they chose:</strong> Did the character understand what would happen, or not yet?</li>')
LI_NEW = ('    <li><strong>Name the choice:</strong> Find the moment a character decides something.</li>\n'
          '    <li><strong>Follow what happens:</strong> What happens because of that choice? It may come pages later.</li>\n'
          '    <li><strong>Ask what they knew:</strong> Did the character know what would happen?</li>')
READT = {1: ('📖 Read: Ch. 4', 'Turkish Delight', 'read-ch'), 2: ('📖 Read: Ch. 5', 'Back on This Side of the Door', 'read-ch'),
         3: ('📖 Read: Ch. 6', 'Into the Forest', 'read-ch'), 4: ('📖 Look Back: Ch. 4–6', 'No new chapters today', 'look-ch46')}
WW = {1: 'ww-choice1', 2: 'ww-connect', 3: 'ww-together', 4: 'ww-polish'}
CHECK = {1: ('I answered all 3 chapter questions with evidence.', 'I answered all 3 chapter questions with details from the book.'),
         2: ('I answered all 3 chapter questions with evidence.', 'I answered all 3 chapter questions with details from the book.'),
         3: ('I answered all 3 reading questions with text evidence.', 'I answered all 3 chapter questions with details from the book.'),
         4: ('I answered all 3 questions with clear evidence and explanation.', 'I answered all 3 questions with details from the book.')}

def common(h, f, d):
    # warm-up
    h = head(h, '📚 What Good Readers Do', f, sub='What to watch for while you read', slug='readers')
    h = must(h, LI_OLD, LI_NEW, f)
    h = must(h, '<p>Good readers <strong>track the choices characters make</strong> and what those choices cost. In a story, almost nothing that goes wrong is an accident &mdash; someone decided something first.</p>',
               '<p>Good readers <strong>track the choices characters make</strong> and what those choices cost.</p>', f)
    h = must(h, '<p class="socratic-q"><strong>Track choices and consequences.</strong></p>', '<p class="socratic-q"><strong>Follow each choice to what it causes.</strong></p>', f)
    h = h.replace('<p class="socratic-q">As you read today, ask yourself: ', '<p class="socratic-q">Ask yourself: ')
    h = must(h, "<div class=\"thinking-stop\">💭 Keep this question in your mind as you read — you'll answer it in the Reading tab.</div>", '', f)
    h = head(h, '✏️ Daily Oral Language', f, sub='Study the model. Then fix a sentence.', slug='dol')
    h = must(h, '<p>The first sentence is <strong>correct</strong>. Tap the highlighted words to see what is done right. Then use the model to fix the second sentence.</p>', '', f)
    h = must(h, 'Your mind is warmed up. Let&rsquo;s sharpen your words and skills.', 'Next: word study.', f)
    h = must(h, 'Words and skills sharpened. Time to open the book.', 'Next: reading.', f)
    h = must(h, 'Great reading work! Now bring your thinking to the assignment.', 'Next: turn in your work.', f)
    # reading
    t, sub, slug = READT[d]
    h = head(h, 'Reading: Ch. 4–6', f, sub=sub, slug=slug, newtitle=t)
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
    return h

def rwm(h, f):
    h = resub(h, r'<div class="rwm-header">📖 RWM (?:&mdash;|—) Read like a Reader, Read like a Writer, Mimic</div>',
               '<div class="rwm-header">📖 Read Like a Writer</div>\n' + do_line('rwm'), f)
    h = h.replace("{ title: '📖 RWM — READ LIKE A READER / WRITER / MIMIC'", "{ title: '📖 READ LIKE A WRITER'")
    for a, b in (('Read like a Reader', 'Read like a reader'), ('Read like a Writer', 'Read like a writer'), ('Mimic', 'Write your own')):
        h = h.replace('data-label="RWM &mdash; %s"' % a, 'data-label="%s"' % b).replace('data-label="RWM — %s"' % a, 'data-label="%s"' % b)
    return h

GRAM = '✏️ Grammar: Verb tense consistency'
SPELL = '🔠 Spelling: Academic vocabulary syllable practice'
MORPH = '🌱 Morphology: form'
RULE1 = '<div class="callout callout-gold" style="margin-bottom:14px;background:#FFF8E8;border:2px solid #F5E6C8;border-left:5px solid #C7922C;border-radius:10px;padding:14px 18px;"><span class="callout-icon">&#x1F4D6;</span><p style="font-size:15px;color:#0E1C42;line-height:1.6;"><strong>The Rule:</strong> The long words that school asks you to use &mdash; <em>describe</em>, <em>evidence</em>, <em>compare</em> &mdash; are not harder than story words. They just have more beats. Count the vowel <em>sounds</em>: one vowel sound, one syllable. That tells you how many chunks to read.</p></div>'
def day1(h, f):
    h = common(h, f, 1)
    h = head(h, '🌱 Morphology: Root/base: form means shape', f, sub='One word part in four words', slug='morph-form1', newtitle=MORPH)
    h = must(h, '<p>Fill in the missing part after the prefix to build the word.</p>', '<p><strong>Build the word.</strong></p>', f)
    h = head(h, '🔤 Vocabulary: Decode &amp; Discover', f, sub='Three words from Ch. 4–6', slug='vocabcloze', newtitle='🔤 Vocabulary')
    h = head(h, GRAM, f, sub='Keep every verb in the same time', slug='gram-tense1')
    h = must(h, '<strong>Your turn.</strong> Tap <strong>every</strong> word in the passage that needs fixing. The passage only finishes when you have found them all &mdash; count first, then start tapping. The passage starts in the past and keeps slipping. Every slipped verb needs catching.',
               '<strong>Your turn.</strong> The passage starts in the past. Tap every verb that slips out of the past.', f)
    h = head(h, SPELL, f, sub='Count the beats in long school words', slug='spell-beats1')
    h = must(h, RULE1, '', f)
    h = must(h, '<strong>Practice: Sort the words.</strong> Clap each word, then tap the column for how many beats you heard.', '<strong>Sort the Words!</strong>', f)
    return h

def day2(h, f):
    h = common(h, f, 2)
    h = head(h, '🪶 Poetry', f, sub='A poem that turns the wind into a rider', slug='poem-windy1')
    h = head(h, MORPH, f, sub='Match each word to its meaning.', slug='morph2')
    h = must(h, '<p>Before you start: find the word part, then read what is left.</p>', '<p>Find <strong>form</strong> in each word. Then look at what is left.</p>', f)
    h = must(h, '<strong>Practice: Match the Word to Its Meaning!</strong> Tap a word, then tap what it means.', '<strong>Match the Word to Its Meaning!</strong>', f)
    h = head(h, '🔤 Vocabulary: Identify &amp; Match', f, sub='Four words from Ch. 4–6', slug='vmatch', newtitle='🔤 Vocabulary')
    h = resub(h, callout('🎯', r'<strong>Vocabulary Match:</strong> Tap a word, then tap its meaning\. Use what you know from your reading\.'), '', f)
    h = head(h, GRAM, f, sub='Find the verb that slipped. Then fix a paragraph.', slug='gram-tense2')
    h = must(h, '<p>Identify the key word or pattern in each sentence. Think: what rule does it follow?</p>', '<p>In each sentence, one verb slipped into a different time. Find it.</p>', f)
    h = must(h, '<strong>Your turn.</strong> Same job, but the mistakes are not all the same kind this time. Tap <strong>every</strong> word that is wrong.',
               '<strong>Your turn.</strong> The mistakes in this paragraph are not all the same kind. Tap <strong>every</strong> word that is wrong.', f)
    h = head(h, SPELL, f, sub='How many beats?', slug='spell-beats2')
    h = must(h, '<div class="callout callout-info" style="margin-bottom:14px;"><span class="callout-icon">&#x1F440;</span><p>Before you start: clap the word first, then look at it.</p></div>', '', f)
    h = must(h, '<strong>Beat Detective!</strong> Only one word in each row has the number of beats named above it.', '<strong>Beat Detective!</strong>', f)
    h = rwm(h, f)
    return h

def day3(h, f):
    h = common(h, f, 3)
    h = head(h, MORPH, f, sub='Build four words.', slug='morph-struct3')
    h = must(h, '<p>Before you start: read the parts aloud, push them together, then write the word.</p>', '<p>Say each part out loud. Then say them together as one word.</p>', f)
    h = must(h, '<strong>Build the word.</strong> Put the parts together and type what they make.', '<strong>Build the word.</strong>', f)
    h = head(h, '🔤 Vocabulary: Use the Words', f, sub='Pick the word that fits.', slug='vselect', newtitle='🔤 Vocabulary')
    h = resub(h, callout('🎯', r'Choose the vocabulary word that best fits each sentence\.'), '', f)
    h = head(h, GRAM, f, sub='Rewrite it all in the past.', slug='gram-tense3')
    h = must(h, '<p>Someone has already edited the first one. Read the before and the after side by side before you touch the second.</p>', '<p>Read the before and the after.</p>', f)
    h = must(h, '<li>List the changes. How many are capitals? How many are punctuation?</li>\n<li>Did the editor change any of the writer&rsquo;s actual words?</li>',
               '<li>Which verbs changed?</li>\n<li>What time are they all in now?</li>', f)
    h = must(h, '<p>Editing changes how the words are <em>presented</em> &mdash; never which words the writer chose. Every original word is still there.</p>',
               '<p><em>Sees</em> became <em>saw</em> and <em>stops</em> became <em>stopped</em>. Now every verb is in the past, like <em>walked</em> and <em>stared</em>.</p>', f)
    h = head(h, SPELL, f, sub='Split each word into beats.', slug='spell-beats3')
    h = must(h, '<div class="callout callout-info" style="margin-bottom:14px;"><span class="callout-icon">&#x1F440;</span><p>Before you start: clap it, count the beats, then decide where the splits go.</p></div>', '', f)
    h = resub(h, r'\s*<p>These are words your teachers use every day\. Split each one before you tap &mdash; then check whether your ear was right\.</p>', '', f)
    h = must(h, '<strong>Split it!</strong> Say the word in chunks, then tap the card to see the beats.', '<strong>Split it!</strong>', f)
    h = rwm(h, f)
    return h

def day4(h, f):
    h = common(h, f, 4)
    h = head(h, '🪶 Poetry', f, sub='When the picture replaces the thing', slug='poem-windy2')
    h = head(h, MORPH, f, sub='Roll a word and tell what it means.', slug='morph-dice')
    h = must(h, '<p>Before you start: say what the word part does from memory, then roll.</p>', '<p>Before you roll, say out loud what <strong>form</strong> means.</p>', f)
    h = must(h, '<strong>Dice Roll Challenge!</strong> Roll a word, then say out loud what it means and how the word part changed it. Tap to check yourself.', '<strong>Dice Roll Challenge!</strong>', f)
    h = head(h, '🔤 Vocabulary: Justify Your Choice', f, sub='Use a word to tell about the story.', slug='vsentence46', newtitle='🔤 Vocabulary')
    h = resub(h, callout('🎯', r'Choose one word\. Write a sentence connecting it to a specific moment in Ch\. 4–6\.'), '', f)
    h = head(h, GRAM, f, sub='Fix it in passes.', slug='gram-pass2')
    h = must(h, '<p>Everything you have learned this year is fair game in this passage. Read it like the person who has to fix it, not the person who wrote it.</p>',
               '<p>This passage has mistakes from things you learned this year. Fix it like an editor.</p>', f)
    h = must(h, '<li>Now everything else &mdash; commas, verb forms, endings.</li>', '<li>Now verbs and commas. Does every verb stay in the past? Does a comma join two complete thoughts?</li>', f)
    h = must(h, '<p>Work in passes, not all at once: capitals, then apostrophes, then the rest. Three quick trips through a passage beat one slow one &mdash; that is how an editor actually reads.</p>',
               '<p>Work in passes, not all at once: capitals, then verbs, then commas. That is how an editor reads.</p>', f)
    h = must(h, '<strong>Your turn.</strong> A full editing pass. Tap <strong>every</strong> word that needs fixing &mdash; capitals, apostrophes, commas, verb forms, anything from this year.',
               '<strong>Your turn.</strong> Tap <strong>every</strong> word that needs fixing.', f)
    h = head(h, SPELL, f, sub='Roll a word and split it.', slug='spell-beats4')
    h = resub(h, r'\s*<p>Last day\. Roll a school word.*?</p>', '', f)
    h = must(h, '<strong>Academic Word Dice!</strong> Roll a word, split it into beats out loud, say how you knew &mdash; then tap to check.', '<strong>Academic Word Dice!</strong>', f)
    h = must(h, 'Split it &mdash; which vowel teams do you see?', 'Split it into beats. How many did you hear?', f)
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
    how['delight'] = DO['delight']
    io.open(os.path.join(HERE, 'how_wk26.json'), 'w', encoding='utf-8').write(json.dumps(how, ensure_ascii=False, indent=1))
    print('reused:', sorted(k for k in USED if k in OLD))
    print('new lines:', sorted(how))
