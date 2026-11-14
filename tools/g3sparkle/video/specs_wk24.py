# Scene specs for the week 24 Opti teach videos (Medieval Nonfiction, part 2).
# Each item appears when Opti says its anchor (a phrase from the script). Scripts = DATA.teach.
# Never shows an answer the page asks for: examples are postscript, scriptwriter, description, subscription;
# battlements, lance, stall, legend; knights trained hard / the castle kitchen / smiths-weavers-potters / the market;
# painful/painless, calm/calmness/calmly, breathless, gladness, thoughtful/thoughtless;
# and the 24.2 article line "In reality, not every knight followed the code."
def word(w, part=None, cls=''):
    if part:
        i = w.index(part)
        return '<span class="wd %s">%s<b class="pt">%s</b>%s</span>' % (cls, w[:i], part, w[i+len(part):])
    return '<span class="wd %s">%s</span>' % (cls, w)
PILL = lambda t: '<span class="pill">👆 %s</span>' % t
V = {}
# ---------------- Day 1: teach the idea ----------------
V['g3ela-24-1-teach-morph'] = dict(title='Morphology', sub='A root that means write', scenes=[
 dict(at=None, items=[
   (None, '<div class="ask">🤔 A letter, a story, a grocery list…</div>'),
   ('Somebody wrote them', '<div class="big">✉️ 📖 📝 ✍️</div>'),
 ]),
 dict(at="There's a root", items=[
   (None, '<div class="lab">One root, two spellings</div>'),
   ('Script.', '<div class="huge">script</div>'),
   ('And scribe', '<div class="build"><span class="tile key">script</span><b>=</b><span class="tile key">scribe</span><b>=</b><span class="tile">write ✍️</span></div>'),
 ]),
 dict(at="Here's a word", items=[
   (None, word('postscript', 'script')),
   ('Post means after', '<div class="build"><span class="tile">post</span><b>+</b><span class="tile key">script</span></div>'),
   ('So a postscript is writing', '<div class="def"><b>P.S.</b><span>writing you add after a letter ✉️</span></div>'),
 ]),
 dict(at='Read the four words', items=[
   (None, '<div class="say">📖 Read the four words. Think about the questions.</div>'),
   ('Then tap See if you cracked it', PILL('See if you cracked it')),
   ('type the missing parts', '<div class="build"><span class="tile">de</span><b>+</b><span class="tile"><i class="blank"></i></span></div>'),
 ]),
])
V['g3ela-24-1-teach-vocab'] = dict(title='Vocabulary', sub='Be a word detective', scenes=[
 dict(at=None, items=[
   (None, '<div class="lab">🔍 Word detective</div>'),
   ('Battlements', '<div class="huge">battlements</div>'),
 ]),
 dict(at="Here's a sentence", items=[
   (None, '<div class="quote">The archers hid behind the <b class="hl">battlements</b> at the top of the wall.</div>'),
   ('They hid behind them', '<div class="say">behind them… on top of the wall 🏰</div>'),
   ('So battlements must be', '<div class="def"><b>battlements</b><span>the bumpy stone edge on top of a castle wall</span></div>'),
 ]),
 dict(at='One, read the sentence', items=[
   (None, '<div class="steps"><span><i>1</i>Read</span><span><i>2</i>Word parts</span><span><i>3</i>Check</span></div>'),
   ('Now fill in each sentence', '<div class="say">✏️ Fill in each sentence from the word bank.</div>'),
   ('tap Check My Work', PILL('Check My Work')),
   ('Then play the matching game', PILL('Matching game')),
 ]),
])
V['g3ela-24-1-teach-gram'] = dict(title='Grammar', sub='Main idea and details', scenes=[
 dict(at=None, items=[
   (None, '<div class="lab">🪑 A paragraph is like a table</div>'),
   ('The main idea is the tabletop', '<div class="build"><span class="tile key">main idea</span><b>=</b><span class="tile">the tabletop</span></div>'),
   ('The details are the legs', '<div class="build"><span class="tile">details</span><b>=</b><span class="tile">the legs</span></div>'),
 ]),
 dict(at='Listen. Knights trained hard', items=[
   (None, '<div class="quote"><b class="hl">Knights trained hard.</b> They practiced with swords. They rode horses every day.</div>'),
   ('Knights trained hard is the main idea', '<div class="say">⭐ Knights trained hard → <b>main idea</b></div>'),
   ('The other two hold it up', '<div class="say">⚔️ 🐎 → <b>details</b></div>'),
   ('And I like pizza', '<div class="say">🍕 I like pizza? → <b>off the topic</b> ❌</div>'),
 ]),
 dict(at='Read the paragraph', items=[
   (None, PILL('Now check your thinking')),
   ('Then sort each sentence', '<div class="bins"><span style="width:270px">Main idea</span><span style="width:270px">Detail</span><span style="width:270px">Off the topic</span></div>'),
 ]),
])
V['g3ela-24-1-teach-spell'] = dict(title='Spelling', sub='Four endings, four jobs', scenes=[
 dict(at=None, items=[
   (None, '<div class="lab">🗣️ Say these with me</div>'),
   ('Painful', word('painful', 'ful')),
   ('Painless', word('painless', 'less')),
 ], layout='words'),
 dict(at='Same base word', items=[
   (None, '<div class="def"><b>-ful</b><span>full of: painful = full of pain</span></div>'),
   ('Less means without', '<div class="def"><b>-less</b><span>without: painless = without pain</span></div>'),
 ]),
 dict(at='Now two more jobs', items=[
   (None, '<div class="build"><span class="tile">calm</span><b>➜</b><span class="tile key">calmness</span></div>'),
   ('Ness turns a describing word', '<div class="say"><b>-ness</b> names a thing</div>'),
   ('Calm, calmly', '<div class="build"><span class="tile">calm</span><b>➜</b><span class="tile key">calmly</span></div>'),
   ('Ly tells how', '<div class="say"><b>-ly</b> tells how</div>'),
 ]),
 dict(at='Say the words in Group A', items=[
   (None, '<div class="say">🗣️ Say Group A and Group B out loud.</div>'),
   ('tap See the Rule', PILL('See the Rule')),
   ('Then sort all eight words', '<div class="bins"><span style="width:190px">-ful</span><span style="width:190px">-less</span><span style="width:190px">-ness</span><span style="width:190px">-ly</span></div>'),
 ]),
])
# ---------------- Day 2 ----------------
V['g3ela-24-2-teach-morph'] = dict(title='Morphology', sub='Match each word to its meaning', scenes=[
 dict(at=None, items=[
   (None, '<div class="lab">👀 Watch one match first</div>'),
   ('Script and scribe mean write', '<div class="def"><b>script / scribe</b><span>write</span></div>'),
   ('Scriptwriter', word('scriptwriter', 'script')),
 ]),
 dict(at='A scriptwriter writes', items=[
   (None, '<div class="build"><span class="tile">scriptwriter</span><b>➜</b><span class="tile m">writes the words actors say 🎬</span></div>'),
   ("That's my match", '<div class="big">✅</div>'),
 ]),
 dict(at='Read the Remember box', items=[
   (None, '<div class="say">📌 Read the Remember box.</div>'),
   ('Then tap a word', '<div class="build"><span class="tile">word</span><b>➜</b><span class="tile m">what it means</span></div>'),
   ('Match all four words', '<div class="say">Match all four! ✨</div>'),
 ]),
])
V['g3ela-24-2-teach-vocab'] = dict(title='Vocabulary', sub='A word from the joust', scenes=[
 dict(at=None, items=[
   (None, '<div class="ask">Ever seen a joust?</div>'),
   ('Two knights charge', '<div class="big">🐎 ➡️ ⬅️ 🐎</div>'),
   ('Lance.', '<div class="huge">lance</div>'),
 ]),
 dict(at='They charge holding it', items=[
   (None, '<div class="say">🐎 They charge holding it…</div>'),
   ('so a lance must be', '<div class="def"><b>lance</b><span>a long pole for fighting on a horse</span></div>'),
 ]),
 dict(at='Read how we figured out', items=[
   (None, '<div class="say">📖 Read how we figured out the first word.</div>'),
   ('fill in each sentence', '<div class="say">✏️ Fill in each sentence from the word bank.</div>'),
   ('tap Check My Work', PILL('Check My Work')),
   ('Last, play the matching game', PILL('Matching game')),
 ]),
])
V['g3ela-24-2-teach-gram'] = dict(title='Grammar', sub='Find the main idea', scenes=[
 dict(at=None, items=[
   (None, '<div class="ask">Which one holds up the others?</div>'),
   ('Bakers made bread', '<div class="chips"><span class="tile">Bakers made bread.</span><span class="tile">The castle kitchen was busy.</span><span class="tile">Cooks roasted meat.</span></div>'),
 ]),
 dict(at="It's the middle one", items=[
   (None, '<div class="chips"><span class="tile">Bakers made bread.</span><span class="tile key">The castle kitchen was busy.</span><span class="tile">Cooks roasted meat.</span></div>'),
   ('The kitchen was busy, and', '<div class="say">⭐ main idea &nbsp;·&nbsp; 🍞 🍖 details</div>'),
 ]),
 dict(at='Read the Remember box', items=[
   (None, '<div class="say">📌 Read the Remember box.</div>'),
   ('Then in each mixed-up paragraph', PILL('Tap the main idea')),
 ]),
])
V['g3ela-24-2-teach-spell'] = dict(title='Spelling', sub='Find the named ending', scenes=[
 dict(at=None, items=[
   (None, '<div class="lab">🔎 Which word means <i>without</i>?</div>'),
   ('Mindful', '<span class="wd">mindful</span>'),
   ('Breathless', '<span class="wd">breathless</span>'),
   ('Fondness', '<span class="wd">fondness</span>'),
   ('Softly', '<span class="wd">softly</span>'),
 ], layout='words'),
 dict(at='Breathless!', items=[
   (None, word('breathless', 'less', 'on')),
   ('Breath, plus less', '<div class="build"><span class="tile">breath</span><b>+</b><span class="tile key">less</span><b>=</b><span class="tile">without breath</span></div>'),
 ]),
 dict(at='Read the rule', items=[
   (None, '<div class="say">📖 Read the rule.</div>'),
   ('Then in each row', PILL('Tap the word with the named ending')),
 ]),
])
V['g3ela-24-2-teach-rwm'] = dict(title='Read Like a Writer', sub='A short sentence, a big surprise', scenes=[
 dict(at=None, items=[
   ('all three parts', '<div class="steps"><span><i>1</i>Reader</span><span><i>2</i>Writer</span><span><i>3</i>Mimic</span></div>'),
   ('In reality, not every knight', '<div class="quote">“In reality, not every knight followed the code.”<small>Knights: Warriors and Gentlemen</small></div>'),
 ]),
 dict(at='Part one', items=[
   (None, '<div class="step1"><i>1</i> Read like a Reader</div>'),
   ('Some knights broke the rules', '<div class="say">⚔️ Some knights broke the rules of chivalry.</div>'),
 ]),
 dict(at='Part two', items=[
   (None, '<div class="step1"><i>2</i> Read like a Writer</div>'),
   ("It's short", '<div class="quote"><b class="hl">In reality,</b> not every knight followed the code.</div>'),
   ('the truth, not the story', '<div class="build"><span class="tile">the story 📖</span><b>➜</b><span class="tile key">the truth ❗</span></div>'),
 ]),
 dict(at='Part three', items=[
   (None, '<div class="step1"><i>3</i> Mimic</div>'),
   ("Here's mine", '<div class="quote mine"><b class="hl">In reality,</b> not every owl stays up all night. 🦉☀️</div>'),
   ("Now it's your turn", '<div class="say">✏️ Your turn: the sentence about years of training.<br>One sentence in each box.</div>'),
 ]),
])
# ---------------- Day 3 ----------------
V['g3ela-24-3-teach-morph'] = dict(title='Morphology', sub='Build the word', scenes=[
 dict(at=None, items=[
   (None, '<div class="lab">🧱 Snap three parts together</div>'),
   ('De. Script. Ion', '<div class="build"><span class="tile">de</span><b>+</b><span class="tile key">script</span><b>+</b><span class="tile">ion</span></div>'),
   ('Description!', '<div class="huge">description</div>'),
   ('A description writes down', '<div class="say">📝 writes down what something is like</div>'),
 ]),
 dict(at='Say the parts out loud', items=[
   (None, '<div class="say">🗣️ Say the parts, then say them fast.</div>'),
   ('Type the whole word', '<div class="build"><span class="tile">…</span><b>+</b><span class="tile key">script</span><b>=</b><span class="tile"><i class="blank"></i></span></div>'),
   ('tap Check My Answers', PILL('Check My Answers')),
 ]),
])
V['g3ela-24-3-teach-vocab'] = dict(title='Vocabulary', sub='A word from the market', scenes=[
 dict(at=None, items=[
   (None, '<div class="lab">🏘️ Listen in a busy town</div>'),
   ('Stall.', '<div class="huge">stall</div>'),
   ('A merchant sold apples', '<div class="quote">A merchant sold apples from his <b class="hl">stall</b> in the market square. 🍎</div>'),
 ]),
 dict(at='He sold things from it', items=[
   (None, '<div class="say">He sold things from it, outside… 🧺</div>'),
   ('so a stall must be', '<div class="def"><b>stall</b><span>a little shop with a table, outside</span></div>'),
 ]),
 dict(at='Put a bank word', items=[
   (None, '<div class="say">Try a bank word in the blank. Does it make sense? ✅</div>'),
   ('Then try the matching game', PILL('Matching game')),
 ]),
])
V['g3ela-24-3-teach-gram'] = dict(title='Grammar', sub='Three details, one topic', scenes=[
 dict(at=None, items=[
   (None, '<div class="lab">🔎 Three details, one topic</div>'),
   ('Smiths made tools', '<div class="say">🔨 Smiths made tools.</div>'),
   ('Weavers made cloth', '<div class="say">🧵 Weavers made cloth.</div>'),
   ('Potters made bowls', '<div class="say">🏺 Potters made bowls.</div>'),
 ]),
 dict(at='What one word', items=[
   (None, '<div class="ask">What one word are they all about?</div>'),
   ('Workers!', '<div class="huge">workers</div>'),
   ('That one word is the topic', '<div class="def"><b>topic</b><span>the one thing the details are about</span></div>'),
 ]),
 dict(at='Read the Remember box', items=[
   (None, '<div class="say">📌 Read the Remember box.</div>'),
   ('Then read each set of details', '<div class="build"><span class="tile">details</span><b>➜</b><span class="tile"><i class="blank"></i></span></div>'),
 ]),
])
V['g3ela-24-3-teach-spell'] = dict(title='Spelling', sub='Break the word apart', scenes=[
 dict(at=None, items=[
   (None, '<div class="lab">😬 Oops!</div>'),
   ('I split gladness', '<div class="build bad"><span class="tile">gladn</span><b>·</b><span class="tile">ess</span></div>'),
   ("That's not right", '<div class="big">❌</div>'),
 ]),
 dict(at='The base word is glad', items=[
   (None, '<div class="huge">glad</div>'),
   ('So it breaks into glad', '<div class="build"><span class="tile">glad</span><b>+</b><span class="tile key">ness</span></div>'),
   ('Glad is a describing word', '<div class="say"><b>-ness</b> turns it into a thing</div>'),
 ]),
 dict(at='Read the rule', items=[
   (None, '<div class="say">📖 Read the rule.</div>'),
   ('Then tap each card', PILL('Tap each card to break it apart')),
 ]),
])
# ---------------- Day 4 ----------------
V['g3ela-24-4-teach-morph'] = dict(title='Morphology', sub='Roll a word', scenes=[
 dict(at=None, items=[
   (None, '<div class="big">😌</div>'),
   ('What do script and scribe mean', '<div class="ask">script · scribe = ?</div>'),
   ('Write!', '<div class="huge">write ✍️</div>'),
 ]),
 dict(at="Here's a word", items=[
   (None, '<div class="say">Not on the dice:</div>'),
   ('Subscription', word('subscription', 'script')),
   ('You write your name', '<div class="say">✍️ write your name to sign up</div>'),
 ]),
 dict(at='Now tap Roll the Dice', items=[
   (None, PILL('Roll the Dice!')),
   ('Say what each word means', '<div class="say">🗣️ Say what it means.</div>'),
   ('tap Check My Thinking', PILL('Check My Thinking')),
   ('Roll all six', '<div class="big">🎲 × 6</div>'),
 ]),
])
V['g3ela-24-4-teach-vocab'] = dict(title='Vocabulary', sub='A word from today’s article', scenes=[
 dict(at=None, items=[
   (None, '<div class="lab">📜 From today’s article</div>'),
   ('A legend is an old story', '<div class="def"><b>legend</b><span>an old story people told for years</span></div>'),
   ('like the stories of King Arthur', '<div class="big">🗡️ 🪨 👑</div>'),
   ('Did it really happen', '<div class="ask">Did it really happen? 🤷 Nobody knows for sure.</div>'),
 ]),
 dict(at='Try each bank word', items=[
   (None, '<div class="say">Try each bank word in a blank. Keep the one that makes sense. ✅</div>'),
   ('Then finish with the matching game', PILL('Matching game')),
 ]),
])
V['g3ela-24-4-teach-gram'] = dict(title='Grammar', sub='Find the sentence that wandered off', scenes=[
 dict(at=None, items=[
   (None, '<div class="lab">🚶 One of these wandered off</div>'),
   ('The market was busy', '<div class="chips"><span class="tile">The market was busy.</span><span class="tile">People bought fish.</span><span class="tile">My cat is orange.</span></div>'),
 ]),
 dict(at='Which one?', items=[
   (None, '<div class="chips"><span class="tile">The market was busy.</span><span class="tile">People bought fish.</span><span class="tile key">My cat is orange. 🐈</span></div>'),
   ("It isn't about the market", '<div class="say">Not about the market → off the topic ❌</div>'),
 ]),
 dict(at='In each paragraph', items=[
   (None, PILL('Tap the off-topic sentence')),
   ('If every sentence fits', PILL('No mistake')),
 ]),
])
V['g3ela-24-4-teach-spell'] = dict(title='Spelling', sub='Pick the ending and say why', scenes=[
 dict(at=None, items=[
   (None, '<div class="lab">🎲 Here’s my roll</div>'),
   ('Thought.', '<div class="huge">thought</div>'),
 ]),
 dict(at='Do I want full of thought', items=[
   (None, '<div class="ask">full of thought?</div>'),
   ('Then I pick ful', word('thoughtful', 'ful')),
   ('Without thought?', '<div class="ask">without thought?</div>'),
   ('Less: thoughtless', word('thoughtless', 'less')),
   ('I choose the ending', '<div class="say">Pick the ending that does the job you need.</div>'),
 ]),
 dict(at='Tap Roll the dice', items=[
   (None, PILL('Roll the dice')),
   ('pick an ending', '<div class="say">Pick an ending. Say why. 🗣️</div>'),
   ('Then tap Check my answer', PILL('Check my answer')),
 ]),
])
