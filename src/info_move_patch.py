#!/usr/bin/env python3
"""Pferde-App: Info-Knopf aus der Kopfzeile, Schalter ganz nach rechts (wie dasein-design).
Info bleibt erreichbar: fettes INFO im Tipp-Balken und Link "Info" in der Fusszeile (idempotent)."""
import re
s=open('index.html',encoding='utf8').read()
if 'id="info-move"' not in s:
    css='<style id="info-move">#infoBtn{display:none!important}.titlebar .wsw{margin-right:-6px!important}.copy .ilink{margin-left:12px;font:inherit;font-size:inherit;color:inherit;text-decoration:underline;background:none;border:0;padding:4px 2px;cursor:pointer}#tipInfo{text-decoration:underline;cursor:pointer}</style>'
    js=('<script id="info-move-js">(function(){var b=document.getElementById("infoBtn");function o(){if(b)b.click();}'
        'var t=document.getElementById("tipInfo");if(t)t.addEventListener("click",o);'
        'var l=document.getElementById("infoLink");if(l)l.addEventListener("click",o);})();</script>')
    s=s.replace('</head>',css+'</head>',1)
    s=s.replace('siehe <b>INFO</b>','siehe <b id="tipInfo" role="button" tabindex="0">INFO</b>',1)
    s=s.replace('<span>© Steuart JM HARRISON (steux)</span></footer>','<span>© Steuart JM HARRISON (steux)</span><button type="button" class="ilink" id="infoLink">Info</button></footer>',1)
    s=s.replace('</body>',js+'</body>',1)
s=re.sub(r'(<meta name="app-version" content=")[^"]*',r'\g<1>2026-11-01zzb',s,count=1)
open('index.html','w',encoding='utf8').write(s)
