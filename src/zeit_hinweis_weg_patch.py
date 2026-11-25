# PASSAGE 25.11.2026: Hinweiszeile unter den Zeitleisten ("Seitlich wischen · antippen ...") entfernt. Idempotent.
import re, sys
P = """+'<p class="tline">Seitlich wischen · antippen für Bild und Text. Dunkle Felder: Zeitgeschehen. Bilder: Wikipedia / Wikimedia Commons.</p>'"""
n = 0
for f in ['index.html', 'src/zeit.js', 'src/zeit.tpl.js']:
    s = open(f, encoding='utf-8').read()
    n += s.count(P)
    open(f, 'w', encoding='utf-8').write(s.replace(P, ''))
if n == 0: sys.exit('schon angewendet')
s = open('index.html', encoding='utf-8').read()
if '--noversion' not in sys.argv:
    s = re.sub(r'(<meta name="app-version" content=")([^"]*)(")', lambda m: m.group(1) + '2026-11-25l' + m.group(3), s, count=1)
open('index.html', 'w', encoding='utf-8').write(s)
print('ok', n)
