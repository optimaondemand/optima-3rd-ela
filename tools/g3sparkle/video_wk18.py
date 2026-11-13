#!/usr/bin/env python3
"""Week 18 gets the Nov 13 2026 Opti videos (as week 19): a film on every Word Study
section, Days 1-4, plus Read Like a Writer on Day 2 (18.2). Days 2-4 clips were already
recorded (fd84364); repeated lines were TRIMMED out of them (no re-recording), so the
DATA scripts below are the trimmed words. Writes data/lesson-18-N.json and the page
DATA together (setdata.py logic). Run after teach_wk18.py if that is ever re-run.
    python tools/g3sparkle/video_wk18.py"""
import io, json, re
TRIM = json.load(io.open('tools/g3sparkle/video/trimmed_wk18.json', encoding='utf-8'))
RWM = {"id": "rwm", "sel": ".rwm-box", "after": ":scope > .rwm-header", "label": "Opti shows you how", "fold": [],
       "script": "[warmly] Here's how Read Like a Writer works. I'll do one first, with a different sentence from Chapter 4. Like a snake striking, a ghostly hand darted through the fog and clutched his arm. Part one, read like a reader. What is happening? Someone in the fog grabs Jemmy, fast. Part two, read like a writer. What is the author doing? He says the hand moves like a snake striking, so we feel how quick and scary it is. Part three, mimic. Here's mine: Like a cat pouncing, my little sister grabbed the last cookie. Now it's your turn with the fog sentence. Write one sentence in each box.",
       "video": "g3ela-18-2-teach-rwm"}
WS = ('morph', 'vocab', 'gram', 'spell')
def write_page(f, D):
    html = io.open(f, encoding='utf-8', newline='').read()
    m = re.search(r'(<script type="application/json" id="oao-data">)(.*?)(</script>)', html, re.S)
    old = m.group(2)
    body = json.dumps(D, ensure_ascii=False, separators=(',', ':')) if '\n' not in old.strip() else json.dumps(D, ensure_ascii=False, indent=1)
    body = body.replace('</script', '<\\/script')
    lead = old[:len(old) - len(old.lstrip())]; tail = old[len(old.rstrip()):]
    io.open(f, 'w', encoding='utf-8', newline='').write(html[:m.start(2)] + lead + body + tail + html[m.end(2):])
for d in (1, 2, 3, 4):
    p = 'data/lesson-18-%d.json' % d
    raw = io.open(p, encoding='utf-8').read()
    ind = len(raw.split('\n')[1]) - len(raw.split('\n')[1].lstrip()) if '\n' in raw.strip() else None
    j = json.loads(raw)
    mods = j['teach']['mods']
    for m in mods:
        if m['id'] in WS:
            name = 'g3ela-18-%d-teach-%s' % (d, m['id'])
            m['video'] = name
            if name in TRIM: m['script'] = TRIM[name]
    if d == 2 and not any(m['id'] == 'rwm' for m in mods):
        i = next(n for n, m in enumerate(mods) if m['id'] == 'read'); mods.insert(i + 1, RWM)
    io.open(p, 'w', encoding='utf-8').write(json.dumps(j, ensure_ascii=False, indent=ind) + ('\n' if raw.endswith('\n') else ''))
    write_page([f for f in ('lesson-18-%d-wb.html' % d,)][0], j)
    print('18.%d videos:' % d, [m['id'] for m in mods if m.get('video')])
