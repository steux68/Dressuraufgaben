# Hinweis "Punkt tippen / Bild tippen" als schlichte Textzeile unter dem Bild (ohne Band, ohne Kasten). Im Vollbild: weisse Schrift mit Schatten direkt auf dem Bild. Idempotent. 06.11.2026
import re, sys
s = open('index.html', encoding='utf-8').read()
if '/* hint-plain */' in s:
    print('schon angewendet'); sys.exit(0)

def rep(old, new):
    global s
    assert s.count(old) == 1, f'{s.count(old)}x: {old[:80]}'
    s = s.replace(old, new)

rep('<div id="aDots"></div></div></div></div>\'+', '<div id="aDots"></div></div></div></div><p class="aTip" id="aTip"></p>\'+')
rep("h.textContent=x;o.hidden=!(full||x);}", "h.textContent=x;o.hidden=!full;$('aTip').textContent=full?'':x;}")
CSS = '''
/* hint-plain */
.tlpop .tlbody p.aTip{margin:0;text-align:center;font-size:12px;line-height:18px;color:#999;letter-spacing:.02em}
.anapop .aOv{background:none;padding:8px 12px;color:#fff;text-shadow:0 1px 3px rgba(0,0,0,.95),0 0 8px rgba(0,0,0,.6)}
.anapop .aOv .aHint{color:#fff}
.anapop .aOv button{border:0;padding:2px 0;color:#fff;text-shadow:inherit}
'''
i = s.index('</style>', s.index('/* hdr-follow */'))
s = s[:i] + CSS + s[i:]
if '--noversion' not in sys.argv:
    s = re.sub(r'(<meta name="app-version" content=")([^"]*)(")', lambda m: m.group(1) + '2026-11-06zzz82' + m.group(3), s, count=1)
open('index.html', 'w', encoding='utf-8').write(s)
print('ok')
