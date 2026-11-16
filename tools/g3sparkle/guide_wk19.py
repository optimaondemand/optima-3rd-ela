"""Week 19 family guide (The Whipping Boy, Ch. 6-11). It was never built when week 19 was sparkled (found in the Q3-Q4
audit, Nov 16 2026). Head/CSS and How the Lesson Pages Work from week 22 (keeps the fluency line: week 19 has a fluency page);
every line from the finished week 19 lessons, DATA, check-in JSON and claude/g3-ela-wk19 docs. Run from the repo root."""
import io, json
s = io.open('parent-guide-week-22.html', encoding='utf-8').read()
H0 = s[:s.index('<body>')]
howto = s[s.index('<section class="howto">'):s.index('</section>', s.index('<section class="howto">')) + 10]
OWL = 'https://raw.githubusercontent.com/optimaondemand/optima-assets/eeb0b335630058906d52f478028361d352253a93/images/Optima%20Final%20Circle%20-%20Owl%20Only.png'
ART = 'https://optimaondemand.github.io/optima-3rd-ela/assets/art/wb/'
def w(a, b): return '<div class="word"><b>%s</b><span>%s</span></div>' % (a, b)
WORDS = []
for d in (1, 2, 3, 4):
    for a, b in json.load(io.open('data/lesson-19-%d.json' % d, encoding='utf-8'))['notes']['vocab']:
        if a not in [x[0] for x in WORDS]: WORDS.append((a, b))
week = H0.replace('Week 22 Family Guide', 'Week 19 Family Guide')
assert 'Week 19 Family Guide' in week
week += '''<body>
<div class="wrap">

<header class="hero">
<div class="hero-text">
<div class="brand"><img src="''' + OWL + '''" alt="Optima Academy Online">Family Guide · 3rd Grade ELA</div>
<h1>Week 19: The Whipping Boy, Chapters 6–11</h1>
<div class="sub">Captured by outlaws: who can read, who is “the prince,” and why each boy does what he does</div>
<div class="chips">
<span class="chip">4 lessons + fluency</span>
<span class="chip">Chapters 6–11</span>
<span class="chip">Check-In at week’s end</span>
</div>
<button class="print-btn" onclick="window.print()">🖨️ Print this guide</button>
</div>
<div class="hero-art" style="background-image:url(\'''' + ART + '''wb-forest-hut.jpg');background-position:center 45%;" role="img" aria-label="A painting of a small wooden hut among tall pine trees"></div>
</header>

''' + howto + '''

<section class="card">
<div class="card-head"><span class="ico">🧭</span><h2>This Week at a Glance</h2></div>
<p>Prince Brat and Jemmy have run away from the castle, and the outlaws Hold-Your-Nose Billy and Cutwater have caught them. When the outlaws find out that Jemmy can read and write but the prince cannot, they decide Jemmy must be the prince. Jemmy plays along. This week your student keeps asking <strong>why</strong>: why each boy wants to get away, why Jemmy helps a prince who has been cruel to him, and why the prince refuses to go home when he has the chance.</p>
<div class="glance">
<div class="box b-sky"><div class="box-label">Reading skill</div><strong>Think about why characters do what they do:</strong> what each one wants, and what he does to get it.</div>
<div class="box b-green"><div class="box-label">Big idea</div><strong>Is Jemmy starting to change how he feels about the prince?</strong></div>
</div>
<p class="quote">“It’s not me you think you’re protecting, is it?”<small>Jemmy, <em>The Whipping Boy</em></small></p>
</section>

<section class="card">
<div class="card-head"><span class="ico">📅</span><h2>Day by Day</h2></div>
<table class="days">
<thead><tr><th>Lesson</th><th>Reading</th><th>Big question</th></tr></thead>
<tbody>
<tr><td class="day-n">19.1<span>Day 1</span></td>
<td><span class="ch">Chapters 6–7</span><br>The outlaws’ hut. Billy discovers that Jemmy can read and write, and decides Jemmy is the prince. Your student explains why each boy wanted to get away, and why Jemmy plays along.<br><span class="pill p-guide">Guide: Opti</span><span class="pill p-extra">Sentence rewrite</span></td>
<td>Jemmy can read and write but the prince cannot. How does knowing this change Jemmy’s situation with the outlaws?</td></tr>
<tr><td class="day-n">19.2<span>Day 2</span></td>
<td><span class="ch">Chapters 8–9</span><br>The ransom note. Jemmy tells Billy to ask for a whole wagonload of gold and jewels, and Billy makes him read the note backward. Also two short haiku.<br><span class="pill p-guide">Guide: Opti</span><span class="pill p-poem">Poetry</span><span class="pill p-extra">Read It Backward</span><span class="pill p-extra">Read Like a Writer video</span></td>
<td>Why does Jemmy try to help the prince even when the prince has been so cruel to him?</td></tr>
<tr><td class="day-n">19.3<span>Day 3</span></td>
<td><span class="ch">Chapters 10–11</span><br>The prince refuses to carry the ransom note back to the castle. When Billy goes to whip the prince, Jemmy steps in.<br><span class="pill p-guide">Guide: Opti</span></td>
<td>The prince refuses to go home even when he has the chance. What does this tell you about his real feelings?</td></tr>
<tr><td class="day-n">19.4<span>Day 4</span></td>
<td><span class="ch">Look back: Chapters 6–11</span><br>Your student compares each boy now with how he was in Chapter 1, and writes a full opinion paragraph. Also a chance to write a haiku.<br><span class="pill p-guide">Guide: Opti</span><span class="pill p-poem">Poetry</span></td>
<td>After reading Chapters 6–11, is Jemmy starting to change how he feels about the prince?</td></tr>
<tr class="extra-row"><td class="day-n">🎙️<span>Fluency</span></td>
<td colspan="2">A short passage from Chapter 11, read out loud three times to build smooth, expressive reading.</td></tr>
<tr class="extra-row"><td class="day-n">📋<span>Check-In</span></td>
<td colspan="2">A 14-point check in Canvas: compound sentences, the root <em>port</em>, consonant-le syllables, a passage from the book, and opinion writing.</td></tr>
</tbody>
</table>
</section>

<section class="card">
<div class="card-head"><span class="ico">🔤</span><h2>Words to Know</h2><span class="tag">Use them at home!</span></div>
<div class="words">
''' + '\n'.join(w(a, b) for a, b in WORDS) + '''
</div>
<div class="skills">
<div class="box b-sky"><div class="box-label">Word parts</div>The root <strong>port</strong> means “carry.”<span class="eg">transport · import · export · report · portable</span></div>
<div class="box b-gold"><div class="box-label">Spelling</div><strong>Consonant-le syllables</strong>: the consonant before <em>-le</em> joins it to make the last syllable.<span class="eg">ta·ble · can·dle · sim·ple</span></div>
<div class="box b-green"><div class="box-label">Grammar</div><strong>Compound sentences</strong> join two complete thoughts with a comma and a joining word.<span class="eg">Jemmy wrote the note, and Billy watched.</span></div>
</div>
</section>

<section class="card">
<div class="card-head"><span class="ico">✨</span><h2>New in the Lessons</h2></div>
<div class="extras">
<div class="box b-plum"><div class="box-label">💰 Fill the Wagon</div>This week’s word game is the outlaws’ wagon. In Chapter 8, Jemmy tells Billy to ask the king for a whole wagonload of gold and jewels. Your student sorts one thing at a time into the right sack, and every right answer drops a coin or a jewel into the wagon. Day 1: what a <em>port</em> word means. Day 2: is it a compound sentence? Day 3: does it end in consonant-le? Day 4: all three. By Day 4 the wagon is full.</div>
<div class="box b-gold"><div class="box-label">🔄 Read It Backward</div>On Day 2, your student tries Billy’s test from Chapter 9: Billy makes Jemmy read the ransom note backward, from the last word to the first. Your student reads three short notes backward out loud, then puts the words in the right order.</div>
<div class="box b-sky"><div class="box-label">🎬 Opti’s videos</div>Every Word Study activity starts with a short video where Opti, the owl guide, shows how it works. On Day 2, Opti also shows Read Like a Writer with a different sentence from the book.</div>
<div class="box b-green"><div class="box-label">🦁 Courage Watch</div>After reading, your student decides if three moments from the chapters show courage: Yes or Not yet.</div>
</div>
<p class="small" style="margin-top:12px;">Each day opens with real art: Ivan Shishkin’s hut in a forest, a 1400s painting of the scribe Jean Miélot at his desk, George Stubbs’s horse <em>Whistlejacket</em> (about 1762), and Johann Adam Delsenbach’s Imperial Crown (1751).</p>
</section>

<section class="card">
<div class="card-head"><span class="ico">✍️</span><h2>Your Student’s Opinion Writing</h2><span class="tag">Writer’s Workshop</span></div>
<div class="essay"><span class="done">Wk 18 · Choose a claim</span><span class="now">Wk 19 · Add reasons</span><span>Wk 20 · Draft</span><span>Wk 21 · Revise &amp; publish</span><span>Wk 22 · Compare &amp; present</span></div>
<p>Your student is building an <strong>opinion paragraph</strong> about a character in <em>The Whipping Boy</em>. Day 1: think about <strong>the other side</strong> (what would someone who disagrees say?). Day 2: read the draft aloud to see if it <strong>flows</strong>. Day 3: write a <strong>conclusion sentence</strong>. Day 4: write the <strong>whole paragraph</strong> with all five parts: claim, reason, example, the other side, and conclusion.</p>
<p class="small">An example writer named Clara shows each step first. Her claim: Prince Brat is the most unfair character, because he uses his power to hurt others.</p>
</section>

<section class="card">
<div class="card-head"><span class="ico">💬</span><h2>Ask at Home</h2></div>
<ol class="ask">
<li><span class="q">Why does Billy think Jemmy is the prince?</span><span class="listen">Listen for: Jemmy can read and write, and the real prince can’t.</span></li>
<li><span class="q">Why does Jemmy play along?</span><span class="listen">Listen for: a reason from the book, in your student’s own words.</span></li>
<li><span class="q">Why does Jemmy want a whole wagonload of gold and jewels?</span><span class="listen">Listen for: what your student thinks Jemmy is planning, with a detail from Chapter 8.</span></li>
<li><span class="q">Is Jemmy starting to feel differently about the prince? How can you tell?</span><span class="listen">Listen for: an action, like Jemmy stepping in when Billy goes to whip the prince.</span></li>
</ol>
</section>

<div class="two">
<section class="card">
<div class="card-head"><span class="ico">📬</span><h2>What Gets Turned In</h2></div>
<ul class="check">
<li>Each lesson’s work, copied and pasted into Canvas</li>
<li>The fluency recording</li>
<li>The Week 19 Check-In in Canvas</li>
</ul>
</section>
<section class="card">
<div class="card-head"><span class="ico">🏡</span><h2>Try at Home</h2></div>
<ul class="check">
<li>Write a short note and read it to each other backward, the way Billy tested Jemmy</li>
<li>Hunt for <em>port</em> words on signs and labels: transport, airport, report</li>
<li>Clap the syllables in candle, table and bubble</li>
</ul>
</section>
</div>

<section class="card">
<div class="card-head"><span class="ico">🎒</span><h2>Have on Hand</h2></div>
<ul class="check">
<li>A copy of <em>The Whipping Boy</em> by Sid Fleischman</li>
<li>A device that can record for the fluency page</li>
</ul>
</section>

<section class="card next">
<div class="card-head"><span class="ico">⏭️</span><h2>Coming Up in Week 20</h2></div>
<p><strong>Chapters 11–15.</strong> Jemmy and the prince try to get away from the outlaws.</p>
</section>

<p class="foot">Optima Academy Online · 3rd Grade ELA · Week 19 Family Guide · <a href="parent-guide-wb-unit.html">The Whipping Boy unit guide</a></p>
</div>
</body>
</html>
'''
io.open('parent-guide-week-19.html', 'w', encoding='utf-8').write(week)
print('ok')
