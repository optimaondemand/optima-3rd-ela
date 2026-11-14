#!/usr/bin/env python3
"""Week 22 plain-language pass (The Whipping Boy wrap-up, no new chapters).

Same rules as plain_wk18.py (Bethany, Nov 8 2026). Reads ~/g3w22/pristine-orig
(the week 22 files after acc_wk22.py), writes ~/g3w22/pristine. Every
replacement is asserted. Re-runnable. Helpers copied from plain_wk21.py."""
import io, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC, DST = os.path.expanduser('~/g3w22/pristine-orig'), os.path.expanduser('~/g3w22/pristine')
DAYS = ['lesson-22-1-wb.html', 'lesson-22-2-wb.html', 'lesson-22-3-wb.html', 'lesson-22-4-wb.html']
FLU = 'lesson-22-fluency.html'

WK18 = {}
for w in (18, 19, 20, 21):
    for k, v in json.load(io.open(os.path.join(HERE, 'how_wk%d.json' % w), encoding='utf-8')).items(): WK18.setdefault(k, v)
NEW22 = {
 'morph-struct1': 'Read the three words and their parts. Think about the three questions. Then tap See what was hiding. Type the missing word part in each box and tap Check My Work. Last, answer the question in the box.',
 'morph-struct3': 'Say the parts out loud. Type the whole word in the box. Then tap Check My Answers.',
 'gram-pro1':     'Read the sentence in the box and tap Now check your thinking. Then tap each pronoun, and tap its column: does the action, receives the action, or shows belonging. Last, answer the question in the box.',
 'gram-pro2':     'Read the Remember box. Then tap every pronoun in each sentence. There are three in each one. Last, answer the question in the box.',
 'gram-pro3':     'Read the Remember box. Then type a word from the word bank in each blank, and tap Check My Answers. Last, answer the question in the box.',
 'spell-comp1':   'Say the words out loud. Think about the three questions, then tap Now name the pattern. Last, tap each of the eight words, and tap its column: compound word or not.',
 'spell-comp2':   'Read the rule. Then in each row, tap the one compound word.',
 'spell-comp3':   'Read the two small words on each card. Tap the card to join them into one word. Then answer the question in the box.',
 'spell-comp4':   'Tap Roll the dice. Say the word out loud, and say the two small words that make it. Then tap Check my answer. Roll all six words.',
 'poem-cricket':  'Read the poem out loud again. Then answer the question in the box.',
 'readrev-book':  'There are no new chapters today. Read the two Pause and Think questions. Then look back through the whole book to find your answers. You do not write these answers.',
 'answer':        'Read the question. Then write your answer in the box.',
 'ww-specific':   'Read Clara’s vague and specific sentences. Then find one vague sentence in your comparison paragraph. Write it again with a chapter number.',
 'ww-theme':      'Read Clara’s two conclusions. Then write your conclusion again, and add a sentence that says what the story teaches.',
 'ww-pronoun':    'Read how Clara fixed a pronoun. Then find one pronoun in your comparison paragraph. Check it, and write the sentence the right way.',
 'ww-share':      'Read your comparison paragraph out loud. Then write what you noticed when you heard it.',
 'castle':        'Read the question. Tap the answer you think is right. A right answer lays the next stone in the castle.',
}
NEW = NEW22
for k in NEW: assert k not in WK18, k
DO = dict(WK18); DO.update(NEW)
USED = set()
def do_line(slug):
    USED.add(slug)
    return '<p class="g3-do" data-say="%s"><b>What to do:</b> %s</p>' % (slug, DO[slug])

def must(h, old, new, f, n=1):
    c = h.count(old)
    if c != n:
        sys.exit('%s: expected %d of %r, found %d' % (f, n, old[:100], c))
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


def common(h, f, day):
    h = must(h, '<div class="thinking-stop">💭 Think about this as you read today — you don\'t need to write anything here.</div>', '', f)
    h = head(h, '📚 What Good Readers Do', f, sub='What to watch for while you read', slug='readers')
    h = head(h, '✏️ Daily Oral Language', f, sub='Study the model. Then fix a sentence.', slug='dol')
    h = resub(h, r'\s*<p>The first sentence is <strong>correct</strong>\. Tap the parts you notice.*?</p>', '', f)
    # transitions
    h = must(h, 'Now that your mind is warmed up, let&rsquo;s sharpen your words and skills.', 'Next: word study.', f)
    h = must(h, 'Your words and skills are sharp. Time to open the book.', 'Next: reading.', f)
    h = must(h, 'You&rsquo;ve read and noticed. Now answer the questions and submit your work.', 'Next: answer the questions and turn in your work.', f)
    # reading tab
    h = must(h, '<div class="thinking-stop">💭 Think: How will your character help someone in your story?</div>', '', f)
    h = h.replace('<div class="thinking-stop">💭 Pause and think about this — no need to write.</div>', '')
    h = resub(h, r'\s*<div class="key-concept" style="background:#F0E8FF;border-color:#D8CCF0;margin-bottom:14px;">\s*<div class="key-concept-label" style="color:#6B4FB0;">💎 As you read, notice:</div>\s*<p>.*?</p>\s*</div>', '', f)
    h = resub(h, r'\s*<div class="callout callout-info" style="margin-bottom:14px;">\s*<span class="callout-icon">📕</span>\s*<p><strong>You have finished the novel\.</strong>.*?</p>\s*</div>', '', f)
    h = resub(h, r'(<div class="activity-sub">)A key theme from Synthesis: [^<]*(</div>)', r'\1A moment from the book\2', f)
    # assignment
    h = head(h, '📖 Chapter Thinking', f, sub='Answer in full sentences. Use details from the book.', slug='chapter')
    h = must(h, '<div class="activity-title">🔤 Word Study Connection (Morphology)</div><div class="activity-sub">Your morphology response from the Word Study tab.</div>',
               '<div class="activity-title">🔤 Word Study Check</div><div class="activity-sub">The word part work on the Word Study tab</div>', f)
    h = must(h, 'Your morphology answer was saved on the Word Study tab. It will appear in your gathered work below.',
               'Finish the word part work on the Word Study tab. It shows in your work below.', f)
    h = must(h, 'I completed my Morphology response.', 'I finished the word part work on the Word Study tab.', f)
    h = re.sub(r'(I answered all 3 (?:chapter|review|synthesis) questions) with evidence(?: from the book)?\.', r'\1 with details from the book.', h)
    h = h.replace('{ title: \'🔤 WORD STUDY CONNECTION (MORPHOLOGY)\'', '{ title: \'🔤 WORD STUDY CHECK\'')
    # Writer's Workshop
    h = must(h, 'Meet Today, our example writer', 'Meet Clara, our example writer', f)
    h = re.sub(r'(<strong>Today&rsquo;s focus:</strong> )Today: ', r'\1', h)
    h = resub(h, r'\s*<p style="font-size:14px;"><em>Today: [^<]*</em></p>', '', f)
    h = resub(h, r'\s*<div class="callout callout-info" style="background:#E8F1E8;border-color:#A8C8A8;margin:0 0 10px 0;padding:10px 14px;"><span class="callout-icon">📝</span><p style="font-size:14px;"><strong>Now you try\.</strong>.*?</p></div>', '', f)
    h = head(h, 'Writer&rsquo;s Workshop', f, slug=['ww-specific', 'ww-theme', 'ww-pronoun', 'ww-share'][day - 1])
    # vocabulary: the do line says how the cards work
    h = re.sub(r'<div class="callout callout-info" style="margin-top:16px;"><span class="callout-icon">🎯</span><p><strong>Your turn!</strong> Each word below has its actual sentence from the book above it\..*?</p></div>', '', h, count=1)
    # spelling: a See the Rule button that opens an empty box
    if 'id="spellReveal"></div>' in h:
        h = resub(h, r'\s*<button class="dol-check-btn"[^>]*spellReveal[^>]*>🔍 See the Rule</button>\s*<div class="dol-answer" id="spellReveal"></div>', '', f)
    return h


def rwm(h, f):
    h = must(h, '<div class="rwm-header">📖 RWM &mdash; Read like a Reader, Read like a Writer, Mimic</div>',
               '<div class="rwm-header">📖 Read Like a Writer</div>\n' + do_line('rwm'), f)
    h = h.replace("{ title: '📖 RWM — READ LIKE A READER / WRITER / MIMIC'", "{ title: '📖 READ LIKE A WRITER'")
    h = h.replace('data-label="RWM &mdash; Read like a Reader"', 'data-label="Read like a reader"')
    h = h.replace('data-label="RWM &mdash; Read like a Writer"', 'data-label="Read like a writer"')
    h = h.replace('data-label="RWM &mdash; Mimic"', 'data-label="Write your own"')
    return h


def wgrd2(h, f, oldp, oldq, p, q):
    h = must(h, '<p>%s</p>' % oldp, '<p>%s</p>' % p, f)
    h = must(h, '<p class="socratic-q">%s</p>' % oldq, '<p class="socratic-q"><strong>%s</strong></p>' % q, f)
    return h

REMEMBER = ('<div class="key-concept"><div class="key-concept-label">&#x1F4CC; Remember</div>\n'
            '<p>A <strong>subject pronoun</strong> does the action: I, he, she, we, they. An <strong>object pronoun</strong> receives it: me, him, her, us, them. '
            'A <strong>belonging pronoun</strong> shows whose: my, his, her, their.</p></div>')
NOTICE = r'<!-- grammar-notice-first -->.*?<div class="dol-answer" id="gramNotice">.*?</div>'
VOC = '<div class="activity-sub">Words from this week\'s chapters.</div>'
SPB = '<p>Before you start: split each word into the two words that made it.</p>'
P = {
 1: ('Good readers can look back at an entire novel and trace how characters grow. Today we think about the whole book and compare Jemmy and Prince Brat side by side.',
     'Compare the beginning (Chapter 1) with the end (Chapter 20). <strong>Which boy changed more &mdash; and what proof would you give?</strong>',
     'Good readers look back at a whole book and see how the characters grew.', 'Which boy changed more, and how do you know?'),
 2: ('Good readers look for the lesson the author is teaching. Today we name the theme of The Whipping Boy — in our own words — and find two events that prove it.', None,
     'The lesson a story teaches is called its <strong>theme</strong>. Today you say it in your own words.', 'What did this story teach you?'),
 3: ("Good readers listen for the character's voice. Today we perform a scene aloud and think about how each character sounds, feels, and moves.", None,
     'Good readers hear each character&rsquo;s voice. Today you read a scene out loud.', 'How would each character sound?'),
 4: ("Good readers carry a book with them even after they close the cover. Today we celebrate what we've read, share our thinking, and reflect on what we'll take away.", None,
     'Good readers remember a book after they close it. Today you share your work and look back.', 'What will you remember most?'),
}
def wg(h, f, d):
    op, oq, p, q = P[d]
    return wgrd2(h, f, op, oq or op, p, q)

def gram_remember(h, f): return resub(h, NOTICE, REMEMBER, f)

def day1(h, f):
    h = common(h, f, 1); h = wg(h, f, 1)
    h = head(h, '🌱 Morphology: Root/base: struct means build', f, sub='A root that means <em>build</em>', slug='morph-struct1')
    h = must(h, '<div class="activity-title">🌱 Morphology: Root/base: struct means build</div>', '<div class="activity-title">🌱 Morphology: struct</div>', f)
    h = head(h, '🔤 Vocabulary', f, slug='vocabflip2')
    h = must(h, VOC, '<div class="activity-sub">Four words for talking about the whole book</div>', f)
    h = head(h, '✏️ Grammar: Pronoun Review', f, sub='A pronoun takes the place of a noun.', slug='gram-pro1')
    h = must(h, '<strong>Your turn.</strong> Nine pronouns, three jobs. Test each one in a sentence before you place it.', '<strong>Your turn.</strong> Tap a pronoun, then tap the job it does.', f)
    h = head(h, '🔠 Spelling: Compound words', f, sub='Two small words joined into one', slug='spell-comp1')
    h = must(h, '<strong>Sort the Words!</strong> Tap a word, then tap the column where it belongs.', '<strong>Sort the Words!</strong>', f)
    h = head(h, '&#128213; Looking Back: Characters', f, slug='readrev-book')
    return h

def day2(h, f):
    h = common(h, f, 2); h = wg(h, f, 2)
    h = head(h, '🪶 Poetry', f, sub='A poem can make a thing act like a person.', slug='poem-person')
    h = head(h, '🌱 Morphology: struct', f, sub='Match each word to its meaning.', slug='morph2')
    h = must(h, '<p>Before you start: find the word part, then read what is left.</p>', '<p>Find <strong>struct</strong> in each word. Then look at what is left.</p>', f)
    h = must(h, '<strong>Practice: Match the Word to Its Meaning!</strong> Tap a word, then tap what it means.', '<strong>Match the Word to Its Meaning!</strong>', f)
    h = head(h, '🔤 Vocabulary', f, slug='vocabflip2')
    h = must(h, VOC, '<div class="activity-sub">Four words for talking about theme</div>', f)
    h = head(h, '✏️ Grammar: Pronouns', f, sub='Find every pronoun.', slug='gram-pro2')
    h = gram_remember(h, f)
    h = must(h, '<strong>Your turn.</strong> Tap <strong>every</strong> pronoun in each sentence. There are three in each one, and they are all doing different jobs.',
               '<strong>Your turn.</strong> Each sentence has three pronouns, and each one does a different job.', f)
    h = head(h, '🔠 Spelling: Compound words', f, sub='Find the compound word.', slug='spell-comp2')
    h = must(h, SPB, '<p>Say each word out loud. Listen for two small words.</p>', f)
    h = must(h, '<strong>Sound Detective!</strong> Three of these are one word all the way through. One is two words joined together.', '<strong>Sound Detective!</strong>', f)
    h = head(h, '&#128213; Looking Back: Theme', f, slug='readrev-book')
    h = rwm(h, f)
    return h

def day3(h, f):
    h = common(h, f, 3); h = wg(h, f, 3)
    h = head(h, '🌱 Morphology: struct', f, sub='Build four new words.', slug='morph-struct3')
    h = must(h, '<p>Before you start: read the parts aloud, push them together, then write the word.</p>', '<p>Say each part out loud. Then say them together as one word.</p>', f)
    h = head(h, '🔤 Vocabulary', f, slug='vocabcloze')
    h = must(h, VOC, '<div class="activity-sub">Four words for reading out loud</div>', f)
    h = head(h, '✏️ Grammar: Pronouns', f, sub='Use a pronoun instead of saying the name again.', slug='gram-pro3')
    h = gram_remember(h, f)
    h = must(h, '<strong>Your turn.</strong> Swap the repeated names for pronouns so the writing stops sounding clunky.', '<strong>Your turn.</strong> Type a pronoun in each blank so the name is not said twice.', f)
    h = must(h, 'Every answer below comes from this list. Some may be used more than once.', 'Every answer comes from this list. You can use a word more than once.', f)
    h = head(h, '🔠 Spelling: Compound words', f, sub='Join two small words into one.', slug='spell-comp3')
    h = must(h, SPB, '<p>Say both small words out loud. Then say them together as one word.</p>', f)
    h = must(h, '<strong>Compound Builder!</strong> Read both small words, then tap to join them.', '<strong>Compound Builder!</strong>', f)
    h = head(h, '&#128213; Looking Back: Reader&rsquo;s Theater', f, slug='readrev-book')
    h = rwm(h, f)
    return h

def day4(h, f):
    h = common(h, f, 4); h = wg(h, f, 4)
    h = head(h, '🪶 Poetry', f, sub='Why a cheerful cricket matters', slug='poem-cricket')
    h = head(h, '🌱 Morphology: struct', f, sub='Roll a word and tell what it means.', slug='morph-dice')
    h = must(h, '<p>Before you start: say what the word part does from memory, then roll.</p>', '<p>Before you roll, say out loud what <strong>struct</strong> means.</p>', f)
    h = must(h, '<strong>Dice Roll Challenge!</strong> Roll a word, then say out loud what it means and how the word part changed it. Tap to check yourself.', '<strong>Dice Roll Challenge!</strong>', f)
    h = head(h, '🔤 Vocabulary', f, slug='vocabcloze')
    h = must(h, VOC, '<div class="activity-sub">Four words for finishing a book</div>', f)
    h = head(h, '✏️ Grammar: Pronoun Review', f, sub='Find the mistake. Not every sentence has one.', slug='gram-hunt')
    h = gram_remember(h, f)
    h = resub(h, r'<strong>Your turn\.</strong> Each sentence either has one mistake.*?</p>', '<strong>Your turn.</strong> Each sentence has one mistake or no mistake.</p>', f)
    h = head(h, '🔠 Spelling: Compound words', f, sub='Roll a word and split it.', slug='spell-comp4')
    h = must(h, SPB, '<p>Before you roll, say what a compound word is.</p>', f)
    h = must(h, '<strong>Compound Dice!</strong> Roll a word, say it out loud, decide &mdash; then tap to check yourself.', '<strong>Compound Dice!</strong>', f)
    h = head(h, '&#128213; Looking Back: Publish + Celebrate', f, slug='readrev-book')
    h = head(h, '📝 Summarize the Whole Book', f, slug='answer')
    h = head(h, '🎤 Say It Out Loud', f, slug='answer')
    h = rwm(h, f)
    return h

def flu(h, f):
    h = must(h, '<div class="activity-sub">From Chapter 20 — Synthesis: Ch. 1–20</div>', '<div class="activity-sub">From Chapter 20</div>', f)
    h = must(h, "This is the ending — gentle, warm, and full of friendship. Read the conversation between the boys quietly and honestly. The king's last line should sound like the warmest smile you've ever heard.",
               '<strong>How to read it:</strong> Read the boys&rsquo; talk quietly, like two friends. Read the king&rsquo;s last line warm, like a big smile.', f)
    h = must(h, '<strong>Read with expression.</strong> Read it a third time. Let your voice show the feeling — this is the ending — gentle, warm, and full of friendship.',
               '<strong>Read with expression.</strong> Read it a third time. Read it the way <em>How to read it</em> says.', f)
    h = must(h, 'Did my voice carry the warmth and happiness of this ending — without rushing through it?', 'Did I read the king&rsquo;s last line warm and slow?', f)
    h = head(h, '🎯 The 4 Steps', f, sub='Do these in order.', slug='flu')
    return h

FIX = {DAYS[0]: day1, DAYS[1]: day2, DAYS[2]: day3, DAYS[3]: day4, FLU: flu}
if __name__ == '__main__':
    os.makedirs(DST, exist_ok=True)
    for f, fn in FIX.items():
        h = io.open(os.path.join(SRC, f), encoding='utf-8').read()
        o = h.count('<div') - h.count('</div')
        h = fn(h, f)
        assert h.count('<div') - h.count('</div') == o, f
        io.open(os.path.join(DST, f), 'w', encoding='utf-8').write(h)
        print('ok', f)
    how = {k: DO[k] for k in sorted(USED) if k not in WK18}
    io.open(os.path.join(HERE, 'how_wk22.json'), 'w', encoding='utf-8').write(json.dumps(how, ensure_ascii=False, indent=1))
    print('reused:', sorted(k for k in USED if k in WK18))
    print('new lines:', sorted(how))
