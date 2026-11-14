# Scene specs for the week 21 Opti teach videos (The Whipping Boy, Ch. 16-20).
# Each item appears when Opti says its anchor (a phrase from the script). Scripts = DATA.teach.
# Never shows an answer the page asks for: examples are retell, replay, prepay, notorious,
# under the potatoes / after dark / with a shout, two boys / too hot / to the castle,
# their cart, "Blank coats were torn", behind the golden doors, "Petunia can dance two",
# "on of the cart", "two big dogs", and the Ch. 18 bell clapper sentence.
def word(w, part=None, cls=''):
    if part:
        i = w.index(part)
        return '<span class="wd %s">%s<b class="pt">%s</b>%s</span>' % (cls, w[:i], part, w[i+len(part):])
    return '<span class="wd %s">%s</span>' % (cls, w)
PILL = lambda t: '<span class="pill">👆 %s</span>' % t
STEPS = '<div class="steps"><span><i>🔊</i>listen</span><span><i>🤔</i>guess</span><span><i>🃏</i>flip</span></div>'
V = {}
# ---------------- Day 1: teach the idea ----------------
V['g3ela-21-1-teach-morph'] = dict(title='Morphology', sub='Front word parts', scenes=[
 dict(at=None, items=[
   (None, '<div class="lab">🔍 A trick for big words</div>'),
   ('Retell', word('retell', 're')),
   ('Cover the re', '<div class="build"><span class="tile key">re</span><b>+</b><span class="tile">tell</span></div>'),
   ('Re means again, so', '<div class="say">re = <b>again</b> · retell = tell again</div>'),
 ], hl=[('Cover the re', '.pt')]),
 dict(at='Five word parts', items=[
   (None, '<div class="lab">Five front parts</div>'),
   ('Re means again. Pre', '<div class="say"><b>re</b> = again</div>'),
   ('Pre means before', '<div class="say"><b>pre</b> = before</div>'),
   ('Mis means wrong', '<div class="say"><b>mis</b> = wrong</div>'),
   ('And two of them mean not', '<div class="say"><b>un</b> and <b>dis</b> = not</div>'),
 ]),
 dict(at='Read the five words', items=[
   (None, '<div class="say">📖 Read the five words. Think about the question.</div>'),
   ('Then tap See what was hiding', PILL('See what was hiding')),
   ('Last, type each whole word', '<div class="build"><span class="tile">part</span><b>+</b><span class="tile">word</span><b>→</b><span class="tile"><i class="blank"></i></span></div>'),
 ]),
])
V['g3ela-21-1-teach-vocab'] = dict(title='Vocabulary', sub='Be a word detective', scenes=[
 dict(at=None, items=[
   (None, '<div class="lab">🔍 Word detective</div>'),
   ('In Chapter 17', '<div class="say">🐻 Chapter 17: the prince gets up off the mud.</div>'),
   ('There was a cast-iron', '<div class="quote">“There was a cast-iron streak of <b class="hl">pluck</b> in him.”<small>Chapter 17</small></div>'),
 ]),
 dict(at='Cast iron is hard', items=[
   (None, '<div class="big">🍳</div>'),
   ('Cast iron is hard', '<div class="say">cast iron = <b>hard and strong</b></div>'),
   ('So pluck must be', '<div class="say">something strong <u>inside</u> a person</div>'),
   ('Courage', '<div class="def"><b>pluck</b><span>courage</span></div>'),
 ]),
 dict(at='Now tap Opti reads it', items=[
   (None, PILL('Opti reads it')),
   ('Guess, then flip', STEPS),
   ('Then play the matching game', PILL('Matching game')),
 ]),
])
V['g3ela-21-1-teach-gram'] = dict(title='Grammar', sub='Prepositional phrases', scenes=[
 dict(at=None, items=[
   (None, '<div class="lab">👂 Listen</div>'),
   ('Jemmy hid. Jemmy', '<div class="quote">Jemmy hid.</div>'),
   ('Jemmy hid under', '<div class="quote">Jemmy hid <b class="hl">under the potatoes</b>.</div>'),
   ('The new part starts', '<div class="say">starts with <b>under</b> · ends with <b>potatoes</b></div>'),
 ]),
 dict(at='That whole group', items=[
   (None, '<div class="def"><b>prepositional phrase</b><span>the whole group of words</span></div>'),
   ('It starts with a preposition', '<div class="eq"><span class="th">preposition</span><span class="glue">…</span><span class="th">noun</span></div>'),
   ('Some tell where', '<div class="say">📍 Where? <b>under the potatoes</b></div>'),
   ('Some tell when', '<div class="say">🕰️ When? <b>after dark</b></div>'),
   ('Some tell how', '<div class="say">📣 How? <b>with a shout</b></div>'),
 ]),
 dict(at='Tap Now check your thinking', items=[
   (None, PILL('Now check your thinking')),
   ('Then sort each phrase', '<div class="bins"><span>Where</span><span>When</span><span>How</span></div>'),
 ]),
])
V['g3ela-21-1-teach-spell'] = dict(title='Spelling', sub='to · two · too', scenes=[
 dict(at=None, items=[
   (None, '<div class="lab">🗣️ Say these with me</div>'),
   ('To. Two. Too.', '<div class="huge">to · two · too</div>'),
   ('They sound exactly', '<div class="say">👂 They sound exactly the same!</div>'),
   ("Your ears can't help", '<div class="say">So the <b>spelling</b> has to help.</div>'),
 ]),
 dict(at='Two, t w o', items=[
   (None, '<div class="say"><b>two</b> = the number 2 · two boys</div>'),
   ("Too, with two o's", '<div class="say"><b>too</b> = also, or more than enough · too hot</div>'),
   ('To points somewhere', '<div class="say"><b>to</b> = points somewhere · to the castle</div>'),
 ]),
 dict(at='Read the three sentences', items=[
   (None, PILL('See the Rule')),
   ('Then tap each phrase', '<div class="bins"><span>to</span><span>two</span><span>too</span></div>'),
 ]),
])
# ---------------- Day 2 ----------------
V['g3ela-21-2-teach-morph'] = dict(title='Morphology', sub='Match the word to its meaning', scenes=[
 dict(at=None, items=[
   (None, '<div class="ask">🤔 Spot the front part?</div>'),
   ('Can you spot', word('replay', 're')),
   ('Cover it, and play', '<div class="build"><span class="tile key">re</span><b>+</b><span class="tile">play</span></div>'),
   ('So replay means', '<div class="say">replay = play <u>again</u> 🔁</div>'),
 ], hl=[('Cover it', '.pt')]),
 dict(at='Do that with every word', items=[
   (None, '<div class="grid2"><span class="tile">a word</span><span class="tile m">its meaning</span><span class="tile">a word</span><span class="tile m">its meaning</span></div>'),
   ('Read the Remember box', '<div class="say">📌 Read the Remember box.</div>'),
   ('Then tap a word', PILL('Tap a word, then its meaning')),
 ]),
])
V['g3ela-21-2-teach-vocab'] = dict(title='Vocabulary', sub='Listen, guess, flip', scenes=[
 dict(at=None, items=[
   (None, '<div class="big">🎪 🤹 🎡</div>'),
   ('The prince laughs', '<div class="say">😄 The prince laughs!</div>'),
   ('The book calls that sound', '<span class="wd">merriment</span>'),
   ('Merry, plus ment', '<div class="build"><span class="tile">merry</span><b>+</b><span class="tile">ment</span></div>'),
   ('Happy laughing and fun', '<div class="say">happy laughing and fun</div>'),
 ]),
 dict(at='Listen to each card', items=[
   (None, STEPS),
   ('Then match all four', PILL('Match all four')),
 ]),
])
V['g3ela-21-2-teach-spell2'] = dict(title='Spelling Bonus', sub='their · there · they\'re', scenes=[
 dict(at=None, items=[
   (None, '<div class="lab">🧩 A riddle</div>'),
   ('Which word has the word here', '<div class="ask">Which word has <b>here</b> hiding inside it?</div>'),
   ('There!', word('there', 'here')),
   ('And there is a place', '<div class="say">📍 there = a place, just like here</div>'),
 ], hl=[('There!', '.pt')]),
 dict(at='Their means it belongs', items=[
   (None, '<div class="say"><b>their</b> = belongs to them · their cart 🛒</div>'),
   ("They're is two words", '<div class="say"><b>they’re</b> = they are</div>'),
   ('The apostrophe stands in', '<div class="say">’ = a missing letter</div>'),
   ("Its and it's", '<div class="say"><b>its</b> · <b>it’s</b> work the same way</div>'),
 ]),
 dict(at='Read the two sentences', items=[
   (None, PILL('Now check your thinking')),
   ('Then sort the words', '<div class="bins"><span>Shows belonging</span><span>Two words squeezed together</span></div>'),
   ('pick the right spelling', PILL('Tap the right spelling')),
 ]),
])
V['g3ela-21-2-teach-spell'] = dict(title='Spelling', sub='Pick by meaning', scenes=[
 dict(at=None, items=[
   (None, '<div class="lab">👀 Watch me pick one</div>'),
   ('Blank coats', '<div class="quote"><i class="blank"></i> coats were torn.</div>'),
   ('Try they are', '<div class="say">they are coats were torn? ❌</div>'),
   ('Is it a place', '<div class="say">a place? ❌</div>'),
   ('The coats belong', '<div class="say">The coats belong to the boys ✅</div>'),
   ("So it's their", '<div class="huge"><b class="gold">their</b> coats</div>'),
 ]),
 dict(at='Read each whole sentence', items=[
   (None, '<div class="say">📖 Read the whole sentence first.</div>'),
   ('Then tap the spelling', PILL('Tap the spelling that fits')),
 ]),
])
V['g3ela-21-2-teach-rwm'] = dict(title='Read Like a Writer', sub='Three parts', scenes=[
 dict(at=None, items=[
   ('has three parts', '<div class="steps"><span><i>1</i>Reader</span><span><i>2</i>Writer</span><span><i>3</i>Mimic</span></div>'),
   ('The news seller appeared', '<div class="quote">“The news seller appeared, his tongue wagging like a bell clapper.”<small>Chapter 18</small></div>'),
 ]),
 dict(at='Part one', items=[
   (None, '<div class="step1"><i>1</i> Read like a Reader</div>'),
   ('What is happening', '<div class="ask">🤔 What is happening?</div>'),
   ('A man is selling news', '<div class="say">📰 A man selling news shouts and shouts.</div>'),
 ]),
 dict(at='Part two', items=[
   (None, '<div class="step1"><i>2</i> Read like a Writer</div>'),
   ('The author says', '<div class="quote">“…his tongue wagging <b class="hl">like a bell clapper</b>.”</div>'),
   ('the part that swings', '<div class="big">🔔</div>'),
   ('Now we can hear', '<div class="say">Now we can <u>hear</u> how loud he is!</div>'),
 ]),
 dict(at='Part three', items=[
   (None, '<div class="step1"><i>3</i> Mimic</div>'),
   ("Here's mine", '<div class="quote mine">The puppy’s tail thumped <b class="hl">like a drum</b>. 🐶🥁</div>'),
   ("Now it's your turn", '<div class="say">✏️ Your turn: Jemmy’s sentence.<br>One sentence in each box.</div>'),
 ]),
])
# ---------------- Day 3 ----------------
V['g3ela-21-3-teach-morph'] = dict(title='Morphology', sub='Build the word', scenes=[
 dict(at=None, items=[
   ('Pre, plus pay', '<div class="build"><span class="tile">pre</span><b>+</b><span class="tile">pay</span></div>'),
   ('Prepay', '<div class="huge">prepay 💰</div>'),
   ('To pay before', '<div class="say">to pay <u>before</u></div>'),
 ]),
 dict(at='Say each pair', items=[
   (None, '<div class="say">🗣️ Say each pair of parts out loud.</div>'),
   ('Type the whole word', '<div class="build"><span class="tile">part</span><b>+</b><span class="tile">word</span><b>→</b><span class="tile"><i class="blank"></i></span></div>'),
   ('Then tap Check My Answers', PILL('Check My Answers')),
 ]),
])
V['g3ela-21-3-teach-vocab'] = dict(title='Vocabulary', sub='Use the word bank', scenes=[
 dict(at=None, items=[
   (None, '<div class="lab">📜 A bonus word from Chapter 20</div>'),
   ('The ballad sellers sang', '<div class="quote">…the <b class="hl">notorious</b> life of Hold-Your-Nose Billy<small>Chapter 20</small></div>'),
   ('Notorious means', '<div class="def"><b>notorious</b><span>famous for something bad</span></div>'),
 ]),
 dict(at='Read how we figured out', items=[
   (None, '<div class="say">🔍 Read how we figured out the first word.</div>'),
   ('Then fill in each sentence', '<div class="quote">… <i class="blank"></i> …</div>'),
   ('tap Check My Work', PILL('Check My Work')),
   ('Last, play the matching game', PILL('Matching game')),
 ]),
])
V['g3ela-21-3-teach-gram'] = dict(title='Grammar', sub='Where does the phrase stop?', scenes=[
 dict(at=None, items=[
   (None, '<div class="ask">🤔 Where does a phrase stop?</div>'),
   ('On a noun', '<div class="say">On a <b>noun</b>.</div>'),
   ('Behind the golden doors', '<div class="quote q3"><span class="p1">Behind</span> <span class="p2">the</span> <span class="p3">golden</span> <b class="hl">doors</b></div>'),
   ("Doors is the noun", '<div class="huge">doors 🚪✨</div>'),
 ], hl=[('Behind. The', '.p1'), ('The. Golden', '.p2'), ('Golden. Doors', '.p3')]),
 dict(at='Read each sentence', items=[
   (None, '<div class="say">Find the phrase. Type the noun it ends on.</div>'),
   ('Use the word bank', '<div class="chips"><span>word bank</span></div>'),
 ]),
])
V['g3ela-21-3-teach-spell'] = dict(title='Spelling', sub='to · two · too · their · there · they\'re', scenes=[
 dict(at=None, items=[
   (None, '<div class="lab">🕵️ Spot my mistake</div>'),
   ('Petunia can dance two', '<div class="quote bad">Petunia can dance <b class="hl">two</b>. 🐻</div>'),
   ('Two is a number', '<div class="say">two = a number ❌</div>'),
   ('I mean also', '<div class="quote good">Petunia can dance <b class="hl">too</b>. ✅</div>'),
 ]),
 dict(at='Say each sentence', items=[
   (None, '<div class="say">💭 Think about the meaning.</div>'),
   ('Then tap the spelling', PILL('Tap the spelling that fits')),
 ]),
])
# ---------------- Day 4 ----------------
V['g3ela-21-4-teach-morph'] = dict(title='Morphology', sub='Roll the dice', scenes=[
 dict(at=None, items=[
   (None, '<div class="big">🎲</div>'),
   ('Five word parts, one dice', '<div class="chips"><span>re</span><span>un</span><span>pre</span><span>dis</span><span>mis</span></div>'),
   ('Roll a word', PILL('Roll the Dice')),
 ]),
 dict(at='Find the front part', items=[
   (None, '<div class="steps"><span><i>1</i>find the front part</span><span><i>2</i>say what it means</span><span><i>3</i>say the whole word’s meaning</span></div>'),
   ('Tap Check My Thinking', PILL('Check My Thinking')),
   ('Roll all six', '<div class="say">🎲 × 6</div>'),
 ]),
])
V['g3ela-21-4-teach-vocab'] = dict(title='Vocabulary', sub='Words from the whole week', scenes=[
 dict(at=None, items=[
   (None, '<div class="huge">Gaw!</div>'),
   ("That's Jemmy's word", '<div class="say">😮 Jemmy’s word when something amazes him</div>'),
 ]),
 dict(at="Today's words come", items=[
   (None, '<div class="lab">📚 Words from all week</div>'),
   ('Read each sentence out loud', '<div class="quote">… <i class="blank"></i> …</div>'),
   ('If it sounds right', '<div class="say">Sounds right? Makes sense? Keep it ✅</div>'),
   ('Then play the matching game', PILL('Matching game')),
 ]),
])
V['g3ela-21-4-teach-gram'] = dict(title='Grammar', sub='Find the mistake', scenes=[
 dict(at=None, items=[
   (None, '<div class="lab">🖼️ Picture this</div>'),
   ('The bear danced', '<div class="quote bad">The bear danced <b class="hl">on of</b> the cart. 🐻</div>'),
   ('On of?', '<div class="say">Two prepositions in a row ❌</div>'),
   ('A phrase needs one', '<div class="eq"><span class="th">1 preposition</span><span class="glue">+</span><span class="th">1 noun</span></div>'),
 ]),
 dict(at='Read each sentence and picture', items=[
   (None, '<div class="say">📖 Read it. Picture it.</div>'),
   ('Tap the broken word', PILL('Tap the broken word')),
   ('or tap No mistake', PILL('No mistake')),
 ]),
])
V['g3ela-21-4-teach-spell'] = dict(title='Spelling', sub='Homophone dice', scenes=[
 dict(at=None, items=[
   (None, '<div class="big">🎲</div>'),
   ('Blank big dogs', '<div class="quote"><i class="blank"></i> big dogs 🐕🐕</div>'),
   ('Is it a number', '<div class="ask">A number? Yes!</div>'),
   ('two dogs', '<div class="huge"><b class="gold">two</b> dogs</div>'),
 ]),
 dict(at='Now roll all six', items=[
   (None, PILL('Roll the dice')),
   ('Say which spelling fits', '<div class="say">🗣️ Which spelling? Why?</div>'),
 ]),
])
