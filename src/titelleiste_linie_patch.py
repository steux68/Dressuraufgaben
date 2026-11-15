#!/usr/bin/env python3
"""Titelleiste behält ihre untere gestrichelte Linie auch bei gestapelten Menüleisten (Steuart, 15 Nov 2026):
die obere gepunktete Linie der oben haftenden Leisten entfällt stattdessen; Linie und Rahmenmarken (.tk) bekommen
dasselbe Strichmuster und dieselbe Farbe, damit sie nicht versetzt wirken. Aufruf im Hauptordner: python3 src/titelleiste_linie_patch.py"""
import re, sys
p = "index.html"
s = open(p, encoding="utf-8").read()
if "/* titelleiste-linie */" in s: sys.exit("already patched")
for old in ("body.tstk:has(#tip[hidden]) .titlebar{background-image:none!important}\n",
            "body.tstk:has(#tip[hidden]) .tk.t{visibility:hidden}\n"):
    if old not in s: sys.exit("Anker fehlt: " + old[:40])
    s = s.replace(old, "")
CSS = """/* titelleiste-linie */
.hb.stt.hl{background:var(--bl) left bottom/100% 1px no-repeat,var(--hv) right top/1px 100% no-repeat,#fff}
.hb.stt.hr{background:var(--bl) left bottom/100% 1px no-repeat,var(--hv) left top/1px 100% no-repeat,#fff}
.hbody.inpg .hb.stt{background-color:#f2f2f2}.hb.stt.on,.hb.stt.hit{background-color:#cdff3e!important}
.tk{--t:repeating-linear-gradient(to right,#b8b8b8 0 4px,transparent 4px 7px)}
.titlebar{background-image:repeating-linear-gradient(to right,#b8b8b8 0 4px,transparent 4px 7px)!important}
"""
a = "/* 15 Nov: bars stacked right under the header"
i = s.index(a)
s = s[:i] + CSS + s[i:]
old = "if(r.top<=R.top+t+.5)tb=Math.max(tb,r.bottom);"
if old not in s: sys.exit("JS-Anker fehlt")
s = s.replace(old, "const st=r.top<=R.top+t+.5;b.classList.toggle('stt',st);if(st)tb=Math.max(tb,r.bottom);")
m = re.search(r'name="app-version" content="(\d{4}-\d\d-\d\d)([a-z]?)"', s)
if m: s = s.replace(m.group(0), 'name="app-version" content="%s%s"' % (m.group(1), chr(ord(m.group(2) or "`") + 1)))
open(p, "w", encoding="utf-8").write(s); print("OK")
