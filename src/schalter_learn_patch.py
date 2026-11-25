# PASSAGE 25.11.2026: Schalter im Kopf "Wissen | Wunder" -> "learn | wonder" (wie in DOCH!; dasein-design behaelt "work | wonder"). Idempotent.
import re, sys
s = open('index.html', encoding='utf-8').read()
a = '<span class="wk" id="mlL">Wissen</span>'
if a not in s: sys.exit('schon angewendet')
s = s.replace(a, '<span class="wk" id="mlL">learn</span>', 1)
b = '<span class="wo" id="mlR">Wunder</span>'
assert s.count(b) == 1
s = s.replace(b, '<span class="wo" id="mlR">wonder</span>', 1)
c = 'aria-label="Zwischen Wissen und Wunder (Galerie) wechseln"'
assert s.count(c) == 1
s = s.replace(c, 'aria-label="Zwischen learn und wonder (Galerie) wechseln"', 1)
if '--noversion' not in sys.argv:
    s = re.sub(r'(<meta name="app-version" content=")([^"]*)(")', lambda m: m.group(1) + '2026-11-25i' + m.group(3), s, count=1)
open('index.html', 'w', encoding='utf-8').write(s)
print('ok')
