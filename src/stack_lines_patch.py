#!/usr/bin/env python3
"""Gestapelte Menüleisten: zwischen den Zeilen bleibt die gepunktete Linie (Steuart, 18 Nov 2026).
Die obere Linie der oben haftenden Leisten entfiel für ALLE Zeilen, die untere der Leiste darüber entfällt per .nb ->
dazwischen fehlte jede Linie. Jetzt entfällt sie nur noch in der ersten Zeile (unter der Titelleiste). Aufruf im Hauptordner: python3 src/stack_lines_patch.py"""
import re, sys
p = "index.html"
s = open(p, encoding="utf-8").read()
if "/* stack-lines */" in s: sys.exit("already patched")
old = "b.className='hb '+(i&1?'hr':'hl')+(i===0?' first':'');"
if s.count(old) != 1: sys.exit("JS-Anker fehlt")
s = s.replace(old, "b.className='hb '+(i&1?'hr':'hl')+(i===0?' first':'')+(r===0?' r0':'');")
CSS = """/* stack-lines */
.hb.stt.hl:not(.r0){background:repeating-linear-gradient(to right,#b8b8b8 0 1px,transparent 1px 3px) left top/100% 1px no-repeat,var(--bl) left bottom/100% 1px no-repeat,var(--hv) right top/1px 100% no-repeat,#fff}
.hb.stt.hr:not(.r0){background:repeating-linear-gradient(to right,#b8b8b8 0 1px,transparent 1px 3px) left top/100% 1px no-repeat,var(--bl) left bottom/100% 1px no-repeat,var(--hv) left top/1px 100% no-repeat,#fff}
.hbody.inpg .hb.stt:not(.r0){background-color:#f2f2f2}.hb.stt.on:not(.r0),.hb.stt.hit:not(.r0){background-color:#cdff3e!important}
"""
a = "/* 15 Nov: bars stacked right under the header"
i = s.index(a); s = s[:i] + CSS + s[i:]
m = re.search(r'name="app-version" content="(\d{4}-\d\d-\d\d)([a-z]?)"', s)
if m: s = s.replace(m.group(0), 'name="app-version" content="%s%s"' % (m.group(1), chr(ord(m.group(2) or "`") + 1)))
open(p, "w", encoding="utf-8").write(s); print("OK")
