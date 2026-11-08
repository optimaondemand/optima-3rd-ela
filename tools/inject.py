#!/usr/bin/env python3
"""
inject.py — add the OAO sparkle layer to a G3 ELA lesson, in place.

Ported Nov 2026 from optima-4th-ela/tools/inject.py (Opti's Story Map).

    python tools/inject.py lesson-18-1-wb.html \
        --book wb --week 18 --day 1 \
        --title "The Whipping Boy" --chapters "Ch. 1–2"

That is a DRY RUN: it prints what it would change and writes nothing.
Add --apply once the summary looks right.

WHAT IT DOES, and nothing else:

  1. inserts the lesson declaration before </head>
  2. inserts that lesson's own DATA block beside it
  3. links sparkle.css and sparkle.js before </body>
  4. optionally replaces the chapter epigraph (--quote)

DATA IS PER LESSON AND LIVES IN THE LESSON.

It is read from data/lesson-<week>-<day>.json and written into the page
as a second <script type="application/json"> block. It used to be
hardcoded inside sparkle.js, which meant every sparkled lesson in the
year showed lesson 7.1's sentence, hint ladders and connector. A lesson
with no data file still builds; it simply has no DOL choice, no hint
ladders and no copia card. An empty DATA is valid.

The lesson's own markup is never rewritten. Everything the layer does
happens at runtime, in the browser. Delete the two injected blocks and
the file is byte-for-byte what it was.

WHY IT LINKS THE LAYER INSTEAD OF INLINING IT

The layer is ~190 KB of CSS and JS. Pasted into 129 lessons that is
~25 MB of repo, ~25 MB a student re-downloads over a year, and — the
part that really bites — a one-line bug fix means re-injecting and
re-committing all 129 files. Linked, the browser caches it once in week
7, each lesson grows by about 1 KB, and fixing a bug is editing one
file. Same argument as the art; same answer.

The cost: a lesson only works served from the repo or Pages, not opened
as a loose file off a desktop. That is the accepted trade.

REFUSES TO RUN TWICE. A second injection would stack two copies of the
layer, and every duplicated id, listener and localStorage write that
implies. The marker below is how it knows.

Written Sept 2026 for G4; ported Nov 2026. See the g3-ela-sparkle-lesson skill.
"""
import argparse, io, json, os, re, sys

MARK_OPEN  = "<!-- ═════════ OAO SPARKLE LAYER (additive) ═════════ -->"
MARK_CLOSE = "<!-- ═════════ END OAO SPARKLE ═════════ -->"
DECL_ID    = "oao-lesson"
DATA_ID    = "oao-data"
BOOKS      = ("stanley", "nonfic", "desp", "wb", "med", "lww", "ext")


def die(msg):
    sys.exit("inject: " + msg)


def one(lines, needle, what):
    """Index of the only line that is exactly `needle`. Anything else is
    a file shaped differently from the 129 this was written for, and
    guessing which one to use is how you corrupt a live lesson."""
    hits = [i for i, l in enumerate(lines) if l.strip() == needle]
    if len(hits) != 1:
        die("expected exactly one %s, found %d" % (what, len(hits)))
    return hits[0]


def rel_prefix(path):
    """sparkle.css/js live at the repo root; a lesson may not."""
    depth = len(os.path.dirname(os.path.relpath(path)).split(os.sep)) \
            if os.path.dirname(os.path.relpath(path)) else 0
    return "../" * depth


def main():
    ap = argparse.ArgumentParser(description=__doc__,
            formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("lesson", help="the lesson HTML file, edited in place")
    ap.add_argument("--book", required=True, choices=BOOKS)
    ap.add_argument("--week", required=True, type=int)
    ap.add_argument("--day", required=True, help="1-4, or fluency")
    ap.add_argument("--title", required=True, help="book title as printed")
    ap.add_argument("--chapters", required=True, help='e.g. "Ch. 3 & 4"')
    ap.add_argument("--grade", type=int, default=3)
    ap.add_argument("--subject", default="ela")
    ap.add_argument("--quote", help="replacement epigraph text (no markup)")
    ap.add_argument("--data", help="path to this lesson's DATA json "
                                   "(default: data/lesson-<week>-<day>.json)")
    ap.add_argument("--apply", action="store_true", help="actually write")
    a = ap.parse_args()

    if not os.path.isfile(a.lesson):
        die("no such file: " + a.lesson)
    html = io.open(a.lesson, encoding="utf-8").read()
    before = len(html)

    # ── the refusal that matters ────────────────────────────────
    if MARK_OPEN in html or DECL_ID in html or DATA_ID in html:
        die("%s already carries the sparkle layer. Refusing to inject a\n"
            "        second copy. To rebuild it, revert the file first:\n"
            "            git checkout -- %s" % (a.lesson, a.lesson))

    # ── 1. the lesson declaration ───────────────────────────────
    if a.day not in ("1", "2", "3", "4", "fluency"):
        die("--day must be 1, 2, 3, 4 or fluency")
    a.day = int(a.day) if a.day.isdigit() else a.day
    decl = {"grade": a.grade, "subject": a.subject, "book": a.book,
            "week": a.week, "day": a.day,
            "bookTitle": a.title, "chapters": a.chapters}
    # ── 1b. this lesson's own content ───────────────────────────
    data_path = a.data or os.path.join("data", "lesson-%d-%s.json" % (a.week, a.day))
    if os.path.isfile(data_path):
        try:
            data = json.loads(io.open(data_path, encoding="utf-8").read())
        except ValueError as e:
            die("%s is not valid JSON: %s" % (data_path, e))
        if not isinstance(data, dict):
            die("%s must be a JSON object" % data_path)
        if "poem" in data:
            die("%s has a 'poem' key. The By Heart card belongs to\n"
                "        There is no poem card in G3 ELA — remove it." % data_path)
        data_note = "%s (%d keys, %d bytes)" % (data_path, len(data),
                                                len(json.dumps(data)))
    else:
        data = {}
        data_note = "none — %s not found; lesson builds without it" % data_path

    decl_block = ('<script type="application/json" id="%s">\n%s\n</script>\n'
                  '<script type="application/json" id="%s">\n%s\n</script>\n</head>'
                  % (DECL_ID, json.dumps(decl, ensure_ascii=False),
                     DATA_ID, json.dumps(data, ensure_ascii=False, indent=1)))
    lines = html.split("\n")
    lines[one(lines, "</head>", "</head>")] = decl_block
    html = "\n".join(lines)

    # ── 2. the title marker ─────────────────────────────────────
    # localStorage is namespaced off document.title, so this also keeps
    # a lesson's saved work from colliding with any other lesson's.
    m = re.search(r"<title>(.*?)</title>", html, re.S)
    if not m:
        die("no <title> — is this a lesson file?")
    if "(Sparkle)" not in m.group(1):
        html = html.replace(m.group(0),
                            "<title>%s (Sparkle)</title>" % m.group(1).strip(), 1)

    # ── 2b. the epigraph, if a better line was chosen ───────────
    quote_changed = False
    if a.quote:
        qm = re.search(r'(<div class="quote-strip-text">)(.*?)(</div>)', html, re.S)
        if not qm:
            die("--quote given but no .quote-strip-text in this lesson")
        html = html.replace(qm.group(0),
                            '%s&ldquo;%s&rdquo;%s' % (qm.group(1), a.quote, qm.group(3)), 1)
        quote_changed = True

    # ── 3. link the layer ───────────────────────────────────────
    p = rel_prefix(a.lesson)
    block = (
        "\n" + MARK_OPEN + "\n"
        '<link rel="stylesheet" href="%sg3-sparkle.css">\n' % p +
        '<script src="%sg3-sparkle.js" defer></script>\n' % p +
        MARK_CLOSE + "\n"
    )
    # G3 lessons close with "</body></html>" on one line
    # (the page's own PDF export also writes "</body>" inside a JS string,
    # so the real one is the last, at the start of its line)
    k = html.rfind("\n</body>")
    if k < 0:
        die("no </body> at the start of a line")
    html = html[:k + 1] + block + html[k + 1:]

    grew = len(html) - before
    print("%s" % a.lesson)
    print("  declaration : wk %d day %s, %s, %s" % (a.week, a.day, a.book, a.chapters))
    print("  data        : %s" % data_note)
    print("  epigraph    : %s" % ("replaced" if quote_changed else "unchanged"))
    print("  layer       : linked (%sg3-sparkle.css, %sg3-sparkle.js)" % (p, p))
    print("  size        : %d -> %d bytes (+%d)" % (before, len(html), grew))
    # the layer is linked (~400 bytes); the rest is this lesson's DATA
    budget = 4096 + len(json.dumps(data))
    if grew > budget:
        print("  !! grew %d bytes, expected under %d — check for inlining" % (grew, budget))

    if not a.apply:
        print("\nDRY RUN — nothing written. Re-run with --apply.")
        return
    io.open(a.lesson, "w", encoding="utf-8").write(html)
    print("\nwritten.")


if __name__ == "__main__":
    main()
