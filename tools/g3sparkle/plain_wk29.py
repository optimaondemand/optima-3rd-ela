#!/usr/bin/env python3
"""Week 29 plain-language pass (The Lion, the Witch and the Wardrobe, Ch. 13-15; Narnia page template, as weeks 25-28).

Same rules as plain_wk18-28 (Bethany, Nov 8 2026). Reads ~/g3w29/pristine-orig (the week 29 files after
acc_wk29.py + acc2_wk29.py), writes ~/g3w29/pristine. Every replacement is asserted. Re-runnable."""
import io, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC, DST = os.path.expanduser('~/g3w29/pristine-orig'), os.path.expanduser('~/g3w29/pristine')
DAYS = ['lesson-29-1-lww.html', 'lesson-29-2-lww.html', 'lesson-29-3-lww.html', 'lesson-29-4-lww.html']
FLU = 'lesson-29-fluency.html'

OLD = {}
for w in range(18, 29):
    for k, v in json.load(io.open(os.path.join(HERE, 'how_wk%d.json' % w), encoding='utf-8')).items(): OLD.setdefault(k, v)
NEW = {
 'morph-ject1':   'Read the four words and their parts. Think about the three questions, then tap See if you were right. Last, type the missing part of each word and tap Check My Work.',
 'vmatch3':       'Tap a word, then tap its meaning. Match all three words.',
 'vsentence1315': 'Choose one word. Write one sentence that tells how it connects to the theme you are building.',
 'gram-dlg1':     'Read The Rule box. Think about the question, then tap Now check your thinking. Then tap the three words in the passage that have a dialogue mistake. Last, answer the question in the box.',
 'gram-dlg2':     'Read the four sentences and find each mistake. Tap Now check your thinking. Next, tap every word in the paragraph that is wrong. Last, answer the question in the box.',
 'gram-dlg3':     'Read the before and after, then tap Check yourself. Fix the line of dialogue in the gray box. Write it in the answer box, and list the four things you changed.',
 'gram-pass5':    'Think about the question, then tap Check yourself. Tap every word that needs fixing: capitals, apostrophes, a comma, and the dialogue. Then tap See the answers, and answer the question in the box.',
 'spell-root1':   'Think about the questions, then tap Now name the pattern. Last, tap each of the eight words, and tap its column: ject or script and scribe.',
 'spell-root2':   'Read the rule. Then tap every word in the two sentences that is built from a root with parts added.',
 'spell-root3':   'Read the rule. Look hard at each word, cover it, and write it on paper. Then tap the card to check every letter.',
 'spell-root4':   'Tap Roll the dice. Say the word out loud, and name its root and the parts added. Then tap Check my answer. Roll all six words.',
 'poem-form1':    'Read the poem out loud. Count the lines and listen to the line endings. Then say which of the four kinds it is, and two reasons why. You do not need to write it.',
 'poem-sort':     'Think back to the poems you read this year. On paper, make four columns: free verse, rhymed verse, haiku and limerick. Write each poem’s name in a column.',
 'look-ch1315':   'There are no new chapters today. Look back through Chapters 13 to 15 in your book. Then answer the three questions below.',
 'ww-thm1':       'Read Clara’s before and after. Then write two or three possible themes, each as a full sentence that starts The story shows that. Last, say which one has the most proof.',
 'ww-thm2':       'Read Clara’s draft. Then draft your response: say your theme as a full sentence, give proof from two parts of the story, and explain how they connect.',
 'ww-thm3':       'Read Clara’s revision. Then add two sentences of proof from Chapter 15 to your response. Start with a joining phrase like Even more importantly.',
 'ww-thm4':       'Read how Clara put her response in order. Then write your whole response: your theme, proof from three different chapters, and a closing sentence.',
 'skip':          'Read the word on the stone. Tap the right answer. A right answer skips the stone across the river.',
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

LI_OLD = ('    <li><strong>Say the lesson in one sentence:</strong> Start with what you think the story is teaching.</li>\n'
          '    <li><strong>Find proof from across the book:</strong> Pick one detail from the beginning, one from the middle, and one from the end.</li>\n'
          '    <li><strong>Explain how each detail proves it:</strong> A theme you can only support from one page is not the theme yet.</li>')
LI_NEW = ('    <li><strong>Say the big lesson:</strong> What is the story teaching? Say it in one full sentence.</li>\n'
          '    <li><strong>Find proof all through the book:</strong> Look for one detail near the start, one in the middle, and one near the end.</li>\n'
          '    <li><strong>Check it:</strong> If only one page proves it, it is not the theme yet.</li>')
READT = {1: ('📖 Read: Ch. 13', 'Deep Magic From the Dawn of Time', 'read-ch'), 2: ('📖 Read: Ch. 14', 'The Triumph of the Witch', 'read-ch'),
         3: ('📖 Read: Ch. 15', 'Deeper Magic From Before the Dawn of Time', 'read-ch'), 4: ('📖 Look Back: Ch. 13–15', 'No new chapters today', 'look-ch1315')}
WW = {1: 'ww-thm1', 2: 'ww-thm2', 3: 'ww-thm3', 4: 'ww-thm4'}
CHECK = {1: ('I answered all 3 reading questions with evidence.', 'I answered all 3 chapter questions with details from the book.'),
         2: ('I answered all 3 reading questions with evidence.', 'I answered all 3 chapter questions with details from the book.'),
         3: ('I answered all 3 reading questions with evidence.', 'I answered all 3 chapter questions with details from the book.'),
         4: None}

def common(h, f, d):
    h = head(h, '📚 What Good Readers Do', f, sub='What to watch for while you read', slug='readers')
    h = must(h, LI_OLD, LI_NEW, f)
    h = must(h, '<p>Good readers <strong>explain the theme using details from across the whole story</strong>. A theme is not hiding on one page &mdash; it is built from the beginning, the middle, and the end together.</p>',
               '<p>Good readers <strong>explain the theme using details from across the whole story</strong>. A <em>theme</em> is the big lesson a story teaches, said as a full sentence.</p>', f)
    h = must(h, '<p class="socratic-q"><strong>Explain theme using details from across the story.</strong></p>', '<p class="socratic-q"><strong>Find the big lesson, and the details that prove it.</strong></p>', f)
    h = h.replace('<p class="socratic-q">As you read today, ask yourself: ', '<p class="socratic-q">Ask yourself: ')
    h = must(h, "<div class=\"thinking-stop\">💭 Keep this question in your mind as you read — you'll answer it in the Reading tab.</div>", '', f)
    h = head(h, '✏️ Daily Oral Language', f, sub='Study the model. Then fix a sentence.', slug='dol')
    h = must(h, '<p>The first sentence is <strong>correct</strong>. Tap the highlighted words to see what is done right. Then use the model to fix the second sentence.</p>', '', f)
    h = must(h, 'Your mind is warmed up. Let&rsquo;s sharpen your words and skills.', 'Next: word study.', f)
    h = must(h, 'Words and skills sharpened. Time to open the book.', 'Next: reading.', f)
    h = must(h, 'Great reading work! Now bring your thinking to the assignment.', 'Next: turn in your work.', f)
    t, sub, slug = READT[d]
    h = head(h, 'Reading: Ch. 13–15', f, sub=sub, slug=slug, newtitle=t)
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

GRAM = '✏️ Grammar: Dialogue punctuation review'
SPELL = '🔠 Spelling: Review roots and affixes in literary vocabulary'
BEFORE_SP = '<div class="callout callout-info" style="margin-bottom:14px;"><span class="callout-icon">&#x1F5C2;&#xFE0F;</span><p>Before you start: break each word into parts before spelling it.</p></div>'
WIDER = '<p>Many words in this novel contain roots and affixes you have studied this year. When you meet an unfamiliar word, ask: Do I see a root (form, script, ject, port, spect) or an affix (re-, un-, -tion, -ful)?</p>'
def spell_common(h, f):
    h = must(h, BEFORE_SP, '', f)
    return h

def day1(h, f):
    h = common(h, f, 1)
    h = head(h, '🌱 Morphology: Root/base: ject means throw', f, sub='A word part that means throw', slug='morph-ject1', newtitle='🌱 Morphology: ject')
    h = must(h, '<p>Root/base: ject means throw.</p>', '<p>The root <strong>ject</strong> means <strong>throw</strong>.</p>', f)
    h = head(h, '🔤 Vocabulary: Decode &amp; Discover', f, sub='Three words from Ch. 13–15', slug='vocabcloze', newtitle='🔤 Vocabulary')
    h = head(h, GRAM, f, sub='Where the marks go when someone speaks', slug='gram-dlg1')
    h = must(h, '<strong>Your turn.</strong> Tap <strong>every</strong> word in the passage that needs fixing. The passage only finishes when you have found them all &mdash; count first, then start tapping. Three dialogue mistakes in this passage, and they are not all the same.',
               '<strong>Your turn.</strong> Three words in this passage have a dialogue mistake. Tap all three.', f)
    h = must(h, '<p>When writing dialogue: (1) Put quotation marks around the exact words spoken. (2) The first word of speech gets a capital letter. (3) Punctuation — comma, period, ?, ! — goes INSIDE the closing quotation mark. (4) The dialogue tag (he said, she asked) comes outside the quotation marks.</p>',
               '<p>Four rules for dialogue: (1) Quotation marks go around the exact words someone says. (2) The first word they say gets a capital letter. (3) The comma, period, question mark or exclamation mark goes INSIDE the closing quotation mark. (4) The tag, like <em>he said</em> or <em>she asked</em>, goes outside the quotation marks.</p>', f)
    h = head(h, SPELL, f, sub='Long words built from parts you know', slug='spell-root1')
    h = must(h, WIDER, '', f)
    h = must(h, '<p>Sort these words into the correct spelling pattern group.</p>', '<p><strong>Sort the Words!</strong></p>', f)
    return h

def day2(h, f):
    h = common(h, f, 2)
    h = head(h, '🪶 Poetry', f, sub='Which kind of poem is it?', slug='poem-form1')
    h = head(h, '🌱 Morphology: ject', f, sub='Match each word to its meaning.', slug='morph2')
    h = must(h, '<p>Before you start: find the word part, then read what is left.</p>', '<p>Find <strong>ject</strong> in each word. Then look at the part in front of it.</p>', f)
    h = must(h, '<strong>Practice: Match the Word to Its Meaning!</strong> Tap a word, then tap what it means.', '<strong>Match the Word to Its Meaning!</strong>', f)
    h = head(h, '🔤 Vocabulary: Identify &amp; Match', f, sub='Three words from Ch. 13–15', slug='vmatch3', newtitle='🔤 Vocabulary')
    h = resub(h, callout('🎯', r'<strong>Vocabulary Match:</strong> Tap a word, then tap its meaning\. Use what you know from your reading\.'), '', f)
    h = head(h, GRAM, f, sub='Find the mistake in each sentence. Then fix a paragraph.', slug='gram-dlg2')
    h = must(h, '<p>Identify the key word or pattern in each sentence. Think: what rule does it follow?</p>', '<p>Look at the capitals and marks around the spoken words. What is wrong in each sentence?</p>', f)
    h = must(h, '<strong>Your turn.</strong> Same job, but the mistakes are not all the same kind this time. Tap <strong>every</strong> word that is wrong.',
               '<strong>Your turn.</strong> Tap <strong>every</strong> word that is wrong.', f)
    h = head(h, SPELL, f, sub='Find the long words built from parts.', slug='spell-root2')
    h = spell_common(h, f)
    h = must(h, 'The</span> <span class="spotter-word" onclick="spellSpotAll(this,\'spellSpot1\')" data-correct="false">words</span> <span class="spotter-word" onclick="spellSpotAll(this,\'spellSpot1\')" data-correct="false">of</span> <span class="spotter-word" onclick="spellSpotAll(this,\'spellSpot1\')" data-correct="false">Aslan</span> <span class="spotter-word" onclick="spellSpotAll(this,\'spellSpot1\')" data-correct="false">were</span>',
               'What</span> <span class="spotter-word" onclick="spellSpotAll(this,\'spellSpot1\')" data-correct="false">Aslan</span> <span class="spotter-word" onclick="spellSpotAll(this,\'spellSpot1\')" data-correct="false">said</span> <span class="spotter-word" onclick="spellSpotAll(this,\'spellSpot1\')" data-correct="false">was</span>', f)
    h = must(h, '<span class="spotter-word" onclick="spellSpotAll(this,\'spellSpot1\')" data-correct="false">freeing</span> <span class="spotter-word" onclick="spellSpotAll(this,\'spellSpot1\')" data-correct="false">Edmund</span> <span class="spotter-word" onclick="spellSpotAll(this,\'spellSpot1\')" data-correct="false">became</span>',
               '<span class="spotter-word" onclick="spellSpotAll(this,\'spellSpot1\')" data-correct="false">to</span> <span class="spotter-word" onclick="spellSpotAll(this,\'spellSpot1\')" data-correct="false">save</span> <span class="spotter-word" onclick="spellSpotAll(this,\'spellSpot1\')" data-correct="false">Edmund</span> <span class="spotter-word" onclick="spellSpotAll(this,\'spellSpot1\')" data-correct="false">was</span>', f)
    h = must(h, '<p>Find the root ject in each word and explain what the prefix adds to the meaning.</p>', '<p>Here is what each front part adds to <strong>ject</strong>.</p>', f)
    h = rwm(h, f)
    return h

def day3(h, f):
    h = common(h, f, 3)
    h = head(h, '🌱 Morphology: ject', f, sub='Build four words.', slug='morph3')
    h = must(h, '<p>Before you start: read the parts aloud, push them together, then write the word.</p>', '<p>Say each part out loud. Then say them together as one word.</p>', f)
    h = must(h, '<strong>Build the word.</strong> Put the parts together and type what they make.', '<strong>Build the word.</strong>', f)
    h = head(h, '🔤 Vocabulary: Use the Words', f, sub='Pick the word that fits.', slug='vselect', newtitle='🔤 Vocabulary')
    h = resub(h, callout('🎯', r'Choose the vocabulary word that best fits each sentence\.'), '', f)
    h = head(h, GRAM, f, sub='Fix a line of dialogue.', slug='gram-dlg3')
    h = must(h, '<p>Someone has already edited the first one. Read the before and the after side by side before you touch the second.</p>', '<p>Read the before and the after.</p>', f)
    h = must(h, '<li>Did the editor change any of the writer&rsquo;s actual words?</li>', '<li>Did the editor change any of the words Lucy said?</li>', f)
    h = must(h, '<strong>Now you.</strong> Fix everything wrong with this line of dialogue. There are four things.', '<strong>Now you.</strong> Fix this line. There are four things to fix.', f)
    h = head(h, SPELL, f, sub='Spell long words from memory.', slug='spell-root3')
    h = spell_common(h, f)
    h = must(h, '<strong>Cover, Write, Check!</strong> Find the root first, then spell out from it. Look hard at the word, cover it with your hand, write it in your notebook, <em>then</em> tap to check every letter.', '<strong>Cover, Write, Check!</strong> Find the root first.', f)
    h = rwm(h, f)
    return h

def day4(h, f):
    h = common(h, f, 4)
    h = head(h, '🪶 Poetry', f, sub='Sort the poems you read this year', slug='poem-sort')
    h = must(h, 'In your journal, make a four-column chart: free verse, rhymed verse, haiku, limerick. Put every poem you have read this year into a column. If you cannot decide, write down what is confusing you.',
               'Which column does each poem you read this year go in? If you cannot decide, say what makes it hard.', f)
    h = head(h, '🌱 Morphology: ject', f, sub='Roll a word and tell what it means.', slug='morph-dice')
    h = must(h, '<p>Before you start: say what the word part does from memory, then roll.</p>', '<p>Before you roll, say out loud what <strong>ject</strong> means.</p>', f)
    h = must(h, '<strong>Dice Roll Challenge!</strong> Roll a word, then say out loud what it means and how the word part changed it. Tap to check yourself.', '<strong>Dice Roll Challenge!</strong>', f)
    h = head(h, '🔤 Vocabulary: Justify Your Choice', f, sub='Use a word to tell about the story.', slug='vsentence1315', newtitle='🔤 Vocabulary')
    h = resub(h, callout('🎯', r'Choose one word\. Write a sentence explaining how it connects to the theme you have been developing\.'), '', f)
    h = head(h, GRAM, f, sub='Fix it in passes.', slug='gram-pass5')
    h = must(h, '<p>Everything you have learned this year is fair game in this passage. Read it like the person who has to fix it, not the person who wrote it.</p>',
               '<p>This passage needs capitals, apostrophes, a comma and one dialogue fix. Fix it like an editor.</p>', f)
    h = must(h, '<li>Now everything else &mdash; commas, verb forms, endings.</li>', '<li>Last, the comma and the dialogue.</li>', f)
    h = must(h, '<strong>Your turn.</strong> A full editing pass. Tap <strong>every</strong> word that needs fixing &mdash; capitals, apostrophes, commas, verb forms, anything from this year.',
               '<strong>Your turn.</strong> Tap <strong>every</strong> word that needs fixing.', f)
    h = head(h, SPELL, f, sub='Roll a word and find its parts.', slug='spell-root4')
    h = spell_common(h, f)
    h = must(h, '<strong>Root and Affix Dice!</strong> Roll a word, say it out loud, decide &mdash; then tap to check yourself.', '<strong>Root and Affix Dice!</strong>', f)
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
    how['skip'] = DO['skip']
    io.open(os.path.join(HERE, 'how_wk29.json'), 'w', encoding='utf-8').write(json.dumps(how, ensure_ascii=False, indent=1))
    print('reused:', sorted(k for k in USED if k in OLD))
    print('new lines:', sorted(how))
