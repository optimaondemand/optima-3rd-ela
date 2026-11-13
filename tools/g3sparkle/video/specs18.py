# Week 18 Opti films (Nov 13 2026): clips recorded Nov 13 (fd84364); Days 2-4 trimmed (tools/g3sparkle/video/trim.py).
from specs_wk19 import word, PILL
V18 = {}
V18['g3ela-18-1-teach-morph'] = dict(title='Morphology', sub='Word parts: inter and sub', scenes=[
 dict(at=None, items=[
   (None, '<div class="big">🏰</div>'),
   ('built from smaller parts', '<div class="say">Long words are built from <u>smaller parts</u>.</div>'),
   ("Today's parts are inter and sub", '<div class="chips"><span>inter</span><span>sub</span></div>'),
 ]),
 dict(at='Think of the internet', items=[
   (None, '<div class="build"><span class="wd">🌐 <b class="pt on">inter</b>net</span></div>'),
   ('It connects computers', '<div class="say">connects computers <u>between</u> each other</div>'),
   ('Now think of a subway', '<div class="build"><span class="wd">🚇 <b class="pt on">sub</b>way</span></div>'),
   ("It's a train that runs under", '<div class="say">a train that runs <u>under</u> the city</div>'),
 ], layout='words'),
 dict(at='So inter means between', items=[
   (None, '<div class="chips"><span>inter = between</span><span>sub = under</span></div>'),
   ('Tap See what each part means', PILL('See what each part means')),
   ('Then put the parts together', '<div class="build"><span class="tile">part</span><b>+</b><span class="tile">part</span><b>→</b><span class="tile"><i class="blank"></i></span></div>'),
 ]),
])
V18['g3ela-18-1-teach-vocab'] = dict(title='Vocabulary', sub='Be a word detective', scenes=[
 dict(at=None, items=[
   (None, '<div class="lab">🔍 Word detective</div>'),
   ("don't skip it", '<div class="say">Meet a new word? <u>Don\'t skip it!</u></div>'),
   ("Let's try exasperation", '<div class="huge">exasperation</div>'),
 ]),
 dict(at='First, read the sentence around it', items=[
   (None, '<div class="quote">“…he was feeling a growing <b class="hl">exasperation</b> with his whipping boy.”</div>'),
   ('The prince is pretending', '<div class="say">😇 outside … 😤 inside</div>'),
   ('Next, look at the parts', '<div class="build"><span class="tile">ex</span><span class="tile key">asper</span><span class="tile">ation</span></div>'),
   ('Asper means rough', '<div class="chips"><span>asper = rough</span></div>'),
 ]),
 dict(at='So exasperation is', items=[
   (None, '<div class="def"><b>exasperation</b><span>a rough, fed-up feeling 😤</span></div>'),
   ('Now tap Opti reads it', PILL('Opti reads it')),
   ('guess what the word means', '<div class="steps"><span><i>🔊</i>listen</span><span><i>🤔</i>guess</span><span><i>🃏</i>flip</span></div>'),
   ('Then play the matching game', PILL('Matching game')),
 ]),
])
V18['g3ela-18-1-teach-gram'] = dict(title='Grammar', sub='Joining words', scenes=[
 dict(at=None, items=[
   ('And, but, and so', '<div class="chips"><span>and</span><span>but</span><span>so</span></div>'),
   ('They glue two ideas', '<div class="say">🧴 They glue two ideas into one sentence.</div>'),
 ]),
 dict(at='And adds one more idea', items=[
   (None, '<div class="say">➕ I\'m hungry <b class="gold">and</b> I\'m tired.</div>'),
   ('But shows a difference', '<div class="say">↔️ I\'m hungry, <b class="gold">but</b> there\'s no food.</div>'),
   ('So shows what happens next', '<div class="say">➡️ I\'m hungry, <b class="gold">so</b> I\'ll eat.</div>'),
 ]),
 dict(at="Find the joining word in Jemmy's sentence", items=[
   (None, PILL('Find the joining word')),
   ('Then tap each sentence', '<div class="say">Tap a sentence, then drop it in <b class="gold">and</b>, <b class="gold">but</b> or <b class="gold">so</b>.</div>'),
   ('Say it out loud', '<div class="say">🗣️ Try each word. Which one fits?</div>'),
 ]),
])
V18['g3ela-18-1-teach-spell'] = dict(title='Spelling', sub='Vowel teams', scenes=[
 dict(at=None, items=[
   (None, '<div class="big">👫</div>'),
   ('Some vowels like to work in pairs', '<div class="say">Some vowels work in <u>pairs</u>.</div>'),
   ('we call them a vowel team', '<div class="huge">vowel team</div>'),
 ]),
 dict(at='In feast', items=[
   (None, '<div class="build"><span class="wd">f<b class="pt on">ea</b>st</span><b>→ ee</b></div>'),
   ('In groan', '<div class="build"><span class="wd">gr<b class="pt on">oa</b>n</span><b>→ oh</b></div>'),
 ]),
 dict(at='Say each word out loud', items=[
   (None, '<div class="say">🗣️ Say it. 👏 Clap the beats.</div>'),
   ('Then tap Now name the pattern', PILL('Now name the pattern')),
   ('Last, sort the words', '<div class="bins"><span>sort the words</span></div>'),
   ('Two vowels side by side', '<div class="say">Two vowels side by side? That\'s a team!</div>'),
 ]),
])
V18['g3ela-18-2-teach-morph'] = dict(title='Morphology', sub='Find the start first', scenes=[
 dict(at=None, items=[
   ('find the part at the start first', '<div class="build"><span class="tile key">1 start</span><span class="tile">2 the rest</span></div>'),
   ('then read the rest', '<div class="say">Find the start first. Then read the rest.</div>'),
 ]),
 dict(at='Tap a word in the game', items=[
   (None, '<div class="grid2"><span class="tile">a word</span><span class="tile m">its meaning</span><span class="tile">a word</span><span class="tile m">its meaning</span></div>'),
   ("If you're stuck", '<div class="say">🔑 Stuck? The first part is a big clue.</div>'),
 ]),
])
V18['g3ela-18-2-teach-vocab'] = dict(title='Vocabulary', sub='Detective, again', scenes=[
 dict(at=None, items=[
   ("Here's astonishment", '<div class="huge">astonishment 😲</div>'),
 ]),
 dict(at='Read the sentence', items=[
   (None, '<div class="quote">“Jemmy stared at him with dreadful <b class="hl">astonishment</b>.”</div>'),
   ('Jemmy just heard something', '<div class="say">He never expected that!</div>'),
 ]),
 dict(at='Now look at the parts', items=[
   (None, '<div class="build"><span class="tile">astonish</span><b>+</b><span class="tile">ment</span></div>'),
   ('Astonish means to surprise', '<div class="chips"><span>astonish = surprise</span><span>ment = a thing</span></div>'),
   ('So astonishment is', '<div class="def"><b>astonishment</b><span>a feeling of great surprise</span></div>'),
 ]),
])
V18['g3ela-18-2-teach-gram'] = dict(title='Grammar', sub='Joining-word spotter', scenes=[
 dict(at=None, items=[
   (None, '<div class="lab">🔭 Joining-word spotter</div>'),
   ('first tap the joining word', '<div class="quote q2">It started to rain, <span class="h1">so</span> <span class="h2">we went inside.</span></div>'),
   ('That part is the new idea', '<div class="say">That part is the <u>new idea</u>.</div>'),
 ], hl=[('first tap the joining word', '.h1'), ('Then tap the part of the sentence', '.h2')]),
 dict(at='Last, pick one sentence', items=[
   (None, '<div class="quote q2">It started to rain, <b class="gold">but</b> we kept playing.</div>'),
   ('Notice how the meaning changes', '<div class="say">🔄 New joining word, new meaning!</div>'),
 ]),
])
V18['g3ela-18-2-teach-spell'] = dict(title='Spelling', sub='Vowel team hunt', scenes=[
 dict(at=None, items=[
   (None, '<div class="lab">🔎 Vowel team hunt</div>'),
   ('Read the two sentences slowly', '<div class="quote q3"><span class="t1">Wait</span> for the <span class="t2">train</span> in the <span class="t3">rain</span>.</div>'),
   ("There's more than one", '<div class="say">More than one! Keep looking. 👀</div>'),
 ], hl=[('tap that word', '.t1'), ("There's more than one", '.t2'), ('keep looking', '.t3')]),
])
V18['g3ela-18-3-teach-morph'] = dict(title='Morphology', sub='Build the word', scenes=[
 dict(at=None, items=[
   ('Remember, inter means between', '<div class="chips"><span>inter = between</span><span>sub = under</span></div>'),
 ]),
 dict(at='Say each pair of parts', items=[
   (None, '<div class="build"><span class="tile">inter</span><b>+</b><span class="tile">rupt</span></div>'),
   ('interrupt', '<div class="huge">interrupt</div>'),
   ('Hear how the parts snap', '<div class="say">🧲 Snap! Two parts, one word.</div>'),
 ]),
 dict(at='Type the whole word', items=[
   (None, '<div class="build"><span class="tile"><i class="blank"></i></span></div>'),
   ('then tap Check My Answers', PILL('Check My Answers')),
   ('Look at the little meaning', '<div class="say">📝 The little meaning tells you what you built.</div>'),
 ]),
])
V18['g3ela-18-3-teach-vocab'] = dict(title='Vocabulary', sub='Use the word bank', scenes=[
 dict(at=None, items=[
   (None, '<div class="bubble"><b>The prince:</b> “…a clod and a <b class="hl">ruffian</b>!”</div>'),
   ("He's insulting him", '<div class="say">An insult ➜ someone rough and rude?</div>'),
   ('A ruffian is a rough', '<div class="def"><b>ruffian</b><span>a rough, violent person, a bully</span></div>'),
 ]),
 dict(at='Now the other words', items=[
   (None, '<div class="lab">The other words in the word bank</div>'),
   ('An exploit is', '<div class="say"><b class="gold">exploit</b> = a bold, daring act</div>'),
   ('An heir is', '<div class="say"><b class="gold">heir</b> = the one who will be king one day</div>'),
   ('And a ransom is', '<div class="say"><b class="gold">ransom</b> = money to set a prisoner free</div>'),
 ]),
 dict(at='Fill in each sentence', items=[
   (None, PILL('Check My Work')),
 ]),
])
V18['g3ela-18-3-teach-gram'] = dict(title='Grammar', sub='Do the joining', scenes=[
 dict(at=None, items=[
   ('Each pair has two short sentences', '<div class="build"><span class="tile">sentence.</span><span class="tile key">and / but / so</span><span class="tile">sentence.</span></div>'),
   ('Glue them into one', '<div class="say">🧴 Glue them into one.</div>'),
 ]),
 dict(at='Ask yourself', items=[
   ('am I adding an idea', '<div class="say">➕ Adding an idea? ➜ <b class="gold">and</b></div>'),
   ('Are the two ideas different', '<div class="say">↔️ Different or surprising? ➜ <b class="gold">but</b></div>'),
   ('Does the first thing cause', '<div class="say">➡️ First causes the second? ➜ <b class="gold">so</b></div>'),
 ]),
 dict(at='Read each one out loud', items=[
   (None, '<div class="say">🗣️ Read it out loud.</div>'),
   ('Then tap Check My Answers', PILL('Check My Answers')),
   ('write your own sentence', '<div class="say">✏️ Your own sentence about Chapter 5, with <b>but</b>.</div>'),
 ]),
])
V18['g3ela-18-3-teach-spell'] = dict(title='Spelling', sub='Never split the team', scenes=[
 dict(at=None, items=[
   (None, '<div class="lab">📏 Today\'s rule</div>'),
   ('never split the team', '<div class="big" style="font:700 64px Poppins">Never split the team!</div>'),
 ]),
 dict(at='Rain, bow', items=[
   (None, '<div class="build"><span class="wd">r<b class="pt on">ai</b>n · bow</span></div>'),
   ('Sea, son', '<div class="build"><span class="wd">s<b class="pt on">ea</b> · son</span></div>'),
 ]),
 dict(at='Look at each word', items=[
   ('find the vowel team', '<div class="steps"><span><i>1</i>find the team</span><span><i>2</i>where\'s the split?</span></div>'),
   ('Then tap the word to check', PILL('Tap the word to check')),
 ]),
])
V18['g3ela-18-4-teach-morph'] = dict(title='Morphology', sub='Roll the dice', scenes=[
 dict(at=None, items=[
   (None, '<div class="lab">One more time!</div>'),
   ('inter means between, sub means under', '<div class="chips"><span>inter = between</span><span>sub = under</span></div>'),
 ]),
 dict(at='Tap Roll the Dice', items=[
   (None, '<div class="big">🎲</div>'),
   ('find its first part', '<div class="build"><span class="tile key">first part</span><span class="tile">rest</span></div>'),
   ('Then tap Check My Thinking', PILL('Check My Thinking')),
   ('Keep rolling', '<div class="dots6">● ● ● ● ● ●</div>'),
 ]),
])
V18['g3ela-18-4-teach-vocab'] = dict(title='Vocabulary', sub='Use four words', scenes=[
 dict(at=None, items=[
   (None, '<div class="lab">📚 This week\'s words</div>'),
   ("Let's start with contrite", '<span class="wd">contrite</span>'),
   ('The prince lowered his head', '<div class="quote">“The prince lowered his head so as to appear humbled and <b class="hl">contrite</b>.”</div>'),
   ("He's trying to look sorry", '<div class="say">🎭 Trying to <u>look</u> sorry.</div>'),
 ]),
 dict(at='So contrite means', items=[
   (None, '<div class="def"><b>contrite</b><span>truly sorry for something you did wrong</span></div>'),
   ('Fill in each sentence', PILL('Check My Work')),
 ]),
])
V18['g3ela-18-4-teach-gram'] = dict(title='Grammar', sub='You check the work', scenes=[
 dict(at=None, items=[
   (None, '<div class="lab">🧑‍🏫 You\'re the teacher</div>'),
   ('Some of these sentences use the wrong', '<div class="quote q3">I was hungry, <span class="bad">but</span> I ate a snack.</div>'),
   ("If the joining word doesn't match", '<div class="say">Doesn\'t match the meaning? Tap it.</div>'),
 ], hl=[("If the joining word doesn't match", '.bad')]),
 dict(at='If the sentence is right', items=[
   (None, '<div class="build"><span class="pill">👆 the wrong word</span><b>or</b><span class="pill">👆 No mistake</span></div>'),
   ('Then tell which sentence', '<div class="say">✏️ Which one had no mistake? How did you know?</div>'),
 ]),
])
V18['g3ela-18-4-teach-spell'] = dict(title='Spelling', sub='Roll and split', scenes=[
 dict(at=None, items=[
   (None, '<div class="big">🎲</div>'),
   ('Tap Roll the dice', PILL('Roll the dice')),
   ('say it out loud and clap', '<div class="say">🗣️ Say it. 👏 Clap it.</div>'),
 ]),
 dict(at='Find the vowel team', items=[
   (None, '<div class="say">The team never splits.</div>'),
   ('Meadow', '<div class="build"><span class="wd">m<b class="pt on">ea</b>d · ow</span></div>'),
   ('Then tap Check my answer', PILL('Check my answer')),
 ]),
])
V18['g3ela-18-2-teach-rwm'] = dict(title='Read Like a Writer', sub='Three parts', scenes=[
 dict(at=None, items=[
   ("Here's how Read Like a Writer works", '<div class="steps"><span><i>1</i>Reader</span><span><i>2</i>Writer</span><span><i>3</i>Mimic</span></div>'),
   ('Like a snake striking', '<div class="quote">“Like a snake striking, a ghostly hand darted through the fog and clutched his arm.”<small>Chapter 4</small></div>'),
 ]),
 dict(at='Part one', items=[
   (None, '<div class="step1"><i>1</i> Read like a Reader</div>'),
   ('What is happening', '<div class="ask">🤔 What is happening?</div>'),
   ('Someone in the fog grabs', '<div class="say">Someone in the fog grabs Jemmy, <u>fast</u>.</div>'),
 ]),
 dict(at='Part two', items=[
   (None, '<div class="step1"><i>2</i> Read like a Writer</div>'),
   ('What is the author doing', '<div class="quote">“<b class="hl">Like a snake striking</b>, a ghostly hand darted…”</div>'),
   ('He says the hand moves', '<div class="say">🐍 We feel how <u>quick</u> and <u>scary</u> it is.</div>'),
 ]),
 dict(at='Part three', items=[
   (None, '<div class="step1"><i>3</i> Mimic</div>'),
   ("Here's mine", '<div class="quote mine"><b class="hl">Like a cat pouncing</b>, my little sister grabbed the last cookie.</div>'),
   ("Now it's your turn", '<div class="say">✏️ Your turn: the fog sentence.<br>One sentence in each box.</div>'),
 ]),
])
