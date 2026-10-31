"""P a–x: (1) Abstand über jeder Kapitelleiste 39 → 22 px (gleich wie in der Deutsch-App),
(2) keine Doppellinie über der „mehr Zitate“-Leiste: endet die Liste schon mit einer gepunkteten Linie, entfällt die obere Linie der Leiste (.zmore.nl).
Aufruf im Repo-Hauptordner: python3 src/spacing_pax_patch.py  (idempotent)"""
import re,sys
f='index.html'; s=open(f,encoding='utf8').read()
if '.zmore.nl' in s: sys.exit('schon angewendet')
def rep(a,b):
    global s
    assert s.count(a)==1,a[:70]; s=s.replace(a,b,1)
rep('.hb.hl{margin:39px 50% -1px 0;','.hb.hl{margin:22px 50% -1px 0;')
rep('.hb.hr{margin:39px 0 -1px calc(50% - 1px);','.hb.hr{margin:22px 0 -1px calc(50% - 1px);')
rep('@keyframes zcp{','.zmore.nl{margin-top:0;background:repeating-linear-gradient(to right,#b8b8b8 0 1px,transparent 1px 3px) left bottom/100% 1px no-repeat,#fff}@keyframes zcp{')
FN=("<script id=\"zm-dedup\">window.zmDedup=function(zm){if(!zm)return;zm.classList.remove('nl');const pv=zm.previousElementSibling,T=zm.getBoundingClientRect().top;if(!pv||!T)return;"
    "for(const e of pv.querySelectorAll('*')){const r=e.getBoundingClientRect();if(!r.height||r.bottom>T+1||r.bottom<T-9)continue;const cs=getComputedStyle(e);"
    "if(/gradient/.test(cs.backgroundImage)||(cs.borderBottomStyle!=='none'&&parseFloat(cs.borderBottomWidth)>0)){zm.classList.add('nl');return;}}};"
    "(function(){const all=()=>document.querySelectorAll('.zmore').forEach(window.zmDedup);[0,300,1200,3000].forEach(t=>setTimeout(all,t));addEventListener('load',all);addEventListener('resize',all);})();</script>")
rep("const zm=c.querySelector('.zmore');if(zm)zm.onclick=","const zm=c.querySelector('.zmore');window.zmDedup&&window.zmDedup(zm);if(zm)zm.onclick=")
rep('<script id="sw-reg">',FN+'<script id="sw-reg">')
mm=re.search(r'(<meta name="app-version" content=")(\d{4}-\d{2}-\d{2})([a-z]+)(">)',s); nv=mm.group(3)[:-1]+chr(ord(mm.group(3)[-1])+1)
s=s.replace(mm.group(0),mm.group(1)+mm.group(2)+nv+mm.group(4),1)
open(f,'w',encoding='utf8').write(s); print('ok ->',mm.group(2)+nv)
