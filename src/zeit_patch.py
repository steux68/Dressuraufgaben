#!/usr/bin/env python3
"""Geschichte: Zeitleiste "Pferd und Reitkunst" (wie Deutsch-App, seitlich wischbar) am Anfang von "Geschichte und Zitate".
Aufruf: python3 src/zeit_patch.py <version> index.html"""
import sys, re
ver, path = sys.argv[1], sys.argv[2]
s = open(path, encoding='utf8').read()
if 'id="zeit-js"' in s: sys.exit('schon angewendet')
css = open('src/zeit.css', encoding='utf8').read()
js = open('src/zeit_data.js', encoding='utf8').read() + '\n' + open('src/zeit.js', encoding='utf8').read()
i = s.rfind('</style>'); assert i > 0
s = s[:i] + '\n/* ---- Zeitleiste (aus der Deutsch-App) ---- */\n' + css + '\n#zlsec{padding-top:0;margin-top:0}\n.tlw{margin-top:6px}\n' + s[i:]
assert s.count('</body></html>') == 1
s = s.replace('</body></html>', '<script id="zeit-js">\n' + js + '\n</script>\n</body></html>')
s = re.sub(r'(<meta name="app-version" content=")[^"]*"', r'\g<1>' + ver + '"', s, count=1)
open(path, 'w', encoding='utf8').write(s); print('ok')
