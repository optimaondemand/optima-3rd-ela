# G3 sparkle build kit

- `port.py` builds `g3-sparkle.js` / `g3-sparkle.css` from `optima-4th-ela/sparkle.js` + `sparkle.css`, `g3mod.js` and `g3.css`:
  `python tools/g3sparkle/port.py ../optima-4th-ela/sparkle.js ../optima-4th-ela/sparkle.css tools/g3sparkle/g3mod.js tools/g3sparkle/g3.css .`
  Never hand-edit g3-sparkle.*; edit g3mod.js / g3.css / port.py and rebuild. A layer change means re-sweeping every sparkled page.
- `data_wk18.py` writes data/lesson-18-2..4 and fluency (18.1 is hand-written JSON). One script per week.
- `checkin_wk18.py` writes assessments/g3-ela-wk18-checkin.json + key.
- `preview.py` builds an inline preview (layer, art, audio embedded) for Bethany. Never committed.
