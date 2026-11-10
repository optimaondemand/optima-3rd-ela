# G3 ELA handoff: finish The Whipping Boy unit (weeks 19–22), then the unit project

Written Nov 8, 2026. Week 18 is **done and live** (main at `54b4d11`, pushed).

## Paste this to start the next session

> Use the **g3-ela-sparkle-lesson** skill. Read `claude/g3-ela-handoff.md`, `claude/g3-ela-wk18-status.md` and `claude/g3-ela-nov8-update.md` in the ELA OAO project first. Then sparkle **G3 ELA week 19** (The Whipping Boy) the same way week 18 was done, including the Nov 8 rules (Opti reads every "What to do" line, plain-language pass). Ask me the brainstorm questions, show me a preview, and push only when I say "push". After week 19, continue with weeks 20, 21 and 22, one week per run.

## Where everything is

- Repo on Bethany's computer: `C:\repos\optima-3rd-ela` (device_bash: `$HOME/mnt/optima-3rd-ela`). Live: https://optimaondemand.github.io/optima-3rd-ela/
- Build tools in the repo: `tools/g3sparkle/` (`port.py`, `g3mod.js`, `g3.css`, `data_wk18.py`, `checkin_wk18.py`, `plain_wk18.py`, `how_wk18.json`, `preview.py`), `tools/inject.py`, `tools/sweep.js`.
- The layer `g3-sparkle.js` / `g3-sparkle.css` is **generated** by `port.py` from G4's `sparkle.js`/`sparkle.css` (`C:\repos\optima-4th-ela`) + `g3mod.js` + `g3.css`. Never hand-edit the two outputs.
- Each lesson's content: `data/lesson-<w>-<d>.json` (written by `data_wk<NN>.py`).
- Book text for accuracy checks: `Planning docs\whipping_boy_ocr.txt` and `whipping_boy_chapter_index.txt`.
- Earlier accuracy audit for weeks 18–22: project doc `claude/g3-whipping-boy-accuracy-audit.md`. Its HIGH and MED fixes are already in the repo; use it to check what is still open.
- The container sweep runs Playwright. The VM on Bethany's computer has no disk space for Chromium, so run the sweep in the container on byte-identical copies and check sha256 on both sides.

## How week 18 was built (repeat per week)

1. Read all 4 lessons + fluency + `week-<NN>-checkin.html`. Run the accuracy audit against the OCR, ask for approval of each fix, and commit fixes on their own.
2. Copy the untouched lessons to a `pristine-orig` folder. Write `plain_wk<NN>.py`, which turns pristine-orig into pristine. It holds the plain-language edits, plus one `<p class="g3-do" data-say="slug"><b>What to do:</b> …</p>` per activity. Assert every replacement.
3. Write `data_wk<NN>.py`, which produces `data/lesson-<w>-<d>.json`. That covers Opti notes, cards, the word game, copia (day 1 only, never on a lesson with Read Like a Writer), hints, miss lines and transcripts.
4. Rebuild: port, then copy pristine to the repo, then `inject.py --book wb --week W --day D --title "The Whipping Boy" --chapters "Ch. x–y" --apply`. Then run `node tools/sweep.js` on all 5 pages. All 5 must pass.
5. Preview with `preview.py` (everything inline) and send it. Voice clips **only after** Bethany approves the wording.
6. Audio: ElevenLabs flow, `eleven_v4`, voice `DucuBrYttQHeSPCIsQfU`, **one take** (`generations_count: 1`). Download through the built-in browser (fetch, then blob, then `<a download>`) into her Downloads folder, then copy into `assets/audio/...`. Neither cloud shell can reach elevenlabsusercontent.com.
   - **Reuse the 29 direction clips** `assets/audio/guide/opti/g3ela-how-<slug>.mp3` when a line's words match `how_wk18.json` exactly. Record only the new lines.
7. Check-in: audit `week-<NN>-checkin.html` so it tests only what that week taught. Write `assets/g3-ela-wk<NN>-checkin.json` plus the answer key, and get Bethany's approval. Do **not** build the .imscc until she says ready.
8. Weekly family guide `parent-guide-week-<NN>.html` (navy G4-style, same layout as week 18).
9. Commit on her computer as `bbirchum1 <bbirchum@optimaed.com>` with the attribution lines. Run `rm -f .git/index.lock` before and after. Check sha256 against the container build. Push only on "push".
10. Record each week in `claude/g3-ela-wk<NN>-status.md` and add a row to `claude/g3-ela-sparkle-variety-log.md` (word game, art, words voiced) so weeks don't repeat.

## Bethany's standing decisions

- Opti the owl guides every lesson. Keep the original navy header and the page's own colors (no purple, no G4 cream).
- Art is public domain, found by Claude, and credited in `assets/art/CREDITS.md`. No book illustrations. The 4 novel covers on the shelf are the only exception.
- No teacher video scripts. No poem card.
- Every activity gets a "What to do" line that Opti reads.
- Plain words: direct, nothing left to interpretation, each fact once, a sort item has exactly one right answer.
- Read-along: words light up as Opti speaks (📄 Read along with Opti). The open book flips to today's page. Tooltips never clip.
- Reading Road is her painted board, one space per week. Rows read left to right, and weeks 19–22 sit on spaces 19–22 of the North Tower row. Nothing to re-measure.
- Each week ships a preview, a family guide, a sparkled fluency page and an audited check-in (as a Canvas quiz later).

## Known issues for later weeks

- Week 19 day 3 and week 20 day 1 both read Ch. 11.
- The accuracy audit lists LOW wording nits for 19.x–22.x (19.2 Ch. 9 title, 19.3 "sand for brains" is Ch. 11, 19.3 "unprinced", 19.4 "angling for a share of the reward", the 19.4 question mark, 19-fluency punctuation, and others). Fix them in each week's accuracy commit.
- The Opti welcome and card clips were recorded before the Nov 8 plain-language pass. Diff each `transcripts` entry against the page after any change.

## After week 22: the unit project

- Build only after weeks 19–22 are all sparkled.
- **The Whipping Boy project:** a Wanted poster for Hold-Your-Nose Billy and Cutwater, plus a letter from Jemmy to the king telling what really happened.
- It is one fixed project, modeled on G4's `lesson-14-scrapbook.html` and `lesson-19-nts-project.html` in `C:\repos\optima-4th-ela`:
  - short steps, one at a time, guided by Opti
  - a 4-level rubric
  - work saves as you go
  - **turned in as ONE PDF in Canvas**
- Ask Bethany for project ideas for Flat Stanley, Despereaux and Narnia when those units come up.

## Still open from week 18

- Canvas QTI/.imscc for the check-ins: build when Bethany says ready.
- Add the week 18 and unit family guides to the Canvas parent module. Embed codes are in `claude/g3-ela-wk18-status.md`.
- The skill update (What to do lines, plain-language pass, unit project) was proposed on Nov 8. If it wasn't saved, follow this doc.
