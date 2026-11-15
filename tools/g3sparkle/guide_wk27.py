"""Week 27 family guide (unit guide is week 25's). Head/CSS and How the Lesson Pages Work from week 22 (a novel week with a
fluency page); bodies from the finished week 27 lessons, DATA and the S&S v4 rows 25-30. Run from the repo root."""
import io
s = io.open('parent-guide-week-22.html', encoding='utf-8').read()
H0 = s[:s.index('<body>')]
howto = s[s.index('<section class="howto">'):s.index('</section>', s.index('<section class="howto">')) + 10]
assert 'Fluency' in howto
OWL = 'https://raw.githubusercontent.com/optimaondemand/optima-assets/eeb0b335630058906d52f478028361d352253a93/images/Optima%20Final%20Circle%20-%20Owl%20Only.png'
ART = 'https://optimaondemand.github.io/optima-3rd-ela/assets/art/lww/'
def w(a, b): return '<div class="word"><b>%s</b><span>%s</span></div>' % (a, b)
WORDS = [('authority', 'the right or power to give orders and make decisions'), ('prophecy', 'a statement that something will happen in the future'),
         ('betray', 'to be disloyal to someone who trusted you'), ('treachery', 'betraying someone’s trust in a very serious way')]
UNIT = '<p class="unit-link"><a href="parent-guide-lww-unit.html">Read the unit guide for The Lion, the Witch and the Wardrobe →</a></p>'

week = H0.replace('Week 22 Family Guide · The Whipping Boy · 3rd Grade ELA', 'Week 27 Family Guide · The Lion, the Witch and the Wardrobe · 3rd Grade ELA')
assert 'Week 27 Family Guide' in week
week += '''<body>
<div class="wrap">

<header class="hero">
<div class="hero-text">
<div class="brand"><img src="''' + OWL + '''" alt="Optima Academy Online">Family Guide · 3rd Grade ELA</div>
<h1>Week 27: Two Sides of One Name</h1>
<div class="sub"><em>The Lion, the Witch and the Wardrobe</em>, Chapters 7–9: how different characters see the same thing</div>
<div class="chips">
<span class="chip">4 lessons</span>
<span class="chip">Chapters 7–9</span>
<span class="chip">Fluency page</span>
<span class="chip">Check-In at week’s end</span>
</div>
<button class="print-btn" onclick="window.print()">🖨️ Print this guide</button>
''' + UNIT + '''
</div>
<div class="hero-art" style="background-image:url(\'''' + ART + '''lww-bird-trap.jpg');background-position:center 60%;" role="img" aria-label="An old painting of a snowy village beside a frozen river, with people skating on the ice"></div>
</header>

''' + howto + '''

<section class="card">
<div class="card-head"><span class="ico">🧭</span><h2>This Week at a Glance</h2></div>
<p>In Chapter 7, a beaver leads the children through the snowy wood to his house on a dam, and whispers a name: Aslan. Each child feels something different when they hear it. In Chapter 8, after dinner, Mr. Beaver tells them about Aslan and an old prophecy about four thrones, and then they find that Edmund has slipped away. Chapter 9 follows Edmund alone through the snow to the White Witch’s castle, full of stone statues. Day 1 reads Chapter 7, Day 2 Chapter 8, Day 3 Chapter 9, and Day 4 looks back at all three.</p>
<div class="glance">
<div class="box b-sky"><div class="box-label">Reading skill</div><strong>Different characters, different views.</strong> Good readers ask what each character wants, fears, or knows, and why two characters can see the same moment so differently.</div>
<div class="box b-green"><div class="box-label">Big idea</div><strong>Why do two people in the same situation see things so differently?</strong> Lucy and Edmund hear the same name and feel opposite things.</div>
</div>
<p class="quote">“They say Aslan is on the move.”<small>Mr. Beaver, Chapter 7</small></p>
</section>

<section class="card">
<div class="card-head"><span class="ico">📅</span><h2>Day by Day</h2></div>
<table class="days">
<thead><tr><th>Lesson</th><th>Reading</th><th>Big question</th></tr></thead>
<tbody>
<tr><td class="day-n">27.1<span>Day 1</span></td>
<td><span class="ch">Chapter 7: A Day with the Beavers</span><br>Your student describes how each child feels at the name Aslan, then plans a short response comparing two characters.<br><span class="pill p-guide">Guide: Opti</span><span class="pill p-extra">Sentence rewrite</span></td>
<td>Why do two people in the same situation sometimes see things completely differently?</td></tr>
<tr><td class="day-n">27.2<span>Day 2</span></td>
<td><span class="ch">Chapter 8: What Happened after Dinner</span><br>Your student looks for clues about what Edmund is thinking, then drafts the comparison.<br><span class="pill p-guide">Guide: Opti</span><span class="pill p-poem">Poetry</span><span class="pill p-extra">Read Like a Writer video</span></td>
<td>How does Lewis show you what a character is thinking without telling you directly?</td></tr>
<tr><td class="day-n">27.3<span>Day 3</span></td>
<td><span class="ch">Chapter 9: In the Witch’s House</span><br>Your student uses details from Edmund’s night walk to explain how he sees the Witch, then makes the comparison more precise.<br><span class="pill p-guide">Guide: Opti</span><span class="pill p-extra">Read Like a Writer</span></td>
<td>How does Edmund’s perspective change what we know about the danger coming to Narnia?</td></tr>
<tr><td class="day-n">27.4<span>Day 4</span></td>
<td><span class="ch">Look back: Chapters 7–9</span><br>Your student explains what Edmund’s and Lucy’s different views show, and publishes the final response.<br><span class="pill p-guide">Guide: Opti</span><span class="pill p-poem">Poetry</span><span class="pill p-extra">Read Like a Writer</span></td>
<td>What does the contrast between Edmund’s and Lucy’s perspectives tell us about the book so far?</td></tr>
<tr class="extra-row"><td class="day-n">🎙️<span>Fluency</span></td>
<td colspan="2">The moment in Chapter 7 when the children hear Aslan’s name, and each one feels something different. Your student reads it three times (right words, then smooth, then a different voice for each child’s feeling), then <strong>records and submits in Canvas.</strong></td></tr>
<tr class="extra-row"><td class="day-n">📋<span>Check-In</span></td>
<td colspan="2">A 14-point check on the week, in Canvas: irregular verbs, the word parts in- and im-, prefix words, a short passage from Chapter 7, and a short writing response.</td></tr>
</tbody>
</table>
</section>

<section class="card">
<div class="card-head"><span class="ico">🔤</span><h2>Words to Know</h2><span class="tag">Use them at home!</span></div>
<div class="words">
''' + '\n'.join(w(a, b) for a, b in WORDS) + '''
</div>
<div class="skills">
<div class="box b-sky"><div class="box-label">Word parts</div>The word parts <strong>in-</strong> and <strong>im-</strong> both mean <strong>not</strong>. <strong>Im-</strong> goes before words that start with m or p.<span class="eg">impossible · incorrect · impatient · invisible</span></div>
<div class="box b-gold"><div class="box-label">Spelling</div>A <strong>prefix</strong> goes on the front of a <strong>base word</strong>, and the base word keeps its spelling. Peel the prefix off to read the base.<span class="eg">un·happy · re·build · pre·heat · dis·appear</span></div>
<div class="box b-green"><div class="box-label">Grammar</div><strong>Irregular verbs</strong> don’t add -ed for the past. You learn each one.<span class="eg">go → went · run → ran · eat → ate · tell → told</span></div>
</div>
</section>

<section class="card">
<div class="card-head"><span class="ico">✨</span><h2>New in the Lessons</h2></div>
<div class="extras">
<div class="box b-plum"><div class="box-label">🐟 Mr. Beaver’s Ice Hole</div>This week’s word game is Mr. Beaver’s fishing hole in the ice. On Days 1 and 2 your student decides whether a word takes in- or im- to mean not. On Days 3 and 4 they keep the words that have a prefix and a real base word, and throw the others back. Each right answer lands a fish on the ice, and by Day 4 the catch is complete.</div>
<div class="box b-gold"><div class="box-label">🎬 Opti’s videos</div>Every Word Study activity, all four days, starts with a short video where Opti shows how it works. On Day 2, Opti also shows Read Like a Writer with a different sentence from Chapter 8. The videos have captions for now; Opti’s voice will be added later.</div>
<div class="box b-sky"><div class="box-label">🌍 World Notes</div>Each day opens the Reading tab with a real thing behind the story: real beavers and their dams, ice fishing (and staying safe on ice), stone statues, and how the full moon lights up snow.</div>
<div class="box b-green"><div class="box-label">🏮 Truth Watch</div>After reading, your student decides if three moments show someone being honest: Yes or Not yet. This week includes Edmund’s secret, the excuses he tells himself, and the people who tell hard truths.</div>
</div>
<p class="small" style="margin-top:12px;">Each day opens with real art, never pictures from the book: two beavers from the Audubons’ book of North American animals (1840s), Pieter Bruegel’s village skating on a frozen river (1565), an old colored photograph of Neuschwanstein Castle in Germany (1890s), and Arkhip Kuindzhi’s moonlight on a snowy forest (about 1900). Your student looks first, then taps to learn about it.</p>
</section>

<section class="card">
<div class="card-head"><span class="ico">✍️</span><h2>Your Student’s Writing</h2><span class="tag">Writer’s Workshop</span></div>
<div class="essay"><span>Wk 26 · Explain a character’s choice</span><span class="now">Wk 27 · Compare two characters’ perspectives</span></div>
<p>This week’s short response compares how two characters see Aslan or Narnia, and why. Day 1: <strong>plan</strong> (two characters, how each one feels, and the big difference). Day 2: <strong>draft</strong> in full sentences with words like <em>shows</em> and <em>reveals</em>. Day 3: <strong>revise</strong> one vague phrase into precise words. Day 4: <strong>publish</strong> the final response, ending with what the difference shows.</p>
<p class="small">An example writer named Clara shows each step first.</p>
</section>

<section class="card">
<div class="card-head"><span class="ico">💬</span><h2>Ask at Home</h2></div>
<ol class="ask">
<li><span class="q">How did each child feel when Mr. Beaver said “Aslan”?</span><span class="listen">Listen for: Peter brave, Susan like music floating by, Lucy like the start of summer, Edmund horror.</span></li>
<li><span class="q">Why do you think Edmund felt so differently from Lucy?</span><span class="listen">Listen for: Edmund has already sided with the Witch; any answer with a reason from the book.</span></li>
<li><span class="q">What did Edmund tell himself on his way to the Witch’s house? Was it true?</span><span class="listen">Listen for: that she was the rightful Queen and wouldn’t hurt them; deep down he knew she was bad.</span></li>
<li><span class="q">What does “impossible” mean? Why im- and not in-?</span><span class="listen">Listen for: not possible; possible starts with p.</span></li>
</ol>
</section>

<div class="two">
<section class="card">
<div class="card-head"><span class="ico">📬</span><h2>What Gets Turned In</h2></div>
<ul class="check">
<li>Each lesson’s Assignment tab: the chapter questions and the day’s writing step, copied and pasted into Canvas</li>
<li>The Week 27 fluency recording</li>
<li>The Week 27 Check-In in Canvas</li>
</ul>
</section>
<section class="card">
<div class="card-head"><span class="ico">🏡</span><h2>Try at Home</h2></div>
<ul class="check">
<li>Pick one moment from today, and each tell it from your own side</li>
<li>Play “not” words: say a word, and your student adds in- or im- (polite → impolite)</li>
<li>Catch irregular verbs at dinner: “I eated…” “You mean ate!”</li>
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
<div class="card-head"><span class="ico">⏭️</span><h2>Coming Up in Week 28</h2></div>
<p><strong>Chapters 10–12.</strong> Reading skill: noticing symbols and ideas that come back again and again. Word parts: <strong>com-</strong> and <strong>con-</strong>.</p>
</section>

<p class="foot">Optima Academy Online · 3rd Grade ELA · Week 27 Family Guide</p>
</div>
</body>
</html>
'''
io.open('parent-guide-week-27.html', 'w', encoding='utf-8').write(week)

print('ok')
