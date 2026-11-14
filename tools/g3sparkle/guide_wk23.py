"""Week 23 family guide: week 22's guide (head/CSS) with a new body. Every line from the finished week 23 lessons and DATA."""
import io
s = io.open('parent-guide-week-22.html', encoding='utf-8').read()
head = s[:s.index('<body>')].replace('Week 22 Family Guide · The Whipping Boy · 3rd Grade ELA', 'Week 23 Family Guide · Medieval Nonfiction · 3rd Grade ELA')
assert 'Week 23 Family Guide' in head
howto = s[s.index('<section class="howto">'):s.index('</section>', s.index('<section class="howto">')) + 10]
howto = howto.replace('<li><span>🎙️</span><strong>Fluency is a separate page</strong> in the Canvas module, because recording doesn’t work inside a lesson. Keep the novel nearby.</li>\n', '')
assert 'Fluency' not in howto
def w(a, b): return '<div class="word"><b>%s</b><span>%s</span></div>' % (a, b)
WORDS = [('fortress','a large, strong building built to resist attack'),('keep','the strongest, innermost tower of a castle'),('servant','a person who works in someone else’s household'),('page','a young boy in training at a noble household, learning to become a knight'),
 ('apprentice','a person learning a trade by working under an expert'),('craftsman','a skilled worker who makes things by hand'),('pottage','a thick soup of vegetables and grains'),('embroider','to decorate cloth with needle and thread'),
 ('protocol','official rules for how to behave in formal situations'),('rank','a person’s position or level of importance'),('noble','a person of high birth, below a king or queen'),('courteous','polite, respectful and well-mannered'),
 ('feast','a large, fancy meal for a celebration'),('coarse','rough in texture'),('pewter','a dull grey metal used for plates and cups')]
body = '''<body>
<div class="wrap">

<header class="hero">
<div class="hero-text">
<div class="brand"><img src="https://raw.githubusercontent.com/optimaondemand/optima-assets/eeb0b335630058906d52f478028361d352253a93/images/Optima%20Final%20Circle%20-%20Owl%20Only.png" alt="Optima Academy Online">Family Guide · 3rd Grade ELA</div>
<h1>Week 23: Illuminate the Page</h1>
<div class="sub">Medieval Nonfiction: four true articles about life in the Middle Ages</div>
<div class="chips">
<span class="chip">4 lessons</span>
<span class="chip">4 short articles</span>
<span class="chip">No novel this week</span>
<span class="chip">Check-In at week’s end</span>
</div>
<button class="print-btn" onclick="window.print()">🖨️ Print this guide</button>
</div>
<div class="hero-art" style="background-image:url('https://optimaondemand.github.io/optima-3rd-ela/assets/art/med/med-sept.jpg');background-position:center 30%;" role="img" aria-label="An old painting of a tall white castle on a hill above a grape harvest"></div>
</header>

''' + howto + '''

<section class="card">
<div class="card-head"><span class="ico">🧭</span><h2>This Week at a Glance</h2></div>
<p>Your student just finished <em>The Whipping Boy</em>, a made-up story set long ago. This week and next, your student reads true articles about real life in the Middle Ages. Each lesson has one short article, right on the page, so there is no book to have nearby. Day 1 visits a castle. Day 2 is about how children learned a job by working. Day 3 explains the strict rules of a royal court. Day 4 compares what rich and poor people ate.</p>
<div class="glance">
<div class="box b-sky"><div class="box-label">Reading skill</div><strong>Central idea.</strong> The central idea is the most important point an author makes. A detail is one fact that helps prove it.</div>
<div class="box b-green"><div class="box-label">Big idea</div><strong>Real life long ago.</strong> What was it really like to live in a castle, learn a trade, or sit at a king’s table?</div>
</div>
<p class="quote">“A medieval castle was not just a home — it was a fortress, a workplace, and a whole community.”<small>Life in a Medieval Castle, Day 1</small></p>
</section>

<section class="card">
<div class="card-head"><span class="ico">📅</span><h2>Day by Day</h2></div>
<table class="days">
<thead><tr><th>Lesson</th><th>Reading</th><th>Big question</th></tr></thead>
<tbody>
<tr>
<td class="day-n">23.1<span>Day 1</span></td>
<td><span class="ch">Life in a Medieval Castle</span><br>Your student finds the central idea of the article and two details that prove it, then picks a medieval topic to write about.<br><span class="pill p-guide">Guide: Opti</span><span class="pill p-extra">Sentence rewrite</span></td>
<td>You just read about Prince Brat living in a castle. What do you think it was actually like to live in one?</td>
</tr>
<tr>
<td class="day-n">23.2<span>Day 2</span></td>
<td><span class="ch">Servants and Apprentices</span><br>Your student finds the central idea of each paragraph and compares how boys and girls learned to work.<br><span class="pill p-guide">Guide: Opti</span><span class="pill p-poem">Poetry</span><span class="pill p-extra">Read Like a Writer video</span></td>
<td>If you lived in medieval times, what job do you think you would have? What would you learn, and how?</td>
</tr>
<tr>
<td class="day-n">23.3<span>Day 3</span></td>
<td><span class="ch">Royal Courts: Power and Protocol</span><br>Your student explains the central idea and why the author wrote the article.<br><span class="pill p-guide">Guide: Opti</span><span class="pill p-extra">Read Like a Writer</span></td>
<td>In The Whipping Boy, the prince can do whatever he wants without punishment. Today’s article might explain why. What do you predict?</td>
</tr>
<tr>
<td class="day-n">23.4<span>Day 4</span></td>
<td><span class="ch">What Did Medieval People Eat?</span><br>Your student compares what the rich and the poor ate, using details from the article.<br><span class="pill p-guide">Guide: Opti</span><span class="pill p-poem">Poetry</span><span class="pill p-extra">Read Like a Writer</span></td>
<td>In The Whipping Boy, the prince runs away with a basket of food from the king’s table. What do you remember was inside?</td>
</tr>
<tr class="extra-row">
<td class="day-n">📋<span>Check-In</span></td>
<td colspan="2">A 14-point check on the week, in Canvas: capital letters, the word part trans, splitting VCCV words, the Day 1 castle article, and a short writing response.</td>
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
<div class="box b-sky"><div class="box-label">Word parts</div>The word part <strong>trans</strong> means <strong>across</strong>. Careful: some words only start with t-r-a-n, like tranquil (calm).<span class="eg">transport · transform · translate · transfer</span></div>
<div class="box b-gold"><div class="box-label">Spelling</div><strong>VCCV</strong> means vowel, consonant, consonant, vowel. Split the word between the two consonants.<span class="eg">bas · ket · tun · nel · nap · kin</span></div>
<div class="box b-green"><div class="box-label">Grammar</div>Names of people, places and titles get <strong>capital letters</strong>. Small words like the, of and in stay small inside a name or title, unless they come first.<span class="eg">Queen Eleanor lived near the Tower of London.</span></div>
</div>
</section>

<section class="card">
<div class="card-head"><span class="ico">✨</span><h2>New in the Lessons</h2></div>
<div class="extras">
<div class="box b-plum"><div class="box-label">🖌️ Illuminate the Page</div>This week’s word game. Long ago, books were written and painted by hand. Each right answer paints one part of a medieval book page: the big gold capital letter on Day 1, the border on Day 2, a little castle picture on Day 3, and the lines of writing on Day 4.</div>
<div class="box b-gold"><div class="box-label">🎬 Opti’s videos</div>Every Word Study activity, all four days, starts with a short video where Opti shows how it works. On Day 2, Opti also shows how to do Read Like a Writer with a different sentence from the article.</div>
<div class="box b-sky"><div class="box-label">⭐ Job Spotlight</div>Each day opens the Reading tab with a real medieval job: a page, an apprentice, a herald, and a castle cook.</div>
<div class="box b-green"><div class="box-label">🏮 Diligence Watch</div>After reading, your student decides if three facts from the article show someone working hard: Yes or Not yet. Diligence means working hard and carefully.</div>
</div>
<p class="small" style="margin-top:12px;">Each day opens with a real painting from the Middle Ages: a French castle above a grape harvest, a baker at his oven in Nuremberg, a king’s feast in Paris in 1378, and an English lord at dinner. Your student looks first, then taps to learn about it.</p>
</section>

<section class="card">
<div class="card-head"><span class="ico">✍️</span><h2>Your Student’s Writing</h2><span class="tag">Writer’s Workshop</span></div>
<div class="essay"><span class="now">Wk 23 · Choose &amp; take notes</span><span>Wk 24 · Draft, revise &amp; publish</span></div>
<p>This week your student starts an informational paragraph about one part of medieval life. Day 1: <strong>choose a topic</strong> that is not too big. Day 2: write a <strong>research question</strong> and take notes from <strong>two articles</strong>. Day 3: <strong>plan the paragraph</strong> (topic sentence, two details, closing). Day 4: <strong>write the topic sentence</strong> and at least one detail. Week 24 finishes it.</p>
<p class="small">An example writer named Clara shows each step first.</p>
</section>

<section class="card">
<div class="card-head"><span class="ico">💬</span><h2>Ask at Home</h2></div>
<ol class="ask">
<li><span class="q">What was the central idea of today’s article? What is one detail that proves it?</span><span class="listen">Listen for: one big point, not just a fact, and a fact that backs it up.</span></li>
<li><span class="q">How did children learn a job in the Middle Ages?</span><span class="listen">Listen for: by working, often as an apprentice to a master.</span></li>
<li><span class="q">What does trans mean? Can you name a word with it?</span><span class="listen">Listen for: across, and a word like transport or translate.</span></li>
<li><span class="q">What topic are you writing about? What is your research question?</span><span class="listen">Listen for: one small part of medieval life, and a question that starts with What, How or Why.</span></li>
</ol>
</section>

<div class="two">
<section class="card">
<div class="card-head"><span class="ico">📬</span><h2>What Gets Turned In</h2></div>
<ul class="check">
<li>Each lesson’s Assignment tab: the article questions and the day’s writing step, copied and pasted into Canvas</li>
<li>The Week 23 Check-In in Canvas</li>
</ul>
</section>
<section class="card">
<div class="card-head"><span class="ico">🏡</span><h2>Try at Home</h2></div>
<ul class="check">
<li>Make up silly hyperbole together: “I’m so hungry I could eat a castle!”</li>
<li>Look at a book cover or street sign and find the words with capital letters</li>
<li>Talk about a job your family knows. How did someone learn it?</li>
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
<div class="card-head"><span class="ico">⏭️</span><h2>Coming Up in Week 24</h2></div>
<p><strong>More medieval nonfiction.</strong> How castles were built, knights, busy medieval towns, and the Middle Ages in stories. Word study: the root script/scribe (write). Your student finishes the informational paragraph.</p>
</section>

<p class="foot">Optima Academy Online · 3rd Grade ELA · Week 23 Family Guide</p>
</div>
</body>
</html>
'''
io.open('parent-guide-week-23.html', 'w', encoding='utf-8').write(head + body)
print('ok')
