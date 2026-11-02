# Zeit-Popups (zapop/zbpop): Datum/Epoche als gepunktete Datenzeile unten, Text .98rem. Idempotent. 02.11.2026
import re,sys
s=open('index.html',encoding='utf-8').read()
if 'id="zeitpop-css"' in s: sys.exit('schon angewendet')
CSS='''<style id="zeitpop-css">
#zapop .tlbody,#zbpop .tlbody{display:flex;flex-direction:column}
#zapop .tlbody>*,#zbpop .tlbody>*{flex:none}
#zapop .tlbody h4,#zbpop .tlbody h4{margin-top:10px}
#zapop .tlbody p:not(.gs):not(.tline),#zbpop .tlbody p:not(.gs):not(.tline){font-size:.98rem;line-height:1.45;color:#222}
#zapop .tlbody .tline,#zbpop .tlbody .tline{order:8}
#zapop .tlbody .gs,#zbpop .tlbody .gs{order:9;margin:8px 0 0;padding-top:6px;border-top:1px dotted #b8b8b8;font-size:12px;letter-spacing:0;color:#888}
</style>
'''
assert s.count('</head>')==1
s=s.replace('</head>',CSS+'</head>',1)
if '--noversion' not in sys.argv:
    s=re.sub(r'(<meta name="app-version" content=")([^"]*)(")',lambda m:m.group(1)+'2026-11-02zzz63'+m.group(3),s,count=1)
open('index.html','w',encoding='utf-8').write(s)
