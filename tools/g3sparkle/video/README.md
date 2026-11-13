# G3 ELA Opti teach videos (Nov 13 2026 pilot, week 19)

Zero extra ElevenLabs credits: each film reuses the Opti teach clip (`assets/audio/guide/opti/g3ela-W-D-teach-<id>.mp3`).
Output: `assets/video/g3ela-W-D-teach-<id>.mp4` + `.jpg` poster. A teach mod with `"video": "<name>"` in DATA.teach shows the film in place of the button (layer: `teachVideo` in g3mod.js / g3-sparkle.js; falls back to the button if the film won't load). `"after": "<css>"` places it after an element (RWM: after `.rwm-header`).

Built in the cloud container (needs Chromium/Playwright, ffmpeg, Poppins + Lora + Noto Color Emoji fonts; the VM on Bethany's computer has no room for Chromium).

1. `specs.py`: one entry per film. Scenes appear when Opti says their anchor phrase (text from the script); items fade in on their own anchors; `hl` highlights, `dots` adds syllable dots.
2. `python timeline.py scripts.json` (scripts.json = {clip-name: script}; mp3s in /tmp/vid/) → timeline.json. Times come from the clip's pauses (ffmpeg silencedetect) aligned to the script's punctuation; check the printed captions against the pauses and add an override in `OV` when one is off.
3. `node capture.js <clip-name> 12` → frames (render.html; opti.b64 = Opti PNG as base64).
4. `ffmpeg -framerate 12 -i frames/<k>/f%04d.jpg -i <k>.mp3 -c:v libx264 -preset slow -tune stillimage -crf 30 -pix_fmt yuv420p -r 24 -c:a aac -b:a 96k -af apad -shortest -movflags +faststart <k>.mp4` (~1 MB each). Poster = the frame 0.4 s before scene 2.

## Saving credits (Nov 13 2026)
- Joined endings: when a film's last lines are word-for-word an existing `g3ela-how-*.mp3` clip, record only the opening and join:
  `ffmpeg -i head.mp3 -f lavfi -t 0.25 -i anullsrc=r=44100:cl=mono -i g3ela-how-X.mp3 -filter_complex "[0:a]aresample=44100,aformat=channel_layouts=mono[a];[2:a]aresample=44100,aformat=channel_layouts=mono[c];[a][1:a][c]concat=n=3:v=0:a=1" -c:a libmp3lame -b:a 128k g3ela-W-D-teach-<id>.mp3`
  (week 19: 19.3 morph + how-morph3, 19.4 spell + how-spell4). DATA `script` = full joined words.
- Trims: cut a repeated sentence out of a recorded clip inside its pause (silencedetect), 0.1 s fades; update DATA `script`.
- Downloads from the browser sometimes land as GUID `.tmp` files in Downloads: match them to clips by byte size.
- Caption times: check `timeline.py`'s printout against the pauses; joined clips and very short phrases may need `OV` overrides.
- **Exact timings + free trims: `trim.py`** (pip install pocketsphinx; its English model ships in the package, nothing to download). `python trim.py in.mp3 out.mp3 "full script" "sentence to cut" ...` cuts whole sentences inside their pauses and prints the new script. `timeline.py` uses the same forced alignment for word-exact cue times when it can (falls back to pauses; add missing words to `EXTRA` in trim.py). Week 18: 8 clips trimmed (`trimmed_wk18.json`, `video_wk18.py`).
