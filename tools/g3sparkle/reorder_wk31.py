"""Week 31 Reading tab, made clear for a 3rd grader (Bethany, Nov 16 2026: "very convoluted ... not clear which step is
where"). The texts were separate boxes AFTER the Read box, so the layer's Courage Watch ("After you read") came before
the text. Now the text(s) sit INSIDE the Read box, today's text first (Day 2: Text 2, then Text 1 folded), so the order
is: World Notes -> Read box (lens, what to look for, the text) -> Courage Watch -> Q1-Q3 -> Read Like a Writer.
Also: the "Reading-Writing-Meaning Connection" box (jargon) goes, and the Read box's note no longer repeats the What to do
line. Run once: python tools/g3sparkle/reorder_wk31.py"""
import io, re
ASK = {1: 'As you read, ask yourself: What does this author say courage is? What examples does the author give?',
       2: 'As you read, ask yourself: How does the author show that Mira is brave, without using the word brave? How does that fit what Text 1 said?',
       3: 'Look for one detail in each text that you can use in your comparison. Tap Read Text 1 again to see Text 1.',
       4: 'Look for your strongest detail for your closing. Tap Read Text 1 again to see Text 1.'}
KC = '\n      <div class="key-concept"><div class="key-concept-label">🌟 Reading–Writing–Meaning Connection</div><p>Compare/contrast language shows how two texts connect.</p></div>'
CALL = re.compile(r'(<div class="callout callout-info"><span class="callout-icon">📖</span><p style="white-space:pre-line;">)(.*?)(</p></div>)', re.S)
TXT = re.compile(r'<div class="activity" style="(border-left:5px solid #(1B7A4E|8B6FC0);[^"]*)">\n(.*?)\n</div>\n', re.S)
END = '\n    </div>\n  </div>\n  \n'
for d in (1, 2, 3, 4):
    f = 'lesson-31-%d-ext.html' % d
    s = io.open(f, encoding='utf-8', newline='').read()
    assert 'g3-text-in' not in s, f
    o = s.count('<div') - s.count('</div')
    assert s.count(KC) == 1, f; s = s.replace(KC, '')
    i = s.index('activity-title">📖 ')
    m = CALL.search(s, i); s = s[:m.start(2)] + ASK[d] + s[m.end(2):]
    e = s.index(END, i)
    blocks = []; j = e + len(END)
    while True:
        t = TXT.match(s, j)
        if not t: break
        blocks.append((t.group(2), t.group(1), t.group(3))); j = t.end()
    assert len(blocks) == (1 if d == 1 else 2), (f, len(blocks))
    if d > 1: blocks.sort(key=lambda b: 0 if b[0] == '8B6FC0' else 1)   # today's/open text (Text 2) first, Text 1 (folded) after
    inner = ''.join('\n      <div class="g3-text-in" style="%s;margin-top:14px;">\n%s\n      </div>' % (b[1].replace('margin-bottom:18px;', ''), b[2]) for b in blocks)
    s = s[:e] + inner + s[e:e + len(END)] + s[j:]
    assert s.count('<div') - s.count('</div') == o, f
    io.open(f, 'w', encoding='utf-8', newline='').write(s); print('ok', f, [b[0] for b in blocks])
