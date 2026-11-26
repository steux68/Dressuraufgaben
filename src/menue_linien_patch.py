# PASSAGE 26.11.2026: Menuebalken unten ohne gepunktete Trennlinien (Farbkontrast genuegt); nur das weisse Band 05 "Material & Links" behaelt oben/unten die Punktlinie. Idempotent.
import re, sys
s = open('index.html', encoding='utf-8').read()
if 'id="menue-linien-css"' in s: sys.exit('schon angewendet')
dot = 'repeating-linear-gradient(to right,#b8b8b8 0 1px,transparent 1px 3px)'
css = ('<style id="menue-linien-css">'
       '.hb[data-i]:not([data-i="4"]){background-image:none!important}'
       '.hb[data-i]:not([data-i="4"])::after,.hb.first[data-i]::before{display:none!important}'
       '.hb[data-i="4"]::before{content:"";position:absolute;left:0;right:0;top:0;height:1px;pointer-events:none;background:' + dot + '}'
       '</style>')
s = s.replace('</head>', css + '</head>', 1)
if '--noversion' not in sys.argv:
    s = re.sub(r'(<meta name="app-version" content=")([^"]*)(")', lambda m: m.group(1) + '2026-11-26o' + m.group(3), s, count=1)
open('index.html', 'w', encoding='utf-8').write(s); print('ok')
