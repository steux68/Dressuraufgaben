import sys,re
path,prefix,ver_mode,ver=sys.argv[1:5]
s=open(path,encoding='utf-8').read()
if 'id="barfx-css"' in s: print('schon da'); sys.exit(0)
P=prefix  # selector prefix, e.g. '' or '.stack main > '
CSS=f'''<style id="barfx-css">
/* 19.11: Mikro-Animation der Menüleisten wie in DOCH!: beim Halten wölbt sich die Leiste (Höhe x1,5, Schrift x1,3), federt beim Loslassen zurück;
   rastet eine Leiste oben ein, kurz grösser, dann kleiner, dann fest. Nur transform, kein Layout-Sprung. */
{P}.hb{{transition:transform .38s cubic-bezier(.3,1.7,.5,1)}}
{P}.hb>b,{P}.hb>small{{transform-origin:left center;transition:font-size .38s cubic-bezier(.3,1.7,.5,1),transform .38s cubic-bezier(.3,1.7,.5,1)}}
{P}.hb.hold{{z-index:40;transform:scale(1,1.5);transition:transform .2s cubic-bezier(.2,1.3,.4,1)}}
{P}.hb.hold>b{{font-size:16.2px;transform:scale(1,.667);transition:font-size .2s cubic-bezier(.2,1.3,.4,1),transform .2s cubic-bezier(.2,1.3,.4,1)}}
{P}.hb.hold>small{{transform:scale(1.3,.867);transition:transform .2s cubic-bezier(.2,1.3,.4,1)}}
{P}.hb.lock:not(.hold){{z-index:40;animation:blk .6s ease-out}}
{P}.hb.lock:not(.hold)>b{{animation:blkb .6s ease-out}}{P}.hb.lock:not(.hold)>small{{animation:blkt .6s ease-out}}
@keyframes blk{{0%{{transform:scale(1,1)}}32%{{transform:scale(1,1.5)}}68%{{transform:scale(1,.9)}}100%{{transform:scale(1,1)}}}}
@keyframes blkb{{0%{{font-size:12.5px;transform:none}}32%{{font-size:16.2px;transform:scale(1,.667)}}68%{{font-size:11.9px;transform:scale(1,1.11)}}100%{{font-size:12.5px;transform:none}}}}
@keyframes blkt{{0%{{transform:none}}32%{{transform:scale(1.3,.867)}}68%{{transform:scale(.95,1.11)}}100%{{transform:none}}}}
@media (prefers-reduced-motion:reduce){{{P}.hb,{P}.hb>b,{P}.hb>small{{transition:none!important;animation:none!important}}}}
</style>
<script id="barfx-js">(function(){{
var held=[],t0=0,stuck=new WeakMap(),scm=new WeakMap(),raf=0,ready=0;
function on(e){{var b=e.target&&e.target.closest?e.target.closest(".hb"):null;if(!b)return;b.classList.remove("lock");b.classList.add("hold");held.push(b);t0=Date.now();}}
function off(){{var l=held;held=[];if(!l.length)return;var w=Math.max(0,170-(Date.now()-t0));setTimeout(function(){{l.forEach(function(b){{b.classList.remove("hold")}})}},w);}}
document.addEventListener("touchstart",on,{{passive:true,capture:true}});
document.addEventListener("mousedown",on,true);
["touchend","touchcancel","mouseup","dragend","blur"].forEach(function(n){{addEventListener(n,off,true)}});
function scr(b){{var c=scm.get(b);if(c!==undefined)return c;var e=b;c=null;while((e=e.parentElement)){{var o=getComputedStyle(e).overflowY;if(o==="auto"||o==="scroll"){{c=e;break}}}}scm.set(b,c);return c;}}
function check(){{raf=0;var bars=document.querySelectorAll(".hb"),i,b,r,c,ct,top,s;
 for(i=0;i<bars.length;i++){{b=bars[i];r=b.getBoundingClientRect();c=scr(b);ct=c?c.getBoundingClientRect().top:0;top=parseFloat(getComputedStyle(b).top);if(isNaN(top))top=0;
  s=r.height>0&&r.top<=ct+top+1&&r.top>=ct-2;
  if(ready&&s&&stuck.get(b)===false&&!b.classList.contains("hold")){{b.classList.remove("lock");void b.offsetWidth;b.classList.add("lock");(function(x){{setTimeout(function(){{x.classList.remove("lock")}},700)}})(b);}}
  stuck.set(b,s);}}
 ready=1;}}
document.addEventListener("scroll",function(){{if(!raf)raf=requestAnimationFrame(check)}},{{passive:true,capture:true}});
setTimeout(check,300);
}})();</script>
'''
i=s.rindex('</body>'); s=s[:i]+CSS+s[i:]
if ver_mode=='meta':
    s=re.sub(r'(<meta name="app-version" content=")([^"]*)(")',lambda m:m.group(1)+ver+m.group(3),s,count=1)
open(path,'w',encoding='utf-8').write(s); print('ok')
