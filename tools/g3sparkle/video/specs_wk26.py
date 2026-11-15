# Scene specs for the week 26 Opti teach films (LWW Ch. 4-6). SILENT for now (tone.py timing); captions carry the words.
# Never shows a page answer: examples are platform, formless, format, landform; superior, beastly; climbed/sits,
# looked/sees, run/hide, the queen/edmund feels; dangerous, beautiful, wardrobe/lamp/enchanted, Professor, inquisitive;
# and the Ch. 5 line "Edmund, who was becoming a nastier person every minute, thought that he had scored a great success."
def word(w, part=None, cls=''):
    if part:
        i = w.index(part)
        return '<span class="wd %s">%s<b class="pt">%s</b>%s</span>' % (cls, w[:i], part, w[i+len(part):])
    return '<span class="wd %s">%s</span>' % (cls, w)
PILL = lambda t: '<span class="pill">👆 %s</span>' % t
def tiles(*ps): return '<div class="build">' + '<b>+</b>'.join('<span class="tile%s">%s</span>' % (' key' if k else '', t) for t, k in ps) + '</div>'
V = {}
V['g3ela-26-1-teach-morph'] = dict(title='Morphology', sub='A root that means shape', scenes=[
 dict(at=None, items=[(None, '<div class="lab">Some word parts tell you about shape</div>'),
   ('Form means shape', '<div class="build"><span class="tile key">form</span><b>=</b><span class="tile">shape ⬛🔺⚪</span></div>')]),
 dict(at="Here's a word", items=[(None, word('platform', 'form')),
   ('Plat means flat', tiles(('plat: flat', False), ('form: shape', True))),
   ('So a platform', '<div class="def"><b>platform</b><span>a flat shape you stand on 🚉</span></div>')]),
 dict(at='Read the four words', items=[(None, '<div class="say">📖 Read the four words and their parts.</div>'),
   ('Then tap See what was hiding', PILL('See what was hiding')),
   ('type the missing parts', '<div class="build"><span class="tile">uni</span><b>+</b><span class="tile"><i class="blank"></i></span></div>')]),
])
V['g3ela-26-1-teach-vocab'] = dict(title='Vocabulary', sub='Be a word detective', scenes=[
 dict(at=None, items=[(None, '<div class="lab">🔍 Word detective</div>'), ('Superior.', '<div class="huge">superior</div>')]),
 dict(at="Here's the sentence", items=[(None, '<div class="quote">Edmund gave a very <b class="hl">superior</b> look, as if he were far older than Lucy.<small>Chapter 5</small></div>')]),
 dict(at='One, read the sentence', items=[(None, '<div class="steps"><span><i>1</i>Read</span><span><i>2</i>Word parts</span><span><i>3</i>Check</span></div>'),
   ('One, read', '<div class="say">1️⃣ acting older and better 😏</div>'),
   ('Two, look for word parts', tiles(('super: above', True), ('ior', False))),
   ('Superior means', '<div class="def"><b>superior</b><span>acting as if you are above someone</span></div>')]),
 dict(at='Read how we figured', items=[(None, '<div class="say">✏️ Fill in each sentence from the word bank.</div>'),
   ('tap Check My Work', PILL('Check My Work')), ('Last, play the matching game', PILL('Matching game'))]),
])
V['g3ela-26-1-teach-gram'] = dict(title='Grammar', sub='Keep verbs in one time', scenes=[
 dict(at=None, items=[(None, '<div class="lab">⏪ past · or · now ▶️</div>'),
   ('Once you pick a time', '<div class="say">Pick a time. The verbs stay there. 📌</div>')]),
 dict(at='Listen.', items=[(None, '<div class="quote">Edmund <b class="hl">climbed</b> onto the sledge and <b class="hl">sits</b> down.</div>'),
   ('Climbed is past', '<div class="say">climbed = past ⏪</div>'), ('Sits is now', '<div class="say">sits = now ▶️ 🌀 slipped!</div>'),
   ('It should be sat', '<div class="swap"><s>sits</s> ➜ <b>sat</b></div>')]),
 dict(at='Read The Rule box', items=[(None, '<div class="say">📌 Read The Rule box.</div>'), ('tap Now check your thinking', PILL('Now check your thinking')),
   ('Then find every verb', '<div class="say">🔍 Find every verb that slipped.</div>')]),
])
V['g3ela-26-1-teach-spell'] = dict(title='Spelling', sub='Count the beats', scenes=[
 dict(at=None, items=[(None, '<div class="lab">👏 Clap with me</div>'), ('Dan, ger, ous', '<div class="say">dan · ger · ous</div>'), ('Three claps', '<div class="big">👏👏👏</div>')]),
 dict(at='Each beat has one vowel sound', items=[(None, '<div class="def"><b>1 beat</b><span>= 1 vowel sound</span></div>')]),
 dict(at='Now try beautiful', items=[(None, '<div class="huge">beautiful</div>'), ('Beau, ti, ful', '<div class="say"><b class="gold">beau</b> · ti · ful</div>'),
   ('Beau has two vowel letters', '<div class="say">e + a + u … but only ONE sound in <b>beau</b></div>'),
   ('Count the sounds', '<div class="say">Count the <b>sounds</b>, not the letters. 👂</div>')]),
 dict(at='Clap the words in Group A', items=[(None, '<div class="say">👏 Clap Group A and Group B.</div>'), ('tap See the Rule', PILL('See the Rule')),
   ('Then sort the words', '<div class="bins"><span>2 beats</span><span>3 beats</span><span>4 beats</span></div>')]),
])
V['g3ela-26-2-teach-morph'] = dict(title='Morphology', sub='Match the word to its meaning', scenes=[
 dict(at=None, items=[(None, '<div class="lab">👀 Watch one match first</div>'), ('Find form', '<div class="build"><span class="tile key">form</span><b>=</b><span class="tile">shape</span></div>')]),
 dict(at='Formless.', items=[(None, word('formless', 'form')), ('Form, plus less', tiles(('form: shape', True), ('less: without', False))),
   ('Formless means', '<div class="build"><span class="tile">formless</span><b>➜</b><span class="tile m">without a shape 🌫️</span></div>'),
   ("That's my match", '<div class="say">✅ That’s my match!</div>')]),
 dict(at='Read the Remember box', items=[(None, '<div class="say">📌 Read the Remember box.</div>'),
   ('Then tap a word', '<div class="build"><span class="tile">👆 a word</span><b>➜</b><span class="tile m">👆 its meaning</span></div>')]),
])
V['g3ela-26-2-teach-vocab'] = dict(title='Vocabulary', sub='Match each word', scenes=[
 dict(at=None, items=[(None, '<div class="lab">A strong word from Chapter 5</div>'), ('Beastly.', '<div class="huge">beastly</div>')]),
 dict(at='Peter says', items=[(None, '<div class="quote">You’ve been perfectly <b class="hl">beastly</b> to Lu.<small>Peter, Chapter 5</small></div>'),
   ('Acting like a beast', '<div class="say">acting like a beast? 🐺 ➜ very mean!</div>')]),
 dict(at='Now tap a word', items=[(None, '<div class="build"><span class="tile">👆 a word</span><b>➜</b><span class="tile m">👆 its meaning</span></div>'),
   ('Match all four', '<div class="say">Match all four ✅✅✅✅</div>')]),
])
V['g3ela-26-2-teach-gram'] = dict(title='Grammar', sub='Find the verb that slipped', scenes=[
 dict(at=None, items=[(None, '<div class="ask">🌀 Which verb slipped?</div>'),
   ('Susan looked inside', '<div class="quote">Susan <b class="hl">looked</b> inside and <b class="hl">sees</b> only coats.</div>')]),
 dict(at='Looked is past', items=[(None, '<div class="say">looked = past ⏪ · sees = now ▶️</div>'), ('It should be saw', '<div class="swap"><s>sees</s> ➜ <b>saw</b></div>')]),
 dict(at='Find the slipped verb', items=[(None, '<div class="say">🔍 Find the slipped verb in each sentence.</div>'),
   ('tap Now check your thinking', PILL('Now check your thinking')), ('Then fix the paragraph', '<div class="say">✏️ Then fix the paragraph.</div>')]),
])
V['g3ela-26-2-teach-spell'] = dict(title='Spelling', sub='Beat detective', scenes=[
 dict(at=None, items=[(None, '<div class="lab">🔎 Beat detective time!</div>'),
   ('Which word has two beats', '<div class="chips"><span>wardrobe</span><span>lamp</span><span>enchanted</span></div>')]),
 dict(at='Clap them', items=[(None, '<div class="say">👏 Clap them!</div>'), ('Ward, robe', '<div class="say">ward · robe 👏👏</div>'),
   ('Lamp: one', '<div class="say">lamp 👏</div>'), ('En, chant, ed', '<div class="say">en · chant · ed 👏👏👏</div>'), ('Wardrobe it is', '<div class="say">✅ wardrobe</div>')]),
 dict(at='Read the rule', items=[(None, '<div class="say">📌 Read the rule.</div>'), ('Then in each row', '<div class="say">👆 In each row, tap the word that matches.</div>')]),
])
V['g3ela-26-2-teach-rwm'] = dict(title='Read Like a Writer', sub='Reader, writer, mimic', scenes=[
 dict(at=None, items=[(None, '<div class="lab">A different sentence from Chapter 5</div>'),
   ('Edmund, who was becoming', '<div class="quote">Edmund, <b class="hl">who was becoming a nastier person every minute</b>, thought that he had scored a great success.<small>Chapter 5</small></div>')]),
 dict(at='Part one', items=[(None, '<div class="step1"><i>1</i>Read like a reader</div>'), ('Edmund thinks he won', '<div class="say">Edmund thinks he won 🏆 … but he hurt Lucy 💔</div>')]),
 dict(at='Part two', items=[(None, '<div class="step1"><i>2</i>Read like a writer</div>'), ('Lewis tucks a fact', '<div class="say">A fact about Edmund, tucked in the middle with <b class="gold">who</b></div>')]),
 dict(at='Part three', items=[(None, '<div class="step1"><i>3</i>Mimic</div>'),
   ("Here's mine", '<div class="quote mine">Opti, <b class="hl">who was getting sleepier every minute</b>, thought that one more chapter would do.<small>Opti’s sentence</small></div>')]),
 dict(at="Now it's your turn", items=[(None, '<div class="say">Now you: the sentence about Edmund being tired 😴</div>'),
   ('Write one sentence', '<div class="boxes"><span class="slot">Reader</span><span class="slot">Writer</span><span class="slot">Mimic</span></div>')]),
])
V['g3ela-26-3-teach-morph'] = dict(title='Morphology', sub='Build the word', scenes=[
 dict(at=None, items=[(None, '<div class="lab">🧱 Snap the parts together</div>'), ('Form.', tiles(('form', True))), ('At.', tiles(('form', True), ('at', False))), ('Format!', '<div class="huge">format</div>')]),
 dict(at='The format of a page', items=[(None, '<div class="def"><b>📄 format</b><span>the shape of a page: where the title and words go</span></div>')]),
 dict(at='Say each pair', items=[(None, '<div class="say">🗣️ Say each pair of parts out loud.</div>'),
   ('Type the whole word', '<div class="build"><span class="tile">re</span><b>+</b><span class="tile">form</span><b>=</b><span class="tile"><i class="blank"></i></span></div>'),
   ('Then tap Check My Answers', PILL('Check My Answers'))]),
])
V['g3ela-26-3-teach-vocab'] = dict(title='Vocabulary', sub='Pick the word that fits', scenes=[
 dict(at=None, items=[(None, '<div class="say">Try each word in the blank. Keep the one that makes sense.</div>')]),
 dict(at="Here's my sentence", items=[(None, '<div class="quote">Edmund gave Lucy a <i class="blank"></i> look, as if he were much older.</div>'),
   ('Beastly?', '<div class="say">beastly? 🤔 no</div>'), ('Superior? Yes', '<div class="say">superior? ✅</div>')]),
 dict(at='Now pick the word', items=[(None, '<div class="say">👆 Pick the word that fits each sentence.</div>')]),
])
V['g3ela-26-3-teach-gram'] = dict(title='Grammar', sub='Move it into the past', scenes=[
 dict(at=None, items=[(None, '<div class="lab">⏪ Move a sentence into the past</div>'),
   ('The children run upstairs', '<div class="quote">The children <b class="hl">run</b> upstairs and <b class="hl">hide</b> in the wardrobe.</div>')]),
 dict(at='Run becomes ran', items=[(None, '<div class="swap"><s>run</s> ➜ <b>ran</b></div>'), ('Hide becomes hid', '<div class="swap"><s>hide</s> ➜ <b>hid</b></div>'),
   ('The children ran upstairs', '<div class="quote">The children <b class="hl">ran</b> upstairs and <b class="hl">hid</b> in the wardrobe.</div>')]),
 dict(at='Read the before and after', items=[(None, '<div class="say">📖 Read the before and after.</div>'), ('Then rewrite', '<div class="say">✏️ Rewrite the two sentences in the past.</div>')]),
])
V['g3ela-26-3-teach-spell'] = dict(title='Spelling', sub='Split it into chunks', scenes=[
 dict(at=None, items=[(None, '<div class="lab">✂️ Split a long word into chunks</div>'), ('Professor.', '<div class="huge">Professor</div>')]),
 dict(at='Pro, fes, sor', items=[(None, '<div class="say">pro · fes · sor</div>'), ('Three chunks', '<div class="big">👏👏👏</div>'),
   ('push them back together', '<div class="huge">Professor ✅</div>')]),
 dict(at='Read the rule', items=[(None, '<div class="say">📌 Read the rule.</div>'), ('Then say each word in chunks', '<div class="say">👆 Say it in chunks, then tap the card.</div>')]),
])
V['g3ela-26-4-teach-morph'] = dict(title='Morphology', sub='Roll and explain', scenes=[
 dict(at=None, items=[(None, '<div class="ask">⚡ Quick! What does form mean?</div>'), ('Shape!', '<div class="build"><span class="tile key">form</span><b>=</b><span class="tile">shape</span></div>')]),
 dict(at="Here's a word", items=[(None, word('landform', 'form')), ('A landform is', '<div class="def"><b>landform</b><span>a shape of the land, like a hill or a valley ⛰️</span></div>')]),
 dict(at='Now tap Roll the Dice', items=[(None, PILL('🎲 Roll the Dice')), ('Say what each word means', '<div class="say">🗣️ Say what the word means.</div>'), ('tap Check My Thinking', PILL('Check My Thinking'))]),
])
V['g3ela-26-4-teach-vocab'] = dict(title='Vocabulary', sub='Use a word to tell the story', scenes=[
 dict(at=None, items=[(None, '<div class="lab">✍️ Here’s how I’d use a word</div>'), ('Superior.', '<div class="huge">superior</div>')]),
 dict(at='Edmund gave Lucy a superior look', items=[(None, '<div class="quote mine">Edmund gave Lucy a <b class="hl">superior</b> look when he said they were only pretending.<small>Opti’s sentence</small></div>'),
   ('One word, one moment', '<div class="say">1 word + 1 moment 📖</div>')]),
 dict(at='Now choose one', items=[(None, '<div class="say">✏️ Choose one of your words. Write a sentence about Chapters 4 to 6.</div>')]),
])
V['g3ela-26-4-teach-gram'] = dict(title='Grammar', sub='Three passes', scenes=[
 dict(at=None, items=[(None, '<div class="lab">✏️ Three passes, like an editor</div>'), ('Lucy said the queen', '<div class="quote">Lucy said the queen was terrible and edmund feels sick</div>')]),
 dict(at='Pass one', items=[(None, '<div class="step1"><i>1</i>Capitals</div>'), ('Queen and Edmund', '<div class="quote">Lucy said the <b class="hl">Q</b>ueen was terrible and <b class="hl">E</b>dmund feels sick</div>')]),
 dict(at='Pass two', items=[(None, '<div class="step1"><i>2</i>Verbs</div>'), ('feels slipped', '<div class="swap"><s>feels</s> ➜ <b>felt</b></div>')]),
 dict(at='Pass three', items=[(None, '<div class="step1"><i>3</i>Commas</div>'), ('a comma before and', '<div class="quote">Lucy said the Queen was terrible<b class="hl">,</b> and Edmund felt sick.</div>')]),
 dict(at='Now do your passes', items=[(None, '<div class="say">👆 Tap every word that needs fixing.</div>')]),
])
V['g3ela-26-4-teach-spell'] = dict(title='Spelling', sub='Academic word dice', scenes=[
 dict(at=None, items=[(None, '<div class="lab">🎲 Here’s my roll</div>'), ('Inquisitive.', '<div class="huge">inquisitive</div>'), ('In, quis, i, tive', '<div class="say">in · quis · i · tive</div>')]),
 dict(at='Four beats', items=[(None, '<div class="big">👏👏👏👏</div>'), ('How did I know', '<div class="say">4 vowel sounds = 4 beats 👂</div>')]),
 dict(at='Tap Roll the dice', items=[(None, PILL('🎲 Roll the dice')), ('split the word out loud', '<div class="say">🗣️ Split it. Say how you knew.</div>'), ('Then tap Check my answer', PILL('Check my answer'))]),
])
