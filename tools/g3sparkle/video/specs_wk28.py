def word(w, part=None, cls=''):
    if part:
        i = w.index(part)
        return '<span class="wd %s">%s<b class="pt">%s</b>%s</span>' % (cls, w[:i], part, w[i+len(part):])
    return '<span class="wd %s">%s</span>' % (cls, w)
PILL = lambda t: '<span class="pill">👆 %s</span>' % t
def tiles(*ps): return '<div class="build">' + '<b>+</b>'.join('<span class="tile%s">%s</span>' % (' key' if k else '', t) for t, k in ps) + '</div>'
# Scene specs for the week 28 Opti teach films (LWW Ch. 10-12). SILENT for now (tone.py timing); captions carry the words.
# Never shows a page answer: examples are constellation, companion, contact, community; uncombed, repulsive, renewed (in
# Opti's own sentence), solemn (Opti's own sentence); can't, dog's, Mrs. Beaver's, dwarf's/wasn't, Mr. Beaver's tail;
# swimming, baking, tried, fatter, hiking, fried; and the Ch. 11 line "The snow was again falling ... on the sledge."
V = {}
V['g3ela-28-1-teach-morph'] = dict(title='Morphology', sub='Two word parts that mean together', scenes=[
 dict(at=None, items=[(None, '<div class="lab">✨ Look up at the night sky!</div>'), ('Constellation.', '<div class="huge">constellation</div>')]),
 dict(at='A constellation is', items=[(None, '<div class="def"><b>constellation</b><span>a group of stars together in the sky ⭐⭐⭐</span></div>'),
   ('The front part', word('constellation', 'con')), ('means with or together', '<div class="build"><span class="tile key">con</span><b>=</b><span class="tile">with, together 🤝</span></div>'),
   ('Its twin, com', '<div class="build"><span class="tile key">com</span><b>=</b><span class="tile key">con</span><b>=</b><span class="tile">together</span></div>')]),
 dict(at='Read the four words', items=[(None, '<div class="say">📖 Read the four words.</div>'), ('tap See what was hiding', PILL('See what was hiding')),
   ('Then type each whole word', '<div class="build"><span class="tile">com</span><b>+</b><span class="tile">?</span><b>=</b><span class="tile"><i class="blank"></i></span></div>')]),
])
V['g3ela-28-1-teach-vocab'] = dict(title='Vocabulary', sub='Be a word detective', scenes=[
 dict(at=None, items=[(None, '<div class="lab">🔍 Word detective</div>'), ('Uncombed.', '<div class="huge">uncombed</div>')]),
 dict(at="Here's the sentence", items=[(None, '<div class="quote">They came bundling out of the cave … looking very frowsty and unbrushed and <b class="hl">uncombed</b>.<small>Chapter 10</small></div>')]),
 dict(at='One, read the sentence', items=[(None, '<div class="steps"><span><i>1</i>Read</span><span><i>2</i>Word parts</span><span><i>3</i>Check</span></div>'),
   ('they just woke up', '<div class="say">1️⃣ They just woke up 😴</div>'),
   ('Two, look for word parts', tiles(('un', False), ('comb', True), ('ed', False))),
   ('Uncombed means', '<div class="def"><b>uncombed</b><span>not combed 💇</span></div>')]),
 dict(at='Read how we figured', items=[(None, '<div class="say">✏️ Fill in each sentence from the word bank.</div>'),
   ('tap Check My Work', PILL('Check My Work')), ('Last, play the matching game', PILL('Matching game'))]),
])
V['g3ela-28-1-teach-gram'] = dict(title='Grammar', sub='An apostrophe has two jobs', scenes=[
 dict(at=None, items=[(None, '<div class="lab">An apostrophe ’ has two jobs</div>')]),
 dict(at='Job one', items=[(None, '<div class="step1"><i>1</i>Joins two words</div>'), ('Can, plus not', '<div class="build"><span class="tile">can</span><b>+</b><span class="tile m">not</span><b>=</b><span class="tile key">can’t</span></div>'),
   ('The apostrophe sits', '<div class="say">’ sits where the letters left 👋</div>')]),
 dict(at='Job two', items=[(None, '<div class="step1"><i>2</i>Shows belonging</div>'), ("The dog's bone", '<div class="quote">the <b class="hl">dog’s</b> bone 🐕🦴</div>'),
   ('belongs to the dog', '<div class="say">the bone belongs to the dog</div>')]),
 dict(at='Tap Now check your thinking', items=[(None, PILL('Now check your thinking')), ('Then find the five words', '<div class="say">🔍 Find the five words that need an apostrophe.</div>')]),
])
V['g3ela-28-1-teach-spell'] = dict(title='Spelling', sub='Three spelling changes', scenes=[
 dict(at=None, items=[(None, '<div class="lab">Three spelling changes, coming up!</div>')]),
 dict(at='Swim, swimming', items=[(None, '<div class="swap">swim ➜ <b>swim<b class="hl">m</b>ing</b></div>'), ('the m doubles', '<div class="say">✌️ double the last letter</div>')]),
 dict(at='Bake, baking', items=[(None, '<div class="swap">bak<s>e</s> ➜ <b>baking</b></div>'), ('the e drops off', '<div class="say">✂️ drop the silent e</div>')]),
 dict(at='Try, tried', items=[(None, '<div class="swap">tr<s>y</s> ➜ <b>tr<b class="hl">i</b>ed</b></div>'), ('the y turns into i', '<div class="say">🔁 change y to i</div>')]),
 dict(at='Think about the questions', items=[(None, PILL('Now name the pattern')),
   ('Then sort the words', '<div class="bins"><span>Doubled</span><span>Dropped the e</span><span>y ➜ i</span></div>')]),
])
V['g3ela-28-2-teach-morph'] = dict(title='Morphology', sub='Match the word to its meaning', scenes=[
 dict(at=None, items=[(None, '<div class="lab">👀 Watch one match first</div>'), ('Companion.', word('companion', 'com'))]),
 dict(at='Find the front part', items=[(None, tiles(('com: with', True), ('panion', False))),
   ('A companion is', '<div class="build"><span class="tile">companion</span><b>➜</b><span class="tile m">a friend who goes along with you 🚶🚶</span></div>'),
   ("That's my match", '<div class="say">✅ That’s my match!</div>')]),
 dict(at='Read the Remember box', items=[(None, '<div class="say">📌 Read the Remember box.</div>'),
   ('Then tap a word', '<div class="build"><span class="tile">👆 a word</span><b>➜</b><span class="tile m">👆 its meaning</span></div>')]),
])
V['g3ela-28-2-teach-vocab'] = dict(title='Vocabulary', sub='Match each word', scenes=[
 dict(at=None, items=[(None, '<div class="ask">Ever seen a grin that made you want to look away? 😬</div>'), ('Repulsive.', '<div class="huge">repulsive</div>')]),
 dict(at='The dwarf grins', items=[(None, '<div class="quote">He grinned in a <b class="hl">repulsive</b> manner.<small>the dwarf, Chapter 11</small></div>'),
   ('Repulsive means', '<div class="def"><b>repulsive</b><span>so nasty you want to turn away 🙈</span></div>')]),
 dict(at='Now tap a word', items=[(None, '<div class="build"><span class="tile">👆 a word</span><b>➜</b><span class="tile m">👆 its meaning</span></div>'),
   ('Match all four', '<div class="say">Match all four ✅✅✅✅</div>')]),
])
V['g3ela-28-2-teach-gram'] = dict(title='Grammar', sub='What does each apostrophe do?', scenes=[
 dict(at=None, items=[(None, '<div class="ask">🔍 Spot the apostrophe</div>'),
   ("Mrs. Beaver's sewing", '<div class="quote">Mrs. <b class="hl">Beaver’s</b> sewing machine was too heavy to bring. 🧵</div>')]),
 dict(at="Beaver's, with", items=[(None, '<div class="say">Beaver’s = the machine belongs to Mrs. Beaver</div>')]),
 dict(at='Find the apostrophes', items=[(None, '<div class="bins"><span>joins two words</span><span>shows belonging</span></div>'),
   ('tap Now check your thinking', PILL('Now check your thinking')), ('Then fix the paragraph', '<div class="say">✏️ Then fix the paragraph.</div>')]),
])
V['g3ela-28-2-teach-spell'] = dict(title='Spelling', sub='Change detective', scenes=[
 dict(at=None, items=[(None, '<div class="lab">🔎 Detective question!</div>'),
   ('Which of these doubled', '<div class="build"><span class="tile">fatter</span><b>or</b><span class="tile">faster</span></div>')]),
 dict(at='Fatter!', items=[(None, '<div class="huge">fa<b class="hl">tt</b>er ✅</div>'), ('Fat has a short vowel', '<div class="say">f<b class="gold">a</b>t: short vowel + one t ➜ the t doubles</div>')]),
 dict(at='Read the rule', items=[(None, '<div class="say">📌 Read the rule.</div>'), ('Then in each row', '<div class="say">👆 In each row, tap the one word that matches.</div>')]),
])
V['g3ela-28-2-teach-rwm'] = dict(title='Read Like a Writer', sub='Reader, writer, mimic', scenes=[
 dict(at=None, items=[(None, '<div class="lab">A sentence from Chapter 11</div>'),
   ('The snow was again', '<div class="quote">The snow was again falling as they came into the courtyard, <b class="hl">but</b> she took no notice of that and made Edmund sit beside her on the sledge.<small>Chapter 11</small></div>')]),
 dict(at='Part one', items=[(None, '<div class="step1"><i>1</i>Read like a reader</div>'), ("The Witch doesn't care", '<div class="say">The Witch doesn’t care about the snow ❄️🙅</div>')]),
 dict(at='Part two', items=[(None, '<div class="step1"><i>2</i>Read like a writer</div>'), ('Weather first', '<div class="say"><b class="gold">weather</b> first ➜ <b class="gold">but</b> ➜ the story</div>')]),
 dict(at='Part three', items=[(None, '<div class="step1"><i>3</i>Mimic</div>'),
   ("Here's mine", '<div class="quote mine">The rain was pouring as we left school, <b class="hl">but</b> Mom took no notice and made us run to the car.<small>Opti’s sentence</small></div>')]),
 dict(at="Now it's your turn", items=[(None, '<div class="say">Now you: the sentence about the snow and the moon 🌙</div>'),
   ('Write one sentence', '<div class="boxes"><span class="slot">Reader</span><span class="slot">Writer</span><span class="slot">Mimic</span></div>')]),
])
V['g3ela-28-3-teach-morph'] = dict(title='Morphology', sub='Build the word', scenes=[
 dict(at=None, items=[(None, '<div class="lab">🧱 Snap the parts together</div>'), ('Con.', tiles(('con', True))), ('Tact.', tiles(('con', True), ('tact', False))), ('Contact!', '<div class="huge">contact</div>')]),
 dict(at='When two things', items=[(None, '<div class="def"><b>contact</b><span>touching together 🤝</span></div>')]),
 dict(at='Say each pair', items=[(None, '<div class="say">🗣️ Say each pair of parts out loud.</div>'),
   ('Type the whole word', '<div class="build"><span class="tile">con</span><b>+</b><span class="tile">?</span><b>=</b><span class="tile"><i class="blank"></i></span></div>'),
   ('Then tap Check My Answers', PILL('Check My Answers'))]),
])
V['g3ela-28-3-teach-vocab'] = dict(title='Vocabulary', sub='Pick the word that fits', scenes=[
 dict(at=None, items=[(None, '<div class="say">Try each word in the blank. Keep the one that makes sense.</div>')]),
 dict(at="Here's my sentence", items=[(None, '<div class="quote mine">After a long nap, my grandpa felt <i class="blank"></i>.<small>Opti’s sentence</small></div>'),
   ('Herald?', '<div class="say">herald? 🤔 no</div>'), ('Renewed? Yes', '<div class="say">renewed? ✅</div>')]),
 dict(at='Now pick the word', items=[(None, '<div class="say">👆 Pick the word that fits each sentence.</div>')]),
])
V['g3ela-28-3-teach-gram'] = dict(title='Grammar', sub='Be the editor', scenes=[
 dict(at=None, items=[(None, '<div class="lab">✏️ Let’s be the editor</div>'),
   ('The dwarfs whip', '<div class="quote">The <b class="hl">dwarfs</b> whip <b class="hl">wasnt</b> kind to the reindeer.</div>')]),
 dict(at="Dwarf's needs", items=[(None, '<div class="swap">dwarfs ➜ <b>dwarf’s</b> (belonging)</div>'), ("Wasn't needs one too", '<div class="swap">wasnt ➜ <b>wasn’t</b> (was + not)</div>')]),
 dict(at='Read the before and after', items=[(None, '<div class="say">📖 Read the before and after.</div>'), ('tap Check yourself', PILL('Check yourself')),
   ('Then fix the sentence', '<div class="say">✏️ Fix the sentence in the gray box.</div>')]),
])
V['g3ela-28-3-teach-spell'] = dict(title='Spelling', sub='Build the word', scenes=[
 dict(at=None, items=[(None, '<div class="lab">🧱 Let’s build one</div>'), ('Hike, plus', tiles(('hike', True), ('ing', False)))]),
 dict(at='Hike ends in a silent e', items=[(None, '<div class="swap">hik<s>e</s> + ing</div>'), ('Hiking!', '<div class="huge">hiking 🥾</div>')]),
 dict(at='Read the rule', items=[(None, '<div class="say">📌 Read the rule.</div>'), ('Decide which change', '<div class="bins"><span>✌️ double</span><span>✂️ drop e</span><span>🔁 y ➜ i</span></div>'),
   ('Then tap the card', PILL('Tap the card'))]),
])
V['g3ela-28-4-teach-morph'] = dict(title='Morphology', sub='Roll and explain', scenes=[
 dict(at=None, items=[(None, '<div class="ask">⚡ Quick question: what do com and con mean?</div>'), ('With, or together', '<div class="build"><span class="tile key">com</span><b>·</b><span class="tile key">con</span><b>=</b><span class="tile">with, together</span></div>')]),
 dict(at="Here's a word", items=[(None, word('community', 'com')), ('A community is', '<div class="def"><b>community</b><span>people who live together 🏘️</span></div>')]),
 dict(at='Now tap Roll the Dice', items=[(None, PILL('🎲 Roll the Dice')), ('Say what each word means', '<div class="say">🗣️ Say what the word means.</div>'), ('tap Check My Thinking', PILL('Check My Thinking'))]),
])
V['g3ela-28-4-teach-vocab'] = dict(title='Vocabulary', sub='Use a word to tell the story', scenes=[
 dict(at=None, items=[(None, '<div class="lab">✍️ Here’s how I’d use a word</div>'), ('Solemn.', '<div class="huge">solemn</div>')]),
 dict(at='Peter was silent', items=[(None, '<div class="quote mine">Peter was silent and <b class="hl">solemn</b> when Father Christmas handed him a sword.<small>Opti’s sentence</small></div>'),
   ('One word, one moment', '<div class="say">1 word + 1 moment 📖</div>')]),
 dict(at='Now choose one', items=[(None, '<div class="say">✏️ Choose one of your words. Write a sentence about Chapters 10 to 12.</div>')]),
])
V['g3ela-28-4-teach-gram'] = dict(title='Grammar', sub='Two passes', scenes=[
 dict(at=None, items=[(None, '<div class="lab">✏️ Two passes, like an editor</div>'), ('mr beavers tail', '<div class="quote">mr beavers tail was the last thing lucy saw</div>')]),
 dict(at='Pass one', items=[(None, '<div class="step1"><i>1</i>Capitals</div>'), ('Mr., Beaver and Lucy', '<div class="quote"><b class="hl">M</b>r. <b class="hl">B</b>eavers tail was the last thing <b class="hl">L</b>ucy saw</div>')]),
 dict(at='Pass two', items=[(None, '<div class="step1"><i>2</i>Apostrophes</div>'), ("Beaver's tail", '<div class="quote">Mr. Beaver<b class="hl">’</b>s tail was the last thing Lucy saw. 🦫</div>')]),
 dict(at='Now do your passes', items=[(None, '<div class="say">👆 Tap every word that needs fixing.</div>')]),
])
V['g3ela-28-4-teach-spell'] = dict(title='Spelling', sub='Which change dice', scenes=[
 dict(at=None, items=[(None, '<div class="lab">🎲 Here’s my roll</div>'), ('Fry, plus', tiles(('fry', True), ('ed', False)))]),
 dict(at='Fry ends in y', items=[(None, '<div class="swap">fr<s>y</s> ➜ fr<b class="hl">i</b> + ed</div>'), ('Fried!', '<div class="huge">fried 🍳</div>')]),
 dict(at='Tap Roll the dice', items=[(None, PILL('🎲 Roll the dice')), ('decide which change', '<div class="say">🤔 Which change, or none?</div>'), ('Check my answer', PILL('Check my answer'))]),
])
