# Scene specs for the week 23 Opti teach videos (Medieval Nonfiction, part 1).
# Each item appears when Opti says its anchor (a phrase from the script). Scripts = DATA.teach.
# Never shows an answer the page asks for: examples are transpacific/tranquil, transcontinental, transit,
# transcribe; chamber, guild, Majesty, trencher; Robin Hood / Sherwood Forest / The Wind in the Willows,
# abbot peter / bath abbey, earl roger / ireland, "a Castle on the hill"; puppet, doctor, garlic, window;
# and the 23.2 article line "Poor children worked in the fields or served in the homes of nobles."
def word(w, part=None, cls=''):
    if part:
        i = w.index(part)
        return '<span class="wd %s">%s<b class="pt">%s</b>%s</span>' % (cls, w[:i], part, w[i+len(part):])
    return '<span class="wd %s">%s</span>' % (cls, w)
PILL = lambda t: '<span class="pill">👆 %s</span>' % t
V = {}
# ---------------- Day 1: teach the idea ----------------
V['g3ela-23-1-teach-morph'] = dict(title='Morphology', sub='A word part that means across', scenes=[
 dict(at=None, items=[
   (None, '<div class="ask">🤔 Have you ever walked across a bridge?</div>'),
   ('You start on one side', '<div class="big">🧍 🌉 ➡️ 🧍</div>'),
 ]),
 dict(at="There's a word part", items=[
   (None, '<div class="huge">trans</div>'),
   ('T, r, a, n, s', '<div class="say">t · r · a · n · s</div>'),
   ('Trans, plus Pacific', '<div class="build"><span class="tile key">trans</span><b>+</b><span class="tile">Pacific</span></div>'),
   ('across the Pacific Ocean', '<div class="def"><b>transpacific</b><span>across the Pacific Ocean 🌊</span></div>'),
 ]),
 dict(at='But careful', items=[
   (None, '<div class="lab">⚠️ Careful!</div>'),
   ('Tranquil starts', word('tranquil', 'tran')),
   ('it just means calm', '<div class="say">tranquil = calm 😌<br>Nothing goes across. ❌</div>'),
 ]),
 dict(at='Read the three words', items=[
   (None, '<div class="say">📖 Read the three words. Think about the questions.</div>'),
   ('Then tap See if you cracked it', PILL('See if you cracked it')),
   ('type the missing parts', '<div class="build"><span class="tile key">trans</span><b>+</b><span class="tile"><i class="blank"></i></span></div>'),
 ]),
])
V['g3ela-23-1-teach-vocab'] = dict(title='Vocabulary', sub='Be a word detective', scenes=[
 dict(at=None, items=[
   (None, '<div class="lab">🔍 Word detective</div>'),
   ('Chamber', '<div class="huge">chamber</div>'),
 ]),
 dict(at="Here's a sentence", items=[
   (None, '<div class="quote">The lord slept in a small <b class="hl">chamber</b> at the top of the tower.</div>'),
   ('He slept in it', '<div class="say">He slept <b>in</b> it… 🛏️</div>'),
   ('a chamber must be a room', '<div class="def"><b>chamber</b><span>a room</span></div>'),
 ]),
 dict(at='One, read the sentence', items=[
   (None, '<div class="steps"><span><i>1</i>Read</span><span><i>2</i>Word parts</span><span><i>3</i>Check</span></div>'),
   ('Fill in each sentence', '<div class="say">✏️ Fill in each sentence from the word bank.</div>'),
   ('tap Check My Work', PILL('Check My Work')),
   ('Then play the matching game', PILL('Matching game')),
 ]),
])
V['g3ela-23-1-teach-gram'] = dict(title='Grammar', sub='Names get capital letters', scenes=[
 dict(at=None, items=[
   (None, '<div class="lab">🏷️ Names get capital letters</div>'),
   ('Stories say Robin Hood', '<div class="quote">Stories say <b class="hl">Robin Hood</b> lived in <b class="hl">Sherwood Forest</b>.</div>'),
   ('Robin Hood names a person', '<div class="say">🏹 Robin Hood → a <b>person</b></div>'),
   ('Sherwood Forest names a place', '<div class="say">🌳 Sherwood Forest → a <b>place</b></div>'),
 ]),
 dict(at='Every important word', items=[
   (None, '<div class="say">Every important word in a name gets a capital.</div>'),
   ('A book title does too', '<div class="quote"><b class="hl">The Wind</b> in the <b class="hl">Willows</b><small>a book title</small></div>'),
   ('But little words inside', '<div class="say"><b>in</b> · <b>the</b> stay small</div>'),
 ]),
 dict(at='Tap Now check your thinking', items=[
   (None, PILL('Now check your thinking')),
   ('Then sort each name', '<div class="bins"><span style="width:270px">Person</span><span style="width:270px">Place</span><span style="width:270px">Title</span></div>'),
 ]),
])
V['g3ela-23-1-teach-spell'] = dict(title='Spelling', sub='VCCV: split between two consonants', scenes=[
 dict(at=None, items=[
   (None, '<div class="lab">✂️ Watch me split a long word</div>'),
   ('Puppet', '<div class="huge">puppet</div>'),
 ]),
 dict(at='Find the vowels', items=[
   (None, '<div class="row4"><span class="tile on2">u</span><span class="tile">p</span><span class="tile">p</span><span class="tile on2">e</span></div>'),
   ('In between sit two consonants', '<div class="row4"><span class="tile on2">V</span><span class="tile on2">C</span><span class="tile on2">C</span><span class="tile on2">V</span></div>'),
   ("That's V C C V", '<div class="def"><b>VCCV</b><span>vowel, consonant, consonant, vowel</span></div>'),
 ]),
 dict(at='So I split right between', items=[
   (None, '<div class="build"><span class="tile">pup</span><b>·</b><span class="tile">pet</span></div>'),
   ('Say the words in Group A', '<div class="say">🗣️ Say Group A and Group B out loud.</div>'),
   ('tap See the Rule', PILL('See the Rule')),
   ('Then sort all eight words', '<div class="bins"><span>VCCV</span><span>Consonant-le</span></div>'),
 ]),
])
# ---------------- Day 2 ----------------
V['g3ela-23-2-teach-morph'] = dict(title='Morphology', sub='Match each word to its meaning', scenes=[
 dict(at=None, items=[
   (None, '<div class="def"><b>trans</b><span>across</span></div>'),
   ('Transcontinental', word('transcontinental', 'trans')),
   ('A continent is a giant piece of land', '<div class="say">🌎 a giant piece of land</div>'),
   ('So a transcontinental train', '<div class="say">🚂 ➡️ all the way across it!</div>'),
 ]),
 dict(at='Read the Remember box', items=[
   (None, '<div class="say">📌 Read the Remember box.</div>'),
   ('Then tap a word', '<div class="build"><span class="tile">word</span><b>➜</b><span class="tile m">what it means</span></div>'),
   ('Match all four words', '<div class="say">Match all four! ✨</div>'),
 ]),
])
V['g3ela-23-2-teach-vocab'] = dict(title='Vocabulary', sub='Words from the world of trades', scenes=[
 dict(at=None, items=[
   (None, '<div class="lab">🛠️ A word from the world of trades</div>'),
   ('A guild was a club', '<div class="def"><b>guild</b><span>a club for one kind of worker</span></div>'),
   ('like all the bakers', '<div class="big">🍞 🍞 🍞</div>'),
 ]),
 dict(at='Read each sentence', items=[
   (None, '<div class="say">Try a bank word in the blank. Does it make sense? ✅</div>'),
   ('Then play the matching game', PILL('Matching game')),
 ]),
])
V['g3ela-23-2-teach-gram'] = dict(title='Grammar', sub='Tap every word that needs a capital', scenes=[
 dict(at=None, items=[
   (None, '<div class="lab">🔎 Spot the capitals</div>'),
   ('abbot peter walked', '<div class="quote">abbot peter walked to bath abbey.</div>'),
 ]),
 dict(at='Abbot starts the sentence', items=[
   (None, '<div class="quote"><b class="hl">A</b>bbot peter walked to bath abbey.</div>'),
   ("it's his title", '<div class="say">first word + a title</div>'),
 ]),
 dict(at='Peter is his name', items=[
   (None, '<div class="quote"><b class="hl">A</b>bbot <b class="hl">P</b>eter walked to bath abbey.</div>'),
   ('Bath Abbey is a place', '<div class="quote"><b class="hl">A</b>bbot <b class="hl">P</b>eter walked to <b class="hl">B</b>ath <b class="hl">A</b>bbey.</div>'),
   ("That's four", '<div class="big">4 ✅</div>'),
 ]),
 dict(at='Read the Remember box', items=[
   (None, '<div class="say">📌 Read the Remember box.</div>'),
   ('Then tap every word', PILL('Tap every word that needs a capital')),
 ]),
])
V['g3ela-23-2-teach-spell'] = dict(title='Spelling', sub='Find the VCCV word', scenes=[
 dict(at=None, items=[
   (None, '<div class="lab">👀 Use your eyes</div>'),
   ('Sofa', '<span class="wd">sofa</span>'),
   ('Pony', '<span class="wd">pony</span>'),
   ('Doctor', '<span class="wd">doctor</span>'),
 ], layout='words'),
 dict(at='Which one has two consonants', items=[
   (None, '<div class="ask">Which one has two consonants between its vowels?</div>'),
   ('Doctor!', word('doctor', 'ct', 'on')),
   ('Doc. Tor', '<div class="build"><span class="tile">doc</span><b>·</b><span class="tile">tor</span></div>'),
 ]),
 dict(at='Read the rule', items=[
   (None, '<div class="say">📖 Read the rule.</div>'),
   ('Then in each row', PILL('Tap the word with two consonants in the middle')),
 ]),
])
V['g3ela-23-2-teach-rwm'] = dict(title='Read Like a Writer', sub='Two choices, one shape', scenes=[
 dict(at=None, items=[
   ('all three parts', '<div class="steps"><span><i>1</i>Reader</span><span><i>2</i>Writer</span><span><i>3</i>Mimic</span></div>'),
   ('Poor children worked', '<div class="quote">“Poor children worked in the fields or served in the homes of nobles.”<small>Servants and Apprentices</small></div>'),
 ]),
 dict(at='Part one', items=[
   (None, '<div class="step1"><i>1</i> Read like a Reader</div>'),
   ('Poor children had jobs', '<div class="say">🌾 in the fields &nbsp;or&nbsp; 🏰 in a noble’s home</div>'),
 ]),
 dict(at='Part two', items=[
   (None, '<div class="step1"><i>2</i> Read like a Writer</div>'),
   ('The little word or', '<div class="quote">…worked in the fields <b class="hl">or</b> served in the homes…</div>'),
   ('both halves have the same shape', '<div class="build"><span class="tile key">worked in</span><b>=</b><span class="tile key">served in</span></div>'),
 ]),
 dict(at='Part three', items=[
   (None, '<div class="step1"><i>3</i> Mimic</div>'),
   ("Here's mine", '<div class="quote mine">Opti <b class="hl">worked in</b> the library <b class="hl">or</b> <b class="hl">perched in</b> the old oak. 🦉📚</div>'),
   ("Now it's your turn", '<div class="say">✏️ Your turn: the apprentice sentence.<br>One sentence in each box.</div>'),
 ]),
])
# ---------------- Day 3 ----------------
V['g3ela-23-3-teach-morph'] = dict(title='Morphology', sub='Build the word', scenes=[
 dict(at=None, items=[
   (None, '<div class="lab">🧱 Let’s build one together</div>'),
   ('Trans. It', '<div class="build"><span class="tile key">trans</span><b>+</b><span class="tile">it</span></div>'),
   ('transit!', '<div class="huge">transit</div>'),
   ('Transit means going across', '<div class="say">🚌 ➡️ across town</div>'),
 ]),
 dict(at='Say each pair of parts', items=[
   (None, '<div class="say">🗣️ Say each pair of parts out loud.</div>'),
   ('Type the whole word', '<div class="build"><span class="tile key">trans</span><b>+</b><span class="tile">…</span><b>=</b><span class="tile"><i class="blank"></i></span></div>'),
   ('Then tap Check My Answers', PILL('Check My Answers')),
 ]),
])
V['g3ela-23-3-teach-vocab'] = dict(title='Vocabulary', sub='A word from the royal court', scenes=[
 dict(at=None, items=[
   (None, '<div class="big">👑</div>'),
   ('Your Majesty', '<div class="quote">“Your <b class="hl">Majesty</b>!”</div>'),
   ('Majesty is a word', '<div class="def"><b>majesty</b><span>the greatness of a king or queen</span></div>'),
   ('Saying it showed respect', '<div class="say">🙇 a sign of respect</div>'),
 ]),
 dict(at='Read how we figured out', items=[
   (None, '<div class="say">📖 Read how we figured out the first word.</div>'),
   ('fill in each sentence', '<div class="say">✏️ Fill in each sentence from the word bank.</div>'),
   ('tap Check My Work', PILL('Check My Work')),
   ('Last, play the matching game', PILL('Matching game')),
 ]),
])
V['g3ela-23-3-teach-gram'] = dict(title='Grammar', sub='Count the capitals', scenes=[
 dict(at=None, items=[
   (None, '<div class="lab">🔢 Count with me</div>'),
   ('earl roger sailed', '<div class="quote">earl roger sailed to ireland.</div>'),
 ]),
 dict(at='Earl starts the sentence', items=[
   (None, '<div class="quote"><b class="hl">E</b>arl roger sailed to ireland.</div>'),
   ('One.', '<div class="big">1</div>'),
 ]),
 dict(at='Roger is his name', items=[
   (None, '<div class="quote"><b class="hl">E</b>arl <b class="hl">R</b>oger sailed to ireland.</div>'),
   ('Two.', '<div class="big">2</div>'),
 ]),
 dict(at='Ireland is a place', items=[
   (None, '<div class="quote"><b class="hl">E</b>arl <b class="hl">R</b>oger sailed to <b class="hl">I</b>reland.</div>'),
   ('Three.', '<div class="big">3</div>'),
 ]),
 dict(at="Sailed and to", items=[
   (None, '<div class="say"><b>sailed</b> · <b>to</b> → not names, stay small</div>'),
   ('Read the Remember box', '<div class="say">📌 Read the Remember box.</div>'),
   ('count the capitals', '<div class="say">Count the capitals. Type the number. <span class="tile"><i class="blank"></i></span></div>'),
 ]),
])
V['g3ela-23-3-teach-spell'] = dict(title='Spelling', sub='Split it between the consonants', scenes=[
 dict(at=None, items=[
   (None, '<div class="lab">😬 Oops</div>'),
   ('I split garlic', '<div class="build bad"><span class="tile">ga</span><b>·</b><span class="tile">rlic</span> ❌</div>'),
   ('That sounds wrong', '<div class="say">That sounds wrong!</div>'),
 ]),
 dict(at='The two consonants', items=[
   (None, word('garlic', 'rl', 'on')),
   ('Split between them', '<div class="build good"><span class="tile">gar</span><b>·</b><span class="tile">lic</span> ✅</div>'),
   ('Garlic!', '<div class="big">🧄</div>'),
 ]),
 dict(at='Read the rule', items=[
   (None, '<div class="say">📖 Read the rule.</div>'),
   ('Then tap each word', PILL('Tap each word to split it')),
 ]),
])
# ---------------- Day 4 ----------------
V['g3ela-23-4-teach-morph'] = dict(title='Morphology', sub='Roll a word', scenes=[
 dict(at=None, items=[
   (None, '<div class="lab">🧩 Riddle time</div>'),
   ('I come at the front', '<div class="say">I come at the <b>front</b> of a word.</div>'),
   ('I have five letters', '<div class="row4"><span class="tile">?</span><span class="tile">?</span><span class="tile">?</span><span class="tile">?</span><span class="tile">?</span></div>'),
   ('Trans!', '<div class="huge">trans</div>'),
 ]),
 dict(at='Try this one', items=[
   (None, word('transcribe', 'trans')),
   ('To write across', '<div class="say">✍️ copy words from one place to another</div>'),
 ]),
 dict(at='Tap Roll the Dice', items=[
   (None, PILL('Roll the Dice!')),
   ('Say what each word means', '<div class="say">🗣️ Say what each word means.</div>'),
   ('tap Check My Thinking', PILL('Check My Thinking')),
 ]),
])
V['g3ela-23-4-teach-vocab'] = dict(title='Vocabulary', sub='One more food word', scenes=[
 dict(at=None, items=[
   (None, '<div class="lab">🍞 One more food word</div>'),
   ('Trencher', '<div class="huge">trencher</div>'),
   ('The article says', '<div class="quote">…thick slices of bread called <b class="hl">trenchers</b>.<small>What Did Medieval People Eat?</small></div>'),
   ('A plate you could eat', '<div class="big">🍞 = 🍽️</div>'),
 ]),
 dict(at='Read each sentence', items=[
   (None, '<div class="say">Try a bank word in the blank. Does it make sense? ✅</div>'),
   ('Then play the matching game', PILL('Matching game')),
 ]),
])
V['g3ela-23-4-teach-gram'] = dict(title='Grammar', sub='Find the mistake', scenes=[
 dict(at=None, items=[
   (None, '<div class="lab">🧐 Something looks funny</div>'),
   ('We saw a Castle', '<div class="quote">We saw a <b class="hl">C</b>astle on the hill.</div>'),
 ]),
 dict(at='Castle has a capital', items=[
   (None, '<div class="say">Is it the name of one castle? 🤔</div>'),
   ('It could be any castle', '<div class="big">🏰 🏰 🏰</div>'),
   ('So it stays small', '<div class="quote good">We saw a <b class="hl">c</b>astle on the hill. ✅</div>'),
 ]),
 dict(at='Read each sentence out loud', items=[
   (None, '<div class="say">🗣️ Read each sentence out loud.</div>'),
   ("Tap the word that's wrong", '<div class="build"><span class="tile">👆 the wrong word</span><b>or</b><span class="tile m">No mistake</span></div>'),
 ]),
])
V['g3ela-23-4-teach-spell'] = dict(title='Spelling', sub='Roll and split', scenes=[
 dict(at=None, items=[
   (None, '<div class="lab">🎲 Roll one with me</div>'),
   ('Window!', '<div class="huge">window</div>'),
   ('The vowels are i and o', '<div class="row4"><span class="tile on2">i</span><span class="tile">n</span><span class="tile">w</span><span class="tile on2">o</span></div>'),
   ('Split between them', '<div class="build"><span class="tile">win</span><b>·</b><span class="tile">dow</span></div>'),
 ]),
 dict(at='Tap Roll the dice', items=[
   (None, PILL('Roll the dice')),
   ('Say the word out loud', '<div class="say">🗣️ Say it. Split it.</div>'),
   ('Then tap Check my answer', PILL('Check my answer')),
   ('Roll all six words', '<div class="say">Roll all six! 🎲🎲🎲</div>'),
 ]),
])
