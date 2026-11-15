"""Week 26 family guide (unit guide is week 25's). Head/CSS and How the Lesson Pages Work from week 22 (a novel week with a
fluency page); bodies from the finished week 25 lessons, DATA and the S&S v4 rows 25-30. Run from the repo root."""
import io
s = io.open('parent-guide-week-22.html', encoding='utf-8').read()
H0 = s[:s.index('<body>')]
howto = s[s.index('<section class="howto">'):s.index('</section>', s.index('<section class="howto">')) + 10]
assert 'Fluency' in howto
OWL = 'https://raw.githubusercontent.com/optimaondemand/optima-assets/eeb0b335630058906d52f478028361d352253a93/images/Optima%20Final%20Circle%20-%20Owl%20Only.png'
ART = 'https://optimaondemand.github.io/optima-3rd-ela/assets/art/lww/'
def w(a, b): return '<div class="word"><b>%s</b><span>%s</span></div>' % (a, b)
WORDS = [('enchanted', 'under a magic spell; bewitched'), ('dominions', 'the lands ruled by someone'),
         ('wretched', 'very unhappy or miserable'), ('treachery', 'betraying someone’s trust in a serious way')]
UNIT = '<p class="unit-link"><a href="parent-guide-lww-unit.html">Read the unit guide for The Lion, the Witch and the Wardrobe →</a></p>'

week = H0.replace('Week 22 Family Guide · The Whipping Boy · 3rd Grade ELA', 'Week 26 Family Guide · The Lion, the Witch and the Wardrobe · 3rd Grade ELA')
assert 'Week 26 Family Guide' in week
week += '''<body>
<div class="wrap">

<header class="hero">
<div class="hero-text">
<div class="brand"><img src="''' + OWL + '''" alt="Optima Academy Online">Family Guide · 3rd Grade ELA</div>
<h1>Week 26: Edmund’s Choice</h1>
<div class="sub"><em>The Lion, the Witch and the Wardrobe</em>, Chapters 4–6: a choice and what it costs</div>
<div class="chips">
<span class="chip">4 lessons</span>
<span class="chip">Chapters 4–6</span>
<span class="chip">Fluency page</span>
<span class="chip">Check-In at week’s end</span>
</div>
<button class="print-btn" onclick="window.print()">🖨️ Print this guide</button>
''' + UNIT + '''
</div>
<div class="hero-art" style="background-image:url(\'''' + ART + '''lww-skaters.jpg');background-position:center 45%;" role="img" aria-label="A round old painting of skaters and sledges on a frozen river"></div>
</header>

''' + howto + '''

<section class="card">
<div class="card-head"><span class="ico">🧭</span><h2>This Week at a Glance</h2></div>
<p>In Chapter 4, Edmund rides on the Queen’s sledge and eats enchanted Turkish Delight. The more he eats, the more he wants, and he promises to bring his brother and sisters to her. Back home in Chapter 5, he tells Peter and Susan that Lucy’s story was only a game, and the Professor helps Peter and Susan think it through. In Chapter 6, all four children step into Narnia, find Mr. Tumnus’s cave broken and empty, and choose to go on. Day 1 reads Chapter 4, Day 2 Chapter 5, Day 3 Chapter 6, and Day 4 looks back at all three.</p>
<div class="glance">
<div class="box b-sky"><div class="box-label">Reading skill</div><strong>Choices and what they cost.</strong> Good readers find the moment a character decides something, and follow what happens because of it.</div>
<div class="box b-green"><div class="box-label">Big idea</div><strong>Why do people make choices they know are wrong?</strong> Is Edmund to blame, or the enchanted sweets?</div>
</div>
<p class="quote">“The more he ate the more he wanted to eat.”<small>Chapter 4</small></p>
</section>

<section class="card">
<div class="card-head"><span class="ico">📅</span><h2>Day by Day</h2></div>
<table class="days">
<thead><tr><th>Lesson</th><th>Reading</th><th>Big question</th></tr></thead>
<tbody>
<tr><td class="day-n">26.1<span>Day 1</span></td>
<td><span class="ch">Chapter 4: Turkish Delight</span><br>Your student names Edmund’s choices on the Queen’s sledge and what they lead to, then drafts a paragraph about a character’s choice.<br><span class="pill p-guide">Guide: Opti</span><span class="pill p-extra">Sentence rewrite</span></td>
<td>Why do people sometimes make choices they know are wrong?</td></tr>
<tr><td class="day-n">26.2<span>Day 2</span></td>
<td><span class="ch">Chapter 5: Back on This Side of the Door</span><br>Your student follows Edmund’s lie and what it costs Lucy, then adds connecting words like <em>because</em> to the paragraph.<br><span class="pill p-guide">Guide: Opti</span><span class="pill p-poem">Poetry</span><span class="pill p-extra">Read Like a Writer video</span></td>
<td>How do you recognize when a character’s choice is going to change the whole story?</td></tr>
<tr><td class="day-n">26.3<span>Day 3</span></td>
<td><span class="ch">Chapter 6: Into the Forest</span><br>Your student explains the children’s choice at Mr. Tumnus’s cave, then puts the whole paragraph together.<br><span class="pill p-guide">Guide: Opti</span><span class="pill p-extra">Read Like a Writer</span></td>
<td>What details in Ch. 6 show you that the children are committed to Narnia, with no turning back?</td></tr>
<tr><td class="day-n">26.4<span>Day 4</span></td>
<td><span class="ch">Look back: Chapters 4–6</span><br>Your student explains how Edmund’s choice leads to trouble, and polishes the paragraph with a stronger word.<br><span class="pill p-guide">Guide: Opti</span><span class="pill p-poem">Poetry</span><span class="pill p-extra">Read Like a Writer</span></td>
<td>What does Edmund’s choice in Ch. 4 show us about how consequences work in stories?</td></tr>
<tr class="extra-row"><td class="day-n">🎙️<span>Fluency</span></td>
<td colspan="2">Edmund on the Queen’s sledge in Chapter 4, eating Turkish Delight while she asks him questions. Your student reads it three times (right words, then smooth, then the long sentence in one smooth run), then <strong>records and submits in Canvas.</strong></td></tr>
<tr class="extra-row"><td class="day-n">📋<span>Check-In</span></td>
<td colspan="2">A 14-point check on the week, in Canvas: verb tense, the root form, beats in long words, a short passage from Chapter 4, and a short writing response.</td></tr>
</tbody>
</table>
</section>

<section class="card">
<div class="card-head"><span class="ico">🔤</span><h2>Words to Know</h2><span class="tag">Use them at home!</span></div>
<div class="words">
''' + '\n'.join(w(a, b) for a, b in WORDS) + '''
</div>
<div class="skills">
<div class="box b-sky"><div class="box-label">Word parts</div>The root <strong>form</strong> means <strong>shape</strong>.<span class="eg">form · uniform · reform · transform</span></div>
<div class="box b-gold"><div class="box-label">Spelling</div>Long school words are read in <strong>beats</strong>. Every beat has one vowel <strong>sound</strong>, so count sounds, not letters.<span class="eg">de·tail · ev·i·dence · in·for·ma·tion</span></div>
<div class="box b-green"><div class="box-label">Grammar</div><strong>Verb tense consistency:</strong> once a story starts in the past, every verb stays in the past.<span class="eg">Edmund sat on the sledge and ate the sweets.</span></div>
</div>
</section>

<section class="card">
<div class="card-head"><span class="ico">✨</span><h2>New in the Lessons</h2></div>
<div class="extras">
<div class="box b-plum"><div class="box-label">🍬 The Turkish Delight Box</div>This week’s word game is the Queen’s box of Turkish Delight. On Days 1 and 3 your student claps long school words and taps how many beats they have. On Days 2 and 4 they read a sentence and decide if its verbs stay in one time. Each right answer adds a sweet, and by Day 4 the box is full.</div>
<div class="box b-gold"><div class="box-label">🎬 Opti’s videos</div>Every Word Study activity, all four days, starts with a short video where Opti shows how it works. On Day 2, Opti also shows Read Like a Writer with a different sentence from Chapter 5. The videos have captions for now; Opti’s voice will be added later.</div>
<div class="box b-sky"><div class="box-label">🌍 World Notes</div>Each day opens the Reading tab with a real thing behind the story: Turkish delight (a real candy), old country houses that visitors come to see, robins in winter, and Arctic explorers.</div>
<div class="box b-green"><div class="box-label">🏮 Truth Watch</div>After reading, your student decides if three moments show someone being honest: Yes or Not yet. This week there is a lot to notice: Edmund’s secret, his lie, and the people who tell the truth.</div>
</div>
<p class="small" style="margin-top:12px;">Each day opens with a real painting, never pictures from the book: Hendrick Avercamp’s skaters on a frozen river (about 1608), John Constable’s English country house (1816), robins from a bird book (1837), and Ivan Shishkin’s lone snowy pine (1891). Your student looks first, then taps to learn about it.</p>
</section>

<section class="card">
<div class="card-head"><span class="ico">✍️</span><h2>Your Student’s Writing</h2><span class="tag">Writer’s Workshop</span></div>
<div class="essay"><span>Wk 25 · Describe a fantasy setting</span><span class="now">Wk 26 · Explain a character’s choice</span></div>
<p>This week’s literary response explains a character’s choice in three parts: the <strong>choice</strong>, the <strong>reason</strong>, and the <strong>consequence</strong>. Day 1: <strong>draft</strong> the paragraph. Day 2: <strong>revise</strong> with connecting words like <em>because</em> and <em>as a result</em>. Day 3: <strong>put it all together</strong> with an opening and a closing. Day 4: <strong>polish</strong> by swapping a weak word for a stronger one.</p>
<p class="small">An example writer named Clara shows each step first.</p>
</section>

<section class="card">
<div class="card-head"><span class="ico">💬</span><h2>Ask at Home</h2></div>
<ol class="ask">
<li><span class="q">What did Edmund promise the Queen, and why?</span><span class="listen">Listen for: to bring his brother and sisters, so he could have more Turkish Delight.</span></li>
<li><span class="q">What did Edmund say about Narnia when Peter asked? How did Lucy feel?</span><span class="listen">Listen for: that it was only a game; Lucy rushed out of the room.</span></li>
<li><span class="q">Is Edmund to blame, or the enchanted sweets?</span><span class="listen">Listen for: any answer with a reason from the book.</span></li>
<li><span class="q">Clap “information.” How many beats?</span><span class="listen">Listen for: four: in·for·ma·tion.</span></li>
</ol>
</section>

<div class="two">
<section class="card">
<div class="card-head"><span class="ico">📬</span><h2>What Gets Turned In</h2></div>
<ul class="check">
<li>Each lesson’s Assignment tab: the chapter questions and the day’s writing step, copied and pasted into Canvas</li>
<li>The Week 26 fluency recording</li>
<li>The Week 26 Check-In in Canvas</li>
</ul>
</section>
<section class="card">
<div class="card-head"><span class="ico">🏡</span><h2>Try at Home</h2></div>
<ul class="check">
<li>Tell what you did yesterday, and catch each other if a verb slips into “now”</li>
<li>Clap long words from a cereal box or a sign and count the beats</li>
<li>Talk about a time someone made a choice and something happened because of it</li>
</ul>
</section>
</div>

<section class="card">
<div class="card-head"><span class="ico">🎒</span><h2>Have on Hand</h2></div>
<ul class="check">
<li><em>The Lion, the Witch and the Wardrobe</em> by C.S. Lewis</li>
</ul>
</section>

<section class="card next">
<div class="card-head"><span class="ico">⏭️</span><h2>Coming Up in Week 27</h2></div>
<p><strong>Chapters 7–9.</strong> The children meet the Beavers. Reading skill: understanding different characters’ points of view. Word parts: <strong>in-</strong> and <strong>im-</strong>.</p>
</section>

<p class="foot">Optima Academy Online · 3rd Grade ELA · Week 26 Family Guide</p>
</div>
</body>
</html>
'''
io.open('parent-guide-week-26.html', 'w', encoding='utf-8').write(week)

print('ok')
