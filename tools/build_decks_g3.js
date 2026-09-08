// OAO G3 Despereaux teacher decks, Weeks 9-16.
// Brand system and slide grammar follow the oao-ela-slides skill. The skill's
// lesson_helpers.js is truncated mid-file (349 lines, ends inside morphSlide,
// no module.exports), so the builders below are implemented here.
const fs = require('fs');
const PptxGenJS = require('pptxgenjs');

const C = { navy:'0E1C42', cyan:'55C8E8', cyanLight:'E5F7FC', gold:'C7922C', goldLight:'FEF6E8',
  green:'34B76F', greenLight:'E8F8EF', purple:'8B6FC0', purpleLight:'F0E8FF', white:'FFFFFF',
  offWhite:'F8FAFC', gray:'64748B', darkGray:'1E293B' };
const F = 'Calibri';
const mkSh = () => ({ type:'outer', color:'000000', blur:8, offset:3, angle:45, opacity:0.12 });
const NC = { primary:'3D1A6B', accent:'8B6FC0', emoji:'🐭', virtue:'Courage' };

function initPres(){ const p=new PptxGenJS(); p.layout='LAYOUT_16x9'; p.author='Optima Academy Online'; return p; }
function base(pres,title,accent,bg){
  const s=pres.addSlide(); s.background={color:bg||C.white};
  s.addShape(pres.ShapeType.rect,{x:0,y:0,w:10,h:0.62,fill:{color:accent||NC.accent}});
  s.addText(title,{x:0.4,y:0.06,w:9.2,h:0.5,fontSize:22,bold:true,fontFace:F,color:C.white,valign:'middle',margin:0});
  return s;
}
const cSlide=(p,t,a)=>base(p,t,a,C.white);
const iSlide=(p,t,a)=>base(p,t,a,C.offWhite);
function card(s,pres,x,y,w,h,fill){ s.addShape(pres.ShapeType.roundRect,{x,y,w,h,fill:{color:fill||C.offWhite},rectRadius:0.1,shadow:mkSh()}); }
function lbl(s,text,x,y,color){ s.addText(text,{x,y,w:9,h:0.26,fontSize:11,bold:true,fontFace:F,color:color||C.gray,charSpacing:1,margin:0}); }
function qBox(s,pres,text,x,y,w,h,fill,tc,bc){
  s.addShape(pres.ShapeType.roundRect,{x,y,w,h,fill:{color:fill||C.cyanLight},rectRadius:0.1,line:{color:bc||C.cyan,width:1.5},shadow:mkSh()});
  s.addText(text,{x:x+0.25,y:y+0.14,w:w-0.5,h:h-0.28,fontSize:17,fontFace:F,color:tc||C.darkGray,wrap:true,valign:'middle',margin:0});
}
const clip=(t,n)=>{ t=(t||'').toString(); return t.length>n? t.slice(0,n-1)+'…' : t; };

function titleSlide(pres,d){
  const s=pres.addSlide(); s.background={color:NC.primary};
  s.addText(NC.emoji,{x:0,y:0.9,w:10,h:0.9,fontSize:52,align:'center',margin:0});
  s.addText('The Tale of Despereaux',{x:0.5,y:1.85,w:9,h:0.62,fontSize:34,bold:true,fontFace:F,color:C.white,align:'center',margin:0});
  s.addText(`Lesson ${d.week}.${d.day}${d.ch_range?'  ·  '+d.ch_range:''}`,{x:0.5,y:2.55,w:9,h:0.45,fontSize:20,fontFace:F,color:NC.accent,align:'center',margin:0});
  s.addText(`Grade 3 ELA  ·  Virtue: ${NC.virtue}`,{x:0.5,y:3.15,w:9,h:0.35,fontSize:14,fontFace:F,color:'C9BCE4',align:'center',margin:0});
  s.addNotes(`Lesson ${d.week}.${d.day}. Reading: ${d.ch_range}.`);
}
function tmwPromptSlide(pres,d){
  const s=cSlide(pres,'✍️  10-Minute Write',C.gold);
  lbl(s,'READ THE PROMPT — 1 MINUTE',0.4,0.9,C.gold);
  qBox(s,pres,d.tmw.prompt,0.4,1.25,9.2,1.9,C.goldLight,C.darkGray,C.gold);
  s.addText('Think first. You will have five minutes to write.',{x:0.4,y:3.35,w:9.2,h:0.4,fontSize:16,italic:true,fontFace:F,color:C.gray,margin:0});
  s.addNotes('Read the prompt aloud. Give students a moment to think before writing.');
}
function tmwWriteSlide(pres,d){
  const s=base(pres,'✍️  Writing Time',C.gold,C.goldLight);
  s.addText('5 minutes — keep your pencil moving!',{x:0.4,y:0.95,w:9.2,h:0.55,fontSize:26,bold:true,fontFace:F,color:C.navy,margin:0});
  lbl(s,'YOUR PROMPT',0.4,1.6,C.gold);
  qBox(s,pres,d.tmw.prompt,0.4,1.9,9.2,1.55,C.white,C.darkGray,C.gold);
  s.addText('Do not stop to erase. If you get stuck, write the last word again and keep going.',{x:0.4,y:3.6,w:9.2,h:0.4,fontSize:15,italic:true,fontFace:F,color:C.gray,margin:0});
  s.addNotes('Five minutes of sustained writing. Stamina over polish. Do not correct spelling now.');
}
function tmwEditSlide(pres,d){
  const s=base(pres,'🔍  Edit & Revise',C.green,C.greenLight);
  s.addText('1 minute — pick ONE thing to fix.',{x:0.4,y:0.95,w:9.2,h:0.5,fontSize:24,bold:true,fontFace:F,color:C.navy,margin:0});
  lbl(s,"TODAY'S EDIT FOCUS",0.4,1.55,C.green);
  qBox(s,pres,d.tmw.edit_focus,0.4,1.85,9.2,0.85,C.white,C.darkGray,C.green);
  s.addText([{text:'Quick check:  ',options:{bold:true}},{text:'capitals  ·  end punctuation  ·  circle a word you are unsure of  ·  read it aloud'}],
    {x:0.4,y:2.9,w:9.2,h:0.4,fontSize:15,fontFace:F,color:C.darkGray,margin:0});
  s.addNotes('One fix only. Editing is conventions; revision is ideas. Name which one you are asking for.');
}
function tmwShareSlide(pres){
  const s=base(pres,'🗣️  Share Time',C.cyan,C.cyanLight);
  s.addText("3 minutes — let's hear your writing!",{x:0.4,y:1.1,w:9.2,h:0.6,fontSize:26,bold:true,fontFace:F,color:C.navy,margin:0});
  s.addText('Raise your hand  ·  paste it in the chat  ·  or hold your paper up to the camera',{x:0.4,y:1.85,w:9.2,h:0.5,fontSize:17,fontFace:F,color:C.darkGray,margin:0});
  s.addNotes('Two or three volunteers. Praise something specific in each.');
}
function recapSlide(pres,d){
  const s=iSlide(pres,'📖  Today',NC.accent);
  let y=0.85;
  if(d.ch_range){ lbl(s,'READING',0.4,y,C.purple); s.addText(d.ch_range,{x:0.4,y:y+0.26,w:9.2,h:0.4,fontSize:20,bold:true,fontFace:F,color:C.navy,margin:0}); y+=0.8; }
  if(d.big_question){ lbl(s,'BIG QUESTION',0.4,y,C.gold); qBox(s,pres,d.big_question,0.4,y+0.26,9.2,0.8,C.goldLight,C.darkGray,C.gold); y+=1.2; }
  if(d.wgrd){ lbl(s,'READING LENS',0.4,y,C.cyan); s.addText(clip(d.wgrd,300),{x:0.4,y:y+0.26,w:9.2,h:1.0,fontSize:15,fontFace:F,color:C.darkGray,wrap:true,margin:0}); }
  s.addNotes(`Reading lens: ${d.wgrd}`);
}
function dolSlide(pres,d,show){
  const s=iSlide(pres,'✏️  Daily Oral Language',C.cyan);
  lbl(s,'FIX THESE SENTENCES',0.4,0.82,C.cyan);
  qBox(s,pres,d.dol_fix,0.4,1.12,9.2,0.85,C.white,C.darkGray,C.cyan);
  if(d.dol_fix2) qBox(s,pres,d.dol_fix2,0.4,2.05,9.2,0.85,C.white,C.darkGray,C.cyan);
  if(show){
    card(s,pres,0.4,3.0,9.2,1.55,C.greenLight);
    lbl(s,'✅  CORRECTED',0.62,3.08,C.green);
    s.addText([{text:d.dol_ans||'',options:{breakLine:true}},{text:d.dol_ans2||''}],
      {x:0.62,y:3.36,w:8.76,h:0.75,fontSize:14,fontFace:F,italic:true,color:C.darkGray,wrap:true,margin:0});
    if(d.dol_errors) s.addText(d.dol_errors,{x:0.62,y:4.12,w:8.76,h:0.35,fontSize:12,fontFace:F,color:C.gray,wrap:true,margin:0});
  } else {
    s.addText('Rewrite both sentences correctly in your notebook.',{x:0.4,y:3.05,w:9.2,h:0.4,fontSize:16,bold:true,fontFace:F,color:C.navy,margin:0});
  }
  s.addNotes(`Corrected: ${d.dol_ans} ${d.dol_ans2||''}\nLook for: ${d.dol_errors}`);
}
function morphSlide(pres,d){
  if(!d.morph_fillin||!d.morph_fillin.length) return;
  const s=cSlide(pres,'🌱  Morphology',NC.accent);
  lbl(s,(d.morph_title||'WORD PARTS').replace(/^🌱\s*/,'').toUpperCase(),0.4,0.88,C.purple);
  let y=1.2;
  d.morph_fillin.slice(0,4).forEach((it,i)=>{ card(s,pres,0.4,y,9.2,0.68,i%2?'F8F4FF':C.purpleLight);
    s.addText('🌱  '+it,{x:0.65,y:y+0.13,w:8.6,h:0.42,fontSize:15,fontFace:F,color:C.darkGray,wrap:true,valign:'middle',margin:0}); y+=0.76; });
  s.addNotes('Break the word into base + word part. Ask what the part adds to the meaning.');
}
function vocabSlide(pres,d){
  if(!d.vocab||!d.vocab.length) return;
  const s=cSlide(pres,'🔤  Vocabulary',C.cyan);
  lbl(s,"THIS WEEK'S WORDS — FROM THE CHAPTERS YOU ARE READING",0.4,0.88,C.cyan);
  let y=1.2;
  d.vocab.slice(0,4).forEach((v,i)=>{ card(s,pres,0.4,y,9.2,0.72,i%2?C.white:C.cyanLight);
    s.addText([{text:v.word+'  ',options:{bold:true,color:C.navy,fontSize:17}},{text:v.def||'',options:{color:C.darkGray,fontSize:14}}],
      {x:0.65,y:y+0.14,w:8.6,h:0.46,fontFace:F,wrap:true,valign:'middle',margin:0}); y+=0.8; });
  s.addNotes('Each word appears in the chapters read this week, in the author’s own sentence.');
}
function grammarSlide(pres,d,show){
  if(!d.grammar||!d.grammar.length) return;
  const s=iSlide(pres,'✏️  Grammar',C.gold);
  lbl(s,(d.grammar_title||'GRAMMAR').replace(/^✏️\s*Grammar:\s*/,'').toUpperCase(),0.4,0.85,C.gold);
  let y=1.18;
  d.grammar.slice(0,4).forEach((g,i)=>{
    card(s,pres,0.4,y,9.2,0.72,i%2?C.white:C.goldLight);
    if(show && g.answer){
      const parts=g.sentence.split(new RegExp('('+g.answer.replace(/[.*+?^${}()|[\]\\]/g,'\\$&')+')'));
      const runs=parts.filter(p=>p!=='').map(p=> p===g.answer
        ? {text:p,options:{bold:true,color:C.green}} : {text:p,options:{color:C.darkGray}});
      s.addText(runs,{x:0.65,y:y+0.16,w:8.6,h:0.44,fontSize:16,fontFace:F,wrap:true,valign:'middle',margin:0});
    } else {
      s.addText(g.sentence,{x:0.65,y:y+0.16,w:8.6,h:0.44,fontSize:16,fontFace:F,color:C.darkGray,wrap:true,valign:'middle',margin:0});
    }
    y+=0.8;
  });
  s.addText(show?'✅  Answers revealed':'Tap the word that fits the rule.',
    {x:0.4,y:y+0.05,w:9.2,h:0.4,fontSize:15,bold:show,italic:!show,fontFace:F,color:show?C.green:C.gray,margin:0});
  s.addNotes('Answers: '+d.grammar.map(g=>g.answer).join(', '));
}
function spellSlide(pres,d,show){
  const groups=Object.entries(d.spell_groups||{}).filter(([,w])=>w&&w.length);
  if(!groups.length) return;
  const s=iSlide(pres,'🔠  Spelling',C.navy);
  lbl(s,(d.spell_title||'SPELLING').replace(/^🔠\s*Spelling:\s*/,'').toUpperCase(),0.4,0.85,C.navy);
  if(!show){
    const all=groups.flatMap(([,w])=>w);
    lbl(s,'WORD BANK',0.4,1.18,C.gray);
    qBox(s,pres,all.join('   ·   '),0.4,1.48,9.2,1.1,C.white,C.navy,C.navy);
    s.addText('Which column does each word belong in?  Columns: '+groups.map(([g])=>g).join('  |  '),
      {x:0.4,y:2.75,w:9.2,h:0.5,fontSize:15,italic:true,fontFace:F,color:C.gray,wrap:true,margin:0});
  } else {
    const w=9.2/groups.length;
    groups.forEach(([g,words],i)=>{
      const x=0.4+i*w;
      s.addShape(pres.ShapeType.roundRect,{x:x+0.05,y:1.18,w:w-0.1,h:0.5,fill:{color:C.navy},rectRadius:0.08});
      s.addText(g,{x:x+0.1,y:1.24,w:w-0.2,h:0.38,fontSize:13,bold:true,fontFace:F,color:C.white,align:'center',wrap:true,margin:0});
      card(s,pres,x+0.05,1.74,w-0.1,2.3,C.white);
      s.addText(words.join('\n'),{x:x+0.15,y:1.86,w:w-0.3,h:2.06,fontSize:14,fontFace:F,color:C.darkGray,align:'center',wrap:true,margin:0});
    });
  }
  s.addNotes(groups.map(([g,w])=>g+': '+w.join(', ')).join(' | '));
}
function readingSlide(pres,d){
  const s=cSlide(pres,'📕  Read',NC.accent);
  s.addText(d.ch_range||'Today’s chapters',{x:0.4,y:0.95,w:9.2,h:0.55,fontSize:26,bold:true,fontFace:F,color:C.navy,margin:0});
  let y=1.6;
  if(d.copywork){ lbl(s,'COPYWORK — FROM THE NOVEL',0.4,y,C.purple);
    qBox(s,pres,'“'+clip(d.copywork,240)+'”',0.4,y+0.28,9.2,1.25,C.purpleLight,C.darkGray,C.purple); y+=1.7; }
  if(d.pause_qs&&d.pause_qs.length){ lbl(s,'PAUSE & THINK',0.4,y,C.gold);
    s.addText(d.pause_qs.map(q=>'•  '+q).join('\n'),{x:0.4,y:y+0.28,w:9.2,h:1.0,fontSize:15,fontFace:F,color:C.darkGray,wrap:true,margin:0}); }
  s.addNotes('Read the chapters, then return to the pause questions.');
}
function writingSlide(pres,d){
  const w=d.writing||{}; if(!w.stage&&!w.subtitle) return;
  const s=cSlide(pres,'🪶  Writer’s Workshop',C.green);
  lbl(s,'THIS WEEK’S STAGE',0.4,0.9,C.green);
  s.addText(w.stage||'',{x:0.4,y:1.18,w:9.2,h:0.6,fontSize:30,bold:true,fontFace:F,color:C.navy,margin:0});
  if(w.subtitle) s.addText(w.subtitle,{x:0.4,y:1.85,w:9.2,h:0.5,fontSize:18,fontFace:F,color:C.darkGray,wrap:true,margin:0});
  s.addNotes('Writer’s Workshop stage for the week.');
}

const data=JSON.parse(fs.readFileSync('lesson_data.json','utf8'));
const tmw=JSON.parse(fs.readFileSync('tmw.json','utf8'));
let rows=data.lessons||data; if(!Array.isArray(rows)) rows=Object.values(rows);
const outDir='/home/claude/decks/out'; fs.mkdirSync(outDir,{recursive:true});
(async()=>{
  let n=0;
  for(const d of rows){
    const key=`${d.week}-${d.day}`;
    if(!tmw[key]){ console.log('NO 10MW PROMPT for',key); continue; }
    d.tmw={prompt:tmw[key][0],edit_focus:tmw[key][1]};
    const pres=initPres();
    titleSlide(pres,d);
    tmwPromptSlide(pres,d); tmwWriteSlide(pres,d); tmwEditSlide(pres,d); tmwShareSlide(pres);
    recapSlide(pres,d);
    dolSlide(pres,d,false); dolSlide(pres,d,true);
    morphSlide(pres,d);
    vocabSlide(pres,d);
    grammarSlide(pres,d,false); grammarSlide(pres,d,true);
    spellSlide(pres,d,false); spellSlide(pres,d,true);
    readingSlide(pres,d);
    writingSlide(pres,d);
    const f=`${outDir}/lesson-${d.week}-${d.day}-teacher-slides.pptx`;
    await pres.writeFile({fileName:f}); n++;
  }
  console.log('decks written:',n);
})();
