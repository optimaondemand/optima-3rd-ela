"""Week 29 family guide (unit guide is week 25's). Head/CSS and How the Lesson Pages Work from week 22 (a novel week with a
fluency page); bodies from the finished week 29 lessons, DATA and the S&S v4 rows 29-30. Run from the repo root.
Ch. 14 (Aslan's death on the Stone Table) is named plainly in Good to Know (Bethany, Nov 15 2026)."""
import io
s = io.open('parent-guide-week-22.html', encoding='utf-8').read()
H0 = s[:s.index('<body>')]
howto = s[s.index('<section class="howto">'):s.index('</section>', s.index('<section class="howto">')) + 10]
assert 'Fluency' in howto
OWL = 'https://raw.githubusercontent.com/optimaondemand/optima-assets/eeb0b335630058906d52f478028361d352253a93/images/Optima%20Final%20Circle%20-%20Owl%20Only.png'
ART = 'https://optimaondemand.github.io/optima-3rd-ela/assets/art/lww/'
def w(a, b): return '<div class="word"><b>%s</b><span>%s</span></div>' % (a, b)
WORDS = [('traitor', 'someone who betrays the trust of their own side'), ('atone', 'to make up for a wrong you have done'),
         ('sacrifice', 'giving up something precious for something or someone more important'), ('resurrection', 'coming back to life after death')]
UNIT = '<p class="unit-link"><a href="parent-guide-lww-unit.html">Read the unit guide for The Lion, the Witch and the Wardrobe →</a></p>'

week = H0.replace('Week 22 Family Guide · The Whipping Boy · 3rd Grade ELA', 'Week 29 Family Guide · The Lion, the Witch and the Wardrobe · 3rd Grade ELA')
assert 'Week 29 Family Guide' in week
week += '''<body>
<div class="wrap">

<header class="hero">
<div class="hero-text">
<div class="brand"><img src="''' + OWL + '''" alt="Optima Academy Online">Family Guide · 3rd Grade ELA</div>
<h1>Week 29: Deep Magic, Deeper Magic</h1>
<div class="sub"><em>The Lion, the Witch and the Wardrobe</em>, Chapters 13–15: finding the theme with details from across the whole story</div>
<div class="chips">
<span class="chip">4 lessons</span>
<span class="chip">Chapters 13–15</span>
<span class="chip">Fluency page</span>
<span class="chip">Check-In at week’s end</span>
</div>
<button class="print-btn" onclick="window.print()">🖨️ Print this guide</button>
''' + UNIT + '''
</div>
<div class="hero-art" style="background-image:url(\'''' + ART + '''lww-impression-sunrise.jpg');background-position:center 50%;" role="img" aria-label="A painting of a misty harbor at sunrise, with a small orange sun and its reflection on the water"></div>
</header>

''' + howto + '''

<section class="card">
<div class="card-head"><span class="ico">🧭</span><h2>This Week at a Glance</h2></div>
<p>In Chapter 13, Aslan’s rescuers save Edmund from the Witch, and Aslan tells the others there is no need to talk about what is past. Then the Witch comes to claim Edmund under the Deep Magic, an old law that says every traitor belongs to her. Aslan talks with her alone, and she gives up her claim. In Chapter 14 we learn the price: Aslan gives his own life in Edmund’s place. Chapter 15 begins on that sad night and ends at sunrise, when the Stone Table cracks and Aslan is alive again, because of a deeper magic the Witch did not know. Day 1 reads Chapter 13, Day 2 Chapter 14, Day 3 Chapter 15, and Day 4 looks back at the whole book so far.</p>
<div class="glance">
<div class="box b-sky"><div class="box-label">Reading skill</div><strong>Explaining the theme.</strong> A theme is the big lesson a story teaches, said as a full sentence. A topic is one word, like <em>loyalty</em>. Good readers back up a theme with details from the beginning, the middle and the end.</div>
<div class="box b-green"><div class="box-label">Big idea</div><strong>What is the most important proof for your theme across the whole book?</strong> Edmund’s betrayal, his rescue and forgiveness, and Aslan’s choice all point to the same big lesson.</div>
</div>
<p class="quote">“Though the Witch knew the Deep Magic, there is a magic deeper still which she did not know.”<small>Aslan, Chapter 15</small></p>
</section>

<section class="card">
<div class="card-head"><span class="ico">📅</span><h2>Day by Day</h2></div>
<table class="days">
<thead><tr><th>Lesson</th><th>Reading</th><th>Big question</th></tr></thead>
<tbody>
<tr><td class="day-n">29.1<span>Day 1</span></td>
<td><span class="ch">Chapter 13: Deep Magic From the Dawn of Time</span><br>Your student explains the Deep Magic, guesses what Aslan offered the Witch, and brainstorms two or three possible themes.<br><span class="pill p-guide">Guide: Opti</span><span class="pill p-extra">Sentence rewrite</span></td>
<td>What is the difference between a topic and a theme in a story?</td></tr>
<tr><td class="day-n">29.2<span>Day 2</span></td>
<td><span class="ch">Chapter 14: The Triumph of the Witch</span><br>Your student tells what happens at the Stone Table and how Lucy and Susan stay loyal, then drafts a literary response on theme.<br><span class="pill p-guide">Guide: Opti</span><span class="pill p-poem">Poetry</span><span class="pill p-extra">Read Like a Writer video</span></td>
<td>How can you find proof for a theme by looking at what happens to characters across the whole story?</td></tr>
<tr><td class="day-n">29.3<span>Day 3</span></td>
<td><span class="ch">Chapter 15: Deeper Magic From Before the Dawn of Time</span><br>Your student explains the Deeper Magic and how Lucy and Susan feel at sunrise, then adds proof from Chapter 15 to the response.<br><span class="pill p-guide">Guide: Opti</span><span class="pill p-extra">Read Like a Writer</span></td>
<td>How does the Deeper Magic in Chapter 15 change what everything before it means?</td></tr>
<tr><td class="day-n">29.4<span>Day 4</span></td>
<td><span class="ch">Look back: the whole book so far</span><br>Your student writes the theme as a full sentence, picks three moments from different chapters, and finishes the literary response.<br><span class="pill p-guide">Guide: Opti</span><span class="pill p-poem">Poetry</span><span class="pill p-extra">Read Like a Writer</span></td>
<td>What is the most important proof for your theme across the whole book so far?</td></tr>
<tr class="extra-row"><td class="day-n">🎙️<span>Fluency</span></td>
<td colspan="2">A quiet passage from Chapter 14: Lucy and Susan walk beside Aslan in the moonlight, and he tells them, “I am sad and lonely.” Your student reads it three times (right words, then smooth, then slow and gentle, letting the girls’ questions sound worried), then <strong>records and submits in Canvas.</strong></td></tr>
<tr class="extra-row"><td class="day-n">📋<span>Check-In</span></td>
<td colspan="2">A 14-point check on the week, in Canvas: punctuating dialogue, the root ject, long words built from parts, a short passage from Chapter 15, and a short writing response on theme.</td></tr>
</tbody>
</table>
</section>

<section class="card">
<div class="card-head"><span class="ico">🔤</span><h2>Words to Know</h2><span class="tag">Use them at home!</span></div>
<div class="words">
''' + '\n'.join(w(a, b) for a, b in WORDS) + '''
</div>
<div class="skills">
<div class="box b-sky"><div class="box-label">Word parts</div>The root <strong>ject</strong> means <strong>throw</strong>. The part in front tells which way.<span class="eg">reject (back) · inject (into) · eject (out) · project (forward)</span></div>
<div class="box b-gold"><div class="box-label">Spelling</div>Long words are often a <strong>root</strong> with parts added to the front, the end, or both. Find the root first.<span class="eg">un + expect + ed = unexpected</span></div>
<div class="box b-green"><div class="box-label">Grammar</div>In <strong>dialogue</strong>, quotation marks go around the exact words, the first word gets a capital, and the comma or period goes inside the closing mark.<span class="eg">“Let him approach,” said Aslan.</span></div>
</div>
</section>

<section class="card">
<div class="card-head"><span class="ico">✨</span><h2>New in the Lessons</h2></div>
<div class="extras">
<div class="box b-plum"><div class="box-label">🪨 Skipping Stones</div>This week’s word game is a river at a shallow crossing. On Days 1 and 2 your student reads a sentence with a ject word and taps which way something is thrown: back, into, out or forward. On Days 3 and 4 they find the root in the middle of a long word: ject, script or scribe, spect, or port. Each right answer skips a stone into the river, and by Day 4 the stepping stones fill the crossing.</div>
<div class="box b-gold"><div class="box-label">🎬 Opti’s videos</div>Every Word Study activity, all four days, starts with a short video where Opti shows how it works. On Day 2, Opti also shows Read Like a Writer with a gentle sentence from Chapter 14. The videos have captions for now; Opti’s voice will be added later.</div>
<div class="box b-sky"><div class="box-label">🌍 World Notes</div>Each day opens the Reading tab with a real thing behind the story: how far a real lion’s roar carries, real stone tables called dolmens built more than 5,000 years ago, field mice and the morning star (the planet Venus), and why male lions grow manes.</div>
<div class="box b-green"><div class="box-label">🏮 Truth Watch</div>After reading, your student decides if three moments show someone being honest: Yes or Not yet. This week includes Edmund saying “I’m sorry,” Aslan refusing to make a promise he may not keep, and the Witch hiding by making herself look like a rock.</div>
</div>
<p class="small" style="margin-top:12px;">Each day opens with real art, never pictures from the book: Caspar David Friedrich’s <em>Dolmen in the Snow</em> (1807) and <em>Moonrise over the Sea</em> (1822), Claude Monet’s <em>Impression, Sunrise</em> (1872), and Rosa Bonheur’s <em>Portrait of a Lion</em> (1879). Your student looks first, then taps to learn about it.</p>
</section>

<section class="card">
<div class="card-head"><span class="ico">⚠️</span><h2>Good to Know</h2></div>
<p><strong>This is the hardest week of the book.</strong> At the start of Chapter 13, the Witch has Edmund tied to a tree and gets ready to kill him, but Aslan’s rescuers arrive in time. In Chapter 14, Aslan dies. He walks to the Stone Table at night and lets the Witch and her creatures tie him up, shave his mane, make fun of him, and then the Witch kills him with a knife, in Edmund’s place. Lucy and Susan watch from the bushes and cover their eyes at the moment he dies. Chapter 15 begins with the girls crying beside him through the night. At sunrise the Stone Table cracks, and Aslan is alive again.</p>
<p>The lessons keep all of this gentle: Opti tells students before Chapter 14 that it is the saddest chapter, that it is okay to feel sad, and that the story is not over yet. Your student may want to read Chapter 14 with you, or to know ahead of time that Aslan comes back to life in Chapter 15. It is fine to tell them. The <a href="parent-guide-lww-unit.html">unit guide</a> has more about this part of the book.</p>
</section>

<section class="card">
<div class="card-head"><span class="ico">✍️</span><h2>Your Student’s Writing</h2><span class="tag">Writer’s Workshop</span></div>
<div class="essay"><span>Wk 28 · Add a symbol paragraph</span><span class="now">Wk 29 · A literary response on theme</span></div>
<p>This week your student writes a literary response about the story’s theme. Day 1: <strong>brainstorm</strong> two or three possible themes, each as a full sentence that starts “The story shows that…”. Day 2: <strong>draft</strong> the response with proof from two parts of the story. Day 3: <strong>revise</strong> by adding two sentences of proof from Chapter 15. Day 4: <strong>finish</strong> the whole response, with proof from three different chapters and a closing sentence.</p>
<p class="small">An example writer named Clara shows each step first.</p>
</section>

<section class="card">
<div class="card-head"><span class="ico">💬</span><h2>Ask at Home</h2></div>
<ol class="ask">
<li><span class="q">What is the difference between a topic and a theme?</span><span class="listen">Listen for: a topic is a word, like loyalty; a theme is a full sentence about it, like “The story shows that…”.</span></li>
<li><span class="q">What did Aslan say to the others about Edmund after the rescue?</span><span class="listen">Listen for: there is no need to talk about what is past; they forgave him.</span></li>
<li><span class="q">What was the Deeper Magic the Witch did not know?</span><span class="listen">Listen for: when someone who did nothing wrong gives his life for a traitor, death works backwards.</span></li>
<li><span class="q">Where does the comma go in “Let him approach, said Aslan”?</span><span class="listen">Listen for: inside the closing quotation mark, after approach.</span></li>
</ol>
</section>

<div class="two">
<section class="card">
<div class="card-head"><span class="ico">📬</span><h2>What Gets Turned In</h2></div>
<ul class="check">
<li>Each lesson’s Assignment tab: the chapter questions and the day’s writing step, copied and pasted into Canvas</li>
<li>The Week 29 fluency recording</li>
<li>The Week 29 Check-In in Canvas</li>
</ul>
</section>
<section class="card">
<div class="card-head"><span class="ico">🏡</span><h2>Try at Home</h2></div>
<ul class="check">
<li>Name the theme of a favorite movie or family story as one sentence: “The story shows that…”</li>
<li>Throw a soft ball back, out, and forward, and name the ject word each time: reject, eject, project</li>
<li>Write a short conversation between two family members, with quotation marks and commas in the right places</li>
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
<div class="card-head"><span class="ico">⏭️</span><h2>Coming Up in Week 30</h2></div>
<p><strong>Chapters 16–17, the end of the book.</strong> Reading skill: how the ending shows the theme. Word study: a review of the roots and word parts from the whole year. Writing: the final revision of the literary response.</p>
</section>

<p class="foot">Optima Academy Online · 3rd Grade ELA · Week 29 Family Guide</p>
</div>
</body>
</html>
'''
io.open('parent-guide-week-29.html', 'w', encoding='utf-8').write(week)

print('ok')
