"""Week 23 (Medieval Nonfiction) accuracy + wording fixes (approved by Bethany Nov 14 2026, all 20 in claude/g3-ela-wk23-audit.md). Run once on the pre-sparkle files."""
OBJ_OLD = ('        <div class="obj-line"><span class="obj-icon">📖</span><span><strong>Reading:</strong> I will identify central idea and relevant details.</span></div>\n'
           '        <div class="obj-line"><span class="obj-icon">✏️</span><span><strong>Grammar:</strong> I will study capitalization of titles, names, and places.</span></div>\n'
           '        <div class="obj-line"><span class="obj-icon">🔤</span><span><strong>Spelling:</strong> I will practice VCCV syllable division.</span></div>\n')
def ol(icon, k, t): return '        <div class="obj-line"><span class="obj-icon">%s</span><span><strong>%s:</strong> %s</span></div>\n' % (icon, k, t)
OBJ = {
 1: [('📖','Reading','I will find the central idea of an article and two details that support it.'),
     ('🌱','Word parts','I will use trans- (across) to work out what a word means.'),
     ('✏️','Grammar','I will sort names of people, places and titles that get capital letters.'),
     ('🔤','Spelling','I will split VCCV words between the two consonants.'),
     ('✍️','Writing','I will choose one medieval topic to explain.')],
 2: [('📖','Reading','I will find the central idea of each paragraph and of the whole article.'),
     ('🌱','Word parts','I will match trans- words to their meanings.'),
     ('✏️','Grammar','I will find every word in a name or title that needs a capital.'),
     ('🔤','Spelling','I will hear and find the word that splits between two consonants.'),
     ('✍️','Writing','I will write a research question and take notes from two articles.')],
 3: [('📖','Reading','I will explain the central idea and why the author wrote the article.'),
     ('🌱','Word parts','I will build trans- words from their parts.'),
     ('✏️','Grammar','I will count the capitals a sentence needs.'),
     ('🔤','Spelling','I will split longer VCCV words.'),
     ('✍️','Writing','I will plan a paragraph: topic sentence, two details, closing.')],
 4: [('📖','Reading','I will compare two groups in an article using details.'),
     ('🌱','Word parts','I will explain how trans- changes a word.'),
     ('✏️','Grammar','I will find capital-letter mistakes, or say there are none.'),
     ('🔤','Spelling','I will split VCCV words and use them in sentences.'),
     ('✍️','Writing','I will write my topic sentence and a detail.')],
}
VOC = ("<div class=\"activity-sub\">Words from this week's chapters.</div>", "<div class=\"activity-sub\">Words from this week's articles.</div>")
QS_OLD = ('  <div class="quote-strip-text">&ldquo;%s&rdquo;</div>\n  <div class="quote-strip-attr">&mdash; Medieval Nonfiction Extension</div>')
QS_NEW = ('  <div class="quote-strip-text">&ldquo;%s&rdquo;</div>\n  <div class="quote-strip-attr">&mdash; &ldquo;%s&rdquo;</div>')
QS = {
 1: ('King Henry lived in the Tower of London during the Middle Ages.', 'A medieval castle was not just a home &mdash; it was a fortress, a workplace, and a whole community.', 'Life in a Medieval Castle'),
 2: ('In medieval England, an apprentice might work for Master Thomas for seven years.', 'In the Middle Ages, most children did not go to school. Instead, they learned by working.', 'Servants and Apprentices'),
 3: ('Duke Richard of York bowed before Queen Margaret at the court of Westminster.', 'A royal court was more than just a king and a throne.', 'Royal Courts: Power and Protocol'),
 4: ('At the feast of Saint George, Lord Pembroke served roasted boar and French wine.', 'Most ordinary people ate very differently. Their main food was bread.', 'What Did Medieval People Eat?'),
}
def ALL(d):
    return [(OBJ_OLD, ''.join(ol(*x) for x in OBJ[d])), VOC,
            (QS_OLD % QS[d][0], QS_NEW % (QS[d][1], QS[d][2]))]
def chip(g, w): return '<span class="sort-chip" data-group="%s" onclick="pickSortChip(this)">%s</span>' % (g, w)
SORT_OLD = ''.join(chip(g, w) for g, w in [('a','turret'),('b','castle'),('a','tunnel'),('b','table'),('a','mortar'),('b','little'),('a','helmet'),('b','simple')])
SORT_NEW = ''.join(chip(g, w) for g, w in [('a','turret'),('b','noble'),('a','tunnel'),('b','table'),('a','mortar'),('b','bugle'),('a','helmet'),('b','title')])
R = {
 'lesson-23-1-med.html': ALL(1) + [
  ('The king or lord lived in the strongest part of the castle, called the keep.', 'The king or lord often lived in the strongest part of the castle, called the keep.'),
  ('Hundreds of people worked inside the castle walls every day.', 'Many people worked inside the castle walls every day.'),
  ('<p class="socratic-q">The article mentions pages — young boys training to be knights. How does this connect to what you know from <em>The Whipping Boy</em>?</p>',
   '<p class="socratic-q">A page was a young boy training to be a knight. How was Jemmy&rsquo;s job in the castle in <em>The Whipping Boy</em> different?</p>'),
  (SORT_OLD, SORT_NEW),
 ],
 'lesson-23-2-med.html': ALL(2) + [
  ("<p style='margin:0 0 12px 0;'>Girl children often worked", "<p style='margin:0 0 12px 0;'>Girls often worked"),
  ('For most medieval children, work began very early in life — often by age seven or eight.', 'For most medieval children, work began early in life. Many helped at home or in the fields by age seven or eight.'),
  ('The article says most children began work by age seven or eight.', 'The article says many children helped with work by age seven or eight.'),
  ('<div class="decode-sentence">"A boy who wanted to learn a trade became an apprentice."</div>',
   '<div class="decode-sentence">"A boy who wanted to learn a trade — like blacksmithing, baking, or carpentry — became an apprentice."</div>'),
  ('<div class="match-item is-word" data-match="D" onclick="morphMatchClick(this)">transfer</div>\n<div class="match-item" data-match="D" onclick="morphMatchClick(this)">to carry across to another place</div>',
   '<div class="match-item is-word" data-match="D" onclick="morphMatchClick(this)">transplant</div>\n<div class="match-item" data-match="D" onclick="morphMatchClick(this)">to dig up a plant and plant it somewhere new</div>'),
  ('Work often began by age seven or eight.</div>', 'Many helped with work by age seven or eight.</div>'),
  ('<span class="spotter-word" onclick="gramSpotAll(this,\'gspot3\')" data-correct="false">the</span> <span class="spotter-word" onclick="gramSpotAll(this,\'gspot3\')" data-correct="true">canterbury</span>',
   '<span class="spotter-word" onclick="gramSpotAll(this,\'gspot3\')" data-correct="true">the</span> <span class="spotter-word" onclick="gramSpotAll(this,\'gspot3\')" data-correct="true">canterbury</span>'),
 ],
 'lesson-23-3-med.html': ALL(3) + [
  ('lord henry of cornwall knelt before king james at the palace of windsor.', 'lord henry of cornwall knelt before king james at windsor castle.'),
  ('<strong>Corrected:</strong> Lord Henry of Cornwall knelt before King James at the Palace of Windsor.</p>', '<strong>Corrected:</strong> Lord Henry of Cornwall knelt before King James at Windsor Castle.</p>'),
  ('capital P, W on Palace of Windsor (proper place name)', 'capital W, C on Windsor Castle (proper place name)'),
  ('In The Whipping Boy, the prince breaks rule after rule, and for most of the book his whipping boy takes the punishment.',
   'At the start of The Whipping Boy, the prince breaks rule after rule, and Jemmy takes the punishment.'),
  ('id="gfill1" data-answer="5"', 'id="gfill1" data-answer="4"'),
  ('id="gfill2" data-answer="5"', 'id="gfill2" data-answer="4"'),
  ('id="gfill4" data-answer="4"', 'id="gfill4" data-answer="3"'),
  ('Grammar: Capitalization: Historical Eras and Institutions</div>', 'Grammar: Capitalization: Count the Capitals</div>'),
  ('<p>Today we practice capitalizing historical eras (Middle Ages), institutions (the Court of Westminster), and titles used as names (Your Majesty).</p>',
   '<p>Today you count the capitals a sentence needs: one for the first word, and one for every word in a name or title.</p>'),
  ('Detail 2:</strong> Poor children began as young as age 7.', 'Detail 2:</strong> Many children helped with work by age 7.'),
 ],
 'lesson-23-4-med.html': ALL(4) + [
  ('Wealthy nobles drank wine from silver goblets and ate off pewter plates.', 'Wealthy nobles drank wine from silver goblets. Many ate from pewter plates or from thick slices of bread called trenchers.'),
  ("<p>In The Whipping Boy, Prince Brat's basket contains a feast. Jemmy thinks about the food. What might that basket have contained — and why would it matter so much to Jemmy?</p>",
   "<p>In The Whipping Boy, the prince runs away with a basket of food from the king's table. What do you remember was inside?</p>"),
  ("Think about the basket in The Whipping Boy. Based on today's article, what foods were probably in it, and why would Jemmy — a street boy — react to it the way he did?",
   "In Chapter 6 of The Whipping Boy, the outlaws open the prince's basket and find meat pies, fruit tarts and roast pheasant. Jemmy is happy to eat bread and herring. Use today's article to explain why the two boys ate so differently."),
  ('placeholder="The basket probably contained... Jemmy reacted the way he did because..."', 'placeholder="The prince ate... because... Jemmy ate... because..."'),
  ('<p>Today you write your own sentences about medieval life using correct capitalization — names, titles, places, and historical eras.</p>',
   '<p>Today you hunt for capital-letter mistakes in names, titles and places. Some sentences have none.</p>'),
 ],
}
if __name__ == '__main__':
    import sys
    dry = '--apply' not in sys.argv
    for f, reps in R.items():
        s = open(f, encoding='utf-8', newline='').read()
        o = s.count('<div') - s.count('</div')
        for r in reps:
            old, new = r[0], r[1]; n = r[2] if len(r) > 2 else 1
            c = s.count(old)
            assert c == n, (f, c, old[:110])
            s = s.replace(old, new)
        assert s.count('<div') - s.count('</div') == o, f
        if not dry: open(f, 'w', encoding='utf-8', newline='').write(s)
        print('ok' if not dry else 'dry-ok', f, len(reps))
