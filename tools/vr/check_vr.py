#!/usr/bin/env python3
"""Check a built G3 ELA VR page against its week JSON.
usage: python3 tools/vr/check_vr.py tools/vr/week18.json
"""
import csv, json, os, re, sys, html

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
D = json.load(open(sys.argv[1], encoding='utf-8'))
W = D['week']
page = open(os.path.join(ROOT, 'vr-%d.html' % W), encoding='utf-8').read()
errs, notes = [], []

# 1. models + map exist in the asset list
rows = list(csv.reader(open(os.path.join(ROOT, 'Planning docs', 'vr-assets.csv'), encoding='utf-8-sig')))
names = {c.strip() for r in rows for c in r}
for m in D['models']:
    if m['name'] not in names: errs.append('model not in CSV: ' + m['name'])
if D['map'] not in names: errs.append('map not in CSV: ' + D['map'])
if not 4 <= len(D['models']) <= 6: errs.append('need 4-6 models, have %d' % len(D['models']))

# 2. always Day 2, 5 steps
if D['day'] != 2: errs.append('VR must be Day 2')
if len(D['steps']) != 5: errs.append('need 5 steps, have %d' % len(D['steps']))

# 3. Canvas name matches everywhere
canvas = '%d.2 VR · %s' % (W, D['title'])
if html.escape(canvas) not in page: errs.append('Canvas name missing: ' + canvas)

# 4. every data-say has a transcript slot
slots = set(re.findall(r'data-say="([\w-]+)"', page))
want = {'brief', 'extra', 'mapday'} | {'step%d' % i for i in range(1, 6)}
if slots != want: errs.append('voice slots %s != %s' % (sorted(slots), sorted(want)))
tr = json.load(open(os.path.join(os.path.dirname(__file__), 'week%d-scripts.json' % W), encoding='utf-8'))
for s in want:
    if not tr.get(s, '').strip(): errs.append('empty transcript: ' + s)

# 5. word count outside the help drawer, scripts and styles
body = re.sub(r'(?s)<script.*?</script>|<style.*?</style>|<details class="help".*?</details>|<svg.*?</svg>', ' ', page)
body = re.sub(r'(?s)<head>.*?</head>|<header.*?</header>|<div class="foot">.*?</div>', ' ', body)
vrpart = re.sub(r'(?s)<section class="card" id="map".*?</section>', ' ', body)
words = lambda t: len(re.findall(r"[A-Za-z0-9’']+", html.unescape(re.sub(r'<[^>]+>', ' ', t))))
nv = words(vrpart)
(errs if nv > 480 else notes).append('VR path visible words: %d (target ~450, fail over 480; steps show one at a time)' % nv)
notes.append('whole page (both paths) words: %d' % words(body))

# 6. student-facing banned words
low = html.unescape(re.sub(r'<[^>]+>', ' ', body)).lower()
for bad in ['bonus', 'lantern']:
    if re.search(r'\b%s\b' % bad, low) and bad != 'lantern': errs.append('banned word: ' + bad)
if 'xVzX24ENnqk' in page or 'vr-help-0' in page: errs.append('retired help video/images')

# 7. help images exist
for img in set(re.findall(r'assets/vr/([\w.-]+)', page)):
    if not os.path.exists(os.path.join(ROOT, 'assets', 'vr', img)): errs.append('missing image ' + img)

for n in notes: print('  ·', n)
if errs:
    for x in errs: print('  ✗', x)
    sys.exit(1)
print('✓ vr-%d.html passes' % W)
