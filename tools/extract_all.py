# -*- coding: utf-8 -*-
"""Unified extractor for every OAO G3 ELA lesson family.

Scoping is by ACTIVITY TITLE, not by HTML comment. The skill's extractor scopes
on <!-- MORPHOLOGY --> style comments, but only the Despereaux files have them:
Weeks 1-7 and 18-32 have no per-section comments at all, so comment scoping
silently returns nothing and the morphology and vocabulary fill-ins get mixed.
Every family does put each strand in its own <div class="activity ..."> with a
titled head, so that is what we split on.
"""
import re, io, os, json, glob, html, sys

def cl(x):
    x = re.sub(r'<[^>]+>', ' ', x or '')
    return re.sub(r'\s+', ' ', html.unescape(x)).strip()

TITLE_KEYS = [
    ('📚', 'What Good Readers', 'wgrd'),
    ('✏️', 'Daily Oral Language', 'dol'),
    ('🪶', 'Copywork', 'copywork'),
    ('🪶', 'Poetry', 'poetry'),
    ('🌱', 'Morphology', 'morph'),
    ('🔤', 'Vocabulary', 'vocab'),
    ('✏️', 'Grammar', 'gram'),
    ('🔠', 'Spelling', 'spell'),
    ('🪶', 'Writing Connection', 'writeconn'),
    # The reading slot. Order matters and the needles are deliberately specific:
    # a bare 'Read' also matches 'Reading Comprehension' and "Reader's Theater",
    # which is how W5 D2-4 once reported ch_range='Reading Comprehension'.
    # Writing/synthesis days carry no reading assignment and are titled for the
    # real work, so they are matched explicitly here.
    # The reading slot. Writing/synthesis days carry no reading assignment and are
    # titled for the real work, so they are matched by their ✍️ marker rather than
    # by wording - naming specific verbs here broke twice as titles were reworded.
    ('📕', 'Looking Back', 'reading'),
    ('✍️', '✍️', 'reading'),
    ('&#9997;', '&#9997;', 'reading'),
    ('📕', 'Read:', 'reading'),
]

def activities(s):
    """Split the document into activity blocks keyed by strand."""
    idx = [m.start() for m in re.finditer(r'<div class="activity[ "]', s)]
    idx.append(len(s))
    out = {}
    for a, b in zip(idx, idx[1:]):
        blk = s[a:b]
        m = re.search(r'activity-title"[^>]*>(.*?)</div>', blk, re.S)
        if not m: continue
        title = cl(m.group(1))
        raw = m.group(1)
        for emoji, needle, key in TITLE_KEYS:
            hay = (raw if needle.startswith(('✍', '&#')) else title).lower()
            if needle.lower() in hay and key not in out:
                out[key] = {'title': title, 'html': blk,
                            'sub': cl((re.search(r'activity-sub"[^>]*>(.*?)</div>', blk, re.S) or [None,''])[1]
                                      if re.search(r'activity-sub"[^>]*>(.*?)</div>', blk, re.S) else '')}
                break
    return out

def extract(path, week, day):
    s = io.open(path, encoding='utf-8', errors='replace').read()
    A = activities(s)
    d = {'week': week, 'day': day, 'file': os.path.basename(path)}
    g = lambda k: A.get(k, {}).get('html', '')
    t = lambda k: A.get(k, {}).get('title', '')

    # ── reading / chapter range ───────────────────────────────────────────
    # strip any leading section emoji and the 'Read:' / 'Looking Back:' label
    d['ch_range'] = re.sub(r'^(?:📕|📰|✍️|✍)\s*(?:Read:|Looking Back:)?\s*', '', t('reading')).strip()
    # Pause & Think prompts: key on the ⏸️ label, not on position or activity.
    # A document-order scan of socratic-q picks up morphology/spelling boxes that
    # sit earlier in the page (that is how W22 decks showed the VCCV spelling
    # prompt under "PAUSE & THINK"), and activity scoping fails for W23-24, whose
    # reading block is titled with the article name ("Life in a Medieval Castle").
    # Every unit marks its real pause boxes with ⏸️, so match that.
    d['pause_qs'] = [cl(x) for x in re.findall(
        r'socratic-label">\s*⏸️.*?</div>\s*<p class="socratic-q"[^>]*>(.*?)</p>', s, re.S)][:3]
    if not d['pause_qs']:
        d['pause_qs'] = [cl(x) for x in re.findall(
            r'class="socratic-q"[^>]*>(.*?)</p>', g('reading'), re.S)][:3]
    bq = re.search(r'class="big-question"[^>]*>(.*?)</', s, re.S) or re.search(r'class="socratic-q"[^>]*>(.*?)</p>', s, re.S)
    d['big_question'] = cl(bq.group(1)) if bq else ''

    # ── What Good Readers Do ─────────────────────────────────────────────
    m = re.search(r'<div class="activity-body">\s*<p>(.*?)</p>', g('wgrd'), re.S)
    d['wgrd'] = cl(m.group(1)) if m else ''

    # ── DOL: two markup eras ─────────────────────────────────────────────
    dol = g('dol') or s
    d['dol_model'] = d['dol_fix'] = d['dol_fix2'] = ''
    d['dol_ans'] = d['dol_ans2'] = d['dol_errors'] = ''
    d['model_hints'] = []
    wraps = re.findall(r'<div class="dol-sentence-wrap"([^>]*)>(.*?)</div>', dol, re.S)
    if wraps:                                     # era B (W18-32)
        for attrs, body in wraps:
            txt = cl(body)
            if 'dolModel' in attrs:
                d['dol_model'] = txt
                d['model_hints'] = [{'word': cl(w), 'hint': cl(h)} for h, w in
                    re.findall(r"dolHighlight\(this,'([^']*)'\)[^>]*>(.*?)</span>", body, re.S)]
            elif not d['dol_fix']:
                d['dol_fix'] = txt
    else:                                          # era A (W1-16)
        fixes = [cl(x) for x in re.findall(r'class="task-sentence"[^>]*>(.*?)</div>', dol, re.S)]
        fixes = [f for f in fixes if f]
        if fixes:
            d['dol_fix'] = fixes[0]
            d['dol_fix2'] = fixes[1] if len(fixes) > 1 else ''
    ansblk = re.search(r'id="dolAns"[^>]*>(.*?)</div>', dol, re.S)
    if ansblk:
        ps = [cl(p) for p in re.findall(r'<p[^>]*>(.*?)</p>', ansblk.group(1), re.S)]
        ps = [p for p in ps if p]
        corr = [p for p in ps if re.match(r'^(Corrected|\d\.)', p)]
        d['dol_ans']  = re.sub(r'^Corrected sentences?:\s*', '', corr[0]) if corr else (ps[0] if ps else '')
        d['dol_ans2'] = corr[1] if len(corr) > 1 else ''
        rest = [p for p in ps if p not in corr]
        d['dol_errors'] = rest[-1] if rest else ''

    # ── Copywork ─────────────────────────────────────────────────────────
    m = re.search(r'class="copywork-text"[^>]*>(.*?)</div>', g('copywork') or s, re.S)
    d['copywork'] = cl(m.group(1)) if m else ''
    m = re.search(r'class="copywork-instruction"[^>]*>(.*?)</div>', g('copywork') or s, re.S)
    d['copywork_note'] = cl(m.group(1)) if m else ''

    # ── Morphology (scoped) ──────────────────────────────────────────────
    mo = g('morph')
    d['morph_title'] = re.sub(r'^🌱\s*Morphology:\s*', '', t('morph')).strip()
    items = []
    # Order matters: the "input first, full word in <strong> after" shape must be
    # tried BEFORE the generic prefix+input one, or the generic pattern matches
    # with an empty prefix and reports the base word as the whole word.
    for m in re.finditer(r'class="fillin-item"[^>]*>\s*<input[^>]*data-answer="([^"]+)"[^>]*>\s*(?:&rarr;|&#8594;|→)?\s*<strong>([^<]+)</strong>', mo):
        items.append('%s — base word: %s' % (cl(m.group(2)), cl(m.group(1))))
    for m in ([] if items else re.finditer(r'class="fillin-item"[^>]*>([^<]*)<input[^>]*data-answer="([^"]+)"[^>]*>\s*([^<]*)', mo)):
        pre, ans, tail = cl(m.group(1)), cl(m.group(2)), cl(m.group(3)).lstrip('—→ ').strip()
        if re.search(r'_{3,}', pre):
            # cloze variant: the blank sits inside a full sentence
            items.append(re.sub(r'_{3,}', ans, pre))
        elif pre:
            items.append('%s%s%s' % (pre, ans, (' — ' + tail) if tail else ''))
        else:
            items.append('%s — base word: %s' % (tail or ans, ans))
    if not items:
        for m in re.finditer(r'class="fillin-item"[^>]*>\s*<input[^>]*data-answer="([^"]+)"[^>]*>\s*(?:&rarr;|→)?\s*<strong>([^<]+)</strong>', mo):
            items.append('%s — base word: %s' % (m.group(2).strip(), m.group(1).strip()))
    if not items:
        for m in re.finditer(r'class="key-concept-label"[^>]*>(.*?)</div>(.*?)(?=</div>\s*</div>|$)', mo, re.S):
            for p in re.findall(r'<p[^>]*>(.*?)</p>', m.group(2), re.S)[:4]:
                if cl(p): items.append(cl(p))
    d['morph_items'] = items[:5]
    d['morph_match'] = [cl(x) for x in re.findall(r'class="match-item is-word"[^>]*>([^<]+)<', mo)][:6]

    # ── Vocabulary (scoped) ──────────────────────────────────────────────
    vo = g('vocab')
    d['vocab_title'] = t('vocab')
    words = [cl(x) for x in re.findall(r'class="fc-word-back"[^>]*>([^<]+)<', vo)]
    defs  = [cl(x) for x in re.findall(r'class="fc-def"[^>]*>(.*?)</div>', vo, re.S)]
    vocab = [{'word': w, 'def': dv} for w, dv in zip(words, defs)]
    if not vocab:                                  # cloze days
        vocab = [{'word': cl(a), 'def': ''} for a in
                 re.findall(r'class="fillin-item"[^>]*>.*?data-answer="([^"]+)"', vo, re.S)]
    if not vocab:                                  # LWW/med: match-item pairs
        mi = [cl(x) for x in re.findall(r'class="match-item(?: is-word)?"[^>]*>(.*?)</div>', vo, re.S)]
        vocab = [{'word': mi[i], 'def': mi[i+1]} for i in range(0, len(mi)-1, 2)]
    if not vocab:
        # LWW/med Day 3: a cloze with <select>; the correct answer is the second
        # argument of checkVocabSel(). Keep the sentence with the blank marked.
        for m in re.finditer(r"<div style=\"padding:12px 16px;background:#fff;[^>]*>(.*?)</div>", vo, re.S):
            blk = m.group(1)
            ans = re.search(r"checkVocabSel\(\d+,'([^']+)'\)", blk)
            if not ans: continue
            sent = re.sub(r'<select[\s\S]*?</select>', ' ______ ', blk)
            sent = re.sub(r'<span[^>]*id="vocab_fb[\s\S]*?</span>', '', sent)
            vocab.append({'word': ans.group(1), 'def': cl(sent)})
    if not vocab:
        # W1-4 Day 4: "Use the Word!" — no cards, but the week's words are in the
        # match game or the worked example.
        ws = [cl(x) for x in re.findall(r'class="match-item is-word"[^>]*>([^<]+)<', vo)]
        if not ws:
            ws = [cl(x) for x in re.findall(r'<strong>Word:</strong>\s*([^<]+)<', vo)]
        vocab = [{'word': w, 'def': ''} for w in dict.fromkeys(ws)]
    d['vocab'] = vocab[:6]

    # ── Grammar (scoped) ─────────────────────────────────────────────────
    gr = g('gram')
    d['gram_title'] = re.sub(r'^✏️\s*Grammar:\s*', '', t('gram')).strip()
    gram = []
    for m in re.finditer(r'<div class="spotter-sentence"[^>]*>(.*?)<div class="spotter-result"', gr, re.S):
        pairs = re.findall(r'data-correct="(true|false)"[^>]*>([^<]*)</span>', m.group(1))
        if not pairs: continue
        choices = [cl(w) for _, w in pairs]
        ans = next((cl(w) for c, w in pairs if c == 'true'), '')
        # Week 1 offers two whole word-groups to choose between rather than
        # single words in a sentence; join those with a separator so the slide
        # reads as two options, not one run-on sentence.
        multi = len(choices) <= 3 and all(len(c.split()) > 2 for c in choices)
        sent = ('   |   ' if multi else ' ').join(choices)
        gram.append({'sentence': sent, 'answer': ans, 'choices': choices, 'pick_one': multi})
    if not gram:
        # W1-4: a tap-to-reveal classification game — the answer is baked into
        # the inline onclick, so pull the sentence and the label it reveals.
        for m in re.finditer(r"<span class=\"spotter-word\" onclick=\"[^\"]*textContent='([^']*)'[^>]*>(.*?)</span>", gr, re.S):
            gram.append({'sentence': cl(m.group(2)), 'answer': cl(m.group(1))})
    if not gram:
        # LWW / med / ext: inline-styled sentence + note cards, no game at all.
        for m in re.finditer(r'<div style="padding:12px 16px;background:#fff;[^>]*>\s*<div style="font-family:Lora[^>]*>(.*?)</div>\s*<div style="font-size:13px[^>]*>(.*?)</div>', gr, re.S):
            gram.append({'sentence': cl(m.group(1)), 'answer': cl(m.group(2))})
    if not gram:
        # LWW/ext Day 3-4: sentence frames to complete, or a write-your-own task.
        for fr in re.findall(r'>([^<>]{15,110}_____[^<>]{0,60})<', gr):
            gram.append({'sentence': cl(fr), 'answer': ''})
    d['grammar'] = gram[:4]
    m = re.search(r'class="callout[^"]*"[^>]*>.*?<p>(.*?)</p>', gr, re.S)
    d['gram_task'] = cl(m.group(1)) if m else ''
    d['gram_examples'] = [cl(x) for x in re.findall(r'class="task-sentence"[^>]*>(.*?)</div>', gr, re.S)][:2]

    # ── Spelling (scoped) ────────────────────────────────────────────────
    sp = g('spell')
    d['spell_title'] = re.sub(r'^🔠\s*Spelling:\s*', '', t('spell')).strip()
    labels = dict()
    cols = re.findall(r'class="sort-col-header"[^>]*>(.*?)</div>\s*<div class="sort-col-drop"[^>]*data-col="([^"]+)"', sp, re.S)
    for lbl, grp in cols: labels[grp] = cl(lbl)
    groups = {}
    for grp, word in re.findall(r'class="sort-chip" data-group="([^"]+)"[^>]*>([^<]*)<', sp):
        groups.setdefault(labels.get(grp, grp), []).append(cl(word))
    d['spell_groups'] = groups
    d['spell_rules'] = [cl(p) for p in re.findall(r'class="key-concept"[^>]*>(?:.*?)</div>(.*?)</div>', sp, re.S)][:1]

    # ── Writer's Workshop ────────────────────────────────────────────────
    m = re.search(r"Writer(?:&rsquo;|’)s Workshop:\s*Week\s*\d+\s*(?:&middot;|·)\s*([A-Z][A-Z ]*)</div>\s*<div[^>]*>(.*?)</div>", s, re.S)
    d['writing'] = {'stage': cl(m.group(1)), 'subtitle': cl(m.group(2))} if m else {'stage': '', 'subtitle': ''}
    return d

UNIT = [(1,1,'launch'),(2,5,'flatStanley'),(6,7,'nonfiction'),(8,16,'despereaux'),
        (18,22,'whippingBoy'),(23,24,'med'),(25,30,'lww'),(31,32,'extension')]
def unit_of(week):
    for a,b,u in UNIT:
        if a <= week <= b: return u
    return 'launch'

def main():
    base = sys.argv[1]; out = sys.argv[2]
    rows = []
    for week in range(1, 33):
        for day in (1,2,3,4):
            hits = glob.glob(os.path.join(base, 'lesson-%d-%d-*.html' % (week, day)))
            hits = [h for h in hits if not h.endswith('.bak-poetry')]
            if not hits: continue
            d = extract(hits[0], week, day)
            d['unit'] = unit_of(week)
            rows.append(d)
    json.dump(rows, open(out,'w'), ensure_ascii=False, indent=1)
    print('lessons extracted:', len(rows))
    bad = []
    for d in rows:
        miss = [k for k in ('vocab','grammar','spell_groups','dol_fix') if not d[k]]
        if miss: bad.append((d['file'], miss))
    print('lessons with empty sections:', len(bad))
    for f,m in bad[:40]: print('  ', f, m)

main()
