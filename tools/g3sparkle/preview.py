#!/usr/bin/env python3
"""Inline build of a sparkled lesson for Bethany to open from the chat:
layer, art and any audio embedded. Never committed to the repo."""
import sys, re, base64, os, io
repo, lesson, out = sys.argv[1:4]
h = io.open(os.path.join(repo, lesson), encoding='utf-8').read()
js = io.open(os.path.join(repo, 'g3-sparkle.js'), encoding='utf-8').read()
css = io.open(os.path.join(repo, 'g3-sparkle.css'), encoding='utf-8').read()
def uri(rel):
    p = os.path.join(repo, 'assets', rel)
    if not os.path.exists(p): return None
    ext = os.path.splitext(p)[1].lower()
    mt = {'.png':'image/png','.jpg':'image/jpeg','.jpeg':'image/jpeg','.mp3':'audio/mpeg','.svg':'image/svg+xml'}[ext]
    return 'data:%s;base64,%s' % (mt, base64.b64encode(open(p,'rb').read()).decode())
for rel in set(re.findall(r'(?:art|companions)/[\w./-]+\.(?:jpg|png)', h + js)):
    u = uri(rel)
    if u: h = h.replace('"' + rel + '"', '"' + u + '"'); js = js.replace("'" + rel + "'", "'" + u + "'")
# audio: embed every clip that exists, keyed by its path, and let Audio() find it
audio = {}
import json as _j
m = re.search(r'id="oao-lesson">\s*(\{.*?\})', h, re.S)
decl = _j.loads(m.group(1)) if m else {}
md = re.search(r'id="oao-data">\s*(\{.*?\})\s*</script>', h, re.S)
data = _j.loads(md.group(1)) if md else {}
want_words = set(re.sub(r"[^a-z0-9]+", "-", w.lower()).strip('-') for w in data.get('sayWords', []))
pref = 'g3ela-%s-%s-' % (decl.get('week'), decl.get('day'))
def wanted(rel):
    b = os.path.basename(rel)
    if b.startswith(pref) or b.startswith('g3ela-how-'): return True
    if b.startswith('g3ela-word-'): return b[11:-4] in want_words
    return False
adir = os.path.join(repo, 'assets', 'audio')
for root, _, files in os.walk(adir):
    for f in files:
        if f.endswith('.mp3') and wanted(f):
            rel = os.path.relpath(os.path.join(root, f), os.path.join(repo)).replace(os.sep, '/')
            audio[rel] = uri(os.path.relpath(os.path.join(root, f), os.path.join(repo, 'assets')))
shim = ''
if audio:
    import json
    shim = '<script>(function(){var M=%s;var A=window.Audio;window.Audio=function(s){var a=new A();if(s)a.src=M[s]||s;var d=Object.getOwnPropertyDescriptor(HTMLMediaElement.prototype,"src");Object.defineProperty(a,"src",{set:function(v){d.set.call(a,M[v]||v)},get:function(){return d.get.call(a)}});return a;};})();</script>\n' % json.dumps(audio)
h = h.replace('<link rel="stylesheet" href="g3-sparkle.css">', '<style>\n' + css + '\n</style>')
h = h.replace('<script src="g3-sparkle.js" defer></script>', shim + '<script>\n' + js.replace('</script', '<\\/script') + '\n</script>')
io.open(out, 'w', encoding='utf-8').write(h)
print(out, os.path.getsize(out), 'audio clips:', len(audio))
