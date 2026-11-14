# Scene specs for the week 25 Opti teach films (The Lion, the Witch and the Wardrobe, Ch. 1-3).
# Each item appears when Opti says its anchor (a phrase from the script). Scripts = DATA.teach (teach_wk25.py).
# SILENT for now (Bethany, Nov 14 2026): timed from an estimated track (tone.py, ~15 characters a second, pauses at
# punctuation); captions carry the words. When the clips are recorded, re-run timeline.py on the real mp3s.
# Never shows an answer the page asks for: examples are telegraph, telework, telephoto, teleconference; spiteful,
# glimpse; "When Lucy felt something crunching", "Because it was raining", the others/unhappy, the Queen's sledge;
# Narnia, Edmund, Susan, apart, lion, Tumnus; and the Ch. 3 line "There was crisp, dry snow under his feet..."
def word(w, part=None, cls=''):
    if part:
        i = w.index(part)
        return '<span class="wd %s">%s<b class="pt">%s</b>%s</span>' % (cls, w[:i], part, w[i+len(part):])
    return '<span class="wd %s">%s</span>' % (cls, w)
PILL = lambda t: '<span class="pill">👆 %s</span>' % t
def tiles(*ps): return '<div class="build">' + '<b>+</b>'.join('<span class="tile%s">%s</span>' % (' key' if k else '', t) for t, k in ps) + '</div>'
V = {}
# ---------------- Day 1: teach the idea ----------------
V['g3ela-25-1-teach-morph'] = dict(title='Morphology', sub='A word part that means far', scenes=[
 dict(at=None, items=[
   (None, '<div class="quote">And then she saw that there was a light ahead of her… <b class="hl">a long way off</b>.<small>Chapter 1</small></div>'),
   ('Far!', '<div class="huge">far 🔭</div>'),
 ]),
 dict(at="There's a word part", items=[
   (None, '<div class="lab">A word part that means far</div>'),
   ('Tele.', '<div class="build"><span class="tile key">tele</span><b>=</b><span class="tile">far</span></div>'),
 ]),
 dict(at="Here's a word", items=[
   (None, word('telegraph', 'tele')),
   ('Long ago', '<div class="say">📨 ⚡ messages sent far away, over wires</div>'),
   ('Tele, far', tiles(('tele: far', True), ('graph: write', False))),
   ('Writing sent far', '<div class="def"><b>telegraph</b><span>writing sent far ✉️ ➜ ➜ ➜</span></div>'),
 ]),
 dict(at='Read the four words', items=[
   (None, '<div class="say">📖 Read the four words and their parts.</div>'),
   ('Then tap See what was hiding', PILL('See what was hiding')),
   ('type each word', '<div class="build"><span class="tile">tele</span><b>+</b><span class="tile"><i class="blank"></i></span></div>'),
 ]),
])
V['g3ela-25-1-teach-vocab'] = dict(title='Vocabulary', sub='Be a word detective', scenes=[
 dict(at=None, items=[
   (None, '<div class="lab">🔍 Word detective</div>'),
   ('Spiteful', '<div class="huge">spiteful</div>'),
 ]),
 dict(at="Here's the sentence", items=[
   (None, '<div class="quote">Edmund could be <b class="hl">spiteful</b>, and on this occasion he was spiteful. He sneered and jeered at Lucy.<small>Chapter 3</small></div>'),
 ]),
 dict(at='One, read the sentence', items=[
   (None, '<div class="steps"><span><i>1</i>Read</span><span><i>2</i>Word parts</span><span><i>3</i>Check</span></div>'),
   ('One, read the sentence', '<div class="say">1️⃣ mean to her on purpose 😠</div>'),
   ('Two, look for word parts', tiles(('spite', False), ('ful: full of', True))),
   ('Spiteful means', '<div class="def"><b>spiteful</b><span>full of meanness</span></div>'),
 ]),
 dict(at='Read how we figured', items=[
   (None, '<div class="say">✏️ Fill in each sentence from the word bank.</div>'),
   ('tap Check My Work', PILL('Check My Work')),
   ('Last, play the matching game', PILL('Matching game')),
 ]),
])
V['g3ela-25-1-teach-gram'] = dict(title='Grammar', sub='Complex sentences', scenes=[
 dict(at=None, items=[
   (None, '<div class="lab">Some sentences have two parts</div>'),
   ('One part can stand alone', '<div class="build"><span class="tile key">can stand alone ✅</span></div>'),
   ("The other part can't", '<div class="build"><span class="tile">can’t stand alone ❌</span></div>'),
 ]),
 dict(at='Listen.', items=[
   (None, '<div class="quote">When Lucy felt something crunching<i class="blank"></i></div>'),
   ('It can', '<div class="ask">🤔 …what happened?</div>'),
 ]),
 dict(at='Add the main idea', items=[
   (None, '<div class="quote q2">When Lucy felt something crunching<b class="hl">,</b> she stooped down to feel it.</div>'),
   ('put a comma after it', '<div class="say">part that can’t stand alone <b class="gold">,</b> main idea</div>'),
 ]),
 dict(at='Read The Rule box', items=[
   (None, '<div class="say">📌 Read The Rule box.</div>'),
   ('tap Now check your thinking', PILL('Now check your thinking')),
   ('Then find where each comma goes', '<div class="say">Where does each comma go? 🔍</div>'),
 ]),
])
V['g3ela-25-1-teach-spell'] = dict(title='Spelling', sub='The lazy schwa', scenes=[
 dict(at=None, items=[
   (None, '<div class="lab">🗣️ Say this name with me</div>'),
   ('Narnia.', '<div class="huge">Narnia</div>'),
   ('Nar, nee, uh', '<div class="say">Nar · nee · <b class="gold">uh</b></div>'),
 ]),
 dict(at='Hear that last beat', items=[
   (None, '<div class="say">quiet… lazy… 😴 <b>uh</b></div>'),
   ('That lazy sound', '<div class="def"><b>schwa</b><span>the lazy uh sound</span></div>'),
 ]),
 dict(at='Now try Edmund', items=[
   (None, '<div class="huge">Edmund</div>'),
   ('Ed, mund', '<div class="say">Ed · m<b class="gold">u</b>nd: the <b>u</b> says uh</div>'),
   ('Any vowel', '<div class="chips"><span>a</span><span>e</span><span>i</span><span>o</span><span>u</span></div>'),
 ]),
 dict(at='Say the eight words', items=[
   (None, '<div class="say">🗣️ Say the eight words in the sort.</div>'),
   ('tap Now name the pattern', PILL('Now name the pattern')),
   ('Then sort the words', '<div class="bins"><span>a says uh</span><span>e or o says uh</span></div>'),
 ]),
])
# ---------------- Days 2-4: show that day's activity ----------------
V['g3ela-25-2-teach-morph'] = dict(title='Morphology', sub='Match the word to its meaning', scenes=[
 dict(at=None, items=[
   (None, '<div class="lab">👀 Watch one match first</div>'),
   ('Find tele', '<div class="build"><span class="tile key">tele</span><b>=</b><span class="tile">far</span></div>'),
 ]),
 dict(at='Telework.', items=[
   (None, word('telework', 'tele')),
   ('Telework means', '<div class="build"><span class="tile">telework</span><b>➜</b><span class="tile m">working far from the office 🏠💻</span></div>'),
   ("That's my match", '<div class="say">✅ That’s my match!</div>'),
 ]),
 dict(at='Read the Remember box', items=[
   (None, '<div class="say">📌 Read the Remember box.</div>'),
   ('Then tap a word', '<div class="build"><span class="tile">👆 a word</span><b>➜</b><span class="tile m">👆 its meaning</span></div>'),
 ]),
])
V['g3ela-25-2-teach-vocab'] = dict(title='Vocabulary', sub='Match each word', scenes=[
 dict(at=None, items=[
   (None, '<div class="lab">Another word from Chapter 1</div>'),
   ('Glimpse.', '<div class="huge">glimpse</div>'),
 ]),
 dict(at='Lucy could even', items=[
   (None, '<div class="quote">…and even catch a <b class="hl">glimpse</b> of the empty room.<small>Chapter 1</small></div>'),
   ('Just a quick look', '<div class="say">👀 just a quick look, through the trees 🌲</div>'),
   ('So a glimpse is', '<div class="def"><b>glimpse</b><span>a quick look</span></div>'),
 ]),
 dict(at='Now tap a word', items=[
   (None, '<div class="build"><span class="tile">👆 a word</span><b>➜</b><span class="tile m">👆 its meaning</span></div>'),
   ('Match all four', '<div class="say">Match all four ✅✅✅✅</div>'),
 ]),
])
V['g3ela-25-2-teach-gram'] = dict(title='Grammar', sub='Find the connecting word', scenes=[
 dict(at=None, items=[
   (None, '<div class="lab">🔍 Spot the connecting word</div>'),
   ('Because it was raining', '<div class="quote q2"><span class="jw">Because</span> it was raining, the children explored the house.</div>'),
 ]),
 dict(at='Because!', items=[
   (None, '<div class="huge gold">because</div>'),
   ('It starts the part', '<div class="say">starts the part that can’t stand alone</div>'),
 ]),
 dict(at='Find the connecting word in each', items=[
   (None, '<div class="say">🔍 Find the connecting word in each sentence.</div>'),
   ('tap Now check your thinking', PILL('Now check your thinking')),
   ('Then fix the paragraph', '<div class="say">✏️ Fix the paragraph. Read slowly! 🐢</div>'),
 ]),
])
V['g3ela-25-2-teach-spell'] = dict(title='Spelling', sub='Find the schwa', scenes=[
 dict(at=None, items=[
   (None, '<div class="lab">🔍 Lazy beat hunt!</div>'),
   ('Susan pulled', '<div class="quote">Susan pulled the coats apart.<small>Chapter 3</small></div>'),
 ]),
 dict(at='Susan. Soo', items=[
   (None, '<div class="say">Soo · z<b class="gold">u</b>n</div>'),
   ('A lazy beat, yes', '<div class="say">Susan ✅</div>'),
   ('Pulled?', '<div class="say">pulled: one beat ❌</div>'),
   ('Apart.', '<div class="say"><b class="gold">uh</b> · part: apart ✅</div>'),
 ]),
 dict(at='Read the rule', items=[
   (None, '<div class="say">📌 Read the rule.</div>'),
   ('Then tap every word', '<div class="say">👆 Tap every word with a schwa.</div>'),
 ]),
])
V['g3ela-25-2-teach-rwm'] = dict(title='Read Like a Writer', sub='Reader, writer, mimic', scenes=[
 dict(at=None, items=[
   (None, '<div class="lab">A different sentence from Chapter 3</div>'),
   ('There was crisp', '<div class="quote">There was crisp, dry snow under his feet and more snow lying on the branches of the trees.<small>Chapter 3</small></div>'),
 ]),
 dict(at='Part one', items=[
   (None, '<div class="step1"><i>1</i>Read like a reader</div>'),
   ('Edmund is in Narnia', '<div class="say">Edmund is in Narnia now. ❄️ It’s winter.</div>'),
 ]),
 dict(at='Part two', items=[
   (None, '<div class="step1"><i>2</i>Read like a writer</div>'),
   ('Lewis starts at', '<div class="say">👣 his feet ➜ 🌲 the trees</div>'),
   ('so you look around', '<div class="say">You look around with him 👀</div>'),
 ]),
 dict(at='Part three', items=[
   (None, '<div class="step1"><i>3</i>Mimic</div>'),
   ("Here's mine", '<div class="quote mine">There was cold, wet sand under my feet and more sand stuck to my shoes.<small>Opti’s sentence</small></div>'),
 ]),
 dict(at="Now it's your turn", items=[
   (None, '<div class="say">Now you: Lewis’s sentence about the house 🏠</div>'),
   ('Write one sentence', '<div class="boxes"><span class="slot">Reader</span><span class="slot">Writer</span><span class="slot">Mimic</span></div>'),
 ]),
])
V['g3ela-25-3-teach-morph'] = dict(title='Morphology', sub='Build the word', scenes=[
 dict(at=None, items=[
   (None, '<div class="lab">🧱 Snap the parts together</div>'),
   ('Tele.', tiles(('tele', True))),
   ('Photo.', tiles(('tele', True), ('photo', False))),
   ('Telephoto!', '<div class="huge">telephoto</div>'),
 ]),
 dict(at='A telephoto lens', items=[
   (None, '<div class="def"><b>📷 telephoto</b><span>takes pictures of things far away</span></div>'),
 ]),
 dict(at='Say each pair', items=[
   (None, '<div class="say">🗣️ Say each pair of parts out loud.</div>'),
   ('Type the whole word', '<div class="build"><span class="tile">tele</span><b>+</b><span class="tile">…</span><b>=</b><span class="tile"><i class="blank"></i></span></div>'),
   ('Then tap Check My Answers', PILL('Check My Answers')),
 ]),
])
V['g3ela-25-3-teach-vocab'] = dict(title='Vocabulary', sub='Pick the word that fits', scenes=[
 dict(at=None, items=[
   (None, '<div class="say">Try each word in the blank. Keep the one that makes sense.</div>'),
 ]),
 dict(at="Here's my sentence", items=[
   (None, '<div class="quote">Lucy took a quick <i class="blank"></i> back at the wardrobe.</div>'),
   ('Spiteful? No', '<div class="say">spiteful? ❌</div>'),
   ('Glimpse? Yes', '<div class="say">glimpse? ✅</div>'),
   ('A glimpse is', '<div class="def"><b>glimpse</b><span>a quick look</span></div>'),
 ]),
 dict(at='Now pick the word', items=[
   (None, '<div class="say">👆 Pick the word that fits each sentence.</div>'),
 ]),
])
V['g3ela-25-3-teach-gram'] = dict(title='Grammar', sub='Join two sentences', scenes=[
 dict(at=None, items=[
   (None, '<div class="lab">Two short sentences can become one</div>'),
   ('The others did not', '<div class="quote">The others did not believe Lucy.</div>'),
   ('She was very unhappy', '<div class="quote">She was very unhappy.</div>'),
 ]),
 dict(at='Put a joining word', items=[
   (None, '<div class="say">Put a joining word in front ➜</div>'),
   ('Because the others', '<div class="quote q2"><span class="jw">Because</span> the others did not believe her<b class="hl">,</b> Lucy was very unhappy.</div>'),
 ]),
 dict(at='Read the before and after', items=[
   (None, '<div class="say">📖 Read the before and after.</div>'),
   ('Then join the two', '<div class="say">✏️ Join the two sentences in the box.</div>'),
 ]),
])
V['g3ela-25-3-teach-spell'] = dict(title='Spelling', sub='Which vowel blurred?', scenes=[
 dict(at=None, items=[
   (None, '<div class="ask">😬 Oops!</div>'),
   ('I spelled lion', '<div class="swap"><s>L I U N</s></div>'),
 ]),
 dict(at="That's how it sounds", items=[
   (None, '<div class="say">li · <b class="gold">uh</b>n</div>'),
   ('But that lazy uh', '<div class="swap"><s>liun</s> ➜ li<b>o</b>n</div>'),
   ('The schwa hides', '<div class="say">🙈 The schwa hides the real letter.</div>'),
 ]),
 dict(at='Read the rule', items=[
   (None, '<div class="say">📌 Read the rule.</div>'),
   ('Then tap each card', '<div class="say">👆 Tap each card: which vowel blurred?</div>'),
 ]),
])
V['g3ela-25-4-teach-morph'] = dict(title='Morphology', sub='Roll and explain', scenes=[
 dict(at=None, items=[
   (None, '<div class="ask">😌 Eyes closed for a second…</div>'),
   ('What does tele mean', '<div class="say">tele = ?</div>'),
   ('Far!', '<div class="build"><span class="tile key">tele</span><b>=</b><span class="tile">far</span></div>'),
 ]),
 dict(at="Here's a word", items=[
   (None, word('teleconference', 'tele')),
   ('A meeting with people', '<div class="def"><b>teleconference</b><span>a meeting with people far away, on a screen 💻</span></div>'),
 ]),
 dict(at='Now tap Roll the Dice', items=[
   (None, PILL('🎲 Roll the Dice')),
   ('Say what each word means', '<div class="say">🗣️ Say what the word means.</div>'),
   ('tap Check My Thinking', PILL('Check My Thinking')),
 ]),
])
V['g3ela-25-4-teach-vocab'] = dict(title='Vocabulary', sub='Use a word to tell the story', scenes=[
 dict(at=None, items=[
   (None, '<div class="ask">🤔 Can one word tell a whole moment?</div>'),
   ('Spiteful.', '<div class="huge">spiteful</div>'),
 ]),
 dict(at='Edmund was spiteful', items=[
   (None, '<div class="quote mine">Edmund was <b class="hl">spiteful</b> when he jeered at Lucy about countries in cupboards.<small>Opti’s sentence</small></div>'),
   ('One word, one moment', '<div class="say">1 word + 1 moment from the book 📖</div>'),
 ]),
 dict(at='Now choose one', items=[
   (None, '<div class="say">✏️ Choose one of your words. Write your own sentence.</div>'),
 ]),
])
V['g3ela-25-4-teach-gram'] = dict(title='Grammar', sub='Edit in passes', scenes=[
 dict(at=None, items=[
   (None, '<div class="lab">✏️ Editors read in passes</div>'),
   ('The queens sledge', '<div class="quote">the queens sledge had bells and edmund heard them</div>'),
 ]),
 dict(at='Pass one', items=[
   (None, '<div class="step1"><i>1</i>Capitals</div>'),
   ('The, Queen', '<div class="quote"><b class="hl">T</b>he <b class="hl">Q</b>ueens sledge had bells and <b class="hl">E</b>dmund heard them</div>'),
 ]),
 dict(at='Pass two', items=[
   (None, '<div class="step1"><i>2</i>Apostrophes</div>'),
   ("Queen's sledge", '<div class="quote">The Queen<b class="hl">’</b>s sledge had bells and Edmund heard them</div>'),
 ]),
 dict(at='Pass three', items=[
   (None, '<div class="step1"><i>3</i>Commas</div>'),
   ('one before and', '<div class="quote">The Queen’s sledge had bells<b class="hl">,</b> and Edmund heard them.</div>'),
 ]),
 dict(at='Now do your passes', items=[
   (None, '<div class="say">👆 Tap every word that needs fixing.</div>'),
 ]),
])
V['g3ela-25-4-teach-spell'] = dict(title='Spelling', sub='Schwa dice', scenes=[
 dict(at=None, items=[
   (None, '<div class="lab">🎲 Here’s my roll</div>'),
   ('Tumnus.', '<div class="huge">Tumnus</div>'),
   ('Tum, nus', '<div class="say">Tum · nus</div>'),
 ]),
 dict(at='Which beat is quiet', items=[
   (None, '<div class="say">Which beat is quiet and lazy? 😴</div>'),
   ('The second one', '<div class="say">Tum · <b class="gold">nus</b></div>'),
   ('The u!', '<div class="say">n<b class="gold">u</b>s: the <b>u</b> says uh</div>'),
 ]),
 dict(at='Tap Roll the dice', items=[
   (None, PILL('🎲 Roll the dice')),
   ('find the lazy beat', '<div class="say">🗣️ Say it. Find the lazy beat.</div>'),
   ('Then tap Check my answer', PILL('Check my answer')),
 ]),
])
