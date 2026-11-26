# PASSAGE 26.11.2026 (Nacht): Theorie, Zeile "Aufgaben R1-R6": statt Dunkelblau grau (dunkelste Flaeche der App, ausserhalb des Neon/Grau-Systems). Idempotent.
import re, sys
s = open('index.html', encoding='utf-8').read()
if 'id="theograu-css"' in s: sys.exit('schon angewendet')
css = '<style id="theograu-css">#theo .tests span.on{background:#ececea!important;border-color:#ececea!important;color:#1a1a1a!important}</style>'
s = s.replace('</head>', css + '</head>', 1)
if '--noversion' not in sys.argv:
    s = re.sub(r'(<meta name="app-version" content=")([^"]*)(")', lambda m: m.group(1) + '2026-11-26k' + m.group(3), s, count=1)
open('index.html', 'w', encoding='utf-8').write(s); print('ok')
