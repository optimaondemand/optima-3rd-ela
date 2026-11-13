# Scene specs for the week 20 Opti teach videos (The Whipping Boy, Ch. 11-15).
# Each item appears when Opti says its anchor (a phrase from the script). Scripts = DATA.teach.
# Never shows an answer the page asks for: examples are spectacular, prospector, hamburger,
# fantastic, helicopter, bacon/cake, Captain Nips, and the Ch. 14 brambles sentence.
def word(w, part=None, cls=''):
    if part:
        i = w.index(part)
        return '<span class="wd %s">%s<b class="pt">%s</b>%s</span>' % (cls, w[:i], part, w[i+len(part):])
    return '<span class="wd %s">%s</span>' % (cls, w)
PILL = lambda t: '<span class="pill">👆 %s</span>' % t
V = {}
# ---------------- Day 1: teach the idea ----------------
V['g3ela-20-1-teach-morph'] = dict(title='Morphology', sub='Crack the hidden root', scenes=[
 dict(at=None, items=[
   (None, '<div class="lab">🧩 A puzzle</div>'),
   ('Inspect', word('inspect', 'spect')), ('Spectator', word('spectator', 'spect')), ('Respect', word('respect', 'spect')),
   ('What five letters', '<div class="ask">🤔 What five letters hide in all three?</div>'),
 ], hl=[('What five letters', '.pt')], layout='words'),
 dict(at='Now picture a spectator', items=[
   (None, '<div class="big">🏟️ ⚾ 👀</div>'),
   ('What is a spectator doing', '<div class="ask">What is a spectator doing the whole time?</div>'),
   ('Watching', '<div class="huge">Watching! 👀</div>'),
   ('So what could that hidden part mean', '<div class="huge"><b class="gold">spect</b> = ?</div>'),
 ]),
 dict(at='Tap See if you were right', items=[
   (None, PILL('See if you were right')),
   ('type the missing part', '<div class="boxes"><span class="wd">in<i class="blank"></i></span><span class="wd">sus<i class="blank"></i></span><span class="wd">ex<i class="blank"></i></span></div>'),
   ('Careful with suspect', '<div class="say">⚠️ sus·pect · ex·pect<br>Say them slowly. Listen for the <b>s</b>.</div>'),
 ]),
])
V['g3ela-20-1-teach-vocab'] = dict(title='Vocabulary', sub='Be a word detective', scenes=[
 dict(at=None, items=[
   (None, '<div class="lab">🔍 Word detective</div>'),
   ('Back in Chapter 8', '<div class="quote">“Hold-Your-Nose Billy\'s red eyebrows shot up in <b class="hl">bewildered</b> surprise.”<small>Chapter 8</small></div>'),
   ('Jemmy had just shocked him', '<div class="say">😲 Jemmy just shocked him.</div>'),
 ]),
 dict(at='Now the parts', items=[
   (None, '<div class="build"><span class="tile">be</span><b>+</b><span class="tile">wilder</span><b>+</b><span class="tile">ed</span></div>'),
   ('Wilder is an old word', '<div class="say">🌲 wilder = lost in a wild place</div>'),
   ('So bewildered means', '<div class="def"><b>bewildered</b><span>so confused you feel lost</span></div>'),
 ]),
 dict(at='Now tap Opti reads it', items=[
   (None, PILL('Opti reads it')),
   ('Guess, then flip', '<div class="steps"><span><i>🔊</i>listen</span><span><i>🤔</i>guess</span><span><i>🃏</i>flip</span></div>'),
   ('Then play the matching game', PILL('Matching game')),
 ]),
])
V['g3ela-20-1-teach-gram'] = dict(title='Grammar', sub='Prepositions', scenes=[
 dict(at=None, items=[
   (None, '<div class="lab">Two sentences</div>'),
   ('Leaves crackled. Leaves', '<div class="quote">Leaves crackled.</div>'),
   ('Leaves crackled under', '<div class="quote">Leaves crackled <b class="hl">under</b> Jemmy\'s feet.</div>'),
   ('What did the second one add', '<div class="ask">🤔 What did the second one add?</div>'),
 ]),
 dict(at='Under is a preposition', items=[
   (None, '<div class="huge"><b class="gold">under</b></div>'),
   ('Under is a preposition', '<div class="say">is a <b>preposition</b></div>'),
   ('It sits in front of a noun', '<div class="eq"><span class="th">preposition</span><span class="glue">+</span><span class="th">noun</span></div>'),
   ('Some prepositions tell where', '<div class="col">Where?</div>'),
   ('Some tell when', '<div class="col">When?</div>'),
   ('Some tell how', '<div class="col">How?</div>'),
 ]),
 dict(at='Tap Now check your thinking', items=[
   (None, PILL('Now check your thinking')),
   ('Then tap each phrase', PILL('Tap a phrase, then its question')),
 ]),
])
V['g3ela-20-1-teach-spell'] = dict(title='Spelling', sub='Long words, small chunks', scenes=[
 dict(at=None, items=[
   (None, '<div class="lab">👏 Clap with me</div>'),
   ('Im, por, tant', '<div class="huge">im · por · tant</div>'),
   ('Three beats', '<div class="say">👏 👏 👏 Three beats!</div>'),
 ]),
 dict(at='A long word is just small chunks', items=[
   (None, '<div class="steps"><span><i>1</i>find the vowels</span><span><i>2</i>split</span><span><i>3</i>read each chunk</span><span><i>4</i>push together</span></div>'),
   ('Say the words in Group A', '<div class="say">🗣️ Say and clap Group A and Group B.</div>'),
   ('Tap See the Rule', PILL('See the Rule')),
 ]),
 dict(at='Then sort the six words', items=[
   (None, '<div class="bins"><span>Only closed or r-controlled</span><span>Open syllable or silent e</span></div>'),
   ('like ba in bacon', '<div class="say">open: <b>ba</b>·con</div>'),
   ('like cake', '<div class="say">silent e: cak<b>e</b></div>'),
 ]),
])
# ---------------- Day 2 ----------------
V['g3ela-20-2-teach-morph'] = dict(title='Morphology', sub='Match the word to its meaning', scenes=[
 dict(at=None, items=[
   (None, '<div class="chips"><span>spect = look</span></div>'),
   ('Spectacular. Find spect', word('spectacular', 'spect')),
   ('The fireworks were spectacular', '<div class="big">🎆 👀 🎆</div>'),
   ('So amazing', '<div class="say">So amazing that everybody had to <u>look</u>!</div>'),
 ], hl=[('Spectacular. Find spect', '.pt')]),
 dict(at='Do the same with each word', items=[
   (None, '<div class="grid2"><span class="tile">a word</span><span class="tile m">its meaning</span><span class="tile">a word</span><span class="tile m">its meaning</span></div>'),
   ('then tap the meaning', PILL('Tap a word, then its meaning')),
 ]),
])
V['g3ela-20-2-teach-vocab'] = dict(title='Vocabulary', sub='Listen, guess, flip', scenes=[
 dict(at=None, items=[
   (None, '<span class="wd">instinct</span>'),
   ('Jemmy acted on instinct', '<div class="quote">“A thoroughbred of the streets, Jemmy acted on <b class="hl">instinct</b>.”<small>Chapter 13</small></div>'),
   ("He just ran", '<div class="say">🏃 No stopping to think. He just ran!</div>'),
   ('Instinct is what you do', '<div class="say">⚡ before your brain catches up</div>'),
 ]),
 dict(at='Listen to each card', items=[
   (None, '<div class="steps"><span><i>🔊</i>listen</span><span><i>🤔</i>guess</span><span><i>🃏</i>flip</span></div>'),
   ('Then match all four', PILL('Match all four')),
 ]),
])
V['g3ela-20-2-teach-gram'] = dict(title='Grammar', sub='Find every preposition', scenes=[
 dict(at=None, items=[
   (None, '<div class="lab">🔎 Listen</div>'),
   ('The prince ran across', '<div class="quote q3">The prince ran <span class="p1">across</span> the clearing <span class="p2">to</span> the edge <span class="p3">of</span> the woods.</div>'),
   ('Three!', '<div class="huge">3 prepositions!</div>'),
 ], hl=[('Across. To', '.p1'), ('To. Of', '.p2'), ('Of. Three', '.p3')]),
 dict(at='Tap Check yourself', items=[
   (None, PILL('Check yourself')),
   ('Then tap every preposition', PILL('Tap every preposition')),
   ('Keep going until', '<div class="say">More than one in each sentence. Find them all!</div>'),
 ]),
])
V['g3ela-20-2-teach-spell'] = dict(title='Spelling', sub='Sound Detective', scenes=[
 dict(at=None, items=[
   ('ham, bur, ger', '<div class="huge">ham · bur · ger 🍔</div>'),
   ('Three beats', '<div class="say">👏 👏 👏</div>'),
 ]),
 dict(at='In each row', items=[
   (None, '<div class="row4"><span class="tile">👏👏</span><span class="tile">👏👏</span><span class="tile on2">👏👏👏</span><span class="tile">👏👏</span></div>'),
   ('Clap every word', PILL('Tap the one with three beats')),
 ]),
])
V['g3ela-20-2-teach-rwm'] = dict(title='Read Like a Writer', sub='Three parts', scenes=[
 dict(at=None, items=[
   ('has three parts', '<div class="steps"><span><i>1</i>Reader</span><span><i>2</i>Writer</span><span><i>3</i>Mimic</span></div>'),
   ('Brambles, reaching out', '<div class="quote">“Brambles, reaching out like cat\'s claws, tore at their fine garments.”<small>Chapter 14</small></div>'),
 ]),
 dict(at='Part one', items=[
   (None, '<div class="step1"><i>1</i> Read like a Reader</div>'),
   ('What is happening', '<div class="ask">🤔 What is happening?</div>'),
   ('The boys push through', '<div class="say">🌿 Thorny bushes rip the boys\' fancy clothes.</div>'),
 ]),
 dict(at='Part two', items=[
   (None, '<div class="step1"><i>2</i> Read like a Writer</div>'),
   ('What does the author do', '<div class="quote">“Brambles, reaching out <b class="hl">like cat\'s claws</b>…”</div>'),
   ('so we can almost feel', '<div class="say">🐾 We can almost <u>feel</u> the scratch.</div>'),
 ]),
 dict(at='Part three', items=[
   (None, '<div class="step1"><i>3</i> Mimic</div>'),
   ('The snow, stinging', '<div class="quote mine">The snow, stinging <b class="hl">like tiny bees</b>, bit at my cheeks. ❄️</div>'),
   ("Now it's your turn", '<div class="say">✏️ Your turn: the chase sentence.<br>One sentence in each box.</div>'),
 ]),
])
# ---------------- Day 3 ----------------
V['g3ela-20-3-teach-morph'] = dict(title='Morphology', sub='Build the word', scenes=[
 dict(at=None, items=[
   ('Pro, plus spect', '<div class="build"><span class="tile">pro</span><b>+</b><span class="tile">spect</span><b>+</b><span class="tile">or</span></div>'),
   ('Prospector', '<div class="huge">prospector ⛏️✨</div>'),
   ('A person who looks for gold', '<div class="say">a person who <u>looks</u> for gold</div>'),
 ]),
 dict(at='The last word on your page', items=[
   (None, '<div class="build"><span class="tile">part</span><b>+</b><span class="tile">spect</span><b>+</b><span class="tile">part</span></div>'),
   ('Push all three together', '<div class="say">Three parts? Push all three together.</div>'),
   ('Type the whole word', '<div class="build"><span class="say">⌨️</span><span class="tile"><i class="blank"></i></span></div>'),
   ('Then tap Check My Answers', PILL('Check My Answers')),
 ]),
])
V['g3ela-20-3-teach-vocab'] = dict(title='Vocabulary', sub='Use the word bank', scenes=[
 dict(at=None, items=[
   (None, '<div class="bubble"><b>Prince:</b> “What are you doing?”</div>'),
   ('Mudlarking', '<div class="bubble"><b>Jemmy:</b> “<b class="hl">Mudlarking.</b>”</div>'),
   ('Mud, plus lark', '<div class="build"><span class="tile">mud</span><b>+</b><span class="tile">lark</span><b>+</b><span class="tile">ing</span></div>'),
   ('which means to poke about', '<div class="say">lark = poke about 🔍</div>'),
 ]),
 dict(at='Read how we figured out', items=[
   (None, '<div class="say">Try each bank word in the ▁▁▁▁</div>'),
   ('tap Check My Work', PILL('Check My Work')),
   ('Last, play the matching game', PILL('Matching game')),
 ]),
])
V['g3ela-20-3-teach-gram'] = dict(title='Grammar', sub='Pick the preposition', scenes=[
 dict(at=None, items=[
   (None, '<div class="lab">Same coach, three places</div>'),
   ('The coach rolled into', '<div class="quote">The coach rolled <b class="hl">into</b> the mud. 🛑</div>'),
   ('The coach rolled through', '<div class="quote">The coach rolled <b class="hl">through</b> the mud. ➡️</div>'),
   ('The coach rolled past', '<div class="quote">The coach rolled <b class="hl">past</b> the mud. ↗️</div>'),
   ('Only one word changed', '<div class="say">Only <u>one</u> word changed!</div>'),
 ]),
 dict(at='Now read each sentence', items=[
   (None, '<div class="quote">They walked ▁▁▁▁ the hill. <small>(tells where)</small></div>'),
   ('where, when, or how', '<div class="chips"><span>where</span><span>when</span><span>how</span></div>'),
   ('Type the bank word', PILL('Type the bank word that fits')),
 ]),
])
V['g3ela-20-3-teach-spell'] = dict(title='Spelling', sub='Build with tiles', scenes=[
 dict(at=None, items=[
   ("Here's a word in pieces", '<div class="build"><span class="tile">tic</span><span class="tile">fan</span><span class="tile">tas</span></div>'),
   ("That's the wrong order", '<div class="say">❌ Wrong order!</div>'),
   ('Clap it first', '<div class="build"><span class="tile">fan</span><span class="tile">tas</span><span class="tile">tic</span></div>'),
   ('Fantastic', '<div class="huge">fantastic! ⭐</div>'),
 ]),
 dict(at='Now tap the chunks in order', items=[
   (None, '<div class="steps"><span><i>1</i>first</span><span><i>2</i>middle</span><span><i>3</i>last</span></div>'),
   ("If a chunk won't stick", '<div class="say">Won\'t stick? Try another one.</div>'),
 ]),
])
# ---------------- Day 4 ----------------
V['g3ela-20-4-teach-morph'] = dict(title='Morphology', sub='Roll and tell', scenes=[
 dict(at=None, items=[
   (None, '<div class="big">🎲</div>'),
   ('Every word on the dice', '<div class="say">Every word has <b class="gold">spect</b> = look 👀</div>'),
   ('Look at the parts around spect', '<div class="build"><span class="tile key">?</span><span class="tile">spect</span><span class="tile key">?</span></div>'),
   ('They tell you what kind', '<div class="say">🔑 They tell you what kind of looking.</div>'),
 ]),
 dict(at='Say what the whole word means', items=[
   (None, '<div class="say">🗣️ Say what it means.</div>'),
   ('Then tap Check My Thinking', PILL('Check My Thinking')),
   ('Do all six', '<div class="dots6">● ● ● ● ● ●</div>'),
 ]),
])
V['g3ela-20-4-teach-vocab'] = dict(title='Vocabulary', sub='Review the week', scenes=[
 dict(at=None, items=[
   (None, '<div class="bubble"><b>Jemmy:</b> “I can\'t have you sticking to me like a <b class="hl">barnacle</b>!”</div>'),
   ("That's Jemmy, grumbling", '<div class="say">Chapter 14 😤</div>'),
   ('A barnacle is a little sea creature', '<div class="def"><b>barnacle</b><span>a little sea creature that glues itself to ships 🐚⛵</span></div>'),
 ]),
 dict(at='Now read each sentence', items=[
   (None, '<div class="say">🗣️ Read it out loud with a bank word in the ▁▁▁▁</div>'),
   ('If it sounds right', '<div class="say">Sounds right? ✔ Keep it.</div>'),
 ]),
])
V['g3ela-20-4-teach-gram'] = dict(title='Grammar', sub='Spot the wrong preposition', scenes=[
 dict(at=None, items=[
   ('Captain Nips sat under', '<div class="quote q3">Captain Nips sat <span class="bad">under</span> his coach and drove away.</div>'),
   ("He'd be in the mud", '<div class="big">🛞 🙃 🟫</div>'),
   ('He sat on his coach', '<div class="quote q3 good">Captain Nips sat <b class="hl">on</b> his coach. ✔</div>'),
 ], hl=[('Wait, under', '.bad')]),
 dict(at="That's a preposition doing the wrong job", items=[
   (None, '<div class="say">🖼️ Read it. Picture it.</div>'),
   ('Tap the wrong word', '<div class="build"><span class="pill">👆 the wrong word</span><b>or</b><span class="pill">👆 No mistake</span></div>'),
 ]),
])
V['g3ela-20-4-teach-spell'] = dict(title='Spelling', sub='Roll and split', scenes=[
 dict(at=None, items=[
   ('Hel, i, cop, ter', '<div class="huge">hel · i · cop · ter 🚁</div>'),
   ('Four beats', '<div class="say">👏 👏 👏 👏 Four beats.</div>'),
 ]),
 dict(at='Tap Roll the dice', items=[
   (None, '<div class="big">🎲</div>'),
   ('Say the word out loud', '<div class="say">🗣️ Say it. Split it.</div>'),
   ('Then tap Check my answer', PILL('Check my answer')),
   ('Roll all six words', '<div class="dots6">● ● ● ● ● ●</div>'),
 ]),
])
