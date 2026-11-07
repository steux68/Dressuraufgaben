# Pop-ups (.gpop, .tlpop): Seitenränder auf den 18px-Inhaltsrand (10px Puffer). Idempotent. 07.11.2026
import re,sys
s=open('index.html',encoding='utf-8').read()
if 'id="popedge-css"' in s: sys.exit('schon angewendet')
CSS='''<style id="popedge-css">
.gpop{padding-left:18px!important;padding-right:18px!important}
.tlpop{padding-left:18px!important;padding-right:18px!important}
</style>
'''
assert s.count('</head>')==1
s=s.replace('</head>',CSS+'</head>',1)
if '--noversion' not in sys.argv:
    s=re.sub(r'(<meta name="app-version" content=")([^"]*)(")',lambda m:m.group(1)+'2026-11-07zzz105'+m.group(3),s,count=1)
open('index.html','w',encoding='utf-8').write(s)
