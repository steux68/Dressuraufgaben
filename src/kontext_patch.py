# Titelseite: Leitsatz + neuer Untertitel; Figuren-Karten: Kontextbox (Was lernen wir? / Was braucht das Pferd? / Worauf achten wir?)
# für fünf Figuren. Bewusst nur allgemeine, gängige Aussagen, nichts Medizinisches. Idempotent. 22.11.2026
# Aufruf: python3 -I src/kontext_patch.py [--noversion]
import re, sys
s = open('index.html', encoding='utf-8').read()
if 'id="thCx"' in s:
    sys.exit('schon angewendet')

def rep(old, new, count=1):
    global s
    assert s.count(old) == count, (old[:70], s.count(old))
    s = s.replace(old, new)

# 1. Titelseite
rep('<p class="isub">Dressuraufgaben R1–R6 · Lernen, Spiel, Theorie · Pferdewissen</p>',
    '<p class="imotto">Das Pferd verstehen, bevor wir etwas von ihm verlangen.</p>'
    '<p class="isub">Dressuraufgaben R1–R6 · Pferdewissen · Geschichte</p>')
CSS = ('<style id="kontextCss">'
       '#intro .imotto{margin:6px 14px 0;text-align:center;font-size:15px;line-height:1.3;font-style:italic;color:#222}'
       '#thCx{margin:12px 0 0}#thCx[hidden]{display:none}'
       '#thCx p{margin:6px 0 0;font-size:14px;line-height:1.4;color:#222}'
       '#thCx p b{font-weight:700;display:block;font-size:12px;letter-spacing:.04em;text-transform:uppercase;color:#8a8a86}'
       '#thCx p.cxn{font-size:12px;color:#8a8a86;font-style:italic}'
       '</style>')
rep('<section id="intro" class="intro"', CSS + '<section id="intro" class="intro"')

# 2. Kontextbox in der Figuren-Lernkarte
rep('<p class="de" id="thDe"></p>', '<p class="de" id="thDe"></p><div id="thCx" hidden></div>')

CTX = r"""/* Kontextbox: nur allgemeine Aussagen, Entwurf, mit Reitlehrer abzugleichen */
const CTX={
 'Tour (10 m)':['Das Pferd genau auf einer gebogenen Linie zu führen.','Gleichgewicht, Geschmeidigkeit und gleichmäßigen Takt in der Biegung.','Das Pferd fällt nicht über die äußere Schulter weg und behält den Takt. Die Größe passt zu seinem Ausbildungsstand.'],
 'Große Tour':['Eine runde, gleichmäßige Kreislinie zu reiten.','Platz und Ruhe zum Ausbalancieren. Der Kreis ist weiter als die Volte.','Gleichmäßige Biegung, gleicher Takt, ein runder Kreis ohne Ecken.'],
 'Diagonale wechseln':['Die Hand zu wechseln und eine gerade Linie zu reiten.','Klare Hilfen rechtzeitig vor dem Wechselpunkt, damit es gerade bleibt.','Gerade Linie von Punkt zu Punkt, in der Ecke gleiches Tempo und gleicher Takt.'],
 'Einfache Schlangenlinie':['Einen flachen Bogen zu reiten und wieder auf den Hufschlag zurückzukehren.','Geschmeidigkeit, um sich sanft in die Biegung hinein und wieder hinaus zu bewegen.','Gleichmäßiger, flacher Bogen ohne Ecken. Takt und Tempo bleiben gleich.'],
 'Schlangentour in 3 Bögen':['Drei gleichmäßige Bögen zu reiten und die Linie vorauszuplanen.','Zeit zum Umstellen: Auf der Mittellinie wird es gerade, dann biegt es sich andersherum.','Gleich große Bögen, gerade auf der Mittellinie, gleicher Takt. Galopp mit Fußwechsel nur, wenn beide dafür ausgebildet sind.']
};
function ctx(f){const b=g('thCx'),c=CTX[f.n];
 if(!c){b.hidden=true;b.textContent='';return}
 b.hidden=false;
 b.innerHTML='<p><b>Was lernen wir?</b>'+c[0]+'</p><p><b>Was braucht das Pferd?</b>'+c[1]+'</p><p><b>Worauf achten wir?</b>'+c[2]+'</p><p class="cxn">Im Zweifel den Reitlehrer fragen.</p>';}

"""
rep('/* Figuren lernen */\n', CTX + '/* Figuren lernen */\n')

# showLearn und lockAll (Höhenreservierung) rufen ctx() auf
pat = "g('thDe').textContent=f.g?(f.g.startsWith('Österr')?f.g:'Deutsch (FN): '+f.g):'';"
rep(pat, pat + 'ctx(f);', count=2)

if '--noversion' not in sys.argv:
    s, n = re.subn(r'(<meta name="app-version" content=")([^"]*)(")', lambda m: m.group(1) + '2026-11-22b' + m.group(3), s, count=1)
    assert n == 1
open('index.html', 'w', encoding='utf-8').write(s)
print('ok')
