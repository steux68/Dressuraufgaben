# Pferdewissen: neuer Reiter "Koerpersprache" (Ohren, Augen, Maul, Schweif, Haltung). Eigene Formulierungen nach allgemeinen Verhaltensratgebern. Idempotent. 02.11.2026
import re,sys
s=open('index.html',encoding='utf-8').read()
if 'id="thsK"' in s: sys.exit('schon angewendet')
def rep(old,new,cnt=1):
    global s
    assert s.count(old)>=1,old[:60]
    s=s.replace(old,new,cnt)
# 1) Reiter-Knopf
rep('<button id="thsV" aria-pressed="false">Sehen</button>','<button id="thsV" aria-pressed="false">Sehen</button>\n<button id="thsK" aria-pressed="false">Körpersprache</button>')
# 2) Container
rep('<div class="tp" id="thHorse" hidden>','<div class="tp" id="thBody" hidden></div>\n<div class="tp" id="thHorse" hidden>')
# 3) Listen und sub()
rep("const SUBS=['thsF','thsG','thsQ','thsS','thsV','thsA'","const SUBS=['thsF','thsG','thsQ','thsS','thsV','thsK','thsA'")
rep("SUBG=['thsS','thsV','thsA'","SUBG=['thsS','thsV','thsK','thsA'")
rep("g('thHorse').hidden=which!=='thsP';","g('thHorse').hidden=which!=='thsP';g('thBody').hidden=which!=='thsK';")
rep("['thsP','thsH','thsZ','thsA','thsB'].includes(which)","['thsP','thsH','thsZ','thsA','thsB','thsK'].includes(which)")
rep("else if(which==='thsP')horses();","else if(which==='thsP')horses();else if(which==='thsK')bodyLang();")
# 4) Kachel auf der Startseite
rep("  ['thsA','An','Anatomie',","  ['thsK','Kö','Körpersprache','Ohren, Augen, Maul, Schweif und Haltung: was dir das Pferd zeigt'],\n  ['thsA','An','Anatomie',")
# 5) Funktion + CSS
JS=r"""
const BL=[
 {k:'Ohren',t:'Die Ohren',rows:[
  ['Nach vorn gerichtet','Das Pferd ist aufmerksam und interessiert an dem, was vor ihm ist.'],
  ['Zur Seite, locker, hängend','Es ist entspannt, zufrieden oder döst.'],
  ['Ein Ohr nach hinten, eines vorn','Es hört in zwei Richtungen. Beim Reiten oft: „Ich höre auf dich.“'],
  ['Eng nach hinten angelegt','Das Pferd ist wütend oder droht. Vorsicht: Tritt oder Biss sind möglich.'],
  ['Schnelles Drehen und Zucken','Es sucht ein Geräusch und ist unsicher, woher es kommt.']]},
 {k:'Augen',t:'Die Augen',rows:[
  ['Weich, halb geschlossen','Das Pferd ist entspannt oder schläfrig.'],
  ['Weit offen, das Weiße sichtbar','Es ist erschrocken oder gestresst. Ruhig bleiben und nicht bedrängen.'],
  ['Starr, angespannter Blick','Das Pferd ist nervös und sucht einen Ausweg.']]},
 {k:'Maul',t:'Maul und Nüstern',rows:[
  ['Unterlippe hängt, Kiefer locker','Tiefe Entspannung, das Pferd döst.'],
  ['Lecken und Kauen','Eine Spannung löst sich oder das Pferd verarbeitet gerade etwas Neues.'],
  ['Weite Nüstern, feste Lippen','Anspannung, Angst, Schmerz oder große Anstrengung.'],
  ['Oberlippe hochgekrempelt (Flehmen)','Das Pferd prüft einen neuen oder starken Geruch.']]},
 {k:'Schweif',t:'Der Schweif',rows:[
  ['Locker hängend','Das Pferd ist ruhig und fühlt sich wohl.'],
  ['Hoch getragen','Es ist aufgeregt, aufmerksam und bereit loszulaufen.'],
  ['Fest eingeklemmt','Angst, Schmerz oder starker Stress.'],
  ['Kräftiges Schlagen','Ärger oder Ungeduld, im Sommer oft einfach Fliegen.']]},
 {k:'Haltung',t:'Haltung und Beine',rows:[
  ['Kopf und Hals tief','Das Pferd vertraut dir und ist entspannt.'],
  ['Kopf hoch, Rücken steif','Es ist alarmiert und bereit zur Flucht.'],
  ['Ein Hinterhuf locker aufgestellt','Das Pferd ruht und fühlt sich sicher.'],
  ['Scharren und Stampfen','Ungeduld, Langeweile oder Ärger.']]}
];
let bli=0;
function bodyLang(){
 const root=g('thBody');root.innerHTML='';
 const seg=document.createElement('div');seg.className='anaSeg blseg';
 BL.forEach((b,i)=>{const x=document.createElement('button');x.type='button';x.textContent=b.k;x.setAttribute('aria-pressed',i===bli);x.onclick=()=>{bli=i;[...seg.children].forEach((c,j)=>c.setAttribute('aria-pressed',j===i));fill(i);};seg.appendChild(x);});
 const card=document.createElement('div');card.className='card blcard';
 const note=document.createElement('p');note.className='tline';
 note.textContent='Immer mehrere Zeichen zusammen lesen und das Pferd nie von hinten ansprechen. Entwurf, mit Reitlehrer abgleichen. Nach allgemeinen Verhaltensratgebern (u. a. RSPCA, EQUUS, Horseware), in eigenen Worten.';
 const fill=i=>{const b=BL[i];card.innerHTML='';const h=document.createElement('p');h.className='blt';h.textContent=b.t;card.appendChild(h);
  const dl=document.createElement('dl');dl.className='bldl';b.rows.forEach(r=>{const dt=document.createElement('dt');dt.textContent=r[0];const dd=document.createElement('dd');dd.textContent=r[1];dl.appendChild(dt);dl.appendChild(dd);});card.appendChild(dl);};
 root.appendChild(seg);root.appendChild(card);root.appendChild(note);
 const lock=()=>{card.style.minHeight='';let m=0;for(let i=0;i<BL.length;i++){fill(i);m=Math.max(m,card.offsetHeight);}card.style.minHeight=m+'px';fill(bli);};
 fill(bli);lock();if(document.fonts&&document.fonts.ready)document.fonts.ready.then(()=>{if(!g('thBody').hidden)lock();});
}
"""
rep("function hist(){",JS+"function hist(){")
CSS="""
.blseg{flex-wrap:wrap;margin:8px 0 10px}.blseg button{margin-left:0;margin-top:-1.5px}
#thBody .blcard{padding:12px 14px;margin:0 0 8px}
#thBody .blt{margin:0 0 8px;color:#e30613;text-transform:uppercase;font-weight:700;font-size:1.35rem;line-height:1.15;letter-spacing:.01em}
#thBody .bldl{margin:0;padding:6px 0 0;border-top:1px dotted #b8b8b8}
#thBody .bldl dt{margin:10px 0 2px;font-weight:700;font-size:.98rem;color:#111}
#thBody .bldl dd{margin:0;font-size:.98rem;line-height:1.4;color:#222}
"""
rep("</style>",CSS+"</style>") if s.count("</style>")==1 else None
if CSS not in s:
    i=s.rindex("</style>");s=s[:i]+CSS+s[i:]
if '--noversion' not in sys.argv:
    s=re.sub(r'(<meta name="app-version" content=")([^"]*)(")',lambda m:m.group(1)+'2026-11-02zzz52'+m.group(3),s,count=1)
open('index.html','w',encoding='utf-8').write(s)
