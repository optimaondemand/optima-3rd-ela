"""Week 32 workload cuts, approved by Bethany Nov 16 2026 ("err on the fun side. Less workload, more payoff for a hard
year's work. still educational, but more fun interactives and reflection"). Four cuts she chose:
  1. 2 pillars, not 4 (plan 2, draft 2 body paragraphs; Clara's model shows 2).
  2. No double writing: Writer's Workshop no longer repeats the Reading-tab paragraphs (Days 1-2 box goes; Day 3 box is
     only the share-out-loud notes; Day 4 box is only the title).
  3. Grammar "Show What You Know" writing boxes go on Days 1-3 (the tap passage checks the skill); Day 3 gets a
     "Check your sentence" reveal instead.
  4. Sharing is a 1-minute video OR reading it to someone at home, with ONE thing to show.
Runs on the repo files after acc_wk32.py:  python tools/g3sparkle/light_wk32.py [--apply]"""
import io, re, sys

def sub1(s, a, b, f, n=1):
    c = s.count(a)
    assert c == n, (f, c, a[:100])
    return s.replace(a, b)

SWYK_RE = re.compile(r'\n?<div class="swyk"><div class="swyk-label">🪶 Show What You Know</div>\n<div class="swyk-prompt">[^<]*</div>\n'
                     r'<div class="journal-label">📓 Your answer <span class="saved-dot" id="dot-grammar"></span></div>\n'
                     r'<textarea class="journal-box" id="journal-grammar"[^>]*></textarea></div>')
WW_TA = re.compile(r'\n\s*<textarea class="journal-box" id="journal-writing".*?</textarea>', re.S)
NOWTRY = re.compile(r'(<p style="font-size:14px;"><strong>Now you try\.</strong>).*?(</p></div>)', re.S)
def nowtry(s, f, text):
    assert len(NOWTRY.findall(s)) == 1, (f, 'nowtry')
    return NOWTRY.sub(lambda m: m.group(1) + ' ' + text + m.group(2), s)
TA = '<textarea class="journal-box" id="journal-writing" data-label="%s" placeholder="%s" oninput="autoSave(this,\'dot-writing\');gatherAnswers();"></textarea>'
Q3_RE = re.compile(r'\n        <div class="activity bl-cyan" style="margin-bottom:14px;">\n          <div class="activity-head"><div class="activity-num"[^>]*>Q3</div><div><div class="activity-title">Q3 — Two More Body Paragraphs</div></div></div>.*?</textarea>\n          </div>\n        </div>', re.S)
CHECK3 = ('\n<button class="dol-check-btn" onclick="document.getElementById(\'gram3Fix\').classList.toggle(\'show\')">&#x1F50D; Check your sentence</button>'
          '\n<div class="dol-answer" id="gram3Fix"><p>Despereaux&rsquo;s sister showed him the library, and he read a book about a knight.</p>'
          '<p style="font-size:13px;color:#7A88A8;">Six changes: <strong>Despereaux&rsquo;s</strong> (capital + apostrophe), a comma before <em>and</em>, <strong>read</strong> (not readed), and a capital at the start.</p></div>')
DAY4_READ_OLD = re.compile(r'(<p style="white-space:pre-line;">)Today is your final day of 3rd grade ELA\..*?saying\.(</p></div>)', re.S)
DAY4_READ_NEW = ('Today is your last day of 3rd grade ELA!\n\nShare your response out loud. Pick one: record a 1-minute video for Canvas, or read it to someone at home.\n\n'
                 'When you share:\n1. Name your character and the book.\n2. Say your most important pillar and why.\n3. Share your best detail from the book.\n'
                 '4. Show your picture or object.\n5. End with one sentence about what this character taught you.\n\nSpeak slowly and clearly. Look up from your paper when you can.')
R = {
 1: [('Look at the 7 Pillars of Virtue. List at least 4 pillars that your character shows during the novel. For each, write one brief example.',
      'Look at the 7 Pillars of Virtue. Choose 2 pillars your character shows. For each one, write one example from the book.'),
     ('turn-in-item-text">I chose my character and listed at least 4 pillars with examples.', 'turn-in-item-text">I chose my character and 2 pillars, with an example for each.'),
     ('a written response and a short oral presentation about one character', 'a short written response about one character, which you will share out loud,'),
     ("Pillars I will cover: Responsibility (he says &ldquo;I&rsquo;m sorry&rdquo; to each of his brother and sisters), Courage (in the battle he smashes the Witch&rsquo;s wand with his sword), "
      "Service (Peter says they would have been beaten without him), Perseverance (Peter says &ldquo;nothing would stop him&rdquo;).",
      "Pillars I will cover: Responsibility (he says &ldquo;I&rsquo;m sorry&rdquo; to each of his brother and sisters) and Courage (in the battle he smashes the Witch&rsquo;s wand with his sword)."),
     ('and she plans to use examples from across the whole novel, not just one scene.', 'and one real example from the book for each pillar.')],
 2: [('Write one paragraph for each of the 4 pillars you identified.', 'Write one paragraph for each of your 2 pillars.'),
     ('turn-in-item-text">I wrote at least four body paragraphs — one per pillar.', 'turn-in-item-text">I wrote two body paragraphs — one per pillar.')],
 3: [('Today you revise your culmination response using the checklist below and prepare for your oral presentation.',
      'Today you revise your culmination response using the checklist below and get ready to share it out loud.'),
     ('turn-in-item-text">I prepared my oral presentation notes and chose two multimedia pieces.', 'turn-in-item-text">I wrote my sharing notes and chose one thing to show.'),
     ('<div class="key-concept-label" style="color:#0E5A7A;">🖼️ Add Two Multimedia Pieces</div><p style="font-size:14px;">A presentation is stronger when your listener can see or hear something too. Pick <strong>two</strong> of these to use while you present:</p>',
      '<div class="key-concept-label" style="color:#0E5A7A;">🖼️ Add One Thing to Show</div><p style="font-size:14px;">Sharing is more fun when your listener can see something too. Pick <strong>one</strong> of these to show while you share:</p>'),
     ('<p style="font-size:14px;">Add a line to your notes for each one: what it is, and the moment you will show or play it.</p>',
      '<p style="font-size:14px;">Add a line to your notes: what it is, and when you will show it.</p>'),
     ('Clara revises her culmination response and prepares her oral presentation notes.', 'Clara revises her closing.'),
     ('he has shown responsibility, courage, service, and perseverance', 'he has shown responsibility and courage'),
     ('names several pillars, and ends', 'names her pillars, and ends')],
 4: [('Make sure it has: an opening with a claim, at least four body paragraphs (one per pillar), and a closing.',
      'Make sure it has: an opening with your claim, two body paragraphs (one per pillar), and a closing.'),
     ('turn-in-item-text">I delivered my oral presentation (or recorded it for Canvas).', 'turn-in-item-text">I shared my response out loud (a 1-minute video, or reading it at home).'),
     ('Clara submits her final published culmination response and delivers her oral presentation.', 'Clara gives her response a title and shares it.'),
     ("She reads her response aloud once, then submits it and delivers her presentation.", "She reads her response out loud to her family, then submits it.")],
}
WW = {1: ('Your plan is your answers to Q1&ndash;Q3 on the Reading tab. There is nothing more to write here.', None),
      2: ('Your draft is your answers to Q1 and Q2 on the Reading tab. There is nothing more to write here.', None),
      3: ('Your closing is Q3 on the Reading tab. Here, write 3 short notes for sharing out loud, and name the one thing you will show.',
          TA % ('Writing Workshop: notes for sharing', 'My notes for sharing:\n• My character is...\n• My most important pillar is...\n• My best detail is...\n\nThe one thing I will show:\n___ (I will show it when ___)')),
      4: ('Give your response a title. Then share it out loud: record a 1-minute video for Canvas, or read it to someone at home.',
          TA % ('Writing Workshop: my title', 'Title: ___'))}

def main(apply):
    for d in (1, 2, 3, 4):
        f = 'lesson-32-%d-ext.html' % d
        s = io.open(f, encoding='utf-8', newline='').read(); o = s
        for a, b in R[d]: s = sub1(s, a, b, f)
        if d < 4:
            assert len(SWYK_RE.findall(s)) == 1, (f, 'swyk')
            s = SWYK_RE.sub(lambda m: CHECK3 if d == 3 else '', s)
        if d == 3:
            s = sub1(s, '<strong>Now you.</strong> Fix everything, then check it twice &mdash; once for capitals, once for punctuation.',
                     '<strong>Now you.</strong> Say the sentence the right way, out loud. Then tap Check your sentence.', f)
        if d == 2:
            assert len(Q3_RE.findall(s)) == 1, (f, 'q3')
            s = Q3_RE.sub('', s)
        if d == 4:
            assert len(DAY4_READ_OLD.findall(s)) == 1, (f, 'read4')
            s = DAY4_READ_OLD.sub(lambda m: m.group(1) + DAY4_READ_NEW + m.group(2), s)
        txt, ta = WW[d]
        s = nowtry(s, f, txt)
        assert len(WW_TA.findall(s)) == 1, (f, 'ww ta')
        s = WW_TA.sub(lambda m: ('\n    ' + ta) if ta else '', s)
        assert s.count('<div') - s.count('</div') == o.count('<div') - o.count('</div'), (f, 'div balance')
        print(f, 'ok', len(o), '->', len(s))
        if apply: io.open(f, 'w', encoding='utf-8', newline='').write(s)

if __name__ == '__main__':
    main('--apply' in sys.argv)
