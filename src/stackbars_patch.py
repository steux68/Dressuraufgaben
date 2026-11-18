# 18.11.2026: PASSAGE wie DOCH!: sechs Balken in voller Breite (je eine Zeile, 25 px, Grossbuchstaben), Text buendig mit dem Seitentext,
# alle Abschnitte hellgrau mit weisser Luecke, Einrasten am Balken, gepunktete Linie unter jedem Balken, Start auf der Titelseite.
# Idempotent. Mit --preview wird stack.html geschrieben (index.html bleibt). Zurueck: git revert dieses Commit.
import re, sys
s = open('index.html', encoding='utf-8').read()
if 'id="stack-css"' in s:
    print('schon vorhanden'); sys.exit(0)
H = 25; HB = H - 1
def rep(a, b, n=1):
    global s
    assert s.count(a) == n, (a, s.count(a)); s = s.replace(a, b)
rep("const HB=22,ROWS=Math.ceil(SECS.length/2),", "const HB=%d,ROWS=SECS.length," % HB)
rep("const r=i>>1,b=document.createElement('div');b.className='hb '", "const r=i,b=document.createElement('div');b.className='hb '")
rep("PAGES[i].style.scrollMarginTop=(r*HB+22)+'px'", "PAGES[i].style.scrollMarginTop=(r*HB+%d)+'px'" % HB)
rep("PAGES[i].offsetTop-((i>>1)*HB+22)", "PAGES[i].offsetTop-(i*HB+%d)" % HB)
css = '''<style id="stack-css">
/* Balken: volle Breite, 25 px, Grossbuchstaben, Text buendig mit dem Seitentext */
.hb{--hv:linear-gradient(transparent,transparent)!important;height:%dpx!important;font-size:13px!important;padding:0!important}
.hb b{text-transform:uppercase;letter-spacing:1.6px;font-size:12.5px}
.hb small{font-size:9.5px!important;margin-left:6px!important;letter-spacing:.5px}
.hb.hl,.hb.hr{margin:%dpx 0 -1px 0!important}
.hb.first{margin-top:14px!important}
.hb::after{content:"";position:absolute;left:0;right:0;bottom:0;height:1px;pointer-events:none;background:repeating-linear-gradient(to right,#b8b8b8 0 1px,transparent 1px 3px)}
.hb.first::before{content:"";position:absolute;left:0;right:0;top:0;height:1px;pointer-events:none;background:repeating-linear-gradient(to right,#b8b8b8 0 1px,transparent 1px 3px)}
/* Abschnitte hellgrau, dazwischen eine weisse Luecke */
#p-a,#p-w,#p-g,#p-z,#p-m,#p-x{background:#f4f4f2!important}
#p-a,#p-w,#p-g,#p-z,#p-m{margin-bottom:12px!important}
/* Einrasten am Balken, Start auf der Titelseite */
.hscroll{scroll-snap-type:y proximity!important}
#p-title,#p-a,#p-w,#p-g,#p-z,#p-m,#p-x{scroll-snap-align:start}
</style>
</head>''' % (H, HB)
rep('</head>', css)
if '--preview' in sys.argv:
    s = re.sub(r'<title>[^<]*</title>', '<title>PASSAGE TEST volle Balken</title>', s, count=1)
    out = 'stack.html'
else:
    s = re.sub(r'(<meta name="app-version" content=")([^"]*)(")', lambda m: m.group(1) + '2026-11-18b' + m.group(3), s, count=1)
    out = 'index.html'
open(out, 'w', encoding='utf-8').write(s)
print('ok', out)
