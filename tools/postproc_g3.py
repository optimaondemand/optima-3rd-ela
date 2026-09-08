# -*- coding: utf-8 -*-
"""Clean the extracted G3 JSON: unescape entities, strip markup left in titles,
and fill the fields the shared extractor doesn't know about in G3 files."""
import json,re,io,html,os,glob

SRC='/mnt/user-data/uploads/optima-3rd-ela'
def clean(t):
    if not isinstance(t,str): return t
    t=re.sub(r'^.*?activity-title"[^>]*>','',t)
    t=t.rstrip('<')
    t=re.sub(r'<[^>]+>','',t)
    return html.unescape(t).strip()

d=json.load(open('lesson_data.json'))
L=d['lessons'] if isinstance(d,dict) and 'lessons' in d else d
rows=L if isinstance(L,list) else list(L.values())
for x in rows:
    f=glob.glob(os.path.join(SRC,'lesson-%d-%d-*.html'%(x['week'],x['day'])))[0]
    s=io.open(f,encoding='utf-8').read()
    for k in ['ch_range','morph_title','spell_title','grammar_title','dol_fix','dol_fix2','dol_ans','dol_ans2','dol_errors','big_question']:
        if k in x: x[k]=clean(x[k])
    for v in x.get('vocab',[]):
        v['word']=clean(v['word']); v['def']=clean(v['def'])
    for g in x.get('grammar',[]):
        g['sentence']=clean(g['sentence']); g['answer']=clean(g['answer'])
    x['spell_groups']={clean(k):[clean(w) for w in v] for k,v in x.get('spell_groups',{}).items()}
    # What Good Readers Do: first paragraph of that activity
    m=re.search(r'📚 What Good Readers Do.*?<div class="activity-body">\s*<p>(.*?)</p>',s,re.S)
    if m: x['wgrd']=clean(m.group(1))
    # Big question / socratic prompt
    m=re.search(r'class="socratic-q"[^>]*>(.*?)</p>',s,re.S)
    if m and not x.get('big_question'): x['big_question']=clean(m.group(1))
    # Writer's Workshop stage + subtitle
    m=re.search(r"Writer&rsquo;s Workshop:\s*Week\s*\d+\s*&middot;\s*([A-Z ]+)</div>\s*<div[^>]*>(.*?)</div>",s,re.S)
    if m:
        x['writing']={'stage':clean(m.group(1)),'subtitle':clean(m.group(2)),'prompt':''}
    # Copywork passage (useful on the reading slide)
    m=re.search(r'class="copywork-text">(.*?)</div>',s,re.S)
    if m: x['copywork']=clean(m.group(1))
    # Pause questions
    x['pause_qs']=[clean(q) for q in re.findall(r'class="pause-q"[^>]*>(.*?)</div>',s,re.S)][:3] or x.get('pause_qs',[])
json.dump(d,open('lesson_data.json','w'),ensure_ascii=False,indent=1)
print('post-processed',len(rows),'lessons')
