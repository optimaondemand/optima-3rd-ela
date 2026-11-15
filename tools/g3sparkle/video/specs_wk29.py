def word(w, part=None, cls=''):
    if part:
        i = w.index(part)
        return '<span class="wd %s">%s<b class="pt">%s</b>%s</span>' % (cls, w[:i], part, w[i+len(part):])
    return '<span class="wd %s">%s</span>' % (cls, w)
PILL = lambda t: '<span class="pill">👆 %s</span>' % t
def tiles(*ps): return '<div class="build">' + '<b>+</b>'.join('<span class="tile%s">%s</span>' % (' key' if k else '', t) for t, k in ps) + '</div>'
TAPMEAN = '<div class="build"><span class="tile">👆 a word</span><b>➜</b><span class="tile m">👆 its meaning</span></div>'
# Scene specs for the week 29 Opti teach films (LWW Ch. 13-15). SILENT for now (tone.py timing); captions carry the words.
# Never shows a page answer or a game item: examples are projectile, interject, object, trajectory; earnestly (Ch. 13),
# stern (Ch. 14), Opti's cup sentence, Edmund the traitor (Opti's sentence); We're home / come here / where are my boots /
# its snowing; unbreakable, unlocked, replanted, uncovered; and part of a Ch. 14 sentence (kissed his mane and his nose ...).
V = {}
V['g3ela-29-1-teach-morph'] = dict(title='Morphology', sub='A word part that means throw', scenes=[
 dict(at=None, items=[(None, '<div class="lab">🎯 A throw is hiding inside this word</div>'), ('Projectile.', '<div class="huge">projectile</div>')]),
 dict(at='Pro means forward', items=[(None, tiles(('pro: forward', False), ('ject: throw', True), ('ile', False))),
   ('A projectile is', '<div class="def"><b>projectile</b><span>something thrown forward, like a snowball ❄️➡️</span></div>')]),
 dict(at='Read the four words', items=[(None, '<div class="say">📖 Read the four words and their parts.</div>'), ('tap See if you were right', PILL('See if you were right')),
   ('Then type the missing part', '<div class="build"><span class="tile">re</span><b>+</b><span class="tile"><i class="blank"></i></span></div>')]),
])
V['g3ela-29-1-teach-vocab'] = dict(title='Vocabulary', sub='Be a word detective', scenes=[
 dict(at=None, items=[(None, '<div class="lab">🔍 Word detective</div>'), ('Earnestly.', '<div class="huge">earnestly</div>')]),
 dict(at="Here's the sentence", items=[(None, '<div class="quote">… the Lion and the Witch talked <b class="hl">earnestly</b> together in low voices.<small>Chapter 13</small></div>')]),
 dict(at='One, read the sentence', items=[(None, '<div class="steps"><span><i>1</i>Read</span><span><i>2</i>Word parts</span><span><i>3</i>Check</span></div>'),
   ('everyone is waiting', '<div class="say">1️⃣ Everyone is waiting, and worried 😟</div>'),
   ('Two, look for word parts', tiles(('earnest', True), ('ly', False))),
   ('Earnestly means', '<div class="def"><b>earnestly</b><span>in a very serious way 🙂‍↕️</span></div>')]),
 dict(at='Read how we figured', items=[(None, '<div class="say">✏️ Fill in each sentence from the word bank.</div>'),
   ('tap Check My Work', PILL('Check My Work')), ('Last, play the matching game', PILL('Matching game'))]),
])
V['g3ela-29-1-teach-gram'] = dict(title='Grammar', sub='Where the marks go when someone speaks', scenes=[
 dict(at=None, items=[(None, '<div class="lab">💬 Spoken words get a little house</div>'), ("We're home, said Mom", '<div class="quote"><b class="hl">“</b>We’re home<b class="hl">,”</b> said Mom.</div>')]),
 dict(at='Quotation marks go around', items=[(None, '<div class="say">“ ” go around the words Mom says 🏠</div>'),
   ("We're gets a capital", '<div class="say"><b class="gold">W</b>e’re starts with a capital</div>'),
   ('The comma goes inside', '<div class="say">the comma goes <b class="gold">inside</b>: home<b class="gold">,”</b></div>')]),
 dict(at='Tap Now check your thinking', items=[(None, PILL('Now check your thinking')), ('Then find the three', '<div class="say">🔍 Find the three dialogue mistakes.</div>')]),
])
V['g3ela-29-1-teach-spell'] = dict(title='Spelling', sub='Long words come apart', scenes=[
 dict(at=None, items=[(None, '<div class="lab">🧩 Big words come apart!</div>'), ('Unbreakable.', '<div class="huge">unbreakable</div>')]),
 dict(at='Find the root first', items=[(None, tiles(('break', True))), ('The front part is un', tiles(('un', False), ('break', True))),
   ('The end part is able', tiles(('un', False), ('break', True), ('able', False)))]),
 dict(at='Think about the questions', items=[(None, PILL('Now name the pattern')),
   ('Then sort the words', '<div class="bins"><span>ject (throw)</span><span>script, scribe (write)</span></div>')]),
])
V['g3ela-29-2-teach-morph'] = dict(title='Morphology', sub='Match the word to its meaning', scenes=[
 dict(at=None, items=[(None, '<div class="lab">👀 Watch one match first</div>'), ('Interject.', word('interject', 'ject'))]),
 dict(at='Inter means between', items=[(None, tiles(('inter: between', False), ('ject: throw', True))),
   ('To interject is', '<div class="build"><span class="tile">interject</span><b>➜</b><span class="tile m">throw your words in while someone talks 🗣️</span></div>'),
   ("That's my match", '<div class="say">✅ That’s my match!</div>')]),
 dict(at='Read the Remember box', items=[(None, '<div class="say">📌 Read the Remember box.</div>'), ('Then tap a word', TAPMEAN)]),
])
V['g3ela-29-2-teach-vocab'] = dict(title='Vocabulary', sub='Match each word', scenes=[
 dict(at=None, items=[(None, '<div class="ask">Ever seen a face so serious that nobody dared to ask a question? 😶</div>'), ('Stern.', '<div class="huge">stern</div>')]),
 dict(at="Aslan's face was stern", items=[(None, '<div class="quote">… his face was <b class="hl">stern</b> …<small>Chapter 14</small></div>'),
   ('Stern means', '<div class="def"><b>stern</b><span>very serious, and a little strict</span></div>')]),
 dict(at='Now tap a word', items=[(None, TAPMEAN), ('Match all three', '<div class="say">Match all three ✅✅✅</div>')]),
])
V['g3ela-29-2-teach-gram'] = dict(title='Grammar', sub='Find the mistake', scenes=[
 dict(at=None, items=[(None, '<div class="ask">🔍 Find the two mistakes</div>'), ('come here. said Dad', '<div class="quote">“<b class="hl">c</b>ome here<b class="hl">.</b>” said Dad.</div>')]),
 dict(at='Come needs a capital', items=[(None, '<div class="swap">come ➜ <b>Come</b> (starts the spoken words)</div>'),
   ('And that period', '<div class="swap">here. ➜ <b>here,”</b> (comma inside)</div>')]),
 dict(at='Read the four sentences', items=[(None, PILL('Now check your thinking')), ('Then fix the paragraph', '<div class="say">✏️ Then fix the paragraph.</div>')]),
])
V['g3ela-29-2-teach-spell'] = dict(title='Spelling', sub='Root hunt', scenes=[
 dict(at=None, items=[(None, '<div class="lab">🔎 Root hunt!</div>'), ('Lucy unlocked the door', '<div class="quote mine">Lucy <b class="hl">unlocked</b> the door. 🚪<small>Opti’s sentence</small></div>')]),
 dict(at='Unlocked: un', items=[(None, tiles(('un', False), ('lock', True), ('ed', False))), ('Lock is the root', '<div class="say">lock = the root, parts on both ends</div>'),
   ('That one gets a tap', '<div class="say">👆 That one gets a tap!</div>')]),
 dict(at='Read the rule', items=[(None, '<div class="say">📌 Read the rule.</div>'), ('Then tap every word', '<div class="say">👆 Tap every word built from a root with parts added.</div>')]),
])
V['g3ela-29-2-teach-rwm'] = dict(title='Read Like a Writer', sub='Reader, writer, mimic', scenes=[
 dict(at=None, items=[(None, '<div class="lab">Part of a sentence from Chapter 14</div>'),
   ('They kissed his mane', '<div class="quote">… kissed his mane <b class="hl">and</b> his nose <b class="hl">and</b> his paws <b class="hl">and</b> his great, sad eyes.<small>Chapter 14</small></div>')]),
 dict(at='Part one', items=[(None, '<div class="step1"><i>1</i>Read like a reader</div>'), ('Lucy and Susan love Aslan', '<div class="say">Lucy and Susan love Aslan. They are saying goodbye. 💛</div>')]),
 dict(at='Part two', items=[(None, '<div class="step1"><i>2</i>Read like a writer</div>'), ("It's a list joined by and", '<div class="say">a list joined by <b class="gold">and</b></div>'),
   ('The last one', '<div class="say">mane · nose · paws · <b class="gold">his great, sad eyes</b> ⬅️ longest</div>')]),
 dict(at='Part three', items=[(None, '<div class="step1"><i>3</i>Mimic</div>'),
   ("Here's mine", '<div class="quote mine">I hugged my dog’s ears <b class="hl">and</b> his nose <b class="hl">and</b> his paws <b class="hl">and</b> his warm, sleepy head.<small>Opti’s sentence</small></div>')]),
 dict(at="Now it's your turn", items=[(None, '<div class="say">Now you: the Witch’s list of names 📜</div>'),
   ('Write one sentence', '<div class="boxes"><span class="slot">Reader</span><span class="slot">Writer</span><span class="slot">Mimic</span></div>')]),
])
V['g3ela-29-3-teach-morph'] = dict(title='Morphology', sub='Build the word', scenes=[
 dict(at=None, items=[(None, '<div class="lab">🧱 Snap the parts together</div>'), ('Ob.', tiles(('ob', False))), ('Ject.', tiles(('ob', False), ('ject', True))), ('Object!', '<div class="huge">object</div>')]),
 dict(at='When you object', items=[(None, '<div class="def"><b>object</b><span>to throw a “no” against an idea ✋</span></div>')]),
 dict(at='Say each pair', items=[(None, '<div class="say">🗣️ Say each pair of parts out loud.</div>'),
   ('Type the whole word', '<div class="build"><span class="tile">?</span><b>+</b><span class="tile">ject</span><b>=</b><span class="tile"><i class="blank"></i></span></div>'),
   ('Then tap Check My Answers', PILL('Check My Answers'))]),
])
V['g3ela-29-3-teach-vocab'] = dict(title='Vocabulary', sub='Pick the word that fits', scenes=[
 dict(at=None, items=[(None, '<div class="say">Try each word in the blank. Keep the one that makes sense.</div>')]),
 dict(at="Here's my sentence", items=[(None, '<div class="quote mine">My brother broke my cup, so he cleaned up the mess to <i class="blank"></i>.<small>Opti’s sentence</small></div>'),
   ('Traitor?', '<div class="say">traitor? 🤔 no</div>'), ('Atone? Yes', '<div class="say">atone? ✅</div>')]),
 dict(at='Now pick the word', items=[(None, '<div class="say">👆 Pick the word that fits each sentence.</div>')]),
])
V['g3ela-29-3-teach-gram'] = dict(title='Grammar', sub='Be the editor', scenes=[
 dict(at=None, items=[(None, '<div class="lab">✏️ Be the editor</div>'), ('where are my boots', '<div class="quote">“<b class="hl">w</b>here are my boots<b class="hl">,</b>” asked Peter.</div>')]),
 dict(at='Where needs a capital', items=[(None, '<div class="swap">where ➜ <b>Where</b></div>'), ("It's a question", '<div class="swap">boots, ➜ <b>boots?”</b> 🥾</div>')]),
 dict(at='Read the before and after', items=[(None, '<div class="say">📖 Read the before and after.</div>'), ('tap Check yourself', PILL('Check yourself')),
   ('Then fix the line', '<div class="say">✏️ Fix the line in the gray box.</div>')]),
])
V['g3ela-29-3-teach-spell'] = dict(title='Spelling', sub='Spell it from the root', scenes=[
 dict(at=None, items=[(None, '<div class="lab">🌱 Spell one from the root</div>'), ('Replanted.', '<div class="huge">replanted</div>')]),
 dict(at='The root is plant', items=[(None, tiles(('plant', True))), ('Re goes on the front', tiles(('re', False), ('plant', True))),
   ('e d goes on the end', tiles(('re', False), ('plant', True), ('ed', False)))]),
 dict(at='Read the rule', items=[(None, '<div class="say">👀 Look ➜ ✋ cover ➜ ✏️ write</div>'), ('Then tap the card', PILL('Tap the card to check'))]),
])
V['g3ela-29-4-teach-morph'] = dict(title='Morphology', sub='Roll and explain', scenes=[
 dict(at=None, items=[(None, '<div class="ask">⚡ Quick question: what does ject mean?</div>'), ('Throw!', '<div class="build"><span class="tile key">ject</span><b>=</b><span class="tile">throw 🎯</span></div>')]),
 dict(at="Here's a word", items=[(None, word('trajectory', 'ject')), ("It's the path", '<div class="def"><b>trajectory</b><span>the path something takes when you throw it ⚾〰️</span></div>')]),
 dict(at='Say what the word part means', items=[(None, PILL('🎲 Roll the Dice')), ('Say what the word means', '<div class="say">🗣️ Say what the word means.</div>'), ('tap Check My Thinking', PILL('Check My Thinking'))]),
])
V['g3ela-29-4-teach-vocab'] = dict(title='Vocabulary', sub='Use a word to tell a big idea', scenes=[
 dict(at=None, items=[(None, '<div class="lab">✍️ One word can carry a big idea</div>'), ('Traitor.', '<div class="huge">traitor</div>')]),
 dict(at='At first, Edmund', items=[(None, '<div class="quote mine">At first, Edmund acts like a <b class="hl">traitor</b>, but in Chapter 13 his family forgives him.<small>Opti’s sentence</small></div>'),
   ('One word, one big idea', '<div class="say">1 word + 1 big idea 💡</div>')]),
 dict(at='Now choose your word', items=[(None, '<div class="say">✏️ Choose your word. Write a sentence about the theme.</div>')]),
])
V['g3ela-29-4-teach-gram'] = dict(title='Grammar', sub='Two passes', scenes=[
 dict(at=None, items=[(None, '<div class="lab">✏️ Two passes, like an editor</div>'), ('its snowing, said peter', '<div class="quote">“its snowing,” said peter.</div>')]),
 dict(at='Pass one', items=[(None, '<div class="step1"><i>1</i>Capitals</div>'), ("It's and Peter", '<div class="quote">“<b class="hl">I</b>ts snowing,” said <b class="hl">P</b>eter.</div>')]),
 dict(at='Pass two', items=[(None, '<div class="step1"><i>2</i>Apostrophes</div>'), ("it's means it is", '<div class="quote">“It<b class="hl">’</b>s snowing,” said Peter. ❄️</div>'),
   ('The comma is already inside', '<div class="say">the comma is already inside ✅</div>')]),
 dict(at='Now do your passes', items=[(None, '<div class="say">👆 Tap every word that needs fixing.</div>')]),
])
V['g3ela-29-4-teach-spell'] = dict(title='Spelling', sub='Root and affix dice', scenes=[
 dict(at=None, items=[(None, '<div class="lab">🎲 Dice roll: uncovered!</div>')]),
 dict(at='Cover the front and the end', items=[(None, '<div class="swap"><s>un</s> cover <s>ed</s></div>'), ("That's the root", tiles(('un', False), ('cover', True), ('ed', False)))]),
 dict(at='Tap Roll the dice', items=[(None, PILL('🎲 Roll the dice')), ('say the root and the parts', '<div class="say">🗣️ Say the root and the parts.</div>'), ('Check my answer', PILL('Check my answer'))]),
])
