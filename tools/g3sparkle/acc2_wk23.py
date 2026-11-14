"""Week 23 accuracy, finding 21 (Nov 14 2026): every Vocabulary Quick Match paired each word with the
wrong meaning (data-match letters followed the screen order, not the meanings). This re-keys each
meaning tile to its word. Words and meanings are unchanged."""
import re, sys
KEY = {
 'lesson-23-1-med.html': {"A person who works in another's household, doing domestic tasks.": 'C',
   'A young boy in training at a noble household, learning to become a knight.': 'D',
   'A large, strong building built to resist attack.': 'A',
   'The strongest, innermost tower of a castle where the lord lived.': 'B'},
 'lesson-23-2-med.html': {'A thick soup of vegetables and grains eaten by poor medieval people.': 'C',
   'To decorate fabric with needle and thread; a skill wealthy girls learned.': 'D',
   'A person learning a trade by working under an expert.': 'A',
   'A skilled worker who makes things by hand.': 'B'},
 'lesson-23-3-med.html': {'A person of high social class or birth, below royalty.': 'C',
   'Polite, respectful, and well-mannered — especially to others.': 'D',
   'Official rules for behavior in formal or important situations.': 'A',
   "A person's position or level in a system of power or importance.": 'B'},
 'lesson-23-4-med.html': {'Rough in texture; coarse bread was made from unrefined grain.': 'C',
   'A dull grey metal alloy used to make plates and cups for wealthy households.': 'D',
   'A thick vegetable-and-grain soup that was the main food of poor medieval people.': 'A',
   'A large, elaborate meal — a sign of wealth and celebration.': 'B'},
}
dry = '--apply' not in sys.argv
for f, km in KEY.items():
    p = (sys.argv[sys.argv.index('--dir') + 1] + '/' if '--dir' in sys.argv else '') + f
    s = open(p, encoding='utf-8', newline='').read()
    for text, k in km.items():
        pat = re.compile(r'(<div class="match-item" data-match=")[A-D](" onclick="matchClick\(this\)">)' + re.escape(text.replace("'", "&#x27;")) if False else r'(<div class="match-item" data-match=")[A-D](" onclick="matchClick\(this\)">)' + re.escape(text))
        s, n = pat.subn(r'\g<1>' + k + r'\2' + text.replace('\\', '\\\\'), s)
        assert n == 1, (f, n, text)
    if not dry: open(p, 'w', encoding='utf-8', newline='').write(s)
    print('ok' if not dry else 'dry-ok', p)
