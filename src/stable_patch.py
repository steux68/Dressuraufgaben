# Stabil: Diagramme springen nicht mehr. Die Textboxen (Karten, "Warum?"-Zeile) reservieren die Hoehe des laengsten Eintrags,
# damit die Flaeche fuer das Diagramm immer gleich gross bleibt. Gilt fuer Sehen (Karten + Quiz) und Figuren (Karten + Quiz). Idempotent. 02.11.2026
import re,sys
s=open('index.html',encoding='utf-8').read()
if 'function lockAll()' not in s:
    js='''/* Stabil: laengster Text bestimmt die Hoehe, nichts springt */
function lockCard(card,fill,n,back){card.style.minHeight='';let m=0;for(let k=0;k<n;k++){fill(k);m=Math.max(m,card.offsetHeight);}card.style.minHeight=m+'px';back();}
function lockWhy(fb,wy,texts){const w=g(wy),f=g(fb);f.style.minHeight='';w.style.minHeight='';const keep=w.innerHTML;let m=0;texts.forEach(t=>{why(wy,t);m=Math.max(m,w.offsetHeight);});w.innerHTML=keep;m=Math.max(m,f.offsetHeight);f.style.minHeight=m+'px';w.style.minHeight=m+'px';}
function lockAll(){
 if(g('theo').hidden)return;
 if(!g('thSee').hidden){
  if(!g('thVlearn').hidden)lockCard(g('thVlearn').querySelector('.card'),k=>{g('thVnm').textContent=V[k].n;g('thVds').textContent=V[k].d;},V.length,()=>seeShow());
  else if(!g('thVquiz').hidden)lockWhy('thVfb','thVwhy',Object.values(VW));
 }
 if(!g('thLearn').hidden)lockCard(g('thLearn').querySelector('.card'),k=>{const f=F[k];g('thNm').textContent=f.n;g('thDs').textContent=f.d;g('thDe').textContent=f.g?(f.g.startsWith('Österr')?f.g:'Deutsch (FN): '+f.g):'';},F.length,()=>showLearn());
 if(!g('thGame').hidden)lockWhy('thFb','thWhy',F.map(f=>f.d));
}
let lockT=0;function lockSoon(){clearTimeout(lockT);lockT=setTimeout(()=>requestAnimationFrame(lockAll),60);}
addEventListener('resize',lockSoon);addEventListener('orientationchange',lockSoon);
if(document.fonts&&document.fonts.ready)document.fonts.ready.then(lockSoon);
'''
    anchor='const MAIN=[\'lg\',\'stage\',\'panels\'];'
    assert anchor in s
    s=s.replace(anchor,js+anchor,1)
    # Aufruf nach Wechsel der Unterseite und des Sehen-Modus
    old="else if(!wip)qask();\n}\nSUBS.forEach"
    assert old in s
    s=s.replace(old,"else if(!wip)qask();\n lockSoon();\n}\nSUBS.forEach",1)
    old2="function seeMode(m){vMode=m;"
    assert old2 in s
    s=s.replace(old2,old2+"lockSoon();",1)

# Anatomie-Panel: feste Mindesthoehe, damit der Kasten beim Wechsel der Punkte nicht waechst und schrumpft
if '.tlpop .anaPanel{min-height' not in s:
    k='.tlpop .tlbody p{font-size:.98rem;line-height:1.45;color:#222}'
    assert k in s
    s=s.replace(k,k+'\n.tlpop .anaPanel{min-height:10.4rem}',1)
if '--noversion' not in sys.argv:
    s=re.sub(r'(<meta name="app-version" content=")([^"]*)(")',lambda m:m.group(1)+'2026-11-02zzz42'+m.group(3),s,count=1)
open('index.html','w',encoding='utf-8').write(s)
