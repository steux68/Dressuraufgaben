/* Titelseite: rote Spuren laufen schnell auf Hufschlag und Figuren um das Viereck.
   Vorne eine dünne, durchgezogene rote Linie, dahinter löst sie sich in immer kürzere Striche mit größeren Lücken auf und verblasst. */
(function(){
 const I=document.getElementById('intro'),svg=I&&I.querySelector('.vier'),pic=I&&I.querySelector('.ipic');if(!svg||!pic)return;
 if(window.matchMedia&&matchMedia('(prefers-reduced-motion:reduce)').matches)return;
 const NS='http://www.w3.org/2000/svg',RED='#e30613';
 const D={
  track:'M62 36H138A16 16 0 0 1 154 52V248A16 16 0 0 1 138 264H62A16 16 0 0 1 46 248V52A16 16 0 0 1 62 36Z',
  zirkelC:'M100 36A54 54 0 1 1 100 144A54 54 0 1 1 100 36Z',
  zirkelA:'M100 264A54 54 0 1 1 100 156A54 54 0 1 1 100 264Z',
  diag1:'M50 66L150 234',diag2:'M50 234L150 66',
  schlange:'M100 264C170 240 170 170 100 150C30 130 30 60 100 36',
  acht:'M100 150C135 120 135 90 100 90C65 90 65 120 100 150C135 180 135 210 100 210C65 210 65 180 100 150Z',
  volteL:'M76 36A30 30 0 1 1 76 96A30 30 0 1 1 76 36Z',volteR:'M124 264A30 30 0 1 1 124 204A30 30 0 1 1 124 264Z',
  mitte:'M100 264L100 36',quer:'M46 150H154',
  halbe:'M46 150C46 90 62 36 100 36C138 36 154 90 154 150'
 };
 const keys=Object.keys(D),P={};
 keys.forEach(k=>{const p=document.createElementNS(NS,'path');p.setAttribute('d',D[k]);P[k]={p,L:p.getTotalLength()};});
 const cv=document.createElement('canvas');cv.setAttribute('aria-hidden','true');
 cv.style.cssText='position:absolute;inset:0;width:100%;height:100%;pointer-events:none';pic.appendChild(cv);
 const ctx=cv.getContext('2d');let W=0,H=0,dpr=1,M=null;
 function size(){const r=pic.getBoundingClientRect();dpr=Math.min(2,devicePixelRatio||1);W=r.width;H=r.height;cv.width=Math.round(W*dpr);cv.height=Math.round(H*dpr);
  const c=svg.getScreenCTM();if(!c)return;M={a:c.a,d:c.d,e:c.e-r.left,f:c.f-r.top};}
 const X=x=>M.a*x+M.e,Y=y=>M.d*y+M.f;
 function pt(tr,s){const L=tr.r.L,u=tr.rev?L-s:s,q=tr.r.p.getPointAtLength(Math.max(0,Math.min(L,u)));return[X(q.x),Y(q.y)];}
 function strokePart(tr,s0,s1,alpha,w){ /* Teilstück [s0,s1] in Pfadlänge */
  const L=tr.r.L;s0=Math.max(0,s0);s1=Math.min(L,s1);if(s1<=s0)return;
  const n=Math.max(2,Math.ceil((s1-s0)/3));ctx.globalAlpha=alpha;ctx.lineWidth=w;ctx.beginPath();
  for(let i=0;i<=n;i++){const q=pt(tr,s0+(s1-s0)*i/n);i?ctx.lineTo(q[0],q[1]):ctx.moveTo(q[0],q[1]);}ctx.stroke();}
 let trails=[],last=0,run=0,t0=0,lastKey='';
 function spawn(delay){
  let k;do{k=keys[Math.floor(Math.random()*keys.length)];}while(trails.some(t=>t.k===k)||k===lastKey);lastKey=k;
  const r=P[k],speed=230+Math.random()*120;
  trails.push({k,r,rev:Math.random()<.5,s:-delay*speed,v:speed,head:10+Math.random()*6,tail:70+Math.random()*50});}
 function frame(now){
  if(!run)return;requestAnimationFrame(frame);
  const dt=Math.min(.05,(now-last)/1000);last=now;
  if(I.hidden||document.hidden||!M||!W){ctx.clearRect(0,0,cv.width,cv.height);return;}
  ctx.setTransform(dpr,0,0,dpr,0,0);ctx.clearRect(0,0,W,H);
  if((now-t0)/1000<3.9)return;
  ctx.lineCap='round';ctx.strokeStyle=RED;const w=Math.max(1.1,M.a*.95);
  trails.forEach(tr=>{tr.s+=tr.v*dt;
   const s=tr.s,hs=s-tr.head;
   strokePart(tr,hs,s,1,w*1.15);                 /* durchgezogener Kopf */
   let u=0;const T=tr.tail,base=hs;                /* Strichspur dahinter */
   while(u<T){const f=u/T,d=Math.max(1.6,6*(1-f)),g=2.5+13*f,a=Math.pow(1-f,1.4)*.85;
    strokePart(tr,base-u-d,base-u,a,w*(1-.35*f));u+=d+g;}
  });
  ctx.globalAlpha=1;
  trails=trails.filter(tr=>{const done=tr.s-tr.head-tr.tail>tr.r.L;if(done)spawn(Math.random()*.35);return !done;});
 }
 function start(){if(run)return;size();run=1;t0=performance.now();last=t0;trails=[];lastKey='';spawn(0);spawn(.7);spawn(1.5);requestAnimationFrame(frame);}
 function stop(){run=0;ctx.clearRect(0,0,cv.width,cv.height);}
 new MutationObserver(()=>{I.hidden?stop():start();}).observe(I,{attributes:true,attributeFilter:['hidden']});
 addEventListener('resize',()=>{size();});if(window.ResizeObserver)new ResizeObserver(size).observe(pic);
 if(!I.hidden)start();
})();
