#!/usr/bin/env python3
"""Week 21 plain-language pass (The Whipping Boy, Ch. 16-20).

Same rules as plain_wk18.py (Bethany, Nov 8 2026): direct instruction,
nothing left to interpretation, valuable words only, each fact once, a
sort item has exactly one right answer. Every activity gets one
"What to do:" line that Opti reads (data-say = the clip slug; a slug that
already exists in how_wk18.json reuses that clip, so its words must match
exactly).

Reads pristine-orig/ (the week 21 files after acc_wk21.py), writes
pristine/ (the build input). Every replacement is asserted. Re-runnable."""
import io, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC, DST = os.path.expanduser('~/g3w21/pristine-orig'), os.path.expanduser('~/g3w21/pristine')
DAYS = ['lesson-21-1-wb.html', 'lesson-21-2-wb.html', 'lesson-21-3-wb.html', 'lesson-21-4-wb.html']
FLU = 'lesson-21-fluency.html'

# ── Opti's "What to do" lines. Week 18 slugs keep their exact words. ──
WK18 = json.load(io.open(os.path.join(HERE, 'how_wk18.json'), encoding='utf-8'))
WK19 = json.load(io.open(os.path.join(HERE, 'how_wk19.json'), encoding='utf-8'))
for k, v in WK19.items(): WK18.setdefault(k, v)
WK20 = json.load(io.open(os.path.join(HERE, 'how_wk20.json'), encoding='utf-8'))
for k, v in WK20.items(): WK18.setdefault(k, v)
NEW21 = {
 'morph-pre1':   'Read the five words and their parts. Think about the question. Then tap See what was hiding. Last, type each whole word and tap Check My Answers.',
 'gram-phrase1': 'Read the sentence in the box and tap Now check your thinking. Then tap each phrase, and tap the column it belongs in: where, when, or how. Last, answer the question in the box.',
 'gram-phrase3': 'Read the Remember box. Then type the noun each phrase ends on, and tap Check My Answers. Last, answer the question in the box.',
 'spell-homo1':  'Read the three sentences out loud. Think about the question, then tap See the Rule. Last, tap each phrase, and tap the spelling it needs: to, two, or too.',
 'spell-homob':  'Read the two sentences out loud and tap Now check your thinking. Then tap each word, and tap its column. Next, tap the right spelling in each sentence. Last, answer the question in the box.',
 'spell-homo2':  'Read the rule. Then in each sentence, tap the spelling that fits.',
 'spell-homo4':  'Tap Roll the dice. Read the words, and say which spelling fits and why. Then tap Check my answer. Roll all six.',
 'poem-person':  'Read the poem out loud. Then find two things in the poem that act like people.',
 'poem-crawl':   'Read the poem out loud again. Then answer the question about the word crawls.',
 'ww-chart':     'Read Clara’s notes. Then fill in the chart for Jemmy and for Prince Brat: how he was at the beginning, how he is at the end, and what changed him.',
 'ww-open':      'Read Clara’s two openings. Then write the opening sentence of your comparison. Name both boys.',
 'ww-body':      'Read Clara’s notes and her body sentences. Then write one way the boys changed the same, and one way they changed differently.',
 'ww-publish':   'Read Clara’s conclusion. Then write a conclusion for your comparison, and one sentence that says what the story teaches.',
 'sewer':        'Read the question. Tap the tunnel with the right answer. A right answer moves Jemmy and the prince closer to daylight.',
}
LI21 = [('<li><strong>Notice what the characters have learned:</strong> By the last chapters, someone usually understands something new.</li>',
         '<li><strong>What has someone learned?</strong> By the last chapters, a character understands something new.</li>'),
        ('<li><strong>Look for the idea the book keeps returning to:</strong> Themes repeat &mdash; that is how you spot them.</li>',
         '<li><strong>What idea keeps coming back?</strong> A big idea that shows up again and again is the theme.</li>'),
        ('<li><strong>Say the lesson in one sentence:</strong> Write it so it would make sense to someone who never read the book.</li>',
         '<li><strong>Can you say it in one sentence?</strong> Say the lesson so a friend who never read the book would get it.</li>')]

NEW = NEW21
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

LI = LI21

def common(h, f, day):
    for a, b in LI: h = must(h, a, b, f)
    h = must(h, '<div class="thinking-stop">💭 Think about this as you read today — you don\'t need to write anything here.</div>', '', f)
    h = head(h, '📚 What Good Readers Do', f, sub='What to watch for while you read', slug='readers')
    h = head(h, '✏️ Daily Oral Language', f, sub='Fix a sentence from the story.', slug='dol')
    h = resub(h, r'\s*<p>The first sentence is <strong>correct</strong>\. Tap the parts you notice.*?</p>', '', f)
    # transitions
    h = must(h, 'Now that your mind is warmed up, let&rsquo;s sharpen your words and skills.', 'Next: word study.', f)
    h = must(h, 'Your words and skills are sharp. Time to open the book.', 'Next: reading.', f)
    h = must(h, 'You&rsquo;ve read and noticed. Now answer the questions and submit your work.', 'Next: answer the questions and turn in your work.', f)
    # reading tab
    h = must(h, '<div class="thinking-stop">💭 Think: How will your character help someone in your story?</div>', '', f)
    h = resub(h, r'<div class="callout callout-info" style="margin-bottom:14px;"><span class="callout-icon">&#x23F8;&#xFE0F;</span><p><strong>Read these first\.</strong>.*?</p></div>', '', f)
    h = h.replace('<div class="thinking-stop">💭 Pause and think about this — no need to write.</div>', '')
    h = resub(h, r'\s*<div class="key-concept" style="background:#F0E8FF;border-color:#D8CCF0;margin-bottom:14px;">\s*<div class="key-concept-label" style="color:#6B4FB0;">💎 As you read, notice:</div>\s*<p>.*?</p>\s*</div>', '', f)
    h = resub(h, r'\s*<div class="callout callout-info" style="margin-bottom:14px;">\s*<span class="callout-icon">📕</span>\s*<p><strong>Open your novel to .*?</p>\s*</div>', '', f)
    # assignment
    h = head(h, '📖 Chapter Thinking', f, sub='Answer in full sentences. Use details from the book.', slug='chapter')
    h = must(h, '<div class="activity-title">🔤 Word Study Connection (Morphology)</div><div class="activity-sub">Your morphology response from the Word Study tab.</div>',
               '<div class="activity-title">🔤 Word Study Check</div><div class="activity-sub">The word part work on the Word Study tab</div>', f)
    h = must(h, 'Your morphology answer was saved on the Word Study tab. It will appear in your gathered work below.',
               'Finish the word part work on the Word Study tab. It shows in your work below.', f)
    h = must(h, 'I completed my Morphology response.', 'I finished the word part work on the Word Study tab.', f)
    h = re.sub(r'(I answered all 3 (?:chapter|review) questions) with evidence(?: from the book)?\.', r'\1 with details from the book.', h)
    h = h.replace('{ title: \'🔤 WORD STUDY CONNECTION (MORPHOLOGY)\'', '{ title: \'🔤 WORD STUDY CHECK\'')
    # Writer's Workshop
    h = must(h, 'Meet Today, our example writer', 'Meet Clara, our example writer', f)
    h = re.sub(r'(<strong>Today&rsquo;s focus:</strong> )Today: ', r'\1', h)
    h = resub(h, r'\s*<p style="font-size:14px;"><em>Today: [^<]*</em></p>', '', f)
    h = resub(h, r'\s*<div class="callout callout-info" style="background:#E8F1E8;border-color:#A8C8A8;margin:0 0 10px 0;padding:10px 14px;"><span class="callout-icon">📝</span><p style="font-size:14px;"><strong>Now you try\.</strong>.*?</p></div>', '', f)
    h = head(h, 'Writer&rsquo;s Workshop', f, slug=['ww-chart', 'ww-open', 'ww-body', 'ww-publish'][day - 1])
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

def wgrd(h, f, old, p, q):
    h = must(h, '<p>%s</p>' % old, '<p>%s</p>' % p, f)
    h = must(h, '<p class="socratic-q">%s</p>' % old, '<p class="socratic-q"><strong>%s</strong></p>' % q, f)
    return h

def spell_rule_boxes(h, f):
    h = must(h, '<p class="socratic-q">Look at the last three letters of each word. What two of them are always the same?</p>',
               '<p class="socratic-q">Look at the last three letters of each word. Which two letters are always the same?</p>', f)
    h = must(h, '<p class="socratic-q">Count back three letters from the end of each word. Where does the dot land?</p>',
               '<p class="socratic-q">Count back three letters from the end of each word. Is that where the dot is?</p>', f)
    return h


BEFORE = '<p>Before you start: split each word into beats, then read the pieces.</p>'
def spell_common(h, f):
    h = must(h, BEFORE, '<p>Say each word out loud. Clap the beats.</p>', f)
    return h

REMEMBER = ('<div class="key-concept"><div class="key-concept-label">&#x1F4CC; Remember</div>\n'
            '<p>A prepositional phrase starts with a preposition and ends on a noun: <strong>through the fog</strong>.</p></div>')
NOTICE = r'<!-- grammar-notice-first -->.*?<div class="dol-answer" id="gramNotice">.*?</div>'
MORPH_TITLE = '🌱 Morphology: re-, un-, pre-, dis-, mis-'

def day1(h, f):
    h = common(h, f, 1)
    h = must(h, '<p>Good readers begin to see the theme in the final chapters. As you read Chapters 16 and 17, ask: what is this story really teaching? What is being learned?</p>',
               '<p>In the last chapters of a book, good readers start to see its lesson. That lesson is called the <strong>theme</strong>.</p>', f)
    h = must(h, '<p class="socratic-q">As you read Chapters 16 and 17, ask: <strong>what has each boy learned that he did not understand at the start of the story?</strong></p>',
               '<p class="socratic-q"><strong>What has each boy learned that he did not know at the start?</strong></p>', f)
    h = head(h, MORPH_TITLE, f, sub='Five word parts that go at the front of a word', slug='morph-pre1')
    h = must(h, '<p class="socratic-q">Which one means <em>again</em>? Which one means <em>not</em>?</p>',
               '<p class="socratic-q">Which one means <em>again</em>? Which two mean <em>not</em>?</p>', f)
    h = head(h, '🔤 Vocabulary', f, sub='Four words from Chapters 16&ndash;17', slug='vocabflip2')
    h = head(h, '✏️ Grammar: Prepositional Phrases', f, sub='A prepositional phrase can tell where, when, or how.', slug='gram-phrase1')
    h = must(h, '<strong>Your turn.</strong> Nine whole phrases this time, not single words. Sort each one by the question it answers.',
               '<strong>Your turn.</strong> Tap a phrase, then tap the question it answers.', f)
    h = head(h, '🔠 Spelling: Homophones', f, sub='Words that sound the same: to, two, too', slug='spell-homo1')
    h = resub(h, r'(<div class="socratic-label">&#x1F50D; What do you notice\?</div>)\s*<p class="socratic-q">Say the three bold words.*?</p>\s*<p class="socratic-q">.*?</p>\s*<p class="socratic-q">.*?</p>',
              r'\1\n        <p class="socratic-q">Say the three bold words. They sound the same. <strong>So how does a reader know which one you mean?</strong></p>', f)
    h = must(h, '<strong>Practice: Sort the words.</strong> Read each phrase, decide which spelling it needs, then tap its column.',
               '<strong>Practice:</strong> Tap a phrase, then tap the spelling it needs.', f)
    h = head(h, '📕 Read: Ch. 16–17', f, slug='read')
    return h

def day2(h, f):
    # Vocabulary was one </div> short, so the Spelling Bonus rendered inside it (skill 8d #1)
    h = must(h, '  </div>\n\n  <!-- BONUS WORDPLAY -->', '  </div>\n  </div>\n\n  <!-- BONUS WORDPLAY -->', f)
    h = must(h, '</div></div>\n  </div>\n\n\n  <!-- SPELLING -->', '</div></div>\n\n\n  <!-- SPELLING -->', f)
    h = common(h, f, 2)
    h = wgrd(h, f, 'Good readers look for small moments that carry big meaning. A small word like &lsquo;friend&rsquo; can mean more than a whole speech.',
             'Good readers notice small moments that mean a lot. Today, watch for the word <em>friend</em>.',
             'What does the word friend show about the boys now?')
    h = h.replace('<p>Good readers look for small moments that carry big meaning. A small word like &lsquo;friend&rsquo; can mean more than a whole speech.</p>', '')
    h = head(h, '🪶 Poetry', f, sub='A poem can make a thing act like a person.', slug='poem-person')
    h = head(h, MORPH_TITLE, f, sub='Match each word to its meaning.', slug='morph2')
    h = must(h, '<p>Before you start: find the word part, then read what is left.</p>', '<p>Find the word part at the front of each word. Then look at what is left.</p>', f)
    h = must(h, '<strong>Practice: Match the Word to Its Meaning!</strong> Tap a word, then tap what it means.', '<strong>Match the Word to Its Meaning!</strong>', f)
    h = head(h, '🔤 Vocabulary', f, sub='Four words from Chapters 18&ndash;19', slug='vocabflip2')
    h = head(h, '🔠 Spelling Bonus: Homophones', f, sub='their, there, they&rsquo;re and more', slug='spell-homob')
    h = must(h, 'No grammar today &mdash; you get a second word-study section instead. This happens once all year, and today is the day.',
               'No grammar today. You get two spelling activities instead.', f)
    h = must(h, '<strong>Sort them.</strong> Every word below belongs in one of the two columns. Tap a word, then tap its column &mdash; and look at the apostrophes while you do it.',
               '<strong>Sort them.</strong> Tap a word, then tap its column. Look at the apostrophes.', f)
    h = must(h, '<strong>Now pick the right one.</strong> Each sentence offers two spellings. Tap the one that belongs there.', '<strong>Now pick the right one.</strong> Tap the spelling that fits.', f)
    h = head(h, '🔠 Spelling: Homophones', f, sub='Pick their, there, or they&rsquo;re.', slug='spell-homo2')
    h = must(h, '<p>Before you start: read the whole sentence first. The meaning, not the sound, picks the spelling.</p>', '<p>Read the whole sentence first. The meaning picks the spelling.</p>', f)
    h = resub(h, r'\s*<p>Yesterday you sorted <em>to</em>.*?</p>', '', f)
    h = must(h, '<strong>Tap the right one.</strong> Read the sentence through before you choose.', '<strong>Tap the right one.</strong>', f)
    h = head(h, '📕 Read: Ch. 18–19', f, slug='read')
    h = rwm(h, f)
    return h

def gram_remember(h, f):
    return resub(h, NOTICE, REMEMBER, f)

def day3(h, f):
    h = common(h, f, 3)
    h = wgrd(h, f, "Good readers know that a story's theme is the BIG IDEA it wants you to take away. As you finish Chapter 20, ask: what is the most important thing this story is saying about people, change, and friendship?",
             'The theme is the big lesson a story wants you to take away. Today you read the last chapter.',
             'What is the story saying about friendship and change?')
    h = h.replace("<p>Good readers know that a story's theme is the BIG IDEA it wants you to take away. As you finish Chapter 20, ask: what is the most important thing this story is saying about people, change, and friendship?</p>", '')
    h = head(h, MORPH_TITLE, f, sub='Build five new words.', slug='morph3')
    h = must(h, '<p>Before you start: read the parts aloud, push them together, then write the word.</p>', '<p>Say each part out loud. Then say them together as one word.</p>', f)
    h = head(h, '🔤 Vocabulary', f, sub='Four words from Chapters 18&ndash;20', slug='vocabcloze')
    h = head(h, '✏️ Grammar: Prepositional Phrases', f, sub='Find the noun at the end of each phrase.', slug='gram-phrase3')
    h = gram_remember(h, f)
    h = must(h, '<strong>Your turn.</strong> Every prepositional phrase ends on a noun. Type the noun each phrase lands on.', '<strong>Your turn.</strong> Type the noun each phrase ends on.', f)
    h = must(h, 'Every answer below comes from this list. Some may be used more than once.', 'Every answer comes from this list. You can use a word more than once.', f)
    h = head(h, '🔠 Spelling: Homophones', f, sub='to, two, too and their, there, they&rsquo;re mixed', slug='spell-homo2')
    h = must(h, '<p>Before you start: say what the word <em>means</em> in the sentence, then spell it.</p>', '<p>Say what the word means in the sentence. Then pick the spelling.</p>', f)
    h = resub(h, r'\s*<p>Both sets together now\..*?</p>', '', f)
    h = must(h, '<strong>Tap the right one.</strong> Six sentences, both sets mixed.', '<strong>Tap the right one.</strong>', f)
    h = head(h, '📕 Read: Ch. 20', f, slug='read')
    h = rwm(h, f)
    return h

def day4(h, f):
    h = common(h, f, 4)
    h = wgrd(h, f, 'Good readers think about the whole book. Now that you have read all 20 chapters, ask: what was this story really about? What did we learn from watching these two characters together?',
             'Good readers think about the whole book once they finish it.',
             'What was this story really about?')
    h = h.replace('<p>Good readers think about the whole book. Now that you have read all 20 chapters, ask: what was this story really about? What did we learn from watching these two characters together?</p>', '')
    h = head(h, '🪶 Poetry', f, sub='One word can do a lot of work.', slug='poem-crawl')
    h = head(h, MORPH_TITLE, f, sub='Roll a word and tell what it means.', slug='morph-dice')
    h = must(h, '<p>Before you start: say what the word part does from memory, then roll.</p>', '<p>Before you roll, say out loud what each word part means.</p>', f)
    h = must(h, '<strong>Dice Roll Challenge!</strong> Roll a word, then say out loud what it means and how the word part changed it. Tap to check yourself.', '<strong>Dice Roll Challenge!</strong>', f)
    h = head(h, '🔤 Vocabulary', f, sub='Four words from this week', slug='vocabcloze')
    h = head(h, '✏️ Grammar: Prepositional Phrases', f, sub='Find the mistake. Not every sentence has one.', slug='gram-hunt')
    h = gram_remember(h, f)
    h = resub(h, r'<strong>Your turn\.</strong> Each sentence either has one mistake.*?</p>',
              '<strong>Your turn.</strong> Each sentence has one mistake or no mistake.</p>', f)
    h = head(h, '🔠 Spelling: Homophones', f, sub='Roll a phrase and pick the spelling.', slug='spell-homo4')
    h = resub(h, r'\s*<p>Last day\. Roll a word, then .*?</p>', '', f)
    h = must(h, '<strong>Homophone Dice!</strong> Roll a phrase, choose the spelling, say why &mdash; then tap to check yourself.', '<strong>Homophone Dice!</strong>', f)
    h = must(h, '<div class="activity-title">📕 Read: Ch. 16–20 Review</div><div class="activity-sub">Review, Publish, and Discuss Character Change</div>',
               '<div class="activity-title">📕 Look Back: Ch. 16–20</div><div class="activity-sub">No new chapters today</div>', f)
    h = head(h, '📕 Look Back: Ch. 16–20', f, slug='readrev-week')
    h = must(h, 'Open your novel to Ch. 16–20 Review.</div>', 'Look back at Chapters 16–20.</div>', f)
    h = must(h, '<div class="info-detail">Review, Publish, and Discuss Character Change</div>', '<div class="info-detail">No new chapters today</div>', f)
    h = rwm(h, f)
    return h

def flu(h, f):
    h = must(h, '<div class="activity-sub">From Chapter 17 — Ch. 16–20</div>', '<div class="activity-sub">From Chapter 17</div>', f)
    h = must(h, "Read the bear's approach with low, slow dread. Then let the outlaws' escape be wild and fast and funny. Betsy's whistle at the end — make it sound like calm control after total chaos.",
               '<strong>How to read it:</strong> Read the bear coming down slow and low. Read the outlaws running away fast and funny. Read Betsy&rsquo;s whistle calm.', f)
    h = must(h, "<strong>Read with expression.</strong> Read it a third time. Let your voice show the feeling — read the bear's approach with low, slow dread.",
               '<strong>Read with expression.</strong> Read it a third time. Read it the way <em>How to read it</em> says.', f)
    h = must(h, "Did I slow down for the bear's approach and speed up for the outlaws running away?", 'Did I read the bear slow and the outlaws fast?', f)
    h = head(h, '🎯 The 4 Steps', f, sub='Do these in order.', slug='flu')
    return h

FIX = {DAYS[0]: day1, DAYS[1]: day2, DAYS[2]: day3, DAYS[3]: day4, FLU: flu}
if __name__ == '__main__':
    os.makedirs(DST, exist_ok=True)
    for f, fn in FIX.items():
        h = io.open(os.path.join(SRC, f), encoding='utf-8').read()
        h = fn(h, f)
        io.open(os.path.join(DST, f), 'w', encoding='utf-8').write(h)
        print('ok', f)
    how = {k: DO[k] for k in sorted(USED) if k not in WK18}
    io.open(os.path.join(HERE, 'how_wk21.json'), 'w', encoding='utf-8').write(json.dumps(how, ensure_ascii=False, indent=1))
    print('reused:', sorted(k for k in USED if k in WK18))
    print('new clips:', sorted(how))
