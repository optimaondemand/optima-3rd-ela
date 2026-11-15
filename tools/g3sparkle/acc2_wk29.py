"""Week 29 accuracy, second pass (found during the plain pass, Nov 15 2026; flagged for Bethany in the preview):
30. 29.1 spelling sort: the 'Root: ject' column accepted script words and vice versa, and a third 'Script' column
    split script/scribe -> two columns, ject and script/scribe (describe joins script/scribe).
31. 29.1 grammar Rule note still described the old 'Mr Tumnus' sentence -> describes "Let him approach," said Aslan.
Run once after acc_wk29.py:  python tools/g3sparkle/acc2_wk29.py [--apply]"""
import sys
f = 'lesson-29-1-lww.html'
s = open(f, encoding='utf-8', newline='').read(); o = s.count('<div') - s.count('</div')
R = [('<span class="sort-chip" data-group="scribe" onclick="pickSortChip(this)">describe</span>', '<span class="sort-chip" data-group="script" onclick="pickSortChip(this)">describe</span>'),
 ('Root: ject (throw)</div><div class="sort-col-drop" data-col="scribe" onclick="dropSortChip(this,\'scribe\')">', 'Root: ject (throw)</div><div class="sort-col-drop" data-col="ject" onclick="dropSortChip(this,\'ject\')">'),
 ('Root: script/scribe (write)</div><div class="sort-col-drop" data-col="ject" onclick="dropSortChip(this,\'ject\')">', 'Root: script/scribe (write)</div><div class="sort-col-drop" data-col="script" onclick="dropSortChip(this,\'script\')">'),
 ('\n          \n          <div class="sort-col"><div class="sort-col-header" style="background:linear-gradient(135deg,#C7922C,#C7922C);">Script</div><div class="sort-col-drop" data-col="script" onclick="dropSortChip(this,\'script\')"></div></div>', ''),
 ('Opening quotation mark before Mr; capital M; comma inside the closing quotation mark; the dialogue tag said Lucy follows outside with a period.',
  'Opening quotation mark before Let; capital L; comma inside the closing quotation mark; the dialogue tag said Aslan follows outside with a period.')]
for a, b in R:
    assert s.count(a) == 1, a[:80]; s = s.replace(a, b)
assert s.count('<div') - s.count('</div') == o
if '--apply' in sys.argv: open(f, 'w', encoding='utf-8', newline='').write(s)
print('ok' if '--apply' in sys.argv else 'dry-ok', f)
