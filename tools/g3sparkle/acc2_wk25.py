"""Week 25 accuracy, finding 21 (found during the plain pass, Nov 14 2026): the 25.1 Spelling sort columns are swapped.
"Schwa spelled with a" drops into schwa_eo and "Schwa spelled with e or o" into schwa_a, so every right answer is marked wrong.
Re-keys each column to its header. Words and headers unchanged."""
import sys
F = 'lesson-25-1-lww.html'
OLD = [('Schwa spelled with a</div><div class="sort-col-drop" data-col="schwa_eo" onclick="dropSortChip(this,\'schwa_eo\')">',
        'Schwa spelled with a</div><div class="sort-col-drop" data-col="schwa_a" onclick="dropSortChip(this,\'schwa_a\')">'),
       ('Schwa spelled with e or o</div><div class="sort-col-drop" data-col="schwa_a" onclick="dropSortChip(this,\'schwa_a\')">',
        'Schwa spelled with e or o</div><div class="sort-col-drop" data-col="schwa_eo" onclick="dropSortChip(this,\'schwa_eo\')">')]
d = sys.argv[sys.argv.index('--dir') + 1] + '/' if '--dir' in sys.argv else ''
s = open(d + F, encoding='utf-8', newline='').read()
for a, b in OLD:
    assert s.count(a) == 1, a[:60]; s = s.replace(a, b)
if '--apply' in sys.argv: open(d + F, 'w', encoding='utf-8', newline='').write(s)
print('ok' if '--apply' in sys.argv else 'dry-ok', F)
