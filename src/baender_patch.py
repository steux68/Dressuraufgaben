# Dressuraufgaben-Liste: Abstand ueber den R-Kreisen kleiner, jede Aufgabe samt Lernkarten-Zeile als Band, Baender abwechselnd grau/weiss. 24.11.2026
import re,sys
s=open('index.html',encoding='utf-8').read()
if 'baender-css' in s: sys.exit('schon angewendet')
CSS='''<style id="baender-css">
#tiles{gap:0!important}
#tiles>.tile.tile.tile{background:#f4f4f2!important}
#tiles>.tile.tile.tile:nth-child(4n+3),#tiles>.tile.tile.tile:nth-child(4n+4){background:#fff!important}
#tiles>.tile.hasl{padding:8px 8px 4px!important}
#tiles>.tile.lkrow.lkrow{margin:0!important;width:100%!important;padding:4px 10px 10px 36px!important}
#tiles>.tile.lkrow::before{left:12px!important;top:-4px!important;height:calc(50% + 4px)!important}
</style>
'''
i=s.rindex('</head>'); s=s[:i]+CSS+s[i:]
s=re.sub(r'(<meta name="app-version" content=")[^"]*"',r'\g<1>2026-11-24k"',s,count=1)
open('index.html','w',encoding='utf-8').write(s)
