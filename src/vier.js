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
const ORDER='AKEHCMBF';
let tab='l',sel=null,masse=false,sc=0,tot=0,q=null,done=false;
const NS='http://www.w3.org/2000/svg';
function el(t,c,x){const e=document.createElement(t);if(c)e.className=c;if(x!=null)e.textContent=x;return e}
function arena(onTap,noM){
 const s=document.createElementNS(NS,'svg');s.setAttribute('viewBox','0 0 240 330');s.setAttribute('class','viSvg');s.setAttribute('role','img');s.setAttribute('aria-label','Dressurviereck 20 mal 40 Meter von oben');
 let h='<rect x="'+X0+'" y="'+Y0+'" width="'+(X1-X0)+'" height="'+(Y1-Y0)+'" fill="none" stroke="#6f746d" stroke-width="2.6"/>'+
 '<line x1="'+CX+'" y1="'+Y0+'" x2="'+CX+'" y2="'+Y1+'" stroke="#a5a5a5" stroke-width="1.6" stroke-dasharray="1.5 4" stroke-linecap="round"/>'+
 '<line x1="'+X0+'" y1="'+(Y0+Y1)/2+'" x2="'+X1+'" y2="'+(Y0+Y1)/2+'" stroke="#a5a5a5" stroke-width="1.6" stroke-dasharray="1.5 4" stroke-linecap="round"/>';
 if(masse&&!noM){
  [[Y1-18,'6 m'],[Y1-93,'14 m'],[Y0+93,'14 m'],[Y0+18,'6 m']].forEach(a=>{h+='<text class="vm" x="'+(X0+6)+'" y="'+a[0]+'">'+a[1]+'</text>'});
  [[Y1-36],[Y0+36]].forEach(a=>{h+='<line x1="'+(X0-6)+'" y1="'+a[0]+'" x2="'+(X0+2)+'" y2="'+a[0]+'" stroke="#6f746d" stroke-width="1.6"/>'});
  h+='<text class="vm" x="'+(CX+6)+'" y="'+(Y1-10)+'">20 m</text><text class="vm" x="'+(CX+6)+'" y="'+(Y0+18)+'">20 m</text>';
 }
 s.innerHTML=h;
 L.forEach(l=>{
  const g=document.createElementNS(NS,'g');g.setAttribute('class','vl');g.setAttribute('data-l',l[0]);g.setAttribute('tabindex','0');g.setAttribute('role','button');g.setAttribute('aria-label','Buchstabe '+l[0]);
  g.innerHTML='<circle cx="'+l[1]+'" cy="'+l[2]+'" r="14"/><text x="'+l[1]+'" y="'+l[2]+'">'+l[0]+'</text>';
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
 const lab=el('span','viHint','Tippe auf einen Buchstaben');bar.appendChild(lab);w.appendChild(bar);
 const s=arena(id=>{sel=id;render()});w.appendChild(s);
 if(sel)mark(s,[[sel,'on']]);
 const c=el('div','viCard');
 if(sel){const l=L.find(x=>x[0]===sel);c.appendChild(el('p','viT','Punkt '+sel));c.appendChild(el('p','viD',l[4]))}
 else{c.appendChild(el('p','viT','Das Dressurviereck'));c.appendChild(el('p','viD','20 × 40 m. Du reitest bei A hinein und siehst auf C. Links liegen K, E, H, rechts F, B, M. Die Reihenfolge A K E H C M B F geht im Uhrzeigersinn um die Bahn.'));
  c.appendChild(el('p','viD','Merkspruch (englisch): „All King Edward’s Horses Carry Many Big Fleas“. Erfinde dir einen deutschen dazu.'))}
 w.appendChild(c);
 const nav=el('div','aSwRow');
 const a=el('button','aSw w');a.type='button';a.innerHTML=WSVG+'<span>Zurück</span>';
 const b=el('button','aSw e');b.type='button';b.innerHTML='<span>Weiter</span>'+ESVG;
 const cur=()=>sel?ORDER.indexOf(sel):-1;
 a.onclick=()=>{let i=cur();sel=ORDER[(i<=0?ORDER.length:i)-1];render()};
 b.onclick=()=>{let i=cur();sel=ORDER[(i+1)%ORDER.length];render()};
 nav.append(a,b);w.appendChild(nav);
 return w;
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
 w.appendChild(el('p','viT','Warum diese Buchstaben?'));
 P('Niemand weiß es sicher. Das ist belegt und das ist Vermutung:');
 w.appendChild(el('p','viH','Belegt'));
 P('Bei den Olympischen Spielen 1932 in Los Angeles wurden die Buchstaben erstmals offiziell in einem Dressurviereck verwendet (damals 20 × 60 m).');
 w.appendChild(el('p','viH','Vermutung: der preußische Hof'));
 P('Am häufigsten wird erzählt: Im 18. Jahrhundert warteten die Reitknechte am Hof mit den Pferden ihrer Herren neben dem Buchstaben, der zu deren Rang passte, etwa K für Kaiser oder König und F für Fürst. Das passt zu K, E, H, M, B und F, aber nicht zu A, X und C. Einen Beleg dafür gibt es nicht.');
 w.appendChild(el('p','viH','Vermutung: Pferde im Stall'));
 P('Eine andere Erklärung: Die Buchstaben waren die Anfangsbuchstaben von Pferden im Stall des Herzogs von Newcastle im 17. Jahrhundert. Auch das ist nicht gesichert.');
 w.appendChild(el('p','viH','Die große Bahn'));
 P('Das große Viereck (20 × 60 m) hat zusätzliche Buchstaben: V, S, R, P an den langen Seiten und D, L, I, G auf der Mittellinie. Man sagt, deutsche Kavalleristen hätten sie im 20. Jahrhundert eingeführt. In den Aufgaben R1–R6 brauchst du sie nicht.');
 const im=el('div','viImgs');w.appendChild(im);
 (window.VIER_BILDER||[]).forEach(b=>{const f=el('figure');const i=new Image();i.src=b[0];i.alt=b[1];i.loading='lazy';f.appendChild(i);f.appendChild(el('figcaption',null,b[2]));im.appendChild(f)});
 P('Quellen: Horse and Hound („Ask H&H: dressage letter markers“), The Saddlery Shop („The history of dressage markers“).','viSrc');
 return w;
}
function render(){
 R.textContent='';R.appendChild(tabs());
 R.appendChild(tab==='l'?lernen():tab==='s'?spiel():geschichte());
}
window.vierOpen=function(){if(tab==='s'&&!q)next();render()};
})();
