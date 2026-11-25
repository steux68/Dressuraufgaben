# PASSAGE 25.11.2026: Pfeile der beiden Zeitleisten (Reitkunst und Dressur / Das Pferd) mittig auf der Jahresleiste,
# deckend weiss (Leiste und Daten scheinen nicht mehr durch). Idempotent.
import re, sys
s = open('index.html', encoding='utf-8').read()
if 'id="zeitpfeile-css"' in s: sys.exit('schon angewendet')
css = '''<style id="zeitpfeile-css">
/* Jahresleiste: .tltk top calc(50% - 6px), 23 px hoch -> Mitte bei 50% + 5.5px; Pfeil 26 px, margin-top -13 px */
.tlw>.tlar{top:calc(50% + 5.5px);background:#fff!important;box-shadow:0 0 0 1px rgba(0,0,0,.18)!important}
.tlw>.tlar[data-off]{opacity:1}
.tlw>.tlar[data-off] svg{opacity:.3}
</style>
'''
assert s.count('</head>') == 1
s = s.replace('</head>', css + '</head>', 1)
if '--noversion' not in sys.argv:
    s = re.sub(r'(<meta name="app-version" content=")([^"]*)(")', lambda m: m.group(1) + '2026-11-25k' + m.group(3), s, count=1)
open('index.html', 'w', encoding='utf-8').write(s)
print('ok')
