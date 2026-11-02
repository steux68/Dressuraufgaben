# "Unsere Pferde" ausblenden (App soll allgemein sein). Daten, Fotos und Code bleiben; zum Wiedereinschalten Tab und Kachel zurueckholen. Idempotent. 02.11.2026
import re,sys
s=open('index.html',encoding='utf-8').read()
def rep(old,new):
    global s
    if old in s: s=s.replace(old,new,1)
# Reiter aus der Pferdewissen-Gruppe nehmen (group() blendet Reiter ausserhalb der Gruppe aus)
rep("SUBG=['thsS','thsV','thsK','thsA','thsB','thsP']","SUBG=['thsS','thsV','thsK','thsA','thsB']")
rep("SUBG=['thsS','thsV','thsA','thsB','thsP']","SUBG=['thsS','thsV','thsA','thsB']")
# Kachel auf der Startseite entfernen
s=re.sub(r",\n  \['thsP','Pf','Unsere Pferde','Die Pferde der Reitschule \(in Vorbereitung\)'\]\]\.forEach",r"].forEach",s)
rep("['thsB','Vi','Das Viereck','Buchstaben, Maße, Spiel und Geschichte der Bahn'],\n  ].forEach","['thsB','Vi','Das Viereck','Buchstaben, Maße, Spiel und Geschichte der Bahn']].forEach")
if '--noversion' not in sys.argv:
    s=re.sub(r'(<meta name="app-version" content=")([^"]*)(")',lambda m:m.group(1)+'2026-11-02zzz53'+m.group(3),s,count=1)
open('index.html','w',encoding='utf-8').write(s)
