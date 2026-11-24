# Zitate-Liste (Pferdewissen, Reiter Zitate): Portraits fuer Xenophon und Seneca (eigene Bilder, Credits in der Galerie). 24.11.2026
import re,sys
s=open('index.html',encoding='utf-8').read()
if 'zitate-portrait-css' in s: sys.exit('schon angewendet')
A="p.className='pic';p.setAttribute('aria-hidden','true');p.textContent=z.i;"
assert s.count(A)==2
s=s.replace(A,A+"zPort(p,z.who);")
F="function quotes(){"
assert s.count(F)==1
s=s.replace(F,"const ZP={'Xenophon':'img/zitate/xenophon_buste_q.jpg','Seneca':'img/zitate/seneca_gemaelde.jpg'};\nfunction zPort(p,who){const u=ZP[who];if(!u)return;const im=document.createElement('img');im.alt='';im.onload=()=>{p.textContent='';p.classList.add('has');p.appendChild(im);};im.src=u;}\n"+F)
CSS='<style id="zitate-portrait-css">#theo2 .zq .pic.has,#theo3 .zq .pic.has{padding:0;overflow:hidden;background:#ddd!important}#theo2 .zq .pic img,#theo3 .zq .pic img{width:100%;height:100%;object-fit:cover;display:block}</style>\n'
i=s.rindex('</head>'); s=s[:i]+CSS+s[i:]
s=re.sub(r'(<meta name="app-version" content=")[^"]*"',r'\g<1>2026-11-24i"',s,count=1)
open('index.html','w',encoding='utf-8').write(s)
