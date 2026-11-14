"""Week 25 family guide + the new LWW unit guide. Head/CSS and How the Lesson Pages Work from week 22 (a novel week with a
fluency page); bodies from the finished week 25 lessons, DATA and the S&S v4 rows 25-30. Run from the repo root."""
import io
s = io.open('parent-guide-week-22.html', encoding='utf-8').read()
H0 = s[:s.index('<body>')]
howto = s[s.index('<section class="howto">'):s.index('</section>', s.index('<section class="howto">')) + 10]
assert 'Fluency' in howto
OWL = 'https://raw.githubusercontent.com/optimaondemand/optima-assets/eeb0b335630058906d52f478028361d352253a93/images/Optima%20Final%20Circle%20-%20Owl%20Only.png'
ART = 'https://optimaondemand.github.io/optima-3rd-ela/assets/art/lww/'
def w(a, b): return '<div class="word"><b>%s</b><span>%s</span></div>' % (a, b)
WORDS = [('inquisitive', 'eager to find out; very curious'), ('melancholy', 'a deep feeling of sadness or gloom'),
         ('peculiar', 'strange or unusual in a hard-to-explain way'), ('betray', 'to be disloyal to someone who trusted you')]
UNIT = '<p class="unit-link"><a href="parent-guide-lww-unit.html">Read the unit guide for The Lion, the Witch and the Wardrobe →</a></p>'

week = H0.replace('Week 22 Family Guide · The Whipping Boy · 3rd Grade ELA', 'Week 25 Family Guide · The Lion, the Witch and the Wardrobe · 3rd Grade ELA')
assert 'Week 25 Family Guide' in week
week += '''<body>
<div class="wrap">

<header class="hero">
<div class="hero-text">
<div class="brand"><img src="''' + OWL + '''" alt="Optima Academy Online">Family Guide · 3rd Grade ELA</div>
<h1>Week 25: Through the Wardrobe</h1>
<div class="sub"><em>The Lion, the Witch and the Wardrobe</em>, Chapters 1–3: a new book begins</div>
<div class="chips">
<span class="chip">4 lessons</span>
<span class="chip">Chapters 1–3</span>
<span class="chip">Fluency page</span>
<span class="chip">Check-In at week’s end</span>
</div>
<button class="print-btn" onclick="window.print()">🖨️ Print this guide</button>
''' + UNIT + '''
</div>
<div class="hero-art" style="background-image:url(\'''' + ART + '''lww-winter-wood.jpg');background-position:center 40%;" role="img" aria-label="A painting of a quiet forest deep in snow"></div>
</header>

''' + howto + '''

<section class="card">
<div class="card-head"><span class="ico">🧭</span><h2>This Week at a Glance</h2></div>
<p>A new novel starts this week: <em>The Lion, the Witch and the Wardrobe</em> by C.S. Lewis. Four children are sent to stay in a big old house in the country. Lucy, the youngest, steps into a wardrobe full of fur coats, and keeps walking, into a snowy wood called Narnia. She meets a Faun named Mr. Tumnus. When she comes back, nobody believes her, until Edmund finds his own way in. Day 1 reads Chapter 1, Day 2 reads Chapters 2 and 3, and Days 3 and 4 look back at all three chapters. Please have the book ready.</p>
<div class="glance">
<div class="box b-sky"><div class="box-label">Reading skill</div><strong>How an author builds a world.</strong> Good readers slow down in a fantasy story and notice the details: the weather, the light, and what could never happen at home.</div>
<div class="box b-green"><div class="box-label">Big idea</div><strong>What makes a made-up world feel real?</strong> Lewis uses things you can feel, hear and see: snow that is soft and powdery and extremely cold.</div>
</div>
<p class="quote">“This must be a simply enormous wardrobe!”<small>Lucy, Chapter 1</small></p>
</section>

<section class="card">
<div class="card-head"><span class="ico">📅</span><h2>Day by Day</h2></div>
<table class="days">
<thead><tr><th>Lesson</th><th>Reading</th><th>Big question</th></tr></thead>
<tbody>
<tr>
<td class="day-n">25.1<span>Day 1</span></td>
<td><span class="ch">Chapter 1: Lucy Looks into a Wardrobe</span><br>Your student finds the details Lewis uses to build Narnia, then brainstorms setting details for a literary response.<br><span class="pill p-guide">Guide: Opti</span><span class="pill p-extra">Sentence rewrite</span></td>
<td>How does an author make a brand-new world feel real to the reader?</td>
</tr>
<tr>
<td class="day-n">25.2<span>Day 2</span></td>
<td><span class="ch">Chapters 2–3: What Lucy Found There; Edmund and the Wardrobe</span><br>Your student compares Mr. Tumnus’s cozy cave with the cold wood, then drafts an opening sentence.<br><span class="pill p-guide">Guide: Opti</span><span class="pill p-poem">Poetry</span><span class="pill p-extra">Read Like a Writer video</span></td>
<td>How do you know when a character has crossed from the real world into a fantasy world?</td>
</tr>
<tr>
<td class="day-n">25.3<span>Day 3</span></td>
<td><span class="ch">Look back: Chapters 1–3</span><br>Your student finds Lewis’s exact words for what Lucy feels and hears, then writes two evidence sentences with short quotes.<br><span class="pill p-guide">Guide: Opti</span><span class="pill p-extra">Read Like a Writer</span></td>
<td>If you were writing about a fantasy world, what details would you use to make it feel real?</td>
</tr>
<tr>
<td class="day-n">25.4<span>Day 4</span></td>
<td><span class="ch">Look back: Chapters 1–3</span><br>Your student makes a claim about how Lewis makes Narnia feel real, picks the best detail to prove it, and writes a closing sentence.<br><span class="pill p-guide">Guide: Opti</span><span class="pill p-poem">Poetry</span><span class="pill p-extra">Read Like a Writer</span></td>
<td>What makes a reader believe in a fantasy world an author has invented?</td>
</tr>
<tr class="extra-row">
<td class="day-n">🎙️<span>Fluency</span></td>
<td colspan="2">The moment in Chapter 1 when the coats turn into branches and Lucy finds herself in a snowy wood. Your student reads it three times (right words, then smooth, then slowing down where Lucy is surprised), then <strong>records and submits in Canvas.</strong></td>
</tr>
<tr class="extra-row">
<td class="day-n">📋<span>Check-In</span></td>
<td colspan="2">A 14-point check on the week, in Canvas: complex sentences, the word part tele, the schwa sound, a short passage from Chapter 1, and a short writing response.</td>
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
<div class="box b-sky"><div class="box-label">Word parts</div>The word part <strong>tele</strong> means <strong>far</strong>.<span class="eg">telephone · television · telescope · telegram</span></div>
<div class="box b-gold"><div class="box-label">Spelling</div>The <strong>schwa</strong> is the lazy <strong>uh</strong> sound in a quiet beat of a long word. Any vowel can make it, which is why long words are hard to spell by ear.<span class="eg">a·bout · les·son · pen·cil · cir·cus</span></div>
<div class="box b-green"><div class="box-label">Grammar</div>A <strong>complex sentence</strong> has a main idea and a part that can’t stand alone, joined by a word like <em>when</em>, <em>because</em> or <em>although</em>. When that part comes first, a comma follows it.<span class="eg">When Lucy stepped through the fur coats, she felt snow under her shoes.</span></div>
</div>
</section>

<section class="card">
<div class="card-head"><span class="ico">✨</span><h2>New in the Lessons</h2></div>
<div class="extras">
<div class="box b-plum"><div class="box-label">🧥 Through the Wardrobe</div>This week’s word game is the inside of a wardrobe full of fur coats. Each coat has a word with a lazy uh beat. Your student says the word and taps the vowel that makes the uh. Each right answer pushes a coat aside, so more of the snowy wood shows through, and the lamp-post shines brighter every day.</div>
<div class="box b-gold"><div class="box-label">🎬 Opti’s videos</div>Every Word Study activity, all four days, starts with a short video where Opti shows how it works. On Day 2, Opti also shows Read Like a Writer with a different sentence from Chapter 3. The videos have captions for now; Opti’s voice will be added later.</div>
<div class="box b-sky"><div class="box-label">🌍 World Notes</div>Each day opens the Reading tab with a real thing behind the story: children sent away from London in World War II, fauns in very old stories, gas lamp-posts, and reindeer that pull sledges.</div>
<div class="box b-green"><div class="box-label">🏮 Truth Watch</div>After reading, your student decides if three moments from the chapters show someone being honest: Yes or Not yet. Honesty is the trait for the whole Narnia unit.</div>
</div>
<p class="small" style="margin-top:12px;">Each day opens with a real painting, never pictures from the book: Ivan Shishkin’s snowy pine forest (1890), Pieter Bruegel’s <em>Hunters in the Snow</em> (1565), John Atkinson Grimshaw’s lamp-lit street in Leeds, England (1881), and a print of reindeer sledges crossing Lapland (1827). Your student looks first, then taps to learn about it.</p>
</section>

<section class="card">
<div class="card-head"><span class="ico">✍️</span><h2>Your Student’s Writing</h2><span class="tag">Writer’s Workshop</span></div>
<div class="essay"><span class="now">Wk 25 · Describe a fantasy setting</span><span>Wk 26 · Explain a character’s choice</span></div>
<p>A new kind of writing starts this week: a <strong>literary response</strong>, writing that says what you think about a book and proves it with details from the book. The topic is the setting of Narnia. Day 1: <strong>brainstorm</strong> details from Chapter 1. Day 2: <strong>draft an opening sentence</strong> that names the book and the author. Day 3: <strong>add evidence</strong>, a short quote and what it shows. Day 4: <strong>write a closing sentence</strong>.</p>
<p class="small">An example writer named Clara shows each step first.</p>
</section>

<section class="card">
<div class="card-head"><span class="ico">💬</span><h2>Ask at Home</h2></div>
<ol class="ask">
<li><span class="q">What did Lucy feel and hear when she walked into the wardrobe?</span><span class="listen">Listen for: something crunching under her feet, something soft and powdery and cold, branches instead of coats.</span></li>
<li><span class="q">Why didn’t the others believe Lucy?</span><span class="listen">Listen for: she was gone only a moment, and the wardrobe looked ordinary when they checked.</span></li>
<li><span class="q">What does tele mean? Can you name a tele word?</span><span class="listen">Listen for: far; telephone, television, telescope.</span></li>
<li><span class="q">Say “sofa” slowly. Which part is lazy?</span><span class="listen">Listen for: the end, “uh,” spelled with an a.</span></li>
</ol>
</section>

<div class="two">
<section class="card">
<div class="card-head"><span class="ico">📬</span><h2>What Gets Turned In</h2></div>
<ul class="check">
<li>Each lesson’s Assignment tab: the chapter questions and the day’s writing step, copied and pasted into Canvas</li>
<li>The Week 25 fluency recording</li>
<li>The Week 25 Check-In in Canvas</li>
</ul>
</section>
<section class="card">
<div class="card-head"><span class="ico">🏡</span><h2>Try at Home</h2></div>
<ul class="check">
<li>Open a closet and describe what is inside with three senses, the way Lewis does</li>
<li>Play “lazy beat”: say a long word like lemon or pencil and find the beat that says uh</li>
<li>Take turns starting a sentence with “When…” or “Because…” and finishing it</li>
</ul>
</section>
</div>

<section class="card">
<div class="card-head"><span class="ico">🎒</span><h2>Have on Hand</h2></div>
<ul class="check">
<li><em>The Lion, the Witch and the Wardrobe</em> by C.S. Lewis, for all of Weeks 25–30</li>
</ul>
</section>

<section class="card next">
<div class="card-head"><span class="ico">⏭️</span><h2>Coming Up in Week 26</h2></div>
<p><strong>Chapters 4–6.</strong> Edmund meets the Queen, and the children step through the wardrobe together. Reading skill: tracking the choices characters make and what those choices cost. Word part: <strong>form</strong> (shape).</p>
</section>

<p class="foot">Optima Academy Online · 3rd Grade ELA · Week 25 Family Guide</p>
</div>
</body>
</html>
'''
io.open('parent-guide-week-25.html', 'w', encoding='utf-8').write(week)

u0 = io.open('parent-guide-wb-unit.html', encoding='utf-8').read()
unit = u0[:u0.index('<body>')].replace('The Whipping Boy Unit Guide · 3rd Grade ELA', 'The Lion, the Witch and the Wardrobe Unit Guide · 3rd Grade ELA')
assert 'Wardrobe Unit Guide' in unit
unit += '''<body>
<div class="wrap">

<header class="hero">
<div class="hero-text">
<div class="brand"><img src="''' + OWL + '''" alt="Optima Academy Online">Family Guide · 3rd Grade ELA</div>
<h1>Unit Guide: <em>The Lion, the Witch and the Wardrobe</em></h1>
<div class="sub">by C.S. Lewis · Weeks 25–30</div>
<div class="chips">
<span class="chip">6 weeks</span>
<span class="chip">17 chapters</span>
<span class="chip">Literary response writing</span>
<span class="chip">Guide: Opti the owl</span>
</div>
<button class="print-btn" onclick="window.print()">🖨️ Print this guide</button>
</div>
<div class="hero-art" style="background-image:url(\'''' + ART + '''lww-lamplight.jpg');background-position:center 40%;" role="img" aria-label="A painting of a city street lit by gas lamps"></div>
</header>

''' + howto + '''

<section class="card">
<div class="card-head"><span class="ico">📕</span><h2>About the Book</h2></div>
<p><em>The Lion, the Witch and the Wardrobe</em> was published in 1950. C.S. Lewis was a professor in England. During World War II, four children, Peter, Susan, Edmund and Lucy, are sent away from London to stay in an old Professor’s house in the country. Lucy steps into a wardrobe and finds Narnia, a land where it is always winter and never Christmas, ruled by the White Witch. The children meet talking animals, learn about a great lion named Aslan, and have to decide whom to trust.</p>
<p>We read it because it is a wonderful first fantasy novel, and because it gives third graders big things to think about: honesty, courage, forgiveness, and what it costs to make a wrong choice and then try to put it right.</p>
<p class="quote">“This must be a simply enormous wardrobe!”<small>Lucy, Chapter 1</small></p>
</section>

<section class="card">
<div class="card-head"><span class="ico">🗓️</span><h2>How a Week Works</h2></div>
<div class="grid2">
<div class="box b-sky"><div class="box-label">Days 1–2</div>Read the week’s chapters, practice the week’s word study (a word part, a spelling pattern, a grammar skill and new vocabulary), answer three chapter questions and take one writing step.</div>
<div class="box b-gold"><div class="box-label">Days 3–4</div>Look back at the same chapters for exact words and evidence, keep practicing the word study, and finish the week’s writing step.</div>
<div class="box b-green"><div class="box-label">Fluency</div>One short passage from the book, read three times and recorded in Canvas.</div>
<div class="box b-plum"><div class="box-label">Check-In</div>A short Canvas quiz at the end of the week on that week’s skills and chapters.</div>
</div>
</section>

<section class="card">
<div class="card-head"><span class="ico">🗺️</span><h2>The Unit, Week by Week</h2></div>
<table class="days">
<thead><tr><th>Week</th><th>Chapters</th><th>Writing step</th></tr></thead>
<tbody>
<tr><td class="day-n">25</td><td><span class="ch">Chapters 1–3</span><br>Lucy finds Narnia and meets Mr. Tumnus; nobody believes her until Edmund gets in. Reading: how an author builds a fantasy world. Word part: tele (far).</td><td>Describe a fantasy setting</td></tr>
<tr><td class="day-n">26</td><td><span class="ch">Chapters 4–6</span><br>Reading: the choices characters make and what they cost. Word part: form (shape).</td><td>Explain a character’s choice</td></tr>
<tr><td class="day-n">27</td><td><span class="ch">Chapters 7–9</span><br>Reading: different characters’ points of view. Word parts: in-, im-.</td><td>Compare two characters</td></tr>
<tr><td class="day-n">28</td><td><span class="ch">Chapters 10–12</span><br>Reading: symbols and repeated ideas. Word parts: com-, con-.</td><td>Symbol or theme paragraph</td></tr>
<tr><td class="day-n">29</td><td><span class="ch">Chapters 13–15</span><br>Reading: the theme, using details from the whole story. Word part: ject (throw).</td><td>Draft a response on theme</td></tr>
<tr><td class="day-n">30</td><td><span class="ch">Chapters 16–17 and the whole book</span><br>Reading: how the ending shows the theme. Review of the year’s word parts.</td><td>Final revision</td></tr>
</tbody>
</table>
</section>

<section class="card">
<div class="card-head"><span class="ico">✍️</span><h2>Your Student’s Literary Response Writing</h2><span class="tag">Writer’s Workshop</span></div>
<p>Across the unit, your student writes <strong>literary responses</strong>: short pieces that say what they think about the book and prove it with <strong>details and short quotes from the book</strong>. They start by describing the setting of Narnia, then explain a character’s choice, compare two characters, write about a symbol or theme, and finish with a final revision in Week 30. An example writer named Clara shows each step first.</p>
</section>

<section class="card">
<div class="card-head"><span class="ico">✅</span><h2>How Learning Is Checked</h2></div>
<ul class="check">
<li>Each lesson’s Assignment tab, copied and pasted into Canvas: chapter questions and the day’s writing step</li>
<li>A fluency recording every week</li>
<li>A Canvas check-in quiz at the end of every week</li>
<li>A whole-book check and the revised literary response in Week 30</li>
</ul>
</section>

<section class="card">
<div class="card-head"><span class="ico">💛</span><h2>Good to Know Ahead of Time</h2></div>
<div class="grid2">
<div class="box b-rose"><div class="box-label">A real war</div>The story begins in World War II. The children were sent away from London because of air raids, when planes dropped bombs on the city. The book mentions this only briefly.</div>
<div class="box b-rose"><div class="box-label">The White Witch</div>The Witch is truly frightening. She turns creatures into stone statues, and in Chapter 2 Mr. Tumnus admits he was supposed to hand Lucy over to her. Later, she has Mr. Tumnus taken away.</div>
<div class="box b-rose"><div class="box-label">Aslan’s death</div>In Chapters 13–15, Aslan gives his life in Edmund’s place and is killed by the Witch and her creatures on the Stone Table. It is a sad, serious scene. He comes back to life the next morning.</div>
<div class="box b-rose"><div class="box-label">A battle</div>In Chapter 12, Peter fights a wolf with a sword. Near the end there is a battle, and Edmund is badly wounded and then healed. Nothing is described in gory detail.</div>
<div class="box b-plum"><div class="box-label">Edmund’s choices</div>Edmund lies, is unkind to Lucy, and goes to the Witch. The lessons treat this as a choice with costs, and the book shows him being forgiven and changing.</div>
<div class="box b-plum"><div class="box-label">A Christian author</div>Lewis was a Christian, and many readers see the story of Aslan as a picture of the Christian story. The lessons teach it as a novel and focus on the characters, choices and writing.</div>
</div>
</section>

<section class="card">
<div class="card-head"><span class="ico">🤝</span><h2>How to Help (Without Doing It for Them)</h2></div>
<div class="grid2">
<div>
<h3 style="font-size:19px;margin-bottom:6px;">Try this</h3>
<ul class="check">
<li>Ask “Where in the book does it say that?” when your student answers a question.</li>
<li>Point them to Opti’s videos and the hint buttons before you step in.</li>
<li>Ask the questions in each weekly guide. Talking it through first makes the writing easier.</li>
<li>Be the audience for the fluency reading and the finished literary response.</li>
</ul>
</div>
<div>
<h3 style="font-size:19px;margin-bottom:6px;">Try to avoid</h3>
<ul class="check dont">
<li>Typing or wording answers for them. Teachers need to see your student’s own thinking.</li>
<li>Fixing their writing. Revising is a lesson of its own in Week 30.</li>
<li>Telling them what happens next. The surprises are part of the fun.</li>
</ul>
</div>
</div>
</section>

<section class="card">
<div class="card-head"><span class="ico">📚</span><h2>Family Bookshelf</h2><span class="tag">Optional</span></div>
<ul class="check">
<li><em>The Magician’s Nephew</em> by C.S. Lewis: how Narnia began, and where the lamp-post came from</li>
<li><em>The Horse and His Boy</em> by C.S. Lewis: another adventure in Narnia</li>
<li><em>Prince Caspian</em> by C.S. Lewis: students read this one in 4th grade at Optima</li>
</ul>
</section>

<p class="foot">Optima Academy Online · 3rd Grade ELA · The Lion, the Witch and the Wardrobe Unit Guide</p>
</div>
</body>
</html>
'''
io.open('parent-guide-lww-unit.html', 'w', encoding='utf-8').write(unit)
print('ok')
