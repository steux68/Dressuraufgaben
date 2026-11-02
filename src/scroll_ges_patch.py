# Koerpersprache und Gesundheit: Seite scrollt in sich, wenn sie hoeher ist als der Platz (Fussleiste verdeckte den Hinweistext). Idempotent. 02.11.2026
import re,sys
s=open('index.html',encoding='utf-8').read()
if 'id="scrollges-css"' in s: sys.exit('schon angewendet')
CSS='''<style id="scrollges-css">
#theo:has(#thBody:not([hidden])),#theo:has(#thGes:not([hidden])){overflow-y:auto;overflow-x:hidden;min-height:0;-webkit-overflow-scrolling:touch}
#thBody:not([hidden]),#thGes:not([hidden]){padding-bottom:12px}
</style>
'''
assert s.count('</head>')==1
s=s.replace('</head>',CSS+'</head>',1)
if '--noversion' not in sys.argv:
    s=re.sub(r'(<meta name="app-version" content=")([^"]*)(")',lambda m:m.group(1)+'2026-11-02zzz64'+m.group(3),s,count=1)
open('index.html','w',encoding='utf-8').write(s)
