"""Medieval nonfiction unit guide (weeks 23-24), asked for by Bethany Nov 16 2026. Head/CSS and How the Lesson Pages Work
from parent-guide-week-23.html (no fluency line: these weeks have no fluency page); structure from parent-guide-wb-unit.html.
Every line from the finished week 23-24 lessons, DATA and weekly guides. Run from the repo root."""
import io
s = io.open('parent-guide-week-23.html', encoding='utf-8').read()
H0 = s[:s.index('<body>')]
howto = s[s.index('<section class="howto">'):s.index('</section>', s.index('<section class="howto">')) + 10]
OWL = 'https://raw.githubusercontent.com/optimaondemand/optima-assets/eeb0b335630058906d52f478028361d352253a93/images/Optima%20Final%20Circle%20-%20Owl%20Only.png'
ART = 'https://optimaondemand.github.io/optima-3rd-ela/assets/art/med/'
page = H0.replace('Week 23 Family Guide · Medieval Nonfiction · 3rd Grade ELA', 'Medieval Nonfiction Unit Guide · 3rd Grade ELA · Optima Academy Online')
assert 'Medieval Nonfiction Unit Guide' in page
EXTRA_CSS = ('.grid2{display:grid;grid-template-columns:1fr 1fr;gap:14px;}\n.dont li::before{content:"✗";color:#C0545C;}\n'
             'a{color:#1F6FA8;font-weight:700;}\n@media (max-width:720px){.grid2{grid-template-columns:1fr;}}\n')
assert page.count('</style>') == 1
page = page.replace('</style>', EXTRA_CSS + '</style>')
page += '''<body>
<div class="wrap">

<header class="hero">
<div class="hero-text">
<div class="brand"><img src="''' + OWL + '''" alt="Optima Academy Online">Family Guide · 3rd Grade ELA</div>
<h1>Unit Guide: Life in the Middle Ages</h1>
<div class="sub">True articles about castles, knights, towns and work · Weeks 23–24</div>
<div class="chips">
<span class="chip">2 weeks</span>
<span class="chip">8 short articles</span>
<span class="chip">Informational writing</span>
<span class="chip">Guide: Opti the owl</span>
</div>
<button class="print-btn" onclick="window.print()">🖨️ Print this guide</button>
</div>
<div class="hero-art" style="background-image:url(\'''' + ART + '''med-sept.jpg');background-position:center 35%;" role="img" aria-label="A medieval painting of a castle above fields at harvest time"></div>
</header>

''' + howto + '''

<section class="card">
<div class="card-head"><span class="ico">🏰</span><h2>About the Unit</h2></div>
<p>Your student just finished <em>The Whipping Boy</em>, a made-up story set long ago. For the next two weeks, your student reads <strong>true articles about real life in the Middle Ages</strong>: castles, servants and apprentices, royal courts, food, how castles were built, how a boy became a knight, busy medieval towns, and what stories get right and wrong about the past.</p>
<p>Each lesson has <strong>one short article right on the page</strong>, so there is no book to have nearby. We read these articles because they practice the reading skills nonfiction needs (finding the central idea and spotting cause and effect), and because they help students see what in <em>The Whipping Boy</em> came from history and what the author made up.</p>
<p class="quote">“Stories borrow from history but add imagination.”<small>Real vs. Imagined, Week 24 Day 4</small></p>
</section>

<section class="card">
<div class="card-head"><span class="ico">🗓️</span><h2>How a Week Works</h2></div>
<div class="grid2">
<div class="box b-sky"><div class="box-label">Days 1–4</div>Read one short article, practice the week’s word study (a word part, a spelling pattern, a grammar skill and new vocabulary), answer three questions and take one step in the informational writing.</div>
<div class="box b-gold"><div class="box-label">Job Spotlight</div>Each day meets one real medieval job, like the page, the apprentice, the stonemason or the scribe.</div>
<div class="box b-green"><div class="box-label">Diligence Watch</div>After reading, your student decides if three moments show someone working hard and carefully: Yes or Not yet.</div>
<div class="box b-plum"><div class="box-label">Check-In</div>A short Canvas quiz at the end of each week on that week’s skills and articles.</div>
</div>
</section>

<section class="card">
<div class="card-head"><span class="ico">🗺️</span><h2>The Unit, Week by Week</h2></div>
<table class="days">
<thead><tr><th>Week</th><th>Articles</th><th>Writing step</th></tr></thead>
<tbody>
<tr><td class="day-n">23</td><td><span class="ch">Castles, apprentices, royal courts, food</span><br>Life in a Medieval Castle · Servants and Apprentices · Royal Courts: Power and Protocol · What Did Medieval People Eat? Reading skill: <strong>central idea</strong>. Word part: trans (across). Spelling: VCCV words (bas·ket). Grammar: capital letters in names and titles. Word game: Illuminate the Page.</td><td>Choose a topic, write a research question, take notes, plan</td></tr>
<tr><td class="day-n">24</td><td><span class="ch">Building, knights, towns, real vs. imagined</span><br>How Castles Were Built · Knights: Warriors and Gentlemen · Medieval Towns: Busy, Smelly, and Alive · Real vs. Imagined: The Middle Ages in Stories. Reading skill: <strong>cause and effect</strong>. Word part: script/scribe (write). Spelling: -ful, -less, -ness, -ly. Grammar: main idea and details. Word game: Market Day.</td><td>Draft, revise, edit, publish</td></tr>
</tbody>
</table>
</section>

<section class="card">
<div class="card-head"><span class="ico">✍️</span><h2>Your Student’s Informational Writing</h2><span class="tag">Writer’s Workshop</span></div>
<div class="essay"><span>Wk 23 · Choose &amp; take notes</span><span>Wk 24 · Draft, revise &amp; publish</span></div>
<p>Across the two weeks, your student writes an <strong>informational paragraph</strong> about one small part of medieval life. Week 23: choose a topic that is not too big, write a research question, take notes from two articles, and plan the paragraph (topic sentence, two details, closing). Week 24: draft it, revise so every sentence fits the topic, edit for capitals and periods, and publish. An example writer named Clara shows each step first.</p>
</section>

<section class="card">
<div class="card-head"><span class="ico">✅</span><h2>How Learning Is Checked</h2></div>
<ul class="check">
<li>Each lesson’s work, copied and pasted into Canvas: the article questions, a word study answer, and the day’s writing step</li>
<li>A Canvas check-in quiz at the end of each week</li>
<li>The published informational paragraph at the end of Week 24</li>
</ul>
</section>

<section class="card">
<div class="card-head"><span class="ico">💛</span><h2>Good to Know Ahead of Time</h2></div>
<div class="grid2">
<div class="box b-rose"><div class="box-label">Hard lives</div>The articles are honest that life was hard for most people: servants worked long days, children often learned a job by working instead of going to school, and poor families ate plain food. Nothing is graphic.</div>
<div class="box b-rose"><div class="box-label">Rank and fairness</div>The royal court article explains strict rules about rank. In <em>The Whipping Boy</em>, the prince does whatever he wants without punishment, and the lessons ask students whether that was realistic.</div>
<div class="box b-plum"><div class="box-label">Old jobs</div>The Job Spotlight on the barber-surgeon explains that medieval barbers also pulled bad teeth and treated cuts. “Stories say” the barber pole’s stripes come from that old job.</div>
<div class="box b-plum"><div class="box-label">Real old pictures</div>The lessons use real paintings and book pages from the Middle Ages and later, so the pictures your student sees are from history.</div>
</div>
</section>

<section class="card">
<div class="card-head"><span class="ico">🤝</span><h2>How to Help (Without Doing It for Them)</h2></div>
<div class="grid2">
<div>
<h3 style="font-size:19px;margin-bottom:6px;">Try this</h3>
<ul class="check">
<li>Ask “What was the most important point of today’s article?” and then “What fact proves it?”</li>
<li>Ask “Why?” about something in the article, and listen for a because sentence.</li>
<li>Point them to Opti’s tips and the hint buttons before you step in.</li>
<li>Be the audience for the published paragraph.</li>
</ul>
</div>
<div>
<h3 style="font-size:19px;margin-bottom:6px;">Try to avoid</h3>
<ul class="check dont">
<li>Typing or wording answers for them. Teachers need to see your student’s own thinking.</li>
<li>Fixing their writing. Revising and editing are lessons of their own in Week 24.</li>
<li>Choosing the writing topic for them. A topic they care about makes the writing easier.</li>
</ul>
</div>
</div>
</section>

<section class="card">
<div class="card-head"><span class="ico">🧭</span><h2>Where the Unit Fits</h2></div>
<p>Before: <a href="parent-guide-wb-unit.html"><em>The Whipping Boy</em> unit</a> (weeks 18–22). After: <a href="parent-guide-lww-unit.html"><em>The Lion, the Witch and the Wardrobe</em> unit</a> (weeks 25–30). Each week also has its own family guide: <a href="parent-guide-week-23.html">Week 23</a> · <a href="parent-guide-week-24.html">Week 24</a>.</p>
</section>

<p class="foot">Optima Academy Online · 3rd Grade ELA · Medieval Nonfiction Unit Guide</p>
</div>
</body>
</html>
'''
io.open('parent-guide-med-unit.html', 'w', encoding='utf-8').write(page)
print('ok')
