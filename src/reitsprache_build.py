import re,json
sk=open('skala.html',encoding='utf-8').read()
head=sk[:sk.rfind('</style>',0,sk.index('<h1'))]
D=[
("Pferd","Stute","mare",""),("Pferd","Hengst","stallion",""),("Pferd","Wallach","gelding","kastrierter Hengst"),("Pferd","Fohlen","foal",""),("Pferd","Pony","pony",""),
("Pferd","Warmblut","warmblood","Reitpferdetyp"),("Pferd","Vollblut","thoroughbred",""),("Pferd","Kaltblut","draught horse","schweres Arbeitspferd"),
("Pferd","Widerrist","withers","höchste Stelle des Rückens vor dem Sattel"),("Pferd","Kruppe","croup","Hinterhand oberhalb des Schweifs"),("Pferd","Mähne","mane",""),("Pferd","Schweif","tail",""),
("Pferd","Genick","poll","hinter den Ohren"),("Pferd","Nüstern","nostrils",""),("Pferd","Flanke","flank","Seite hinter dem Rippenbogen"),("Pferd","Fessel","pastern","zwischen Huf und Röhrbein"),
("Pferd","Röhrbein","cannon bone",""),("Pferd","Sprunggelenk","hock","Gelenk am Hinterbein"),("Pferd","Huf","hoof",""),("Pferd","Hufeisen","horseshoe",""),
("Farben","Fuchs","chestnut","rotbraun, Mähne nicht schwarz"),("Farben","Brauner","bay","braun mit schwarzer Mähne und schwarzem Schweif"),("Farben","Rappe","black horse",""),("Farben","Schimmel","grey","wird mit dem Alter heller"),
("Farben","Blesse","blaze","weißer Streifen im Gesicht"),("Farben","Stern","star","weißer Fleck an der Stirn"),("Farben","Schnippe","snip","weißer Fleck zwischen den Nüstern"),("Farben","Stiefel","white stocking","weißes Bein bis zum Knie oder Sprunggelenk"),
("Ausrüstung","Sattel","saddle",""),("Ausrüstung","Sattelgurt","girth",""),("Ausrüstung","Steigbügel","stirrup",""),("Ausrüstung","Schabracke","saddle cloth","Decke unter dem Sattel"),
("Ausrüstung","Zaum","bridle",""),("Ausrüstung","Trense","snaffle bridle","Zaum mit einem Gebiss ohne Hebel"),("Ausrüstung","Kandare","curb bridle","Zaum mit Hebelwirkung, bei höheren Prüfungen"),("Ausrüstung","Gebiss","bit",""),
("Ausrüstung","Zügel","rein",""),("Ausrüstung","Halfter","headcollar (halter)","zum Führen und Anbinden"),("Ausrüstung","Führstrick","lead rope",""),("Ausrüstung","Longe","lunge line",""),
("Ausrüstung","Gerte","riding whip","Hilfsmittel, kein Strafmittel"),("Ausrüstung","Sporen","spurs",""),("Ausrüstung","Reithelm","riding helmet",""),("Ausrüstung","Reitstiefel","riding boots",""),("Ausrüstung","Gamaschen","leg boots","Schutz für die Beine"),
("Bahn","Reitbahn","riding arena",""),("Bahn","Hufschlag","track","der Weg entlang der Bande"),("Bahn","Zirkel","circle","20 m Durchmesser"),("Bahn","Volte","volte","kleiner Zirkel"),
("Bahn","Mittellinie","centre line",""),("Bahn","Diagonale","diagonal",""),("Bahn","Handwechsel","change of rein","Wechsel der Richtung"),("Bahn","Schlangenlinie","serpentine",""),("Bahn","Acht","figure of eight",""),("Bahn","Bande","arena wall (boards)",""),("Bahn","Ecke","corner",""),
("Reiten","Hilfen","aids","Zeichen des Reiters an das Pferd"),("Reiten","Gewichtshilfe","weight aid",""),("Reiten","Schenkelhilfe","leg aid",""),("Reiten","Zügelhilfe","rein aid",""),("Reiten","Sitz","seat",""),
("Reiten","treibend","driving","vorwärts treiben"),("Reiten","verwahrend","containing","begrenzend, zurückhaltend"),("Reiten","Anlehnung","contact","Verbindung von Reiterhand und Pferdemaul"),
("Reiten","Leichttraben","rising trot",""),("Reiten","Aussitzen","sitting trot",""),("Reiten","Übergang","transition",""),("Reiten","Halt","halt",""),("Reiten","Rückwärtsrichten","rein-back",""),
("Skala","Takt","rhythm (regularity)","Punkt 1 der Skala der Ausbildung"),("Skala","Losgelassenheit","suppleness (relaxation)","Punkt 2"),("Skala","Anlehnung","contact","Punkt 3"),("Skala","Schwung","impulsion","Punkt 4"),("Skala","Geraderichten","straightness","Punkt 5"),("Skala","Versammlung","collection","Punkt 6"),("Skala","Durchlässigkeit","throughness","das Ziel der Ausbildung"),
("Gangarten","Schritt","walk","Viertakt"),("Gangarten","Trab","trot","Zweitakt"),("Gangarten","Galopp","canter","Dreitakt mit Schwebe; schneller, im Rennsport: gallop"),
("Lektionen","Schenkelweichen","leg-yield",""),("Lektionen","Schulterherein","shoulder-in",""),("Lektionen","Kruppeherein","haunches-in",""),("Lektionen","Renvers","haunches-out (renvers)",""),("Lektionen","Traversale","half-pass",""),
("Lektionen","Außengalopp","counter-canter",""),("Lektionen","Fliegender Wechsel","flying change","Galoppwechsel in der Schwebephase"),("Lektionen","Pirouette","pirouette",""),("Lektionen","Piaffe","piaffe","Trab auf der Stelle"),("Lektionen","Passage","passage","Trab mit langer Schwebephase"),
("Stall","Box","loose box",""),("Stall","Koppel","paddock (field)",""),("Stall","Heu","hay",""),("Stall","Hafer","oats",""),("Stall","Einstreu","bedding",""),("Stall","Ausmisten","to muck out",""),
("Stall","Putzzeug","grooming kit",""),("Stall","Hufkratzer","hoof pick",""),("Stall","Striegel","curry comb",""),("Stall","Kardätsche","body brush",""),("Stall","Hufschmied","farrier",""),("Stall","Tierarzt","vet",""),("Stall","Reitlehrer","riding instructor",""),
]
cats=[]
for c,*_ in D:
    if c not in cats: cats.append(c)
css='''
.sr{width:100%;height:40px;border:1px solid #d8d8d8;background:var(--grey);font:inherit;font-size:16px;padding:0 12px;margin-top:6px}
.chips{display:flex;flex-wrap:wrap;gap:2px;margin:6px 0}
.chips button{border:0;background:var(--grey);font:inherit;font-size:13px;padding:7px 10px;cursor:pointer;color:#555}
.chips button.on{background:var(--lime);color:var(--ink);font-weight:700}
.g{display:grid;grid-template-columns:1fr 1fr;gap:8px;padding:8px 0;font-size:15px;line-height:1.25;border-bottom:1px dotted var(--line)}
.g b{font-weight:700}.g em{font-style:normal;color:#444}
.g small{grid-column:1/3;color:#888;font-size:12px;line-height:1.3}
.cnt{font-size:11px;color:#888;margin:6px 0}
.zurueck{display:inline-block;margin:10px 0 0 2px;font:700 13px Carlito,sans-serif;letter-spacing:.06em;color:#1a1a1a;text-decoration:none}
'''
body='''</style>
<a class="zurueck" href="index.html">← PASSAGE</a>
<h1>Reitsprache Deutsch – English</h1>
<div class="dot"></div>
<input class="sr" id="q" type="search" placeholder="Suchen: Wort oder English" aria-label="Suchen">
<div class="chips" id="chips"></div>
<div class="cnt" id="cnt"></div>
<div id="list"></div>
<p class="note">Testseite PASSAGE · Reitsprache · Entwurf, eigene Formulierung. Englisch ist britisch-international (FEI) gewählt; Fachbegriffe können je nach Land abweichen.</p>
<script>
const D=%s;
const cats=['Alle',%s];let cat='Alle';
const $=s=>document.querySelector(s);
function norm(s){return s.toLowerCase().normalize('NFD').replace(/[\\u0300-\\u036f]/g,'')}
function esc(s){return s.replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]))}
function draw(){
  const t=norm($('#q').value.trim());
  const L=D.filter(r=>(cat==='Alle'||r[0]===cat)&&(!t||norm(r[1]).includes(t)||norm(r[2]).includes(t)));
  $('#cnt').textContent=L.length+' Begriffe';
  $('#list').innerHTML=L.map(r=>'<div class="g"><b lang="de">'+esc(r[1])+'</b><em lang="en">'+esc(r[2])+'</em>'+(r[3]?'<small lang="de">'+esc(r[3])+'</small>':'')+'</div>').join('')||'<p class="note">Nichts gefunden.</p>';
}
$('#chips').innerHTML=cats.map(c=>'<button data-c="'+c+'"'+(c===cat?' class="on"':'')+'>'+c+'</button>').join('');
$('#chips').onclick=e=>{const b=e.target.closest('button');if(!b)return;cat=b.dataset.c;[...$('#chips').children].forEach(x=>x.classList.toggle('on',x===b));draw()};
$('#q').oninput=draw;draw();
</script>
'''%(json.dumps(D,ensure_ascii=False),','.join("'%s'"%c for c in cats))
open('reitsprache.html','w',encoding='utf-8').write(head+css+body)
print(len(D),cats)
