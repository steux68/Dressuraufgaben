# "und"/"and" in Knopf-, Kachel-, Filter- und Kartentiteln durch "&" ersetzen (nur kurze Titel, keine Saetze). Idempotent. 06.11.2026
import re, sys
s = open('index.html', encoding='utf-8').read()
L = ['Kopf und Auge', 'Maul und Nüstern', 'Haltung und Beine', 'Augen und Nase', 'Beine und Hufe', 'Geschichte und Zitate',
     'Umgang und Stall', 'Verhalten im Gelände und im Straßenverkehr', 'Sattel- und Zaumzeugkunde', 'Pferdehaltung und Fütterung',
     'Pferdekrankheiten und Erste Hilfe', 'Huf und Beschlag', 'Nerven und Gefäße im Huf', 'Alexander und Bukephalos',
     'Ritter und Schlachtross', 'Kopf und Hals tief', 'Lecken und Kauen', 'Scharren und Stampfen', 'Schnelles Drehen und Zucken',
     'Kot und Wasser', 'Obst und Karotten', 'Hell und dunkel', 'Trachten und Ballen', 'Netzhaut und Aderhaut',
     'Kniescheibe und Kniegelenk', 'Mensch und Pferd', 'Dichter und Denker', 'Info und Anleitung', 'Bilder und Quellen',
     'Reiten und Prüfungen', 'Head and eye', 'Hoof and shoeing', 'Nerves and vessels in the hoof', 'Heels and bulbs',
     'Stifle joint and patella (F)']
n = 0
for t in L:
    u = t.replace(' und ', ' & ').replace(' and ', ' & ').replace('Sattel- und ', 'Sattel- & ')
    n += s.count(t)
    s = s.replace(t, u)
print('ersetzt:', n)
for a, b in [('<h3>Bilder & Quellen</h3>', '<h3>Bilder &amp; Quellen</h3>'), ('<h2>Info & Anleitung</h2>', '<h2>Info &amp; Anleitung</h2>'), ('<h3>Reiten & Prüfungen</h3>', '<h3>Reiten &amp; Prüfungen</h3>')]:
    s = s.replace(a, b)
if '--noversion' not in sys.argv:
    s = re.sub(r'(<meta name="app-version" content=")([^"]*)(")', lambda m: m.group(1) + '2026-11-06zzz79' + m.group(3), s, count=1)
open('index.html', 'w', encoding='utf-8').write(s)
