"""Week 31 family guide (extension week, no unit guide, no fluency page). Head/CSS and How the Lesson Pages Work from week 22
(fluency line removed); bodies from the finished week 31 lessons, DATA and the S&S v4 rows 31-32. Run from the repo root."""
import io, re
s = io.open('parent-guide-week-22.html', encoding='utf-8').read()
H0 = s[:s.index('<body>')]
howto = s[s.index('<section class="howto">'):s.index('</section>', s.index('<section class="howto">')) + 10]
howto, n = re.subn(r'\s*<li><span>🎙️</span><strong>Fluency is a separate page</strong>.*?</li>', '', howto)
assert n == 1
OWL = 'https://raw.githubusercontent.com/optimaondemand/optima-assets/eeb0b335630058906d52f478028361d352253a93/images/Optima%20Final%20Circle%20-%20Owl%20Only.png'
ART = 'https://optimaondemand.github.io/optima-3rd-ela/assets/art/ext/'
def w(a, b): return '<div class="word"><b>%s</b><span>%s</span></div>' % (a, b)
WORDS = [('courageous', 'having or showing courage; willing to act even when afraid'), ('perseverance', 'continuing to try even when things are hard'),
         ('virtue', 'a quality that shows good character'), ('integrity', 'doing the right thing even when no one is watching')]

week = H0.replace('Week 22 Family Guide · The Whipping Boy · 3rd Grade ELA', 'Week 31 Family Guide · Paired Texts: The Courage to Act · 3rd Grade ELA')
assert 'Week 31 Family Guide' in week
week += '''<body>
<div class="wrap">

<header class="hero">
<div class="hero-text">
<div class="brand"><img src="''' + OWL + '''" alt="Optima Academy Online">Family Guide · 3rd Grade ELA</div>
<h1>Week 31: The Courage to Act</h1>
<div class="sub">Two texts about courage: comparing how two authors write about the same topic</div>
<div class="chips">
<span class="chip">4 lessons</span>
<span class="chip">Text 1 + Text 2</span>
<span class="chip">Check-In at week’s end</span>
</div>
<button class="print-btn" onclick="window.print()">🖨️ Print this guide</button>
</div>
<div class="hero-art" style="background-image:url(\'''' + ART + '''ext-darling-rescue-parker.jpg');background-position:center 55%;" role="img" aria-label="A painting of two people rowing a small boat through stormy waves"></div>
</header>

''' + howto + '''

<section class="card">
<div class="card-head"><span class="ico">🧭</span><h2>This Week at a Glance</h2></div>
<p>The novels are finished, and this is an extension week. Your student reads two short texts about courage, both written for Optima Academy Online. <strong>Text 1, “What Is Courage?”</strong> is informational: it explains that courage is not the same as having no fear, but choosing to act anyway because it matters. <strong>Text 2, “The Choice at the Bridge,”</strong> is a made-up story about a girl named Mira who stands up for a smaller boy on an old, narrow bridge, even though she is scared. All week your student compares how the two authors write about the same topic, and builds a comparison response.</p>
<div class="glance">
<div class="box b-sky"><div class="box-label">Reading skill</div><strong>Compare how two authors write about the same topic.</strong> One text explains courage with facts and ideas. The other shows it through a character’s actions.</div>
<div class="box b-green"><div class="box-label">Big idea</div><strong>What does it mean to be truly courageous?</strong> On Day 4, your student thinks back over every book read this year.</div>
</div>
<p class="quote">“I just decided that he mattered more than my fear did.”<small>Mira, Text 2</small></p>
</section>

<section class="card">
<div class="card-head"><span class="ico">📅</span><h2>Day by Day</h2></div>
<table class="days">
<thead><tr><th>Lesson</th><th>Reading</th><th>Big question</th></tr></thead>
<tbody>
<tr><td class="day-n">31.1<span>Day 1</span></td>
<td><span class="ch">Text 1: What Is Courage?</span><br>Your student explains what Text 1 says courage is, finds a big moment and a quiet moment of courage in the text, and picks a character from this year’s books who fits. Then plans the comparison and writes a claim.<br><span class="pill p-guide">Guide: Opti</span><span class="pill p-extra">Sentence rewrite</span></td>
<td>What does it mean to be truly courageous?</td></tr>
<tr><td class="day-n">31.2<span>Day 2</span></td>
<td><span class="ch">Text 2: The Choice at the Bridge</span><br>Your student finds how the author shows Mira’s courage without using the word brave, compares Mira with Text 1, and drafts the opening of the comparison. Also a short poem by Amy Lowell.<br><span class="pill p-guide">Guide: Opti</span><span class="pill p-poem">Poetry</span><span class="pill p-extra">Read Like a Writer video</span></td>
<td>How does a fiction author show courage differently from the way an informational author explains it?</td></tr>
<tr><td class="day-n">31.3<span>Day 3</span></td>
<td><span class="ch">Look back: both texts</span><br>Your student collects the best detail from each text and drafts one paragraph about each.<br><span class="pill p-guide">Guide: Opti</span><span class="pill p-extra">Read Like a Writer</span></td>
<td>How do you use details from two different texts in the same response?</td></tr>
<tr><td class="day-n">31.4<span>Day 4</span></td>
<td><span class="ch">Look back: both texts</span><br>Your student writes the closing, finishes the comparison response, picks the character from this year who showed the most courage, and talks it over with someone at home.<br><span class="pill p-guide">Guide: Opti</span><span class="pill p-poem">Poetry</span><span class="pill p-extra">Read Like a Writer</span></td>
<td>After a whole year of reading, what do you think courage really means?</td></tr>
<tr class="extra-row"><td class="day-n">📋<span>Check-In</span></td>
<td colspan="2">A 14-point check on the week, in Canvas: grammar from the whole year, prefixes and suffixes, splitting long words into syllables, a short passage from Text 1, and a comparison of the two texts.</td></tr>
</tbody>
</table>
</section>

<section class="card">
<div class="card-head"><span class="ico">🔤</span><h2>Words to Know</h2><span class="tag">Use them at home!</span></div>
<div class="words">
''' + '\n'.join(w(a, b) for a, b in WORDS) + '''
</div>
<div class="skills">
<div class="box b-sky"><div class="box-label">Word parts</div>A review of this year’s <strong>prefixes and suffixes</strong>: re- (again), un- (not), trans- (across), inter- (between), -ful (full of), -less (without).<span class="eg">rebuild · unkind · hopeful · endless</span></div>
<div class="box b-gold"><div class="box-label">Spelling</div><strong>Long words</strong>: find the vowels, split between them, read each chunk, then push the chunks together.<span class="eg">in·vi·ta·tion · dis·cov·er·y</span></div>
<div class="box b-green"><div class="box-label">Grammar</div>A <strong>review of the whole year</strong>: capitals, commas after an opening part, apostrophes, irregular past forms, and simple, compound and complex sentences.<span class="eg">although mira was scared she goed → Although Mira was scared, she went</span></div>
</div>
</section>

<section class="card">
<div class="card-head"><span class="ico">✨</span><h2>New in the Lessons</h2></div>
<div class="extras">
<div class="box b-plum"><div class="box-label">🚣 Row to the Wreck</div>This week’s word game follows a real rescue. Each right answer is one pull on the oars as Grace Darling and her father row through the storm to a wrecked ship. On Days 1 and 2 your student picks what a word with a prefix or suffix means. On Days 3 and 4 your student counts the beats (syllables) in long words. By Day 4 the boat reaches the wreck.</div>
<div class="box b-gold"><div class="box-label">🎬 Opti’s videos</div>Every Word Study activity, all four days, starts with a short video where Opti shows how it works. On Day 2, Opti also shows Read Like a Writer with a different sentence from Text 2. The videos are silent with captions for now.</div>
<div class="box b-sky"><div class="box-label">🌍 World Notes</div>Each day opens the Reading tab with a real story of courage: Grace Darling, who in 1838, at age 22, rowed with her father from the Longstone Lighthouse to save nine people from a shipwreck; how a lighthouse works; rowing through rough water; and the stone monument in Bamburgh, England, that shows her holding an oar.</div>
<div class="box b-green"><div class="box-label">🦁 Courage Watch</div>After reading, your student decides if three moments show someone being brave: Yes or Not yet. For example: Mira walks onto the bridge even though her feet want to turn around (Yes), or someone who is never scared of anything (Not yet: Text 1 says brave people feel fear and act anyway).</div>
</div>
<p class="small" style="margin-top:12px;">Each day opens with real art: Thomas Musgrave Joy’s portrait of Grace Darling (1839), Camille Corot’s painting of the old bridge at Narni in Italy (1827), Peder Balke’s lighthouse on the coast of Norway (about 1855), and Henry Perlee Parker’s painting of Grace and her father rowing to the rescue.</p>
</section>

<section class="card">
<div class="card-head"><span class="ico">✍️</span><h2>Your Student’s Writing</h2><span class="tag">Writer’s Workshop</span></div>
<div class="essay"><span class="done">Wk 30 · Literary response, published</span><span class="now">Wk 31 · A comparison response: two texts on courage</span><span>Wk 32 · Year-end</span></div>
<p>This week your student writes a <strong>comparison response</strong>. Day 1: <strong>plan</strong> what Text 1 says courage is, a character who shows it, and a claim. Day 2: draft the <strong>opening</strong>, naming both texts and what they agree on. Day 3: draft <strong>one paragraph for each text</strong>, plus a sentence that connects them. Day 4: write the <strong>closing</strong> and put the whole response together.</p>
<p class="small">An example writer named Clara shows each step first.</p>
</section>

<section class="card">
<div class="card-head"><span class="ico">💬</span><h2>Ask at Home</h2></div>
<ol class="ask">
<li><span class="q">What does Text 1 say courage is?</span><span class="listen">Listen for: not having no fear, but choosing to act anyway because it is important or right; something you practice, one choice at a time.</span></li>
<li><span class="q">How does the author show that Mira is scared, without using the word scared?</span><span class="listen">Listen for: her heart hammered, her feet wanted to turn around, she took a breath.</span></li>
<li><span class="q">How are the two texts alike? How are they different?</span><span class="listen">Listen for: both say courage means acting even when afraid; one explains it, the other shows it in a story.</span></li>
<li><span class="q">Which character from this year’s books showed the most courage?</span><span class="listen">Listen for: a character and one thing they did, like Despereaux going into the dungeon or Lucy telling the truth about Narnia.</span></li>
</ol>
</section>

<div class="two">
<section class="card">
<div class="card-head"><span class="ico">📬</span><h2>What Gets Turned In</h2></div>
<ul class="check">
<li>Each lesson’s Assignment tab: the reading questions and the day’s writing step, copied and pasted into Canvas</li>
<li>The finished comparison response on Day 4</li>
<li>The Week 31 Check-In in Canvas</li>
</ul>
</section>
<section class="card">
<div class="card-head"><span class="ico">🏡</span><h2>Try at Home</h2></div>
<ul class="check">
<li>Share a time you did something brave while you were scared</li>
<li>Read Text 2 aloud together and point to every sentence that shows fear without saying it</li>
<li>Look up a photo of a lighthouse near you, or one you have visited</li>
</ul>
</section>
</div>

<section class="card next">
<div class="card-head"><span class="ico">⏭️</span><h2>Coming Up in Week 32</h2></div>
<p><strong>The last week of the year.</strong> Your student looks back at the books read this year and the seven pillars of virtue, then writes, revises and shares a year-end response.</p>
</section>

<p class="foot">Optima Academy Online · 3rd Grade ELA · Week 31 Family Guide</p>
</div>
</body>
</html>
'''
io.open('parent-guide-week-31.html', 'w', encoding='utf-8').write(week)
print('ok')
