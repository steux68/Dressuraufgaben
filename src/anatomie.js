/* Anatomie: Skelett mit pulsierenden Punkten, Lernen + Quiz, Deutsch/Englisch, Vollbild */
(function(){
const AR=1420/1108,IMGS={sk:'img/skelett.jpg',ex:'img/exterieur.jpg'};
/* [id, deutsch, englisch, x, y (Pixel im 1420×1108-Bild), Hinweis de, Hinweis en] */
const PS=[
['sk','Schädel','Skull',120,170,'Schützt das Gehirn. Die Augen sitzen seitlich – darum sieht das Pferd fast rundum.','Protects the brain. The eyes sit at the sides, so the horse sees almost all around.'],
['uk','Unterkiefer','Lower jaw (mandible)',190,215,'Zwischen Schneide- und Backenzähnen liegt die zahnlose Lade – dort liegt das Gebiss (die Trense).','The gap between front and cheek teeth (the bars) is where the bit rests.'],
['at','Atlas','Atlas (C1)',255,105,'Erster Halswirbel. Er trägt den Schädel und erlaubt das „Ja“-Nicken.','First neck vertebra. It carries the skull and allows nodding “yes”.'],
['hw','Halswirbel','Neck vertebrae',335,200,'Sieben Halswirbel, wie beim Menschen. Ein lockerer Hals gehört zur Losgelassenheit.','Seven, as in humans. A supple neck is part of “Losgelassenheit” (suppleness).'],
['wi','Widerrist','Withers',590,290,'Die hohen Dornfortsätze der vorderen Brustwirbel. Hier misst man das Stockmaß, hier sitzt der Sattel vorne.','The tall spines of the front thoracic vertebrae. Height is measured here; the saddle sits just behind.'],
['bw','Brustwirbel','Thoracic vertebrae',720,308,'18 Brustwirbel, an jedem hängt ein Rippenpaar. Unter dem Sattel liegen sie nur wenig beweglich.','18 vertebrae, each carrying a pair of ribs. Little movement beneath the saddle.'],
['ri','Rippen','Ribs',700,470,'18 Rippenpaare. Sie schützen Herz und Lunge. Der Gurt liegt hinter den Ellbogen um den Brustkorb.','18 pairs. They protect heart and lungs. The girth lies behind the elbows around the rib cage.'],
['lw','Lendenwirbel','Lumbar vertebrae',880,335,'Sechs Wirbel. Sie verbinden Rücken und Hinterhand; der Rücken muss hier schwingen.','Six vertebrae linking back and hindquarters; the back must swing here.'],
['kb','Kreuzbein','Sacrum',1000,300,'Fünf verwachsene Wirbel, fest mit dem Becken verbunden. Sie leiten die Schubkraft der Hinterhand nach vorn.','Five fused vertebrae joined to the pelvis. They pass the thrust of the hindquarters forward.'],
['be','Becken','Pelvis',985,375,'Ansatz der Hinterhand und Hüftgelenk. Beim Reiten wichtig: die Hanken beugen.','Attachment of the hind limb and hip joint. Important for “Hankenbeugung” (hind-leg flexion).'],
['sw','Schweifwirbel','Tail vertebrae',1305,480,'Die Fortsetzung der Wirbelsäule im Schweif. Ein schwingender Schweif zeigt einen losgelassenen Rücken.','The continuation of the spine in the tail. A swinging tail shows a relaxed back.'],
['sb','Schulterblatt','Scapula',520,340,'Hängt nur mit Muskeln am Rumpf, das Pferd hat kein Schlüsselbein. Das macht die Schulter beweglich.','Held to the trunk by muscle only – horses have no collarbone. That makes the shoulder mobile.'],
['oa','Oberarmbein','Humerus',440,545,'Kurz und kräftig. Es verbindet Schulter und Ellbogen.','Short and strong. It links shoulder and elbow.'],
['eb','Ellbogen','Elbow (olecranon)',495,600,'Der Ellbogenhöcker liegt direkt hinter dem Gurt.','The point of the elbow lies just behind the girth.'],
['ua','Unterarm (Speiche)','Forearm (radius)',485,690,'Langer Knochen über dem „Vorderknie“. Er trägt den Großteil des Gewichts.','Long bone above the “knee”. It carries most of the weight.'],
['vk','Vorderknie (Vorderfußwurzel)','Knee (carpus)',495,820,'Entspricht dem Handgelenk des Menschen, ein Paket aus mehreren kleinen Knochen.','The equivalent of the human wrist, a package of several small bones.'],
['rb','Röhrbein','Cannon bone',485,930,'Ein einziger kräftiger Knochen: Das Pferd geht auf der Spitze des Mittelfingers.','One strong bone: the horse stands on the tip of its middle finger.'],
['fb','Fesselbein','Long pastern bone',492,1018,'Liegt zwischen Fessel- und Kronengelenk.','Lies between the fetlock joint and the pastern joint.'],
['kr','Kronbein','Short pastern bone',468,1050,'Der kurze Knochen zwischen Fesselbein und Hufbein.','The short bone between long pastern and coffin bone.'],
['hu','Hufbein','Coffin bone',430,1078,'Liegt im Huf, vom Horn umschlossen.','Lies inside the hoof, surrounded by horn.'],
['ob','Oberschenkelbein','Femur',1060,520,'Der kräftigste Knochen des Pferdes. Seine Muskeln erzeugen die Schubkraft.','The strongest bone of the horse. Its muscles create the thrust.'],
['ks','Kniescheibe','Patella (kneecap)',995,600,'Sitzt im Kniegelenk (Stifle). Sie kann einrasten, so kann das Pferd im Stehen dösen.','Sits in the stifle joint. It can lock, so the horse can doze standing up.'],
['sc','Schienbein','Tibia',1060,720,'Verbindet Knie und Sprunggelenk. Das Pferd hat es lang und schräg nach hinten.','Connects stifle and hock. Long and angled backwards in the horse.'],
['sg','Sprunggelenk','Hock',1100,810,'Das große Gelenk der Hinterhand, entspricht der Ferse des Menschen. Beim Beugen der Hanken federt es mit.','The big joint of the hind limb, like the human heel. It springs with the hind-leg flexion.'],
['hr','Hinteres Röhrbein','Hind cannon bone',1100,920,'Wie vorne ein einziger langer Knochen unter dem Sprunggelenk.','As in front, one long bone below the hock.']
];
const PE=[
['au','Auge','Eye',128,189,'Seitlich am Kopf: Das Pferd sieht fast rundum, direkt vor der Nase und hinter dem Schweif aber nicht.','Seitlich am Kopf: Das Pferd sieht fast rundum, direkt vor der Nase und hinter dem Schweif aber nicht.'],
['oh','Ohr','Ear',166,85,'Die Ohren zeigen, worauf das Pferd achtet. Nach hinten gelegt: Warnung oder Ärger.','Die Ohren zeigen, worauf das Pferd achtet. Nach hinten gelegt: Warnung oder Ärger.'],
['st','Stirn','Forehead',151,140,'Zwischen Ohren und Augen. Hier sitzt der Stirnriemen der Trense.','Zwischen Ohren und Augen. Hier sitzt der Stirnriemen der Trense.'],
['ge','Genick','Poll',211,118,'Das Gelenk zwischen Kopf und Hals. Beim Reiten soll es der höchste Punkt sein und nachgeben.','Das Gelenk zwischen Kopf und Hals. Beim Reiten soll es der höchste Punkt sein und nachgeben.'],
['nr','Nasenrücken','Bridge of the nose',109,251,'Der Verlauf von der Stirn zu den Nüstern. Hier liegt der Nasenriemen.','Der Verlauf von der Stirn zu den Nüstern. Hier liegt der Nasenriemen.'],
['nu','Nüstern','Nostrils',62,310,'Das Pferd atmet nur durch die Nase. Weite, weiche Nüstern zeigen Ruhe.','Das Pferd atmet nur durch die Nase. Weite, weiche Nüstern zeigen Ruhe.'],
['ma','Maul','Muzzle',88,341,'Lippen und Kinn. Sehr fein und empfindlich, das Pferd tastet damit.','Lippen und Kinn. Sehr fein und empfindlich, das Pferd tastet damit.'],
['ba','Backe','Cheek',189,254,'Hier liegt der Backenriemen der Trense. Darunter die Ganasche.','Hier liegt der Backenriemen der Trense. Darunter die Ganasche.'],
['ka','Kehlgang','Throatlatch',227,279,'Die Stelle zwischen Unterkiefer und Hals. Der Kehlriemen darf nicht zu eng sitzen.','Die Stelle zwischen Unterkiefer und Hals. Der Kehlriemen darf nicht zu eng sitzen.'],
['mk','Mähne (Kamm)','Crest',390,163,'Der obere Halsrand. Bei gut aufgerichtetem Hals ist der Kamm leicht gewölbt.','Der obere Halsrand. Bei gut aufgerichtetem Hals ist der Kamm leicht gewölbt.'],
['ha','Hals','Neck',310,248,'Eine tragende Brücke von Kopf zum Rumpf. Ein lockerer Hals gehört zur Losgelassenheit.','Eine tragende Brücke von Kopf zum Rumpf. Ein lockerer Hals gehört zur Losgelassenheit.'],
['wi','Widerrist','Withers',580,268,'Höchster Punkt des Rückens vor dem Sattel. Hier misst man das Stockmaß.','Höchster Punkt des Rückens vor dem Sattel. Hier misst man das Stockmaß.'],
['rü','Rücken','Back',760,319,'Der Teil unter dem Sattel. Er soll schwingen und das Reitergewicht tragen.','Der Teil unter dem Sattel. Er soll schwingen und das Reitergewicht tragen.'],
['le','Lende','Loin',930,296,'Die Verbindung von Rücken und Hinterhand. Eine kurze, kräftige Lende ist wichtig für die Schubkraft.','Die Verbindung von Rücken und Hinterhand. Eine kurze, kräftige Lende ist wichtig für die Schubkraft.'],
['kr','Kruppe','Croup',1090,310,'Der höchste Teil der Hinterhand bis zum Schweifansatz. Kräftige Muskeln erzeugen den Schub.','Der höchste Teil der Hinterhand bis zum Schweifansatz. Kräftige Muskeln erzeugen den Schub.'],
['sa','Schweifansatz','Dock',1166,346,'Hier beginnt der Schweif. Ein schwingender Schweif zeigt einen losgelassenen Rücken.','Hier beginnt der Schweif. Ein schwingender Schweif zeigt einen losgelassenen Rücken.'],
['sh','Schweif','Tail',1302,563,'Der Schweif hilft gegen Fliegen und zeigt die Stimmung des Pferdes.','Der Schweif hilft gegen Fliegen und zeigt die Stimmung des Pferdes.'],
['sl','Schulter','Shoulder',473,390,'Eine freie, weit ausgreifende Schulter bringt Raumgriff in den Gängen.','Eine freie, weit ausgreifende Schulter bringt Raumgriff in den Gängen.'],
['bu','Buggelenk','Point of shoulder',402,476,'Das Gelenk von Schulter und Oberarm, vorne an der Brust.','Das Gelenk von Schulter und Oberarm, vorne an der Brust.'],
['br','Brust','Chest',402,530,'Vorne zwischen den Vorderbeinen. Sie soll breit genug sein, aber nicht zu schwer.','Vorne zwischen den Vorderbeinen. Sie soll breit genug sein, aber nicht zu schwer.'],
['ell','Ellbogen','Elbow',535,580,'Direkt hinter dem Gurt. Der Gurt darf den Ellbogen nicht drücken.','Direkt hinter dem Gurt. Der Gurt darf den Ellbogen nicht drücken.'],
['rp','Rippen (Rumpf)','Barrel',698,469,'Der Brustkorb: Platz für Herz und Lunge. Hier liegt der Sattelgurt.','Der Brustkorb: Platz für Herz und Lunge. Hier liegt der Sattelgurt.'],
['bc','Bauch','Belly',769,599,'Die Unterseite des Rumpfes. Ein gut aufgezogener Bauch gibt dem Pferd Leichtigkeit.','Die Unterseite des Rumpfes. Ein gut aufgezogener Bauch gibt dem Pferd Leichtigkeit.'],
['fl','Flanke','Flank',947,592,'Die weiche Stelle vor dem Hinterbein. Hier sieht man die Atmung.','Die weiche Stelle vor dem Hinterbein. Hier sieht man die Atmung.'],
['hü','Hüfte (Hüfthöcker)','Point of hip',1015,335,'Der Knochenhöcker seitlich an der Hinterhand, auch „Hüfthöcker“ genannt.','Der Knochenhöcker seitlich an der Hinterhand, auch „Hüfthöcker“ genannt.'],
['os','Oberschenkel','Thigh',1065,469,'Der große Muskel der Hinterhand: die Kraftquelle für Schub und Tragen.','Der große Muskel der Hinterhand: die Kraftquelle für Schub und Tragen.'],
['kn','Knie (hinten)','Stifle',1006,622,'Entspricht dem Knie des Menschen, vorne am Hinterbein.','Entspricht dem Knie des Menschen, vorne am Hinterbein.'],
['sp','Sprunggelenk','Hock',1100,722,'Das große Gelenk der Hinterhand. Beim Beugen der Hanken federt es mit.','Das große Gelenk der Hinterhand. Beim Beugen der Hanken federt es mit.'],
['hr','Röhrbein (hinten)','Hind cannon',1166,882,'Wie vorne der lange Knochen unter dem Sprunggelenk, mit den Sehnen dahinter.','Wie vorne der lange Knochen unter dem Sprunggelenk, mit den Sehnen dahinter.'],
['hh','Hinterhuf','Hind hoof',1124,1025,'Der Huf trägt das Gewicht. Hufpflege und Hufschmied sind wichtig.','Der Huf trägt das Gewicht. Hufpflege und Hufschmied sind wichtig.'],
['va','Vorarm','Forearm',467,692,'Der Teil zwischen Ellbogen und Vorderknie, mit kräftigen Muskeln.','Der Teil zwischen Ellbogen und Vorderknie, mit kräftigen Muskeln.'],
['vn','Vorderknie','Knee',456,811,'Das „Handgelenk“ des Pferdes, ein Paket mehrerer kleiner Knochen.','Das „Handgelenk“ des Pferdes, ein Paket mehrerer kleiner Knochen.'],
['rv','Röhrbein (vorne)','Cannon',456,893,'Unterhalb des Knies. Hier verlaufen die Beugesehnen – bei Pferden oft Problemzone.','Unterhalb des Knies. Hier verlaufen die Beugesehnen – bei Pferden oft Problemzone.'],
['fe','Fesselgelenk','Fetlock',444,958,'Das Gelenk über der Fessel. Es federt jeden Tritt ab.','Das Gelenk über der Fessel. Es federt jeden Tritt ab.'],
['hv','Vorderhuf','Front hoof',408,1030,'Rund und fest. Der Huf wächst ständig nach und muss regelmäßig gepflegt werden.','Rund und fest. Der Huf wächst ständig nach und muss regelmäßig gepflegt werden.']
];
/* Rückenlinie (x, y im 1420×1108-Bild) für die Klammern */
const TOP=[[480,212],[500,225],[520,235],[540,245],[560,249],[600,256],[640,269],[680,288],[720,299],[760,303],[800,301],[840,296],[880,288],[920,280],[960,275],[1000,273],[1040,277],[1080,288],[1120,299],[1160,306],[1180,311]];
const ZONES=[['Widerrist',520,640],['Rücken',640,880],['Lende',880,1020],['Kruppe',1020,1170]];
const UI={
 de:{lern:'Lernen',quiz:'Quiz',full:'⤢ Vollbild',close:'✕ Schließen',names:'Namen',tip:'Tippe auf einen pulsierenden Punkt.',prev:'← Zurück',next:'Weiter →',
  qn:'Wie heißt dieser Teil?',qw:n=>'Wo liegt: '+n+'?',qwt:'Tippe den Punkt an.',ok:'Richtig!',bad:'Leider nein.',nq:'Nächste Frage →',fin:'Fertig!',again:'Noch einmal',pts:'Punkte',of:'von',
  alt:'Skelett des Pferdes, Seitenansicht',cap:'Skelett des Pferdes, Seitenansicht.',sk:'Skelett',ex:'Äußeres',alt2:'Pferd von außen, Seitenansicht',cap2:'Das Pferd von außen mit seinen Körperteilen. Wische nach links oder rechts, um zum Skelett zu wechseln.'},
 en:{lern:'Learn',quiz:'Quiz',full:'⤢ Full screen',close:'✕ Close',names:'Names',tip:'Tap a pulsing dot.',prev:'← Back',next:'Next →',
  qn:'What is this part called?',qw:n=>'Where is the '+n+'?',qwt:'Tap the dot.',ok:'Correct!',bad:'Not quite.',nq:'Next question →',fin:'Done!',again:'Again',pts:'Points',of:'of',
  alt:'Horse skeleton, side view',cap:'Horse skeleton, side view.',sk:'Skeleton',ex:'Exterior',alt2:'Horse exterior, side view',cap2:'The horse from the outside with its parts. Swipe left or right to switch to the skeleton.'}};
let P=PS,set='sk',lang='de',mode='lern',sel=-1,full=false,zoom=1,all=false,built=false;
try{lang=localStorage.getItem('ana_lang')==='en'?'en':'de';}catch(e){}
let Q=[],qi=0,score=0,answered=false,qtype='name',R;
const $=id=>document.getElementById(id);
const nm=p=>lang==='en'?p[2]:p[1],nt=p=>lang==='en'?p[6]:p[5],t=()=>UI[lang];
function el(tag,cls,txt){const e=document.createElement(tag);if(cls)e.className=cls;if(txt!=null)e.textContent=txt;return e;}
function build(){
 if(built)return;built=true;R=$('thAna');
 R.innerHTML='<div class="anaBar"><div class="anaSeg" id="aSet"><button data-s="sk" type="button"></button><button data-s="ex" type="button"></button></div></div><div class="anaBar"><div class="anaSeg" id="aMode"><button id="aLern" type="button"></button><button id="aQuiz" type="button"></button></div><div class="anaSeg" id="aLang"><button data-l="de" type="button">DE</button><button data-l="en" type="button">EN</button></div><button id="aNames" type="button" class="abt"></button><button id="aFull" type="button" class="abt"></button></div>'+
 '<div class="anaScroll" id="aScroll"><button type="button" class="aSw" id="aSw"></button><div class="anaFig" id="aFig"><img id="aImg" src="'+IMGS.sk+'" draggable="false"><svg id="aBr" viewBox="0 0 1420 1108" preserveAspectRatio="none" hidden></svg><div id="aBl" hidden></div><div id="aDots"></div></div></div>'+
 '<div class="anaZoom" id="aZoom"><button id="aZm" type="button" aria-label="−">−</button><button id="aZp" type="button" aria-label="+">+</button></div>'+
 '<div class="anaPanel" id="aPanel" aria-live="polite"></div><p class="tline" id="aCap"></p>';
 buildDots();buildBr();$('aSw').onclick=()=>setSet(set==='sk'?'ex':'sk');
 $('aSet').querySelectorAll('button').forEach(b=>b.onclick=()=>setSet(b.dataset.s));
 var sc=$('aScroll'),tx=0,ty=0;
 sc.addEventListener('touchstart',e=>{tx=e.touches[0].clientX;ty=e.touches[0].clientY;},{passive:true});
 sc.addEventListener('touchend',e=>{if(full)return;const dx=e.changedTouches[0].clientX-tx,dy=e.changedTouches[0].clientY-ty;if(Math.abs(dx)>60&&Math.abs(dx)>Math.abs(dy)*1.6)setSet(set==='sk'?'ex':'sk');},{passive:true});
 $('aLern').onclick=()=>setMode('lern');$('aQuiz').onclick=()=>setMode('quiz');
 $('aLang').querySelectorAll('button').forEach(b=>b.onclick=()=>{lang=b.dataset.l;try{localStorage.setItem('ana_lang',lang)}catch(e){}paint();});
 $('aNames').onclick=()=>{all=!all;paint();};
 $('aFull').onclick=()=>setFull(!full);
 $('aZm').onclick=()=>{zoom=Math.max(1,zoom/1.4);fit();};$('aZp').onclick=()=>{zoom=Math.min(5,zoom*1.4);fit();};
 addEventListener('keydown',e=>{if(e.key==='Escape'&&full)setFull(false);});
 addEventListener('resize',()=>{if(full)fit();});
}
function buildDots(){const D=$('aDots');D.textContent='';
 P.forEach((p,i)=>{const b=el('button','ad');b.type='button';b.style.left=(p[3]/1420*100)+'%';b.style.top=(p[4]/1108*100)+'%';b.style.setProperty('--d',(i%8)*.22+'s');
  b.dataset.i=i;b.onclick=()=>dot(i);const l=el('span','alab');l.hidden=true;b.appendChild(l);if(p[3]>780)b.classList.add('lft');D.appendChild(b);});}
function topY(x){for(let i=1;i<TOP.length;i++)if(x<=TOP[i][0]){const a=TOP[i-1],b=TOP[i];return a[1]+(b[1]-a[1])*(x-a[0])/(b[0]-a[0]);}return TOP[TOP.length-1][1];}
function buildBr(){const sv=$('aBr'),L=$('aBl');let d='',h='';
 ZONES.forEach(z=>{const o=22,pts=[];for(let x=z[1];x<=z[2];x+=10)pts.push([x,topY(x)-o]);pts.push([z[2],topY(z[2])-o]);
  const a=pts[0],b=pts[pts.length-1];
  d+='<path d="M'+a[0]+','+(a[1]+16)+' L'+a[0]+','+a[1]+' '+pts.map(q=>'L'+q[0]+','+q[1]).join(' ')+' L'+b[0]+','+(b[1]+16)+'" />';
  const mx=(z[1]+z[2])/2;h+='<span class="abl" style="left:'+(mx/1420*100)+'%;top:'+((topY(mx)-o)/1108*100)+'%">'+z[0]+'</span>';});
 sv.innerHTML=d;L.innerHTML=h;}
function setSet(s){if(s===set)return;set=s;P=s==='ex'?PE:PS;sel=-1;Q=[];
 $('aImg').src=IMGS[s];$('aBr').toggleAttribute('hidden',s!=='ex');$('aBl').hidden=s!=='ex';buildDots();if(mode==='quiz')startQuiz();paint();}
function fit(){const f=$('aFig');if(!full){f.style.width='';return;}
 const base=Math.min(innerWidth,(innerHeight-170)*AR);f.style.width=Math.round(base*zoom)+'px';
 if(sel>=0&&mode==='lern')centre(sel);}
function centre(i){const s=$('aScroll'),f=$('aFig');if(!full)return;requestAnimationFrame(()=>{const W=f.offsetWidth,H=f.offsetHeight;
 s.scrollTo({left:Math.max(0,P[i][3]/1420*W-s.clientWidth/2),top:Math.max(0,P[i][4]/1108*H-s.clientHeight/2),behavior:'smooth'});});}
function setFull(v){full=v;R.classList.toggle('full',v);document.documentElement.classList.toggle('anaFull',v);
 zoom=v&&innerWidth<innerHeight?2.4:1;fit();paint();if(v)$('aScroll').scrollTo(0,0);}
function setMode(m){mode=m;sel=-1;if(m==='quiz')startQuiz();paint();}
function dot(i){
 if(mode==='lern'){sel=i;paint();centre(i);return;}
 if(qtype==='where'&&!answered){answered=true;const ok=i===Q[qi];if(ok)score++;
  result(ok,Q[qi],i);}
}
function paint(){if(!built)return;
 const u=t();
 $('aLern').textContent=u.lern;$('aQuiz').textContent=u.quiz;$('aFull').textContent=full?u.close:u.full;$('aNames').textContent=u.names;
 $('aLern').setAttribute('aria-pressed',mode==='lern');$('aQuiz').setAttribute('aria-pressed',mode==='quiz');
 $('aLang').querySelectorAll('button').forEach(b=>b.setAttribute('aria-pressed',b.dataset.l===lang));
 $('aNames').setAttribute('aria-pressed',all);$('aNames').hidden=mode!=='lern';$('aZoom').hidden=!full;
 $('aImg').alt=set==='ex'?u.alt2:u.alt;$('aCap').textContent=set==='ex'?u.cap2:u.cap;
 {const sw=$('aSw'),east=set==='sk',ring='<circle class="tr" r="9.5"/><path class="rg" d="M5.31 -7.88A9.5 9.5 0 1 1 -5.31 -7.88"/>';
  sw.className='aSw '+(east?'e':'w');sw.setAttribute('aria-label',east?u.ex:u.sk);
  sw.innerHTML='<svg class="ar" width="40" height="40" viewBox="-12 -12 24 24" aria-hidden="true">'+ring+'<path class="dt" transform="rotate('+(east?0:180)+')" d="M5.4 0L-4.6 -4.9L-2.2 0L-4.6 4.9Z"/><text x="0" y="-9.5">N</text></svg><span>'+(east?u.ex:u.sk)+'</span>';}
 $('aSet').querySelectorAll('button').forEach(b=>{b.textContent=u[b.dataset.s];b.setAttribute('aria-pressed',b.dataset.s===set);});
 const dots=$('aDots').children;
 for(let i=0;i<dots.length;i++){const b=dots[i],p=P[i],l=b.firstChild;b.className='ad'+(p[3]>780?' lft':'');b.setAttribute('aria-label',mode==='lern'||answered?nm(p):'?');
  l.hidden=true;
  if(mode==='lern'){if(i===sel)b.classList.add('on');if(all||i===sel){l.hidden=false;l.textContent=nm(p);}}
  else if(qi<Q.length&&Q.length){const tg=Q[qi];
   if(qtype==='name'){if(i!==tg)b.classList.add('hid');else{b.classList.add(answered?(lastOk?'ok':'bad'):'on');if(answered){l.hidden=false;l.textContent=nm(p);}}}
   else{b.classList.add('calm');if(answered){if(i===tg){b.classList.remove('calm');b.classList.add('ok');l.hidden=false;l.textContent=nm(p);}else if(i===pick){b.classList.remove('calm');b.classList.add('bad');}}}}
  else b.classList.add('hid');}
 panel();}
function panel(){const B=$('aPanel'),u=t();B.textContent='';
 if(mode==='lern'){
  if(sel<0){B.appendChild(el('p','ds',u.tip));return;}
  const p=P[sel];B.appendChild(el('p','nm',nm(p)));B.appendChild(el('p','alt',lang==='en'?p[1]:p[2]));B.appendChild(el('p','ds',nt(p)));
  const r=el('div','anaNav'),a=el('button',null,u.prev),b=el('button','primary',u.next);a.type=b.type='button';
  a.onclick=()=>{sel=(sel+P.length-1)%P.length;paint();centre(sel);};b.onclick=()=>{sel=(sel+1)%P.length;paint();centre(sel);};r.append(a,b);B.appendChild(r);return;}
 if(qi>=Q.length){B.appendChild(el('p','nm',u.fin+' '+score+' '+u.of+' '+Q.length));const b=el('button','primary',u.again);b.type='button';b.onclick=()=>{startQuiz();paint();};B.appendChild(b);return;}
 const tg=P[Q[qi]];
 B.appendChild(el('div','anaScore',u.pts+' '+score+' / '+Q.length+'   ·   '+(qi+1)+' / '+Q.length));
 B.appendChild(el('p','nm',qtype==='name'?u.qn:u.qw(nm(tg))));
 if(qtype==='where'&&!answered)B.appendChild(el('p','ds',u.qwt));
 if(qtype==='name'){const o=el('div','anaOpts');opts.forEach(i=>{const b=el('button','opt',nm(P[i]));b.type='button';b.disabled=answered;
   if(answered){if(i===Q[qi])b.classList.add('ok');else if(i===pick)b.classList.add('bad');}
   b.onclick=()=>{if(answered)return;answered=true;pick=i;const ok=i===Q[qi];if(ok)score++;result(ok,Q[qi],i);};o.appendChild(b);});B.appendChild(o);}
 if(answered){B.appendChild(el('p','fb '+(lastOk?'okt':'badt'),lastOk?u.ok:u.bad));B.appendChild(el('p','ds',nm(tg)+': '+nt(tg)));
  const b=el('button','primary',u.nq);b.type='button';b.onclick=()=>{qi++;next();paint();};B.appendChild(b);}}
let opts=[],pick=-1,lastOk=false;
function result(ok,tg,pk){lastOk=ok;pick=pk;paint();}
function shuffle(a){a=a.slice();for(let i=a.length-1;i>0;i--){const j=Math.floor(Math.random()*(i+1));[a[i],a[j]]=[a[j],a[i]];}return a;}
function startQuiz(){Q=shuffle(P.map((_,i)=>i)).slice(0,10);qi=0;score=0;next();}
function next(){answered=false;pick=-1;lastOk=false;if(qi>=Q.length)return;qtype=Math.random()<.6?'name':'where';
 const tg=Q[qi];opts=shuffle([tg].concat(shuffle(P.map((_,i)=>i).filter(i=>i!==tg)).slice(0,3)));}
window.anaOpen=function(){build();if(mode==='quiz'&&!Q.length)startQuiz();paint();};
window.anaClose=function(){if(full)setFull(false);};
})();
