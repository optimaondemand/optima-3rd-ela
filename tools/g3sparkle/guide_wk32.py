"""Week 32 family guide (last week of the year; extension week, no unit guide, no fluency page). Head/CSS and How the Lesson
Pages Work from week 22 (fluency line removed), as week 31; bodies from the finished week 32 lessons and DATA. Run from the repo root."""
import io, re
s = io.open('parent-guide-week-22.html', encoding='utf-8').read()
H0 = s[:s.index('<body>')]
howto = s[s.index('<section class="howto">'):s.index('</section>', s.index('<section class="howto">')) + 10]
howto, n = re.subn(r'\s*<li><span>🎙️</span><strong>Fluency is a separate page</strong>.*?</li>', '', howto)
assert n == 1
OWL = 'https://raw.githubusercontent.com/optimaondemand/optima-assets/eeb0b335630058906d52f478028361d352253a93/images/Optima%20Final%20Circle%20-%20Owl%20Only.png'
ART = 'https://optimaondemand.github.io/optima-3rd-ela/assets/art/ext/'
def w(a, b): return '<div class="word"><b>%s</b><span>%s</span></div>' % (a, b)
WORDS = [('integrity', 'doing the right thing even when no one is watching'), ('empathy', 'understanding and sharing the feelings of another person'),
         ('resilience', 'the ability to keep going after something hard'), ('perseverance', 'continuing to try even when things are hard')]
week = H0.replace('Week 22 Family Guide · The Whipping Boy · 3rd Grade ELA', 'Week 32 Family Guide · The 7 Pillars of Virtue · 3rd Grade ELA')
assert 'Week 32 Family Guide' in week
week += '''<body>
<div class="wrap">

<header class="hero">
<div class="hero-text">
<div class="brand"><img src="''' + OWL + '''" alt="Optima Academy Online">Family Guide · 3rd Grade ELA</div>
<h1>Week 32: The 7 Pillars of Virtue</h1>
<div class="sub">The last week of 3rd grade ELA: one character, good character, and a year to celebrate</div>
<div class="chips">
<span class="chip">4 lessons</span>
<span class="chip">All four books</span>
<span class="chip">Check-In at week’s end</span>
</div>
<button class="print-btn" onclick="window.print()">🖨️ Print this guide</button>
</div>
<div class="hero-art" style="background-image:url(\'''' + ART + '''ext-parthenon-church.jpg');background-position:center 45%;" role="img" aria-label="A painting of an old stone temple with tall pillars"></div>
</header>

''' + howto + '''

<section class="card">
<div class="card-head"><span class="ico">🧭</span><h2>This Week at a Glance</h2></div>
<p>This is the last week of the year, and it is built to be lighter and fun: a reward for a year of hard work. Your student learns the <strong>7 Pillars of Virtue</strong> (honesty, respect, courtesy, responsibility, courage, service and perseverance), chooses one character from this year’s books (<em>Flat Stanley</em>, <em>The Tale of Despereaux</em>, <em>The Whipping Boy</em> or <em>The Lion, the Witch and the Wardrobe</em>), and writes a short response about <strong>two pillars</strong> that character shows. On Day 4 your student shares it out loud, looks back at the whole year, and saves a certificate.</p>
<div class="glance">
<div class="box b-sky"><div class="box-label">Reading skill</div><strong>Look back at how your reading has grown.</strong> Name one skill that was hard in the fall and is easy now.</div>
<div class="box b-green"><div class="box-label">Big idea</div><strong>What does it mean to have good character, and which character from our books best shows it?</strong></div>
</div>
<p class="quote">“But they can try.”<small>Mrs. Lambchop, <em>Flat Stanley</em></small></p>
</section>

<section class="card">
<div class="card-head"><span class="ico">📅</span><h2>Day by Day</h2></div>
<table class="days">
<thead><tr><th>Lesson</th><th>What your student does</th><th>Writing step</th></tr></thead>
<tbody>
<tr><td class="day-n">32.1<span>Day 1</span></td>
<td><span class="ch">Meet the 7 pillars</span><br>Reads each pillar with a real example from our books, chooses a character, and picks two pillars that character shows.<br><span class="pill p-guide">Guide: Opti</span><span class="pill p-extra">Sentence rewrite</span></td>
<td>Plan</td></tr>
<tr><td class="day-n">32.2<span>Day 2</span></td>
<td><span class="ch">Write the draft</span><br>Writes an opening (character, book, most important pillar) and two body paragraphs, one per pillar. Also a train poem by Robert Louis Stevenson.<br><span class="pill p-guide">Guide: Opti</span><span class="pill p-poem">Poetry</span><span class="pill p-extra">Read Like a Writer video</span></td>
<td>Draft</td></tr>
<tr><td class="day-n">32.3<span>Day 3</span></td>
<td><span class="ch">Make it stronger</span><br>Revises the opening and one paragraph, writes a closing, and gives out the Bookshelf Awards.<br><span class="pill p-guide">Guide: Opti</span><span class="pill p-extra">Bookshelf Awards</span><span class="pill p-extra">Read Like a Writer</span></td>
<td>Revise + notes for sharing</td></tr>
<tr><td class="day-n">32.4<span>Day 4</span></td>
<td><span class="ch">Share and celebrate</span><br>Finishes the response, shares it out loud, walks the Reading Road one last time, writes a short letter to a new 3rd grader, and saves a certificate.<br><span class="pill p-guide">Guide: Opti</span><span class="pill p-poem">Poetry</span><span class="pill p-extra">Certificate</span></td>
<td>Title + share</td></tr>
<tr class="extra-row"><td class="day-n">📋<span>Check-In</span></td>
<td colspan="2">A 14-point check in Canvas: editing rules, the week’s word parts and words, spelling rules, the 7 pillars, and the opening of a response.</td></tr>
</tbody>
</table>
</section>

<section class="card">
<div class="card-head"><span class="ico">🔤</span><h2>Words to Know</h2><span class="tag">Use them at home!</span></div>
<div class="words">
''' + '\n'.join(w(a, b) for a, b in WORDS) + '''
</div>
<div class="skills">
<div class="box b-sky"><div class="box-label">Word parts</div>The word parts inside the pillar words: <strong>-y</strong> (being), <strong>-ous</strong> (full of), <strong>-ance</strong>, and <strong>re-</strong>.<span class="eg">honest + y · courage + ous · persevere + ance</span></div>
<div class="box b-gold"><div class="box-label">Spelling</div>Find the <strong>base word</strong> first, then the rule: drop the silent e, double the last letter, change y to i, or add -es.<span class="eg">hope → hoping · hop → hopping · cry → cried · box → boxes</span></div>
<div class="box b-green"><div class="box-label">Grammar</div>A <strong>final editing review</strong>: capitals, apostrophes, commas in a list and before <em>and</em>, and irregular past forms.<span class="eg">lucy goed to narnia → Lucy went to Narnia</span></div>
</div>
</section>

<section class="card">
<div class="card-head"><span class="ico">✨</span><h2>New in the Lessons</h2></div>
<div class="extras">
<div class="box b-plum"><div class="box-label">🏛️ Raise the 7 Pillars</div>This week’s word game: every right answer raises the stone pillars of a temple a little more. Days 1 and 2: what a word with a prefix or suffix means. Days 3 and 4: which spelling rule a word used. On Day 4 the last pillar stands and the roof goes on.</div>
<div class="box b-gold"><div class="box-label">🏅 Bookshelf Awards</div>On Day 3 your student gives ribbons (Bravest, Most Honest, Kindest, Biggest Change) to characters from this year’s books. Each ribbon shows a real moment from the book.</div>
<div class="box b-green"><div class="box-label">🗺️ Reading Road look-back + certificate</div>On Day 4 Opti walks the year’s Reading Road, one book at a time, and your student picks a favorite book. Then your student picks the pillar to take to 4th grade and saves a “Story Map Explorer” certificate as a picture.</div>
<div class="box b-sky"><div class="box-label">🌍 World Notes + Pillar Watch</div>Each day opens with a real thing behind one of our books: the real Flat Stanley Project (1995), Prince Edward’s best friend Barnaby Fitzpatrick (stories say he was a whipping boy; historians have no proof), where the word courtesy comes from, and the real Lewis family wardrobe at Wheaton College. After reading, the Pillar Watch asks if three book moments show a pillar: Yes or Not yet.</div>
</div>
<p class="small" style="margin-top:12px;">Opti’s short Word Study videos are silent with captions for now. Each day opens with real art: Frederic Edwin Church’s <em>The Parthenon</em> (1871), Hans Holbein’s <em>Edward VI as a Child</em> (about 1538), Edmund Blair Leighton’s <em>God Speed!</em> (1900), and Jean-Honoré Fragonard’s <em>A Young Girl Reading</em> (about 1769).</p>
</section>

<section class="card">
<div class="card-head"><span class="ico">✍️</span><h2>Your Student’s Writing</h2><span class="tag">Writer’s Workshop</span></div>
<div class="essay"><span class="done">Wk 31 · Comparison response, published</span><span class="now">Wk 32 · Culmination response: one character and two pillars</span></div>
<p>The last piece of writing of the year is short on purpose: an <strong>opening</strong> with a claim (the character, the book, and the pillar that matters most), <strong>two body paragraphs</strong> (a pillar, a real example from the book, and what it shows), and a <strong>closing</strong>. The writing lives on the Reading tab, so nothing is written twice. On Day 4 your student gives it a title and <strong>shares it out loud</strong>: a 1-minute video for Canvas, or reading it to someone at home, with one picture or object to show.</p>
<p class="small">An example writer named Clara shows each step first, writing about Edmund.</p>
</section>

<section class="card">
<div class="card-head"><span class="ico">💬</span><h2>Ask at Home</h2></div>
<ol class="ask">
<li><span class="q">What are the 7 pillars? Which one is hardest for you?</span><span class="listen">Listen for: honesty, respect, courtesy, responsibility, courage, service, perseverance.</span></li>
<li><span class="q">Which character did you choose? Which two pillars do they show?</span><span class="listen">Listen for: a real moment from the book for each pillar.</span></li>
<li><span class="q">Who won your Bookshelf Awards?</span><span class="listen">Listen for: a reason, like Despereaux going into the dungeon or Lucy telling the truth about Narnia.</span></li>
<li><span class="q">What can you do as a reader now that was hard in the fall?</span><span class="listen">Listen for: one skill, and a time they used it on their own.</span></li>
</ol>
</section>

<div class="two">
<section class="card">
<div class="card-head"><span class="ico">📬</span><h2>What Gets Turned In</h2></div>
<ul class="check">
<li>Each lesson’s work, copied and pasted into Canvas</li>
<li>The finished response on Day 4, shared out loud (a 1-minute video or reading it at home)</li>
<li>The Week 32 Check-In in Canvas</li>
</ul>
</section>
<section class="card">
<div class="card-head"><span class="ico">🏡</span><h2>Try at Home</h2></div>
<ul class="check">
<li>Be the audience: listen to your student’s response and ask one question</li>
<li>Print or save the certificate and put it somewhere special</li>
<li>Make a summer reading list together, starting with a book your student would recommend</li>
</ul>
</section>
</div>

<section class="card next">
<div class="card-head"><span class="ico">🎉</span><h2>Coming Up</h2></div>
<p><strong>Summer, then 4th grade!</strong> Your student read four whole books this year. Keep reading together over the summer: a few pages a day keeps every skill from this year strong.</p>
</section>

<p class="foot">Optima Academy Online · 3rd Grade ELA · Week 32 Family Guide</p>
</div>
</body>
</html>
'''
io.open('parent-guide-week-32.html', 'w', encoding='utf-8').write(week)
print('ok')
