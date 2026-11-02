# Anatomie: Auswahl nach Thema (Alle, Koerper, Beine, Huf, Kopf und Auge) ueber den Kacheln. Idempotent. 02.11.2026
import re,sys
s=open('index.html',encoding='utf-8').read()
if 'galGrp' in s: sys.exit('schon angewendet')
def rep(old,new):
    global s
    assert old in s,old[:70]
    s=s.replace(old,new,1)
rep("R.append(ip,g,el('p','tline',t().more));placeDots(g);",
"""const GR={sk:'Körper',ex:'Körper',hb:'Beine',hz:'Beine',fe:'Beine',hf:'Huf',hr:'Huf',hg:'Huf',hi:'Huf',ko:'Kopf und Auge',uk:'Kopf und Auge',au:'Kopf und Auge',ap:'Kopf und Auge'};
 const GN=['Alle','Körper','Beine','Huf','Kopf und Auge'],gs=el('div','anaSeg blseg');
 const apply=()=>{[...g.children].forEach((b,i)=>{b.hidden=!(window.galGrp==='Alle'||GR[SETS[i].k]===window.galGrp);});[...gs.children].forEach(c=>c.setAttribute('aria-pressed',c.textContent===window.galGrp));placeDots(g);};
 if(!window.galGrp)window.galGrp='Alle';
 GN.forEach(n=>{const x=el('button',null,lang==='en'?({'Alle':'All','Körper':'Body','Beine':'Legs','Huf':'Hoof','Kopf und Auge':'Head and eye'}[n]):n);x.type='button';x.textContent=lang==='en'?x.textContent:n;x.dataset.g=n;x.onclick=()=>{window.galGrp=n;apply();};gs.appendChild(x);});
 R.append(ip,gs,g,el('p','tline',t().more));
 [...gs.children].forEach(c=>c.setAttribute('aria-pressed',c.dataset.g===window.galGrp));
 const apply2=()=>{[...g.children].forEach((b,i)=>{b.hidden=!(window.galGrp==='Alle'||GR[SETS[i].k]===window.galGrp);});[...gs.children].forEach(c=>c.setAttribute('aria-pressed',c.dataset.g===window.galGrp));placeDots(g);};
 [...gs.children].forEach(c=>{c.onclick=()=>{window.galGrp=c.dataset.g;apply2();};});apply2();""")
CSS="\n.anaSeg.blseg{margin:2px 0 12px}\n.agc[hidden]{display:none}\n"
i=s.rindex("</style>");s=s[:i]+CSS+s[i:]
if '--noversion' not in sys.argv:
    s=re.sub(r'(<meta name="app-version" content=")([^"]*)(")',lambda m:m.group(1)+'2026-11-02zzz56'+m.group(3),s,count=1)
open('index.html','w',encoding='utf-8').write(s)
