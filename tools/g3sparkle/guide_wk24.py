"""Week 24 family guide: week 23's guide (head/CSS) with a new body. Every line from the finished week 24 lessons and DATA."""
import io
s = io.open('parent-guide-week-23.html', encoding='utf-8').read()
head = s[:s.index('<body>')].replace('Week 23 Family Guide · Medieval Nonfiction · 3rd Grade ELA', 'Week 24 Family Guide · Medieval Nonfiction · 3rd Grade ELA')
assert 'Week 24 Family Guide' in head
howto = s[s.index('<section class="howto">'):s.index('</section>', s.index('<section class="howto">')) + 10]
assert 'Fluency' not in howto
def w(a, b): return '<div class="word"><b>%s</b><span>%s</span></div>' % (a, b)
WORDS = [('moat','a deep ditch, often filled with water, around a castle'),('stonemason','a skilled worker who cuts and builds with stone'),('drawbridge','a bridge over a moat that can be raised to block the way in'),('keep','the strongest inner tower of a castle'),
 ('chivalry','the code of honorable behavior for knights'),('squire','a young man serving a knight while training to become one'),('dubbed','made a knight in a ceremony, with the tap of a sword'),('tournament','a contest where knights showed their skill'),
 ('guild','a group of craftsmen or merchants in the same trade'),('merchant','a person who buys and sells goods for profit'),('trade','the buying and selling of goods'),('cathedral','a large, important church'),
 ('historian','a person who studies history using evidence'),('accurate','correct; true to the facts'),('idealize','to make something seem better than it really is'),('evidence','facts used to support a claim')]
body = '''<body>
<div class="wrap">

<header class="hero">
<div class="hero-text">
<div class="brand"><img src="https://raw.githubusercontent.com/optimaondemand/optima-assets/eeb0b335630058906d52f478028361d352253a93/images/Optima%20Final%20Circle%20-%20Owl%20Only.png" alt="Optima Academy Online">Family Guide · 3rd Grade ELA</div>
<h1>Week 24: Market Day</h1>
<div class="sub">Medieval Nonfiction, part 2: castles, knights, towns, and what stories get right</div>
<div class="chips">
<span class="chip">4 lessons</span>
<span class="chip">4 short articles</span>
<span class="chip">No novel this week</span>
<span class="chip">Check-In at week’s end</span>
</div>
<button class="print-btn" onclick="window.print()">🖨️ Print this guide</button>
</div>
<div class="hero-art" style="background-image:url('https://optimaondemand.github.io/optima-3rd-ela/assets/art/med/med-town.jpg');background-position:center 40%;" role="img" aria-label="An old wall painting of a busy town street with dancers and an open shop"></div>
</header>

''' + howto + '''

<section class="card">
<div class="card-head"><span class="ico">🧭</span><h2>This Week at a Glance</h2></div>
<p>This is the second week of true articles about the Middle Ages. Each lesson has one short article, right on the page, so there is no book to have nearby. Day 1 is about how castles were built. Day 2 follows a boy on the long road to becoming a knight. Day 3 visits a loud, busy, smelly medieval town. Day 4 asks what stories like <em>The Whipping Boy</em> get right about the Middle Ages, and what they make up. Your student also finishes and publishes the informational paragraph started last week.</p>
<div class="glance">
<div class="box b-sky"><div class="box-label">Reading skill</div><strong>Cause and effect.</strong> A cause is why something happens. The effect is what happens. Castles had thick walls because enemies attacked.</div>
<div class="box b-green"><div class="box-label">Big idea</div><strong>Real or imagined?</strong> Stories borrow from history but add imagination. What was the real Middle Ages like?</div>
</div>
<p class="quote">“Stories borrow from history but add imagination.”<small>Real vs. Imagined: The Middle Ages in Stories, Day 4</small></p>
</section>

<section class="card">
<div class="card-head"><span class="ico">📅</span><h2>Day by Day</h2></div>
<table class="days">
<thead><tr><th>Lesson</th><th>Reading</th><th>Big question</th></tr></thead>
<tbody>
<tr>
<td class="day-n">24.1<span>Day 1</span></td>
<td><span class="ch">How Castles Were Built</span><br>Your student finds causes and effects in how castles were built, then drafts the whole paragraph.<br><span class="pill p-guide">Guide: Opti</span><span class="pill p-extra">Sentence rewrite</span></td>
<td>Building a medieval castle could take thirty years. What would that feel like, to work your whole life on one building and never see it finished?</td>
</tr>
<tr>
<td class="day-n">24.2<span>Day 2</span></td>
<td><span class="ch">Knights: Warriors and Gentlemen</span><br>Your student tells the steps to becoming a knight in order, then revises the paragraph so every sentence fits the topic.<br><span class="pill p-guide">Guide: Opti</span><span class="pill p-poem">Poetry</span><span class="pill p-extra">Read Like a Writer video</span></td>
<td>The code of chivalry said knights must be brave, loyal, and courteous. Can you think of a character from any book you’ve read who lived by a code like this?</td>
</tr>
<tr>
<td class="day-n">24.3<span>Day 3</span></td>
<td><span class="ch">Medieval Towns: Busy, Smelly, and Alive</span><br>Your student uses the author’s details to picture a medieval town, then edits the paragraph for capitals and periods.<br><span class="pill p-guide">Guide: Opti</span><span class="pill p-extra">Read Like a Writer</span></td>
<td>Imagine walking through a medieval town. What would you see, hear, and smell? How different would it be from where you live?</td>
</tr>
<tr>
<td class="day-n">24.4<span>Day 4</span></td>
<td><span class="ch">Real vs. Imagined: The Middle Ages in Stories</span><br>Your student sorts what is real from what stories made up, then publishes the paragraph.<br><span class="pill p-guide">Guide: Opti</span><span class="pill p-poem">Poetry</span><span class="pill p-extra">Read Like a Writer</span></td>
<td>After two weeks of reading about the real Middle Ages, what surprised you most? What was different from how you imagined it?</td>
</tr>
<tr class="extra-row">
<td class="day-n">📋<span>Check-In</span></td>
<td colspan="2">A 14-point check on the week, in Canvas: main ideas and details, the root script/scribe, the endings -ful, -less, -ness and -ly, the Day 1 castle article, and a short writing response.</td>
</tr>
</tbody>
</table>
</section>

<section class="card">
<div class="card-head"><span class="ico">🔤</span><h2>Words to Know</h2><span class="tag">Use them at home!</span></div>
<div class="words">
''' + '\n'.join(w(a, b) for a, b in WORDS) + '''
</div>
<div class="skills">
<div class="box b-sky"><div class="box-label">Word parts</div>The root <strong>script</strong> or <strong>scribe</strong> means <strong>write</strong>. One root, two spellings.<span class="eg">script · describe · manuscript · inscription</span></div>
<div class="box b-gold"><div class="box-label">Spelling</div>Four endings, four jobs: <strong>-ful</strong> means full of, <strong>-less</strong> means without, <strong>-ness</strong> names a thing, <strong>-ly</strong> tells how.<span class="eg">hopeful · hopeless · kindness · quickly</span></div>
<div class="box b-green"><div class="box-label">Grammar</div>A paragraph has one <strong>main idea</strong>, often in the first sentence. The other sentences are <strong>details</strong> that support it. A sentence that doesn’t is off the topic.<span class="eg">Castles were built to be hard to attack. The walls were thick enough to stop arrows.</span></div>
</div>
</section>

<section class="card">
<div class="card-head"><span class="ico">✨</span><h2>New in the Lessons</h2></div>
<div class="extras">
<div class="box b-plum"><div class="box-label">🧺 Market Day</div>This week’s word game is a medieval market square. Each stall sells one kind of word: words with the root script or scribe on Day 1, and words with -ful, -less, -ness or -ly after that. Your student reads the word on the basket and taps the stall that sells it. Each right answer brings a customer, and by Day 4 the square is full.</div>
<div class="box b-gold"><div class="box-label">🎬 Opti’s videos</div>Every Word Study activity, all four days, starts with a short video where Opti shows how it works. On Day 2, Opti also shows how to do Read Like a Writer with a different sentence from the knights article.</div>
<div class="box b-sky"><div class="box-label">⭐ Job Spotlight</div>Each day opens the Reading tab with a real medieval job: a stonemason, a squire, a barber-surgeon, and a scribe.</div>
<div class="box b-green"><div class="box-label">🏮 Diligence Watch</div>After reading, your student decides if three facts from the article show someone working hard: Yes or Not yet.</div>
</div>
<p class="small" style="margin-top:12px;">Each day opens with a real painting: Jean Fouquet’s builders and their wooden crane (about 1470), two knights jousting in a book of songs (about 1305–1315), a busy town street painted in Siena, Italy (1338–1339), and a storybook knight painted in 1901, about 600 years after the Middle Ages. Your student looks first, then taps to learn about it.</p>
</section>

<section class="card">
<div class="card-head"><span class="ico">✍️</span><h2>Your Student’s Writing</h2><span class="tag">Writer’s Workshop</span></div>
<div class="essay"><span>Wk 23 · Choose &amp; take notes</span><span class="now">Wk 24 · Draft, revise &amp; publish</span></div>
<p>This week your student finishes the informational paragraph about one part of medieval life. Day 1: <strong>draft the whole paragraph</strong> (topic sentence, two details, closing sentence). Day 2: <strong>revise</strong> so every sentence fits the topic. Day 3: <strong>edit</strong> for capitals and periods with a checklist. Day 4: <strong>publish</strong> and write what they are most proud of.</p>
<p class="small">An example writer named Clara shows each step first.</p>
</section>

<section class="card">
<div class="card-head"><span class="ico">💬</span><h2>Ask at Home</h2></div>
<ol class="ask">
<li><span class="q">Why were castle walls so thick? Can you say it as a because sentence?</span><span class="listen">Listen for: because enemies attacked, or to stop arrows.</span></li>
<li><span class="q">What were the steps to becoming a knight?</span><span class="listen">Listen for: page, then squire, then knight.</span></li>
<li><span class="q">What does -ness do to a word? What does -ly do?</span><span class="listen">Listen for: -ness names a thing (kindness), -ly tells how (quickly).</span></li>
<li><span class="q">What is one thing stories about knights get right, and one thing they change?</span><span class="listen">Listen for: castles and kings were real; perfect, always-honorable knights were more of an ideal.</span></li>
</ol>
</section>

<div class="two">
<section class="card">
<div class="card-head"><span class="ico">📬</span><h2>What Gets Turned In</h2></div>
<ul class="check">
<li>Each lesson’s Assignment tab: the article questions and the day’s writing step, copied and pasted into Canvas</li>
<li>The Week 24 Check-In in Canvas</li>
</ul>
</section>
<section class="card">
<div class="card-head"><span class="ico">🏡</span><h2>Try at Home</h2></div>
<ul class="check">
<li>Play “stall keeper”: say a word like careful or softly, and your student says which ending it has and what it does</li>
<li>Read a paragraph from any book and find the main idea sentence together</li>
<li>Watch or read a story with knights and talk about what might really have been true</li>
</ul>
</section>
</div>

<section class="card">
<div class="card-head"><span class="ico">🎒</span><h2>Have on Hand</h2></div>
<ul class="check">
<li>Nothing extra: all four articles are on the lesson pages</li>
</ul>
</section>

<section class="card next">
<div class="card-head"><span class="ico">⏭️</span><h2>Coming Up in Week 25</h2></div>
<p><strong>A new novel: <em>The Lion, the Witch and the Wardrobe</em>.</strong> Chapters 1–3, when Lucy looks into a wardrobe. Reading skill: noticing how the author builds a fantasy world. Word study: tele-. Please have the book ready.</p>
</section>

<p class="foot">Optima Academy Online · 3rd Grade ELA · Week 24 Family Guide</p>
</div>
</body>
</html>
'''
io.open('parent-guide-week-24.html', 'w', encoding='utf-8').write(head + body)
print('ok')
