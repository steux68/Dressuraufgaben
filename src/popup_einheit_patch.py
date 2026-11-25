# Alle Popups (.tlpop) auf die Masse des Anatomie-Popups: Kopfzeile, Schliessen-Knopf, Seitenrand, Pfeilglyphe; Hilfen-Quiz-Titel 16 px. 25.11.2026
import re,sys
s=open('index.html',encoding='utf-8').read()
if 'popup-einheit-css' in s: sys.exit('schon angewendet')
CSS='<style id="popup-einheit-css">\n.tlpop:not(.full) .tltop{padding:4px 4px 3px;min-height:0}\n.tlpop .tlx{padding:4px;margin:-4px}\n.tlpop .tlx svg{width:22px;height:22px}\n.tlpop:not(.full) .tlcard .tlbody{padding-left:4px;padding-right:4px}\n.tlpop .tlar svg{width:22px;height:22px}\n#thHi .hiQ .hiN{font-size:16px;line-height:1.15}\n#thHi .hiQ{background:#fff}\n</style>\n'
i=s.rindex('</head>'); s=s[:i]+CSS+s[i:]
s=re.sub(r'(<meta name="app-version" content=")[^"]*"',r'\g<1>2026-11-25c"',s,count=1)
open('index.html','w',encoding='utf-8').write(s)
