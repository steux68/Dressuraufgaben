# Koerpersprache/Ohren: drei Ohrenpositionen als Bild (KI-generiert von Steuart Harrison mit Gemini) + Kachel-Ausschnitt. Idempotent. 07.11.2026
import re,sys
s=open('index.html',encoding='utf-8').read()
if 'koerper_ohren_1.jpg' in s: sys.exit('schon angewendet')
def rep(old,new):
    global s
    assert s.count(old)==1,old[:60]
    s=s.replace(old,new,1)
i=s.index("card.appendChild(dl);};")
assert s.rfind("const fill=i=>{const b=BL[i]",0,i)>s.rfind("const fill=i=>{const b=GE[i]",0,i)
s=s[:i]+"card.appendChild(dl);if(b.k==='Ohren')ohrenBilder(card);};"+s[i+len("card.appendChild(dl);};"):]
rep("let bli=0;",r"""const OHR=[['img/koerper_ohren_1.jpg','Pferdekopf mit nach vorn gerichteten Ohren'],['img/koerper_ohren_2.jpg','Pferdekopf mit seitlich gestellten Ohren'],['img/koerper_ohren_3.jpg','Pferdekopf mit eng angelegten Ohren']];
function ohrenBilder(card){const f=document.createElement('div');f.className='ohrfig';OHR.forEach(([u,a])=>{const i=document.createElement('img');i.src=u;i.alt=a;i.loading='lazy';i.width=440;i.height=460;f.appendChild(i);});
 const c=document.createElement('p');c.className='tline ohrcap';c.textContent='Bild: KI-generiert (Gemini) im Auftrag von Steuart Harrison, frei verwendbar.';f.appendChild(c);card.insertBefore(f,card.children[1]);}
let bli=0;""")
rep("thsB:'img/viereck_real.svg',","thsB:'img/viereck_real.svg',thsK:'img/koerper_ohren_1.jpg',")
rep("thsB:'#fff url(img/viereck_real.svg) 22% 58%/185% no-repeat',","thsB:'#fff url(img/viereck_real.svg) 22% 58%/185% no-repeat',thsK:'#fff url(img/koerper_ohren_1.jpg) 52% 16%/289% no-repeat',")
CSS='''<style id="ohren-css">
.ohrfig{display:flex;flex-direction:column;gap:8px;margin:8px 0}
.ohrfig img{display:block;width:100%;height:auto;box-sizing:border-box;border:1px dotted #b8b8b8;background:#fff}
.ohrfig .ohrcap{margin:0;font-size:12px;color:var(--muted)}
</style>
'''
assert s.count('</head>')==1
s=s.replace('</head>',CSS+'</head>',1)
if '--noversion' not in sys.argv:
    s=re.sub(r'(<meta name="app-version" content=")([^"]*)(")',lambda m:m.group(1)+'2026-11-07zzz109'+m.group(3),s,count=1)
open('index.html','w',encoding='utf-8').write(s)
