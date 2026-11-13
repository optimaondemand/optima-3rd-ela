# Scene specs for the week 19 Opti teach videos. Each item appears at the
# moment Opti says its anchor (a phrase from the script). Scripts = DATA.teach.
W = lambda *a: ' '.join(a)
def word(w, part=None, cls=''):
    if part:
        i = w.index(part)
        return '<span class="wd %s">%s<b class="pt">%s</b>%s</span>' % (cls, w[:i], part, w[i+len(part):])
    return '<span class="wd %s">%s</span>' % (cls, w)
PILL = lambda t: '<span class="pill">👆 %s</span>' % t
V = {}
V['g3ela-19-1-teach-morph'] = dict(title='Morphology', sub='Crack the word part', scenes=[
 dict(at=None, items=[
   ('Here are four words', '<div class="lab">Four words</div>'),
   ('transport', word('transport','port')), ('import', word('import','port')),
   ('export', word('export','port')), ('report', word('report','port')),
   ('What part do all four', '<div class="ask">🤔 What part do all four share?</div>'),
 ], hl=[('What part do all four', '.pt')], layout='words'),
 dict(at='Now think about each word', items=[
   (None, '<div class="big">📦 ➜ 🏠</div>'),
   ('something is being moved', '<div class="say">In every word, something is <u>moved</u> from one place to another.</div>'),
   ('So what do you think', '<div class="huge"><b class="gold">port</b> = ?</div>'),
 ]),
 dict(at='Then tap See if you cracked it', items=[
   (None, PILL('See if you cracked it')),
   ('type the missing root', '<div class="boxes"><span class="wd">trans<i class="blank"></i></span><span class="wd">im<i class="blank"></i></span><span class="wd">ex<i class="blank"></i></span></div>'),
   ('tap Check My Work', PILL('Check My Work')),
 ]),
])
V['g3ela-19-1-teach-vocab'] = dict(title='Vocabulary', sub='Be a word detective', scenes=[
 dict(at=None, items=[
   (None, '<div class="lab">🔍 Word detective</div>'),
   ("Here's scheme", '<div class="huge">scheme</div>'),
 ]),
 dict(at='Read the sentence', items=[
   (None, '<div class="quote">“A <b class="hl">scheme</b> had leaped into his head.”</div>'),
   ('Jemmy just thought', '<div class="say">💡 Jemmy just thought of something, all of a sudden.</div>'),
   ('Scheme has no prefix', '<div class="parts"><span class="slot">no prefix</span><span class="wd">scheme</span><span class="slot">no suffix</span></div>'),
   ('Something that leaps', '<div class="say">Leaps into your head + you\'re in trouble ➜ a <u>plan</u>?</div>'),
 ]),
 dict(at='A scheme is a clever plan', items=[
   (None, '<div class="def"><b>scheme</b><span>a clever plan, often a sneaky one</span></div>'),
   ('Now tap Opti reads it', PILL('Opti reads it')),
   ('Guess the meaning', '<div class="say">Guess ➜ flip the card to check 🃏</div>'),
   ('Then play the matching game', PILL('Matching game')),
 ]),
])
V['g3ela-19-1-teach-gram'] = dict(title='Grammar', sub='Compound sentences', scenes=[
 dict(at=None, items=[
   ('A compound sentence is', '<div class="eq"><span class="th">complete thought</span><span class="glue">, + joining word</span><span class="th">complete thought</span></div>'),
   ('like and, but, or so', '<div class="chips"><span>and</span><span>but</span><span>so</span></div>'),
 ]),
 dict(at='Read the sentence from the book', items=[
   (None, '<div class="quote q2"><span class="h1">He reached for the wicker basket,</span> <span class="jw">but</span> <span class="h2">Cutwater snatched it back.</span></div>'),
   ('Could each half stand alone', '<div class="ask">🤔 Could each half stand alone as a sentence?</div>'),
   ('tap Now check your thinking', PILL('Now check your thinking')),
 ], hl=[('Could each half stand alone', '.h1,.h2')]),
 dict(at='Next, sort the word groups', items=[
   (None, '<div class="lab">Sort the word groups</div>'),
   ('Some are one thought', '<div class="col">One thought</div>'),
   ('Some are two thoughts joined', '<div class="col">Two thoughts joined</div>'),
   ('And some are not sentences', '<div class="col">Not a sentence<small>leaves you hanging…</small></div>'),
   ('Tap a word group', PILL('Tap a word group, then its column')),
 ], layout='cols'),
])
V['g3ela-19-1-teach-spell'] = dict(title='Spelling', sub='Consonant-le syllables', scenes=[
 dict(at=None, items=[
   ('table', '<span class="wd">ta<b class="pt">ble</b></span>'), ('little', '<span class="wd">lit<b class="pt">tle</b></span>'),
   ('candle', '<span class="wd">can<b class="pt">dle</b></span>'), ('simple', '<span class="wd">sim<b class="pt">ple</b></span>'),
   ('Listen to the last beat', '<div class="say">🔊 Listen to the <u>last beat</u>.</div>'),
   ('What do you notice', '<div class="ask">🤔 What do you notice?</div>'),
 ], hl=[('Now look at the last three letters', '.pt')], dots='and look where the dot goes', layout='words'),
 dict(at='Tap See the Rule', items=[
   (None, PILL('See the Rule')),
   ('Then tap each of the eight words', '<div class="bins"><span>Consonant-le</span><span>Other ending</span></div>'),
   ('Watch out', '<div class="ask">⚠️ Not every word ends the same way!</div>'),
 ]),
])
V['g3ela-19-2-teach-rwm'] = dict(title='Read Like a Writer', sub='Three parts', scenes=[
 dict(at=None, items=[
   ('has three parts', '<div class="steps"><span><i>1</i>Reader</span><span><i>2</i>Writer</span><span><i>3</i>Mimic</span></div>'),
   ('Cutwater yanked Jemmy', '<div class="quote">“Cutwater yanked Jemmy to his feet.”<small>Chapter 9</small></div>'),
 ]),
 dict(at='Part one', items=[
   (None, '<div class="step1"><i>1</i> Read like a Reader</div>'),
   ('What is happening', '<div class="ask">🤔 What is happening?</div>'),
   ('Cutwater is angry', '<div class="say">Cutwater is angry, so he pulls Jemmy up, <u>hard</u>.</div>'),
 ]),
 dict(at='Part two', items=[
   (None, '<div class="step1"><i>2</i> Read like a Writer</div>'),
   ('Which word does the work', '<div class="quote">“Cutwater <b class="hl">yanked</b> Jemmy to his feet.”</div>'),
   ('The author could have said pulled', '<div class="swap"><s>pulled</s> ➜ <b>yanked</b> 💪</div>'),
   ('so we feel how rough', '<div class="say">We feel how <u>rough</u> Cutwater is.</div>'),
 ]),
 dict(at='Part three', items=[
   (None, '<div class="step1"><i>3</i> Mimic</div>'),
   ('My little brother', '<div class="quote mine">My little brother <b class="hl">yanked</b> the blanket off my bed.</div>'),
   ("Now it's your turn", '<div class="say">✏️ Your turn: the prince\'s sentence.<br>One sentence in each box.</div>'),
 ]),
])

# ---------- Days 2-4 (Nov 13 2026): show that day's activity, never re-teach Day 1 ----------
TILE = lambda t, cls='': '<span class="tile %s">%s</span>' % (cls, t)
V['g3ela-19-2-teach-morph'] = dict(title='Morphology', sub='Match the word to its meaning', scenes=[
 dict(at=None, items=[
   (None, '<div class="lab">👀 Watch this</div>'),
   ('Support', word('support', 'port')),
   ('sup, which means under', '<div class="chips"><span>sup = under</span></div>'),
   ('So to support something', '<div class="say">carry it from <u>underneath</u> 📦⬆️</div>'),
 ], hl=[('Find port at the end', '.pt')]),
 dict(at='Use the same trick', items=[
   (None, '<div class="grid2"><span class="tile">a word</span><span class="tile m">its meaning</span><span class="tile">a word</span><span class="tile m">its meaning</span></div>'),
   ('Tap a word, then tap', PILL('Tap a word, then tap its meaning')),
 ]),
])
V['g3ela-19-2-teach-vocab'] = dict(title='Vocabulary', sub='Listen, guess, flip', scenes=[
 dict(at=None, items=[
   (None, '<span class="wd">obliged</span>'),
   ('He tells the prince', '<div class="quote">“He\'ll be ever so much <b class="hl">obliged</b>…”<small>Billy, Chapter 7</small></div>'),
   ('Billy is pretending', '<div class="say">🎭 Billy is only pretending to be polite.</div>'),
   ('Obliged means thankful', '<div class="def"><b>obliged</b><span>thankful</span></div>'),
 ]),
 dict(at='The cards work just like last time', items=[
   ('listen', '<div class="steps"><span><i>🔊</i>listen</span><span><i>🤔</i>guess</span><span><i>🃏</i>flip</span></div>'),
   ('Then match all four', PILL('Match all four')),
 ]),
])
V['g3ela-19-2-teach-gram'] = dict(title='Grammar', sub='Find the two thoughts', scenes=[
 dict(at=None, items=[
   ('The fog rolled in, and', '<div class="quote q2"><span class="h1">The fog rolled in,</span> <span class="jw">and</span> <span class="h2">the boys got lost.</span></div>'),
   ('First thought', '<div class="say">1️⃣ first thought</div>'),
   ('Second thought', '<div class="say">2️⃣ second thought</div>'),
   ('The word and is just the glue', '<div class="say">🧴 <b>and</b> is the glue. Skip it.</div>'),
 ], hl=[('First thought', '.h1'), ('Second thought', '.h2')]),
 dict(at='In each sentence', items=[
   (None, PILL('Tap the first thought, then the second')),
 ]),
])
V['g3ela-19-2-teach-spell'] = dict(title='Spelling', sub='Pick the consonant-le word', scenes=[
 dict(at=None, items=[
   (None, '<div class="lab">⚡ Quick test</div>'),
   ('Cattle, kitten', '<span class="wd w1">cattle</span>'), ('kitten', '<span class="wd">kitten</span>'), ('carpet', '<span class="wd">carpet</span>'),
   ('Which one ends', '<div class="ask">🤔 Which one ends with a consonant + le?</div>'),
 ], hl=[('Cat, tle', '.w1')], layout='words'),
 dict(at='In each row', items=[
   (None, '<div class="row4"><span class="tile">▢</span><span class="tile">▢</span><span class="tile on2">▢</span><span class="tile">▢</span></div>'),
   ('only one word ends that way', '<div class="say">Only <u>one</u> in each row.</div>'),
   ('Say every word', PILL('Say it, listen, tap it')),
 ]),
])
V['g3ela-19-3-teach-morph'] = dict(title='Morphology', sub='Build the word', scenes=[
 dict(at=None, items=[
   ('Tele means far', '<div class="chips"><span>tele = far</span></div>'),
   ('Tele, plus port', '<div class="build"><span class="tile">tele</span><b>+</b><span class="tile">port</span></div>'),
   ('Teleport', '<div class="huge">teleport 🚀✨</div>'),
   ('To carry something far away', '<div class="say">carry something <u>far away</u> in a flash</div>'),
 ]),
 dict(at='Now you build the real ones', items=[
   ('Say each pair', '<div class="build"><span class="tile">part</span><b>+</b><span class="tile">port</span><b>→</b><span class="tile"><i class="blank"></i></span></div>'),
   ('Type the whole word', '<div class="say">⌨️ Type the whole word.</div>'),
   ('Then tap Check My Answers', PILL('Check My Answers')),
 ]),
])
V['g3ela-19-3-teach-vocab'] = dict(title='Vocabulary', sub='Use the word bank', scenes=[
 dict(at=None, items=[
   (None, '<div class="bubble"><b>Cutwater:</b> “I\'ll whip the <b class="hl">mulishness</b> out of him!”</div>'),
   ('Mule, ish, ness', '<div class="build"><span class="tile">mule 🐴</span><b>+</b><span class="tile">ish</span><b>+</b><span class="tile">ness</span></div>'),
   ('stubborn like a mule', '<div class="say">= stubborn like a mule</div>'),
 ]),
 dict(at='Defiant, parley and contrary', items=[
   (None, '<div class="chips"><span>defiant</span><span>parley</span><span>contrary</span></div>'),
   ('Read each sentence', '<div class="say">Try each word in the ▁▁▁▁ <br>Keep the one that makes sense ✔</div>'),
   ('Then tap Check My Work', PILL('Check My Work')),
 ]),
])
V['g3ela-19-3-teach-gram'] = dict(title='Grammar', sub='Find the comma spot', scenes=[
 dict(at=None, items=[
   (None, '<div class="lab">🔍 These sentences lost their commas</div>'),
   ('The horse was fast', '<div class="quote q3">The horse was <span class="hw">fast</span><span class="cm">,</span> but the outlaws were faster.</div>'),
   ('Hear the little pause', '<div class="say">⏸ Hear the little pause?</div>'),
   ('The comma goes there', '<div class="say">The comma goes right before <b>but</b>.</div>'),
 ], hl=[('The comma goes there', '.cm'), ('The comma goes there', '.hw')]),
 dict(at='Find that spot', items=[
   (None, '<div class="build"><span class="say">The word before the comma:</span><span class="tile"><i class="blank"></i></span></div>'),
   ('type the word', PILL('Type it')),
 ]),
])
V['g3ela-19-3-teach-spell'] = dict(title='Spelling', sub='Build with tiles', scenes=[
 dict(at=None, items=[
   ('Pud, dle', '<div class="build"><span class="tile">pud</span><b>+</b><span class="tile">dle</span></div>'),
   ('Puddle', '<div class="huge">puddle 💧</div>'),
   ('The d sticks', '<div class="say">The <b>d</b> sticks with the <b>le</b>.</div>'),
 ]),
 dict(at='Build each word', items=[
   ('Tap the first part', '<div class="build"><span class="tile"><i>1</i> first part</span><span class="tile"><i>2</i> last part</span></div>'),
   ("If a tile is in the wrong spot", '<div class="say">❌ Wrong spot? It won\'t stick. Try the other one.</div>'),
 ]),
])
V['g3ela-19-4-teach-morph'] = dict(title='Morphology', sub='Roll and crack', scenes=[
 dict(at=None, items=[
   (None, '<div class="big">🎲</div>'),
   ('Every word on the dice', '<div class="say">Every word has <b class="gold">port</b> = carry</div>'),
   ('Look at the part in front', '<div class="build"><span class="tile key">? ? ?</span><span class="tile">port</span></div>'),
   ('That part is your clue', '<div class="say">🔑 That part is your clue.</div>'),
 ]),
 dict(at='Say what the whole word means', items=[
   (None, '<div class="say">🗣️ Say what it means.</div>'),
   ('then tap Check My Thinking', PILL('Check My Thinking')),
   ('Do all six', '<div class="dots6">● ● ● ● ● ●</div>'),
 ]),
])
V['g3ela-19-4-teach-vocab'] = dict(title='Vocabulary', sub='Review the week', scenes=[
 dict(at=None, items=[
   ('fathom', '<div class="chips"><span>fathom</span><span>flummox</span><span>parley</span><span>angling</span></div>'),
 ]),
 dict(at="Here's a trick", items=[
   (None, '<div class="lab">💡 A trick</div>'),
   ('Read each sentence out loud', '<div class="say">🗣️ Read it out loud with the word in the ▁▁▁▁</div>'),
   ('If it sounds right', '<div class="say">Sounds right? Makes sense? ✔ Keep it.</div>'),
   ('Then tap Check My Work', PILL('Check My Work')),
 ]),
])
V['g3ela-19-4-teach-gram'] = dict(title='Grammar', sub='Spot the mistake', scenes=[
 dict(at=None, items=[
   (None, '<div class="ask">🕵️ Can you spot what\'s wrong?</div>'),
   ('The fog was thick but', '<div class="quote q3">The fog was thick but<span class="bad">,</span> they kept going.</div>'),
   ('It belongs right before it', '<div class="quote q3 good">The fog was thick<span class="cm on">,</span> but they kept going. ✔</div>'),
 ], hl=[('The comma jumped', '.bad')]),
 dict(at='Read each sentence', items=[
   (None, '<div class="build"><span class="pill">👆 the wrong word</span><b>or</b><span class="pill">👆 No mistake</span></div>'),
 ]),
])
V['g3ela-19-4-teach-spell'] = dict(title='Spelling', sub='Roll and split', scenes=[
 dict(at=None, items=[
   ('Bottle', '<span class="wd">bot<b class="pt">tle</b></span>'),
   ('Count back three letters', '<div class="say">Count back 3 letters: <b>t · l · e</b></div>'),
   ('Bot, tle', '<div class="huge">bot · tle</div>'),
 ], hl=[('Count back three letters', '.pt')], layout='words'),
 dict(at='Tap Roll the dice', items=[
   (None, '<div class="big">🎲</div>'),
   ('Say the word out loud', '<div class="say">🗣️ Say it. Split it.</div>'),
   ('Then tap Check my answer', PILL('Check my answer')),
   ('Roll all six words', '<div class="dots6">● ● ● ● ● ●</div>'),
 ]),
])

from specs18 import V18
V.update(V18)
