#!/usr/bin/env python3
"""Fewer words on the page (G3 ELA pilot feedback, Nov 10 2026: "a lot of
reading for 3rd grade"). Cuts the boxes that repeat the What to do line or
stack extra think-questions; Opti reads what is left. Same cuts every week.

    python tools/g3sparkle/lean.py lesson-18-1-wb.html [...]

Idempotent; prints what it cut per file. Never touches DATA, answers,
games or anything a student types into."""
import re, sys, io

RULES = [
  # (WGRD "How to Do It" stays: a standing G3-5 piece. With read-to-me it
  #  folds behind Opti's read-along instead of being cut.)
  # Morphology: "Hunt the two word parts" box
  ('morph-hunt', r'\s*<div class="key-concept"><div class="key-concept-label">(?:&#x1F50D;|🔍) Hunt [^<]*</div>\s*<p>.*?</p>\s*</div>', ''),
  # Vocabulary: the lead-in line before the three steps
  ('vocab-lead', r'\s*<p>When you meet a word you don\'t know, use these three steps <em>in order</em>:</p>', ''),
  # Vocabulary: the empty "Let's try it together" box becomes a one-line heading
  ('vocab-model-h', r'<div class="key-concept">\s*<div class="key-concept-label">📌 Let\'s try it together: "([^"]+)"</div>\s*</div>',
   r'<div class="g3-model-h">Watch how we figure out <b>\1</b>:</div>'),
  # Grammar / spelling: the notice-first box repeats the What to do line
  ('notice-first', r'(<!-- (?:grammar|spell)-notice-first -->)\s*<div class="key-concept[^"]*"[^>]*>\s*<div class="key-concept-label"[^>]*>[^<]*</div>\s*<p>.*?</p>\s*</div>', r'\1'),
  # DOL: the hint under the model repeats the What to do line
  ('dol-hint', r'\s*<div class="dol-hint">Tap the highlighted parts to see what\'s correct about them.</div>', ''),
]

def one_question(h):
    """Think-question lists (socratic 'Try these first', 'Think it through',
    'answer these in your head') keep their first question only."""
    n = 0
    def keep_first_li(m):
        nonlocal n
        lis = re.findall(r'<li>.*?</li>', m.group(2), re.S)
        if len(lis) <= 1: return m.group(0)
        n += 1
        return m.group(1) + '\n' + lis[0] + '\n' + m.group(3)
    h = re.sub(r'(<div class="callout callout-info"[^>]*><span class="callout-icon">[^<]*</span><p><strong>(?:Think it through\.|Say each word below\. Then answer these in your head:)</strong></p>\s*<(?:ol|ul)[^>]*>)(.*?)(</(?:ol|ul)></div>)',
               keep_first_li, h, flags=re.S)
    h = re.sub(r'answer these in your head:', 'answer this in your head:', h)
    def keep_first_q(m):
        nonlocal n
        qs = re.findall(r'<p class="socratic-q">.*?</p>', m.group(2), re.S)
        if len(qs) <= 1: return m.group(0)
        n += 1
        return m.group(1).replace('Try these first:', 'Try this first:') + '\n' + qs[0] + '\n' + m.group(3)
    h = re.sub(r'(<div class="socratic-box"><div class="socratic-label">[^<]*Try these first:</div>)(.*?)(</div>)', keep_first_q, h, flags=re.S)
    return h, n

# What to do lines that named the cut questions
TODO = [('Think about the three questions.', 'Think about the question.')]

for f in sys.argv[1:]:
    h = io.open(f, encoding='utf-8').read(); log = []
    for name, pat, rep in RULES:
        h, c = re.subn(pat, rep, h, flags=re.S)
        if c: log.append('%s x%d' % (name, c))
    h, c = one_question(h)
    if c: log.append('one-question x%d' % c)
    for a, b in TODO:
        c = h.count(a)
        if c: h = h.replace(a, b); log.append('todo x%d' % c)
    io.open(f, 'w', encoding='utf-8').write(h)
    print(f, ', '.join(log) or 'nothing to cut')
