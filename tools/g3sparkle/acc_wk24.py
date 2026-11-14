"""Week 24 (Medieval Nonfiction, part 2) accuracy + wording fixes (approved by Bethany Nov 14 2026, claude/g3-ela-wk24-audit.md
findings 2-13, 15, 17-18). Finding 1 (Quick Match keys) is acc2_wk24.py. Findings 14, 16, 19 are wording, in plain_wk24.py.
Findings 20-23 (check-in) live in the quiz JSON (checkin_wk24.py). Run once on the pre-sparkle files."""
OBJ_OLD = ('        <div class="obj-line"><span class="obj-icon">📖</span><span><strong>Reading:</strong> I will explain chronology, comparison, and cause/effect.</span></div>\n'
           '        <div class="obj-line"><span class="obj-icon">✏️</span><span><strong>Grammar:</strong> I will study main idea and details in paragraphs.</span></div>\n'
           '        <div class="obj-line"><span class="obj-icon">🔤</span><span><strong>Spelling:</strong> I will <em>%s</em> %s</span></div>\n')
SPELL_OBJ = {1: ('define', 'what -ful, -less, -ness and -ly each do to a base word.'), 2: ('identify', 'which of the four endings a word uses by the job it does.'),
             3: ('break apart', 'a word into its base and its ending, and name the ending’s job.'), 4: ('explain', 'why a base word takes one ending rather than another.')}
def ol(icon, k, t): return '        <div class="obj-line"><span class="obj-icon">%s</span><span><strong>%s:</strong> %s</span></div>\n' % (icon, k, t)
OBJ = {
 1: [('📖','Reading','I will find a cause and its effect in an article about building castles.'),
     ('🌱','Word parts','I will use script and scribe (write) to build words.'),
     ('✏️','Grammar','I will sort sentences: main idea, detail, or off the topic.'),
     ('🔤','Spelling','I will sort words by what -ful, -less, -ness and -ly do.'),
     ('✍️','Writing','I will draft my whole expository paragraph.')],
 2: [('📖','Reading','I will tell the steps to becoming a knight in order.'),
     ('🌱','Word parts','I will match script and scribe words to their meanings.'),
     ('✏️','Grammar','I will find the main idea sentence in a paragraph.'),
     ('🔤','Spelling','I will find the word that uses a named ending.'),
     ('✍️','Writing','I will revise my paragraph so every sentence fits my topic.')],
 3: [('📖','Reading','I will use the author&rsquo;s details to picture a medieval town.'),
     ('🌱','Word parts','I will build script and scribe words from their parts.'),
     ('✏️','Grammar','I will name the topic a set of details is about.'),
     ('🔤','Spelling','I will break words into a base word and an ending.'),
     ('✍️','Writing','I will edit my paragraph for capitals and periods.')],
 4: [('📖','Reading','I will tell what is real and what is made up in stories about the Middle Ages.'),
     ('🌱','Word parts','I will explain how script and scribe change a word.'),
     ('✏️','Grammar','I will find a sentence that is off the topic, or say there is none.'),
     ('🔤','Spelling','I will choose an ending for a word and say why.'),
     ('✍️','Writing','I will publish my paragraph and think about what I did well.')],
}
VOC = ("<div class=\"activity-sub\">Words from this week's chapters.</div>", "<div class=\"activity-sub\">Words from this week's articles.</div>")
QS_OLD = ('  <div class="quote-strip-text">&ldquo;%s&rdquo;</div>\n  <div class="quote-strip-attr">&mdash; Medieval Nonfiction Extension</div>')
QS_NEW = ('  <div class="quote-strip-text">&ldquo;%s&rdquo;</div>\n  <div class="quote-strip-attr">&mdash; &ldquo;%s&rdquo;</div>')
QS = {
 1: ('The workers at Windsor Castle used over one million stones to build the outer walls.', 'Castles were built for defense.', 'How Castles Were Built'),
 2: ('Sir William of Bath was dubbed a knight by King Edward at Windsor Castle.', 'Becoming a knight took years of training.', 'Knights: Warriors and Gentlemen'),
 3: ('In the market town of Shrewsbury, merchants from France sold silk and spices every Thursday.', 'Towns were the centers of trade and news in the medieval world.', 'Medieval Towns: Busy, Smelly, and Alive'),
 4: ('Historians debate whether whipping boys really existed in the courts of England and France.', 'Stories borrow from history but add imagination.', 'Real vs. Imagined: The Middle Ages in Stories'),
}
def ALL(d):
    return [(OBJ_OLD % SPELL_OBJ[d], ''.join(ol(*x) for x in OBJ[d])), VOC,
            (QS_OLD % QS[d][0], QS_NEW % (QS[d][1], QS[d][2]))]
def hw(tip, t): return '<span class="dol-highlight-word" onclick="dolHighlight(this,\'%s\')">%s</span>' % (tip, t)
DOL1_OLD = (hw('The main idea of the sentence — who it is about.', 'The workers') + ' at ' + hw('The name of a particular castle — both words capitalized.', 'Windsor Castle') +
            ' used over ' + hw('A supporting detail — it tells how many.', 'one million stones') + ' to build the outer ' + hw('A period ends the sentence.', 'walls.'))
DOL1_NEW = (hw('Capital T: the first word of the sentence.', 'The workers') + ' at ' + hw('The name of one real castle — both words get capitals.', 'Dover Castle') +
            ' built a great tower for ' + hw('A title and a name: King gets a capital right before Henry.', 'King Henry II') + hw('A period ends the sentence.', '.'))
OFF = [('The prince had blue eyes.', 'My dog has brown spots.'), ('Jemmy liked the smell of bread.', 'I like the smell of bread.')]
R = {
 'lesson-24-1-med.html': ALL(1) + [
  (DOL1_OLD, DOL1_NEW),
  ('the stonemasons at dover castle spent thirty years to complete the inner tower.', 'the stonemasons at harlech castle built the walls for king edward.'),
  ('<strong>Corrected:</strong> The stonemasons at Dover Castle spent thirty years to complete the inner tower.</p>', '<strong>Corrected:</strong> The stonemasons at Harlech Castle built the walls for King Edward.</p>'),
  ('Capital T on The (starts the sentence); capital D on Dover and capital C on Castle (proper name of a specific castle); period ends.',
   'Capital T on The (starts the sentence); capital H on Harlech and capital C on Castle (the name of one castle); capital K on King (title right before a name); capital E on Edward; period ends.'),
  ('It could take ten to thirty years to complete a large stone castle.', 'A large stone castle could take many years to finish, and some took more than thirty.'),
  ('The walls were thick — sometimes up to ten feet wide — to withstand attack.', 'The walls were thick — often ten feet or more — to withstand attack.'),
  ('Building a large castle could take 10–30 years.', 'Building a large castle could take many years.'),
  ('an off-topic sentence does neither.</p>', 'an off-topic sentence does neither. The paragraphs are about guilds, castle jobs and travel.</p>'),
 ] + OFF,
 'lesson-24-2-med.html': ALL(2) + [
  ('lady anne of salisbury was honored a countess by queen victoria at buckingham palace.', 'lady anne of salisbury was made a countess by queen eleanor at the tower of london.'),
  ('<strong>Corrected:</strong> Lady Anne of Salisbury was honored a countess by Queen Victoria at Buckingham Palace.', '<strong>Corrected:</strong> Lady Anne of Salisbury was made a countess by Queen Eleanor at the Tower of London.'),
  ('capital V on Victoria (proper name); capital B, P on Buckingham Palace (proper place name)', 'capital E on Eleanor (proper name); capital T, L on Tower of London (proper place name; of stays small)'),
  ('How long does the whole process take, based on the clues in the text?', 'What clue in the article tells you how old a boy was when he became a squire?'),
 ],
 'lesson-24-3-med.html': ALL(3) + [
  ('Waste was thrown out of windows.', 'Waste was often thrown into the streets.'),
  ('and barbers also acted as doctors. Towns were', 'and barbers also pulled teeth and treated cuts. Craftsmen in the same trade formed groups called guilds to set prices and protect their work. Towns were'),
 ],
 'lesson-24-4-med.html': ALL(4) + [
  ('"Historians debate whether whipping boys actually existed."</div>', '"Whipping boys may or may not have actually existed — historians debate this."</div>'),
  ('Where do the two consonants split?</p>', 'Which ending did you pick, and why?</p>'),
  ('The paragraph is about castle jobs, not what he looked like.</p>', 'The paragraph is about castle jobs, not about a dog.</p>'),
  ('The paragraph is about what guilds controlled.</p>', 'The paragraph is about what guilds controlled, not what I like.</p>'),
  ('The prince had blue eyes.', 'My dog has brown spots.', 2), ('Jemmy liked the smell of bread.', 'I like the smell of bread.', 2),
 ],
}
if __name__ == '__main__':
    import sys
    dry = '--apply' not in sys.argv
    d = sys.argv[sys.argv.index('--dir') + 1] + '/' if '--dir' in sys.argv else ''
    for f, reps in R.items():
        s = open(d + f, encoding='utf-8', newline='').read()
        o = s.count('<div') - s.count('</div')
        for r in reps:
            old, new = r[0], r[1]; n = r[2] if len(r) > 2 else 1
            c = s.count(old)
            assert c == n, (f, c, old[:110])
            s = s.replace(old, new)
        assert s.count('<div') - s.count('</div') == o, f
        if not dry: open(d + f, 'w', encoding='utf-8', newline='').write(s)
        print('ok' if not dry else 'dry-ok', f, len(reps))
