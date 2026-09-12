#!/usr/bin/env python3
"""
OAO ELA Lesson Extractor
Reads lesson HTML files and outputs structured JSON for slide generation.

Usage:
  python3 extract_lessons.py --base-dir /path/to/optima-3rd-ela/ \
    --weeks 18-22 --suffix wb --out lesson_data.json

  --weeks: single week (18), range (18-22), or comma list (18,19,20)
  --suffix: filename suffix used in lesson files (wb, despereaux, lww, etc.)
            Use "" or "auto" to try common suffixes automatically.
  --out: output JSON path
"""

import re, json, os, argparse, sys
import html as _html

def cl(s):
    """Strip HTML tags and collapse whitespace."""
    return re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', '', s)).strip()

def clx(s):
    """cl() plus entity decoding -- slide text must not show &rarr; or &mdash;."""
    return _html.unescape(cl(s))

def section(html, start_comment, end_comment):
    """Extract HTML between two named comment markers.
    G3 decorates its markers (<!-- ═══ MORPHOLOGY ═══ -->), so match the NAME
    inside any comment rather than requiring an exact string."""
    def find(name, frm=0):
        m = re.compile(r'<!--[^>]*' + re.escape(name) + r'[^>]*-->').search(html, frm)
        return m.start() if m else -1
    i = find(start_comment)
    if i == -1:
        return ''
    j = find(end_comment, i + 1)
    return html[i:j] if j > -1 else html[i:]

def find_lesson_file(base_dir, week, day, suffix):
    """Find the HTML file for a given week/day, trying common suffixes."""
    candidates = []
    if suffix and suffix != 'auto':
        candidates = [f'lesson-{week}-{day}-{suffix}.html']
    else:
        # Try common patterns
        candidates = [
            f'lesson-{week}-{day}-wb.html',
            f'lesson-{week}-{day}-despereaux.html',
            f'lesson-{week}-{day}-lww.html',
            f'lesson-{week}-{day}-stanley-ch{day}.html',
            f'lesson-{week}-{day}-nonfiction.html',
            f'lesson-{week}-{day}-med.html',
            f'lesson-{week}-{day}-ext.html',
        ]
        # Also glob for anything matching lesson-{week}-{day}-*.html
        import glob
        globbed = glob.glob(os.path.join(base_dir, f'lesson-{week}-{day}-*.html'))
        candidates += [os.path.basename(g) for g in globbed]

    for name in candidates:
        path = os.path.join(base_dir, name)
        if os.path.exists(path):
            return path
    return None

def extract_lesson(html, week, day):
    """Extract all content from one lesson HTML file."""
    d = {'week': week, 'day': day}

    # ── Section scoping ────────────────────────────────────────────────────
    sec_morph = section(html, 'MORPHOLOGY', 'VOCABULARY')
    sec_vocab  = section(html, 'VOCABULARY', 'GRAMMAR')
    sec_gram   = section(html, 'GRAMMAR', 'SPELLING')
    sec_spell  = section(html, 'SPELLING', '/tab-words')

    # ── Chapter / lesson header ────────────────────────────────────────────
    ch_m = re.search(r'<h2[^>]*class="[^"]*lesson-title[^"]*"[^>]*>(.*?)</h2>', html, re.S)
    d['ch_range'] = cl(ch_m.group(1)) if ch_m else ''
    if not d['ch_range']:
        m = re.search(r'activity-title"[^>]*>\s*\U0001F4D5\s*Read:\s*([^<]+)<', html)
        if m: d['ch_range'] = cl(m.group(1))

    ch_title_m = (re.search(r'class="chapter-subtitle[^"]*"[^>]*>(.*?)</', html, re.S)
                  or re.search(r'class="chapter-title[^"]*"[^>]*>(.*?)</', html, re.S))
    d['ch_title'] = cl(ch_title_m.group(1)) if ch_title_m else ''

    # ── Big question / reading lens ────────────────────────────────────────
    bq_m = (re.search(r'class="big-question[^"]*"[^>]*>(.*?)</', html, re.S)
            or re.search(r'class="socratic-q[^"]*"[^>]*>(.*?)</', html, re.S))
    d['big_question'] = cl(bq_m.group(1)) if bq_m else ''

    wg_m = re.search(r'Good readers[^<]{20,300}', html)
    d['wgrd'] = wg_m.group(0).strip() if wg_m else ''

    # ── DOL ───────────────────────────────────────────────────────────────
    model_m = re.search(r'id="dolModel"[^>]*>(.*?)</div>', html, re.S)
    d['dol_model'] = cl(model_m.group(1)) if model_m else ''

    fix_m = re.search(r'id="dolFix"[^>]*>(.*?)</div>', html, re.S)
    if not fix_m:
        for w in re.finditer(r'class="dol-sentence-wrap"[^>]*>(.*?)</div>', html, re.S):
            ctx = html[max(0, w.start()-80):w.start()]
            if 'dolModel' not in ctx and 'dolAns' not in ctx:
                fix_m = w
                break
    d['dol_fix'] = cl(fix_m.group(1)) if fix_m else ''

    ans_m = re.search(r'id="dolAns"[^>]*>(.*?)</div>', html, re.S)
    if ans_m:
        corr = re.search(r'<strong>Corrected:</strong>(.*?)(?:<br|</)', ans_m.group(1), re.S)
        d['dol_ans'] = cl(corr.group(1)) if corr else cl(ans_m.group(1))
    else:
        d['dol_ans'] = ''

    err_m = (re.search(r'id="dolErrors?"[^>]*>(.*?)</', html, re.S)
             or re.search(r'class="dol-errors?"[^>]*>(.*?)</', html, re.S))
    d['dol_errors'] = cl(err_m.group(1)) if err_m else ''

    if not d['dol_model'] and not d['dol_fix']:
        # G3 pattern: a <!-- DOL --> section with two numbered fix-it sentences and
        # the corrected versions inside #dolAns. There is no separate model sentence.
        sec_dol = section(html, 'DOL', '/tab-warmup') or html
        fixes = [cl(f) for f in re.findall(r'class="task-sentence"[^>]*>(.*?)</div>', sec_dol, re.S)]
        fixes = [f for f in fixes if f]
        if fixes:
            d['dol_fix']  = fixes[0]
            d['dol_fix2'] = fixes[1] if len(fixes) > 1 else ''
            ans = [cl(a) for a in re.findall(r'<p[^>]*>\s*(\d\..*?)</p>', sec_dol, re.S)]
            d['dol_ans']  = ans[0] if ans else d['dol_ans']
            d['dol_ans2'] = ans[1] if len(ans) > 1 else ''
            m = re.search(r'Did you catch[^<]*', sec_dol)
            if m: d['dol_errors'] = cl(m.group(0))

    # ── Morphology (SCOPED to MORPHOLOGY section) ─────────────────────────
    morph_src = sec_morph if sec_morph else html
    morph_fills = []
    for m in re.finditer(
        r'class="fillin-item"[^>]*>([^<]*)<input[^>]*data-answer="([^"]+)"[^>]*>\s*([^<]*)</div>',
        morph_src
    ):
        prefix = m.group(1).strip()
        answer = m.group(2).strip()
        defn   = m.group(3).strip().lstrip('—').strip()
        morph_fills.append(f"{prefix}{answer} — {defn}")
    if not morph_fills:
        # G3 order: <input data-answer="BASE"> → <strong>FULLWORD</strong>
        for m in re.finditer(
            r'class="fillin-item"[^>]*>\s*<input[^>]*data-answer="([^"]+)"[^>]*>\s*(?:&rarr;|→)\s*<strong>([^<]+)</strong>',
            morph_src):
            morph_fills.append(f"{m.group(2).strip()} — base word: {m.group(1).strip()}")
    d['morph_fillin'] = morph_fills[:6]

    d['morph_match'] = [
        m.group(1).strip()
        for m in re.finditer(r'class="match-item is-word"[^>]*>([^<]+)<', morph_src)
    ][:6]

    mt_m = re.search(r'activity-title[^>]*>🌱[^<]*<', morph_src)
    d['morph_title'] = cl(mt_m.group(0)) if mt_m else ''

    # ── Vocabulary (SCOPED to VOCABULARY section) ─────────────────────────
    vocab = []
    if sec_vocab:
        # Days 1/2: flip cards
        words = re.findall(r'class="fc-word-back"[^>]*>([^<]+)<', sec_vocab)
        defs  = re.findall(r'class="fc-def"[^>]*>([^<]+)<', sec_vocab)
        if words:
            vocab = [{'word': w.strip(), 'def': dv.strip()} for w, dv in zip(words, defs)]
        else:
            # Days 3/4: cloze sentences — extract data-answer values
            cloze = re.findall(
                r'class="fillin-item"[^>]*>.*?data-answer="([^"]+)"', sec_vocab, re.S)
            vocab = [{'word': a.strip(), 'def': ''} for a in cloze]
        if not vocab:
            # Day-4 "Use the Word": the words only survive in the textarea labels.
            # Two spellings of the same Day-4 label are in use.
            vocab = [{'word': clx(w), 'def': ''} for w in
                     re.findall(r'data-label="Voca(?:b|bulary): ([^"]+)"', sec_vocab)]
        if not vocab:
            # W25-32 D3: a select-a-word cloze; the answer is the second argument
            # of checkVocabSel(). D4: a "Choose from:" list above a textarea.
            sel = re.findall(r"checkVocabSel\(\d+,'([^']+)'\)", sec_vocab)
            if sel:
                vocab = [{'word': w, 'def': ''} for w in sel]
            else:
                ch = re.search(r'Choose from:(.*?)</p>', sec_vocab, re.S)
                if ch:
                    vocab = [{'word': clx(w), 'def': ''}
                             for w in re.findall(r'<strong>([^<]+)</strong>', ch.group(1))]
        if not vocab:
            # W25-32 D2: the vocabulary activity is a MATCH GAME, not flip cards or
            # a cloze. Pair each is-word item with the plain item that shares its
            # data-match key. Without this the extractor reported NO VOCAB for
            # every one of those days even though the words were right there.
            pairs = {}
            for mm in re.finditer(
                    r'class="match-item( is-word)?"[^>]*data-match="([^"]+)"[^>]*>([^<]+)<', sec_vocab):
                key = mm.group(2)
                pairs.setdefault(key, {})['word' if mm.group(1) else 'def'] = clx(mm.group(3))
            vocab = [{'word': v['word'], 'def': v.get('def', '')}
                     for v in pairs.values() if v.get('word')]
    d['vocab'] = vocab[:8]

    # ── Grammar (SCOPED to GRAMMAR section) ───────────────────────────────
    gram_src = sec_gram if sec_gram else html
    gt_m = re.search(r'activity-title[^>]*>✏️[^<]*<', gram_src)
    d['grammar_title'] = cl(gt_m.group(0)) if gt_m else ''

    grammar = []
    for spot in re.finditer(
        r'class="spotter-sentence"[^>]*>(.*?)<div class="spotter-result"',
        gram_src, re.S
    ):
        raw = spot.group(1)
        word_pairs = re.findall(
            r'data-correct="(true|false)"[^>]*>(?:<strong>)?([^<]+?)(?:</strong>)?</span>', raw)
        all_words = [w for _, w in word_pairs]
        # Take FIRST data-correct="true" word only (guards against accidental double-marks)
        answer = next((w for c, w in word_pairs if c == 'true'), '')
        sentence = ' '.join(all_words)
        if sentence:
            grammar.append({'sentence': sentence, 'answer': answer})
    d['grammar'] = grammar[:6]

    # ── Spelling (SCOPED to SPELLING section) ─────────────────────────────
    # Prefer the SPELLING section comment; several units (W6-7 nonfiction, W25-32
    # LWW/ext) have no such comment, and falling back to the whole page made the
    # flip-card branch below pick up the VOCABULARY cards. Fall back to the
    # bl-navy spelling activity block instead, and only then to the whole page.
    spell_src = sec_spell
    if not spell_src:
        _si = html.find('\U0001f520 Spelling')
        if _si > -1:
            _si = html.rfind('<div class="activity bl-navy">', 0, _si)
            _sj = html.find('<div class="tab-next-wrap"', _si)
            _sk = html.find('<div class="activity ', _si + 10)
            _ends = [x for x in (_sj, _sk) if x > _si]
            spell_src = html[_si:min(_ends)] if _ends else html[_si:]
    if not spell_src:
        spell_src = html
    st_m = re.search(r'activity-title[^>]*>🔠[^<]*<', spell_src)
    d['spell_title'] = cl(st_m.group(0)) if st_m else ''

    # Map data-col values to column header labels
    col_headers = {}
    for col_m in re.finditer(r'data-col="([^"]+)"', spell_src):
        col_id = col_m.group(1)
        if col_id in col_headers:
            continue
        before = spell_src[:col_m.start()]
        hdr_pos = before.rfind('sort-col-header')
        if hdr_pos > -1:
            hm = re.search(r'sort-col-header[^>]*>(.*?)</div>',
                           spell_src[hdr_pos:hdr_pos+300], re.S)
            if hm:
                col_headers[col_id] = cl(hm.group(1))

    spell_groups = {}
    for chip in re.finditer(
        r'class="sort-chip"[^>]*data-group="([^"]+)"[^>]*>([^<]+)<', spell_src
    ):
        grp_id = chip.group(1)
        word   = chip.group(2).strip()
        label  = col_headers.get(grp_id, grp_id)
        spell_groups.setdefault(label, []).append(word)
    d['spell_groups'] = spell_groups

    # ── Spelling, non-sort activity types (added 2026-09-12) ──────────────
    # From W1-24 only D1 keeps the word sort; D2 is a Sound Detective spotter,
    # D3 a tap-to-build card grid, D4 a dice game. Without these branches the
    # extractor reported NO SPELLING for three days of every week and the deck
    # lost its spelling slide.
    if not spell_groups:
        # D2 — spotter rows: label is the row prompt, words are the choices,
        # the correct one marked so the teacher can read the answer off the slide.
        rows = re.findall(
            r'<p[^>]*>(Tap the[^<]*(?:<[^>]+>[^<]*)*?)</p>\s*'
            r'<div class="spotter-sentence"[^>]*>(.*?)</div>\s*</div>',
            spell_src, re.S)
        for prompt, body in rows:
            words = []
            for wm in re.finditer(r'data-correct="(true|false)"[^>]*>([^<]+)<', body):
                words.append(wm.group(2).strip() + (' \u2713' if wm.group(1) == 'true' else ''))
            if words:
                spell_groups.setdefault(clx(prompt), []).extend(words)
        # D3 — build cards: "before \u2192 after (hint)"
        for cm in re.finditer(
                r'class="(?:rv|ed)-card"[^>]*data-after="([^"]*)"[^>]*data-(?:hint|sound)="([^"]*)"[^>]*>\s*'
                r'<div[^>]*class="(?:rv|ed)-word">([^<]+)<', spell_src, re.S):
            spell_groups.setdefault('Build it', []).append(
                '%s \u2192 %s (%s)' % (clx(cm.group(3)), clx(cm.group(1)), clx(cm.group(2))))
        # D4 — dice words: "word \u2192 answer"
        # D3 variants — Word Ladder and Syllable Tiles
        for lm in re.finditer(r'class="ladder-rung"[^>]*data-word="([^"]*)"', spell_src):
            spell_groups.setdefault('Word ladder', []).append(clx(lm.group(1)))
        for tm in re.finditer(r'class="tile-word"[^>]*data-whole="([^"]*)"', spell_src):
            spell_groups.setdefault('Build the syllables', []).append(clx(tm.group(1)))
        # W25-31 D2 — the "find the pattern words in this passage" hunt
        pw = re.search(r'id="spellAns".*?Pattern words:\s*</strong>(.*?)</p>', spell_src, re.S)
        if pw:
            spell_groups.setdefault('Pattern words in the passage', []).extend(
                [w.strip() for w in clx(pw.group(1)).split(',') if w.strip()])
        # D3 variants — Proofreader and Cover, Write, Check
        for pm in re.finditer(
                r'data-good="([^"]*)"[^>]*data-why="([^"]*)"([^>]*)>([^<]+)<', spell_src):
            if 'data-ok' in pm.group(3):
                continue
            spell_groups.setdefault('Proofread', []).append(
                '%s \u2192 %s (%s)' % (clx(pm.group(4)), clx(pm.group(1)), clx(pm.group(2))))
        # Only when the SPELLING section really was found -- otherwise spell_src is
        # the whole page and this picks up the vocabulary flip cards instead.
        for fm in re.finditer(
                r'class="fc-word">([^<]+)<.*?class="fc-word-back">(.*?)</div>.*?class="fc-def">(.*?)</div>',
                spell_src, re.S):
            spell_groups.setdefault('Cover, write, check', []).append(
                '%s (%s)' % (clx(fm.group(1)), clx(fm.group(3))))
        # W3D4 / W4D4 — the older Magic E / Vowel Team transformer cards
        for mm in re.finditer(
                r'class="magic-e-card"[^>]*data-before="([^"]*)"[^>]*data-after="([^"]*)"'
                r'[^>]*data-vowel="([^"]*)"', spell_src, re.S):
            spell_groups.setdefault('Build it', []).append(
                '%s \u2192 %s (%s)' % (clx(mm.group(1)), clx(mm.group(2)), clx(mm.group(3))))
        dm = re.search(r'var (?:spellDice|edDiceWords)=\[(.*?)\];', spell_src, re.S)
        if dm:
            for w, a in re.findall(r'\{w:"(.*?)",s:"(.*?)"\}', dm.group(1)):
                spell_groups.setdefault('Dice words', []).append(
                    '%s \u2192 %s' % (clx(w), clx(a)))
        d['spell_groups'] = spell_groups

    # ── Pause questions ───────────────────────────────────────────────────
    pause_qs = []
    for pq in re.finditer(r'class="pause-q(?:uestion)?[^"]*"[^>]*>(.*?)</', html, re.S):
        t = cl(pq.group(1))
        if len(t) > 12:
            pause_qs.append(t)
    d['pause_qs'] = pause_qs[:4]

    # ── RWM (Days 3 & 4 only) ─────────────────────────────────────────────
    rwm_m   = re.search(r'class="rwm-sentence[^"]*"[^>]*>(.*?)</', html, re.S)
    craft_m = re.search(r'class="rwm-craft-note[^"]*"[^>]*>(.*?)</', html, re.S)
    d['rwm']       = cl(rwm_m.group(1))   if rwm_m   else ''
    d['rwm_craft'] = cl(craft_m.group(1)) if craft_m else ''
    d['rwm_steps'] = [
        cl(s.group(1))
        for s in re.finditer(r'class="rwm-step-text[^"]*"[^>]*>(.*?)</', html, re.S)
    ][:3]

    # ── Writing workshop ──────────────────────────────────────────────────
    ws_m    = re.search(r'class="writing-stage[^"]*"[^>]*>(.*?)</', html, re.S)
    ws_sub  = re.search(r'class="writing-subtitle[^"]*"[^>]*>(.*?)</', html, re.S)
    ws_pr   = re.search(r'class="writing-prompt[^"]*"[^>]*>(.*?)</', html, re.S)
    d['writing'] = {
        'stage':    cl(ws_m.group(1))   if ws_m   else '',
        'subtitle': cl(ws_sub.group(1)) if ws_sub else '',
        'prompt':   cl(ws_pr.group(1))  if ws_pr  else '',
    }

    return d


def parse_weeks(weeks_str):
    """Parse '18-22' → [18,19,20,21,22], '8,9,10' → [8,9,10], '6' → [6]."""
    if '-' in weeks_str:
        parts = weeks_str.split('-')
        return list(range(int(parts[0]), int(parts[1]) + 1))
    elif ',' in weeks_str:
        return [int(w.strip()) for w in weeks_str.split(',')]
    else:
        return [int(weeks_str)]


def main():
    parser = argparse.ArgumentParser(description='Extract OAO ELA lesson content to JSON.')
    parser.add_argument('--base-dir', required=True, help='Path to optima-3rd-ela/ folder')
    parser.add_argument('--weeks', required=True, help='Weeks to extract (e.g. 18-22 or 8,9,10)')
    parser.add_argument('--suffix', default='auto',
                        help='Filename suffix (wb, despereaux, lww) or "auto" to detect')
    parser.add_argument('--out', required=True, help='Output JSON path')
    args = parser.parse_args()

    weeks = parse_weeks(args.weeks)
    all_data = []
    missing = []

    for week in weeks:
        for day in range(1, 5):
            path = find_lesson_file(args.base_dir, week, day, args.suffix)
            if not path:
                missing.append(f'W{week}D{day}')
                continue
            html = open(path, encoding='utf-8').read()
            lesson = extract_lesson(html, week, day)
            all_data.append(lesson)

            # Quick validation report
            issues = []
            if not lesson['vocab']:        issues.append('NO VOCAB')
            if not lesson['spell_groups']: issues.append('NO SPELLING')
            if not lesson['grammar']:      issues.append('NO GRAMMAR')
            if not lesson['dol_model']:    issues.append('NO DOL MODEL')
            if day in (3,4) and not lesson['rwm']: issues.append('NO RWM')
            bad_morph = [m for m in lesson['morph_fillin'] if ' — ' not in m or m.split(' — ')[0].count(' ') > 0]
            if bad_morph: issues.append(f'MORPH PREFIX ONLY: {bad_morph[:1]}')

            status = '✓' if not issues else '⚠ ' + ', '.join(issues)
            print(f"W{week}D{day}: {status} | vocab={[v['word'] for v in lesson['vocab'][:3]]} "
                  f"| spell={list(lesson['spell_groups'].keys())[:2]}")

    json.dump(all_data, open(args.out, 'w'), indent=2)
    print(f"\n✓ {len(all_data)} lessons → {args.out}")
    if missing:
        print(f"⚠ Missing files: {', '.join(missing)}")

if __name__ == '__main__':
    main()
