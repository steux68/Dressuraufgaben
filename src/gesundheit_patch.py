# Pferdewissen: neuer Reiter "Gesundheit" (Vitalwerte, Kolik, Tierarzt, Taeglicher Check). Orientierung fuer Reiter, kein Ersatz fuer den Tierarzt. Idempotent. 02.11.2026
import re,sys
s=open('index.html',encoding='utf-8').read()
if 'id="thsGe"' in s: sys.exit('schon angewendet')
def rep(old,new):
    global s
    assert s.count(old)==1,old[:70]
    s=s.replace(old,new,1)
rep('<button id="thsK" aria-pressed="false">Körpersprache</button>','<button id="thsK" aria-pressed="false">Körpersprache</button>\n<button id="thsGe" aria-pressed="false">Gesundheit</button>')
rep('<div class="tp" id="thBody" hidden></div>','<div class="tp" id="thBody" hidden></div>\n<div class="tp" id="thGes" hidden></div>')
rep("'thsV','thsK','thsA','thsB','thsH'","'thsV','thsK','thsGe','thsA','thsB','thsH'")
rep("SUBG=['thsS','thsV','thsK','thsA','thsB']","SUBG=['thsS','thsV','thsK','thsGe','thsA','thsB']")
rep("g('thBody').hidden=which!=='thsK';","g('thBody').hidden=which!=='thsK';g('thGes').hidden=which!=='thsGe';")
rep("['thsP','thsH','thsZ','thsA','thsB','thsK'].includes(which)","['thsP','thsH','thsZ','thsA','thsB','thsK','thsGe'].includes(which)")
rep("else if(which==='thsK')bodyLang();","else if(which==='thsK')bodyLang();else if(which==='thsGe')health();")
rep("  ['thsA','An','Anatomie',","  ['thsGe','Ge','Gesundheit','Puls, Atmung, Temperatur, Kolik: normal oder Tierarzt?'],\n  ['thsA','An','Anatomie',")
JS=r"""
const GE=[
 {k:'Normalwerte',t:'Normalwerte in Ruhe',rows:[
  ['Puls','28 bis 44 Schläge pro Minute. Fühlen an der Innenseite des Unterkiefers oder mit dem Stethoskop hinter dem Ellbogen. Eine halbe Minute zählen und mal 2 rechnen.'],
  ['Atmung','8 bis 16 Atemzüge pro Minute. Die Flanke hebt und senkt sich, ein Zug = heben und senken.'],
  ['Temperatur','37,5 bis 38,2 °C, rektal mit einem Digitalthermometer (festhalten, Schweif zur Seite).'],
  ['Schleimhaut','Zahnfleisch blassrosa und feucht. Daumendruck: nach 1 bis 2 Sekunden wieder rosa.']]},
 {k:'Täglicher Check',t:'Der tägliche Blick',rows:[
  ['Verhalten','Munter, frisst gierig, interessiert sich für die Umgebung.'],
  ['Augen und Nase','Klar und offen, kein Ausfluss, kein Husten.'],
  ['Beine und Hufe','Keine Wärme, keine Schwellung, Pferd geht gleichmäßig.'],
  ['Kot und Wasser','Kot in normaler Menge und Form, das Pferd säuft.'],
  ['Haut','Keine Wunden, Schwellungen oder Scheuerstellen vom Sattel.']]},
 {k:'Kolik',t:'Kolik: Warnzeichen',rows:[
  ['Unruhe','Scharren, Blick oder Biss zum Bauch, Schlagen mit dem Schweif, häufiges Hinlegen und Aufstehen.'],
  ['Wälzen','Das Pferd wirft sich hin und wälzt sich oder steht gestreckt.'],
  ['Schwitzen','Nass geschwitzt ohne Anstrengung, schnelle Atmung.'],
  ['Kein Fressen, kein Kot','Futter bleibt liegen, die Därme sind still.'],
  ['Was tun?','Sofort den Tierarzt rufen und den Stallbesitzer holen. Nicht reiten, nichts füttern. Ruhig führen, wenn es sich nicht hinwirft. Puls und Atmung zählen und dem Tierarzt sagen.']]},
 {k:'Tierarzt',t:'Wann sofort zum Tierarzt?',rows:[
  ['Sofort','Kolik-Zeichen, starke Lahmheit, tiefe Wunden, Fieber über 38,5 °C, Atemnot, Pferd steht nicht auf, Augenverletzung.'],
  ['Am selben Tag','Verweigert Futter, Husten mit Ausfluss, dicke Beine, anhaltender Durchfall.'],
  ['Merke','Im Zweifel anrufen. Lieber einmal zu viel als zu spät.']]}
];
let gei=0;
function health(){
 const root=g('thGes');root.innerHTML='';
 const seg=document.createElement('div');seg.className='anaSeg blseg';
 GE.forEach((b,i)=>{const x=document.createElement('button');x.type='button';x.textContent=b.k;x.setAttribute('aria-pressed',i===gei);x.onclick=()=>{gei=i;[...seg.children].forEach((c,j)=>c.setAttribute('aria-pressed',j===i));fill(i);};seg.appendChild(x);});
 const card=document.createElement('div');card.className='card blcard';
 const note=document.createElement('p');note.className='tline';
 note.textContent='Orientierung für Reiter, kein Ersatz für den Tierarzt. Werte gelten für erwachsene Pferde in Ruhe. Entwurf, mit Reitlehrer oder Tierarzt abgleichen.';
 const fill=i=>{const b=GE[i];card.innerHTML='';const h=document.createElement('p');h.className='blt';h.textContent=b.t;card.appendChild(h);
  const dl=document.createElement('dl');dl.className='bldl';b.rows.forEach(r=>{const dt=document.createElement('dt');dt.textContent=r[0];const dd=document.createElement('dd');dd.textContent=r[1];dl.appendChild(dt);dl.appendChild(dd);});card.appendChild(dl);};
 root.appendChild(seg);root.appendChild(card);root.appendChild(note);
 const lock=()=>{card.style.minHeight='';let m=0;for(let i=0;i<GE.length;i++){fill(i);m=Math.max(m,card.offsetHeight);}card.style.minHeight=m+'px';fill(gei);};
 fill(gei);lock();if(document.fonts&&document.fonts.ready)document.fonts.ready.then(()=>{if(!g('thGes').hidden)lock();});
}
"""
rep("function hist(){",JS+"function hist(){")
CSS="#thGes .blcard{padding:12px 14px;margin:0 0 8px}#thGes .blt{margin:0 0 8px;color:#e30613;text-transform:uppercase;font-weight:700;font-size:1.35rem;line-height:1.15;letter-spacing:.01em}#thGes .bldl{margin:0;padding:6px 0 0;border-top:1px dotted #b8b8b8}#thGes .bldl dt{margin:10px 0 2px;font-weight:700;font-size:.98rem;color:#111}#thGes .bldl dd{margin:0;font-size:.98rem;line-height:1.4;color:#222}\n"
i=s.rindex("</style>");s=s[:i]+CSS+s[i:]
if '--noversion' not in sys.argv:
    s=re.sub(r'(<meta name="app-version" content=")([^"]*)(")',lambda m:m.group(1)+'2026-11-02zzz60'+m.group(3),s,count=1)
open('index.html','w',encoding='utf-8').write(s)
