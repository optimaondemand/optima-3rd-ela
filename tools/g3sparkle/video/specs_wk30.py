def word(w, part=None, cls=''):
    if part:
        i = w.index(part)
        return '<span class="wd %s">%s<b class="pt">%s</b>%s</span>' % (cls, w[:i], part, w[i+len(part):])
    return '<span class="wd %s">%s</span>' % (cls, w)
PILL = lambda t: '<span class="pill">👆 %s</span>' % t
def tiles(*ps): return '<div class="build">' + '<b>+</b>'.join('<span class="tile%s">%s</span>' % (' key' if k else '', t) for t, k in ps) + '</div>'
TAPMEAN = '<div class="build"><span class="tile">👆 a word</span><b>➜</b><span class="tile m">👆 its meaning</span></div>'
# Scene specs for the week 30 Opti teach films (LWW Ch. 16-17 + synthesis). SILENT for now (tone.py timing); captions carry the words.
# Never shows a page answer or a game item: interview, transfer, report, transatlantic; liberated (Ch. 16), remarkable (Ch. 17),
# Opti's friends sentence, reconciled Edmund; lucy found mr. tumnus / the fauns scarf / the witchs sledge / the professors house;
# cake-boat-rewrite, goat-ran-lake, sunset, pilot; and a Ch. 16 sentence (Instead of all that deadly white ...).
V = {}
V['g3ela-30-1-teach-morph'] = dict(title='Morphology', sub='Roots from the whole year', scenes=[
 dict(at=None, items=[(None, '<div class="lab">🧩 Can you crack this one?</div>'), ('Interview.', word('interview', 'inter'))]),
 dict(at='Inter means between', items=[(None, tiles(('inter: between', True), ('view: see', False))),
   ('An interview is', '<div class="def"><b>interview</b><span>a talk between two people 🎤🙂</span></div>')]),
 dict(at='Every root on this page', items=[(None, '<div class="say">✅ You already know every root on this page.</div>'), ('tap See if you cracked it', PILL('See if you cracked it')),
   ('Then type the missing part', '<div class="build"><span class="tile">trans</span><b>+</b><span class="tile"><i class="blank"></i></span></div>')]),
])
V['g3ela-30-1-teach-vocab'] = dict(title='Vocabulary', sub='Be a word detective', scenes=[
 dict(at=None, items=[(None, '<div class="lab">🔍 Word detective</div>'), ('Liberated.', '<div class="huge">liberated</div>')]),
 dict(at="Here's the sentence", items=[(None, '<div class="quote">The whole crowd of <b class="hl">liberated</b> statues surged back into the courtyard.<small>Chapter 16</small></div>')]),
 dict(at='One, read the sentence', items=[(None, '<div class="steps"><span><i>1</i>Read</span><span><i>2</i>Word parts</span><span><i>3</i>Check</span></div>'),
   ('the statues are alive', '<div class="say">1️⃣ The statues are alive again 🗿➜🦁</div>'),
   ('Two, look for word parts', tiles(('liber', True), ('ate', False), ('ed', False))),
   ('Liberated means', '<div class="def"><b>liberated</b><span>set free 🕊️</span></div>')]),
 dict(at='Read how we figured', items=[(None, '<div class="say">✏️ Fill in each sentence from the word bank.</div>'),
   ('tap Check My Work', PILL('Check My Work')), ('Last, play the matching game', PILL('Matching game'))]),
])
V['g3ela-30-1-teach-gram'] = dict(title='Grammar', sub='Capital letters', scenes=[
 dict(at=None, items=[(None, '<div class="lab">✏️ An editor hunts for capitals</div>'), ('lucy found mr. tumnus', '<div class="quote">lucy found mr. tumnus.</div>')]),
 dict(at='Lucy is a name', items=[(None, '<div class="quote"><b class="hl">L</b>ucy found mr. tumnus.</div>'),
   ('Mr. Tumnus is a name too', '<div class="quote"><b class="hl">L</b>ucy found <b class="hl">M</b>r. <b class="hl">T</b>umnus. 🐐</div>'),
   ('Names get capitals', '<div class="say">Names get capitals, wherever they are.</div>')]),
 dict(at='Tap Now check your thinking', items=[(None, PILL('Now check your thinking')), ('Then tap the five words', '<div class="say">👆 Tap the five words that need a capital.</div>')]),
])
V['g3ela-30-1-teach-spell'] = dict(title='Spelling', sub='Patterns from the year', scenes=[
 dict(at=None, items=[(None, '<div class="lab">🗂️ Three patterns in one pile!</div>')]),
 dict(at='Cake:', items=[(None, '<div class="swap">cak<b class="hl">e</b> ➜ silent e 🎂</div>'), ('Boat:', '<div class="swap">b<b class="hl">oa</b>t ➜ vowel team ⛵</div>'),
   ('Rewrite:', tiles(('re', False), ('write', True)))]),
 dict(at='Think about the questions', items=[(None, PILL('Now name the pattern')),
   ('Then sort the words', '<div class="bins"><span>Magic-e</span><span>Vowel team</span><span>Prefix + base</span></div>')]),
])
V['g3ela-30-2-teach-morph'] = dict(title='Morphology', sub='Match the word to its meaning', scenes=[
 dict(at=None, items=[(None, '<div class="lab">👀 Watch one match first</div>'), ('Transfer.', word('transfer', 'trans'))]),
 dict(at='Find the root', items=[(None, tiles(('trans: across', True), ('fer', False))),
   ('To transfer is', '<div class="build"><span class="tile">transfer</span><b>➜</b><span class="tile m">move something across to a new place 📦➡️</span></div>'),
   ("That's my match", '<div class="say">✅ That’s my match!</div>')]),
 dict(at='Read the Remember box', items=[(None, '<div class="say">📌 Read the Remember box.</div>'), ('Then tap a word', TAPMEAN)]),
])
V['g3ela-30-2-teach-vocab'] = dict(title='Vocabulary', sub='Match each word', scenes=[
 dict(at=None, items=[(None, '<div class="ask">Ever met someone truly amazing? 🤩</div>'), ('Remarkable.', '<div class="huge">remarkable</div>')]),
 dict(at='The book says', items=[(None, '<div class="quote">… the Professor, who was a very <b class="hl">remarkable</b> man …<small>Chapter 17</small></div>'),
   ('Remarkable means', '<div class="def"><b>remarkable</b><span>so unusual it’s worth talking about</span></div>')]),
 dict(at='Now tap a word', items=[(None, TAPMEAN), ('Match all four', '<div class="say">Match all four ✅✅✅✅</div>')]),
])
V['g3ela-30-2-teach-gram'] = dict(title='Grammar', sub='Four rules, one sentence', scenes=[
 dict(at=None, items=[(None, '<div class="lab">✏️ Four rules, one sentence</div>'), ('the fauns scarf', '<div class="quote">the fauns scarf was red and lucy liked it</div>')]),
 dict(at='The needs a capital', items=[(None, '<div class="swap">the ➜ <b>The</b> (starts the sentence)</div>'), ("Faun's needs", '<div class="swap">fauns ➜ <b>faun’s</b> (belonging) 🧣</div>'),
   ('A comma goes before and', '<div class="swap">red and ➜ <b>red, and</b></div>'), ('And Lucy is a name', '<div class="swap">lucy ➜ <b>Lucy</b></div>')]),
 dict(at='Tap Check yourself', items=[(None, PILL('Check yourself')), ('Then tap every word', '<div class="say">👆 Tap every word that is wrong.</div>')]),
])
V['g3ela-30-2-teach-spell'] = dict(title='Spelling', sub='Pattern hunt', scenes=[
 dict(at=None, items=[(None, '<div class="lab">🔎 Pattern hunt!</div>'), ('The goat ran to the lake', '<div class="quote mine">The goat ran to the lake.<small>Opti’s sentence</small></div>')]),
 dict(at='Goat:', items=[(None, '<div class="swap">g<b class="hl">oa</b>t ➜ vowel team 👆</div>'), ('Ran:', '<div class="swap">ran ➜ closed, no tap</div>'), ('Lake:', '<div class="swap">lak<b class="hl">e</b> ➜ silent e 👆</div>')]),
 dict(at='Read the rule', items=[(None, '<div class="say">📌 Read the rule.</div>'), ('Then tap every word', '<div class="say">👆 Tap every silent-e, vowel-team or r-controlled word.</div>')]),
])
V['g3ela-30-2-teach-rwm'] = dict(title='Read Like a Writer', sub='Reader, writer, mimic', scenes=[
 dict(at=None, items=[(None, '<div class="lab">A sentence from Chapter 16</div>'),
   ('Instead of all that deadly white', '<div class="quote"><b class="hl">Instead of</b> all that deadly white the courtyard was now a blaze of colors.<small>Chapter 16</small></div>')]),
 dict(at='Part one', items=[(None, '<div class="step1"><i>1</i>Read like a reader</div>'), ('The statues are alive', '<div class="say">The statues are alive, and the courtyard is bright 🌈</div>')]),
 dict(at='Part two', items=[(None, '<div class="step1"><i>2</i>Read like a writer</div>'), ('Two pictures', '<div class="say">⬜ deadly white ➜ 🌈 a blaze of colors</div>'),
   ('Instead of flips', '<div class="say"><b class="gold">Instead of</b> flips one picture into the other</div>')]),
 dict(at='Part three', items=[(None, '<div class="step1"><i>3</i>Mimic</div>'),
   ("Here's mine", '<div class="quote mine"><b class="hl">Instead of</b> all that gray snow, the yard was now a carpet of green grass.<small>Opti’s sentence</small></div>')]),
 dict(at="Now it's your turn", items=[(None, '<div class="say">Now you: the museum and the zoo 🏛️➜🦓</div>'),
   ('Write one sentence', '<div class="boxes"><span class="slot">Reader</span><span class="slot">Writer</span><span class="slot">Mimic</span></div>')]),
])
V['g3ela-30-3-teach-morph'] = dict(title='Morphology', sub='Build the word', scenes=[
 dict(at=None, items=[(None, '<div class="lab">🧱 Snap the parts together</div>'), ('Re.', tiles(('re', False))), ('Port.', tiles(('re', False), ('port', True))), ('Report!', '<div class="huge">report</div>')]),
 dict(at='When you report', items=[(None, '<div class="def"><b>report</b><span>to carry the news back 📰</span></div>')]),
 dict(at='Say each pair', items=[(None, '<div class="say">🗣️ Say each pair of parts out loud.</div>'),
   ('Type the whole word', '<div class="build"><span class="tile">?</span><b>+</b><span class="tile">?</span><b>=</b><span class="tile"><i class="blank"></i></span></div>'),
   ('Then tap Check My Answers', PILL('Check My Answers'))]),
])
V['g3ela-30-3-teach-vocab'] = dict(title='Vocabulary', sub='Pick the word that fits', scenes=[
 dict(at=None, items=[(None, '<div class="say">Try each word in the blank. Keep the one that makes sense.</div>')]),
 dict(at="Here's my sentence", items=[(None, '<div class="quote mine">After their fight, the two friends were <i class="blank"></i>.<small>Opti’s sentence</small></div>'),
   ('Sovereign?', '<div class="say">sovereign? 🤔 no</div>'), ('Reconciled? Yes', '<div class="say">reconciled? ✅ 🤝</div>')]),
 dict(at='Now pick the word', items=[(None, '<div class="say">👆 Pick the word that fits each sentence.</div>')]),
])
V['g3ela-30-3-teach-gram'] = dict(title='Grammar', sub='Be the editor', scenes=[
 dict(at=None, items=[(None, '<div class="lab">✏️ Be the editor</div>'), ('the witchs sledge', '<div class="quote">the witchs sledge was fast and edmund was cold</div>')]),
 dict(at='The gets a capital', items=[(None, '<div class="quote"><b class="hl">T</b>he <b class="hl">Witch’s</b> sledge was fast<b class="hl">,</b> and <b class="hl">E</b>dmund was cold. 🛷</div>')]),
 dict(at='Read the before and after', items=[(None, '<div class="say">📖 Read the before and after.</div>'), ('tap Check yourself', PILL('Check yourself')),
   ('Then fix the sentence', '<div class="say">✏️ Fix the sentence in the gray box.</div>')]),
])
V['g3ela-30-3-teach-spell'] = dict(title='Spelling', sub='Spell it by its syllables', scenes=[
 dict(at=None, items=[(None, '<div class="lab">🌅 Spell it by its syllables</div>'), ('Sunset.', '<div class="huge">sunset</div>')]),
 dict(at='Sun:', items=[(None, tiles(('sun', True))), ('Set:', tiles(('sun', True), ('set', True))), ('Sun, set', '<div class="say">two closed syllables, two short vowels</div>')]),
 dict(at='Read the rule', items=[(None, '<div class="say">👀 Look ➜ ✋ cover ➜ ✏️ write</div>'), ('Then tap the card', PILL('Tap the card to check'))]),
])
V['g3ela-30-4-teach-morph'] = dict(title='Morphology', sub='Roll and explain', scenes=[
 dict(at=None, items=[(None, '<div class="ask">⚡ Quick question: what does trans mean?</div>'), ('Across!', '<div class="build"><span class="tile key">trans</span><b>=</b><span class="tile">across ➡️</span></div>')]),
 dict(at="Here's a word", items=[(None, word('transatlantic', 'trans')), ('It means across', '<div class="def"><b>transatlantic</b><span>across the Atlantic Ocean 🚢🌊</span></div>')]),
 dict(at='Say what the word part means', items=[(None, PILL('🎲 Roll the Dice')), ('Say what the word means', '<div class="say">🗣️ Say what the word means.</div>'), ('tap Check My Thinking', PILL('Check My Thinking'))]),
])
V['g3ela-30-4-teach-vocab'] = dict(title='Vocabulary', sub='Use a word about the ending', scenes=[
 dict(at=None, items=[(None, '<div class="lab">✍️ Watch me use a word</div>'), ('Reconciled.', '<div class="huge">reconciled</div>')]),
 dict(at='In the end', items=[(None, '<div class="quote mine">In the end, Edmund and his family are <b class="hl">reconciled</b>.<small>Opti’s sentence</small></div>'),
   ('One word, the whole story', '<div class="say">1 word = the whole story 📖</div>')]),
 dict(at='Now choose your word', items=[(None, '<div class="say">✏️ Choose your word. Write a sentence about the ending.</div>')]),
])
V['g3ela-30-4-teach-gram'] = dict(title='Grammar', sub='Two passes', scenes=[
 dict(at=None, items=[(None, '<div class="lab">✏️ Two passes, like an editor</div>'), ('the professors house', '<div class="quote">the professors house was big and the children explored it</div>')]),
 dict(at='Pass one', items=[(None, '<div class="step1"><i>1</i>Capitals</div>'), ('The, and Professor', '<div class="quote"><b class="hl">T</b>he <b class="hl">P</b>rofessors house was big and the children explored it</div>')]),
 dict(at='Pass two', items=[(None, '<div class="step1"><i>2</i>Apostrophes and commas</div>'), ("Professor's, and a comma", '<div class="quote">The Professor<b class="hl">’</b>s house was big<b class="hl">,</b> and the children explored it. 🏠</div>')]),
 dict(at='Now do your passes', items=[(None, '<div class="say">👆 Tap every word that needs fixing.</div>')]),
])
V['g3ela-30-4-teach-spell'] = dict(title='Spelling', sub='Syllable review dice', scenes=[
 dict(at=None, items=[(None, '<div class="lab">🎲 Dice roll: pilot!</div>')]),
 dict(at='Split it after the vowel', items=[(None, tiles(('pi', True), ('lot', False))), ('Pi is open', '<div class="say">pi: open, the i says its name ✈️</div>'), ('Lot is closed', '<div class="say">lot: closed, short o</div>')]),
 dict(at='Tap Roll the dice', items=[(None, PILL('🎲 Roll the dice')), ('name its syllable types', '<div class="say">🗣️ Name the syllable types.</div>'), ('Check my answer', PILL('Check my answer'))]),
])
