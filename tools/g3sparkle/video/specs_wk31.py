def word(w, part=None, cls=''):
    if part:
        i = w.index(part)
        return '<span class="wd %s">%s<b class="pt">%s</b>%s</span>' % (cls, w[:i], part, w[i+len(part):])
    return '<span class="wd %s">%s</span>' % (cls, w)
PILL = lambda t: '<span class="pill">👆 %s</span>' % t
def tiles(*ps): return '<div class="build">' + '<b>+</b>'.join('<span class="tile%s">%s</span>' % (' key' if k else '', t) for t, k in ps) + '</div>'
TAPMEAN = '<div class="build"><span class="tile">👆 a word</span><b>➜</b><span class="tile m">👆 its meaning</span></div>'
# Scene specs for the week 31 Opti teach films (Paired Texts: The Courage to Act). SILENT for now (tone.py timing); captions carry the words.
# Never shows a page answer or a game item: replay, painless, daring, "when grace saw the wreck she telled her father"; unsafe, loyal,
# Grace rowed / Although the sea was rough, wonderful; repaint, integrity (Leo), the boats oars, everyone; unbroken, integrity (Lucy),
# the keepers daughter, lifeboat; and a Text 2 sentence (Mira's heart hammered.) that is not the page's RWM sentence.
V = {}
V['g3ela-31-1-teach-morph'] = dict(title='Morphology', sub='Prefixes and suffixes', scenes=[
 dict(at=None, items=[(None, '<div class="ask">What happens when you add a part to a word? 🤔</div>'), ('Replay.', word('replay', 're'))]),
 dict(at='Re is a prefix', items=[(None, tiles(('re: again', True), ('play', False))), ('Replay means', '<div class="def"><b>replay</b><span>play again 🔁</span></div>')]),
 dict(at='Painless.', items=[(None, word('painless', 'less')), ('Less is a suffix', tiles(('pain', False), ('less: without', True))),
   ('Painless means', '<div class="def"><b>painless</b><span>without pain 🙂</span></div>')]),
 dict(at='Every part on this page', items=[(None, '<div class="say">✅ You already know every part on this page.</div>'), ('tap See what was hiding', PILL('See what was hiding')),
   ('then type the missing part', '<div class="build"><span class="tile">un</span><b>+</b><span class="tile"><i class="blank"></i></span></div>')]),
])
V['g3ela-31-1-teach-vocab'] = dict(title='Vocabulary', sub='Be a word detective', scenes=[
 dict(at=None, items=[(None, '<div class="lab">🔍 Word detective</div>'), ('Daring.', '<div class="huge">daring</div>')]),
 dict(at="Here's my sentence", items=[(None, '<div class="quote">Grace made a <b class="hl">daring</b> trip across the stormy sea. 🌊<small>Opti’s sentence</small></div>')]),
 dict(at='One, read the sentence', items=[(None, '<div class="steps"><span><i>1</i>Read</span><span><i>2</i>Word parts</span><span><i>3</i>Check</span></div>'),
   ('she went, even though', '<div class="say">1️⃣ She went, even though it was dangerous.</div>'),
   ('Two, look for word parts', tiles(('dare', True), ('ing', False))),
   ('Daring means', '<div class="def"><b>daring</b><span>brave enough to take a risk 🚣</span></div>')]),
 dict(at='Now fill in each sentence', items=[(None, '<div class="say">✏️ Fill in each sentence from the word bank.</div>'), ('play the matching game', PILL('Matching game'))]),
])
V['g3ela-31-1-teach-gram'] = dict(title='Grammar', sub='A year of rules', scenes=[
 dict(at=None, items=[(None, '<div class="lab">✏️ A whole year of rules</div>'), ('when grace saw', '<div class="quote">when grace saw the wreck she telled her father</div>')]),
 dict(at='When starts the sentence', items=[(None, '<div class="swap">when ➜ <b>When</b> (starts the sentence)</div>'),
   ('Grace is a name', '<div class="swap">grace ➜ <b>Grace</b> (a name)</div>'),
   ('A comma goes after wreck', '<div class="swap">wreck ➜ <b>wreck,</b> (closes the opening part)</div>'),
   ('And telled should be told', '<div class="swap">telled ➜ <b>told</b> 🗣️</div>')]),
 dict(at='Tap Now check your thinking', items=[(None, PILL('Now check your thinking')), ('Then tap all six words', '<div class="say">👆 Tap all six words that need fixing.</div>')]),
])
V['g3ela-31-1-teach-spell'] = dict(title='Spelling', sub='Prefix or suffix?', scenes=[
 dict(at=None, items=[(None, '<div class="ask">Front or back? ⬅️➡️</div>')]),
 dict(at='Replay:', items=[(None, '<div class="swap"><b class="hl">re</b>play ➜ prefix at the front</div>'),
   ('Painless:', '<div class="swap">pain<b class="hl">less</b> ➜ suffix at the end</div>')]),
 dict(at='Think about the questions', items=[(None, PILL('Now name the pattern')),
   ('Then sort the words', '<div class="bins"><span>Prefix at the front</span><span>Suffix at the end</span></div>')]),
])
V['g3ela-31-2-teach-morph'] = dict(title='Morphology', sub='Match the word to its meaning', scenes=[
 dict(at=None, items=[(None, '<div class="lab">👀 Watch one match first</div>'), ('Unsafe.', word('unsafe', 'un'))]),
 dict(at='Find the prefix', items=[(None, tiles(('un: not', True), ('safe', False))),
   ('So unsafe means', '<div class="build"><span class="tile">unsafe</span><b>➜</b><span class="tile m">not safe ⚠️</span></div>'),
   ("That's my match", '<div class="say">✅ That’s my match!</div>')]),
 dict(at='Read the Remember box', items=[(None, '<div class="say">📌 Read the Remember box.</div>'), ('Then tap a word', TAPMEAN)]),
])
V['g3ela-31-2-teach-vocab'] = dict(title='Vocabulary', sub='Match each word', scenes=[
 dict(at=None, items=[(None, '<div class="lab">💛 A good-character word</div>'), ('Loyal.', '<div class="huge">loyal</div>')]),
 dict(at='A loyal friend', items=[(None, '<div class="def"><b>loyal</b><span>sticks by you, even when things get hard 🤝</span></div>')]),
 dict(at='Now tap a word', items=[(None, TAPMEAN), ('Match all four', '<div class="say">Match all four ✅✅✅✅</div>')]),
])
V['g3ela-31-2-teach-gram'] = dict(title='Grammar', sub='Three kinds of sentences', scenes=[
 dict(at=None, items=[(None, '<div class="ask">Simple, compound or complex?</div>')]),
 dict(at='Grace rowed, and', items=[(None, '<div class="quote">Grace rowed, <b class="hl">and</b> her father helped.</div>'),
   ('Two complete thoughts', '<div class="say">Two complete thoughts + and = <b>compound</b></div>')]),
 dict(at='Although the sea was rough', items=[(None, '<div class="quote"><b class="hl">Although</b> the sea was rough, they rowed on. 🌊</div>'),
   ("Although starts a part", '<div class="say">A part that can’t stand alone = <b>complex</b></div>')]),
 dict(at='Name each sentence', items=[(None, PILL('Now check your thinking')), ('Then tap the four words', '<div class="say">👆 Tap the four words that are wrong.</div>')]),
])
V['g3ela-31-2-teach-spell'] = dict(title='Spelling', sub='Long words', scenes=[
 dict(at=None, items=[(None, '<div class="lab">👏 Clap it with me</div>'), ('Wonderful.', '<div class="build"><span class="tile">won</span><span class="tile">der</span><span class="tile">ful</span></div>')]),
 dict(at='Three beats', items=[(None, '<div class="say">3 beats ➜ tap it 👆</div>'), ('Brave?', '<div class="say">brave: 1 beat ➜ no tap</div>')]),
 dict(at='Read the rule', items=[(None, '<div class="say">👆 Tap every word with three or more beats.</div>')]),
])
V['g3ela-31-2-teach-rwm'] = dict(title='Read Like a Writer', sub='Opti shows you how', scenes=[
 dict(at=None, items=[(None, '<div class="lab">✍️ All three parts, with a different sentence</div>'), ("Mira's heart hammered.", '<div class="quote">Mira’s heart hammered.<small>Text 2</small></div>')]),
 dict(at='Part one, read like a reader', items=[(None, '<div class="steps"><span><i>1</i>Reader</span><span><i>2</i>Writer</span><span><i>3</i>Your own</span></div>'),
   ('Mira is very scared', '<div class="say">1️⃣ Mira is very scared.</div>')]),
 dict(at='Part two, read like a writer', items=[(None, '<div class="say">2️⃣ No word <s>scared</s>. A body detail shows it.</div>'),
   ('a heart that hammers', '<div class="say">💓 a heart that hammers, like a hammer on wood 🔨</div>')]),
 dict(at='Part three, write your own', items=[(None, '<div class="quote">Sam’s hands shook on the rope.<small>Opti’s sentence</small></div>'),
   ("Now it's your turn", '<div class="say">Your turn with the author’s sentence: one sentence in each box.</div>')]),
])
V['g3ela-31-3-teach-morph'] = dict(title='Morphology', sub='Build the word', scenes=[
 dict(at=None, items=[(None, '<div class="lab">🧩 Snap the parts together</div>'), ('Re.', tiles(('re', True), ('paint', False))), ('Repaint!', '<div class="huge">repaint 🎨</div>')]),
 dict(at='Say each pair', items=[(None, '<div class="say">Say the parts, then type the whole word.</div>'), ('Then tap Check My Answers', PILL('Check My Answers'))]),
])
V['g3ela-31-3-teach-vocab'] = dict(title='Vocabulary', sub='Pick the word that fits', scenes=[
 dict(at=None, items=[(None, '<div class="lab">🎯 Try each word in the blank</div>'), ('Nobody was watching', '<div class="quote">Nobody was watching, but Leo gave back the extra change. That shows ____.<small>Opti’s sentence</small></div>')]),
 dict(at='Courageous?', items=[(None, '<div class="swap">courageous? 🤔 not quite</div>'), ('Integrity?', '<div class="swap"><b>integrity</b> ✅</div>')]),
 dict(at='Now pick the word', items=[(None, '<div class="say">👆 Pick the word that fits each sentence.</div>')]),
])
V['g3ela-31-3-teach-gram'] = dict(title='Grammar', sub='Be the editor', scenes=[
 dict(at=None, items=[(None, '<div class="lab">✏️ Be the editor</div>'), ('the boats oars', '<div class="quote">the boats oars were heavy and grace was tired</div>')]),
 dict(at='The gets a capital', items=[(None, '<div class="swap">the ➜ <b>The</b></div>'), ("Boat's gets", '<div class="swap">boats ➜ <b>boat’s</b> (belonging) 🚣</div>'),
   ('A comma goes before and', '<div class="swap">heavy ➜ <b>heavy,</b> and</div>'), ('Grace is a name', '<div class="swap">grace ➜ <b>Grace</b></div>')]),
 dict(at='Read the before and after', items=[(None, PILL('Check yourself')), ('Then fix the sentence', '<div class="say">Fix the sentence in the gray box.</div>')]),
])
V['g3ela-31-3-teach-spell'] = dict(title='Spelling', sub='Build long words', scenes=[
 dict(at=None, items=[(None, '<div class="lab">🧱 One beat at a time</div>')]),
 dict(at='Ev.', items=[(None, '<div class="build"><span class="tile">ev</span><span class="tile">er</span><span class="tile">y</span><span class="tile">one</span></div>'),
   ('Everyone!', '<div class="huge">everyone</div>'), ('Four beats', '<div class="say">4 beats, in order ✅</div>')]),
 dict(at='Now tap the chunks', items=[(None, '<div class="say">👆 Tap the chunks in order.</div>')]),
])
V['g3ela-31-4-teach-morph'] = dict(title='Morphology', sub='Roll and explain', scenes=[
 dict(at=None, items=[(None, '<div class="ask">Quick question: what does <b>un</b> mean?</div>'), ('Not!', '<div class="say">un = not ✅</div>')]),
 dict(at="Here's a word", items=[(None, word('unbroken', 'un')), ('Not broken.', '<div class="def"><b>unbroken</b><span>not broken 🚣</span></div>')]),
 dict(at='Say what the word part means', items=[(None, PILL('Roll the Dice!')), ('tap Check My Thinking', PILL('Check My Thinking'))]),
])
V['g3ela-31-4-teach-vocab'] = dict(title='Vocabulary', sub='Use a word about a book', scenes=[
 dict(at=None, items=[(None, '<div class="lab">📚 A word about a book from this year</div>'), ('Integrity.', '<div class="huge">integrity</div>')]),
 dict(at='Lucy showed integrity', items=[(None, '<div class="quote">Lucy showed integrity: she kept telling the truth about Narnia, even when nobody believed her.<small>Opti’s sentence</small></div>')]),
 dict(at='Now choose your word', items=[(None, '<div class="say">✏️ Choose a word. Write a sentence about a book.</div>')]),
])
V['g3ela-31-4-teach-gram'] = dict(title='Grammar', sub='Two passes', scenes=[
 dict(at=None, items=[(None, '<div class="lab">✏️ Two passes, like an editor</div>'), ('the keepers daughter', '<div class="quote">the keepers daughter was brave and she rowed hard</div>')]),
 dict(at='Pass one, capitals', items=[(None, '<div class="swap">Pass 1: the ➜ <b>The</b></div>'),
   ('Pass two', '<div class="swap">Pass 2: keepers ➜ <b>keeper’s</b> · brave ➜ <b>brave,</b> and</div>')]),
 dict(at='Now do your passes', items=[(None, '<div class="say">👆 Tap every word that needs fixing.</div>')]),
])
V['g3ela-31-4-teach-spell'] = dict(title='Spelling', sub='Long word dice', scenes=[
 dict(at=None, items=[(None, '<div class="lab">🎲 Dice roll!</div>'), ('Life,', '<div class="build"><span class="tile">life</span><span class="tile">boat</span></div>'),
   ('Two beats', '<div class="say">lifeboat: 2 beats 🛟</div>')]),
 dict(at='Tap Roll the dice', items=[(None, PILL('Roll the dice')), ('Then tap Check my answer', PILL('Check my answer'))]),
])
