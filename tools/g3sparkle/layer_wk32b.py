"""Week 32 layer fix (Nov 16 2026, found in the 420 px playthrough): owlSVG() returns an <img>, which can't sit inside an
SVG, so Opti showed huge under the Reading Road and the certificate. Opti is now an SVG <image> (g3OwlImage), and the
certificate preloads him as a data URL so the saved picture includes him. Edits g3-sparkle.js AND tools/g3sparkle/g3mod.js.
Run once from the repo root: python tools/g3sparkle/layer_wk32b.py"""
import io
FN = """function g3OwlImage(x, y, h) {
  var u = window.__g3OwlData || artURL(ART.companions[resolveCompanion('opti')]);
  return u ? '<image href="' + u + '" x="' + x + '" y="' + y + '" height="' + h + '" width="' + Math.round(h * 0.8) + '" preserveAspectRatio="xMidYMid meet"/>' : '';
}
function g3OwlPreload() {
  if (window.__g3OwlData) return;
  try {
    var ou = artURL(ART.companions[resolveCompanion('opti')]); if (!ou) return;
    if (ou.indexOf('data:') === 0) { window.__g3OwlData = ou; return; }
    fetch(ou).then(function (r) { return r.blob(); }).then(function (bl) {
      var fr = new FileReader(); fr.onload = function () { window.__g3OwlData = fr.result; }; fr.readAsDataURL(bl);
    }).catch(function () {});
  } catch (e) {}
}
"""
PAIRS = [
 ("/* ── Year-end cards (week 32). Taps go into My Work through one gatherAnswers wrapper per card. */\n",
  "/* ── Year-end cards (week 32). Taps go into My Work through one gatherAnswers wrapper per card. */\n" + FN),
 ("""    if (st.at >= 0) s += '<g transform="translate(' + (X[st.at] + 10) + ',' + (Y[st.at] - 2) + ')">' + owlSVG('opti', 26).replace('<svg ', '<svg x="0" y="0" ') + '</g>';""",
  """    if (st.at >= 0) s += g3OwlImage(X[st.at] + 8, Y[st.at] - 34, 32);"""),
 ("""    '<g transform="translate(40,206)">' + owlSVG('opti', 54).replace('<svg ', '<svg x="0" y="0" ') + '</g></svg>';""",
  """    g3OwlImage(34, 194, 66) + '</svg>';"""),
 ("""  var pr = profile(); if (!st.name && pr && pr.name) st.name = pr.name;""",
  """  var pr = profile(); if (!st.name && pr && pr.name) st.name = pr.name;
  g3OwlPreload();"""),
]
for p in ('g3-sparkle.js', 'tools/g3sparkle/g3mod.js'):
    s = io.open(p, encoding='utf-8', newline='').read()
    assert 'function g3OwlImage' not in s, p
    for a, b in PAIRS:
        assert s.count(a) == 1, (p, a[:70], s.count(a)); s = s.replace(a, b)
    io.open(p, 'w', encoding='utf-8', newline='').write(s); print('ok', p)
