#!/usr/bin/env python3
"""Kopf-Logo Pferde-App: Wort PASSAGE als punktierte Umrissschrift (A2: Strich 1.0, Abstand 2.0), a-x rot (idempotent)."""
import re
s=open('index.html',encoding='utf8').read()
if 'id="brand-dots"' not in s:
    css='<style id="brand-dots">#brand .pw{fill:#fff!important;stroke:#e30613!important;stroke-width:1px!important;stroke-linecap:round;stroke-dasharray:0.01 2!important}#brand .pax{fill:#e30613!important;stroke:#e30613!important}</style>'
    s=s.replace('</head>',css+'</head>',1)
s=re.sub(r'(<meta name="app-version" content=")[^"]*',r'\g<1>2026-11-01zzd',s,count=1)
open('index.html','w',encoding='utf8').write(s)
