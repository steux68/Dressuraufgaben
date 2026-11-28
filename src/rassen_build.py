# Baut rassen.html (Rassen + Begriffe) mit den Schriften aus skala.html. Aufruf: python3 -I src/rassen_build.py
import re,json
s=open('skala.html',encoding='utf-8').read()
pre=s[:s.find('<body>')+6].replace('Skala der Ausbildung – PASSAGE Test','Rassen und Begriffe – PASSAGE')
CSS='''<style>
:root{--red:#e30613;--lime:#cdff3e;--line:#b8b8b8;--grey:#f2f2f2;--ink:#1a1a1a}
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:"Carlito",Calibri,system-ui,sans-serif;color:var(--ink);background:#fff;max-width:520px;margin:0 auto;padding:12px 12px 40px}
.dot{height:1px;background:repeating-linear-gradient(to right,var(--line) 0 1px,transparent 1px 3px)}
.zurueck{display:inline-block;margin:10px 0 0 14px;font:700 13px Carlito,sans-serif;letter-spacing:.06em;color:#1a1a1a;text-decoration:none}
h1{font-size:13px;letter-spacing:.08em;color:var(--red);font-weight:700;text-transform:uppercase;padding:8px 0}
.tabs{display:grid;grid-template-columns:1fr 1fr;gap:4px;margin:8px 0}
.tabs button{border:0;background:var(--grey);font:700 14px Carlito,sans-serif;letter-spacing:.08em;text-transform:uppercase;padding:11px 0;cursor:pointer;color:#555}
.tabs button.on{background:var(--lime);color:var(--ink)}
.intro{font-size:14px;line-height:1.4;color:#444;margin:6px 0 10px}
.card{background:var(--grey);margin:8px 0}
.card>button{all:unset;box-sizing:border-box;display:flex;align-items:center;gap:10px;width:100%;padding:12px;cursor:pointer}
.card .nm{font-size:18px;font-weight:700;flex:1}.card .kt{font-size:12px;color:#777}
.card .pl{font-size:18px;color:#999;transition:transform .15s}.card.open .pl{transform:rotate(45deg)}
.card .body{display:none;padding:0 12px 12px;font-size:14px;line-height:1.4}.card.open .body{display:block}
.card .body img{display:block;max-width:100%;max-height:200px;margin:2px auto 10px;mix-blend-mode:multiply}
.card .body .r{display:grid;grid-template-columns:92px 1fr;gap:8px;padding:6px 0;border-top:1px dotted var(--line)}
.card .body .r b{color:var(--red);font-size:12px;letter-spacing:.06em;text-transform:uppercase;padding-top:2px}
.ph{margin:2px 0 10px;text-align:center}.ph img{display:block;max-width:100%;max-height:260px;margin:0 auto}.ph figcaption{font-size:11px;color:#777;margin-top:4px}.ph a{color:#777}
.grp{font-size:12px;letter-spacing:.08em;color:var(--red);font-weight:700;text-transform:uppercase;margin:18px 0 4px}
.row{display:grid;grid-template-columns:104px 1fr;gap:10px;padding:9px 0;font-size:14px;line-height:1.4;border-bottom:1px dotted var(--line)}
.row b{font-size:15px}
.sw{display:inline-block;width:11px;height:11px;border-radius:50%;margin-right:6px;vertical-align:-1px;border:1px solid #bbb}
.note{font-size:12px;color:#888;margin-top:16px;line-height:1.4}
[hidden]{display:none!important}
</style>'''
RASSEN=[
 ('Vollblut','Englisches Vollblut','Rennpferd',[('Typ','schlank, hochbeinig, sehr schnell'),('Herkunft','England, 17./18. Jahrhundert, gezüchtet aus orientalischen Hengsten'),('Stockmaß','meist 160–170 cm'),('Wesen','temperamentvoll, sensibel, leistungsbereit'),('Heute','Galopprennen, Vielseitigkeit; Einkreuzung in viele Sportpferde-Rassen')]),
 ('Araber','Araber','Ausdauer, edel',[('Typ','kleiner, trockener Kopf mit eingebogenem Profil, hoch angesetzter Schweif'),('Herkunft','Arabische Halbinsel; eine der ältesten Zuchten'),('Stockmaß','meist 145–155 cm'),('Wesen','menschenbezogen, ausdauernd, lebhaft'),('Heute','Distanzreiten, Zucht; Ahne vieler Rassen, auch des Vollbluts')]),
 ('Hannoveraner','Hannoveraner','Sportpferd, Warmblut',[('Typ','kräftiges, elegantes Warmblut mit guten Grundgangarten'),('Herkunft','Niedersachsen, Deutschland'),('Stockmaß','meist 160–172 cm'),('Wesen','leistungsbereit, gut zu reiten'),('Heute','Dressur und Springen bis in den Spitzensport')]),
 ('Lipizzaner','Lipizzaner','Barockpferd, Wien',[('Typ','kompakt, kräftiger Hals, starke Hinterhand, Barockpferd'),('Herkunft','Gestüt Lipica (heute Slowenien), gegründet 1580'),('Farbe','kommen dunkel zur Welt und werden meist Schimmel'),('Wesen','lernwillig, ausdauernd, spät reif'),('Heute','Spanische Hofreitschule in Wien; Gestüt Piber in der Steiermark')]),
 ('Haflinger','Haflinger','Tirol, Fuchs mit heller Mähne',[('Typ','kräftiges, genügsames Gebirgspferd'),('Herkunft','Tirol; Name nach dem Ort Hafling in Südtirol'),('Farbe','Fuchs mit hellem Langhaar (Mähne und Schweif)'),('Stockmaß','meist 138–150 cm'),('Heute','Freizeit, Fahren, Reiten; auch für Kinder und Anfänger')]),
 ('Noriker','Noriker','Kaltblut, Österreich',[('Typ','schweres, aber bewegliches Gebirgs-Kaltblut'),('Herkunft','Salzburg und das Alpenland'),('Farbe','Braune, Füchse, Rappen und Schecken; die Tigerschecken sind besonders bekannt'),('Wesen','ruhig, ausgeglichen, trittsicher'),('Heute','Arbeitspferd in den Bergen, Kutschen, Brauerei-Gespanne')]),
 ('Islandpferd','Islandpferd','fünf Gangarten',[('Typ','klein, robust, dichtes Fell'),('Herkunft','Island, seit der Besiedlung im 9./10. Jahrhundert fast rein gezüchtet'),('Gangarten','zusätzlich zu Schritt, Trab und Galopp: Tölt (viertaktig) und Rennpass'),('Stockmaß','meist 130–145 cm'),('Heute','Freizeit- und Turnierreiten (Tölt)')]),
 ('Shetlandpony','Shetlandpony','Pony, klein',[('Typ','sehr klein, kräftig, dichtes Fell und lange Mähne'),('Herkunft','Shetlandinseln, Schottland'),('Stockmaß','bis etwa 107 cm'),('Wesen','klug, robust, bisweilen eigenwillig'),('Heute','Kinderpony, Fahren')]),
]
LOCAL={'Vollblut':('vollblut.webp','Thoms von Nathusius (1866–1904): Englisches Vollblut „No Chance“, um 1880 · gemeinfrei · Wikimedia Commons')}
WIKI={'Vollblut': 'de:Englisches_Vollblut|en:Thoroughbred', 'Araber': 'de:Araber_(Pferd)|en:Arabian_horse', 'Hannoveraner': 'de:Hannoveraner|en:Hanoverian_horse', 'Lipizzaner': 'de:Lipizzaner|en:Lipizzan', 'Haflinger': 'de:Haflinger|en:Haflinger', 'Noriker': 'de:Noriker|en:Noric_horse', 'Islandpferd': 'de:Islandpferd|en:Icelandic_horse', 'Shetlandpony': 'de:Shetlandpony|en:Shetland_pony'}
GR=[('Geschlecht und Alter',[('Hengst','männliches Pferd, nicht kastriert; wird für die Zucht verwendet'),('Stute','weibliches Pferd; die Tragzeit dauert etwa elf Monate'),('Wallach','männliches Pferd, das kastriert wurde; meist ruhiger und deshalb das typische Reitpferd'),('Fohlen','Jungtier im ersten Lebensjahr; je nach Geschlecht Hengstfohlen oder Stutfohlen'),('Jährling','Pferd im zweiten Lebensjahr')]),
 ('Maß und Typ',[('Stockmaß','Höhe vom Boden bis zum höchsten Punkt des Widerrists, mit dem Messstock gemessen'),('Pony','Stockmaß bis 148 cm (ohne Hufeisen); größere Tiere heißen Pferde'),('Vollblut','Rennpferd-Zucht; schlank, schnell, sensibel'),('Warmblut','Reit- und Sportpferde; ausgeglichener als Vollblüter, leichter als Kaltblüter'),('Kaltblut','schweres Arbeitspferd, ruhig und kräftig. „Kalt“ und „warm“ meinen das Temperament, nicht die Körpertemperatur')]),
 ('Farben',[('Fuchs','|#a6522a|rotbraunes Fell; Mähne und Schweif gleich oder heller'),('Rappe','|#1e1e1e|schwarzes Fell, Mähne und Schweif'),('Brauner','|#5b3b24|braunes Fell mit schwarzer Mähne, schwarzem Schweif und schwarzen Beinen'),('Schimmel','|#e9e9e6|graues bis weißes Fell; die Tiere kommen dunkel zur Welt und werden mit den Jahren heller'),('Falbe','|#d7b779|gelblich bis graubeige, meist mit dunklem Streifen auf dem Rücken (Aalstrich)'),('Schecke','|#fff|weiße Flecken auf farbigem Grund')]),
 ('Abzeichen im Gesicht',[('Stern','weißer Fleck auf der Stirn'),('Blesse','breiter weißer Streifen über Stirn und Nase'),('Schnippe','weißer Fleck zwischen den Nüstern')]),
]
html=pre+CSS+'''
<a class="zurueck" href="index.html">← PASSAGE</a>
<h1>Rassen und Begriffe</h1>
<div class="dot"></div>
<div class="tabs" role="tablist"><button class="on" data-t="r" role="tab">Rassen</button><button data-t="b" role="tab">Begriffe</button></div>
<div id="r"><p class="intro">Acht Rassen, die man im Reitstall und in Österreich kennt. Tippe auf eine Rasse.</p><div id="rl"></div></div>
<div id="b" hidden><div id="bl"></div></div>
<p class="note">Angaben zu Größe und Herkunft sind Richtwerte. Testseite PASSAGE · Rassen und Begriffe · Entwurf, eigene Formulierung</p>
<script>
const R=%s, G=%s;
const $=s=>document.querySelector(s), esc=t=>t.replace(/[&<]/g,c=>({'&':'&amp;','<':'&lt;'}[c]));
$('#rl').innerHTML=R.map((r,i)=>`<div class="card" data-i="${i}"><button aria-expanded="false"><span class="nm">${esc(r[1])}</span><span class="kt">${esc(r[2])}</span><span class="pl">+</span></button><div class="body">${r[5]?`<figure class="ph"><img src="img/rassen/${r[5][0]}" alt="${esc(r[1])}" decoding="async"><figcaption>${esc(r[5][1])}</figcaption></figure>`:`<figure class="ph" data-w="${r[4]}" hidden><img alt="${esc(r[1])}" decoding="async"><figcaption></figcaption></figure>`}${r[3].map(x=>`<div class="r"><b>${x[0]}</b><span>${esc(x[1])}</span></div>`).join('')}</div></div>`).join('');
$('#bl').innerHTML=G.map(g=>`<div class="grp">${g[0]}</div>`+g[1].map(x=>{let t=x[1],sw='';const m=t.match(/^\\|(#[0-9a-f]+)\\|/i);if(m){sw=`<i class="sw" style="background:${m[1]}"></i>`;t=t.slice(m[0].length)}return `<div class="row"><b>${sw}${esc(x[0])}</b><span>${esc(t)}</span></div>`}).join('')).join('');
let C={};try{C=JSON.parse(localStorage.getItem('ra_pics')||'{}')}catch(e){}
function pic(f){if(!f.dataset.w||f.dataset.done)return;f.dataset.done=1;const L=f.dataset.w.split('|'),im=f.querySelector('img'),cp=f.querySelector('figcaption');
 const show=o=>{im.onload=()=>{f.hidden=false};im.src=o.u;cp.innerHTML='Foto: <a href="'+o.p+'" target="_blank" rel="noopener">Wikipedia</a> · Urheber und Lizenz dort auf der Bildseite'};
 const k=f.dataset.w;if(C[k]){show(C[k]);return}
 const nx=i=>{if(i>=L.length)return;const q=L[i].indexOf(':'),lg=L[i].slice(0,q),t=L[i].slice(q+1);
  fetch('https://'+lg+'.wikipedia.org/api/rest_v1/page/summary/'+encodeURIComponent(t)).then(r=>r.ok?r.json():null).then(j=>{const u=j&&j.thumbnail&&j.thumbnail.source;if(u){C[k]={u:u,p:j.content_urls.desktop.page};try{localStorage.setItem('ra_pics',JSON.stringify(C))}catch(e){}show(C[k])}else nx(i+1)},()=>nx(i+1))};nx(0)}
document.addEventListener('click',e=>{const c=e.target.closest('.card>button');if(c){const p=c.parentNode;p.classList.toggle('open');if(p.classList.contains('open')){const f=p.querySelector('.ph');if(f)pic(f)}c.setAttribute('aria-expanded',p.classList.contains('open'));return}
 const t=e.target.closest('.tabs button');if(t){document.querySelectorAll('.tabs button').forEach(b=>b.classList.toggle('on',b===t));$('#r').hidden=t.dataset.t!=='r';$('#b').hidden=t.dataset.t!=='b'}});
</script>
</body></html>
''' % (json.dumps([[r[0],r[1],r[2],r[3],WIKI[r[0]],LOCAL.get(r[0])] for r in RASSEN],ensure_ascii=False),json.dumps(GR,ensure_ascii=False))
open('rassen.html','w',encoding='utf-8').write(html);print(len(html))
