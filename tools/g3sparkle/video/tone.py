"""Silent-week timing track (Bethany, Nov 14 2026: no recordings yet). Writes /tmp/vid/<clip>.mp3 as an ESTIMATE of how
Opti would say the script: a soft tone for speech at ~15 characters a second, silence at punctuation
(0.55 s after . ? !, 0.3 s after , : ;). timeline.py reads its pauses; the film itself is encoded with a SILENT track.
    python tone.py scripts.json"""
import json, re, subprocess, sys, os
CPS = 15.0
S = json.load(open(sys.argv[1]))
os.makedirs('/tmp/vid', exist_ok=True)
for k, t in S.items():
    t = re.sub(r'\[[^\]]*\]\s*', '', t)
    parts = re.findall(r'[^.?!,:;]+[.?!,:;]?', t)
    segs = []
    for p in parts:
        p = p.strip()
        if not p: continue
        segs.append(('tone', max(0.35, len(p) / CPS)))
        segs.append(('sil', 0.55 if p[-1] in '.?!' else 0.3))
    if segs and segs[-1][0] == 'sil': segs[-1] = ('sil', 0.6)
    inputs, fl = [], []
    for i, (kind, d) in enumerate(segs):
        src = 'sine=frequency=220:sample_rate=44100:duration=%.2f' % d if kind == 'tone' else 'anullsrc=r=44100:cl=mono:d=%.2f' % d
        inputs += ['-f', 'lavfi', '-i', src]
    n = len(segs)
    filt = ''.join('[%d:a]aformat=channel_layouts=mono,volume=%s[a%d];' % (i, '0.3' if segs[i][0] == 'tone' else '1', i) for i in range(n)) + \
           ''.join('[a%d]' % i for i in range(n)) + 'concat=n=%d:v=0:a=1' % n
    subprocess.run(['ffmpeg', '-y', '-hide_banner', '-loglevel', 'error'] + inputs + ['-filter_complex', filt, '-c:a', 'libmp3lame', '-b:a', '64k', '/tmp/vid/%s.mp3' % k], check=True)
    print(k, round(sum(d for _, d in segs), 1), 's')
