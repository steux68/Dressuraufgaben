#!/usr/bin/env python3
"""Geschichte: zwei Zeitleisten (wie Deutsch-App, seitlich wischbar): "Reitkunst und Dressur" oben, "Das Pferd" statt der Liste
"Kleine Geschichte des Pferdes".  Aufruf: python3 src/zeit_patch.py <version> index.html   (ersetzt eine frühere Fassung)"""
import sys, re, json
ver, path = sys.argv[1], sys.argv[2]
s = open(path, encoding='utf8').read()
s = re.sub(r'<script id="zeit-js">.*?</script>\n', '', s, flags=re.S)   # frühere Fassung entfernen
css = open('src/zeit.css', encoding='utf8').read()
if '/* ---- Zeitleiste (aus der Deutsch-App) ---- */' not in s:
    i = s.rfind('</style>'); assert i > 0
    s = s[:i] + '\n/* ---- Zeitleiste (aus der Deutsch-App) ---- */\n' + css + '\n#zasec,#zbsec{padding-top:0;margin-top:0}\n.tlw{margin-top:6px}\n' + s[i:]
tpl = open('src/zeit.tpl.js', encoding='utf8').read().rstrip()
assert tpl.endswith('});')
body = tpl[:-3]
ERA_A = [[-4000, -500, "Vorzeit", "#ececea", "#6b6b66"], [-500, 500, "Antike", "#e3efb4", "#6f8a1a"], [500, 1500, "Mittelalter", "#f5efcf", "#9a7d0a"], [1500, 1800, "Barock", "#f4dcd8", "#a3241c"], [1800, 2100, "Neuzeit", "#d3def0", "#1d4f9e"]]
ERA_B = [[-1000000000, -9500, "Urzeit", "#ececea", "#6b6b66"], [-9500, -500, "Vorzeit", "#e3efb4", "#6f8a1a"], [-500, 500, "Antike", "#f5efcf", "#9a7d0a"], [500, 1800, "Neuzeit", "#f4dcd8", "#a3241c"], [1800, 2100, "Heute", "#d3def0", "#1d4f9e"]]
def inst(pre, data, era, head, mode):
    return '(function(ZL,ERAS,HEAD,MODE,PRE){' + body.split('\n', 1)[1].replace('@@', pre) + '})(' + data + ',' + json.dumps(era, ensure_ascii=False) + ',' + json.dumps(head, ensure_ascii=False) + ',"' + mode + '","' + pre + '");'
data = open('src/zeit_data.js', encoding='utf8').read()
js = data + '\n' + inst('za', 'ZL_A', ERA_A, 'Zeitleiste: Reitkunst und Dressur', 'A') + '\n' + inst('zb', 'ZL_B', ERA_B, 'Zeitleiste: Das Pferd', 'B')
assert s.count('</body></html>') == 1
s = s.replace('</body></html>', '<script id="zeit-js">\n' + js + '\n</script>\n</body></html>')
s = re.sub(r'(<meta name="app-version" content=")[^"]*"', r'\g<1>' + ver + '"', s, count=1)
open(path, 'w', encoding='utf8').write(s); print('ok')
