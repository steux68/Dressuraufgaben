# PASSAGE 26.11.2026: Titelband einheitlich (58 px hoch, Logo 42 px hoch mit Luft, Schalter learn|wonder mittig). Gleiche Werte in DOCH! und dasein-design. Idempotent.
import re, sys
s = open('index.html', encoding='utf-8').read()
if 'id="header-einheit-css"' in s: sys.exit('schon angewendet')
css = ('<style id="header-einheit-css">.titlebar{height:58px!important;box-sizing:border-box!important;padding-top:0!important;padding-bottom:0!important}'
       '#brand svg,.titlebar .bmark,.titlebar .brand{height:42px!important;width:auto!important}</style>')
s = s.replace('</head>', css + '</head>', 1)
if '--noversion' not in sys.argv:
    s = re.sub(r'(<meta name="app-version" content=")([^"]*)(")', lambda m: m.group(1) + '2026-11-26q' + m.group(3), s, count=1)
open('index.html', 'w', encoding='utf-8').write(s); print('ok')
