// Playtest a G3 ELA VR page in Chromium: both paths at 1150 and 420 px.
// usage: node tools/vr/playtest_vr.js 18 [outdir]
const { chromium } = require('playwright');
const path = require('path'), fs = require('fs');
const W = process.argv[2] || '18';
const ROOT = path.resolve(__dirname, '..', '..');
const OUT = process.argv[3] || path.join(ROOT, '..', 'vrtest');
fs.mkdirSync(OUT, { recursive: true });
const url = 'file://' + path.join(ROOT, `vr-${W}.html`);
const fails = [];
const ok = (c, m) => { if (!c) fails.push(m); };

(async () => {
  const b = await chromium.launch();
  for (const width of [1150, 420]) {
    const ctx = await b.newContext({ viewport: { width, height: 900 } });
    const pg = await ctx.newPage(); const errs = [];
    pg.on('pageerror', e => errs.push(e.message));
    await pg.route(/fonts\.|youtube|githubusercontent/, r => r.abort());
    await pg.goto(url); await pg.waitForTimeout(300);
    const side = () => pg.evaluate(() => document.documentElement.scrollWidth > window.innerWidth + 1);
    ok(!(await side()), `${width}: sideways scroll at start`);
    ok(await pg.isVisible('#steps .step[data-n="1"]'), `${width}: step 1 not shown`);
    ok(!(await pg.isVisible('#steps .step[data-n="2"]')), `${width}: step 2 shown too early`);
    // VR path: click through 5 steps
    for (let i = 1; i <= 5; i++) await pg.click(`#steps .step[data-n="${i}"] .next-step`);
    ok(await pg.isVisible('#vrDone svg.stamp'), `${width}: VR stamp missing`);
    ok(await pg.isVisible('#extra'), `${width}: extra stop hidden`);
    ok((await pg.evaluate(() => localStorage.getItem('oao.g3ela.vr.18'))) === 'vr', `${width}: vr key not saved`);
    // help drawer, images loaded
    await pg.click('#help summary');
    await pg.evaluate(() => document.querySelectorAll('#help img').forEach(i => i.loading = 'eager'));
    await pg.waitForTimeout(600);
    const broken = await pg.evaluate(() => [...document.querySelectorAll('#help img')].filter(i => !i.complete || !i.naturalWidth).map(i => i.src));
    ok(broken.length === 0, `${width}: broken help images ${broken}`);
    ok(!(await side()), `${width}: sideways scroll with help open`);
    await pg.screenshot({ path: `${OUT}/vr-${width}.png`, fullPage: true });

    // Road Map Day path (fresh storage)
    await pg.evaluate(() => localStorage.clear()); await pg.reload(); await pg.waitForTimeout(200);
    await pg.click('#pathMap');
    ok(await pg.isVisible('#map') && !(await pg.isVisible('#vr')), `${width}: path toggle failed`);
    await pg.click('.obj[data-o="sword"]');
    ok((await pg.textContent('#mfb')).startsWith('Not that one'), `${width}: wrong-pick message missing`);
    const clues = await pg.evaluate(() => VR.clues.map(c => c.a));
    for (const a of clues) await pg.click(`.obj[data-o="${a}"]`);
    ok(await pg.isVisible('#frames'), `${width}: frames not shown after clues`);
    ok(await pg.isDisabled('#savePdf'), `${width}: save enabled too early`);
    await pg.click('.chipx[data-k="0"]');
    await pg.fill('#fr0', (await pg.inputValue('#fr0')) + ' and he wanted to see the world outside the castle walls.');
    await pg.click('.chipx[data-k="1"]');
    await pg.fill('#fr1', (await pg.inputValue('#fr1')) + ' who would get whipped for him anyway.');
    await pg.fill('#nm', 'Test Student');
    ok(!(await pg.isDisabled('#savePdf')), `${width}: save still disabled`);
    ok(!(await side()), `${width}: sideways scroll on Road Map Day`);
    await pg.screenshot({ path: `${OUT}/map-${width}.png`, fullPage: true });
    await pg.evaluate(() => { window.print = () => {}; });
    await pg.click('#savePdf');
    ok(await pg.isVisible('#saveview .sheet'), `${width}: save view missing`);
    ok((await pg.evaluate(() => localStorage.getItem('oao.g3ela.vr.18'))) === 'map', `${width}: map key not saved`);
    if (width === 1150) {
      await pg.emulateMedia({ media: 'print' });
      await pg.pdf({ path: `${OUT}/mapday.pdf`, format: 'Letter' });
      const pdf = fs.readFileSync(`${OUT}/mapday.pdf`, 'latin1');
      const pages = (pdf.match(/\/Type\s*\/Page[^s]/g) || []).length;
      ok(pages >= 1 && pages <= 2, `PDF has ${pages} pages`);
      console.log('PDF pages:', pages);
    }
    ok(errs.length === 0, `${width}: page errors ${errs}`);
    await ctx.close();
  }
  await b.close();
  if (fails.length) { console.log('✗ ' + fails.join('\n✗ ')); process.exit(1); }
  console.log(`✓ vr-${W}.html playtest passes (1150 + 420, both paths)`);
})();
