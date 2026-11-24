# Pferdewissen: neuer Reiter "Hilfen" (21 Piktogramme: Zuegel, Sitz, Schenkel; nach der Hilfentafel von S. Steinbach 2000, neu gezeichnet). Idempotent. 24.11.2026
import re,sys
s=open('index.html',encoding='utf-8').read()
if 'id="thsHi"' in s: sys.exit('schon angewendet')
def rep(old,new):
    global s
    assert s.count(old)==1,old[:80]
    s=s.replace(old,new,1)
rep('<button id="thsGe" aria-pressed="false">Gesundheit</button>','<button id="thsGe" aria-pressed="false">Gesundheit</button>\n<button id="thsHi" aria-pressed="false">Hilfen</button>')
rep('<div class="tp" id="thGes" hidden></div>','<div class="tp" id="thGes" hidden></div>\n<div class="tp" id="thHi" hidden></div>')
rep("'thsK','thsGe','thsA','thsB','thsH','thsZ','thsP'],SUBT","'thsK','thsGe','thsHi','thsA','thsB','thsH','thsZ','thsP'],SUBT")
rep("SUBG=['thsB','thsA','thsV','thsK','thsS','thsGe']","SUBG=['thsB','thsA','thsV','thsK','thsS','thsGe','thsHi']")
rep("g('thGes').hidden=which!=='thsGe';","g('thGes').hidden=which!=='thsGe';g('thHi').hidden=which!=='thsHi';")
rep("['thsP','thsH','thsZ','thsA','thsB','thsK','thsGe'].includes(which)","['thsP','thsH','thsZ','thsA','thsB','thsK','thsGe','thsHi'].includes(which)")
rep("else if(which==='thsGe')health();","else if(which==='thsGe')health();else if(which==='thsHi')hilfen();")
rep("  ['thsGe','Ge','Gesundheit','Puls, Atmung, Temperatur, Kolik: normal oder Tierarzt?']","  ['thsGe','Ge','Gesundheit','Puls, Atmung, Temperatur, Kolik: normal oder Tierarzt?'],\n  ['thsHi','Hi','Hilfen','Zügel, Sitz und Schenkel: 21 Zeichen der Hilfentafel']")
rep("thsGe:'img/gesundheit_check.jpg',thsP:","thsGe:'img/gesundheit_check.jpg',thsHi:'img/kreis_hilfen.svg',thsP:")
rep("thsGe:'#fff url(img/gesundheit_check.jpg) 42% 22%/217% no-repeat',","thsGe:'#fff url(img/gesundheit_check.jpg) 42% 22%/217% no-repeat',thsHi:'#fff url(img/kreis_hilfen.svg) center/cover no-repeat',")
JS=r"""
const HL=[
{n:'Halten',g:'Gangarten',h:'TT',s:'FF',l:'HH',t:'Gleichmäßig sitzen, beide Schenkel liegen ruhig am Pferd und verhindern Seitwärtstreten. Steht das Pferd, gibt die Hand leicht nach, die Verbindung bleibt.'},
{n:'Anreiten aus dem Halten',g:'Gangarten',h:'NN',s:'FF',l:'DD',t:'Beide Schenkel treiben. Die Hände geben kurz nach, damit das Pferd vorwärts gehen kann.'},
{n:'Schritt & Trab ohne Tempoverstärkung',g:'Gangarten',h:'TT',s:'FF',l:'DD',t:'Das Kreuz ist leicht angespannt, die Schenkel wirken gleichmäßig mit. Die Hände halten eine ruhige Verbindung zum Pferdemaul.'},
{n:'Tempoverstärkung im Schritt & Trab',g:'Gangarten',h:'NN',s:'FF',l:'DD',t:'Die Hände geben nach, damit die treibenden Hilfen frei wirken können.'},
{n:'Leichttraben, Einsitzen',g:'Gangarten',h:'TT',s:'FF',l:'DD',t:'Beim Einsitzen sinkt das Gesäß wieder in den Sattel. Schenkel und Hände bleiben ruhig.'},
{n:'Erheben des Gesäßes aus dem Sattel',g:'Gangarten',h:'TT',s:'OO',l:'XX',t:'Hebt der Reiter das Gesäß, bleibt der Schenkel bei tiefem Knie und Absatz am Pferd, treibt in diesem Moment aber nicht.'},
{n:'Angaloppieren (links)',g:'Galopp',h:'NT',s:'FH',l:'DH',t:'Der linke Schenkel treibt, der rechte verwahrt. Der linke Gesäßknochen ist mehr belastet. Die linke Hand gibt im Moment des Sprungs kurz nach.'},
{n:'Galopp ohne Tempoveränderung (Linksgalopp)',g:'Galopp',h:'TT',s:'FH',l:'DH',t:'Der linke Gesäßknochen bleibt mehr belastet, der linke Schenkel erhält die Lebendigkeit des Galoppsprungs.'},
{n:'Tempoverstärkung im Galopp (Linksgalopp)',g:'Galopp',h:'NN',s:'FH',l:'DH',t:'Die Hände geben nach, damit die Galoppsprünge länger werden können.'},
{n:'Parade, 1. Phase',g:'Parade & Rückwärts',h:'TT',s:'FF',l:'DD',t:'Gewicht, Schenkel und Hand wirken zusammen. Die Hand hält einen Moment durch, bis das Pferd die Parade annimmt.'},
{n:'Parade, 2. Phase',g:'Parade & Rückwärts',h:'NN',s:'FF',l:'DD',t:'Danach gibt die Hand sofort nach, ohne die Verbindung zum Maul zu verlieren. Eine ganze Parade besteht aus mehreren halben Paraden hintereinander.'},
{n:'Schenkelweichen (links)',g:'Seitwärts & Wenden',b:1,h:'TT',s:'FH',l:'DH',t:'Der linke Schenkel treibt seitwärts, der rechte verwahrt und wirkt nur bei Bedarf. Die linke Hand stellt das Pferd, die rechte verwahrt.'},
{n:'Vorhandwendung (linksum kehrt)',g:'Seitwärts & Wenden',b:1,h:'TT',s:'FH',l:'DH',t:'Auf den Druck des linken Schenkels tritt das Pferd seitwärts und dreht die Hinterhand um die Vorhand. Der rechte Schenkel wird nur aktiv, wenn es zu eilig wird.'},
{n:'Hinterhandwendung (linksum kehrt)',g:'Seitwärts & Wenden',b:1,h:'TT',s:'FH',l:'HD',t:'Das Pferd ist links gestellt und gebogen. Der äußere Schenkel treibt seitwärts, die Vorhand tritt um den inneren Hinterfuß herum.'},
{n:'Wendungen in der Bewegung',g:'Seitwärts & Wenden',b:1,h:'TT',s:'FH',l:'DH',t:'Das Pferd wird mit dem inneren Schenkel an den äußeren Zügel und den äußeren Schenkel herangetrieben. Der äußere Schenkel hält Vorder- und Hinterbeine auf einer Linie.'},
{n:'Rückwärtsrichten, 1. Phase',g:'Parade & Rückwärts',h:'TT',s:'FF',l:'DD',t:'Der Reiter treibt und hält mit der Hand durch, bis das Pferd einen Tritt rückwärts macht.'},
{n:'Rückwärtsrichten, 2. Phase',g:'Parade & Rückwärts',h:'NN',s:'FF',l:'DD',t:'Sobald das Pferd rückwärts tritt, gibt die Hand etwas nach. Dann beginnt die Hilfe von vorn, bis die verlangte Zahl an Tritten erreicht ist.'},
{n:'Rückwärtsrichten, junges Pferd, 1. Phase',g:'Parade & Rückwärts',h:'TT',s:'HH',l:'DD',t:'Beide Gesäßknochen werden weniger belastet. Das entlastet den Rücken und erleichtert dem jungen Pferd das Rückwärtstreten.'},
{n:'Rückwärtsrichten, junges Pferd, 2. Phase',g:'Parade & Rückwärts',h:'NN',s:'HH',l:'DD',t:'Die Hand gibt nach, sobald das Pferd rückwärts tritt. Der Rücken bleibt entlastet.'},
{n:'Überstreichen',g:'Zügel',h:'UU',s:'FF',l:'DD',t:'Die Hände gehen am Hals entlang nach vorn. Die treibenden Hilfen setzen nicht aus, damit das Pferd nicht auseinanderfällt.'},
{n:'Zügel aus der Hand kauen lassen',g:'Zügel',h:'KK',s:'FF',l:'DD',t:'Die Faust öffnet sich etwas, die Handposition bleibt. Die Zügel gleiten durch die Finger, die treibenden Hilfen bleiben unverändert.'}
];
const HLZ={TT:'beide nehmen an',NN:'beide geben nach',NT:'links gibt nach, rechts nimmt an',TN:'links nimmt an, rechts gibt nach',UU:'beide Hände nach vorn',KK:'Faust öffnet sich'};
const HLS={FF:'beide belastet',FH:'links belastet, rechts weniger',HH:'beide weniger belastet',OO:'Gesäß entlastet'};
const HLL={DD:'beide treibend',DH:'links treibt, rechts verwahrt',HD:'links verwahrt, rechts treibt',HH:'beide verwahrend',XX:'beide nicht treibend'};
const HLG=['Alle','Gangarten','Galopp','Parade & Rückwärts','Seitwärts & Wenden','Zügel'];
const HLK=[['hT','Annehmende Zügelhilfe'],['hN','Nachgebende Zügelhilfe'],['sF','Belastende Gewichtshilfe'],['sH','Weniger belastend'],['sO','Entlastende Gewichtshilfe'],['lD','Treibender Schenkel'],['lH','Verwahrender Schenkel'],['lX','Nicht treibender Schenkel']];
const HLC='#1b1b1b',HLW='#fff';let hlU=0;const hls={m:'l',f:'Alle',i:0};
function hlHand(x,y,mir,type){
 const pts='-26,18 -18,-16 24,-16 26,18';let o='<g transform="translate('+x+','+y+') scale('+mir+',1)">';
 if(type==='T')o+='<polygon points="'+pts+'" fill="'+HLC+'"/><circle cx="-3" cy="-1" r="4" fill="'+HLW+'"/><circle cx="9" cy="-1" r="4" fill="'+HLW+'"/>';
 else o+='<polygon points="'+pts+'" fill="'+HLW+'" stroke="'+HLC+'" stroke-width="2.5"/>'+[-8,4,15].map(cx=>'<circle cx="'+cx+'" cy="-2" r="4.5" fill="none" stroke="'+HLC+'" stroke-width="2"/>').join('');
 return o+'</g>';
}
function hlFill(c,id){return c==='D'||c==='F'?HLC:c==='H'?'url(#'+id+')':HLW;}
function hlPic(p,w,h){
 const id='hlst'+(hlU++);
 let o='<svg xmlns="http://www.w3.org/2000/svg" width="'+w+'" height="'+h+'" viewBox="0 -14 200 354" role="img" aria-label="'+p.n+'" style="display:block"><defs><pattern id="'+id+'" width="8" height="6" patternUnits="userSpaceOnUse"><rect width="8" height="6" fill="'+HLW+'"/><rect y="2" width="8" height="2.4" fill="'+HLC+'"/></pattern></defs>';
 const k=p.h==='KK',u=p.h==='UU',y0=k?3:19;let top='';
 top+='<line x1="14" y1="19" x2="186" y2="19" stroke="'+HLC+'" stroke-width="1"/>';
 [69,123].forEach(x=>{top+='<rect x="'+x+'" y="'+y0+'" width="8" height="'+(156-y0)+'" fill="'+HLW+'" stroke="'+HLC+'" stroke-width="2"/>';});
 (k?[-2,14,30]:[14]).forEach(b=>{top+='<rect x="78" y="'+b+'" width="44" height="10" rx="5" fill="'+HLW+'" stroke="'+HLC+'" stroke-width="2"/>';});
 if(u)top+=hlHand(68,172,1,'T')+hlHand(132,172,-1,'T')+hlHand(68,112,1,'N')+hlHand(132,112,-1,'N');
 else{const a=p.h[0]==='K'?'N':p.h[0],b=p.h[1]==='K'?'N':p.h[1];top+=hlHand(68,172,1,a)+hlHand(132,172,-1,b);}
 o+='<line x1="100" y1="24" x2="100" y2="336" stroke="'+HLC+'" stroke-width="1"/>';
 o+=p.b?'<g transform="rotate(-7 100 215)">'+top+'</g><path d="M92 8 C66 90 66 190 100 332" fill="none" stroke="'+HLC+'" stroke-width="1.2"/>':top;
 o+='<line x1="14" y1="312" x2="186" y2="312" stroke="'+HLC+'" stroke-width="1"/>';
 [[34,p.l[0]],[142,p.l[1]]].forEach(q=>{o+='<rect x="'+q[0]+'" y="215" width="24" height="112" rx="12" fill="'+hlFill(q[1],id)+'" stroke="'+HLC+'" stroke-width="2"/>';});
 [[82,p.s[0]],[118,p.s[1]]].forEach(q=>{o+='<circle cx="'+q[0]+'" cy="312" r="14" fill="'+hlFill(q[1],id)+'" stroke="'+HLC+'" stroke-width="2.5"/>';});
 return o+'</svg>';
}
function hlMini(kind){
 const id='hlsm'+(hlU++),st='stroke="'+HLC+'" stroke-width="2"';
 let d='<svg width="40" height="32" viewBox="0 0 40 32" aria-hidden="true"><defs><pattern id="'+id+'" width="6" height="5" patternUnits="userSpaceOnUse"><rect width="6" height="5" fill="'+HLW+'"/><rect y="1.6" width="6" height="2" fill="'+HLC+'"/></pattern></defs>';
 if(kind==='hT')d+='<g transform="scale(.7) translate(28,24)">'+hlHand(0,0,1,'T')+'</g>';
 if(kind==='hN')d+='<g transform="scale(.7) translate(28,24)">'+hlHand(0,0,1,'N')+'</g>';
 if(kind==='sF')d+='<circle cx="20" cy="16" r="10" fill="'+HLC+'"/>';
 if(kind==='sH')d+='<circle cx="20" cy="16" r="10" fill="url(#'+id+')" '+st+'/>';
 if(kind==='sO')d+='<circle cx="20" cy="16" r="10" fill="'+HLW+'" '+st+'/>';
 if(kind==='lD')d+='<rect x="14" y="2" width="12" height="28" rx="6" fill="'+HLC+'"/>';
 if(kind==='lH')d+='<rect x="14" y="2" width="12" height="28" rx="6" fill="url(#'+id+')" '+st+'/>';
 if(kind==='lX')d+='<rect x="14" y="2" width="12" height="28" rx="6" fill="'+HLW+'" '+st+'/>';
 return d+'</svg>';
}
function hlList(){return HL.filter(x=>hls.f==='Alle'||x.g===hls.f);}
function hlRow(l,t){return '<div class="hiRow"><span>'+l+'</span><b>'+t+'</b></div>';}
function hlRender(){
 const root=g('thHi'),L=hlList();if(hls.i>=L.length)hls.i=0;
 let o='<div class="anaSeg blseg">'+[['l','Lernen'],['u','Übersicht'],['z','Zeichen']].map(q=>'<button type="button" data-a="m" data-v="'+q[0]+'" aria-pressed="'+(hls.m===q[0])+'">'+q[1]+'</button>').join('')+'</div>';
 if(hls.m==='l'){
  const p=L[hls.i];
  o+='<div class="hiCard"><p class="hiN">'+p.n+'</p><div class="hiFig"><button type="button" class="hiAr" data-a="p" aria-label="Zurück"><svg width="20" height="20" viewBox="0 0 20 20" aria-hidden="true"><path d="M12.5 4.5 7 10l5.5 5.5" fill="none" stroke="#222" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg></button>'+hlPic(p,150,265)+'<button type="button" class="hiAr" data-a="n" aria-label="Weiter"><svg width="20" height="20" viewBox="0 0 20 20" aria-hidden="true"><path d="M7.5 4.5 13 10l-5.5 5.5" fill="none" stroke="#222" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg></button></div>'
   +hlRow('Zügel',HLZ[p.h])+hlRow('Sitz',HLS[p.s])+hlRow('Schenkel',HLL[p.l])
   +'<p class="hiT">'+p.t+'</p><div class="hiDl"><span>'+p.g+'</span><span>'+String(hls.i+1).padStart(2,'0')+' / '+L.length+'</span></div></div>';
 }
 if(hls.m==='u'){
  o+='<div class="hiChips">'+HLG.map(x=>'<button type="button" data-a="f" data-v="'+x+'" aria-pressed="'+(hls.f===x)+'">'+x+'</button>').join('')+'</div><div class="hiGrid">'
   +L.map((p,j)=>'<button type="button" class="hiTile" data-a="o" data-v="'+j+'">'+hlPic(p,40,71)+'<span>'+p.n+'</span></button>').join('')+'</div>';
 }
 if(hls.m==='z'){o+='<div class="hiLeg">'+HLK.map(q=>'<div>'+hlMini(q[0])+'<span>'+q[1]+'</span></div>').join('')+'</div>';}
 o+='<p class="tline hiSrc">Piktogramme neu gezeichnet, nach der Hilfentafel von S. Steinbach (2000). Entwurf, mit Reitlehrer abgleichen.</p>';
 root.innerHTML=o;
 if(hls.m==='l')hlLock();
}
function hlLock(){
 const root=g('thHi'),p=root.querySelector('.hiT'),t=root.querySelector('.hiN');if(!p||!t||!root.offsetParent)return;
 p.style.minHeight='';t.style.minHeight='';const kp=p.textContent,kt=t.textContent;let a=0,b=0;
 HL.forEach(x=>{p.textContent=x.t;t.textContent=x.n;a=Math.max(a,p.offsetHeight);b=Math.max(b,t.offsetHeight);});
 p.textContent=kp;t.textContent=kt;p.style.minHeight=a+'px';t.style.minHeight=b+'px';
 root.querySelectorAll('.hiRow').forEach((r,k)=>{const bb=r.querySelector('b'),keep=bb.textContent;r.style.minHeight='';let m=0;
  HL.forEach(x=>{bb.textContent=[HLZ[x.h],HLS[x.s],HLL[x.l]][k];m=Math.max(m,r.offsetHeight);});bb.textContent=keep;r.style.minHeight=m+'px';});
}
function hilfen(){
 const root=g('thHi');
 if(!root.dataset.on){
  root.dataset.on='1';
  root.addEventListener('click',e=>{
   const b=e.target.closest('[data-a]');if(!b)return;const a=b.dataset.a,v=b.dataset.v,n=hlList().length;
   if(a==='m')hls.m=v;
   if(a==='f'){hls.f=v;hls.i=0;}
   if(a==='o'){hls.i=+v;hls.m='l';}
   if(a==='n')hls.i=(hls.i+1)%n;
   if(a==='p')hls.i=(hls.i-1+n)%n;
   hlRender();
  });
  let tx=null;
  root.addEventListener('touchstart',e=>{tx=e.touches[0].clientX;},{passive:true});
  root.addEventListener('touchend',e=>{if(tx===null||hls.m!=='l')return;const dx=e.changedTouches[0].clientX-tx;tx=null;if(Math.abs(dx)>50){const n=hlList().length;hls.i=(hls.i+(dx<0?1:n-1))%n;hlRender();}});
  if(document.fonts&&document.fonts.ready)document.fonts.ready.then(()=>{if(!root.hidden)hlLock();});
 }
 hlRender();
}
window.hlPic=hlPic;window.HL=HL;
"""
rep("function hist(){",JS+"function hist(){")
CSS='''<style id="hilfen-css">
#theo:has(#thHi:not([hidden])){overflow-y:auto;overflow-x:hidden;min-height:0;-webkit-overflow-scrolling:touch}
#thHi:not([hidden]){padding-bottom:12px}
#thHi .hiCard{background:var(--surface);padding:14px 12px 10px;margin:0 0 8px}
#thHi .hiN{margin:0;padding:0 4px;color:#e30613;text-transform:uppercase;font-weight:700;font-size:1.35rem;line-height:1.15;letter-spacing:.01em}
#thHi .hiFig{display:flex;align-items:center;justify-content:space-between;margin:10px 0 12px}
#thHi .hiAr{flex:none;width:42px;height:42px;min-height:0;padding:0;border:0!important;border-radius:50%!important;background:rgba(255,255,255,.82)!important;display:flex;align-items:center;justify-content:center;-webkit-tap-highlight-color:transparent}
#thHi .hiRow{display:flex;gap:10px;align-items:baseline;min-height:22px;font-size:.98rem}
#thHi .hiRow span{flex:none;width:68px;font-size:.78rem;letter-spacing:.06em;text-transform:uppercase;color:#777}
#thHi .hiRow b{font-weight:400;color:#222}
#thHi .hiT{margin:10px 0 12px;font-size:.98rem;line-height:1.45;color:#222}
#thHi .hiDl{display:flex;justify-content:space-between;border-top:1.5px dotted #b8b8b8;padding-top:8px;font-size:.85rem;color:#666}
#thHi .hiChips{display:flex;flex-wrap:wrap;gap:6px;margin:0 0 10px}
#thHi .hiChips button{min-height:0;padding:5px 10px;font-size:14px;border:1.5px solid var(--line);background:var(--surface);color:var(--fg);border-radius:0}
#thHi .hiChips button[aria-pressed="true"]{background:#cdff3e;border-color:#22281f;color:#222;font-weight:700}
#thHi .hiGrid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:8px}
#thHi .hiTile{display:flex;gap:8px;align-items:center;text-align:left;min-height:0;padding:8px;border:0!important;border-radius:0;background:var(--surface);color:#222}
#thHi .hiTile svg{flex:none}
#thHi .hiTile span{font-size:.8rem;line-height:1.3}
#thHi .hiLeg{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:4px 10px;background:var(--surface);padding:12px}
#thHi .hiLeg div{display:flex;align-items:center;gap:6px}
#thHi .hiLeg span{font-size:.8rem;line-height:1.3;color:#222}
#thHi .hiSrc{margin:10px 2px 0}
</style>
'''
assert s.count('</head>')==1
s=s.replace('</head>',CSS+'</head>',1)
if '--noversion' not in sys.argv:
    s=re.sub(r'(<meta name="app-version" content=")([^"]*)(")',lambda m:m.group(1)+'2026-11-24b'+m.group(3),s,count=1)
open('index.html','w',encoding='utf-8').write(s)
