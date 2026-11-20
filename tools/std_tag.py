"""Back-end multi-state standards tags for G3 ELA (Nov 20 2026).

Run from the optima-3rd-ela repo root:  python3 tools/std_tag.py 17 18 ... 32
Nothing visible changes on any page. For each lesson, fluency page and check-in
in a week it:
  * adds data-std (FL codes) and data-std-id to every activity block / quiz question
  * embeds <script type="application/json" id="oao-standards"> (before the LAST
    </body>) with every block's tags for FL, TX, AR, MO, AL, TN, PR and a lesson roll-up
  * writes standards/g3-week-WW.json, the week manifest
Block codes come from the block's strand (fixed rules) or, for the reading,
thinking and writing blocks, from the week's row below, which follows the week's
v4 S&S standards bar and the What Good Readers Do skill on the pages.
Re-running replaces earlier tags (idempotent).
"""
import json, re, sys, glob, os, html

CW = json.load(open('standards/crosswalk-g3.json', encoding='utf8'))
STATES = ['TX', 'AR', 'MO', 'AL', 'TN', 'PR']
def F(*c): return ['ELA.K12.' + x if x.startswith('EE') else 'ELA.3.' + x for x in c]

#            WGRD + reading blocks        thinking / response blocks         writing blocks
WEEKS = {
 17: dict(read=F('R.1.1'),          think=F('R.1.1', 'EE.1.1'),          write=F('C.1.3')),
 18: dict(read=F('R.1.3'),          think=F('R.1.3'),                    write=F('C.1.3')),
 19: dict(read=F('R.1.1'),          think=F('R.1.1'),                    write=F('C.1.3')),
 20: dict(read=F('R.1.1', 'EE.3.1'), think=F('R.1.1', 'EE.3.1'),         write=F('C.1.3')),
 21: dict(read=F('R.1.2'),          think=F('R.1.2'),                    write=F('C.1.3', 'C.1.5')),
 22: dict(read=F('R.1.1'),          think=F('R.1.1', 'R.1.2', 'EE.1.1'), write=F('C.1.3', 'C.2.1')),
 23: dict(read=F('R.2.2'),          think=F('R.2.2', 'R.2.3'),           write=F('C.1.4', 'C.4.1')),
 24: dict(read=F('R.2.1'),          think=F('R.2.1', 'R.2.2', 'R.2.4'),           write=F('C.1.4', 'C.1.5')),
 25: dict(read=F('R.1.1'),          think=F('R.1.1', 'EE.1.1'),          write=F('C.1.4')),
 26: dict(read=F('R.1.1'),          think=F('R.1.1'),                    write=F('C.1.4', 'C.1.5')),
 27: dict(read=F('R.1.3'),          think=F('R.1.3'),                    write=F('C.1.4', 'C.1.5')),
 28: dict(read=F('R.1.2'),          think=F('R.1.2', 'EE.1.1'),          write=F('C.1.3', 'C.1.5')),
 29: dict(read=F('R.1.2'),          think=F('R.1.2', 'EE.1.1'),          write=F('C.1.3', 'C.1.5')),
 30: dict(read=F('R.1.2'),          think=F('R.1.2'),                    write=F('C.1.3', 'C.1.5')),
 31: dict(read=F('R.3.3'),          think=F('R.3.3', 'EE.1.1'),          write=F('C.1.3')),
 32: dict(read=F('R.1.1'),          think=F('C.1.3', 'EE.6.1'),          write=F('C.1.3', 'C.1.5')),
}
CHECKIN_Q = {}

def rule(t, tab, W, bar):
    t = t.lower()
    on = lambda c: c in bar
    if re.search(r'\b(virtue|growing-up|courage|freedom|belief|character)\s+(watch|words)\b', t):
        return 'SKIP'   # sparkle.js lifts it off the page at load
    if 'what good readers do' in t: return W.get('wgrd', W['read'])
    if 'daily oral language' in t: return F('C.3.1')
    if 'copywork' in t: return F('C.1.1')
    if re.match(r'^\W*poetry', t) or 'poetry corner' in t or 'by heart' in t:
        # G3 Poetry teaches a figurative-language move inside a named poem type
        return [c for c in F('R.1.4', 'R.3.1') if on(c)] or F('R.3.1')
    if 'word study check' in t: return F('V.1.2')
    if 'summarize the whole book' in t: return F('R.3.2')
    if 'say it out loud' in t: return F('C.2.1')
    if 'digital t' in t: return F('C.5.2')
    if 'talk it over' in t: return F('EE.4.1')
    if re.match(r'^q\d\b', t) or 'article thinking' in t or 'reading answers' in t: return W['think']
    if 'word study connection' in t:
        if 'morph' in t: return F('V.1.2')
        if 'vocab' in t: return F('V.1.2')
        if 'grammar' in t: return F('C.3.1')
        return F('C.3.1', 'F.1.3')
    if re.sub(r'^\W+', '', t).startswith('morphology'): return F('V.1.2', 'F.1.3')
    if 'spelling' in t: return F('C.3.1', 'F.1.3')
    if 'grammar' in t: return F('C.3.1')
    if 'vocabulary' in t:
        c = F('V.1.2')
        if on('ELA.3.V.1.1'): c += F('V.1.1')   # G3 vocab: use the words in sentences
        if on('ELA.3.V.1.3') or re.search(r'context|cloze', t): c += F('V.1.3')
        return c
    if 'rwm' in t: return F('C.3.1')
    if 'digital t' in t: return F('C.5.2')
    if 'read the table' in t: return F('R.2.1')
    if 'talk it over' in t or 'discussion prompts' in t: return F('EE.4.1')
    if 'present your essay' in t: return F('C.2.1', 'C.5.1')
    if 'portfolio' in t or 'getting ready to celebrate' in t: return F('C.2.1', 'EE.6.1')
    if 'back to your own writing' in t: return F('C.3.1')
    if re.search(r'chapters? [\d\s\u2013-]+:? ?review|week at a glance|look(ing)? back', t): return W.get('review', W['read'])
    if re.search(r'writer.s workshop|writing con|part b|part c|final literary|final sentence|build your comparison', t):
        return W['write']
    if re.search(r'chapter thinking|whole-book|source thinking|cross-novel|theme comparison|part a', t): return W['think']
    if tab == 'fluency': return F('F.1.4')
    if tab in ('reading', 'assignment', 'workshop'): return W['read'] if tab == 'reading' else W['think']
    return None

def expand(fl):
    out = {'FL': fl}
    for st in STATES:
        if st == 'PR': out['PR'] = 'pending'; continue
        seen = []
        for c in fl:
            for x in CW['map'][c][st]:
                if x not in seen: seen.append(x)
        out[st] = seen
    return out

STRIP = [(re.compile(r' data-std="[^"]*" data-std-id="[^"]*"'), ''),
         (re.compile(r'<script type="application/json" id="oao-standards">.*?</script>\n', re.S), '')]

def tag_page(path, lid, week, W):
    s = open(path, encoding='utf8', newline='').read()
    for rx, rep in STRIP: s = rx.sub(rep, s)
    bm = re.search(r'class="standards-codes">(.*?)</div>', s, re.S)
    bar = set(re.findall(r'ELA\.[\w]+\.[A-Z]+\.\d\.\d', bm.group(1))) if bm else set()
    tabs = [(m.start(), m.group(1)) for m in re.finditer(r'<div class="tab-panel[^"]*" id="tab-(\w+)"', s)]
    is_checkin, is_fluency = 'checkin' in path, 'fluency' in path
    pat = (re.compile(r'<div class="section-icon (\w+)">|<div class="question"') if is_checkin else
           re.compile(r'<div class="activity(?: bl-[\w-]+)?"|<div class="(intro-card) theme-question"'))
    blocks, out, pos, n, section, qn, untagged = [], [], 0, 0, None, 0, []
    for m in pat.finditer(s):
        if is_checkin:
            if m.group(1): section = m.group(1); continue
            qn += 1
            fl = CHECKIN_Q.get((week, qn)) or {
                'grammar': F('C.3.1'), 'morph': F('V.1.2'), 'spelling': F('F.1.3', 'C.3.1'),
                'writing': W['write']}.get(section, W['think'])
            title = f'Q{qn} ({section})'
        elif m.group(1):
            fl, title = W.get('wonder', W['read']), "Big Question / Today's Wonder"
        else:
            tm = re.search(r'activity-title">(.*?)</div>', s[m.end():m.end() + 1500], re.S)
            title = html.unescape(re.sub(r'<[^>]+>', ' ', tm.group(1))).strip() if tm else ''
            title = re.sub(r'\s+', ' ', title)
            tab = [nm for p, nm in tabs if p < m.start()]
            fl = rule(title, 'fluency' if is_fluency else (tab[-1] if tab else ''), W, bar)
        if fl == 'SKIP': continue
        if not fl: untagged.append(title); continue
        n += 1
        bid = f'{lid}-{n:02d}'
        out.append(s[pos:m.end()]); out.append(f' data-std="{" ".join(fl)}" data-std-id="{bid}"'); pos = m.end()
        blocks.append(dict(id=bid, title=title, **expand(fl)))
    out.append(s[pos:]); s = ''.join(out)
    if not blocks and bar and not is_checkin:   # project pages: steps are built by script, so tag the page
        m = re.search(r'<div class="page"', s)
        if m:
            fl = sorted(bar); bid = f'{lid}-01'
            s = s[:m.end()] + f' data-std="{" ".join(fl)}" data-std-id="{bid}"' + s[m.end():]
            blocks.append(dict(id=bid, title='Project (whole page; its steps are built by script)', **expand(fl)))
    allfl = []
    for b in blocks:
        for c in b['FL']:
            if c not in allfl: allfl.append(c)
    page = dict(page=os.path.basename(path), lesson=lid, week=week, grade=3,
                crosswalk='standards/crosswalk-g3.json', standards_bar=sorted(bar),
                lesson_tags=expand(allfl), blocks=blocks)
    js = json.dumps(page, ensure_ascii=False).replace('</', '<\\/')
    i = s.rfind('</body>')   # the last one: earlier '</body>' strings sit inside print/export JS
    s = s[:i] + f'<script type="application/json" id="oao-standards">{js}</script>\n' + s[i:]
    open(path, 'w', encoding='utf8', newline='').write(s)
    return page, untagged

for week in [int(a) for a in sys.argv[1:]]:
    W = WEEKS[week]
    pages = sorted(glob.glob(f'lesson-{week}-[1-4]-*.html')) + [f'lesson-{week}-fluency.html', f'week-{week}-checkin.html'] + sorted(glob.glob(f'lesson-{week}-*-project.html'))
    manifest = dict(week=week, grade=3, status='DRAFT - for review', pages=[])
    weekfl = set(); barall = set()
    for p in pages:
        if not os.path.exists(p): continue
        m = re.match(r'lesson-(\d+-(?:\d|fluency|project))', p) or re.match(r'lesson-(\d+)-\w+-(project)', p)
        lid = ('.'.join(m.groups()) if m and m.lastindex == 2 else m.group(1).replace('-', '.')) if m else f'{week}.checkin'
        pg, un = tag_page(p, lid, week, W)
        manifest['pages'].append(pg)
        weekfl |= set(pg['lesson_tags']['FL']); barall |= set(pg['standards_bar'])
        print(f'{p}: {len(pg["blocks"])} blocks' + (f'  UNTAGGED: {un}' if un else ''))
    print(f'  week {week}: bar codes never tagged: {sorted(barall - weekfl)}  tagged but not on bar: {sorted(weekfl - barall)}')
    os.makedirs('standards', exist_ok=True)
    json.dump(manifest, open(f'standards/g3-week-{week}.json', 'w', encoding='utf8'), indent=1, ensure_ascii=False)
