#!/usr/bin/env python3
"""G3 ELA weekly VR page: tools/vr/week<W>.json -> vr-<W>.html (repo root).

Reading Road Stops (Bethany, 9 Nov 2026): one VR per week, always Day 2.
VR path = photo straight to Canvas from the headset, earns the road stamp.
Road Map Day (no headset) = on-page clue game + 2 sentence frames -> PDF, earns the Map stamp.
Opti voices the brief, every step, the Extra stop and the Road Map Day intro:
assets/audio/guide/opti/g3ela-vr-<W>-<slot>.mp3 (each 🔊 stays hidden until its file exists).

usage: python3 tools/vr/build_vr.py tools/vr/week18.json
"""
import html, json, os, re, sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
D = json.load(open(sys.argv[1], encoding='utf-8'))
W = D['week']
e = lambda t: html.escape(str(t), quote=True)

def md(t):
    """**bold** -> <b>, escape everything else"""
    return re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', e(t))

def plain(t):
    return re.sub(r'\*\*(.+?)\*\*', r'\1', t)

CANVAS = '%d.%d VR · %s' % (W, D['day'], D['title'])

# ── small drawings for the models and the Road Map Day game (aria-hidden) ──
ICONS = {
 'horse': '<svg viewBox="0 0 64 64"><path d="M14 50 L16 34 Q14 26 22 22 L34 20 L42 10 L46 12 L44 18 Q52 22 52 30 L48 32 L44 28 L44 50 L40 50 L39 36 L24 38 L22 50 L18 50 L18 40 Z" fill="#F4F1EA" stroke="#5B4A36" stroke-width="2" stroke-linejoin="round"/><path d="M42 10 Q36 16 34 20" stroke="#B9A98F" stroke-width="3" fill="none"/><circle cx="46" cy="22" r="1.6" fill="#3B2A14"/></svg>',
 'basket': '<svg viewBox="0 0 64 64"><path d="M10 28 H54 L49 54 H15 Z" fill="#C8955A" stroke="#7A5428" stroke-width="2" stroke-linejoin="round"/><path d="M12 36 H52 M13 44 H51 M20 28 V54 M28 28 V54 M36 28 V54 M44 28 V54" stroke="#9A6A36" stroke-width="1.6"/><path d="M8 24 H56 V30 H8 Z" fill="#B07D45" stroke="#7A5428" stroke-width="2"/></svg>',
 'cloak': '<svg viewBox="0 0 64 64"><path d="M26 10 Q32 6 38 10 L40 16 Q52 36 54 56 Q32 60 10 56 Q12 36 24 16 Z" fill="#2B2B33" stroke="#111" stroke-width="2" stroke-linejoin="round"/><path d="M24 16 Q32 20 40 16" stroke="#C7922C" stroke-width="2.5" fill="none"/><path d="M32 22 Q30 40 32 58" stroke="#46464F" stroke-width="2" fill="none"/></svg>',
 'moon': '<svg viewBox="0 0 64 64"><circle cx="32" cy="32" r="22" fill="#F4E9BE" stroke="#C9B676" stroke-width="2"/><circle cx="24" cy="26" r="4" fill="#E3D49A"/><circle cx="38" cy="38" r="5" fill="#E3D49A"/><circle cx="39" cy="22" r="2.5" fill="#E3D49A"/></svg>',
 'sword': '<svg viewBox="0 0 64 64"><path d="M30 6 H34 V42 H30 Z" fill="#C9CFD8" stroke="#6B7690" stroke-width="2"/><path d="M22 42 H42 V46 H22 Z" fill="#C7922C" stroke="#7A5A10" stroke-width="2"/><path d="M29 46 H35 V58 H29 Z" fill="#6E4E22"/></svg>',
 'dog': '<svg viewBox="0 0 64 64"><path d="M14 46 L16 30 Q18 24 26 24 H40 L46 16 L52 18 L50 26 Q54 30 50 34 H46 L44 46 H40 L39 36 H24 L22 46 H18 Z" fill="#B88A55" stroke="#6E4E22" stroke-width="2" stroke-linejoin="round"/><circle cx="48" cy="24" r="1.6" fill="#3B2A14"/></svg>',
 'frog': '<svg viewBox="0 0 64 64"><ellipse cx="32" cy="40" rx="20" ry="12" fill="#5E9B4C" stroke="#2F5A26" stroke-width="2"/><circle cx="23" cy="28" r="6" fill="#5E9B4C" stroke="#2F5A26" stroke-width="2"/><circle cx="41" cy="28" r="6" fill="#5E9B4C" stroke="#2F5A26" stroke-width="2"/><circle cx="23" cy="28" r="2" fill="#111"/><circle cx="41" cy="28" r="2" fill="#111"/></svg>'
}
NAMES = {'horse': 'a horse', 'basket': 'a basket', 'cloak': 'a cloak', 'moon': 'the moon', 'sword': 'a sword', 'dog': 'a dog', 'frog': 'a frog'}

def stamp_svg(ink, label):
    """horseshoe in a double ring; WEEK n curves along the top, the stamp name along the bottom"""
    uid = re.sub(r'\W', '', label.lower())[:12] or 'st'
    return ('<svg class="stamp" viewBox="0 0 140 140" aria-hidden="true"><defs>'
            '<path id="t-%s" d="M24 70 A46 46 0 0 1 116 70"/><path id="b-%s" d="M20 70 A50 50 0 0 0 120 70"/></defs>'
            '<circle cx="70" cy="70" r="64" fill="none" stroke="%s" stroke-width="5"/>'
            '<circle cx="70" cy="70" r="58" fill="none" stroke="%s" stroke-width="1.5" stroke-dasharray="4 4"/>'
            '<path d="M53 90 Q46 54 70 46 Q94 54 87 90 L78 90 Q83 62 70 59 Q57 62 62 90 Z" fill="%s"/>'
            '<circle cx="55" cy="67" r="2.2" fill="#fff"/><circle cx="59" cy="81" r="2.2" fill="#fff"/><circle cx="85" cy="67" r="2.2" fill="#fff"/><circle cx="81" cy="81" r="2.2" fill="#fff"/>'
            '<text font-family="Nunito,sans-serif" font-weight="900" font-size="11" fill="%s" letter-spacing="1.5"><textPath href="#t-%s" startOffset="50%%" text-anchor="middle">WEEK %d</textPath></text>'
            '<text font-family="Nunito,sans-serif" font-weight="900" font-size="10" fill="%s" letter-spacing="1"><textPath href="#b-%s" startOffset="50%%" text-anchor="middle" dominant-baseline="hanging">%s</textPath></text>'
            '</svg>') % (uid, uid, ink, ink, ink, ink, uid, W, ink, uid, e(label.upper()))

def say_p(slot, inner, cls='do'):
    return '<p class="%s" data-say="%s">%s</p>' % (cls, slot, inner)

# ── VR steps ──
models_html = ''.join(
    '<li class="model"><span class="mi" aria-hidden="true">%s</span><span><b>%s</b>%s<span class="why">%s</span></span></li>'
    % (ICONS.get(m['icon'], ''), e(m['name']), ('<small>type: %s</small>' % e(m['type'])) if m['type'] != m['name'] else '', e(m['why'])) for m in D['models'])
HOWTO_MOVE = ('<div class="howto">✋ <b>To move a model:</b> grab it with the <b>palm trigger</b> (the button under your middle finger). '
              'Use <b>both</b> palm triggers to make it bigger or smaller.</div>')
steps_html = ''
for i, s in enumerate(D['steps']):
    n = i + 1
    if s.get('submit'):
        body = ('Stand back so you can see %s. Open your menu, click <b>Library</b>, then <b>Camera</b>. Move the tablet until it all fits, then click <b>Take photo</b>. '
                'Now click the <b>Canvas</b> tab and pick <b>%s</b>. Click <b>Choose from My Files</b>, pick your photo, click <b>Use this file</b>, then <b>Submit to Canvas</b>. '
                'Look for the green <b>Submitted</b> tag. Last, press the <b>Meta button</b> and click <b>Quit</b>.') % (e(s['fits']), e(CANVAS))
        s['_spoken'] = s.get('spoken') or plain(re.sub(r'<[^>]+>', '', body))
    else:
        body = md(s['text'])
        s['_spoken'] = s.get('spoken') or (plain(s['text']) + ((' ' + s['frame']) if s.get('frame') else ''))
    extra = ''
    if s.get('first'):
        body = '<span class="howto first">🔗 <b>First time only:</b> connect Canvas at <a href="https://xr.optimaed.com" target="_blank" rel="noopener">xr.optimaed.com</a> first. See <b>Having trouble in VR?</b> below.</span>' + body
    if i == 0:
        extra += '<ul class="models">' + models_html + '</ul>'
    if s.get('howto') == 'move':
        extra += HOWTO_MOVE
    if s.get('frame'):
        extra += '<div class="howto say-it">🗣 ' + e(s['frame']) + '</div>'
    if s.get('submit'):
        extra += '<div class="howto">🔁 Want to fix it? Take a new photo and submit again.</div>'
    steps_html += ('<li class="step" data-n="%d" hidden><div class="step-n">Step %d of %d · %s</div>%s%s'
                   '<button type="button" class="btn gold next-step">%s</button></li>') % (
        n, n, len(D['steps']), e(s['title']), say_p(s['say'], body, 'step-t'), extra,
        'Done! Next step →' if n < len(D['steps']) else 'I did it! Show my stamp')

# ── Road Map Day ──
M = D['mapday']
choice_html = ''.join('<button type="button" class="obj" data-o="%s"><span aria-hidden="true">%s</span>%s</button>' % (o, ICONS[o], e(NAMES[o].split(' ', 1)[1])) for o in M['choices'])
frames_html = ''
for k, f in enumerate(M['frames']):
    chips = ''.join('<button type="button" class="chipx" data-k="%d">%s</button>' % (k, e(h)) for h in f['hints'])
    frames_html += ('<div class="frame"><label for="fr%d"><b>%s</b> …</label><textarea id="fr%d" maxlength="300" data-start="%s"></textarea>'
                    '<div class="chips"><span>Need an idea? Tap one:</span>%s</div></div>') % (k, e(f['start']), k, e(f['start']), chips)

TRANSCRIPTS = {'brief': D['brief'], 'mapday': M['intro'], 'extra': plain(D['extra']['text'])}
for s in D['steps']:
    TRANSCRIPTS[s['say']] = s['_spoken']

page = open(os.path.join(os.path.dirname(__file__), 'template.html'), encoding='utf-8').read()
REPL = {
 '{{TITLE}}': e(D['title']), '{{CANVAS}}': e(CANVAS), '{{WEEK}}': str(W), '{{BOOK}}': e(D['book']), '{{CHAPTERS}}': e(D['chapters']),
 '{{MAP}}': e(D['map']), '{{BRIEF}}': e(D['brief']), '{{LOOK}}': e(D['look']),
 '{{JOB}}': ('<b>1</b> Build the scene in VR → <b>2</b> Take a photo → <b>3</b> Submit it to Canvas' if D['pattern'] == 'A'
             else '<b>1</b> Find the place in VR → <b>2</b> Take a photo → <b>3</b> Submit it to Canvas'),
 '{{STEPS}}': steps_html, '{{EXTRA}}': md(D['extra']['text']), '{{EXTRA_ICON}}': ICONS.get('frog', ''), '{{POINTS}}': e(D['points']),
 '{{STAMP_VR}}': stamp_svg('#B8860B', D['stamp']['name']), '{{STAMP_MAP}}': stamp_svg('#1E3A78', 'Road Map Day'),
 '{{MAP_INTRO}}': e(M['intro']), '{{CHOICES}}': choice_html, '{{FRAMES}}': frames_html, '{{MINW}}': str(M['minWords']),
 '{{DATA}}': json.dumps({'week': W, 'canvas': CANVAS, 'clues': M['clues'], 'icons': {k: ICONS[k] for k in M['choices']},
                          'names': NAMES, 'minWords': M['minWords'], 'title': D['title'], 'transcripts': TRANSCRIPTS},
                         ensure_ascii=False).replace('</', '<\\/'),
}
for k, v in REPL.items():
    page = page.replace(k, v)
assert '{{' not in page, re.findall(r'\{\{\w+\}\}', page)
out = os.path.join(ROOT, 'vr-%d.html' % W)
open(out, 'w', encoding='utf-8').write(page)
json.dump(TRANSCRIPTS, open(os.path.join(os.path.dirname(__file__), 'week%d-scripts.json' % W), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('wrote', out)
