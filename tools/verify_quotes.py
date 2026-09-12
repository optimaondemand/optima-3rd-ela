#!/usr/bin/env python3
"""Check passages quoted in OAO lesson HTML against a novel's OCR text.

Why fuzzy and not exact: the novel OCR carries character-level noise, so REAL
quotes fail an exact substring test. ("Light is precious in a world so dark"
OCRs as "light ts precious ina world so dark.")  Observed score bands:
  >= 0.85  real
  0.70-.85 real but noisy -- inspect, never auto-reject
  <  0.70  fabricated (genuine quotes never scored this low; fabrications
           topped out at 0.62)

usage: verify_quotes.py <novel_ocr.txt> <lesson-glob> [more globs...]
"""
import re,io,sys,glob,html,difflib
from collections import defaultdict

QUOTE_CLASSES = ['decode-sentence','copywork-text','copy-sentence','quote-strip-text']
# quote-strip-text is the header banner quote. It was left out of this list until
# 2026-09-12, so the first clean-sweep never checked it -- 29 of 36 Despereaux banner
# quotes were invented aphorisms credited to DiCamillo. Note the [^>]* in the regex
# below matters here: LWW and W31-32 put inline styles on that div.
# Banner quotes are often short (<6 words); those score 0.70-0.83 even when verbatim,
# so grep the novel text before calling one fabricated.

def norm(x, strip_tags=True):
    """strip_tags=True for lesson HTML fragments. MUST be False for the novel:
    the OCR contains stray '<' and '>' characters (e.g. "Chapter Twenty-seven <__"),
    and a tag-stripping regex silently deletes everything between them -- which
    makes real quotes look fabricated."""
    x = html.unescape(x)
    for a,b in [('’',"'"),('‘',"'"),('“','"'),('”','"'),('—',' '),('–',' ')]:
        x = x.replace(a,b)
    if strip_tags:
        x = re.sub(r'<[^>]+>',' ',x)
    x = x.lower()
    x = re.sub(r"[^a-z' ]",' ',x)
    return re.sub(r'\s+',' ',x).strip()

def load(novel):
    t = io.open(novel,encoding='utf-8',errors='replace').read()
    t = '\n'.join(l for l in t.split('\n') if not l.startswith('===HALF') and not l.startswith('===PAGE'))
    return norm(t.replace('- ',''), strip_tags=False).split()

def scorer(words):
    pos = defaultdict(list)
    for i,w in enumerate(words): pos[w].append(i)
    def best(q):
        qw = q.split()
        if not qw: return 0.0,''
        n = len(qw)
        # rarest words first; align each candidate occurrence so the anchor lands
        # at the same index it occupies inside the quote, then jitter a little.
        order = sorted(range(n), key=lambda i: len(pos.get(qw[i],[])) or 10**9)
        top = 0.0; seg = ''
        tried = set()
        for qi in order[:8]:
            for c in pos.get(qw[qi],[])[:600]:
                for jit in (0,-2,2,-5,5):
                    st = c - qi + jit
                    if st < 0 or st in tried: continue
                    tried.add(st)
                    w = ' '.join(words[st:st+n+4])
                    r = difflib.SequenceMatcher(None,q,w).ratio()
                    if r > top: top,seg = r,w
                    if top > 0.97: return top,seg
        return top,seg
    return best

def main():
    words = load(sys.argv[1])
    best = scorer(words)
    files = []
    for g in sys.argv[2:]: files += sorted(glob.glob(g))
    seen = {}
    where = defaultdict(list)
    for f in files:
        s = io.open(f,encoding='utf-8',errors='replace').read()
        for cls in QUOTE_CLASSES:
            for m in re.finditer(r'<div class="%s"[^>]*>(.*?)</div>'%cls, s, re.S):
                q = norm(m.group(1))
                if len(q) < 25: continue
                where[q].append((f,cls))
                if q not in seen: seen[q] = best(q)
    counts = {'real':0,'noisy':0,'fabricated':0}
    for q,(r,seg) in sorted(seen.items(), key=lambda kv: kv[1][0]):
        tag = 'real' if r>=0.85 else ('noisy' if r>=0.70 else 'fabricated')
        counts[tag]+=1
        print('[%-10s %.2f] %s' % (tag.upper(), r, q[:100]))
        print('   in: %s' % ', '.join(sorted({f for f,_ in where[q]})[:6]))
        if tag != 'real': print('   closest: %s' % seg[:100])
    print('\nunique passages: %d  %s' % (len(seen), counts))

main()
