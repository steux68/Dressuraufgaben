/* Titelseite: Figuren-Schau. Solange die Titelseite offen ist, zeigt sie nacheinander Hufschlagfiguren:
   die ganze Strecke liegt als helle graue Linie im Viereck, eine dünne rote Linie läuft sie ab (dahinter löst sie sich in Striche auf),
   ein kleines Namensfeld erscheint kurz. Danach die nächste Figur. */
(function(){
 const I=document.getElementById('intro'),svg=I&&I.querySelector('.vier'),pic=I&&I.querySelector('.ipic');if(!svg||!pic)return;
 if(window.matchMedia&&matchMedia('(prefers-reduced-motion:reduce)').matches)return;
 const NS='http://www.w3.org/2000/svg',RED='#e30613';
 /* d = Pfad im Viereck (viewBox 200×300, Bahn x 40–160, y 30–270; 6 Einheiten = 1 m), n = Name, lab = Lage des Namensfelds */
 const F=[
  {k:'ganze',n:'Ganze Bahn',lab:[100,120],d:'M62 36H138A16 16 0 0 1 154 52V248A16 16 0 0 1 138 264H62A16 16 0 0 1 46 248V52A16 16 0 0 1 62 36Z'},
  {k:'gC',n:'Große Tour',lab:[100,222],d:'M100 30A60 60 0 1 1 100 150A60 60 0 1 1 100 30Z'},
  {k:'kL',n:'Kleine Tour',lab:[104,196],d:'M70 30A30 30 0 1 1 70 90A30 30 0 1 1 70 30Z'},
  {k:'d1',n:'Durch die ganze Bahn wechseln',lab:[126,92],d:'M50 66L150 234'},
  {k:'sl',n:'Schlangenlinie',lab:[66,214],d:'M100 270C155 260 155 200 100 190C45 180 45 120 100 110C155 100 155 40 100 30'},
  {k:'ac',n:'Achterfigur',lab:[100,244],d:'M100 150C135 120 135 90 100 90C65 90 65 120 100 150C135 180 135 210 100 210C65 210 65 180 100 150Z'},
  {k:'mi',n:'Mittellinie',lab:[68,200],d:'M100 270L100 30'},
  {k:'gA',n:'Große Tour',lab:[100,78],d:'M100 270A60 60 0 1 1 100 150A60 60 0 1 1 100 270Z'},
  {k:'kR',n:'Kleine Tour',lab:[96,104],d:'M130 270A30 30 0 1 1 130 210A30 30 0 1 1 130 270Z'},
  {k:'d2',n:'Durch die ganze Bahn wechseln',lab:[126,206],d:'M50 234L150 66'},
  {k:'qu',n:'Quer durch die Bahn',lab:[100,96],d:'M46 150H154'},
  {k:'hg',n:'Halbe Große Tour',lab:[100,210],d:'M100 30A60 60 0 0 1 100 150'}
 ];
 F.forEach(f=>{const p=document.createElementNS(NS,'path');p.setAttribute('d',f.d);f.p=p;f.L=p.getTotalLength();});
 const cv=document.createElement('canvas');cv.setAttribute('aria-hidden','true');
 cv.style.cssText='position:absolute;inset:0;width:100%;height:100%;pointer-events:none';pic.appendChild(cv);
 const tag=document.createElement('div');tag.className='tlab';tag.hidden=true;tag.setAttribute('aria-hidden','true');pic.appendChild(tag);
 const ctx=cv.getContext('2d');let W=0,H=0,dpr=1,M=null;
 function size(){const r=pic.getBoundingClientRect();dpr=Math.min(2,devicePixelRatio||1);W=r.width;H=r.height;cv.width=Math.round(W*dpr);cv.height=Math.round(H*dpr);
  const c=svg.getScreenCTM();if(!c)return;M={a:c.a,d:c.d,e:c.e-r.left,f:c.f-r.top};}
 const X=x=>M.a*x+M.e,Y=y=>M.d*y+M.f;
 function pt(f,s){const q=f.p.getPointAtLength(Math.max(0,Math.min(f.L,s)));return[X(q.x),Y(q.y)];}
 function part(f,s0,s1,alpha,w){s0=Math.max(0,s0);s1=Math.min(f.L,s1);if(s1<=s0)return;
  const n=Math.max(2,Math.ceil((s1-s0)/3));ctx.globalAlpha=alpha;ctx.lineWidth=w;ctx.beginPath();
  for(let i=0;i<=n;i++){const q=pt(f,s0+(s1-s0)*i/n);i?ctx.lineTo(q[0],q[1]):ctx.moveTo(q[0],q[1]);}ctx.stroke();}
 const SPEED=125,HEAD=11,TAIL=80,LEAD=.5,HOLD=.9,FADE=.45;
 let run=0,last=0,t0=0,order=[],cur=null,phase=0,tm=0,pos=0,laps=1;
 function shuffle(a){a=a.slice();for(let i=a.length-1;i>0;i--){const j=Math.floor(Math.random()*(i+1));[a[i],a[j]]=[a[j],a[i]];}return a;}
 function nextFig(first){
  if(!order.length){order=shuffle(F);if(first){order=order.filter(f=>f.k!=='ganze');order.unshift(F[0]);}
   if(cur&&order[0].k===cur.k)order.push(order.shift());}
  cur=order.shift();laps=Math.max(1,Math.min(3,Math.round(3.6*SPEED/cur.L)));pos=0;tm=0;phase=0;
  tag.textContent=cur.n;tag.style.left=X(cur.lab[0])+'px';tag.style.top=Y(cur.lab[1])+'px';
  tag.hidden=false;tag.classList.remove('pop');void tag.offsetWidth;tag.classList.add('pop');}
 function frame(now){
  if(!run)return;requestAnimationFrame(frame);
  const dt=Math.min(.05,(now-last)/1000);last=now;
  if(I.hidden||document.hidden||!M||!W){ctx.clearRect(0,0,cv.width,cv.height);return;}
  ctx.setTransform(dpr,0,0,dpr,0,0);ctx.clearRect(0,0,W,H);
  if((now-t0)/1000<3.9){tag.hidden=true;return;}
  if(!cur)nextFig(true);
  tm+=dt;const w=Math.max(1.1,M.a*.95);ctx.lineCap='round';ctx.lineJoin='round';
  /* Phasen: 0 graue Linie blendet ein, 1 rote Spur läuft, 2 Halten, 3 alles blendet aus */
  const total=cur.L*laps;
  let grey=1;
  if(phase===0){grey=Math.min(1,tm/LEAD);if(tm>=LEAD){phase=1;tm=0;}}
  else if(phase===1){pos+=SPEED*dt;if(pos>total+TAIL+HEAD){phase=2;tm=0;}}
  else if(phase===2){if(tm>=HOLD){phase=3;tm=0;}}
  else{grey=Math.max(0,1-tm/FADE);if(tm>=FADE){nextFig(false);return;}}
  ctx.strokeStyle='#d6d6d1';part(cur,0,cur.L,grey*.95,w*1.5);
  tag.style.opacity=phase===3?grey:1;
  if(phase===1||phase===2){
   ctx.strokeStyle=RED;
   const s=pos%cur.L||0;
   /* Kopf und Strichspur entlang der (gegebenenfalls mehrfach durchlaufenen) Strecke; Strecke ab Ende wieder von vorn */
   const at=u=>{u=((u%cur.L)+cur.L)%cur.L;return u;};
   const lap=Math.floor(pos/cur.L);
   const alive=u=>u>=0&&u<=total; /* u = gesamte zurückgelegte Strecke */
   const seg=(a,b,al,ww)=>{ /* a<b in Gesamtstrecke; zeichnet, auch über die Naht hinweg */
    a=Math.max(0,a);b=Math.min(total,b);if(b<=a)return;
    const A=a%cur.L,B=A+(b-a);
    if(B<=cur.L)part(cur,A,B,al,ww);else{part(cur,A,cur.L,al,ww);part(cur,0,B-cur.L,al,ww);}};
   const head=Math.min(pos,total);
   seg(head-HEAD,head,1,w*1.15);
   const base=head-HEAD;let u=0;
   while(u<TAIL){const f=u/TAIL,d=Math.max(1.6,6*(1-f)),g=2.5+13*f,a=Math.pow(1-f,1.4)*.85;
    seg(base-u-d,base-u,a,w*(1-.35*f));u+=d+g;}
  }
  ctx.globalAlpha=1;
 }
 function start(){if(run)return;size();run=1;t0=performance.now();last=t0;cur=null;order=[];tag.hidden=true;requestAnimationFrame(frame);}
 function stop(){run=0;ctx.clearRect(0,0,cv.width,cv.height);tag.hidden=true;}
 new MutationObserver(()=>{I.hidden?stop():start();}).observe(I,{attributes:true,attributeFilter:['hidden']});
 addEventListener('resize',()=>{size();});if(window.ResizeObserver)new ResizeObserver(()=>{size();}).observe(pic);
 if(!I.hidden)start();
})();
