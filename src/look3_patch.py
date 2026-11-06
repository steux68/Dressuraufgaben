# 06.11.2026: (1) Pferdewissen hellgrau hinterlegt (Startseiten-Abschnitt #p-w und Wissen-Ansicht #theo), (2) Reiter-Balken werden gelb, sobald sie den unteren Stapel verlassen (nicht erst am oberen Anschlag),
# (3) "interaktiv" mit dem pulsierenden Punkt vom Cursor der dasein-Website (limettengelber Punkt, rote Ringe). Idempotent.
import re,sys
s=open('index.html',encoding='utf-8').read()
def rep(old,new):
    global s
    if new in s: return
    assert s.count(old)==1,(s.count(old),old[:80])
    s=s.replace(old,new)
# (2) Balken
rep("BARS.forEach((b,k)=>{if(b.getBoundingClientRect().top<=R0.top+parseFloat(b.style.top)+1)c=k;});",
    "BARS.forEach((b,k)=>{if(isUp(b))c=k;});")
# (1) Wissen-Ansicht: Merker am #theo
rep("general(){group(true);isOn=true;","general(){group(true);isOn=true;g('theo').dataset.k='w';")
rep("on(){isOn=true;MAIN.forEach(id=>g(id).hidden=true);g('theo').hidden=false;","on(){isOn=true;delete g('theo').dataset.k;MAIN.forEach(id=>g(id).hidden=true);g('theo').hidden=false;")
rep("history(){group('h');isOn=true;","history(){group('h');isOn=true;delete g('theo').dataset.k;")
# (3) Punkt neben dem Wort
rep("const ip=el('p','tline intro');ip.append(el('span','inter',lang==='en'?'interactive':'interaktiv'),' '+t().gal);",
    "const ip=el('p','tline intro');const iw=el('span','inter',lang==='en'?'interactive':'interaktiv');iw.prepend(el('i','idot'));ip.append(iw,' '+t().gal);")
rep("const w=document.createElement('span');w.className='inter';w.textContent='interaktiv';ln.append(w,",
    "const w=document.createElement('span');w.className='inter';w.textContent='interaktiv';{const d=document.createElement('i');d.className='idot';w.prepend(d);}ln.append(w,")
CSS="""
/* 06.11.2026 look3: Pferdewissen hellgrau; "interaktiv" mit dem Cursor-Punkt der dasein-Seite */
#p-w{background:#f4f4f4}
#theo[data-k="w"]{background:#f4f4f4}
.inter{display:inline-flex;align-items:center;gap:9px;padding:0;margin-right:6px;border:0}
.inter::before,.inter::after{content:none!important;animation:none!important;border:0!important}
.idot{position:relative;flex:none;width:9px;height:9px;border-radius:50%;background:#d4fb4d;box-shadow:inset 0 0 0 .5px #e30613;animation:idotp 1.4s ease-in-out infinite}
.idot::before,.idot::after{content:"";position:absolute;left:50%;top:50%;width:9px;height:9px;margin:-4.5px 0 0 -4.5px;border-radius:50%;border:.6px solid #e30613;box-sizing:border-box;opacity:0;animation:idotr 1.4s ease-out infinite}
.idot::after{animation-delay:.7s}
@keyframes idotp{50%{transform:scale(.75)}}
@keyframes idotr{from{transform:scale(1);opacity:.8}to{transform:scale(4.4);opacity:0}}
@media (prefers-reduced-motion:reduce){.idot,.idot::before,.idot::after{animation:none}.idot::before,.idot::after{display:none}}
"""
if '/* 06.11.2026 look3' not in s:
    i=s.rindex("</style>");s=s[:i]+CSS+s[i:]
if '--noversion' not in sys.argv:
    s=re.sub(r'(<meta name="app-version" content=")([^"]*)(")',lambda m:m.group(1)+'2026-11-06zzz71'+m.group(3),s,count=1)
open('index.html','w',encoding='utf-8').write(s)
