# PASSAGE 26.11.2026 (Nacht): Wunder-Filter ohne Regenbogen: Chips grau (an) bzw. hell mit gepunkteter Linie und grauer Schrift (aus). Farbe trifft keine Aussage, der Text sagt alles. Idempotent.
import re, sys
s = open('index.html', encoding='utf-8').read()
if 'id="wgrau-css"' in s: sys.exit('schon angewendet')
css = ('<style id="wgrau-css">.wchips:not(.zch) .wchip{background:#ececea!important;color:#1a1a1a!important}'
       '.wchips:not(.zch):has(.off) .wchip:not(.off){background:#cdff3e!important;font-weight:700}'
       '.wchips:not(.zch) .wchip.off{opacity:1!important;background:transparent!important;color:#8a8a86!important;box-shadow:inset 0 0 0 1px #c4c4c0!important;font-weight:400}'
       '</style>')
s = s.replace('</head>', css + '</head>', 1)
if '--noversion' not in sys.argv:
    s = re.sub(r'(<meta name="app-version" content=")([^"]*)(")', lambda m: m.group(1) + '2026-11-26j' + m.group(3), s, count=1)
open('index.html', 'w', encoding='utf-8').write(s); print('ok')
