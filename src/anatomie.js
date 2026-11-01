/* Anatomie-Galerie: Bilder mit pulsierenden Punkten, Lernen + Quiz, Deutsch/Englisch, Popup mit W/E-Tasten */
(function(){
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
/* Kopf von vorn (Bild 1080×1648) und Auge (Bild 1300×1200): [id, de, en, x, y, Hinweis de, Hinweis en] */
const PK=[
['oh','Ohr','Ear',400,140,'Die Ohren drehen sich einzeln und zeigen, worauf das Pferd achtet. Nach hinten gelegt heißt: Vorsicht!','The ears turn independently and show what the horse is attending to. Ears pinned back mean: careful!'],
['sc','Stirnschopf','Forelock',530,350,'Die Haare zwischen den Ohren. Der Stirnriemen der Trense liegt davor.','The hair between the ears. The browband of the bridle sits in front of it.'],
['st','Stirn','Forehead',530,610,'Die breite Fläche zwischen den Augen. Sie zeigt die Mitte des Kopfes.','The broad area between the eyes. It marks the middle of the head.'],
['ab','Augenbogen','Brow ridge',300,520,'Der Knochenrand über dem Auge schützt es von oben.','The bony rim above the eye protects it from above.'],
['au','Auge','Eye',250,630,'Seitlich am Kopf: Das Pferd sieht fast rundum, direkt vor der Nase aber nicht.','On the side of the head: the horse sees almost all around, but not right in front of its nose.'],
['wa','Backe (Kaumuskel)','Cheek (masseter)',720,1130,'Der kräftige Kaumuskel. Beim Reiten sollte das Pferd im Genick nachgeben und kauen, ohne die Backen zu verspannen.','The strong chewing muscle. Ridden well, the horse yields at the poll and chews without tensing the cheeks.'],
['nr','Nasenrücken','Bridge of the nose',524,950,'Der Verlauf von der Stirn zu den Nüstern. Hier liegt der Nasenriemen.','The line from forehead to nostrils. The noseband lies here.'],
['nu','Nüstern','Nostrils',450,1430,'Das Pferd atmet nur durch die Nase. Weite, weiche Nüstern zeigen Ruhe.','The horse breathes only through the nose. Wide, soft nostrils show calm.'],
['mu','Maul','Muzzle',550,1560,'Lippen und Kinn. Sehr fein und empfindlich, das Pferd tastet damit.','Lips and chin. Very fine and sensitive: the horse feels with them.']
];
const PA=[
['ol','Oberlid','Upper lid',700,240,'Das obere Augenlid schützt das Auge. Es hat Wimpern.','The upper eyelid protects the eye. It carries lashes.'],
['wi','Wimpern','Eyelashes',1100,335,'Nur das Oberlid hat lange Wimpern. Sie schützen vor Staub und Stroh.','Only the upper lid has long lashes. They protect from dust and straw.'],
['ul','Unterlid','Lower lid',600,900,'Das untere Augenlid, fast ohne Wimpern.','The lower eyelid, almost without lashes.'],
['aw','Äußerer Augenwinkel','Outer corner (lateral canthus)',1030,470,'Der Winkel zur Schläfe hin, bei diesem Auge rechts im Bild.','The corner towards the temple, on the right in this picture.'],
['iw','Innerer Augenwinkel','Inner corner (medial canthus)',205,815,'Der Winkel zur Nase hin. Dort sitzen Tränenkanal und drittes Augenlid.','The corner towards the nose. Tear duct and third eyelid sit here.'],
['dl','Drittes Augenlid','Third eyelid (nictitating membrane)',285,765,'Die Nickhaut im inneren Augenwinkel. Sie wischt das Auge sauber und schützt es.','The membrane in the inner corner. It wipes and protects the eye.'],
['ir','Iris','Iris',720,790,'Die farbige Regenbogenhaut. Sie öffnet und schließt die Pupille wie eine Blende.','The coloured part. It opens and closes the pupil like an aperture.'],
['pu','Pupille','Pupil',720,610,'Beim Pferd ein liegendes Rechteck mit runden Ecken. So sieht es besonders gut zur Seite und nach hinten.','In horses a horizontal oval. It gives a wide view to the sides and behind.'],
['tk','Traubenkörner','Corpora nigra',740,470,'Die dunklen Knötchen am oberen Pupillenrand. Sie beschatten das Auge wie ein kleiner Sonnenschirm.','The dark knobs on the upper pupil edge. They shade the eye like a small parasol.'],
['li','Hornhautrand','Limbus',990,600,'Hier geht die klare Hornhaut in die weiße Lederhaut über.','Where the clear cornea meets the white of the eye (sclera).']
];
const SETS=[
 {k:'sk',g:'Das Skelett trägt das ganze Pferd: Wirbelsäule, Rippenkorb, Schulter, Becken und vier lange Beine. Wer die Knochen kennt, versteht, warum ein Pferd sich so bewegt, wie es sich bewegt.',gE:'The skeleton carries the whole horse: spine, rib cage, shoulder, pelvis and four long legs. Knowing the bones explains how a horse moves.',src:'noch zu klären',srcE:'to be confirmed',de:'Skelett',en:'Skeleton',img:'img/skelett.jpg',W:1420,H:1108,P:PS,pos:'center 40%',
  alt:'Skelett des Pferdes, Seitenansicht',altE:'Horse skeleton, side view',cap:'Skelett des Pferdes, Seitenansicht.',capE:'Horse skeleton, side view.'},
 {k:'ex',g:'Die Außenansicht zeigt die Körperteile, die im Reitunterricht und in der Richtersprache benannt werden: Widerrist, Rücken, Lende, Kruppe und die Gliedmaßen.',gE:'The outside view shows the body parts named in lessons and by judges: withers, back, loin, croup and the limbs.',src:'noch zu klären',srcE:'to be confirmed',de:'Äußeres',en:'Exterior',img:'img/exterieur.jpg',W:1420,H:1108,P:PE,pos:'center 45%',br:true,
  alt:'Pferd von außen, Seitenansicht',altE:'Horse exterior, side view',cap:'Das Pferd von außen mit seinen Körperteilen.',capE:'The horse from the outside with its parts.'},
 {k:'ko',g:'Von vorn sieht man, wie weit die Augen seitlich sitzen. Darum sieht das Pferd fast rundherum, hat aber direkt vor der Nase einen toten Winkel.',gE:'From the front you see how far to the sides the eyes sit. A horse sees almost all round, but has a blind spot right in front of its nose.',src:'noch zu klären',srcE:'to be confirmed',de:'Kopf von vorn',en:'Head, front',img:'img/kopf.jpg',W:1080,H:1648,P:PK,pos:'center 22%',
  alt:'Pferdekopf von vorn',altE:'Horse head, front view',cap:'Der Kopf von vorn. Zeichnung aus einem alten Anatomiebuch (Quelle noch zu klären).',capE:'The head from the front. Drawing from an old anatomy book (source to be confirmed).'},
 {k:'au',g:'Das Pferdeauge ist eines der größten unter den Landtieren. Die Pupille ist ein liegendes Rechteck, und die Traubenkörner beschatten das Auge.',gE:'The horse eye is among the largest of any land animal. The pupil is a horizontal oval, and the corpora nigra shade the eye.',src:'Foto: Steuart Harrison; Begriffe nach Thal Enterprises',srcE:'Photo: Steuart Harrison; terms after Thal Enterprises',de:'Das Auge',en:'The eye',img:'img/auge.jpg',W:1300,H:1200,P:PA,pos:'center 52%',
  alt:'Pferdeauge, nah',altE:'Horse eye, close-up',cap:'Das Auge von außen (Foto: Steuart Harrison). Begriffe nach Thal Enterprises, übersetzt.',capE:'The eye from the outside (photo: Steuart Harrison). Terms after Thal Enterprises, translated.'}
];
const UI={
 de:{lern:'Lernen',quiz:'Quiz',full:'⤢ Vollbild',close:'✕ Schließen',names:'Namen',tip:'Tippe auf einen pulsierenden Punkt.',prev:'← Zurück',next:'Weiter →',prevT:'Zurück',nextT:'Weiter',
  qn:'Wie heißt dieser Teil?',qw:n=>'Wo liegt: '+n+'?',qwt:'Tippe den Punkt an.',ok:'Richtig!',bad:'Leider nein.',nq:'Nächste Frage →',fin:'Fertig!',again:'Noch einmal',pts:'Punkte',of:'von',
  gal:'Tippe auf ein Bild, um die Punkte zu lernen.',more:'Weitere Bilder folgen.',xs:'Schließen'},
 en:{lern:'Learn',quiz:'Quiz',full:'⤢ Full screen',close:'✕ Close',names:'Names',tip:'Tap a pulsing dot.',prev:'← Back',next:'Next →',prevT:'Back',nextT:'Next',
  qn:'What is this part called?',qw:n=>'Where is the '+n+'?',qwt:'Tap the dot.',ok:'Correct!',bad:'Not quite.',nq:'Next question →',fin:'Done!',again:'Again',pts:'Points',of:'of',
  gal:'Tap a picture to learn its points.',more:'More pictures to come.',xs:'Close'}};
const WSVG='<svg class="ar" width="28" height="28" viewBox="-12 -12 24 24" aria-hidden="true"><circle class="tr" r="9.5"/><path class="rg" d="M-7.88 -5.31A9.5 9.5 0 1 1 -7.88 5.31"/><path class="dt" transform="rotate(180)" d="M5.4 0L-4.6 -4.9L-2.2 0L-4.6 4.9Z"/><text x="-9.50" y="0">W</text></svg>';
const ESVG='<svg class="ar" width="28" height="28" viewBox="-12 -12 24 24" aria-hidden="true"><circle class="tr" r="9.5"/><path class="rg" d="M7.88 5.31A9.5 9.5 0 1 1 7.88 -5.31"/><path class="dt" transform="rotate(0)" d="M5.4 0L-4.6 -4.9L-2.2 0L-4.6 4.9Z"/><text x="9.50" y="0">E</text></svg>';
const XSVG='<svg viewBox="-12 -12 24 24" aria-hidden="true"><circle class="rg" r="9.5"/><path class="xx" d="M-3.6 -3.6L3.6 3.6M3.6 -3.6L-3.6 3.6"/></svg>';
let si=0,P=PS,W=1420,H=1108,lang='de',mode='lern',sel=-1,full=false,zoom=1,all=false,built=false,open=false;
try{lang=localStorage.getItem('ana_lang')==='en'?'en':'de';}catch(e){}
let Q=[],qi=0,score=0,answered=false,qtype='name',pop,galBuilt=false;
const $=id=>document.getElementById(id);
const SET=()=>SETS[si],nm=p=>lang==='en'?p[2]:p[1],nt=p=>lang==='en'?(p[6]||p[5]):p[5],t=()=>UI[lang],sn=s=>lang==='en'?s.en:s.de;
function el(tag,cls,txt){const e=document.createElement(tag);if(cls)e.className=cls;if(txt!=null)e.textContent=txt;return e;}
function gallery(){const R=$('thAna');R.textContent='';
 const g=el('div','agal');
 SETS.forEach((s,i)=>{const b=el('button','agc');b.type='button';
  const im=el('span','agi');im.style.backgroundImage='url('+s.img+')';im.style.backgroundPosition=s.pos;
  const n=el('span','agn',sn(s));const c=el('span','agk',s.P.length+' '+(lang==='en'?'points':'Punkte'));
  b.append(im,n,c);b.onclick=()=>openSet(i);g.appendChild(b);});
 R.append(g,el('p','tline',t().more));}
function buildPop(){if(built)return;built=true;
 pop=el('div','tlpop anapop');pop.id='aPop';pop.hidden=true;pop.setAttribute('role','dialog');pop.setAttribute('aria-modal','true');
 pop.innerHTML='<div class="tlcard"><div class="tltop"><span class="tlk" id="aTk"></span><button type="button" class="tlx" id="aX" aria-label="Schließen">'+XSVG+'</button></div>'+
 '<div class="tlbody anaBody" id="aBody"><div class="anaBar"><div class="anaSeg" id="aMode"><button id="aLern" type="button"></button><button id="aQuiz" type="button"></button></div><div class="anaSeg" id="aLang"><button data-l="de" type="button">DE</button><button data-l="en" type="button">EN</button></div><button id="aNames" type="button" class="abt"></button><button id="aFull" type="button" class="abt"></button></div>'+
 '<p class="aHint" id="aHint"></p><div class="anaStage" id="aStage"><button type="button" class="tlar pw" id="aPrev" aria-label="Zurück">'+WSVG+'</button><button type="button" class="tlar pe" id="aNext" aria-label="Weiter">'+ESVG+'</button><div class="anaScroll" id="aScroll"><div class="anaFig" id="aFig"><img id="aImg" alt="" draggable="false"><svg id="aBr" viewBox="0 0 1420 1108" preserveAspectRatio="none" hidden></svg><div id="aBl" hidden></div><div id="aDots"></div></div></div></div>'+
 '<div class="anaZoom" id="aZoom"><button id="aZm" type="button" aria-label="−">−</button><button id="aZp" type="button" aria-label="+">+</button></div>'+
 '<div class="anaPanel" id="aPanel" aria-live="polite"></div><p class="tline" id="aCap"></p></div>'+
 '</div>';
 document.body.appendChild(pop);
 $('aX').onclick=closeSet;
 pop.addEventListener('click',e=>{if(e.target===pop&&!full)closeSet();});
 $('aPrev').onclick=()=>goSet(-1);$('aNext').onclick=()=>goSet(1);
 $('aLern').onclick=()=>setMode('lern');$('aQuiz').onclick=()=>setMode('quiz');
 $('aLang').querySelectorAll('button').forEach(b=>b.onclick=()=>{lang=b.dataset.l;try{localStorage.setItem('ana_lang',lang)}catch(e){}paint();});
 $('aNames').onclick=()=>{all=!all;if(all&&P.length>14&&!full)setFull(true);else paint();};
 $('aFull').onclick=()=>setFull(!full);
 $('aZm').onclick=()=>{zoom=Math.max(1,zoom/1.4);fit();};$('aZp').onclick=()=>{zoom=Math.min(5,zoom*1.4);fit();};
 let tx=0,ty=0;const sc=$('aScroll');
 sc.addEventListener('touchstart',e=>{tx=e.touches[0].clientX;ty=e.touches[0].clientY;},{passive:true});
 sc.addEventListener('touchend',e=>{if(full)return;const dx=e.changedTouches[0].clientX-tx,dy=e.changedTouches[0].clientY-ty;if(Math.abs(dx)>60&&Math.abs(dx)>Math.abs(dy)*1.6)goSet(dx<0?1:-1);},{passive:true});
 addEventListener('keydown',e=>{if(!open)return;if(e.key==='Escape'){full?setFull(false):closeSet();}else if(e.key==='ArrowLeft')goSet(-1);else if(e.key==='ArrowRight')goSet(1);});
 addEventListener('resize',()=>{if(open)fit();});}
function buildDots(){const D=$('aDots');D.textContent='';
 P.forEach((p,i)=>{const b=el('button','ad');b.type='button';b.style.left=(p[3]/W*100)+'%';b.style.top=(p[4]/H*100)+'%';b.style.setProperty('--d',(i%8)*.22+'s');
  b.dataset.i=i;b.onclick=()=>dot(i);const l=el('span','alab');l.hidden=true;b.appendChild(l);if(p[3]>W*.55)b.classList.add('lft');D.appendChild(b);});}
function topY(x){for(let i=1;i<TOP.length;i++)if(x<=TOP[i][0]){const a=TOP[i-1],b=TOP[i];return a[1]+(b[1]-a[1])*(x-a[0])/(b[0]-a[0]);}return TOP[TOP.length-1][1];}
function buildBr(){const sv=$('aBr'),L=$('aBl');let d='',h='';
 if(!SET().br){sv.toggleAttribute('hidden',true);L.hidden=true;return;}
 ZONES.forEach(z=>{const o=22,pts=[];for(let x=z[1];x<=z[2];x+=10)pts.push([x,topY(x)-o]);pts.push([z[2],topY(z[2])-o]);
  const a=pts[0],b=pts[pts.length-1];
  d+='<path d="M'+a[0]+','+(a[1]+16)+' L'+a[0]+','+a[1]+' '+pts.map(q=>'L'+q[0]+','+q[1]).join(' ')+' L'+b[0]+','+(b[1]+16)+'" />';
  const mx=(z[1]+z[2])/2;h+='<span class="abl" style="left:'+(mx/1420*100)+'%;top:'+((topY(mx)-o)/1108*100)+'%">'+z[0]+'</span>';});
 sv.innerHTML=d;L.innerHTML=h;sv.toggleAttribute('hidden',false);L.hidden=false;}
function showSet(){const s=SET();P=s.P;W=s.W;H=s.H;sel=-1;Q=[];
 const f=$('aFig');f.style.setProperty('--ar',W+'/'+H);f.style.setProperty('--arn',(W/H).toFixed(4));
 $('aImg').src=s.img;buildDots();buildBr();if(mode==='quiz')startQuiz();fit();paint();}
function openSet(i){buildPop();si=i;open=true;pop.hidden=false;document.documentElement.classList.add('anaOpen');showSet();$('aBody').scrollTop=0;}
function closeSet(){if(!open)return;if(full)setFull(false);open=false;pop.hidden=true;document.documentElement.classList.remove('anaOpen');}
function goSet(d){si=(si+SETS.length+d)%SETS.length;showSet();}
function layoutLabels(){const f=$('aFig');if(!f||!open)return;const FW=f.offsetWidth,FH=f.offsetHeight;if(!FW)return;
 const ds=[...$('aDots').children],C=ds.map((b,i)=>[P[i][3]/W*FW,P[i][4]/H*FH]);
 const L=[];ds.forEach((b,i)=>{b.querySelectorAll('.ald').forEach(x=>x.remove());const l=b.firstChild;l.style.left=l.style.top=l.style.right=l.style.transform='';if(!l.hidden){L.push({i,l,w:l.offsetWidth,h:l.offsetHeight,r:null});}});
 if(!L.length)return;
 const R=9;
 const cands=(c,w,h,right)=>{const out=[];[9,26,48,76].forEach((g,ki)=>{const a=[[g,-h/2],[-g-w,-h/2],[-w/2,-g-h-2],[-w/2,g+2],[g-2,-h-g+2],[-w-g+2,-h-g+2],[g-2,g-2],[-w-g+2,g-2]];if(!right){[a[0],a[1]]=[a[1],a[0]];[a[4],a[5]]=[a[5],a[4]];[a[6],a[7]]=[a[7],a[6]];}a.forEach((v,k)=>out.push([c[0]+v[0],c[1]+v[1],ki*8+k]));});return out;};
 const ov=(a,b)=>{const x=Math.min(a[0]+a[2],b[0]+b[2])-Math.max(a[0],b[0]),y=Math.min(a[1]+a[3],b[1]+b[3])-Math.max(a[1],b[1]);return x>0&&y>0?x*y:0;};
 const cost=(e,pos)=>{const r=[pos[0],pos[1],e.w,e.h];let c=pos[2]*(1+Math.floor(pos[2]/8)*1.5);
  if(r[0]<2)c+=300+(2-r[0])*20;if(r[1]<2)c+=300+(2-r[1])*20;if(r[0]+r[2]>FW-2)c+=300+(r[0]+r[2]-FW+2)*20;if(r[1]+r[3]>FH-2)c+=300+(r[1]+r[3]-FH+2)*20;
  L.forEach(o=>{if(o!==e&&o.r)c+=ov(r,o.r)*8;});
  C.forEach((p,j)=>{if(j!==e.i){c+=ov(r,[p[0]-R,p[1]-R,2*R,2*R])>0?900:0;}});return c;};
 const order=L.slice().sort((a,b)=>C[a.i][1]-C[b.i][1]||C[a.i][0]-C[b.i][0]);
 for(let pass=0;pass<3;pass++)order.forEach(e=>{const cs=cands(C[e.i],e.w,e.h,C[e.i][0]<FW*.55);let best=0,bc=1e9;e.r=null;
  cs.forEach((p,k)=>{const c=cost(e,p);if(c<bc){bc=c;best=k;}});const p=cs[best];e.r=[p[0],p[1],e.w,e.h];});
 L.forEach(e=>{const l=e.l;const cx=C[e.i][0],cy=C[e.i][1],nx=Math.max(e.r[0],Math.min(cx,e.r[0]+e.w)),ny=Math.max(e.r[1],Math.min(cy,e.r[1]+e.h)),dd=Math.hypot(nx-cx,ny-cy);
  if(dd>13){const ld=document.createElement('i');ld.className='ald';ld.style.width=(dd-8)+'px';ld.style.transform='rotate('+Math.atan2(ny-cy,nx-cx)+'rad)';ds[e.i].appendChild(ld);}
  l.style.left=(e.r[0]-C[e.i][0]+14)+'px';l.style.top=(e.r[1]-C[e.i][1]+14)+'px';l.style.right='auto';l.style.transform='none';});}
function fit(){const f=$('aFig');if(!f)return;
 if(!full){const st=$('aStage'),bw=st.clientWidth-8,bh=st.clientHeight-8;f.style.maxWidth='none';f.style.width=Math.max(60,Math.round(Math.min(bw,bh*W/H)))+'px';layoutLabels();return;}
 f.style.maxWidth='none';const base=Math.min(innerWidth-20,(innerHeight-170)*W/H);f.style.width=Math.round(base*zoom)+'px';
 if(sel>=0&&mode==='lern')centre(sel);layoutLabels();}
function centre(i){const s=$('aScroll'),f=$('aFig');if(!full)return;requestAnimationFrame(()=>{const w=f.offsetWidth,h=f.offsetHeight;
 s.scrollTo({left:Math.max(0,P[i][3]/W*w-s.clientWidth/2),top:Math.max(0,P[i][4]/H*h-s.clientHeight/2),behavior:'smooth'});});}
function setFull(v){full=v;pop.classList.toggle('full',v);zoom=v&&innerWidth<innerHeight?(W/H>1.2?2.2:1.2):1;fit();paint();if(v)$('aScroll').scrollTo(0,0);}
function setMode(m){mode=m;sel=-1;if(m==='quiz')startQuiz();paint();}
function dot(i){
 if(mode==='lern'){sel=i;paint();centre(i);return;}
 if(qtype==='where'&&!answered){answered=true;const ok=i===Q[qi];if(ok)score++;result(ok,Q[qi],i);}
}
function paint(){if(!built||!open)return;
 const u=t(),s=SET(),pv=SETS[(si+SETS.length-1)%SETS.length],nx=SETS[(si+1)%SETS.length];
 $('aTk').innerHTML='<b></b> · '+(si+1)+' / '+SETS.length;$('aTk').firstChild.textContent=sn(s);
 $('aLern').textContent=u.lern;$('aQuiz').textContent=u.quiz;$('aFull').textContent=full?u.close:u.full;$('aNames').textContent=u.names;
 $('aLern').setAttribute('aria-pressed',mode==='lern');$('aQuiz').setAttribute('aria-pressed',mode==='quiz');
 $('aLang').querySelectorAll('button').forEach(b=>b.setAttribute('aria-pressed',b.dataset.l===lang));
 $('aNames').setAttribute('aria-pressed',all);$('aNames').hidden=mode!=='lern';$('aZoom').hidden=!full;
 $('aImg').alt=lang==='en'?s.altE:s.alt;$('aCap').textContent=lang==='en'?s.capE:s.cap;
 {const h=$('aHint');h.textContent=u.tip;h.style.visibility=(mode==='lern'&&sel<0&&!full)?'visible':'hidden';}$('aPrev').setAttribute('aria-label',sn(pv));$('aNext').setAttribute('aria-label',sn(nx));
 const dots=$('aDots').children;
 for(let i=0;i<dots.length;i++){const b=dots[i],p=P[i],l=b.firstChild;b.className='ad'+(p[3]>W*.55?' lft':'');b.setAttribute('aria-label',mode==='lern'||answered?nm(p):'?');
  l.hidden=true;
  if(mode==='lern'){if(i===sel)b.classList.add('on');if(all||i===sel){l.hidden=false;l.textContent=nm(p);}}
  else if(qi<Q.length&&Q.length){const tg=Q[qi];
   if(qtype==='name'){if(i!==tg)b.classList.add('hid');else{b.classList.add(answered?(lastOk?'ok':'bad'):'on');if(answered){l.hidden=false;l.textContent=nm(p);}}}
   else{b.classList.add('calm');if(answered){if(i===tg){b.classList.remove('calm');b.classList.add('ok');l.hidden=false;l.textContent=nm(p);}else if(i===pick){b.classList.remove('calm');b.classList.add('bad');}}}}
  else b.classList.add('hid');}
 panel();layoutLabels();}
function panel(){const B=$('aPanel'),u=t();B.textContent='';
 if(mode==='lern'){
  if(sel<0){const s=SET(),en=lang==='en';B.appendChild(el('p','nm',sn(s)));
   B.appendChild(el('p','ds',en?s.capE:s.cap));B.appendChild(el('p','ds',en?s.gE:s.g));
   const d=el('dl','anaDl');[[en?'Points':'Punkte',P.length],[en?'Picture':'Bild',en?s.altE:s.alt],[en?'Source':'Quelle',en?s.srcE:s.src],[en?'Set':'Satz',(si+1)+' / '+SETS.length]].forEach(r=>{d.appendChild(el('dt','',r[0]));d.appendChild(el('dd','',String(r[1])));});B.appendChild(d);return;}
  const p=P[sel];B.appendChild(el('p','nm',nm(p)));B.appendChild(el('p','alt',lang==='en'?p[1]:p[2]));B.appendChild(el('p','ds',nt(p)));
  {const d=el('dl','anaDl'),en=lang==='en';[[en?'Part':'Teil',(sel+1)+' / '+P.length],[en?'In':'In',sn(SET())]].forEach(r=>{d.appendChild(el('dt','',r[0]));d.appendChild(el('dd','',r[1]));});B.appendChild(d);}
  const r=el('div','anaNav'),a=el('button','aSw w'),b=el('button','aSw e');a.type=b.type='button';
  a.innerHTML=WSVG+'<span></span>';b.innerHTML='<span></span>'+ESVG;a.lastElementChild.textContent=u.prevT;b.firstElementChild.textContent=u.nextT;
  a.setAttribute('aria-label',u.prevT);b.setAttribute('aria-label',u.nextT);
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
window.anaOpen=function(){gallery();};
window.anaClose=function(){closeSet();};
})();
