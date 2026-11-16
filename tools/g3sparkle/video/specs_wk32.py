def word(w, part=None, cls=''):
    if part:
        i = w.index(part)
        return '<span class="wd %s">%s<b class="pt">%s</b>%s</span>' % (cls, w[:i], part, w[i+len(part):])
    return '<span class="wd %s">%s</span>' % (cls, w)
PILL = lambda t: '<span class="pill">👆 %s</span>' % t
def tiles(*ps): return '<div class="build">' + '<b>+</b>'.join('<span class="tile%s">%s</span>' % (' key' if k else '', t) for t, k in ps) + '</div>'
TAPMEAN = '<div class="build"><span class="tile">👆 a word</span><b>➜</b><span class="tile m">👆 its meaning</span></div>'
# Scene specs for the week 32 Opti teach films (Year-End Culmination: The 7 Pillars of Virtue). SILENT for now (tone.py timing);
# captions carry the words. Never shows a page answer or a game item: kindness, joyous, generous (Maya), "maya and leo goed to
# the library on monday", unhappy/thankful; thoughtful, fair, When the bell rang / I read and my sister drew, raking, and the
# real "Nothing." line from The Tale of Despereaux (not the page's Mrs. Lambchop sentence); sadness, courtesy (Mia),
# "my dogs bowl", puddel; restart, loyalty (Arthur), "my sisters cat", hiking. No two films open the same way.
V = {}
V['g3ela-32-1-teach-morph'] = dict(title='Morphology', sub='Word parts from the whole year', scenes=[
 dict(at=None, items=[(None, '<div class="ask">Every word part this year was a tool 🧰</div>')]),
 dict(at='Kindness.', items=[(None, word('kindness', 'ness')), ('Kind, plus ness', tiles(('kind', False), ('ness: being', True))),
   ('being kind', '<div class="def"><b>kindness</b><span>being kind 💛</span></div>')]),
 dict(at='Joyous.', items=[(None, word('joyous', 'ous')), ('Joy, plus ous', tiles(('joy', False), ('ous: full of', True))),
   ('full of joy', '<div class="def"><b>joyous</b><span>full of joy 🎉</span></div>')]),
 dict(at='Find the base word first', items=[(None, '<div class="say">1️⃣ Find the base word. 2️⃣ Then the part.</div>'),
   ('tap See if you were right', PILL('See if you were right')),
   ('then type the missing part', '<div class="build"><span class="tile">kind</span><b>+</b><span class="tile"><i class="blank"></i></span></div>')]),
])
V['g3ela-32-1-teach-vocab'] = dict(title='Vocabulary', sub='Be a word detective', scenes=[
 dict(at=None, items=[(None, '<div class="lab">🔍 Word detective</div>'), ('Generous.', '<div class="huge">generous</div>')]),
 dict(at="Here's my sentence", items=[(None, '<div class="quote">Maya gave half her lunch to a new friend; she was <b class="hl">generous</b>. 🥪<small>Opti’s sentence</small></div>')]),
 dict(at='One, read the sentence', items=[(None, '<div class="steps"><span><i>1</i>Read</span><span><i>2</i>Word parts</span><span><i>3</i>Check</span></div>'),
   ('she shared', '<div class="say">1️⃣ She shared.</div>'),
   ('Two, look for word parts', '<div class="say">2️⃣ gener<b class="hl">ous</b>: ous means full of</div>'),
   ('Generous means', '<div class="def"><b>generous</b><span>happy to give and share 🤲</span></div>')]),
 dict(at='Now fill in each sentence', items=[(None, '<div class="say">✏️ Fill in each sentence from the word bank.</div>'), ('play the matching game', PILL('Matching game'))]),
])
V['g3ela-32-1-teach-gram'] = dict(title='Grammar', sub='Mistakes from the whole year', scenes=[
 dict(at=None, items=[(None, '<div class="lab">✏️ One sentence, four fixes</div>'), ('maya and leo', '<div class="quote">maya and leo goed to the library on monday</div>')]),
 dict(at='Maya and Leo are names', items=[(None, '<div class="swap">maya, leo ➜ <b>Maya</b>, <b>Leo</b> (names)</div>'),
   ('Monday is a day', '<div class="swap">monday ➜ <b>Monday</b> (a day)</div>'),
   ('And goed should be went', '<div class="swap">goed ➜ <b>went</b> 🗣️</div>')]),
 dict(at='Read The Rule box', items=[(None, PILL('Now check your thinking')), ('Then tap all seven words', '<div class="say">👆 Tap all seven words that need fixing.</div>')]),
])
V['g3ela-32-1-teach-spell'] = dict(title='Spelling', sub='Prefix or suffix?', scenes=[
 dict(at=None, items=[(None, '<div class="ask">Front or back? ⬅️➡️</div>')]),
 dict(at='Unhappy:', items=[(None, '<div class="swap"><b class="hl">un</b>happy ➜ prefix at the front</div>'),
   ('Thankful:', '<div class="swap">thank<b class="hl">ful</b> ➜ suffix at the end</div>')]),
 dict(at='Think about the questions', items=[(None, PILL('Now name the pattern')),
   ('Then sort the words', '<div class="bins"><span>Prefix at the front</span><span>Suffix at the end</span></div>')]),
])
V['g3ela-32-2-teach-morph'] = dict(title='Morphology', sub='Match the word to its meaning', scenes=[
 dict(at=None, items=[(None, '<div class="lab">👀 Watch one match first</div>'), ('Thoughtful.', word('thoughtful', 'ful'))]),
 dict(at='Find the ending', items=[(None, tiles(('thought', False), ('ful: full of', True))),
   ('So thoughtful means', '<div class="build"><span class="tile">thoughtful</span><b>➜</b><span class="tile m">full of kind thoughts 💭</span></div>'),
   ("That's my match", '<div class="say">✅ That’s my match!</div>')]),
 dict(at='Read the Remember box', items=[(None, '<div class="say">📌 Read the Remember box.</div>'), ('Then tap a word', TAPMEAN)]),
])
V['g3ela-32-2-teach-vocab'] = dict(title='Vocabulary', sub='Match each word', scenes=[
 dict(at=None, items=[(None, '<div class="lab">💛 A good-character word</div>'), ('Fair.', '<div class="huge">fair</div>')]),
 dict(at='Being fair means', items=[(None, '<div class="def"><b>fair</b><span>everyone plays by the same rules ⚖️</span></div>')]),
 dict(at='Now tap a word', items=[(None, TAPMEAN), ('Match all four', '<div class="say">Match all four ✅✅✅✅</div>')]),
])
V['g3ela-32-2-teach-gram'] = dict(title='Grammar', sub='Three kinds of sentences', scenes=[
 dict(at=None, items=[(None, '<div class="ask">Simple, compound or complex?</div>')]),
 dict(at='When the bell rang', items=[(None, '<div class="quote"><b class="hl">When</b> the bell rang, we lined up. 🔔</div>'),
   ("When starts a part", '<div class="say">A part that can’t stand alone = <b>complex</b></div>')]),
 dict(at='I read, and', items=[(None, '<div class="quote">I read, <b class="hl">and</b> my sister drew. 🎨</div>'),
   ('Two complete thoughts', '<div class="say">Two complete thoughts + and = <b>compound</b></div>')]),
 dict(at='Name each sentence', items=[(None, PILL('Now check your thinking')), ('Then tap the five words', '<div class="say">👆 Tap the five words that are wrong.</div>')]),
])
V['g3ela-32-2-teach-spell'] = dict(title='Spelling', sub='Which rule is it?', scenes=[
 dict(at=None, items=[(None, '<div class="lab">🕵️ Rule detective!</div>'), ('Which word dropped', '<div class="ask">Which word dropped a silent e?</div>')]),
 dict(at='Raking.', items=[(None, '<div class="build"><span class="tile">rak<s>e</s></span><b>+</b><span class="tile key">ing</span></div>'),
   ('Rake, drop the e', '<div class="swap">rake ➜ <b>raking</b> 🍂</div>')]),
 dict(at='Read the rule', items=[(None, '<div class="say">👆 Read each question. Tap the one word that fits.</div>')]),
])
V['g3ela-32-2-teach-rwm'] = dict(title='Read Like a Writer', sub='Opti shows you how', scenes=[
 dict(at=None, items=[(None, '<div class="lab">✍️ All three parts, with a different sentence</div>'),
   ('Nothing is sweeter', '<div class="quote">Nothing is sweeter in this sad world than the sound of someone you love calling your name. Nothing.<small>The Tale of Despereaux</small></div>')]),
 dict(at='Part one, read like a reader', items=[(None, '<div class="steps"><span><i>1</i>Reader</span><span><i>2</i>Writer</span><span><i>3</i>Your own</span></div>'),
   ('The princess calls', '<div class="say">1️⃣ The princess calls his name. It means everything to him. 🐭</div>')]),
 dict(at='Part two, read like a writer', items=[(None, '<div class="say">2️⃣ The author stops… then adds one more word: <b>Nothing.</b></div>'),
   ('The add-on makes us stop', '<div class="say">The add-on makes us stop and feel it. ✋</div>')]),
 dict(at='Part three, write your own', items=[(None, '<div class="quote">Pizza night is the best night of the week. The best. 🍕<small>Opti’s sentence</small></div>'),
   ("Now it's your turn", '<div class="say">Your turn with Mrs. Lambchop’s sentence: one sentence in each box.</div>')]),
])
V['g3ela-32-3-teach-morph'] = dict(title='Morphology', sub='Build the word', scenes=[
 dict(at=None, items=[(None, '<div class="lab">🧩 Snap the parts together</div>'), ('Sad.', tiles(('sad', False), ('ness', True))), ('Sadness!', '<div class="def"><b>sadness</b><span>being sad 🌧️</span></div>')]),
 dict(at='Say each pair', items=[(None, '<div class="say">Say the parts, then type the whole word.</div>'), ('Then tap Check My Answers', PILL('Check My Answers'))]),
])
V['g3ela-32-3-teach-vocab'] = dict(title='Vocabulary', sub='Pick the word that fits', scenes=[
 dict(at=None, items=[(None, '<div class="lab">🎯 Try each word in the blank</div>'), ('Mia said thank you', '<div class="quote">Mia said thank you and held the door. That shows ____.<small>Opti’s sentence</small></div>')]),
 dict(at='Courage?', items=[(None, '<div class="swap">courage? 🤔 not quite</div>'), ('Courtesy?', '<div class="swap"><b>courtesy</b> ✅</div>')]),
 dict(at='Now pick the word', items=[(None, '<div class="say">👆 Pick the word that fits each sentence.</div>')]),
])
V['g3ela-32-3-teach-gram'] = dict(title='Grammar', sub='Be the editor', scenes=[
 dict(at=None, items=[(None, '<div class="lab">✏️ Be the editor</div>'), ('my dogs bowl', '<div class="quote">my dogs bowl was empty and he looked sad</div>')]),
 dict(at='My gets a capital', items=[(None, '<div class="swap">my ➜ <b>My</b></div>'), ("Dog's gets", '<div class="swap">dogs ➜ <b>dog’s</b> (belonging) 🐶</div>'),
   ('A comma goes before and', '<div class="swap">empty ➜ <b>empty,</b> and</div>')]),
 dict(at='Read the before and after', items=[(None, PILL('Check yourself')), ('Then say the gray sentence', '<div class="say">🗣️ Say it the right way. Then tap Check your sentence.</div>')]),
])
V['g3ela-32-3-teach-spell'] = dict(title='Spelling', sub='Find the misspelled words', scenes=[
 dict(at=None, items=[(None, '<div class="lab">🔍 Spot the mistake</div>'), ('She jumped', '<div class="quote">She jumped in the <b class="hl">puddel</b>.</div>')]),
 dict(at='Puddle ends in', items=[(None, '<div class="swap">puddel ➜ <b>puddle</b> (ends in l e) 💦</div>')]),
 dict(at='Read the rule', items=[(None, '<div class="say">👆 Two misspelled words in each sentence. Find all six.</div>')]),
])
V['g3ela-32-4-teach-morph'] = dict(title='Morphology', sub='Roll and explain', scenes=[
 dict(at=None, items=[(None, '<div class="ask">Quick question: what does <b>re</b> mean?</div>'), ('Again!', '<div class="say">re = again ✅</div>')]),
 dict(at="Here's a word", items=[(None, word('restart', 're')), ('To start again.', '<div class="def"><b>restart</b><span>to start again 🔄</span></div>')]),
 dict(at='Say what the word part means', items=[(None, PILL('Roll the Dice!')), ('tap Check My Thinking', PILL('Check My Thinking'))]),
])
V['g3ela-32-4-teach-vocab'] = dict(title='Vocabulary', sub='A word, a book, and you', scenes=[
 dict(at=None, items=[(None, '<div class="lab">📚 A book… and me</div>'), ('Loyalty.', '<div class="huge">loyalty</div>')]),
 dict(at='Arthur and I', items=[(None, '<div class="quote">Arthur and I both show loyalty: he helps his brother Stanley get round again, and I stick by my friends.<small>Opti’s sentence</small></div>')]),
 dict(at='Now choose your word', items=[(None, '<div class="say">✏️ One sentence: your character and you.</div>')]),
])
V['g3ela-32-4-teach-gram'] = dict(title='Grammar', sub='Three passes', scenes=[
 dict(at=None, items=[(None, '<div class="lab">✏️ Three passes, like an editor</div>'), ('my sisters cat', '<div class="quote">my sisters cat runned under the bed</div>')]),
 dict(at='Pass one, capitals', items=[(None, '<div class="swap">Pass 1: my ➜ <b>My</b></div>'),
   ('Pass two', '<div class="swap">Pass 2: sisters ➜ <b>sister’s</b> 🐱</div>'), ('Pass three', '<div class="swap">Pass 3: runned ➜ <b>ran</b></div>')]),
 dict(at='Now do your passes', items=[(None, '<div class="say">👆 Tap all seven words that need fixing.</div>')]),
])
V['g3ela-32-4-teach-spell'] = dict(title='Spelling', sub='Roll a word, name its rule', scenes=[
 dict(at=None, items=[(None, '<div class="lab">🎲 Dice roll!</div>'), ('hiking!', '<div class="huge">hiking 🥾</div>')]),
 dict(at='The base word is hike', items=[(None, '<div class="build"><span class="tile">hik<s>e</s></span><b>+</b><span class="tile key">ing</span></div>'),
   ('the e dropped', '<div class="say">Rule: drop the silent e ✅</div>')]),
 dict(at='Tap Roll the dice', items=[(None, PILL('Roll the dice')), ('Then tap Check my answer', PILL('Check my answer'))]),
])
