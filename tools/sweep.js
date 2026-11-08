/*
 * sweep.js — regression sweep for a sparkled G3 ELA lesson (Opti's Story Map).
 *
 *     node tools/sweep.js lesson-18-1-wb.html
 *
 * Ported Nov 2026 from optima-4th-ela/tools/sweep.js. Serves the REPO over
 * http (art and the layer are referenced, not embedded, so file:// would
 * test the wrong page), plays the page, and exits non-zero if an INVARIANT
 * fails. Every probe is total: a feature this lesson does not have reports
 * (absent) instead of hanging. READ the output — a PASS with (absent)
 * everywhere means nothing built.
 *
 * Run from the repo root.
 */
const { chromium } = require('playwright');
const http = require('http');
const fs   = require('fs');
const path = require('path');

function launch() {
  const pinned = process.env.SWEEP_CHROMIUM || '/opt/pw-browsers/chromium';
  if (fs.existsSync(pinned)) return chromium.launch({ executablePath: pinned });
  return chromium.launch();
}

const REL = process.argv[2];
if (!REL) { console.error('usage: node tools/sweep.js <lesson.html>'); process.exit(2); }
const ROOT = process.cwd();
const ABS  = path.join(ROOT, REL);
if (!fs.existsSync(ABS)) { console.error('no such file: ' + ABS); process.exit(2); }

const TYPES = { '.html':'text/html', '.css':'text/css', '.js':'text/javascript',
  '.json':'application/json', '.png':'image/png', '.jpg':'image/jpeg',
  '.jpeg':'image/jpeg', '.svg':'image/svg+xml', '.mp3':'audio/mpeg',
  '.mp4':'video/mp4', '.webm':'video/webm', '.woff2':'font/woff2', '.vtt':'text/vtt' };

const missing = [];
const server = http.createServer((req, res) => {
  const rel = decodeURIComponent(req.url.split('?')[0]).replace(/^\/+/, '');
  const file = path.join(ROOT, rel);
  if (!file.startsWith(ROOT) || !fs.existsSync(file) || fs.statSync(file).isDirectory()) {
    missing.push(rel); res.writeHead(404); res.end('nope'); return;
  }
  res.writeHead(200, { 'Content-Type': TYPES[path.extname(file).toLowerCase()] || 'application/octet-stream' });
  fs.createReadStream(file).pipe(res);
});
const EXPECTED_404 = /^assets\/(plates|audio|video|art)\//;
const errs = [];

(async () => {
  await new Promise(r => server.listen(0, '127.0.0.1', r));
  const FILE = 'http://127.0.0.1:' + server.address().port + '/' + path.relative(ROOT, ABS).split(path.sep).join('/');
  console.log('serving ' + ROOT + '\n   ->  ' + FILE + '\n');
  const browser = await launch().catch(e => { console.error('could not start Chromium: ' + e.message); process.exit(2); });
  const ctx = await browser.newContext({ viewport: { width: 1150, height: 900 } });
  const page = await ctx.newPage();
  page.on('console', m => { if (m.type() === 'error' || m.type() === 'warning') errs.push(m.type() + ': ' + m.text()); });
  page.on('pageerror', e => errs.push('pageerror: ' + e.message));
  page.on('dialog', d => d.accept());
  await page.goto(FILE);
  await page.waitForTimeout(500);
  const R = {};
  const SHORT = 1200;
  const has  = async sel => (await page.locator(sel).count()) > 0;
  const txt  = async sel => (await has(sel)) ? (await page.locator(sel).first().innerText().catch(() => '(unreadable)')).trim() : '(absent)';
  const vis  = async sel => (await has(sel)) ? await page.locator(sel).first().isVisible().catch(() => false) : '(absent)';
  const cnt  = async sel => await page.locator(sel).count();
  const tap  = async sel => { if (await has(sel)) { await page.locator(sel).first().click({ timeout: SHORT }).catch(() => {}); return true; } return false; };
  const type = async (sel, v) => { if (await has(sel)) { await page.locator(sel).first().fill(v, { timeout: SHORT }).catch(() => {}); return true; } return false; };
  const DATA = await page.evaluate(() => window.OAO_DATA || {});
  const LESSON = await page.evaluate(() => { try { return JSON.parse(document.getElementById('oao-lesson').textContent); } catch (e) { return {}; } });

  // ── profile + greeting + Opti
  R['no build step failed'] = await page.evaluate(() => window.OAO_SPARKLE_FAILED || 'UNDEFINED');
  R['profile card'] = await vis('#spkProfileCard');
  R['profile card asks for Opti'] = (await txt('#spkProfileCard h3'));
  await type('#spkNameInput', '<b>Nora');
  await tap('#spkBegin');
  await page.waitForTimeout(250);
  R['greeting'] = (await txt('#spkGreet')).replace(/\n/g, ' ').slice(0, 160);
  R['name rendered as text only'] = await page.evaluate(() => { const el = document.getElementById('spkGreetName'); return el ? el.children.length === 0 && el.textContent.indexOf('<') === -1 : '(absent)'; });
  R['Opti owl art (path)'] = await page.evaluate(() => { const i = document.querySelector('.spk-companion-img, #spkGreetOwl img'); return i ? i.getAttribute('src') : '(absent)'; });
  R['plate'] = await page.evaluate(() => { const i = document.querySelector('.spk-plate img'); return i ? i.getAttribute('src') : '(none)'; });
  R['plate look line'] = await txt('.g3-plate-look p');
  R['dol cards'] = await cnt('.spk-dol-card');

  // ── word study
  await tap('.tab-btn[data-tab="words"]');
  await page.waitForTimeout(400);
  R['tower game'] = await cnt('#g3card-tower');
  if (DATA.wordgame && DATA.wordgame.items) {
    const items = DATA.wordgame.items;
    const wrong = items[0].a === 0 ? 1 : 0;
    await tap('#g3card-tower .g3-opt-btn[data-n="' + wrong + '"]');
    await page.waitForTimeout(150);
    R['tower miss line'] = (await txt('#g3card-tower .g3-fb.no')).slice(0, 80);
    for (let i = 0; i < items.length; i++) {
      await tap('#g3card-tower .g3-opt-btn[data-n="' + items[i].a + '"]');
      await page.waitForTimeout(120);
    }
    R['tower finished'] = await txt('#g3card-tower .g3-finish');
    R['tower steps lit'] = await page.evaluate(() => [...document.querySelectorAll('#g3card-tower rect[fill="#F2C14E"]')].length);
  }
  R['copia card'] = await cnt('.spk-copia-card');
  R["say-word row (hidden until audio)"] = await cnt(".g3-sayrow");
  R['glossary words'] = await page.evaluate(() => [...document.querySelectorAll('.g3-gl')].map(s => s.querySelector('.g3-gl-w').textContent));
  // hint ladder on the first fill-in game that has hints
  const hintId = DATA.hints ? Object.keys(DATA.hints)[0] : null;
  if (hintId && await has('#' + hintId)) {
    const lad = [];
    for (let i = 0; i < 3; i++) {
      await page.locator('#' + hintId).fill('zzz').catch(() => {});
      await page.evaluate(id => { const b = document.getElementById(id).closest('.fillin-game, .activity').querySelector('.fillin-check-btn, button[onclick*="FillIn"], button[onclick*="Fill"]'); if (b) b.click(); }, hintId);
      await page.waitForTimeout(160);
      lad.push(await page.evaluate(id => { const h = document.getElementById(id).parentNode.querySelector('.spk-hint'); return h ? h.textContent.slice(0, 50) : '(no hint)'; }, hintId));
    }
    R['hint ladder (' + hintId + ')'] = lad;
  } else R['hint ladder'] = '(no hints in DATA)';

  // ── reading
  await tap('.tab-btn[data-tab="reading"]');
  await page.waitForTimeout(400);
  R['cards'] = await page.evaluate(() => [...document.querySelectorAll('.g3-card')].map(c => c.id));
  R['every card opens with What am I looking at?'] = await page.evaluate(() =>
    [...document.querySelectorAll('.g3-card')].filter(c => !c.querySelector('.g3-look')).map(c => c.id));
  R['road starts folded'] = await page.evaluate(() => { const b = document.getElementById('spkRoadBody'); return b ? b.hidden : '(absent)'; });
  await tap('#spkRoadFold');
  await page.waitForTimeout(600);
  R['map week spaces (32)'] = await cnt('#spkMap .spk-space');
  R['map title'] = await page.evaluate(() => { const t = [...document.querySelectorAll('#spkMap text')].pop(); return t ? t.textContent : '(absent)'; });
  R['here line'] = await txt('#spkHere');
  R['shelf books / read'] = [await cnt('.spk-book'), await cnt('.spk-book.read')];
  R['old tracker gone'] = await cnt('#tab-reading .tracker-card');
  R['no broken images'] = await page.evaluate(() => [...document.images].filter(i => i.complete && i.naturalWidth === 0 && i.src).map(i => i.src));

  // ── assignment
  await tap('.tab-btn[data-tab="assignment"]');
  await page.waitForTimeout(400);
  R['two roads (tiers)'] = await cnt('.spk-road');
  R['coaches'] = await cnt('.spk-coach');
  R['journal button'] = await page.evaluate(() => { const b = [...document.querySelectorAll('button')].find(x => /journal/i.test(x.textContent)); return b ? b.textContent.trim() : '(absent)'; });
  R['downloadJournal defined'] = await page.evaluate(() => typeof window.downloadJournal);
  R['media slots mounted'] = await page.evaluate(() => [...document.querySelectorAll('[data-spk-slot]')].map(e => e.getAttribute('data-spk-slot')));
  R['Opti faces'] = await cnt('.g3-opti-face');

  // ── no sideways scroll at phone width
  await page.setViewportSize({ width: 420, height: 860 });
  await page.waitForTimeout(300);
  for (const t of ['warmup', 'words', 'reading', 'assignment']) {
    await tap('.tab-btn[data-tab="' + t + '"]'); await page.waitForTimeout(200);
    R['420px sideways scroll · ' + t] = await page.evaluate(() => document.documentElement.scrollWidth - document.documentElement.clientWidth);
  }

  // ── storage blocked
  const p2 = await ctx.newPage();
  p2.on('pageerror', e => errs.push('nostorage pageerror: ' + e.message));
  await p2.addInitScript(() => { Object.defineProperty(window, 'localStorage', { get() { throw new Error('blocked'); } }); });
  await p2.goto(FILE); await p2.waitForTimeout(400);
  R['no-storage: tabs render'] = await p2.locator('.tab-btn').count();

  // ── reduced motion
  const p3 = await ctx.newPage();
  p3.on('pageerror', e => errs.push('reduced pageerror: ' + e.message));
  await p3.emulateMedia({ reducedMotion: 'reduce' });
  await p3.goto(FILE); await p3.waitForTimeout(400);
  R['reduced-motion: page builds'] = await p3.evaluate(() => (window.OAO_SPARKLE_FAILED || ['?']).length === 0);

  // ── invariants
  const raw = fs.readFileSync(ABS, 'utf8');
  const bytes = Buffer.byteLength(raw);
  R['INVARIANT no data:image in the file'] = (raw.match(/data:image/g) || []).length;
  R['INVARIANT file size (bytes)'] = bytes;
  R['INVARIANT layer is linked, not pasted'] = /<link[^>]+g3-sparkle\.css/.test(raw) && /<script[^>]+g3-sparkle\.js/.test(raw);
  R['INVARIANT injected exactly once'] = (raw.match(/OAO SPARKLE LAYER/g) || []).length;
  R['404s (art/audio not supplied yet — expected)'] = [...new Set(missing.filter(m => EXPECTED_404.test(m)))];
  const fatal404 = [...new Set(missing.filter(m => !EXPECTED_404.test(m) && m !== 'favicon.ico'))];
  R['INVARIANT unexpected 404s'] = fatal404;

  console.log(JSON.stringify(R, null, 1));
  console.log('\n=== console errors/warnings ===');
  console.log(errs.length ? errs.join('\n') : 'NONE');
  const fail = [];
  if (R['no build step failed'] && R['no build step failed'].length) fail.push('build steps failed: ' + R['no build step failed']);
  if (R['INVARIANT no data:image in the file'] > 0) fail.push('data: URIs found in the file');
  if (!R['INVARIANT layer is linked, not pasted']) fail.push('g3-sparkle.css/js not linked');
  if (R['INVARIANT injected exactly once'] !== 1) fail.push('layer injected ' + R['INVARIANT injected exactly once'] + ' times');
  if (bytes > 260000) fail.push('file is ' + bytes + ' bytes — something got inlined');
  if (fatal404.length) fail.push('404: ' + fatal404.join(', '));
  if (errs.some(e => /pageerror/.test(e))) fail.push('page errors');
  for (const t of ['warmup', 'words', 'reading', 'assignment']) if (R['420px sideways scroll · ' + t] > 2) fail.push('sideways scroll on ' + t + ' at 420px');
  console.log('\n=== verdict ===');
  console.log(fail.length ? 'FAILED\n  - ' + fail.join('\n  - ') : 'PASS');
  await browser.close(); server.close();
  process.exit(fail.length ? 1 : 0);
})();
