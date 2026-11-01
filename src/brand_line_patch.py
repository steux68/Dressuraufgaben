#!/usr/bin/env python3
"""Kopf-Logo Pferde-App: PASSAGE als duenne durchgehende rote Umrisslinie (Strich .6), a-x rot (idempotent).
Ersetzt die punktierte Fassung aus brand_dots_patch.py."""
import re
s=open('index.html',encoding='utf8').read()
css='<style id="brand-dots">#brand .pw{fill:#fff!important;stroke:#e30613!important;stroke-width:.6px!important;stroke-dasharray:none!important}#brand .pax{fill:#e30613!important;stroke:#e30613!important}</style>'
s=re.sub(r'<style id="brand-dots">.*?</style>',css,s,count=1,flags=re.S)
s=re.sub(r'(<meta name="app-version" content=")[^"]*',r'\g<1>2026-11-01zze',s,count=1)
open('index.html','w',encoding='utf8').write(s)
