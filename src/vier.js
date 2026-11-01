(function(){
const R=document.getElementById('thVi');if(!R)return;
const WSVG='<svg class="ar" width="28" height="28" viewBox="-12 -12 24 24" aria-hidden="true"><circle class="tr" r="9.5"/><path class="rg" d="M-7.88 -5.31A9.5 9.5 0 1 1 -7.88 5.31"/><path class="dt" transform="rotate(180)" d="M5.4 0L-4.6 -4.9L-2.2 0L-4.6 4.9Z"/><text x="-9.50" y="0">W</text></svg>';
const ESVG='<svg class="ar" width="28" height="28" viewBox="-12 -12 24 24" aria-hidden="true"><circle class="tr" r="9.5"/><path class="rg" d="M7.88 5.31A9.5 9.5 0 1 1 7.88 -5.31"/><path class="dt" transform="rotate(0)" d="M5.4 0L-4.6 -4.9L-2.2 0L-4.6 4.9Z"/><text x="9.50" y="0">E</text></svg>';
/* Viereck 20 x 40 m: 6 Einheiten pro Meter */
const X0=60,X1=180,Y0=36,Y1=276,CX=120;
const L=[
 ['A',CX,Y1+22,'A','Einritt: Hier kommst du in die Bahn. Mitte der kurzen Seite, 20 m von X.'],
 ['C',CX,Y0-22,'C','Gegenüber von A, Mitte der anderen kurzen Seite. Oft sitzt hier der Richter.'],
 ['X',CX,(Y0+Y1)/2,'X','Mitte der Bahn, 20 m von A und von C, 10 m von den langen Seiten. Hier wird gegrüßt.'],
 ['K',X0-20,Y1-36,'K','Linke lange Seite, 6 m hinter der Ecke bei A. Gegenüber von F.'],
 ['E',X0-20,(Y0+Y1)/2,'E','Mitte der linken langen Seite, 20 m von A und von C. Gegenüber von B, die Linie E–X–B quert die Bahn.'],
 ['H',X0-20,Y0+36,'H','Linke lange Seite, 6 m vor der Ecke bei C. Gegenüber von M.'],
 ['F',X1+20,Y1-36,'F','Rechte lange Seite, 6 m hinter der Ecke bei A. Gegenüber von K.'],
 ['B',X1+20,(Y0+Y1)/2,'B','Mitte der rechten langen Seite, gegenüber von E.'],
 ['M',X1+20,Y0+36,'M','Rechte lange Seite, 6 m vor der Ecke bei C. Gegenüber von H.']
];
const ORDER='AKEHCMBFX';
let tab='l',sel=null,popOn=false,masse=true,sc=0,tot=0,q=null,done=false;
const XSVG='<svg viewBox="-12 -12 24 24" aria-hidden="true"><circle class="rg" r="9.5"/><path class="xx" d="M-3.6 -3.6L3.6 3.6M3.6 -3.6L-3.6 3.6"/></svg>';
const NS='http://www.w3.org/2000/svg';
function el(t,c,x){const e=document.createElement(t);if(c)e.className=c;if(x!=null)e.textContent=x;return e}
function arena(onTap,noM){
 const s=document.createElementNS(NS,'svg');s.setAttribute('viewBox','0 -6 250 358');s.setAttribute('class','viSvg');s.setAttribute('role','img');s.setAttribute('aria-label','Dressurviereck 20 mal 40 Meter von oben');
 const MY=(Y0+Y1)/2;
 let h='<g class="viGit">';for(let x=X0+30;x<X1;x+=30)h+='<line x1="'+x+'" y1="'+Y0+'" x2="'+x+'" y2="'+Y1+'"/>';for(let y=Y0+30;y<Y1;y+=30)if(y!==MY)h+='<line x1="'+X0+'" y1="'+y+'" x2="'+X1+'" y2="'+y+'"/>';h+='</g>'+
 '<rect x="'+X0+'" y="'+Y0+'" width="'+(X1-X0)+'" height="'+(Y1-Y0)+'" fill="none" stroke="#6f746d" stroke-width="2.6"/>'+
 '<line x1="'+CX+'" y1="'+Y0+'" x2="'+CX+'" y2="'+Y1+'" stroke="#a5a5a5" stroke-width="1.6" stroke-dasharray="1.5 4" stroke-linecap="round"/>'+
 '<line x1="'+X0+'" y1="'+MY+'" x2="'+X1+'" y2="'+MY+'" stroke="#a5a5a5" stroke-width="1.6" stroke-dasharray="1.5 4" stroke-linecap="round"/>';
 L.forEach(l=>{if(l[0]==='X')return;const x=l[1],y=l[2];let t;
  if(x<X0)t=[X0-9,y,X0,y];else if(x>X1)t=[X1,y,X1+9,y];else if(y>Y1)t=[x,Y1,x,Y1+9];else t=[x,Y0-9,x,Y0];
  h+='<line x1="'+t[0]+'" y1="'+t[1]+'" x2="'+t[2]+'" y2="'+t[3]+'" stroke="#6f746d" stroke-width="2.6"/>'});
 [Y0+60,Y1-60].forEach(y=>[X0,X1].forEach(x=>{h+='<circle cx="'+x+'" cy="'+y+'" r="3.3" fill="#111"/>'}));
 if(masse&&!noM){
  [[Y1-18,'6 m'],[Y1-93,'14 m'],[Y0+93,'14 m'],[Y0+18,'6 m']].forEach(a=>{h+='<text class="vm" x="'+(X0+6)+'" y="'+a[0]+'">'+a[1]+'</text>'});
  h+='<text class="vm" x="'+(CX+6)+'" y="'+(Y1-10)+'">20 m</text><text class="vm" x="'+(CX+6)+'" y="'+(Y0+18)+'">20 m</text>';
  const dx=X1+34,dy=Y1+36;
  h+='<g class="vd"><line x1="'+dx+'" y1="'+Y0+'" x2="'+dx+'" y2="'+Y1+'"/><line x1="'+(dx-4)+'" y1="'+Y0+'" x2="'+(dx+4)+'" y2="'+Y0+'"/><line x1="'+(dx-4)+'" y1="'+Y1+'" x2="'+(dx+4)+'" y2="'+Y1+'"/>'+
     '<line x1="'+X0+'" y1="'+dy+'" x2="'+X1+'" y2="'+dy+'"/><line x1="'+X0+'" y1="'+(dy-4)+'" x2="'+X0+'" y2="'+(dy+4)+'"/><line x1="'+X1+'" y1="'+(dy-4)+'" x2="'+X1+'" y2="'+(dy+4)+'"/></g>'+
     '<text class="vm vb" x="'+(dx+10)+'" y="'+MY+'" transform="rotate(90 '+(dx+10)+' '+MY+')" text-anchor="middle">40 m</text>'+
     '<text class="vm vb" x="'+CX+'" y="'+(dy+13)+'" text-anchor="middle">20 m</text>'+
     '<text class="vm" text-anchor="end" x="'+(X1-6)+'" y="'+(Y0+60-6)+'">30 m</text><text class="vm" text-anchor="end" x="'+(X1-6)+'" y="'+(Y1-60-6)+'">10 m</text>';
 }
 s.innerHTML=h;
 L.forEach(l=>{
  const g=document.createElementNS(NS,'g');g.setAttribute('class','vl'+(l[0]==='X'?' vx':''));g.setAttribute('data-l',l[0]);g.setAttribute('tabindex','0');g.setAttribute('role','button');g.setAttribute('aria-label','Buchstabe '+l[0]);
  g.innerHTML='<circle cx="'+l[1]+'" cy="'+l[2]+'" r="'+(l[0]==='X'?7.6:5.8)+'"/><text x="'+l[1]+'" y="'+l[2]+'">'+l[0]+'</text>';
  g.addEventListener('click',()=>onTap(l[0]));
  g.addEventListener('keydown',e=>{if(e.key==='Enter'||e.key===' '){e.preventDefault();onTap(l[0])}});
  s.appendChild(g);
 });
 return s;
}
function tabs(){
 const r=el('div','viTabs');
 [['l','Lernen'],['s','Spiel'],['g','Geschichte']].forEach(([k,n])=>{const b=el('button',null,n);b.type='button';b.setAttribute('aria-pressed',tab===k);b.onclick=()=>{tab=k;if(k==='s'){sc=0;tot=0;next()}render()};r.appendChild(b)});
 return r;
}
function mark(s,ids,cls){s.querySelectorAll('.vl').forEach(g=>{g.classList.remove('on','ok','bad','hint');});ids.forEach(([id,c])=>{const g=s.querySelector('[data-l="'+id+'"]');if(g)g.classList.add(c)})}
function lernen(){
 const w=el('div','viBody');
 const bar=el('div','viBar');const cm=el('button','viChip','Maße');cm.type='button';cm.setAttribute('aria-pressed',masse);cm.onclick=()=>{masse=!masse;render()};bar.appendChild(cm);
 bar.appendChild(el('span','viHint','Tippe auf einen Buchstaben'));w.appendChild(bar);
 const s=arena(id=>{sel=id;popOn=true;render()});w.appendChild(s);
 if(sel)mark(s,[[sel,'on']]);
 const c=el('div','viCard');
 c.appendChild(el('p','viT','Das Dressurviereck'));
 c.appendChild(el('p','viD','20 × 40 m. Du reitest bei A hinein und siehst auf C. Links liegen K, E, H, rechts F, B, M. Die Reihenfolge A K E H C M B F geht im Uhrzeigersinn um die Bahn.'));
 c.appendChild(el('p','viD','Maße: 20 m breit, 40 m lang. Die schwarzen Punkte am Zaun liegen 10 m und 30 m von A entfernt. Das Gitter zeigt 5 × 5 m.'));
 c.appendChild(el('p','viH','Merksprüche für A K E H C M B F'));
 [['Englisch: „All King Edward’s Horses Carry Many Big Fleas“.'],['Vorschlag: „Alle Katzen essen Hering, Chiara mag Brot frisch.“'],['Vorschlag: „Anna kocht Eintopf, Hans chauffiert Mama bei Frost.“']].forEach(a=>c.appendChild(el('p','viD',a[0])));
 let mine='';try{mine=localStorage.getItem('viMerk')||''}catch(e){}
 const inp=el('input','viIn');inp.type='text';inp.placeholder='Dein eigener Merkspruch';inp.value=mine;inp.maxLength=120;inp.setAttribute('aria-label','Dein eigener Merkspruch');
 inp.oninput=()=>{try{localStorage.setItem('viMerk',inp.value)}catch(e){}};
 c.appendChild(inp);
 w.appendChild(c);
 return w;
}
let pop=null;
function popup(){
 if(!pop){
  pop=el('div','tlpop anapop viPop');pop.hidden=true;pop.setAttribute('role','dialog');pop.setAttribute('aria-modal','true');
  pop.innerHTML='<div class="tlcard"><div class="tltop"><span class="tlk" id="viTk"></span><button type="button" class="tlx" id="viX" aria-label="Schließen">'+XSVG+'</button></div><div class="tlbody"><figure class="gfig has vifig" id="viFig"><button type="button" class="tlar pw" id="viPv" aria-label="Zurück">'+WSVG+'</button><button type="button" class="tlar pe" id="viNx" aria-label="Weiter">'+ESVG+'</button></figure><p class="viT" id="viPT"></p><p class="viD" id="viPD"></p><dl class="anaDl" id="viDl"></dl></div></div>';
  document.body.appendChild(pop);
  const close=()=>{popOn=false;pop.hidden=true};
  pop.querySelector('#viX').onclick=close;
  pop.addEventListener('click',e=>{if(e.target===pop)close()});
  document.addEventListener('keydown',e=>{if(e.key==='Escape'&&!pop.hidden)close()});
  const go=d=>{let i=ORDER.indexOf(sel);if(i<0)i=d>0?-1:0;sel=ORDER[(i+d+ORDER.length)%ORDER.length];popOn=true;render()};
  setInterval(()=>{if(!pop.hidden&&R.offsetParent===null){popOn=false;pop.hidden=true}},400);
  pop.querySelector('#viPv').onclick=()=>go(-1);pop.querySelector('#viNx').onclick=()=>go(1);
 }
 const show=popOn&&tab==='l'&&sel&&!R.hidden;
 pop.hidden=!show;
 if(show){const fg=pop.querySelector('#viFig');const o=fg.querySelector('.viSvg');if(o)o.remove();const sv=arena(()=>{},true);sv.classList.add('viMini');mark(sv,[[sel,'on']]);fg.insertBefore(sv,fg.firstChild);const l=L.find(x=>x[0]===sel);pop.querySelector('#viTk').textContent='Punkt '+sel;pop.querySelector('#viPT').textContent=sel==='X'?'X, die Mitte':'Buchstabe '+sel;pop.querySelector('#viPD').textContent=l[4];
  const dl=pop.querySelector('#viDl');dl.textContent='';const R8='AKEHCMBF',i8=R8.indexOf(sel);
  const side=sel==='A'?'kurze Seite, Eingang':sel==='C'?'kurze Seite, gegenüber von A':sel==='X'?'Mitte der Bahn':l[1]<CX?'linke lange Seite':'rechte lange Seite';
  const m=sel==='A'?0:sel==='C'?40:sel==='X'?20:Math.round((Y1-l[2])/6);
  const rows=[['Lage',side],['Von A',m+' m'+(sel==='X'?' (auch 20 m von C)':'')]];
  if(i8>=0)rows.push(['Nachbarn',R8[(i8+7)%8]+' und '+R8[(i8+1)%8]],['Reihenfolge',(i8+1)+' von 8 im Uhrzeigersinn']);
  rows.forEach(r=>{dl.appendChild(el('dt','',r[0]));dl.appendChild(el('dd','',r[1]));});}
}
function next(){
 const ids=L.map(l=>l[0]);let n;do{n=ids[Math.floor(Math.random()*ids.length)]}while(q&&n===q.id);
 q={id:n,rev:Math.random()<.4};done=false;
}
function spiel(){
 const w=el('div','viBody');
 const bar=el('div','viBar');bar.appendChild(el('span','viScore','Richtig: '+sc+' von '+tot));w.appendChild(bar);
 const top=el('div','viCard');
 top.appendChild(el('p','viT viQ',q.rev?'Welcher Buchstabe fehlt hier?':'Wo ist '+q.id+'?'));
 w.appendChild(top);
 const s=arena(id=>{if(q.rev)return;answer(id)},true);
 const c=el('div','viCard');
 if(q.rev){s.querySelectorAll('.vl').forEach(g=>{if(g.getAttribute('data-l')===q.id)g.classList.add('hole');else g.classList.add('dim')});
  if(!done){const row=el('div','viOpts');L.map(l=>l[0]).sort().forEach(id=>{const b=el('button','viOpt',id);b.type='button';b.onclick=()=>{if(!done)answer(id)};row.appendChild(b)});c.appendChild(row);}}
 else if(!done)c.appendChild(el('p','viD','Tippe die Stelle im Viereck an.'));
 w.appendChild(s);
 if(done){
  const ok=q.last===q.id;
  s.querySelectorAll('.vl').forEach(g=>{g.classList.remove('dim','hole')});
  mark(s,[[q.id,'ok']].concat(ok?[]:[[q.last,'bad']]));
  c.appendChild(el('p','viFb '+(ok?'ok':'bad'),ok?'Richtig.':'Das war '+q.last+'. Gesucht war '+q.id+'.'));
  const nav=el('div','aSwRow');const b=el('button','aSw e');b.type='button';b.innerHTML='<span>Weiter</span>'+ESVG;b.onclick=()=>{next();render()};nav.appendChild(el('span'));nav.appendChild(b);c.appendChild(nav);
 }
 w.appendChild(c);return w;
}
function answer(id){if(done)return;q.last=id;done=true;tot++;if(id===q.id)sc++;render()}
function geschichte(){
 const w=el('div','viBody viHist');
 const P=(t,c)=>{w.appendChild(el('p',c||'viD',t))};
 const H=t=>w.appendChild(el('p','viH',t));
 w.appendChild(el('p','viT','Warum diese Buchstaben?'));
 P('Niemand weiß es sicher. Hier steht, was belegt ist und was nur erzählt wird.');
 H('Belegt');
 P('Bei den Olympischen Spielen 1932 in Los Angeles wurden die Buchstaben erstmals offiziell in einem Dressurviereck verwendet (damals 20 × 60 m). Bis 1948 durften nur Offiziere mitreiten. Ab 1952 starteten bei Olympia auch Frauen und Zivilisten.');
 H('Erzählt: die Rangordnung am Hof');
 P('Die bekannteste Geschichte: Am preußischen Hof sollen die Reitknechte mit den Pferden ihrer Herren neben dem Buchstaben gewartet haben, der zu deren Rang passte.');
 P('K = Kaiser (oder König), F = Fürst, E = Edeling (Ehrengast), B = Bannerträger, M = Meier (Verwalter), H = Hofmarschall. Bei der großen Bahn: S = Schatzmeister, R = Ritter.');
 P('Das wird oft weitererzählt, aber es gibt keinen Beleg. Außerdem passen A, X und C nicht dazu.');
 H('Erzählt: Kommandos in der Reitbahn');
 P('Eine andere Erklärung: Die Buchstaben standen für Stellen auf dem Kasernenhof. Kommandanten konnten so Befehle geben („bei B abwenden“), ohne dass die Pferde in der Menge zusammenstießen. Auch das ist nicht belegt.');
 H('Erzählt: Pferde im Stall');
 P('Wieder eine andere Geschichte: Die Buchstaben waren die Anfangsbuchstaben von Pferden im Stall des Herzogs von Newcastle (17. Jahrhundert). Nicht gesichert.');
 H('Die Maße');
 P('Das große Viereck ist 20 × 60 m, das kleine 20 × 40 m. Warum genau diese Maße, ist nicht geklärt. Oft heißt es, sie kommen von Kasernenhöfen der Kavallerie.');
 H('Die große Bahn');
 P('Das große Viereck hat zusätzliche Buchstaben: V, S, R, P an den langen Seiten und D, L, I, G auf der Mittellinie. Man sagt, deutsche Kavalleristen hätten sie im 20. Jahrhundert eingeführt. In den Aufgaben R1–R6 brauchst du sie nicht.');
 const im=el('div','viImgs');w.appendChild(im);
 (window.VIER_BILDER||[]).forEach(b=>{const f=el('figure');const i=new Image();i.src=b[0];i.alt=b[1];i.loading='lazy';f.appendChild(i);f.appendChild(el('figcaption',null,b[2]));im.appendChild(f)});
 P('Quellen: Horse and Hound („Ask H&H: dressage letter markers“), The Saddlery Shop („The history of dressage markers“). Weitere Hinweise aus Texten von tempusrenatus.org, eurodressage.com und howtodressage.com, von mir noch nicht im Original geprüft.','viSrc');
 return w;
}
function render(){
 R.textContent='';R.appendChild(tabs());
 R.appendChild(tab==='l'?lernen():tab==='s'?spiel():geschichte());
 popup();
}
window.vierOpen=function(){popOn=false;if(tab==='s'&&!q)next();render()};
window.vierClose=function(){popOn=false;if(pop)pop.hidden=true};
})();
