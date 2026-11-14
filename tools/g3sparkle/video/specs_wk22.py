# Scene specs for the week 22 Opti teach videos (The Whipping Boy wrap-up, no new chapters).
# Each item appears when Opti says its anchor (a phrase from the script). Scripts = DATA.teach.
# Never shows an answer the page asks for: examples are castle/tower/bridge, restructure, act+ion,
# unlikely, pause, farewell, we/us/our, she/us/her, Betsy's bear, "him hat", cupcake/beautiful,
# kitten/window/doghouse/paper, football, toothbrush, and the Ch. 19 "Careful, he thought."
def word(w, part=None, cls=''):
    if part:
        i = w.index(part)
        return '<span class="wd %s">%s<b class="pt">%s</b>%s</span>' % (cls, w[:i], part, w[i+len(part):])
    return '<span class="wd %s">%s</span>' % (cls, w)
PILL = lambda t: '<span class="pill">👆 %s</span>' % t
STEPS = '<div class="steps"><span><i>🔊</i>listen</span><span><i>🤔</i>guess</span><span><i>🃏</i>flip</span></div>'
V = {}
# ---------------- Day 1: teach the idea ----------------
V['g3ela-22-1-teach-morph'] = dict(title='Morphology', sub='A root that means build', scenes=[
 dict(at=None, items=[
   (None, '<div class="ask">🤔 What do these have in common?</div>'),
   ('a castle, a tower', '<div class="big">🏰 🗼 🌉</div>'),
   ('Somebody built them', '<div class="say">Somebody <b>built</b> them!</div>'),
 ]),
 dict(at='Long ago, the Romans', items=[
   (None, '<div class="lab">🏛️ An old Roman word piece</div>'),
   ('Struct. S', '<div class="huge">struct</div>'),
   ('S, t, r, u, c, t', '<div class="say">s · t · r · u · c · t</div>'),
   ('think: build', '<div class="def"><b>struct</b><span>build</span></div>'),
 ]),
 dict(at='Read the three words', items=[
   (None, '<div class="say">📖 Read the three words. Think about the questions.</div>'),
   ('Then tap See what was hiding', PILL('See what was hiding')),
   ('type the missing parts', '<div class="build"><span class="tile">con</span><b>+</b><span class="tile"><i class="blank"></i></span></div>'),
 ]),
])
V['g3ela-22-1-teach-vocab'] = dict(title='Vocabulary', sub='Be a word detective', scenes=[
 dict(at=None, items=[
   (None, '<div class="lab">🔍 Word detective</div>'),
   ('Unlikely', word('unlikely', 'un')),
   ('Un means not', '<div class="say"><b>un</b> = not</div>'),
   ('likely means', '<div class="say"><b>likely</b> = will probably happen</div>'),
 ]),
 dict(at='So unlikely means', items=[
   (None, '<div class="def"><b>unlikely</b><span>not likely at all</span></div>'),
   ('Jemmy and the prince were', '<div class="say">👑 + 🐀 an unlikely pair of friends!</div>'),
 ]),
 dict(at='Listen to each card', items=[
   (None, STEPS),
   ('Then play the matching game', PILL('Matching game')),
 ]),
])
V['g3ela-22-1-teach-gram'] = dict(title='Grammar', sub='Pronouns have jobs', scenes=[
 dict(at=None, items=[
   (None, '<div class="lab">🧩 Pronouns stand in for names</div>'),
   ('We ran', '<div class="quote"><b class="hl">We</b> ran.</div>'),
   ('Betsy helped us', '<div class="quote">Betsy helped <b class="hl">us</b>.</div>'),
   ('It was our coach', '<div class="quote">It was <b class="hl">our</b> coach.</div>'),
 ]),
 dict(at='We does the action', items=[
   (None, '<div class="say">✋ <b>we</b> does the action</div>'),
   ('Us gets the action', '<div class="say">🎁 <b>us</b> gets the action</div>'),
   ('Our shows whose', '<div class="say">🏷️ <b>our</b> shows whose</div>'),
 ]),
 dict(at="Here's a trick for pairs", items=[
   (None, '<div class="lab">🙈 A trick for pairs</div>'),
   ('Betsy and us laughed', '<div class="quote bad">Betsy and <b class="hl">us</b> laughed?</div>'),
   ('Cover Betsy', '<div class="quote bad"><b class="hl">Us</b> laughed? ❌</div>'),
   ('We laughed', '<div class="quote good"><b class="hl">We</b> laughed. ✅</div>'),
 ]),
 dict(at='Tap Now check your thinking', items=[
   (None, PILL('Now check your thinking')),
   ('Then sort each pronoun', '<div class="bins"><span>Does</span><span>Gets</span><span>Whose</span></div>'),
 ]),
])
V['g3ela-22-1-teach-spell'] = dict(title='Spelling', sub='Compound words', scenes=[
 dict(at=None, items=[
   (None, '<div class="lab">✂️ Watch me take one apart</div>'),
   ('Cupcake', '<div class="huge">cupcake 🧁</div>'),
   ('Cup, plus cake', '<div class="build"><span class="tile">cup</span><b>+</b><span class="tile">cake</span></div>'),
   ("That's a compound word", '<div class="def"><b>compound word</b><span>two real words joined into one</span></div>'),
 ]),
 dict(at='Now be careful', items=[
   (None, '<div class="lab">⚠️ Be careful</div>'),
   ('Beautiful is a long word', '<div class="say">beautiful</div>'),
   ('two real words? No', '<div class="say">two real words? ❌</div>'),
   ("Long doesn't mean compound", '<div class="say">Long ≠ compound</div>'),
 ]),
 dict(at='Say the words out loud', items=[
   (None, PILL('Now name the pattern')),
   ('Then sort all eight', '<div class="bins"><span>Compound</span><span>Not compound</span></div>'),
 ]),
])
# ---------------- Day 2 ----------------
V['g3ela-22-2-teach-morph'] = dict(title='Morphology', sub='Match the struct words', scenes=[
 dict(at=None, items=[
   (None, '<div class="say">Remember: <b>struct</b> = build</div>'),
   ('Restructure', word('restructure', 'struct')),
   ('Cover the re at the front', '<div class="build"><span class="tile">re</span><b>+</b><span class="tile key">struct</span><b>+</b><span class="tile">ure</span></div>'),
 ], hl=[('Struct is in the middle', '.key')]),
 dict(at='Re means again', items=[
   (None, '<div class="say">struct = <b>build</b> 🧱 · re = <b>again</b></div>'),
   ('So restructure means', '<div class="def"><b>restructure</b><span>build again in a new way</span></div>'),
 ]),
 dict(at='Read the Remember box', items=[
   (None, '<div class="say">📌 Read the Remember box.</div>'),
   ('tap a word, and tap what it means', '<div class="build"><span class="tile">word</span><b>→</b><span class="tile">meaning</span></div>'),
   ('Match all four words', '<div class="say">✔ × 4</div>'),
 ]),
])
V['g3ela-22-2-teach-vocab'] = dict(title='Vocabulary', sub='Words for big ideas', scenes=[
 dict(at=None, items=[
   (None, '<div class="ask">🧩 A puzzle</div>'),
   ('What happens in a story', '<div class="grid2"><div class="say">What <b>happens</b></div><div class="say">What it <b>means</b></div></div>'),
   ('two different things', '<div class="say">two different things!</div>'),
   ("Today's four words", '<div class="say">💡 Words for what a story <b>means</b></div>'),
 ]),
 dict(at='Listen to each card', items=[
   (None, STEPS),
   ('Then match all four', PILL('Matching game')),
 ]),
])
V['g3ela-22-2-teach-gram'] = dict(title='Grammar', sub='Find every pronoun', scenes=[
 dict(at=None, items=[
   (None, '<div class="lab">🔎 Spot the pronouns</div>'),
   ('She gave us her map', '<div class="quote q3"><span class="p1">She</span> gave <span class="p2">us</span> <span class="p3">her</span> map.</div>'),
   ('She is doing the giving', '<div class="say"><b>She</b> does it</div>'),
   ('Us gets the map', '<div class="say"><b>us</b> gets it</div>'),
   ('Her shows whose', '<div class="say"><b>her</b> shows whose</div>'),
 ], hl=[('She is doing', '.p1'), ('Us gets the map', '.p2'), ('Her shows whose', '.p3')]),
 dict(at='Three pronouns, three jobs', items=[
   (None, '<div class="say">3 pronouns · 3 jobs</div>'),
   ('Read the Remember box', '<div class="say">📌 Read the Remember box.</div>'),
   ('Then tap every pronoun', PILL('Tap every pronoun')),
 ]),
])
V['g3ela-22-2-teach-spell'] = dict(title='Spelling', sub='Find it by ear', scenes=[
 dict(at=None, items=[
   (None, '<div class="lab">👂 Use your ears</div>'),
   ('Kitten. Window', '<div class="chips"><span>kitten</span><span>window</span><span>doghouse</span><span>paper</span></div>'),
   ('Which one is two small words', '<div class="ask">Which one is two small words?</div>'),
   ('Dog, plus house', '<div class="build"><span class="tile">dog</span><b>+</b><span class="tile">house</span></div>'),
   ('Doghouse!', '<div class="huge">doghouse 🐶🏠</div>'),
 ]),
 dict(at='Say each word in the row', items=[
   (None, '<div class="say">🗣️ Say each word out loud.</div>'),
   ('Then tap the compound word', PILL('Tap the compound word')),
 ]),
])
V['g3ela-22-2-teach-rwm'] = dict(title='Read Like a Writer', sub='A thought in his own words', scenes=[
 dict(at=None, items=[
   ('all three parts', '<div class="steps"><span><i>1</i>Reader</span><span><i>2</i>Writer</span><span><i>3</i>Mimic</span></div>'),
   ('Careful, he thought', '<div class="quote">“Careful, he thought.”<small>Chapter 19</small></div>'),
 ]),
 dict(at='Part one', items=[
   (None, '<div class="step1"><i>1</i> Read like a Reader</div>'),
   ('Jemmy is in the dark sewer', '<div class="say">🕯️ Jemmy picks a tunnel in the dark sewer.</div>'),
 ]),
 dict(at='Part two', items=[
   (None, '<div class="step1"><i>2</i> Read like a Writer</div>'),
   ('There are no quotation marks', '<div class="say">No “ ” marks</div>'),
   ("We hear Jemmy's own word", '<div class="quote"><b class="hl">Careful</b>, he thought.</div>'),
   ('right inside his head', '<div class="big">💭</div>'),
 ]),
 dict(at='Part three', items=[
   (None, '<div class="step1"><i>3</i> Mimic</div>'),
   ("Here's mine", '<div class="quote mine"><b class="hl">Hush</b>, Opti thought, the story is just getting good. 🦉📖</div>'),
   ("Now it's your turn", '<div class="say">✏️ Your turn: Jemmy’s sentence.<br>One sentence in each box.</div>'),
 ]),
])
# ---------------- Day 3 ----------------
V['g3ela-22-3-teach-morph'] = dict(title='Morphology', sub='Build the word', scenes=[
 dict(at=None, items=[
   (None, '<div class="lab">✨ One little ending</div>'),
   ('Act, plus', '<div class="build"><span class="tile">act</span><b>+</b><span class="tile">ion</span></div>'),
   ('Action!', '<div class="huge">action 🎬</div>'),
   ('turns a doing word into a thing', '<div class="say">doing word → <b>thing</b></div>'),
 ]),
 dict(at="Today you'll stick it", items=[
   (None, '<div class="build"><span class="tile">front part</span><b>+</b><span class="tile key">struct</span><b>+</b><span class="tile">ion</span></div>'),
   ('Say the parts out loud', '<div class="say">🗣️ Say the parts. Push them together.</div>'),
   ('type the whole word', '<div class="build"><b>→</b><span class="tile"><i class="blank"></i></span></div>'),
   ('Then tap Check My Answers', PILL('Check My Answers')),
 ]),
])
V['g3ela-22-3-teach-vocab'] = dict(title='Vocabulary', sub='Words for reading out loud', scenes=[
 dict(at=None, items=[
   (None, '<div class="lab">🎭 A reading-aloud word</div>'),
   ('Pause.', '<div class="big">⏸️</div>'),
   ('When you pause', '<div class="def"><b>pause</b><span>stop for just a moment</span></div>'),
   ('like at a comma', '<div class="quote">Wait<b class="hl">,</b> listen.</div>'),
 ]),
 dict(at='Read how we figured out', items=[
   (None, '<div class="say">📖 Read how we figured out the first word.</div>'),
   ('fill in each sentence', '<div class="quote">… <i class="blank"></i> …</div>'),
   ('tap Check My Work', PILL('Check My Work')),
   ('play the matching game', PILL('Matching game')),
 ]),
])
V['g3ela-22-3-teach-gram'] = dict(title='Grammar', sub="Don't say the name twice", scenes=[
 dict(at=None, items=[
   (None, '<div class="lab">👂 Listen to this</div>'),
   ("Betsy fed Betsy's bear", '<div class="quote bad">Betsy fed Betsy’s bear, and Betsy’s bear licked Betsy. 😵</div>'),
   ('Clunky!', '<div class="say">Clunky!</div>'),
   ('Betsy fed her bear', '<div class="quote good">Betsy fed <b class="hl">her</b> bear, and the bear licked <b class="hl">her</b>. 🐻</div>'),
 ]),
 dict(at='Read the Remember box', items=[
   (None, '<div class="say">📌 Read the Remember box.</div>'),
   ('type a pronoun from the word bank', '<div class="chips"><span>word bank</span></div>'),
   ('so no name is said twice', '<div class="say">One name, then a pronoun ✅</div>'),
 ]),
])
V['g3ela-22-3-teach-spell'] = dict(title='Spelling', sub='Join the words', scenes=[
 dict(at=None, items=[
   (None, '<div class="lab">🕵️ Oops!</div>'),
   ('I wrote foot', '<div class="quote bad">foot ball ❌</div>'),
   ('a football is one thing', '<div class="big">🏈</div>'),
   ('Foot and ball join', '<div class="quote good">football ✅</div>'),
 ]),
 dict(at='Tap each card', items=[
   (None, PILL('Tap to join them')),
   ('Say the new word out loud', '<div class="say">🗣️ Say the new word.</div>'),
   ('answer the question in the box', '<div class="say">✏️ Answer the question in the box.</div>'),
 ]),
])
# ---------------- Day 4 ----------------
V['g3ela-22-4-teach-morph'] = dict(title='Morphology', sub='Roll the dice', scenes=[
 dict(at=None, items=[
   (None, '<div class="ask">🤔 Riddle time</div>'),
   ("I'm six letters long", '<div class="say">6 letters</div>'),
   ('I hide inside big words', '<div class="say">hides inside big words</div>'),
   ('And I mean build', '<div class="say">means <b>build</b></div>'),
   ('Struct!', '<div class="huge">struct!</div>'),
 ]),
 dict(at='Roll a word', items=[
   (None, '<div class="big">🎲</div>'),
   ('find struct inside it', '<div class="steps"><span><i>1</i>find struct</span><span><i>2</i>say the meaning</span></div>'),
   ('Then tap Check My Thinking', PILL('Check My Thinking')),
   ('Roll all six', '<div class="say">🎲 × 6</div>'),
 ]),
])
V['g3ela-22-4-teach-vocab'] = dict(title='Vocabulary', sub='Words for finishing a book', scenes=[
 dict(at=None, items=[
   (None, '<div class="lab">👋 One more word</div>'),
   ('Farewell', '<div class="big">👋</div>'),
   ('Fare, plus well', '<div class="build"><span class="tile">fare</span><b>+</b><span class="tile">well</span></div>'),
   ('It means goodbye', '<div class="def"><b>farewell</b><span>goodbye, and good luck!</span></div>'),
 ]),
 dict(at='Read each sentence', items=[
   (None, '<div class="quote">… <i class="blank"></i> …</div>'),
   ('If it sounds right', '<div class="say">Sounds right? Makes sense? Keep it ✅</div>'),
   ('Then play the matching game', PILL('Matching game')),
 ]),
])
V['g3ela-22-4-teach-gram'] = dict(title='Grammar', sub='Find the mistake', scenes=[
 dict(at=None, items=[
   (None, '<div class="lab">🔎 Spot the mistake</div>'),
   ('The boy lost him hat', '<div class="quote bad">The boy lost <b class="hl">him</b> hat. 🎩</div>'),
   ('The hat belongs to the boy', '<div class="say">Whose hat? The boy’s.</div>'),
   ("so it's his hat", '<div class="quote good">The boy lost <b class="hl">his</b> hat. ✅</div>'),
 ]),
 dict(at='Read each sentence out loud', items=[
   (None, '<div class="say">🗣️ Read it out loud.</div>'),
   ('Tap the wrong word', PILL('Tap the wrong word')),
   ('or tap No mistake', PILL('No mistake')),
 ]),
])
V['g3ela-22-4-teach-spell'] = dict(title='Spelling', sub='Compound dice', scenes=[
 dict(at=None, items=[
   (None, '<div class="big">🎲</div>'),
   ('Toothbrush', '<div class="huge">toothbrush 🪥</div>'),
   ('Tooth. Brush', '<div class="build"><span class="tile">tooth</span><b>+</b><span class="tile">brush</span></div>'),
 ]),
 dict(at='Now roll all six', items=[
   (None, PILL('Roll the dice')),
   ('say the two small words', '<div class="say">🗣️ Say the word. Say its two small words.</div>'),
 ]),
])
