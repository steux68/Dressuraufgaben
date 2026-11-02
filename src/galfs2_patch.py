# Galerie-Vollbild: nur "Zurück"-Knopf (keine W/E-Pfeile), Zoom um die Finger statt um die Mitte. Idempotent. 02.11.2026
import re
P='index.html';s=open(P,encoding='utf-8').read()
# 1) HTML: Knöpfe
a=s.index('<button type="button" id="gfsx"');b=s.index('<div id="gfh">',a)
s=s[:a]+'<button type="button" id="gfsx" aria-label="Zurück zum Text"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M14.5 5.5L8 12l6.5 6.5"/></svg><span>Zurück</span></button>'+s[b:]
# 2) CSS
if '/* galfs2 */' not in s:
    css='''/* galfs2 */
#gfsx{left:10px;right:auto;top:10px;width:auto;height:44px;padding:0 18px 0 10px;border-radius:22px!important;display:flex;align-items:center;gap:4px;color:#fff;font:700 15px/1 inherit}
#gfsx svg{width:24px;height:24px;fill:none;stroke:#fff;stroke-width:2;stroke-linecap:round;stroke-linejoin:round}
#gfsx span{letter-spacing:.02em}
'''
    i=s.rindex('</style>');s=s[:i]+css+s[i:]
s=s.replace('<div id="gfh">Zwei Finger: zoomen · doppelt tippen: Zoom</div>','<div id="gfh">Zwei Finger: zoomen · doppelt tippen: Zoom</div>')
# 3) JS
a=s.index(' /* Vollbild */');b=s.index('\n })();\n',a)+len('\n })();\n')
js=''' /* Vollbild */
 (function(){const fs=$('gfs'),im=$('gfsi'),v=$('gfsv');let sc=1,tx=0,ty=0,last=0,drag=null,pinch=null;const pts=new Map();
  function ap(){im.style.transform='translate('+tx+'px,'+ty+'px) scale('+sc+')';}
  function clamp(){const w=im.clientWidth*sc,h=im.clientHeight*sc,vw=v.clientWidth,vh=v.clientHeight,ol=im.offsetLeft,ot=im.offsetTop;
   tx=w<=vw?(vw-w)/2-ol:Math.min(-ol,Math.max(vw-w-ol,tx));ty=h<=vh?(vh-h)/2-ot:Math.min(-ot,Math.max(vh-h-ot,ty));}
  function rel(cx,cy){const r=v.getBoundingClientRect();return [cx-r.left-im.offsetLeft,cy-r.top-im.offsetTop];}
  function zoomAt(ns,fx,fy){ns=Math.max(1,Math.min(6,ns));const k=ns/sc;tx=fx-(fx-tx)*k;ty=fy-(fy-ty)*k;sc=ns;clamp();ap();}
  function reset(){sc=1;tx=ty=0;ap();}
  function load(){reset();im.src=GAL[gi].f;im.alt=GAL[gi].n;}
  window.gfsHide=function(){fs.hidden=true;window.gfsOpen=false;};
  function open(){if(!fs.hidden)return;load();fs.hidden=false;window.gfsOpen=true;$('gfh').style.opacity=1;setTimeout(()=>{$('gfh').style.opacity=0},2600);try{history.pushState({app:1,pop:2},'')}catch(e){}}
  function close(){if(history.state&&history.state.pop===2)history.back();else gfsHide();}
  $('gpi').onclick=open;$('gfsx').onclick=close;
  function mid(){const a=[...pts.values()];return [(a[0][0]+a[1][0])/2,(a[0][1]+a[1][1])/2,Math.hypot(a[0][0]-a[1][0],a[0][1]-a[1][1])];}
  v.addEventListener('pointerdown',e=>{v.setPointerCapture(e.pointerId);pts.set(e.pointerId,[e.clientX,e.clientY]);
   if(pts.size===2){const m=mid();pinch={d:m[2],sc:sc,x:m[0],y:m[1]};drag=null;}else if(pts.size===1){drag={x:e.clientX,y:e.clientY,tx:tx,ty:ty,t:e.timeStamp};}});
  v.addEventListener('pointermove',e=>{if(!pts.has(e.pointerId))return;pts.set(e.pointerId,[e.clientX,e.clientY]);
   if(pts.size===2&&pinch){const m=mid();const f=rel(pinch.x,pinch.y);const ns=Math.max(1,Math.min(6,pinch.sc*m[2]/pinch.d));
    /* Zoom um den Punkt zwischen den Fingern; wandert die Mitte, wandert das Bild mit */
    const k=ns/sc;tx=f[0]-(f[0]-tx)*k+(m[0]-pinch.x);ty=f[1]-(f[1]-ty)*k+(m[1]-pinch.y);sc=ns;pinch.x=m[0];pinch.y=m[1];clamp();ap();}
   else if(pts.size===1&&drag&&sc>1){tx=drag.tx+e.clientX-drag.x;ty=drag.ty+e.clientY-drag.y;clamp();ap();}});
  function up(e){const was=pts.size;pts.delete(e.pointerId);
   if(was===2){pinch=null;const r=[...pts.values()][0];if(r)drag={x:r[0],y:r[1],tx:tx,ty:ty,t:0};return;}
   if(was===1&&drag&&drag.t&&Math.hypot(e.clientX-drag.x,e.clientY-drag.y)<8&&e.timeStamp-drag.t<300){
    if(e.timeStamp-last<350){const f=rel(e.clientX,e.clientY);if(sc>1){reset();}else zoomAt(2.5,f[0],f[1]);last=0;}else last=e.timeStamp;}
   if(pts.size===0){drag=null;pinch=null;}}
  v.addEventListener('pointerup',up);v.addEventListener('pointercancel',up);
  v.addEventListener('wheel',e=>{e.preventDefault();const f=rel(e.clientX,e.clientY);zoomAt(sc*(e.deltaY<0?1.15:.87),f[0],f[1]);},{passive:false});
  addEventListener('keydown',e=>{if(fs.hidden)return;if(e.key==='Escape'){e.stopImmediatePropagation();close();}},true);
 })();
'''
s=s[:a]+js+s[b:]
s=re.sub(r'(<meta name="app-version" content=")([^"]*)(")',lambda m:m.group(1)+'2026-11-02zzz40'+m.group(3),s,count=1)
open(P,'w',encoding='utf-8').write(s)
