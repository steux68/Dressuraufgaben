# Galerie: Vollbild beim Antippen des Bildes (Zoom, Wischen, Pfeile). Idempotent. 01.11.2026
import re
P='index.html';s=open(P,encoding='utf-8').read()
if 'id="gfs"' not in s:
    html='<div id="gfs" hidden role="dialog" aria-modal="true" aria-label="Bild im Vollbild"><div id="gfsv"><img id="gfsi" alt="" draggable="false"></div><button type="button" id="gfsx" aria-label="Vollbild schließen"><svg viewBox="-12 -12 24 24" aria-hidden="true"><circle r="9.5"/><path d="M-3.6 -3.6L3.6 3.6M3.6 -3.6L-3.6 3.6"/></svg></button><button type="button" class="gfa" id="gfp" aria-label="Zurück">W</button><button type="button" class="gfa" id="gfn" aria-label="Weiter">E</button><div id="gfh">Zwei Finger: zoomen · doppelt tippen: Zoom</div></div>'
    s=s.replace('<div class="gpop tlpop" id="gpop"',html+'<div class="gpop tlpop" id="gpop"',1)
    css='''/* galfs */
#gfs{position:fixed;inset:0;z-index:100000;background:#111;touch-action:none}
#gfs[hidden]{display:none}
#gfsv{position:absolute;inset:0;overflow:hidden;display:flex;align-items:center;justify-content:center}
#gfsi{max-width:100%;max-height:100%;transform-origin:0 0;user-select:none;-webkit-user-drag:none;will-change:transform}
#gfsx{position:absolute;top:10px;right:10px;width:44px;height:44px;padding:0;border:0;background:rgba(0,0,0,.55);border-radius:50%!important;cursor:pointer}
#gfsx svg{width:30px;height:30px;fill:none;stroke:#fff;stroke-width:1.6}
.gfa{position:absolute;top:50%;margin-top:-22px;width:44px;height:44px;padding:0;border:2px solid #fff;color:#fff;background:rgba(0,0,0,.55);border-radius:50%!important;font:700 14px/1 inherit;cursor:pointer}
.gfa:disabled{opacity:.25}.gfa[hidden]{display:none}
#gfp{left:8px}#gfn{right:8px}
#gfh{position:absolute;left:0;right:0;bottom:10px;text-align:center;color:#ddd;font-size:12px;pointer-events:none;transition:opacity .6s}
#gpi{cursor:zoom-in}
'''
    i=s.rindex('</style>');s=s[:i]+css+s[i:]
    js='''
 /* Vollbild */
 (function(){const fs=$('gfs'),im=$('gfsi'),v=$('gfsv');let sc=1,tx=0,ty=0,pts=new Map(),d0=0,sc0=1,last=0,drag=null;
  function ap(){im.style.transform='translate('+tx+'px,'+ty+'px) scale('+sc+')';}
  function lim(){const w=im.clientWidth*sc,h=im.clientHeight*sc,vw=v.clientWidth,vh=v.clientHeight,bx=im.offsetLeft,by=im.offsetTop;
   const mx=Math.max(0,(w-vw)/2),my=Math.max(0,(h-vh)/2);const cx=(vw-im.clientWidth)/2-bx,cy=(vh-im.clientHeight)/2-by;
   const ox=(1-sc)*im.clientWidth/2,oy=(1-sc)*im.clientHeight/2;
   tx=Math.max(-mx-ox,Math.min(mx-ox,tx));ty=Math.max(-my-oy,Math.min(my-oy,ty));if(sc<=1){tx=ty=0;}}
  function reset(){sc=1;tx=ty=0;ap();}
  function nav(){$('gfp').disabled=gi===0;$('gfn').disabled=gi===GAL.length-1;$('gfp').hidden=$('gfn').hidden=GAL.length<2;}
  function load(){reset();im.src=GAL[gi].f;im.alt=GAL[gi].n;nav();}
  window.gfsHide=function(){fs.hidden=true;window.gfsOpen=false;};
  function open(){if(!fs.hidden)return;load();fs.hidden=false;window.gfsOpen=true;$('gfh').style.opacity=1;setTimeout(()=>{$('gfh').style.opacity=0},2600);try{history.pushState({app:1,pop:2},'')}catch(e){}}
  function close(){if(history.state&&history.state.pop===2)history.back();else gfsHide();}
  $('gpi').onclick=open;$('gfsx').onclick=close;
  $('gfp').onclick=()=>{if(gi>0){gi--;gShow();load();}};$('gfn').onclick=()=>{if(gi<GAL.length-1){gi++;gShow();load();}};
  v.addEventListener('pointerdown',e=>{v.setPointerCapture(e.pointerId);pts.set(e.pointerId,[e.clientX,e.clientY]);if(pts.size===2){const a=[...pts.values()];d0=Math.hypot(a[0][0]-a[1][0],a[0][1]-a[1][1]);sc0=sc;drag=null;}else{drag=[e.clientX,e.clientY,tx,ty,e.timeStamp];}});
  v.addEventListener('pointermove',e=>{if(!pts.has(e.pointerId))return;pts.set(e.pointerId,[e.clientX,e.clientY]);
   if(pts.size===2){const a=[...pts.values()];const d=Math.hypot(a[0][0]-a[1][0],a[0][1]-a[1][1]);sc=Math.max(1,Math.min(5,sc0*d/d0));lim();ap();}
   else if(drag&&sc>1){tx=drag[2]+e.clientX-drag[0];ty=drag[3]+e.clientY-drag[1];lim();ap();}});
  function up(e){const was=pts.size;pts.delete(e.pointerId);
   if(was===1&&drag&&Math.hypot(e.clientX-drag[0],e.clientY-drag[1])<8&&e.timeStamp-drag[4]<300){if(e.timeStamp-last<350){sc=sc>1?1:2.5;if(sc===1)tx=ty=0;lim();ap();last=0;}else last=e.timeStamp;}
   if(was===1&&sc<=1&&drag&&Math.abs(e.clientX-drag[0])>70&&Math.abs(e.clientY-drag[1])<50){(e.clientX<drag[0]?$('gfn'):$('gfp')).click();}
   if(pts.size===0)drag=null;}
  v.addEventListener('pointerup',up);v.addEventListener('pointercancel',up);
  v.addEventListener('wheel',e=>{e.preventDefault();sc=Math.max(1,Math.min(5,sc*(e.deltaY<0?1.15:.87)));lim();ap();},{passive:false});
  addEventListener('keydown',e=>{if(fs.hidden)return;e.stopImmediatePropagation();if(e.key==='Escape')close();if(e.key==='ArrowLeft')$('gfp').click();if(e.key==='ArrowRight')$('gfn').click();},true);
 })();
'''
    k="\n window.galGrid=grid;"
    assert k in s
    s=s.replace(k,js+k,1)
    o="addEventListener('popstate',()=>{if(!$('gpop').hidden)gClose();});"
    assert o in s
    s=s.replace(o,"addEventListener('popstate',()=>{if(window.gfsOpen){gfsHide();return;}if(!$('gpop').hidden)gClose();});",1)
s=re.sub(r'(<meta name="app-version" content=")([^"]*)(")',lambda m:m.group(1)+'2026-11-01zzz35'+m.group(3),s,count=1)
open(P,'w',encoding='utf-8').write(s)
