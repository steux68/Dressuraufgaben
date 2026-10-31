#!/usr/bin/env python3
"""Titelseite: Viereck als Animation (Linien und Buchstaben aus einem Haufen in der Mitte, Pause mit Abstand, dann Zusammenschnappen),
kräftigere Linien, Dock-Balken pulsieren auf der Titelseite.  Aufruf: python3 src/anim_patch.py <version> index.html"""
import sys, re
ver, path = sys.argv[1], sys.argv[2]
s = open(path, encoding='utf8').read()
if 'id="anim-js"' in s: sys.exit('schon angewendet')
def rep(old, new):
    global s
    assert s.count(old) == 1, f'{s.count(old)}x: {old[:60]}'
    s = s.replace(old, new)
# Rechteck in vier Seiten, Linien kräftiger
rep('<rect x="40" y="30" width="120" height="240" fill="#fff" stroke="#8c918a" stroke-width="1.4"/>',
    '<line class="an" x1="40" y1="30" x2="160" y2="30" stroke="#6f746d" stroke-width="2.6" stroke-linecap="square"/>'
    '<line class="an" x1="160" y1="30" x2="160" y2="270" stroke="#6f746d" stroke-width="2.6" stroke-linecap="square"/>'
    '<line class="an" x1="160" y1="270" x2="40" y2="270" stroke="#6f746d" stroke-width="2.6" stroke-linecap="square"/>'
    '<line class="an" x1="40" y1="270" x2="40" y2="30" stroke="#6f746d" stroke-width="2.6" stroke-linecap="square"/>')
i = s.index('<svg class="vier"'); j = s.index('</svg>', i)
seg = s[i:j]
seg = seg.replace('stroke="#8c918a" stroke-width="1.4"', 'stroke="#6f746d" stroke-width="2.6"')
seg = seg.replace('stroke="#b8b8b8" stroke-width="1" stroke-dasharray="1 3"', 'stroke="#a5a5a5" stroke-width="1.8" stroke-dasharray="1.5 4" stroke-linecap="round"')
seg = seg.replace('<line x', '<line class="an" x').replace('<line class="an" class="an"', '<line class="an"')
seg = seg.replace('font-size="15" font-weight="700"', 'font-size="17" font-weight="700"')
seg = seg.replace('<text ', '<text class="an" ').replace('<circle ', '<circle class="an" ').replace('stroke-width="1.2"/>', 'stroke-width="2"/>')
s = s[:i] + seg + s[j:]
CSS = '''
/* ---- Titelseite: Animation, pulsierende Menülinien ---- */
#intro .vier .an{vector-effect:non-scaling-stroke}
@keyframes pxl{0%,100%{opacity:.25;transform:scaleY(1)}50%{opacity:1;transform:scaleY(2.4)}}
body.introOn .hb::after{content:"";position:absolute;left:0;right:0;bottom:0;height:2px;background:#e30613;transform-origin:50% 100%;animation:pxl 2.6s ease-in-out infinite;pointer-events:none}
body.introOn .hb:nth-of-type(2n)::after{animation-delay:-.65s}
body.introOn .hb:nth-of-type(3n)::after{animation-delay:-1.3s}
body.introOn .hb:nth-of-type(5n)::after{animation-delay:-1.95s}
@media (prefers-reduced-motion:reduce){body.introOn .hb::after{animation:none;opacity:.6}}
'''
JS = '''
<script id="anim-js">
(function(){
 const I=document.getElementById('intro'),svg=I&&I.querySelector('.vier');if(!svg)return;
 const els=[...svg.querySelectorAll('.an')],CX=100,CY=150;
 const info=els.map((e,n)=>{let b;try{b=e.getBBox();}catch(x){b={x:0,y:0,width:0,height:0};}
  const cx=b.x+b.width/2,cy=b.y+b.height/2,dx=cx-CX,dy=cy-CY,d=Math.hypot(dx,dy)||1;
  const horiz=e.tagName==='line'&&b.width>=b.height,line=e.tagName==='line'&&(b.width>40||b.height>40);
  const a=n*2.399;return{e,cx,cy,ux:dx/d,uy:dy/d,line,horiz,jx:Math.cos(a)*9,jy:Math.sin(a)*9,r0:(((n*37)%11)-5)*22,delay:(n%9)*0.045,gap:e.tagName==='circle'?0:(line?5.5:7)};});
 info.forEach(o=>{if(Math.hypot(o.cx-CX,o.cy-CY)<6&&!o.line){o.jx=o.jy=0;o.r0=0;o.delay=0;o.gap=0;}});
 const ez=t=>t<0?0:t>1?1:t*t*(3-2*t),eb=t=>{t=t<0?0:t>1?1:t;const c=1.3;return 1+(c+1)*Math.pow(t-1,3)+c*Math.pow(t-1,2);};
 let raf=0,run=0;
 function draw(P,K,tm){
  info.forEach(o=>{
   const p=ez((P-o.delay)/(1-0.4)),k=K,q=1-p,w=Math.sin(tm*9+o.cx)*q*2.2;
   const tx=(CX-o.cx)*q+o.jx*q+o.ux*o.gap*k+w,ty=(CY-o.cy)*q+o.jy*q+o.uy*o.gap*k+w*0.6;
   let sx=1,sy=1;if(o.line){const f=1-0.2*k;if(o.horiz)sx=f;else sy=f;}
   o.e.setAttribute('transform','translate('+(o.cx+tx)+' '+(o.cy+ty)+') rotate('+(o.r0*q)+') scale('+sx+' '+sy+') translate('+(-o.cx)+' '+(-o.cy)+')');
  });
 }
 function clear(){info.forEach(o=>o.e.removeAttribute('transform'));}
 function play(){
  if(window.matchMedia&&matchMedia('(prefers-reduced-motion:reduce)').matches){clear();return;}
  cancelAnimationFrame(raf);const id=++run,t0=performance.now();
  const HOLD=.35,MOVE=2.0,PAUSE=.7,SNAP=.35;
  (function f(now){if(id!==run)return;const t=(now-t0)/1000;
   const P=Math.min(1,Math.max(0,(t-HOLD)/MOVE)),K=t<HOLD+MOVE+PAUSE?1:1-eb((t-HOLD-MOVE-PAUSE)/SNAP);
   if(t>=HOLD+MOVE+PAUSE+SNAP+.05){clear();return;}
   draw(P,Math.max(0,K),t);raf=requestAnimationFrame(f);})(t0);
 }
 const vis=()=>!I.hidden&&I.offsetParent!==null;
 let was=false;
 new MutationObserver(()=>{const v=!I.hidden;upd();if(v&&!was)play();was=v;}).observe(I,{attributes:true,attributeFilter:['hidden']});
 const H=document.getElementById('hscroll'),upd=()=>{document.body.classList.toggle('introOn',!I.hidden&&(!H||H.scrollTop<60));};
 if(H)H.addEventListener('scroll',upd,{passive:true});
 if(!I.hidden){was=true;upd();play();}
 I.addEventListener('click',()=>{run++;clear();},true);
})();
</script>
'''
i = s.rfind('</style>'); assert i > 0
s = s[:i] + CSS + s[i:]
rep('</body></html>', JS + '</body></html>')
s = re.sub(r'(<meta name="app-version" content=")[^"]*"', r'\g<1>' + ver + '"', s, count=1)
open(path, 'w', encoding='utf8').write(s); print('ok')
