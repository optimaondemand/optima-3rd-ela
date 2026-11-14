"""Week 24 accuracy, finding 1 (Nov 14 2026): every Vocabulary Quick Match paired each word with the wrong meaning
(same bug as week 23). Re-keys each meaning tile to its word. Words and meanings are unchanged."""
import re, sys
KEY = {
 'lesson-24-1-med.html': {'A bridge over a moat': 'C', 'The strongest inner tower': 'D', 'A deep water-filled ditch': 'A', 'A skilled worker who cuts': 'B'},
 'lesson-24-2-med.html': {'Officially made a knight': 'C', 'A mock battle': 'D', 'The medieval code': 'A', 'A young man serving': 'B'},
 'lesson-24-3-med.html': {'The buying and selling': 'C', 'A large, important church': 'D', 'An organized group': 'A', 'A person who buys and sells': 'B'},
 'lesson-24-4-med.html': {'To make something seem better': 'C', 'Information or facts': 'D', 'A person who studies': 'A', 'Correct; true': 'B'},
}
dry = '--apply' not in sys.argv
d = sys.argv[sys.argv.index('--dir') + 1] + '/' if '--dir' in sys.argv else ''
for f, km in KEY.items():
    s = open(d + f, encoding='utf-8', newline='').read()
    for text, k in km.items():
        pat = re.compile(r'(<div class="match-item" data-match=")[A-D](" onclick="matchClick\(this\)">' + re.escape(text) + ')')
        s, n = pat.subn(r'\g<1>' + k + r'\2', s)
        assert n == 1, (f, n, text)
    if not dry: open(d + f, 'w', encoding='utf-8', newline='').write(s)
    print('ok' if not dry else 'dry-ok', f)
