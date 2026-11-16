"""G3 ELA VR kit v2 (Nov 16 2026, week 19 run): Pattern B (find a place) and other Road Map Day games without breaking week 18.
- week JSON may give `lookfors` (Pattern B) instead of `models`; `stamp.art` ('horseshoe' | 'hut'); `extra.icon`;
  `mapday.scene` = {bg, aria, slots:[{id,left,top}]}; `mapday.repeat` (an answer can be picked more than once);
  `mapday.right` ("✓ Yes! {name} said it."), `mapday.miss`, `mapday.done`.
- template: {{SCENE}}, {{VR_SUB}}, generic game messages.
- playtest: wrong pick + storage key from the week. check: CSV check only for models (Pattern A).
Run once from the repo root: python3 tools/vr/kit2.py"""
import io, os
K = 'tools/vr/'
def edit(p, pairs):
    s = io.open(K + p, encoding='utf-8', newline='').read()
    for a, b in pairs:
        assert s.count(a) == 1, (p, a[:70], s.count(a)); s = s.replace(a, b)
    io.open(K + p, 'w', encoding='utf-8', newline='').write(s); print('ok', p)

ICONS_ADD = r''' 'trees': '<svg viewBox="0 0 64 64"><path d="M8 54 L20 18 L32 54Z" fill="#3E7A45" stroke="#22492A" stroke-width="2" stroke-linejoin="round"/><path d="M26 54 L40 10 L54 54Z" fill="#2F6A3A" stroke="#22492A" stroke-width="2" stroke-linejoin="round"/><path d="M18 54 H24 V60 H18Z M37 54 H43 V60 H37Z" fill="#6E4E22"/></svg>',
 'nopath': '<svg viewBox="0 0 64 64"><path d="M22 60 Q30 40 26 20 Q24 10 32 4 M42 60 Q46 40 40 20 Q38 10 40 4" stroke="#B88A55" stroke-width="5" fill="none"/><circle cx="32" cy="32" r="24" fill="none" stroke="#C0545C" stroke-width="5"/><path d="M15 15 L49 49" stroke="#C0545C" stroke-width="5"/></svg>',
 'hut': '<svg viewBox="0 0 64 64"><path d="M8 32 L32 12 L56 32Z" fill="#C9A66B" stroke="#7A5428" stroke-width="2" stroke-linejoin="round"/><path d="M14 30 H50 V56 H14Z" fill="#8A6236" stroke="#5B3F1E" stroke-width="2"/><path d="M28 40 H38 V56 H28Z" fill="#3B2A14"/><path d="M14 38 H50 M14 46 H50" stroke="#6E4E22" stroke-width="1.5"/></svg>',
 'shade': '<svg viewBox="0 0 64 64"><path d="M6 30 Q32 2 58 30Z" fill="#2F6A3A" stroke="#22492A" stroke-width="2"/><path d="M30 30 H34 V58 H30Z" fill="#6E4E22"/><ellipse cx="32" cy="58" rx="22" ry="4" fill="#1E3324" opacity=".5"/></svg>',
 'billy': '<svg viewBox="0 0 64 64"><circle cx="32" cy="30" r="16" fill="#E8C29A" stroke="#7A5428" stroke-width="2"/><path d="M16 28 Q18 10 32 10 Q46 10 48 28 Q44 18 32 18 Q20 18 16 28Z" fill="#B5472B"/><path d="M18 34 Q20 52 32 54 Q44 52 46 34 Q40 44 32 44 Q24 44 18 34Z" fill="#B5472B"/><circle cx="26" cy="28" r="2" fill="#3B2A14"/><circle cx="38" cy="28" r="2" fill="#3B2A14"/></svg>',
 'cutwater': '<svg viewBox="0 0 64 64"><ellipse cx="32" cy="32" rx="11" ry="18" fill="#E8C29A" stroke="#7A5428" stroke-width="2"/><path d="M21 22 Q32 6 43 22" fill="#4A3A2A"/><circle cx="28" cy="28" r="1.8" fill="#3B2A14"/><circle cx="36" cy="28" r="1.8" fill="#3B2A14"/><path d="M28 42 H36" stroke="#7A5428" stroke-width="2"/></svg>',
 'jemmy': '<svg viewBox="0 0 64 64"><circle cx="32" cy="34" r="15" fill="#F1D3B3" stroke="#7A5428" stroke-width="2"/><path d="M17 30 Q20 14 32 14 Q44 14 47 30 Q42 22 34 24 Q26 20 17 30Z" fill="#6E4E22"/><circle cx="27" cy="33" r="1.8" fill="#3B2A14"/><circle cx="37" cy="33" r="1.8" fill="#3B2A14"/><path d="M27 41 Q32 44 37 41" stroke="#7A5428" stroke-width="2" fill="none"/></svg>',
 'prince': '<svg viewBox="0 0 64 64"><circle cx="32" cy="36" r="14" fill="#F4DCC2" stroke="#7A5428" stroke-width="2"/><path d="M18 22 L22 10 L28 18 L32 8 L36 18 L42 10 L46 22Z" fill="#E0B23A" stroke="#7A5A10" stroke-width="2" stroke-linejoin="round"/><circle cx="27" cy="35" r="1.8" fill="#3B2A14"/><circle cx="37" cy="35" r="1.8" fill="#3B2A14"/><path d="M27 44 Q32 41 37 44" stroke="#7A5428" stroke-width="2" fill="none"/></svg>'
}'''
NAMES_OLD = "NAMES = {'horse': 'a horse', 'basket': 'a basket', 'cloak': 'a cloak', 'moon': 'the moon', 'sword': 'a sword', 'dog': 'a dog', 'frog': 'a frog'}"
NAMES_NEW = NAMES_OLD + "\nNAMES.update({'trees': 'thick trees', 'nopath': 'no path', 'hut': 'a hut', 'shade': 'deep shade', 'billy': 'a Hold-Your-Nose Billy', 'cutwater': 'a Cutwater', 'jemmy': 'a Jemmy', 'prince': 'a Prince Brat'})\nNAMES.update(D.get('mapday', {}).get('names', {}))"
STAMP_OLD = """def stamp_svg(ink, label):"""
STAMP_NEW = """ART = {'horseshoe': '<path d="M53 90 Q46 54 70 46 Q94 54 87 90 L78 90 Q83 62 70 59 Q57 62 62 90 Z" fill="%s"/><circle cx="55" cy="67" r="2.2" fill="#fff"/><circle cx="59" cy="81" r="2.2" fill="#fff"/><circle cx="85" cy="67" r="2.2" fill="#fff"/><circle cx="81" cy="81" r="2.2" fill="#fff"/>',
       'hut': '<path d="M46 70 L70 48 L94 70 Z" fill="%s"/><path d="M52 68 H88 V92 H52 Z" fill="%s"/><path d="M65 78 H75 V92 H65 Z" fill="#fff"/>'}
def stamp_svg(ink, label, art='horseshoe'):"""
STAMP_BODY_OLD = """'<path d="M53 90 Q46 54 70 46 Q94 54 87 90 L78 90 Q83 62 70 59 Q57 62 62 90 Z" fill="%s"/>'
            '<circle cx="55" cy="67" r="2.2" fill="#fff"/><circle cx="59" cy="81" r="2.2" fill="#fff"/><circle cx="85" cy="67" r="2.2" fill="#fff"/><circle cx="81" cy="81" r="2.2" fill="#fff"/>'
            '<text"""
STAMP_BODY_NEW = """'%s'
            '<text"""
STAMP_ARGS_OLD = """'</svg>') % (uid, uid, ink, ink, ink, ink, uid, W, ink, uid, e(label.upper()))"""
STAMP_ARGS_NEW = """'</svg>') % (uid, uid, ink, ink, ART[art].replace('%s', ink), ink, uid, W, ink, uid, e(label.upper()))"""
MODELS_OLD = """    % (ICONS.get(m['icon'], ''), e(m['name']), ('<small>type: %s</small>' % e(m['type'])) if m['type'] != m['name'] else '', e(m['why'])) for m in D['models'])"""
MODELS_NEW = """    % (ICONS.get(m['icon'], ''), e(m['name']), ('<small>type: %s</small>' % e(m['type'])) if m.get('type', m['name']) != m['name'] else '', e(m['why'])) for m in (D.get('models') or D['lookfors']))"""
SCENE18 = ('<div class="scene" aria-label="A forest at night, waiting for the runaways\' things">\n'
 '      <svg class="bg" viewBox="0 0 600 320" aria-hidden="true"><defs><linearGradient id="sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#12204A"/><stop offset="1" stop-color="#2E4470"/></linearGradient></defs>\n'
 '        <rect width="600" height="320" fill="url(#sky)"/><g fill="#fff" opacity=".7"><circle cx="60" cy="40" r="1.4"/><circle cx="160" cy="22" r="1.2"/><circle cx="250" cy="60" r="1.1"/><circle cx="330" cy="30" r="1.4"/><circle cx="560" cy="70" r="1.2"/></g>\n'
 '        <path d="M0 250 Q150 230 300 248 T600 244 V320 H0Z" fill="#1E3324"/>\n'
 '        <g fill="#16291C"><path d="M20 260 L60 120 L100 260Z"/><path d="M80 262 L118 150 L156 262Z"/><path d="M470 258 L512 130 L554 258Z"/><path d="M530 262 L566 160 L600 262Z"/><path d="M380 256 L410 170 L440 256Z"/></g>\n'
 '        <path d="M0 290 Q300 270 600 292 V320 H0Z" fill="#284430"/>\n'
 '      </svg>\n'
 '      <div class="slot" id="slot-moon" style="left:66%;top:6%">moon</div>\n'
 '      <div class="slot" id="slot-horse" style="left:30%;top:52%">horse</div>\n'
 '      <div class="slot" id="slot-basket" style="left:48%;top:62%">basket</div>\n'
 '      <div class="slot" id="slot-cloak" style="left:14%;top:60%">cloak</div>\n'
 '    </div>')
BUILD_SCENE = '''
SCENES = {'night-forest': SCENE18_REPR,
 'hut-day': '<div class="scene" aria-label="ARIA"><svg class="bg" viewBox="0 0 600 320" aria-hidden="true"><rect width="600" height="320" fill="#BFD9E8"/><path d="M0 240 Q150 222 300 236 T600 232 V320 H0Z" fill="#4E7A3E"/><g fill="#2F5A2C"><path d="M10 250 L50 90 L90 250Z"/><path d="M70 252 L104 120 L138 252Z"/><path d="M480 250 L520 96 L560 250Z"/><path d="M540 252 L572 130 L600 252Z"/></g><path d="M200 170 L300 100 L400 170Z" fill="#C9A66B" stroke="#7A5428" stroke-width="3"/><path d="M220 166 H380 V262 H220Z" fill="#8A6236" stroke="#5B3F1E" stroke-width="3"/><path d="M286 200 H318 V262 H286Z" fill="#3B2A14"/><path d="M220 196 H380 M220 230 H380" stroke="#6E4E22" stroke-width="2"/><path d="M0 284 Q300 266 600 286 V320 H0Z" fill="#5E8C49"/></svg>SLOTS</div>'}
def scene_html(sc):
    if not sc: return SCENES['night-forest']
    slots = ''.join('<div class="slot" id="slot-%s" style="left:%s;top:%s">%s</div>' % (s['id'], s['left'], s['top'], e(s.get('label', ''))) for s in sc['slots'])
    return SCENES[sc['bg']].replace('ARIA', e(sc['aria'])).replace('SLOTS', slots)
'''.replace('SCENE18_REPR', repr(SCENE18))
REPL_OLD = " '{{STEPS}}': steps_html, '{{EXTRA}}': md(D['extra']['text']), '{{EXTRA_ICON}}': ICONS.get('frog', ''), '{{POINTS}}': e(D['points']),"
REPL_NEW = (" '{{STEPS}}': steps_html, '{{EXTRA}}': md(D['extra']['text']), '{{EXTRA_ICON}}': ICONS.get(D['extra'].get('icon', 'frog'), ''), '{{POINTS}}': e(D['points']),\n"
            " '{{SCENE}}': scene_html(M.get('scene')), '{{VR_SUB}}': 'Build it in VR.' if D['pattern'] == 'A' else 'Find it in VR.',")
STAMP_CALL_OLD = "'{{STAMP_VR}}': stamp_svg('#B8860B', D['stamp']['name']),"
STAMP_CALL_NEW = "'{{STAMP_VR}}': stamp_svg('#B8860B', D['stamp']['name'], D['stamp'].get('art', 'horseshoe')),"
DATA_OLD = "'names': NAMES, 'minWords': M['minWords'], 'title': D['title'], 'transcripts': TRANSCRIPTS},"
DATA_NEW = ("'names': NAMES, 'minWords': M['minWords'], 'title': D['title'], 'transcripts': TRANSCRIPTS,\n"
            "                          'repeat': bool(M.get('repeat')), 'right': M.get('right', ''), 'miss': M.get('miss', ''), 'done': M.get('done', '')},")
FRAMES_ANCHOR = "TRANSCRIPTS = {'brief'"
# put the new icons inside ICONS: replace the closing of the frog line
s = io.open(K + 'build_vr.py', encoding='utf-8').read()
frog_end = "fill=\"#111\"/></svg>'\n}"
assert s.count(frog_end) == 1
s = s.replace(frog_end, frog_end.replace("\n}", ",\n" + ICONS_ADD))
io.open(K + 'build_vr.py', 'w', encoding='utf-8').write(s)
edit('build_vr.py', [(NAMES_OLD, NAMES_NEW), (STAMP_OLD, STAMP_NEW), (STAMP_BODY_OLD, STAMP_BODY_NEW), (STAMP_ARGS_OLD, STAMP_ARGS_NEW),
                     (MODELS_OLD, MODELS_NEW), (FRAMES_ANCHOR, BUILD_SCENE + FRAMES_ANCHOR), (REPL_OLD, REPL_NEW), (STAMP_CALL_OLD, STAMP_CALL_NEW), (DATA_OLD, DATA_NEW)])
edit('template.html', [
 (SCENE18, '{{SCENE}}'),
 ('<small>Build it in VR.</small>', '<small>{{VR_SUB}}</small>'),
 ("$$('.obj').forEach(function(b){ b.disabled=S.placed.indexOf(b.getAttribute('data-o'))>=0; });",
  "$$('.obj').forEach(function(b){ b.disabled=!V.repeat&&S.placed.indexOf(b.getAttribute('data-o'))>=0; });"),
 ("$('#mfb').textContent='✓ The scene is ready. Now finish the two sentences.';",
  "$('#mfb').textContent=V.done||'✓ The scene is ready. Now finish the two sentences.';"),
 ("$('#mfb').textContent='✓ Yes! '+V.names[o].charAt(0).toUpperCase()+V.names[o].slice(1)+'.';",
  "$('#mfb').textContent=V.right?V.right.replace('{name}',V.names[o].replace(/^an? /,'')):'✓ Yes! '+V.names[o].charAt(0).toUpperCase()+V.names[o].slice(1)+'.';"),
 ("$('#mfb').textContent='Not that one. Read the clue again and look for the thing it names.';",
  "$('#mfb').textContent=V.miss||'Not that one. Read the clue again and look for the thing it names.';"),
 ("'<p class=\"k\">The scene: '+S.placed.map(function(o){return esc(V.names[o]);}).join(', ')+'</p>'+",
  "(V.repeat?'':'<p class=\"k\">The scene: '+S.placed.map(function(o){return esc(V.names[o]);}).join(', ')+'</p>')+"),
])
edit('playtest_vr.js', [
 ("await pg.click('.obj[data-o=\"sword\"]');",
  "const wrong = await pg.evaluate(() => [...document.querySelectorAll('.obj')].map(b => b.dataset.o).find(o => o !== VR.clues[0].a));\n    await pg.click(`.obj[data-o=\"${wrong}\"]`);"),
 ("ok((await pg.textContent('#mfb')).startsWith('Not that one'), `${width}: wrong-pick message missing`);",
  "ok(/^Not /.test(await pg.textContent('#mfb')), `${width}: wrong-pick message missing`);"),
 ("ok((await pg.evaluate(() => localStorage.getItem('oao.g3ela.vr.18'))) === 'vr', `${width}: vr key not saved`);",
  "ok((await pg.evaluate(w => localStorage.getItem('oao.g3ela.vr.' + w), W)) === 'vr', `${width}: vr key not saved`);"),
 ("ok((await pg.evaluate(() => localStorage.getItem('oao.g3ela.vr.18'))) === 'map', `${width}: map key not saved`);",
  "ok((await pg.evaluate(w => localStorage.getItem('oao.g3ela.vr.' + w), W)) === 'map', `${width}: map key not saved`);"),
])
edit('check_vr.py', [
 ("for m in D['models']:\n    if m['name'] not in names: errs.append('model not in CSV: ' + m['name'])",
  "for m in D.get('models', []):\n    if m['name'] not in names: errs.append('model not in CSV: ' + m['name'])"),
 ("if not 4 <= len(D['models']) <= 6: errs.append('need 4-6 models, have %d' % len(D['models']))",
  "if D['pattern'] == 'A' and not 4 <= len(D['models']) <= 6: errs.append('need 4-6 models, have %d' % len(D['models']))\nif D['pattern'] == 'B' and not 3 <= len(D.get('lookfors', [])) <= 6: errs.append('Pattern B needs 3-6 look-fors')"),
])
