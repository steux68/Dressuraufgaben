# Anatomie-Popup aufgeraeumt: Lernen/Quiz/Namen/Flaggen ganz oben, darunter Titel+Zaehler mit Kreuz oben rechts ueber dem Bild,
# Bild und Text bis fast an die aeusseren Linien, W/E-Kreise auf dem Foto auf 80 %. Idempotent. 06.11.2026
import re, sys
s = open('index.html', encoding='utf-8').read()
if '/* ana-unify */' in s:
    print('schon angewendet'); sys.exit(0)

a = s.index('<div class="anaBar">')
b = s.index("'+\n '<div class=\"anaStage\"", a)
BAR = s[a:b]
assert BAR.count("'") == 0
s = s[:a] + s[b:]
old = '<div class="tlcard"><div class="tltop"><span class="tlk" id="aTk">'
assert s.count(old) == 1
s = s.replace(old, '<div class="tlcard">' + BAR + '<div class="tltop"><span class="tlk" id="aTk">')

CSS = '''
/* ana-unify */
.anapop .tlcard>.anaBar{flex:none;margin:0 4px;border-top:0}
.anapop .tltop{padding:4px 4px 3px;min-height:0}
.anapop .tlx{padding:4px;margin:-4px}.anapop .tlx svg{width:22px;height:22px}
.anapop .tlcard .tlbody{padding-left:4px;padding-right:4px}
.anapop .tlar{width:34px;height:34px;margin-top:-17px}
.anapop .tlar svg{width:22px;height:22px}
.anapop .anaStage{height:calc(var(--ph) * .5)}
'''
i = s.index('</style>', s.index('/* hint-plain */'))
s = s[:i] + CSS + s[i:]
if '--noversion' not in sys.argv:
    s = re.sub(r'(<meta name="app-version" content=")([^"]*)(")', lambda m: m.group(1) + '2026-11-06zzz83' + m.group(3), s, count=1)
open('index.html', 'w', encoding='utf-8').write(s)
print('ok')
