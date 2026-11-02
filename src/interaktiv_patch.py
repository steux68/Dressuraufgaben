# Interaktiv-Hinweis: statische gelbe Punkte auf den Anatomie-Kacheln + Wort "interaktiv" mit sanftem gelbem Ring (nur dieses Wort pulsiert). Idempotent. 02.11.2026
import re,sys
s=open('index.html',encoding='utf-8').read()
if 'placeDots' in s: sys.exit('schon angewendet')
def rep(old,new):
    global s
    assert old in s,old[:70]
    s=s.replace(old,new,1)
# 1) Galerie: Hinweiszeile mit pulsierendem Wort + Punkte auf den Kacheln
rep("R.append(g,el('p','tline',t().more));}",
"""const ip=el('p','tline intro');ip.append(el('span','inter',lang==='en'?'interactive':'interaktiv'),' '+t().gal);
 R.append(ip,g,el('p','tline',t().more));placeDots(g);
 if(window.ResizeObserver){if(window._agRO)window._agRO.disconnect();window._agRO=new ResizeObserver(()=>placeDots(g));window._agRO.observe(g);}}
function placeDots(g){requestAnimationFrame(()=>{g.querySelectorAll('.agc').forEach((b,i)=>{const s=SETS[i],im=b.querySelector('.agi');if(!s||!im)return;
  im.querySelectorAll('.agd').forEach(d=>d.remove());const w=im.clientWidth,h=im.clientHeight;if(!w||!h)return;
  const sc=Math.max(w/s.W,h/s.H),tk=(s.pos||'center 50%').split(' '),fx=tk[0]==='center'?.5:parseFloat(tk[0])/100,fy=tk[1]?parseFloat(tk[1])/100:.5;
  const ox=(w-s.W*sc)*(isNaN(fx)?.5:fx),oy=(h-s.H*sc)*(isNaN(fy)?.5:fy),n=s.P.length,k=Math.min(5,n);
  for(let j=0;j<k;j++){const p=s.P[Math.floor(j*n/k)],x=ox+p[3]*sc,y=oy+p[4]*sc;if(x<5||y<5||x>w-5||y>h-5)continue;
   const d=el('span','agd');d.style.left=x+'px';d.style.top=y+'px';im.appendChild(d);}});});}""")
# 2) Startseite von Pferdewissen: Hinweiszeile vor die erste Kachel
rep("  b.onclick=()=>{openWissen();setTimeout(()=>$(id).click(),0);};PW.appendChild(b);});",
"""  b.onclick=()=>{openWissen();setTimeout(()=>$(id).click(),0);};PW.appendChild(b);});
 {const ln=document.createElement('p');ln.className='tline intro';const w=document.createElement('span');w.className='inter';w.textContent='interaktiv';ln.append(w,' Tippe auf Bilder, Punkte und Quiz.');PW.insertBefore(ln,PW.querySelector('.tile'));}""")
CSS="""
.agi{position:relative}
.agd{position:absolute;width:8px;height:8px;margin:-4px 0 0 -4px;border-radius:50%;background:#ffd400;border:1px solid #e30613;pointer-events:none}
.tline.intro{margin:6px 0 10px;text-align:center}\n#p-w .tline.intro{font-size:.85rem;color:var(--muted)}
.inter{position:relative;display:inline-block;padding:1px 9px;margin-right:4px;color:#e30613;font-weight:700;font-size:.78rem;letter-spacing:.14em;text-transform:uppercase;line-height:1.5}
.inter::before{content:"";position:absolute;inset:0;border:1px solid #ffd400;border-radius:999px;pointer-events:none}
@media (prefers-reduced-motion:no-preference){.inter::after{content:"";position:absolute;inset:0;border:1.5px solid #ffd400;border-radius:999px;pointer-events:none;animation:interp 2.6s ease-out infinite}}
@keyframes interp{0%{transform:scale(1);opacity:.95}100%{transform:scale(1.28,1.9);opacity:0}}
"""
i=s.rindex("</style>");s=s[:i]+CSS+s[i:]
if '--noversion' not in sys.argv:
    s=re.sub(r'(<meta name="app-version" content=")([^"]*)(")',lambda m:m.group(1)+'2026-11-02zzz54'+m.group(3),s,count=1)
open('index.html','w',encoding='utf-8').write(s)
