#!/usr/bin/env python3
"""Anatomie-Galerie wie die Projekt-Kacheln in dasein-design: quadratisch, Beschriftung als durchsichtiges Band ueber dem Bild.
python3 src/anatomie_cap_patch.py <version> index.html (idempotent)"""
import sys, re
ver, path = sys.argv[1], sys.argv[2]
s = open(path, encoding='utf8').read()
if 'id="ana-cap-css"' in s:
    print('schon angewendet'); sys.exit(0)
CSS = '''<style id="ana-cap-css">
/* wie dasein-design .tile/.cap: alle Kacheln gleich gross (quadratisch), Band 70 % dunkelgrau, weisse Schrift */
.agc{align-self:stretch}
.agc .agi{aspect-ratio:1/1}
.agc .agb{background:rgba(68,68,68,.7);padding:4px 6px 5px;gap:0 6px}
.agc .agn{font-size:12px;line-height:1.15;color:#fff}
.agc .agk{font-size:12px;line-height:1.15;color:#fff;opacity:.85}
</style>'''
j = s.rindex('</style>') + len('</style>')
s = s[:j] + '\n' + CSS + s[j:]
m = re.search(r'(<meta name="app-version" content=")([^"]*)(")', s)
s = s[:m.start(2)] + ver + s[m.end(2):]
open(path, 'w', encoding='utf8').write(s)
print('ok', m.group(2), '->', ver)
