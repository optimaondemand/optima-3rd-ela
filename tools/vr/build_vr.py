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
 'frog': '<svg viewBox="0 0 64 64"><ellipse cx="32" cy="40" rx="20" ry="12" fill="#5E9B4C" stroke="#2F5A26" stroke-width="2"/><circle cx="23" cy="28" r="6" fill="#5E9B4C" stroke="#2F5A26" stroke-width="2"/><circle cx="41" cy="28" r="6" fill="#5E9B4C" stroke="#2F5A26" stroke-width="2"/><circle cx="23" cy="28" r="2" fill="#111"/><circle cx="41" cy="28" r="2" fill="#111"/></svg>',
 'trees': '<svg viewBox="0 0 64 64"><path d="M8 54 L20 18 L32 54Z" fill="#3E7A45" stroke="#22492A" stroke-width="2" stroke-linejoin="round"/><path d="M26 54 L40 10 L54 54Z" fill="#2F6A3A" stroke="#22492A" stroke-width="2" stroke-linejoin="round"/><path d="M18 54 H24 V60 H18Z M37 54 H43 V60 H37Z" fill="#6E4E22"/></svg>',
 'nopath': '<svg viewBox="0 0 64 64"><path d="M22 60 Q30 40 26 20 Q24 10 32 4 M42 60 Q46 40 40 20 Q38 10 40 4" stroke="#B88A55" stroke-width="5" fill="none"/><circle cx="32" cy="32" r="24" fill="none" stroke="#C0545C" stroke-width="5"/><path d="M15 15 L49 49" stroke="#C0545C" stroke-width="5"/></svg>',
 'hut': '<svg viewBox="0 0 64 64"><path d="M8 32 L32 12 L56 32Z" fill="#C9A66B" stroke="#7A5428" stroke-width="2" stroke-linejoin="round"/><path d="M14 30 H50 V56 H14Z" fill="#8A6236" stroke="#5B3F1E" stroke-width="2"/><path d="M28 40 H38 V56 H28Z" fill="#3B2A14"/><path d="M14 38 H50 M14 46 H50" stroke="#6E4E22" stroke-width="1.5"/></svg>',
 'shade': '<svg viewBox="0 0 64 64"><path d="M6 30 Q32 2 58 30Z" fill="#2F6A3A" stroke="#22492A" stroke-width="2"/><path d="M30 30 H34 V58 H30Z" fill="#6E4E22"/><ellipse cx="32" cy="58" rx="22" ry="4" fill="#1E3324" opacity=".5"/></svg>',
 'billy': '<svg viewBox="0 0 64 64"><circle cx="32" cy="30" r="16" fill="#E8C29A" stroke="#7A5428" stroke-width="2"/><path d="M16 28 Q18 10 32 10 Q46 10 48 28 Q44 18 32 18 Q20 18 16 28Z" fill="#B5472B"/><path d="M18 34 Q20 52 32 54 Q44 52 46 34 Q40 44 32 44 Q24 44 18 34Z" fill="#B5472B"/><circle cx="26" cy="28" r="2" fill="#3B2A14"/><circle cx="38" cy="28" r="2" fill="#3B2A14"/></svg>',
 'cutwater': '<svg viewBox="0 0 64 64"><ellipse cx="32" cy="32" rx="11" ry="18" fill="#E8C29A" stroke="#7A5428" stroke-width="2"/><path d="M21 22 Q32 6 43 22" fill="#4A3A2A"/><circle cx="28" cy="28" r="1.8" fill="#3B2A14"/><circle cx="36" cy="28" r="1.8" fill="#3B2A14"/><path d="M28 42 H36" stroke="#7A5428" stroke-width="2"/></svg>',
 'jemmy': '<svg viewBox="0 0 64 64"><circle cx="32" cy="34" r="15" fill="#F1D3B3" stroke="#7A5428" stroke-width="2"/><path d="M17 30 Q20 14 32 14 Q44 14 47 30 Q42 22 34 24 Q26 20 17 30Z" fill="#6E4E22"/><circle cx="27" cy="33" r="1.8" fill="#3B2A14"/><circle cx="37" cy="33" r="1.8" fill="#3B2A14"/><path d="M27 41 Q32 44 37 41" stroke="#7A5428" stroke-width="2" fill="none"/></svg>',
 'prince': '<svg viewBox="0 0 64 64"><circle cx="32" cy="36" r="14" fill="#F4DCC2" stroke="#7A5428" stroke-width="2"/><path d="M18 22 L22 10 L28 18 L32 8 L36 18 L42 10 L46 22Z" fill="#E0B23A" stroke="#7A5A10" stroke-width="2" stroke-linejoin="round"/><circle cx="27" cy="35" r="1.8" fill="#3B2A14"/><circle cx="37" cy="35" r="1.8" fill="#3B2A14"/><path d="M27 44 Q32 41 37 44" stroke="#7A5428" stroke-width="2" fill="none"/></svg>'
}
# kit v3 (Nov 16 2026): any icon not drawn above can be an emoji from the week JSON's "emoji" map
for _k, _v in D.get('emoji', {}).items():
    ICONS.setdefault(_k, '<svg viewBox="0 0 64 64"><text x="32" y="47" font-size="42" text-anchor="middle">%s</text></svg>' % _v)
NAMES = {'horse': 'a horse', 'basket': 'a basket', 'cloak': 'a cloak', 'moon': 'the moon', 'sword': 'a sword', 'dog': 'a dog', 'frog': 'a frog'}
NAMES.update({'trees': 'thick trees', 'nopath': 'no path', 'hut': 'a hut', 'shade': 'deep shade', 'billy': 'a Hold-Your-Nose Billy', 'cutwater': 'a Cutwater', 'jemmy': 'a Jemmy', 'prince': 'a Prince Brat'})
NAMES.update(D.get('mapday', {}).get('names', {}))

ART = {'horseshoe': '<path d="M53 90 Q46 54 70 46 Q94 54 87 90 L78 90 Q83 62 70 59 Q57 62 62 90 Z" fill="%s"/><circle cx="55" cy="67" r="2.2" fill="#fff"/><circle cx="59" cy="81" r="2.2" fill="#fff"/><circle cx="85" cy="67" r="2.2" fill="#fff"/><circle cx="81" cy="81" r="2.2" fill="#fff"/>',
       'hut': '<path d="M46 70 L70 48 L94 70 Z" fill="%s"/><path d="M52 68 H88 V92 H52 Z" fill="%s"/><path d="M65 78 H75 V92 H65 Z" fill="#fff"/>'}
def stamp_svg(ink, label, art='horseshoe'):
    """horseshoe in a double ring; WEEK n curves along the top, the stamp name along the bottom"""
    uid = re.sub(r'\W', '', label.lower())[:12] or 'st'
    return ('<svg class="stamp" viewBox="0 0 140 140" aria-hidden="true"><defs>'
            '<path id="t-%s" d="M24 70 A46 46 0 0 1 116 70"/><path id="b-%s" d="M20 70 A50 50 0 0 0 120 70"/></defs>'
            '<circle cx="70" cy="70" r="64" fill="none" stroke="%s" stroke-width="5"/>'
            '<circle cx="70" cy="70" r="58" fill="none" stroke="%s" stroke-width="1.5" stroke-dasharray="4 4"/>'
            '%s'
            '<text font-family="Nunito,sans-serif" font-weight="900" font-size="11" fill="%s" letter-spacing="1.5"><textPath href="#t-%s" startOffset="50%%" text-anchor="middle">WEEK %d</textPath></text>'
            '<text font-family="Nunito,sans-serif" font-weight="900" font-size="10" fill="%s" letter-spacing="1"><textPath href="#b-%s" startOffset="50%%" text-anchor="middle" dominant-baseline="hanging">%s</textPath></text>'
            '</svg>') % (uid, uid, ink, ink, (ART[art].replace('%s', ink) if art in ART else '<text x="70" y="86" font-size="34" text-anchor="middle">%s</text>' % art), ink, uid, W, ink, uid, e(label.upper()))

def say_p(slot, inner, cls='do'):
    return '<p class="%s" data-say="%s">%s</p>' % (cls, slot, inner)

# ── VR steps ──
models_html = ''.join(
    '<li class="model"><span class="mi" aria-hidden="true">%s</span><span><b>%s</b>%s<span class="why">%s</span></span></li>'
    % (ICONS.get(m['icon'], ''), e(m['name']), ('<small>type: %s</small>' % e(m['type'])) if m.get('type', m['name']) != m['name'] else '', e(m['why'])) for m in (D.get('models') or D['lookfors']))
# Shared words (Bethany, Nov 16 2026): the same Go in / Snap and submit clips every week from week 19 on, recorded once:
# assets/audio/guide/opti/g3ela-vr-shared-{go,submit}.mp3, copied to each week's step2 / step5 file name.
SHARED_GO = ('Put on your headset and open the <b>On-Demand</b> app. Click <b>Explore</b>, type today’s map in <b>Filter environments</b>, '
             'and click it. Then click <b>Begin Solo</b>.')
SHARED_SUBMIT = ('Stand back so it all fits. Open your menu: <b>Library</b>, then <b>Camera</b>, then <b>Take photo</b>. '
                 'Click the <b>Canvas</b> tab, pick this week’s VR assignment, and click <b>Choose from My Files</b>. '
                 'Pick your photo, click <b>Use this file</b>, then <b>Submit to Canvas</b>. Look for the green <b>Submitted</b> tag. '
                 'Then press the <b>Meta button</b> and click <b>Quit</b>.')
HOWTO_MOVE = ('<div class="howto">✋ <b>To move a model:</b> grab it with the <b>palm trigger</b> (the button under your middle finger). '
              'Use <b>both</b> palm triggers to make it bigger or smaller.</div>')
steps_html = ''
for i, s in enumerate(D['steps']):
    n = i + 1
    if s.get('submit') and D.get('sharedSubmit'):
        body = SHARED_SUBMIT
        s['_spoken'] = plain(re.sub(r'<[^>]+>', '', body))
    elif s.get('submit'):
        body = ('Stand back so you can see %s. Open your menu, click <b>Library</b>, then <b>Camera</b>. Move the tablet until it all fits, then click <b>Take photo</b>. '
                'Now click the <b>Canvas</b> tab and pick <b>%s</b>. Click <b>Choose from My Files</b>, pick your photo, click <b>Use this file</b>, then <b>Submit to Canvas</b>. '
                'Look for the green <b>Submitted</b> tag. Last, press the <b>Meta button</b> and click <b>Quit</b>.') % (e(s['fits']), e(CANVAS))
        s['_spoken'] = s.get('spoken') or plain(re.sub(r'<[^>]+>', '', body))
    elif s.get('shared') == 'go':
        body = SHARED_GO
        s['_spoken'] = plain(re.sub(r'<[^>]+>', '', body))
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
    if s.get('note'):
        extra += '<div class="howto">' + md(s['note']) + '</div>'
    if s.get('submit') and D.get('sharedSubmit'):
        extra += '<div class="howto">📸 Your photo shows %s. In Canvas, pick <b>%s</b>.</div>' % (e(s['fits']), e(CANVAS))
    if s.get('submit'):
        extra += '<div class="howto">🔁 Want to fix it? Take a new photo and submit again.</div>'
    steps_html += ('<li class="step" data-n="%d" hidden><div class="step-n">Step %d of %d · %s</div>%s%s'
                   '<button type="button" class="btn gold next-step">%s</button></li>') % (
        n, n, len(D['steps']), e(s['title']), say_p(s['say'], body, 'step-t'), extra,
        'Done! Next step →' if n < len(D['steps']) else 'I did it! Show my stamp')

# ── Road Map Day ──
M = D['mapday']
choice_html = ''.join('<button type="button" class="obj" data-o="%s"><span aria-hidden="true">%s</span>%s</button>' % (o, ICONS[o], e(re.sub(r'^(a|an|the) ', '', NAMES[o]))) for o in M['choices'])
frames_html = ''
for k, f in enumerate(M['frames']):
    chips = ''.join('<button type="button" class="chipx" data-k="%d">%s</button>' % (k, e(h)) for h in f['hints'])
    frames_html += ('<div class="frame"><label for="fr%d"><b>%s</b> …</label><textarea id="fr%d" maxlength="300" data-start="%s"></textarea>'
                    '<div class="chips"><span>Need an idea? Tap one:</span>%s</div></div>') % (k, e(f['start']), k, e(f['start']), chips)


SCENES = {'night-forest': '<div class="scene" aria-label="A forest at night, waiting for the runaways\' things">\n      <svg class="bg" viewBox="0 0 600 320" aria-hidden="true"><defs><linearGradient id="sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#12204A"/><stop offset="1" stop-color="#2E4470"/></linearGradient></defs>\n        <rect width="600" height="320" fill="url(#sky)"/><g fill="#fff" opacity=".7"><circle cx="60" cy="40" r="1.4"/><circle cx="160" cy="22" r="1.2"/><circle cx="250" cy="60" r="1.1"/><circle cx="330" cy="30" r="1.4"/><circle cx="560" cy="70" r="1.2"/></g>\n        <path d="M0 250 Q150 230 300 248 T600 244 V320 H0Z" fill="#1E3324"/>\n        <g fill="#16291C"><path d="M20 260 L60 120 L100 260Z"/><path d="M80 262 L118 150 L156 262Z"/><path d="M470 258 L512 130 L554 258Z"/><path d="M530 262 L566 160 L600 262Z"/><path d="M380 256 L410 170 L440 256Z"/></g>\n        <path d="M0 290 Q300 270 600 292 V320 H0Z" fill="#284430"/>\n      </svg>\n      <div class="slot" id="slot-moon" style="left:66%;top:6%">moon</div>\n      <div class="slot" id="slot-horse" style="left:30%;top:52%">horse</div>\n      <div class="slot" id="slot-basket" style="left:48%;top:62%">basket</div>\n      <div class="slot" id="slot-cloak" style="left:14%;top:60%">cloak</div>\n    </div>',
 'clearing': '<div class="scene" aria-label="ARIA"><svg class="bg" viewBox="0 0 600 320" aria-hidden="true"><rect width="600" height="320" fill="#CFE6D6"/><g fill="#E9F3C8" opacity=".6"><path d="M180 0 L240 0 L330 320 L250 320Z"/><path d="M330 0 L370 0 L430 320 L380 320Z"/></g><path d="M0 236 Q300 214 600 234 V320 H0Z" fill="#5E8C49"/><g fill="#2F5A2C"><path d="M0 250 L40 70 L80 250Z"/><path d="M60 252 L96 110 L132 252Z"/><path d="M470 250 L510 80 L550 250Z"/><path d="M530 252 L566 120 L600 252Z"/></g><path d="M0 286 Q300 268 600 288 V320 H0Z" fill="#6E9A55"/></svg>SLOTS</div>',
 'town': '<div class="scene" aria-label="ARIA"><svg class="bg" viewBox="0 0 600 320" aria-hidden="true"><rect width="600" height="320" fill="#BFE0F2"/><g stroke="#5B3F1E" stroke-width="3"><path d="M20 230 V120 L70 80 L120 120 V230Z" fill="#F2E3C6"/><path d="M130 230 V100 L190 60 L250 100 V230Z" fill="#E8D2A8"/><path d="M360 230 V110 L420 70 L480 110 V230Z" fill="#F2E3C6"/><path d="M490 230 V130 L540 90 L590 130 V230Z" fill="#E8D2A8"/></g><g fill="#8A6236"><rect x="60" y="180" width="22" height="50"/><rect x="178" y="170" width="24" height="60"/><rect x="408" y="176" width="24" height="54"/><rect x="528" y="184" width="22" height="46"/></g><path d="M0 230 H600 V320 H0Z" fill="#C9B48A"/><path d="M0 250 H600" stroke="#B39A6E" stroke-width="2" stroke-dasharray="14 10"/></svg>SLOTS</div>',
 'castle': '<div class="scene" aria-label="ARIA"><svg class="bg" viewBox="0 0 600 320" aria-hidden="true"><rect width="600" height="320" fill="#C6E2F5"/><g fill="#B9B3A6" stroke="#6E675C" stroke-width="3"><path d="M150 230 V110 H450 V230Z"/><path d="M120 230 V70 H190 V230Z"/><path d="M410 230 V70 H480 V230Z"/></g><g fill="#B9B3A6" stroke="#6E675C" stroke-width="3"><path d="M120 70 V54 H134 V70 M148 70 V54 H162 V70 M176 70 V54 H190 V70"/><path d="M410 70 V54 H424 V70 M438 70 V54 H452 V70 M466 70 V54 H480 V70"/></g><path d="M270 230 V170 Q300 140 330 170 V230Z" fill="#5B3F1E"/><path d="M300 110 V60" stroke="#5B3F1E" stroke-width="3"/><path d="M300 60 L336 70 L300 80Z" fill="#B5472B"/><path d="M0 230 Q300 214 600 230 V320 H0Z" fill="#5E8C49"/></svg>SLOTS</div>',
 'hut-day': '<div class="scene" aria-label="ARIA"><svg class="bg" viewBox="0 0 600 320" aria-hidden="true"><rect width="600" height="320" fill="#BFD9E8"/><path d="M0 240 Q150 222 300 236 T600 232 V320 H0Z" fill="#4E7A3E"/><g fill="#2F5A2C"><path d="M10 250 L50 90 L90 250Z"/><path d="M70 252 L104 120 L138 252Z"/><path d="M480 250 L520 96 L560 250Z"/><path d="M540 252 L572 130 L600 252Z"/></g><path d="M200 170 L300 100 L400 170Z" fill="#C9A66B" stroke="#7A5428" stroke-width="3"/><path d="M220 166 H380 V262 H220Z" fill="#8A6236" stroke="#5B3F1E" stroke-width="3"/><path d="M286 200 H318 V262 H286Z" fill="#3B2A14"/><path d="M220 196 H380 M220 230 H380" stroke="#6E4E22" stroke-width="2"/><path d="M0 284 Q300 266 600 286 V320 H0Z" fill="#5E8C49"/></svg>SLOTS</div>'}
def scene_html(sc):
    if not sc: return SCENES['night-forest']
    slots = ''.join('<div class="slot" id="slot-%s" style="left:%s;top:%s">%s</div>' % (s['id'], s['left'], s['top'], e(s.get('label', ''))) for s in sc['slots'])
    return SCENES[sc['bg']].replace('ARIA', e(sc['aria'])).replace('SLOTS', slots)
TRANSCRIPTS = {'brief': D['brief'], 'mapday': M['intro'], 'extra': plain(D['extra']['text'])}
for s in D['steps']:
    TRANSCRIPTS[s['say']] = s['_spoken']

page = open(os.path.join(os.path.dirname(__file__), 'template.html'), encoding='utf-8').read()
REPL = {
 '{{TITLE}}': e(D['title']), '{{CANVAS}}': e(CANVAS), '{{WEEK}}': str(W), '{{BOOK}}': e(D['book']), '{{CHAPTERS}}': e(D['chapters']),
 '{{MAP}}': e(D['map']), '{{BRIEF}}': e(D['brief']), '{{LOOK}}': e(D['look']),
 '{{JOB}}': ('<b>1</b> Build the scene in VR → <b>2</b> Take a photo → <b>3</b> Submit it to Canvas' if D['pattern'] == 'A'
             else '<b>1</b> Find the place in VR → <b>2</b> Take a photo → <b>3</b> Submit it to Canvas'),
 '{{STEPS}}': steps_html, '{{EXTRA}}': md(D['extra']['text']), '{{EXTRA_ICON}}': ICONS.get(D['extra'].get('icon', 'frog'), ''), '{{POINTS}}': e(D['points']),
 '{{SCENE}}': scene_html(M.get('scene')), '{{VR_SUB}}': 'Build it in VR.' if D['pattern'] == 'A' else 'Find it in VR.',
 '{{STAMP_VR}}': stamp_svg('#B8860B', D['stamp']['name'], D['stamp'].get('art', 'horseshoe')), '{{STAMP_MAP}}': stamp_svg('#1E3A78', 'Road Map Day'),
 '{{MAP_INTRO}}': e(M['intro']), '{{CHOICES}}': choice_html, '{{FRAMES}}': frames_html, '{{MINW}}': str(M['minWords']),
 '{{DATA}}': json.dumps({'week': W, 'canvas': CANVAS, 'clues': M['clues'], 'icons': {k: ICONS[k] for k in M['choices']},
                          'names': NAMES, 'minWords': M['minWords'], 'title': D['title'], 'transcripts': TRANSCRIPTS,
                          'repeat': bool(M.get('repeat')), 'right': M.get('right', ''), 'miss': M.get('miss', ''), 'done': M.get('done', '')},
                         ensure_ascii=False).replace('</', '<\\/'),
}
for k, v in REPL.items():
    page = page.replace(k, v)
assert '{{' not in page, re.findall(r'\{\{\w+\}\}', page)
out = os.path.join(ROOT, 'vr-%d.html' % W)
open(out, 'w', encoding='utf-8').write(page)
json.dump(TRANSCRIPTS, open(os.path.join(os.path.dirname(__file__), 'week%d-scripts.json' % W), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('wrote', out)
