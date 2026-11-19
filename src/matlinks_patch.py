# 19.11.2026: Die Balken "Materialien" und "Links" werden ein Balken "Material & Links" (fuenf statt sechs Balken).
# Download-Material steht ohnehin bei den Dressuraufgaben; hier bleiben Aushang/OEPS-Blaetter und die Links.
# Idempotent. Zurueck: git revert dieses Commit.
import re, sys
s = open('index.html', encoding='utf-8').read()
if 'id="matlinks-css"' in s:
    print('schon vorhanden'); sys.exit(0)
def rep(a, b, n=1):
    global s
    assert s.count(a) == n, (a, s.count(a)); s = s.replace(a, b)
rep("['m','Materialien'],['x','Links']];", "['m','Material & Links']];")
rep("const PX=mk('p-x','hsec');PX.appendChild($('xyz'));", "PM.appendChild($('xyz'));")
rep("const PAGES=[PA,PW,PG,PZ,PM,PX];", "const PAGES=[PA,PW,PG,PZ,PM];")
rep("const IDX={mat:4,gesch:2,zit:3,xyz:5};", "const IDX={mat:4,gesch:2,zit:3,xyz:4};")
rep("window.openXyz=()=>toHome(5);", "window.openXyz=()=>toHome(4);")
rep("window.xyzRaw=()=>{_show('home');goSec(5);};", "window.xyzRaw=()=>{_show('home');goSec(4);};")
rep("'#xyz':5,'#links':5", "'#xyz':4,'#links':4", 2)
css = '''<style id="matlinks-css">
/* Material & Links: ein Abschnitt, letzter Abschnitt der Seite (kein Abstand darunter) */
#p-m{padding-bottom:40px!important;margin-bottom:0!important}
</style>
</head>'''
rep('</head>', css)
s = re.sub(r'(<meta name="app-version" content=")([^"]*)(")', lambda m: m.group(1) + '2026-11-19b' + m.group(3), s, count=1)
open('index.html', 'w', encoding='utf-8').write(s)
