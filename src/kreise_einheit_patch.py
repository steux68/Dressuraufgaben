# PASSAGE 26.11.2026: Kreis 31 px -> 30 px (wie DOCH! .no). Idempotent.
import re, sys
s=open('index.html',encoding='utf-8').read()
a='#tiles .tile.ready.hasl .code{width:31px!important;height:31px!important;min-width:31px!important'
if a not in s: sys.exit('schon angewendet')
s=s.replace(a,a.replace('31px','30px'))
if '--noversion' not in sys.argv:
    s=re.sub(r'(<meta name="app-version" content=")([^"]*)(")',lambda m:m.group(1)+'2026-11-26s'+m.group(3),s,count=1)
open('index.html','w',encoding='utf-8').write(s); print('ok')
