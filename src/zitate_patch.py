#!/usr/bin/env python3
"""Zitate im Layout der Deutsch-App (Filter-Knöpfe, Bild, gepunktete Linien, grau/weiß im Wechsel).  python3 src/zitate_patch.py <version> index.html"""
import sys, re
ver, path = sys.argv[1], sys.argv[2]
s = open(path, encoding='utf8').read()
if 'id="zitate-js"' in s: sys.exit('schon angewendet')
i = s.rfind('</style>'); assert i > 0
s = s[:i] + '\n' + open('src/zitate.css', encoding='utf8').read() + s[i:]
assert s.count('</body></html>') == 1
s = s.replace('</body></html>', '<script id="zitate-js">\n' + open('src/zitate.js', encoding='utf8').read() + '\n</script>\n</body></html>')
s = re.sub(r'(<meta name="app-version" content=")[^"]*"', r'\g<1>' + ver + '"', s, count=1)
open(path, 'w', encoding='utf8').write(s); print('ok')
