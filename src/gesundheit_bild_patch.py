# Gesundheit/Normalwerte: Bild (KI-generiert von Steuart Harrison, Gemini) + Kachel-Ausschnitt. Idempotent. 07.11.2026
import re,sys
s=open('index.html',encoding='utf-8').read()
if 'gesundheit_check.jpg' in s: sys.exit('schon angewendet')
def rep(old,new):
    global s
    assert s.count(old)==1,old[:60]
    s=s.replace(old,new,1)
i=s.index("card.appendChild(dl);};",s.index("const fill=i=>{const b=GE[i]"))
s=s[:i]+"card.appendChild(dl);if(b.k==='Normalwerte')gesBild(card);};"+s[i+len("card.appendChild(dl);};"):]
rep("function ohrenBilder(card){",r"""function gesBild(card){const f=document.createElement('div');f.className='ohrfig';const i=document.createElement('img');i.src='img/gesundheit_check.jpg';i.alt='Pferdeskelett mit den Normalwerten in Ruhe: Puls, Atmung, Temperatur und Schleimhaut';i.loading='lazy';i.width=955;i.height=485;f.appendChild(i);
 const c=document.createElement('p');c.className='tline ohrcap';c.textContent='Bild: KI-generiert (Gemini) im Auftrag von Steuart Harrison, frei verwendbar. Die Werte stehen auch im Text unten.';f.appendChild(c);card.insertBefore(f,card.children[1]);}
function ohrenBilder(card){""")
rep("thsS:'img/situationen_icon.jpg',","thsS:'img/situationen_icon.jpg',thsGe:'img/gesundheit_check.jpg',")
rep("thsS:'#fff url(img/situationen_icon.jpg) center/cover no-repeat',","thsS:'#fff url(img/situationen_icon.jpg) center/cover no-repeat',thsGe:'#fff url(img/gesundheit_check.jpg) 42% 22%/217% no-repeat',")
if '--noversion' not in sys.argv:
    s=re.sub(r'(<meta name="app-version" content=")([^"]*)(")',lambda m:m.group(1)+'2026-11-07zzz111'+m.group(3),s,count=1)
open('index.html','w',encoding='utf-8').write(s)
