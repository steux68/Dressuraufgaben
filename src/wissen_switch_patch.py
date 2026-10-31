#!/usr/bin/env python3
"""Schalter in der Pferde-App: work/wonder -> Wissen/Wunder (idempotent)."""
import re
s=open('index.html',encoding='utf8').read()
s=s.replace('<span class="wk" id="mlL">work</span>','<span class="wk" id="mlL">Wissen</span>').replace('<span class="wo" id="mlR">wonder</span>','<span class="wo" id="mlR">Wunder</span>')
s=s.replace('aria-label="Zwischen Work und Wonder (Galerie) wechseln"','aria-label="Zwischen Wissen und Wunder (Galerie) wechseln"')
s=re.sub(r'(<meta name="app-version" content=")[^"]*',r'\g<1>2026-11-01zza',s,count=1)
open('index.html','w',encoding='utf8').write(s)
