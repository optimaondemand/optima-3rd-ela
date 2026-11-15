"""Week 30 family guide (unit guide is week 25's). Head/CSS and How the Lesson Pages Work from week 22 (a novel week with a
fluency page); bodies from the finished week 30 lessons, DATA and the S&S v4 rows 30-31. Run from the repo root.
The Ch. 16 battle is named plainly in Good to Know."""
import io
s = io.open('parent-guide-week-22.html', encoding='utf-8').read()
H0 = s[:s.index('<body>')]
howto = s[s.index('<section class="howto">'):s.index('</section>', s.index('<section class="howto">')) + 10]
assert 'Fluency' in howto
OWL = 'https://raw.githubusercontent.com/optimaondemand/optima-assets/eeb0b335630058906d52f478028361d352253a93/images/Optima%20Final%20Circle%20-%20Owl%20Only.png'
ART = 'https://optimaondemand.github.io/optima-3rd-ela/assets/art/lww/'
def w(a, b): return '<div class="word"><b>%s</b><span>%s</span></div>' % (a, b)
WORDS = [('sovereign', 'the supreme ruler of a country or kingdom'), ('coronation', 'the ceremony in which a ruler is officially crowned'),
         ('reconciled', 'restored to friendship or peace after a conflict'), ('vanquished', 'defeated completely in battle')]
UNIT = '<p class="unit-link"><a href="parent-guide-lww-unit.html">Read the unit guide for The Lion, the Witch and the Wardrobe →</a></p>'

week = H0.replace('Week 22 Family Guide · The Whipping Boy · 3rd Grade ELA', 'Week 30 Family Guide · The Lion, the Witch and the Wardrobe · 3rd Grade ELA')
assert 'Week 30 Family Guide' in week
week += '''<body>
<div class="wrap">

<header class="hero">
<div class="hero-text">
<div class="brand"><img src="''' + OWL + '''" alt="Optima Academy Online">Family Guide · 3rd Grade ELA</div>
<h1>Week 30: Once a King or Queen</h1>
<div class="sub"><em>The Lion, the Witch and the Wardrobe</em>, Chapters 16–17: how the ending shows the theme</div>
<div class="chips">
<span class="chip">4 lessons</span>
<span class="chip">Chapters 16–17</span>
<span class="chip">Fluency page</span>
<span class="chip">Check-In at week’s end</span>
</div>
<button class="print-btn" onclick="window.print()">🖨️ Print this guide</button>
''' + UNIT + '''
</div>
<div class="hero-art" style="background-image:url(\'''' + ART + '''lww-bamburgh.jpg');background-position:center 45%;" role="img" aria-label="A painting of a castle on a hill above a long sandy beach"></div>
</header>

''' + howto + '''

<section class="card">
<div class="card-head"><span class="ico">🧭</span><h2>This Week at a Glance</h2></div>
<p>This is the last week of the book. In Chapter 16, Aslan breathes on the Witch’s stone statues and they come back to life, then leads them to help Peter’s army. In Chapter 17, the battle ends, Lucy’s cordial heals Edmund, and the four children are crowned kings and queens at Cair Paravel. Years later, hunting the White Stag, they find the lamp-post and tumble back out of the wardrobe into the Professor’s house, on the same day and at the same hour they left. Day 1 reads Chapters 16 and 17. Days 2, 3 and 4 look back over the whole book.</p>
<div class="glance">
<div class="box b-sky"><div class="box-label">Reading skill</div><strong>How the ending shows the theme.</strong> The end of a book often answers a question the beginning asked. Edmund began as a traitor and ends as King Edmund the Just.</div>
<div class="box b-green"><div class="box-label">Big idea</div><strong>How would you explain what this book is really about to someone who has never read it?</strong> Your student finishes a whole literary response on theme this week.</div>
</div>
<p class="quote">“Once a King in Narnia, always a King in Narnia.”<small>the Professor, Chapter 17</small></p>
</section>

<section class="card">
<div class="card-head"><span class="ico">📅</span><h2>Day by Day</h2></div>
<table class="days">
<thead><tr><th>Lesson</th><th>Reading</th><th>Big question</th></tr></thead>
<tbody>
<tr><td class="day-n">30.1<span>Day 1</span></td>
<td><span class="ch">Chapters 16–17: What Happened About the Statues; The Hunting of the White Stag</span><br>Your student connects the statues coming alive to the winter and stone from earlier in the book, tells how Edmund has changed, and adds proof from the ending to the literary response.<br><span class="pill p-guide">Guide: Opti</span><span class="pill p-extra">Sentence rewrite</span></td>
<td>How does the ending of a story prove or complete its theme?</td></tr>
<tr><td class="day-n">30.2<span>Day 2</span></td>
<td><span class="ch">Look back: the whole book</span><br>Your student finds three moments from different chapters that prove the same theme, and edits the response for capitals, apostrophes and commas.<br><span class="pill p-guide">Guide: Opti</span><span class="pill p-poem">Poetry</span><span class="pill p-extra">Read Like a Writer video</span></td>
<td>How do you recognize when a story has truly fulfilled its theme?</td></tr>
<tr><td class="day-n">30.3<span>Day 3</span></td>
<td><span class="ch">Look back: the whole book</span><br>Your student writes a short paragraph about the whole book, tries a spelling and grammar checker, and gives the response a title.<br><span class="pill p-guide">Guide: Opti</span><span class="pill p-extra">Read Like a Writer</span></td>
<td>How does understanding the theme help you explain what the novel is really about?</td></tr>
<tr><td class="day-n">30.4<span>Day 4</span></td>
<td><span class="ch">Look back: the whole book</span><br>Your student writes a final theme statement, picks the moment that mattered most, and publishes the finished literary response.<br><span class="pill p-guide">Guide: Opti</span><span class="pill p-poem">Poetry</span><span class="pill p-extra">Read Like a Writer</span></td>
<td>How would you explain what The Lion, the Witch and the Wardrobe is really about to someone who has never read it?</td></tr>
<tr class="extra-row"><td class="day-n">🎙️<span>Fluency</span></td>
<td colspan="2">A passage from Chapter 17: the four children grow up as rulers and earn their royal names, King Peter the Magnificent, Susan the Gentle, King Edmund the Just and Queen Lucy the Valiant. Your student reads it three times, then <strong>records and submits in Canvas.</strong></td></tr>
<tr class="extra-row"><td class="day-n">📋<span>Check-In</span></td>
<td colspan="2">A 14-point check on the week, in Canvas: editing for capitals and punctuation, roots and spelling patterns from the year, a short passage from Chapter 17, and a short writing response about the ending.</td></tr>
</tbody>
</table>
</section>

<section class="card">
<div class="card-head"><span class="ico">🔤</span><h2>Words to Know</h2><span class="tag">Use them at home!</span></div>
<div class="words">
''' + '\n'.join(w(a, b) for a, b in WORDS) + '''
</div>
<div class="skills">
<div class="box b-sky"><div class="box-label">Word parts</div>A review of the year’s <strong>roots</strong>: inter (between), trans (across), form (shape), ject (throw), script and scribe (write), port (carry), struct (build).<span class="eg">transport · inspect · construct · describe</span></div>
<div class="box b-gold"><div class="box-label">Spelling</div>A review of the <strong>syllable types</strong>: closed, open, silent-e, vowel team, r-controlled and consonant-le.<span class="eg">nap·kin · ti·ger · com·pete · rain·bow · gar·den · can·dle</span></div>
<div class="box b-green"><div class="box-label">Grammar</div><strong>Editing</strong> in passes: capitals first, then apostrophes, then commas.<span class="eg">the childrens coats → The children’s coats</span></div>
</div>
</section>

<section class="card">
<div class="card-head"><span class="ico">✨</span><h2>New in the Lessons</h2></div>
<div class="extras">
<div class="box b-plum"><div class="box-label">🗿 Statues Come Alive</div>This week’s word game is the Witch’s courtyard from Chapter 16. On Days 1 and 2 your student picks what a word built from one of the year’s roots means. On Days 3 and 4 they name the syllable type of a bold part of a word. Each right answer turns a stone statue to full color, and by Day 4 the courtyard “looked more like a zoo.”</div>
<div class="box b-gold"><div class="box-label">🎬 Opti’s videos</div>Every Word Study activity, all four days, starts with a short video where Opti shows how it works. On Day 2, Opti also shows Read Like a Writer with a different sentence from Chapter 16. The videos have captions for now; Opti’s voice will be added later.</div>
<div class="box b-sky"><div class="box-label">🌍 World Notes</div>Each day opens the Reading tab with a real thing behind the story: real coronations, the bronze lions of Trafalgar Square in London, mermaids in old sailors’ stories, and the white stag of old legends.</div>
<div class="box b-green"><div class="box-label">🏮 Truth Watch</div>After reading, your student decides if three moments show someone being honest: Yes or Not yet. This week looks back over the whole book, from Edmund pretending he never went to Narnia to the children telling the Professor the whole story.</div>
</div>
<p class="small" style="margin-top:12px;">Each day opens with real art, never pictures from the book: George Hayter’s painting of Queen Victoria’s coronation (1838), an old color photograph of the lions in Trafalgar Square, John Varley’s <em>Bamburgh Castle</em>, a castle above the sea, and the white deer from the Wilton Diptych, painted more than 600 years ago. Your student looks first, then taps to learn about it.</p>
</section>

<section class="card">
<div class="card-head"><span class="ico">⚠️</span><h2>Good to Know</h2></div>
<p>Chapter 16 ends with a battle. Aslan leaps on the White Witch, and the Witch is killed; most of her army is killed or runs away. Edmund is badly wounded in the fighting, but Lucy’s cordial heals him, and Aslan makes him a knight. The book keeps the battle short and not detailed. If your student was upset by last week’s chapters, this week brings the happy ending: Aslan alive, Edmund forgiven and healed, and all four children crowned.</p>
</section>

<section class="card">
<div class="card-head"><span class="ico">✍️</span><h2>Your Student’s Writing</h2><span class="tag">Writer’s Workshop</span></div>
<div class="essay"><span>Wk 29 · A literary response on theme</span><span class="now">Wk 30 · Final revision and publishing</span></div>
<p>This week your student finishes the literary response on theme. Day 1: <strong>revise</strong> by adding two sentences of proof from Chapter 16 or 17. Day 2: <strong>edit</strong> for capitals, apostrophes and commas, and read it aloud. Day 3: <strong>prepare to publish</strong> with a title and one last improvement. Day 4: <strong>publish</strong> the finished response, with proof from three different chapters.</p>
<p class="small">An example writer named Clara shows each step first.</p>
</section>

<section class="card">
<div class="card-head"><span class="ico">💬</span><h2>Ask at Home</h2></div>
<ol class="ask">
<li><span class="q">How is Edmund different at the end of the book?</span><span class="listen">Listen for: he fought bravely and broke the Witch’s wand; he was forgiven, healed and crowned King Edmund the Just.</span></li>
<li><span class="q">What happened when the four kings and queens followed the White Stag?</span><span class="listen">Listen for: they found the lamp-post and came back out of the wardrobe, on the same day and at the same hour.</span></li>
<li><span class="q">What is the theme of the book, in one sentence?</span><span class="listen">Listen for: a full sentence such as “The story shows that forgiveness can change someone,” with a detail to back it up.</span></li>
<li><span class="q">What does the root port mean? Can you name a word with it?</span><span class="listen">Listen for: carry; transport, report, portable.</span></li>
</ol>
</section>

<div class="two">
<section class="card">
<div class="card-head"><span class="ico">📬</span><h2>What Gets Turned In</h2></div>
<ul class="check">
<li>Each lesson’s Assignment tab: the chapter questions and the day’s writing step, copied and pasted into Canvas</li>
<li>The finished, titled literary response on Day 4</li>
<li>The Week 30 fluency recording</li>
<li>The Week 30 Check-In in Canvas</li>
</ul>
</section>
<section class="card">
<div class="card-head"><span class="ico">🏡</span><h2>Try at Home</h2></div>
<ul class="check">
<li>Ask your student to read the published response aloud to the family</li>
<li>Talk about the best ending of a book or movie you both know: what question did it answer?</li>
<li>Name a “royal name” for each family member, like Lucy the Valiant</li>
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
<div class="card-head"><span class="ico">⏭️</span><h2>Coming Up in Week 31</h2></div>
<p><strong>A new extension week.</strong> Reading skill: comparing how two authors present the same topic, courage. Word study: a review of prefixes and suffixes, and decoding long words. Writing: planning a response that compares two authors on courage. Poetry: your student chooses a form and writes a poem.</p>
</section>

<p class="foot">Optima Academy Online · 3rd Grade ELA · Week 30 Family Guide</p>
</div>
</body>
</html>
'''
io.open('parent-guide-week-30.html', 'w', encoding='utf-8').write(week)

print('ok')
