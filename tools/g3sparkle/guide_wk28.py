"""Week 28 family guide (unit guide is week 25's). Head/CSS and How the Lesson Pages Work from week 22 (a novel week with a
fluency page); bodies from the finished week 28 lessons, DATA and the S&S v4 rows 25-30. Run from the repo root."""
import io
s = io.open('parent-guide-week-22.html', encoding='utf-8').read()
H0 = s[:s.index('<body>')]
howto = s[s.index('<section class="howto">'):s.index('</section>', s.index('<section class="howto">')) + 10]
assert 'Fluency' in howto
OWL = 'https://raw.githubusercontent.com/optimaondemand/optima-assets/eeb0b335630058906d52f478028361d352253a93/images/Optima%20Final%20Circle%20-%20Owl%20Only.png'
ART = 'https://optimaondemand.github.io/optima-3rd-ela/assets/art/lww/'
def w(a, b): return '<div class="word"><b>%s</b><span>%s</span></div>' % (a, b)
WORDS = [('renewed', 'made new again; restored to a fresh state'), ('herald', 'a person or thing that announces something important is coming'),
         ('solemn', 'serious, formal, and sincere'), ('jovial', 'cheerful and friendly; in high spirits')]
UNIT = '<p class="unit-link"><a href="parent-guide-lww-unit.html">Read the unit guide for The Lion, the Witch and the Wardrobe →</a></p>'

week = H0.replace('Week 22 Family Guide · The Whipping Boy · 3rd Grade ELA', 'Week 28 Family Guide · The Lion, the Witch and the Wardrobe · 3rd Grade ELA')
assert 'Week 28 Family Guide' in week
week += '''<body>
<div class="wrap">

<header class="hero">
<div class="hero-text">
<div class="brand"><img src="''' + OWL + '''" alt="Optima Academy Online">Family Guide · 3rd Grade ELA</div>
<h1>Week 28: Signs of Spring</h1>
<div class="sub"><em>The Lion, the Witch and the Wardrobe</em>, Chapters 10–12: noticing symbols and ideas that come back</div>
<div class="chips">
<span class="chip">4 lessons</span>
<span class="chip">Chapters 10–12</span>
<span class="chip">Fluency page</span>
<span class="chip">Check-In at week’s end</span>
</div>
<button class="print-btn" onclick="window.print()">🖨️ Print this guide</button>
''' + UNIT + '''
</div>
<div class="hero-art" style="background-image:url(\'''' + ART + '''lww-levitan-march.jpg');background-position:center 60%;" role="img" aria-label="A painting of melting snow on a sunny early spring day, with birch trees and a horse waiting by a house"></div>
</header>

''' + howto + '''

<section class="card">
<div class="card-head"><span class="ico">🧭</span><h2>This Week at a Glance</h2></div>
<p>In Chapter 10, the Beavers and the children escape in the night. In the morning they hear sleigh bells, but it is not the Witch: it is Father Christmas, who gives each of them a gift and says the Witch’s magic is weakening. Chapter 11 follows Edmund on the Witch’s sledge, until the snow starts to melt so fast that the sledge gets stuck and spring comes to Narnia. In Chapter 12, the others reach the Stone Table and meet Aslan, and Peter fights his first battle. Day 1 reads Chapter 10, Day 2 Chapter 11, Day 3 Chapter 12, and Day 4 looks back at all three.</p>
<div class="glance">
<div class="box b-sky"><div class="box-label">Reading skill</div><strong>Symbols and repeated ideas.</strong> A symbol is a thing in a story that stands for a bigger idea. Good readers notice what keeps coming back and ask what it stands for.</div>
<div class="box b-green"><div class="box-label">Big idea</div><strong>What does it mean when something in a story stands for more than just itself?</strong> The snow, the thaw and Father Christmas all point to something bigger.</div>
</div>
<p class="quote">“Aslan is on the move. The Witch’s magic is weakening.”<small>Father Christmas, Chapter 10</small></p>
</section>

<section class="card">
<div class="card-head"><span class="ico">📅</span><h2>Day by Day</h2></div>
<table class="days">
<thead><tr><th>Lesson</th><th>Reading</th><th>Big question</th></tr></thead>
<tbody>
<tr><td class="day-n">28.1<span>Day 1</span></td>
<td><span class="ch">Chapter 10: The Spell Begins to Break</span><br>Your student explains what Father Christmas’s arrival and his gifts might stand for, then writes a short paragraph about one symbol.<br><span class="pill p-guide">Guide: Opti</span><span class="pill p-extra">Sentence rewrite</span></td>
<td>What does it mean when something in a story stands for more than just itself?</td></tr>
<tr><td class="day-n">28.2<span>Day 2</span></td>
<td><span class="ch">Chapter 11: Aslan Is Nearer</span><br>Your student tracks the thaw through Edmund’s eyes and how the Witch reacts, then makes the symbol paragraph more precise.<br><span class="pill p-guide">Guide: Opti</span><span class="pill p-poem">Poetry</span><span class="pill p-extra">Read Like a Writer video</span></td>
<td>How do you recognize a symbol, something that stands for more than just itself?</td></tr>
<tr><td class="day-n">28.3<span>Day 3</span></td>
<td><span class="ch">Chapter 12: Peter’s First Battle</span><br>Your student explains what Peter does, how Aslan answers, and how it connects to the four thrones, then adds the symbol paragraph to the full response.<br><span class="pill p-guide">Guide: Opti</span><span class="pill p-extra">Read Like a Writer</span></td>
<td>How does the battle in Chapter 12 connect to the bigger symbols in the story?</td></tr>
<tr><td class="day-n">28.4<span>Day 4</span></td>
<td><span class="ch">Look back: Chapters 10–12</span><br>Your student names one symbol, backs it up with details, and polishes the literary response.<br><span class="pill p-guide">Guide: Opti</span><span class="pill p-poem">Poetry</span><span class="pill p-extra">Read Like a Writer</span></td>
<td>Why do authors use symbols? What can a symbol do that saying it straight out cannot?</td></tr>
<tr class="extra-row"><td class="day-n">🎙️<span>Fluency</span></td>
<td colspan="2">The thaw in Chapter 11, seen through Edmund’s eyes: “Every moment the patches of green grew bigger and the patches of snow grew smaller.” Your student reads it three times (right words, then smooth, then letting the “Every moment” sentences speed up like the thaw), then <strong>records and submits in Canvas.</strong></td></tr>
<tr class="extra-row"><td class="day-n">📋<span>Check-In</span></td>
<td colspan="2">A 14-point check on the week, in Canvas: apostrophes, the word parts com- and con-, endings that change a word, a short passage from Chapter 11, and a short writing response.</td></tr>
</tbody>
</table>
</section>

<section class="card">
<div class="card-head"><span class="ico">🔤</span><h2>Words to Know</h2><span class="tag">Use them at home!</span></div>
<div class="words">
''' + '\n'.join(w(a, b) for a, b in WORDS) + '''
</div>
<div class="skills">
<div class="box b-sky"><div class="box-label">Word parts</div>The word parts <strong>com-</strong> and <strong>con-</strong> both mean <strong>with</strong> or <strong>together</strong>.<span class="eg">combine · connect · company · conversation</span></div>
<div class="box b-gold"><div class="box-label">Spelling</div>Some endings change the base word first: <strong>double</strong> the last letter, <strong>drop</strong> the silent e, or change <strong>y to i</strong>.<span class="eg">run → running · hope → hoping · carry → carried</span></div>
<div class="box b-green"><div class="box-label">Grammar</div>An <strong>apostrophe</strong> has two jobs. It joins two words, or it shows who something belongs to.<span class="eg">did not → didn’t · the bottle that belongs to Lucy → Lucy’s bottle</span></div>
</div>
</section>

<section class="card">
<div class="card-head"><span class="ico">✨</span><h2>New in the Lessons</h2></div>
<div class="extras">
<div class="box b-plum"><div class="box-label">🌼 The Great Thaw</div>This week’s word game is a snowy glade in Narnia. On Days 1 and 2 your student picks what a com- or con- word means. On Days 3 and 4 they decide which change a base word needs before an ending goes on (double, drop the e, change y to i, or none). Each right answer melts a snow patch and a spring flower from Chapter 11 comes up, and by Day 4 the whole glade has thawed.</div>
<div class="box b-gold"><div class="box-label">🎬 Opti’s videos</div>Every Word Study activity, all four days, starts with a short video where Opti shows how it works. On Day 2, Opti also shows Read Like a Writer with a different sentence from Chapter 11. The videos have captions for now; Opti’s voice will be added later.</div>
<div class="box b-sky"><div class="box-label">🌍 World Notes</div>Each day opens the Reading tab with a real thing behind the story: the old English Father Christmas, the real spring flowers Edmund sees (snowdrops, celandines, crocuses), how knights were made long ago, and real wolves, which are shy of people and not like the villains in old stories.</div>
<div class="box b-green"><div class="box-label">🏮 Truth Watch</div>After reading, your student decides if three moments show someone being honest: Yes or Not yet. This week includes the Witch’s broken promise to Edmund, a little squirrel who tells the truth, and Peter owning up to his part in Edmund going wrong.</div>
</div>
<p class="small" style="margin-top:12px;">Each day opens with real art, never pictures from the book: Father Christmas from a London newspaper at Christmas in 1848, Isaac Levitan’s painting of melting snow in March (1895), Edmund Blair Leighton’s <em>The Accolade</em>, a painting of a knight being made (1901), and Vincent van Gogh’s <em>Almond Blossom</em> (1890), which he painted for a newborn baby as a sign of new life. Your student looks first, then taps to learn about it.</p>
</section>

<section class="card">
<div class="card-head"><span class="ico">⚠️</span><h2>Good to Know</h2></div>
<p>Chapter 11 is hard for Edmund: the Witch is cruel to him, slaps him, ties his hands, and turns a happy party of animals into stone. In Chapter 12, a huge wolf named Maugrim chases Susan up a tree, and Peter fights it with his sword and kills it. The fight is short, but it is the scariest part of the book so far. Peter is not hurt, and afterward Aslan makes him a knight. If your student is worried, it helps to talk about how Peter was scared and did the brave thing anyway.</p>
</section>

<section class="card">
<div class="card-head"><span class="ico">✍️</span><h2>Your Student’s Writing</h2><span class="tag">Writer’s Workshop</span></div>
<div class="essay"><span>Wk 27 · Compare two characters’ perspectives</span><span class="now">Wk 28 · Add a symbol paragraph</span></div>
<p>This week your student adds a paragraph about a symbol to the literary response. Day 1: <strong>write</strong> two or three sentences about one symbol from Chapter 10 (name it, say what it stands for, and why it matters). Day 2: <strong>revise</strong> one vague phrase with a precise idea and a word like <em>represents</em> or <em>suggests</em>. Day 3: <strong>add</strong> the paragraph to the whole response with a joining phrase like <em>In addition</em>. Day 4: <strong>polish</strong> and add a closing sentence about what the symbols do for the reader.</p>
<p class="small">An example writer named Clara shows each step first.</p>
</section>

<section class="card">
<div class="card-head"><span class="ico">💬</span><h2>Ask at Home</h2></div>
<ol class="ask">
<li><span class="q">Why was it such big news when Father Christmas got into Narnia?</span><span class="listen">Listen for: the Witch made it always winter and never Christmas; her magic is weakening.</span></li>
<li><span class="q">What does the melting snow stand for?</span><span class="listen">Listen for: the Witch losing her power, hope, Aslan coming; any answer with a reason from the book.</span></li>
<li><span class="q">Was Peter brave in Chapter 12, even though he felt sick with fear?</span><span class="listen">Listen for: yes, because he did what he had to do anyway.</span></li>
<li><span class="q">Where does the apostrophe go in “didnt”? And in “Lucys bottle”?</span><span class="listen">Listen for: didn’t (where the o was), Lucy’s (the bottle belongs to Lucy).</span></li>
</ol>
</section>

<div class="two">
<section class="card">
<div class="card-head"><span class="ico">📬</span><h2>What Gets Turned In</h2></div>
<ul class="check">
<li>Each lesson’s Assignment tab: the chapter questions and the day’s writing step, copied and pasted into Canvas</li>
<li>The Week 28 fluency recording</li>
<li>The Week 28 Check-In in Canvas</li>
</ul>
</section>
<section class="card">
<div class="card-head"><span class="ico">🏡</span><h2>Try at Home</h2></div>
<ul class="check">
<li>Spot symbols around you: what does a red light, a birthday candle or a flag stand for?</li>
<li>Play “together” words: who can name a com- or con- word that means with or together?</li>
<li>Write a grocery list with words that change: bake → baking, try → tried, shop → shopping</li>
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
<div class="card-head"><span class="ico">⏭️</span><h2>Coming Up in Week 29</h2></div>
<p><strong>Chapters 13–15.</strong> Reading skill: explaining a story’s theme with details from across the book. Word parts: the root <strong>ject</strong>, which means throw. Chapter 14 has the saddest part of the book; the unit guide tells what happens so you can be ready.</p>
</section>

<p class="foot">Optima Academy Online · 3rd Grade ELA · Week 28 Family Guide</p>
</div>
</body>
</html>
'''
io.open('parent-guide-week-28.html', 'w', encoding='utf-8').write(week)

print('ok')
