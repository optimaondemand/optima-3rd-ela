"""Week 31: on Days 2-4, Text 1 ("What Is Courage?") folds behind a "Read Text 1 again" button (Bethany, Nov 16 2026:
31.2 ran 39 steps with Text 1 printed beside Text 2). Day 1 keeps Text 1 open. Run once: python tools/g3sparkle/fold_wk31.py"""
import io, re
SUM = ('<details class="g3-reread" style="margin-top:4px;"><summary style="cursor:pointer;font-weight:800;color:#1B7A4E;'
       'padding:8px 12px;border:2px solid #B8E0C8;border-radius:10px;background:#EAF4EE;display:inline-block;">'
       '👆 Read Text 1 again</summary>\n')
PAT = re.compile(r'(Written for Optima Academy Online</div>\n  </div>\n)(  <p style="font-family:Lora,Georgia,serif;[^\n]*</p>)\n(</div>)')
for d in (2, 3, 4):
    f = 'lesson-31-%d-ext.html' % d
    s = io.open(f, encoding='utf-8', newline='').read()
    assert 'g3-reread' not in s, f
    s2, n = PAT.subn(lambda m: m.group(1) + SUM + m.group(2) + '\n</details>\n' + m.group(3), s, count=1)
    assert n == 1, (f, n)
    assert s2.count('<div') - s2.count('</div') == s.count('<div') - s.count('</div')
    io.open(f, 'w', encoding='utf-8', newline='').write(s2); print('ok', f)
