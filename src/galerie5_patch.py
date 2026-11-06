# Galerie: 4 weitere Tafeln der Wellcome Collection (Public Domain Mark), 06.11.2026. Idempotent.
import re, sys
s = open('index.html', encoding='utf-8').read()
if 'markham_maisterpeece.jpg' in s:
    print('schon angewendet'); sys.exit(0)
L = 'Public Domain Mark · Wellcome Collection'
E = [
 ("stubbs_tab5", "Muskeln und Knochen: Umrisszeichnung, Seitenansicht", "George Stubbs (1724–1806), Kupferstich mit Radierung", "„The Anatomy of the Horse“, Tab. V", "1766",
  "Eine der berühmten Tafeln von George Stubbs: das Pferd von der Seite, nur mit feinen Linien gezeichnet. Man sieht die Rippen, das Skelett der Beine und einen Teil der Muskeln am Hals. Die vielen Buchstaben und Zahlen verweisen auf die Erklärungen im Buch.", ['Anatomie','Geschichte','Kunst'], [3,2]),
 ("bonheur_vorderbeine", "Studie der Vorderbeine in Bewegung", "Sirouy (Lithograf) nach Rosa Bonheur (1822–1899)", "„Cours d’études d’animaux“", "1859",
  "Zwei Studien der gebeugten Vorderbeine eines Pferdes, einmal heller, einmal dunkler schattiert. Gut zu erkennen sind Knie, Fessel, Huf und die Haare an der Fessel.", ['Anatomie','Bewegung','Kunst'], [3,4]),
 ("markham_maisterpeece", "Markhams „Maisterpeece“: Pferd mit Linien und Buchstaben", "Gervase Markham (1568–1637)", "„Markhams Maisterpeece“, Buch für Schmied, Hufschmied und Pferdearzt", "1636",
  "Ein Holzschnitt aus einem alten englischen Buch für Schmiede und Pferdeärzte. Das Pferd hebt ein Vorderbein, über den Körper laufen Linien mit Buchstaben, und der Rand ist nummeriert. Die Fußzeile sagt, wo die ausklappbare Tafel im Buch eingeklebt werden soll (zwischen den Seiten 236 und 237).", ['Geschichte','Kunst','Stall'], [3,2]),
 ("pferd_arabische_verse", "Ein Pferd aus arabischen Versen", "Maler unbekannt (vermutlich persisch)", "Gouache-Malerei", "",
  "Der Umriss des Pferdes ist aus arabischer Schrift geformt: Der Körper besteht aus Versen. Der Hintergrund ist mit Blumen und Tropfenmustern gemustert, der Rahmen ist vergoldet.", ['Kunst','Geschichte','Kurioses'], [3,2]),
]
def js(x): return "'" + x.replace("\\", "\\\\").replace("'", "\\'") + "'"
rows = ''
for f, n, a, w, j, x, c, sz in E:
    rows += (" {f:'img/galerie/%s.jpg',k:'img/galerie/%s_k.jpg',n:%s,a:%s,w:%s,%sl:%s,x:%s,c:[%s],s:[%d,%d]},\n"
             % (f, f, js(n), js(a), js(w), ("j:%s," % js(j)) if j else '', js(L), js(x), ','.join(js(t) for t in c), sz[0], sz[1]))
key = " {f:'img/galerie/fussfolge.png'"
assert s.count(key) == 1
s = s.replace(key, rows + key)
# Hawkins Tafel V ist schon in der Galerie: Lizenz jetzt bestaetigt (Public Domain Mark, 1860)
i = s.index('hawkins_tafel5.jpg'); e = s.index('}', i)
seg = s[i:e]
seg2 = seg.replace('"j": "London, Chapman & Hall"', '"j": "1860, London, Chapman & Hall"', 1).replace('Gemeinfrei · Wellcome Collection · Nachweis noch zu prüfen', 'Public Domain Mark · Wellcome Collection', 1)
s = s[:i] + seg2 + s[e:]
s = re.sub(r'(<meta name="app-version" content=")([^"]*)(")', lambda m: m.group(1)+'2026-11-06zzz88'+m.group(3), s, count=1)
open('index.html', 'w', encoding='utf-8').write(s); print('ok')
