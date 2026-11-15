# Scene specs for the week 27 Opti teach films (LWW Ch. 7-9). SILENT for now (tone.py timing); captions carry the words.
# Never shows a page answer: examples are inactive, impolite, incomplete, immature, indirect; sternly, snug, gloating;
# catch/caught, drink/drank, keep/kept, make/made; replay, preview, rewind, unsafe, misbehave;
# and the Ch. 8 line "He is our brother after all, even if he is rather a little beast."
def word(w, part=None, cls=''):
    if part:
        i = w.index(part)
        return '<span class="wd %s">%s<b class="pt">%s</b>%s</span>' % (cls, w[:i], part, w[i+len(part):])
    return '<span class="wd %s">%s</span>' % (cls, w)
PILL = lambda t: '<span class="pill">👆 %s</span>' % t
def tiles(*ps): return '<div class="build">' + '<b>+</b>'.join('<span class="tile%s">%s</span>' % (' key' if k else '', t) for t, k in ps) + '</div>'
V = {}
V['g3ela-27-1-teach-morph'] = dict(title='Morphology', sub='Two word parts that mean not', scenes=[
 dict(at=None, items=[(None, '<div class="lab">Two little word parts, one big job</div>'),
   ('both mean not', '<div class="build"><span class="tile key">in</span><b>·</b><span class="tile key">im</span><b>=</b><span class="tile">not 🚫</span></div>')]),
 dict(at='Inactive means', items=[(None, '<div class="def"><b>' + word('inactive', 'in') + '</b><span>not active 😴</span></div>'),
   ('Impolite means', '<div class="def"><b>' + word('impolite', 'im') + '</b><span>not polite 😝</span></div>')]),
 dict(at="Here's the trick", items=[(None, '<div class="say"><b class="gold">im</b> comes before <b>m</b> or <b>p</b></div>'),
   ('like polite', '<div class="say">im + <b class="hl">p</b>olite ✅</div>')]),
 dict(at='Read the four words', items=[(None, '<div class="say">📖 Read the four words.</div>'), ('tap See if you were right', PILL('See if you were right')),
   ('Then type the base word', '<div class="build"><span class="tile"><i class="blank"></i></span><b>➜</b><span class="tile">base word hiding inside</span></div>')]),
])
V['g3ela-27-1-teach-vocab'] = dict(title='Vocabulary', sub='Be a word detective', scenes=[
 dict(at=None, items=[(None, '<div class="lab">🔍 Word detective</div>'), ('Sternly.', '<div class="huge">sternly</div>')]),
 dict(at="Here's the sentence", items=[(None, '<div class="quote">“Aslan a man!” said Mr. Beaver <b class="hl">sternly</b>.<small>Chapter 8</small></div>')]),
 dict(at='One, read the sentence', items=[(None, '<div class="steps"><span><i>1</i>Read</span><span><i>2</i>Word parts</span><span><i>3</i>Check</span></div>'),
   ('One, read', '<div class="say">1️⃣ serious, maybe a little cross 😠</div>'),
   ('Two, look for word parts', tiles(('stern', True), ('ly', False))),
   ('Sternly means', '<div class="def"><b>sternly</b><span>in a strict, serious way</span></div>')]),
 dict(at='Read how we figured', items=[(None, '<div class="say">✏️ Fill in each sentence from the word bank.</div>'),
   ('tap Check My Work', PILL('Check My Work')), ('Last, play the matching game', PILL('Matching game'))]),
])
V['g3ela-27-1-teach-gram'] = dict(title='Grammar', sub='Verbs that break the rule', scenes=[
 dict(at=None, items=[(None, '<div class="lab">Most verbs add -ed for the past</div>'),
   ('Walk, walked', '<div class="swap">walk ➜ <b>walked</b></div>')]),
 dict(at='But some verbs break the rule', items=[(None, '<div class="say">…but some verbs break the rule! 🚧</div>'),
   ('Mr. Beaver catched', '<div class="quote">Mr. Beaver <b class="hl">catched</b> a fish. 🐟</div>'),
   ("It's caught", '<div class="swap"><s>catched</s> ➜ <b>caught</b></div>')]),
 dict(at='Verbs like that', items=[(None, '<div class="def"><b>irregular verb</b><span>no -ed for the past. You learn each one.</span></div>')]),
 dict(at='Read The Rule box', items=[(None, '<div class="say">📌 Read The Rule box.</div>'), ('tap Now check your thinking', PILL('Now check your thinking')),
   ('Then find the four verbs', '<div class="say">🔍 Find the four verbs that should not end in -ed.</div>')]),
])
V['g3ela-27-1-teach-spell'] = dict(title='Spelling', sub='Peel off the prefix', scenes=[
 dict(at=None, items=[(None, '<div class="lab">A short word with an extra part on the front</div>'), ('Replay.', '<div class="huge">replay</div>')]),
 dict(at='Cover the front part', items=[(None, '<div class="build"><span class="tile m">re</span><b>+</b><span class="tile key">play</span></div>'),
   ("What's left? Play", '<div class="say">play ✅ a real word!</div>'),
   ('That front part means again', '<div class="def"><b>replay</b><span>play again 🔁</span></div>')]),
 dict(at='Peel off the front', items=[(None, '<div class="say">Peel off ➜ read the base ➜ put it back</div>')]),
 dict(at='Tap Now name the pattern', items=[(None, PILL('Now name the pattern')),
   ('Then sort the words', '<div class="bins"><span>Prefix + base word</span><span>Base word only</span></div>')]),
])
V['g3ela-27-2-teach-morph'] = dict(title='Morphology', sub='Match the word to its meaning', scenes=[
 dict(at=None, items=[(None, '<div class="lab">👀 Watch one match first</div>'), ('Incomplete.', word('incomplete', 'in'))]),
 dict(at='Find the word part', items=[(None, tiles(('in: not', True), ('complete', False))),
   ('So incomplete means', '<div class="build"><span class="tile">incomplete</span><b>➜</b><span class="tile m">not complete 🧩</span></div>'),
   ("That's my match", '<div class="say">✅ That’s my match!</div>')]),
 dict(at='Read the Remember box', items=[(None, '<div class="say">📌 Read the Remember box.</div>'),
   ('Then tap a word', '<div class="build"><span class="tile">👆 a word</span><b>➜</b><span class="tile m">👆 its meaning</span></div>')]),
])
V['g3ela-27-2-teach-vocab'] = dict(title='Vocabulary', sub='Match each word', scenes=[
 dict(at=None, items=[(None, '<div class="lab">A cozy word from Chapter 7</div>'), ('Snug.', '<div class="huge">snug</div>')]),
 dict(at='Lucy thinks', items=[(None, '<div class="quote">Lucy thought the Beavers had a very <b class="hl">snug</b> little home.<small>Chapter 7</small></div>'),
   ('Warm, cozy and safe', '<div class="say">warm 🔥 cozy 🛏️ safe 🏠</div>')]),
 dict(at='Now tap a word', items=[(None, '<div class="build"><span class="tile">👆 a word</span><b>➜</b><span class="tile m">👆 its meaning</span></div>'),
   ('Match all four', '<div class="say">Match all four ✅✅✅✅</div>')]),
])
V['g3ela-27-2-teach-gram'] = dict(title='Grammar', sub='Spot the wrong verb', scenes=[
 dict(at=None, items=[(None, '<div class="ask">🔍 Spot the wrong verb</div>'),
   ('The children drinked', '<div class="quote">The children <b class="hl">drinked</b> hot tea. ☕</div>')]),
 dict(at="That's not a word", items=[(None, '<div class="say">drinked? 🙅 not a word!</div>'), ('The past of drink', '<div class="swap"><s>drinked</s> ➜ <b>drank</b></div>'),
   ('The children drank', '<div class="quote">The children <b class="hl">drank</b> hot tea.</div>')]),
 dict(at='Check the verb', items=[(None, '<div class="say">🔍 Check the verb in each sentence.</div>'),
   ('tap Now check your thinking', PILL('Now check your thinking')), ('Then fix the paragraph', '<div class="say">✏️ Then fix the paragraph.</div>')]),
])
V['g3ela-27-2-teach-spell'] = dict(title='Spelling', sub='Prefix hunt', scenes=[
 dict(at=None, items=[(None, '<div class="lab">🔎 Prefix hunt!</div>'),
   ("Here's my sentence", '<div class="quote mine">Mom will preview the movie, then rewind the best part.<small>Opti’s sentence</small></div>')]),
 dict(at='Preview. Pre', items=[(None, '<div class="quote mine">Mom will <b class="hl">preview</b> the movie, then <b class="hl">rewind</b> the best part.</div>'),
   ('Pre, plus view', tiles(('pre', False), ('view', True))), ('Re, plus wind', tiles(('re', False), ('wind', True))),
   ('Two prefix words', '<div class="say">✅ Two prefix words!</div>')]),
 dict(at='Read the rule', items=[(None, '<div class="say">📌 Read the rule.</div>'), ('Then tap every word', '<div class="say">👆 Tap every prefix + base word.</div>')]),
])
V['g3ela-27-2-teach-rwm'] = dict(title='Read Like a Writer', sub='Reader, writer, mimic', scenes=[
 dict(at=None, items=[(None, '<div class="lab">A different sentence from Chapter 8</div>'),
   ('He is our brother', '<div class="quote">He is our brother <b class="hl">after all</b>, <b class="hl">even if</b> he is rather a little beast.<small>Peter, Chapter 8</small></div>')]),
 dict(at='Part one', items=[(None, '<div class="step1"><i>1</i>Read like a reader</div>'), ('Peter is cross', '<div class="say">Peter is cross 😤 … but he still wants to find Edmund 💛</div>')]),
 dict(at='Part two', items=[(None, '<div class="step1"><i>2</i>Read like a writer</div>'), ('After all, and even if', '<div class="say"><b class="gold">after all</b> + <b class="gold">even if</b> = two feelings in one sentence</div>')]),
 dict(at='Part three', items=[(None, '<div class="step1"><i>3</i>Mimic</div>'),
   ("Here's mine", '<div class="quote mine">She is my best friend <b class="hl">after all</b>, <b class="hl">even if</b> she eats the last cookie.<small>Opti’s sentence</small></div>')]),
 dict(at="Now it's your turn", items=[(None, '<div class="say">Now you: the sentence about the whiskered face 🦫</div>'),
   ('Write one sentence', '<div class="boxes"><span class="slot">Reader</span><span class="slot">Writer</span><span class="slot">Mimic</span></div>')]),
])
V['g3ela-27-3-teach-morph'] = dict(title='Morphology', sub='Build the word', scenes=[
 dict(at=None, items=[(None, '<div class="lab">🧱 Snap the parts together</div>'), ('Im.', tiles(('im', True))), ('Mature.', tiles(('im', True), ('mature', False))), ('Immature!', '<div class="huge">immature</div>')]),
 dict(at='Immature means', items=[(None, '<div class="def"><b>immature</b><span>not grown up yet 🐶👟</span></div>')]),
 dict(at='Say each pair', items=[(None, '<div class="say">🗣️ Say each pair of parts out loud.</div>'),
   ('Type the whole word', '<div class="build"><span class="tile">in</span><b>+</b><span class="tile">?</span><b>=</b><span class="tile"><i class="blank"></i></span></div>'),
   ('Then tap Check My Answers', PILL('Check My Answers'))]),
])
V['g3ela-27-3-teach-vocab'] = dict(title='Vocabulary', sub='Pick the word that fits', scenes=[
 dict(at=None, items=[(None, '<div class="say">Try each word in the blank. Keep the one that makes sense.</div>')]),
 dict(at="Here's my sentence", items=[(None, '<div class="quote">The children ate dinner in the Beavers’ <i class="blank"></i> little house.</div>'),
   ('Treachery?', '<div class="say">treachery? 🤔 no</div>'), ('Snug? Yes', '<div class="say">snug? ✅</div>')]),
 dict(at='Now pick the word', items=[(None, '<div class="say">👆 Pick the word that fits each sentence.</div>')]),
])
V['g3ela-27-3-teach-gram'] = dict(title='Grammar', sub='Fix it like the editor', scenes=[
 dict(at=None, items=[(None, '<div class="lab">✏️ Fix it the way the editor did</div>'),
   ('Mr. Beaver keeped', '<div class="quote">Mr. Beaver <b class="hl">keeped</b> a hole open in the ice.</div>')]),
 dict(at='The past of keep', items=[(None, '<div class="swap"><s>keeped</s> ➜ <b>kept</b></div>'),
   ('Mr. Beaver kept', '<div class="quote">Mr. Beaver <b class="hl">kept</b> a hole open in the ice. 🧊</div>')]),
 dict(at='Read the before and after', items=[(None, '<div class="say">📖 Read the before and after.</div>'), ('tap Check yourself', PILL('Check yourself')),
   ('Then fix the sentence', '<div class="say">✏️ Fix the sentence. List 3 more verbs like these.</div>')]),
])
V['g3ela-27-3-teach-spell'] = dict(title='Spelling', sub='Proofreader', scenes=[
 dict(at=None, items=[(None, '<div class="lab">🔎 Proofreader time!</div>'), ('Unsaif.', '<div class="huge"><s>unsaif</s></div>')]),
 dict(at='Peel off the front part', items=[(None, tiles(('un', False), ('saif ❓', True))), ("should be safe", '<div class="say">s · a · f · e</div>'),
   ('so it', '<div class="huge">unsafe ✅</div>')]),
 dict(at='Read the rule', items=[(None, '<div class="say">📌 Read the rule.</div>'), ('Then tap the words', '<div class="say">👆 Tap the words you think are spelled wrong.</div>')]),
])
V['g3ela-27-4-teach-morph'] = dict(title='Morphology', sub='Roll and explain', scenes=[
 dict(at=None, items=[(None, '<div class="ask">⚡ Quick! What do these two word parts mean?</div>'), ('Not!', '<div class="build"><span class="tile key">in</span><b>·</b><span class="tile key">im</span><b>=</b><span class="tile">not</span></div>')]),
 dict(at="Here's a word", items=[(None, word('indirect', 'in')), ('A path that', '<div class="def"><b>indirect</b><span>not direct: it winds around 〰️</span></div>')]),
 dict(at='Now tap Roll the Dice', items=[(None, PILL('🎲 Roll the Dice')), ('Say what each word means', '<div class="say">🗣️ Say what the word means.</div>'), ('tap Check My Thinking', PILL('Check My Thinking'))]),
])
V['g3ela-27-4-teach-vocab'] = dict(title='Vocabulary', sub='Use a word to tell the story', scenes=[
 dict(at=None, items=[(None, '<div class="lab">✍️ Here’s how I’d use a word</div>'), ('Gloating.', '<div class="huge">gloating</div>')]),
 dict(at='Edmund stood gloating', items=[(None, '<div class="quote mine">Edmund stood <b class="hl">gloating</b> over the stone lion, because he thought the Witch had won.<small>Opti’s sentence</small></div>'),
   ('One word, one moment', '<div class="say">1 word + 1 moment 📖</div>')]),
 dict(at='Now choose one', items=[(None, '<div class="say">✏️ Choose one of your words. Write a sentence about Chapters 7 to 9.</div>')]),
])
V['g3ela-27-4-teach-gram'] = dict(title='Grammar', sub='Three passes', scenes=[
 dict(at=None, items=[(None, '<div class="lab">✏️ Three passes, like an editor</div>'), ('mrs beaver maked', '<div class="quote">mrs beaver maked a marmalade roll and they ate it all</div>')]),
 dict(at='Pass one', items=[(None, '<div class="step1"><i>1</i>Capitals</div>'), ('Mrs. and Beaver', '<div class="quote"><b class="hl">M</b>rs. <b class="hl">B</b>eaver maked a marmalade roll and they ate it all</div>')]),
 dict(at='Pass two', items=[(None, '<div class="step1"><i>2</i>Verbs</div>'), ('maked becomes made', '<div class="swap"><s>maked</s> ➜ <b>made</b></div>')]),
 dict(at='Pass three', items=[(None, '<div class="step1"><i>3</i>Commas</div>'), ('a comma before and', '<div class="quote">Mrs. Beaver made a marmalade roll<b class="hl">,</b> and they ate it all.</div>')]),
 dict(at='Now do your passes', items=[(None, '<div class="say">👆 Tap every word that needs fixing.</div>')]),
])
V['g3ela-27-4-teach-spell'] = dict(title='Spelling', sub='Prefix dice', scenes=[
 dict(at=None, items=[(None, '<div class="lab">🎲 Here’s my roll</div>'), ('Misbehave.', '<div class="huge">misbehave</div>')]),
 dict(at='Peel off the front part', items=[(None, tiles(('mis', False), ('behave', True))), ('The front part means badly', '<div class="def"><b>misbehave</b><span>behave badly 🙈</span></div>')]),
 dict(at='Tap Roll the dice', items=[(None, PILL('🎲 Roll the dice')), ('name the prefix', '<div class="say">🗣️ Name the prefix and the base word.</div>'), ('Check my answer', PILL('Check my answer'))]),
])
