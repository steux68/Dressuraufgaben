# PASSAGE 25.11.2026: (1) Google-Fonts-Link und "Source Sans 3" entfernen (alles laeuft in Carlito, kein Aufruf an fremden Server),
# (2) Viereck: aktive Knoepfe in Neon-Gelb #cdff3e statt #ffd400 (Marker-Punkte bleiben gold), (3) Buchstaben im Viereck 15 -> 16 px. Idempotent.
import re, sys
s = open('index.html', encoding='utf-8').read()
if 'id="schriftgelb-done"' in s: sys.exit('schon angewendet')
STACK = '"Carlito",Calibri,"Segoe UI",system-ui,sans-serif'
link = '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Source+Sans+3:wght@400;600;700&display=swap">'
assert s.count(link) == 1
s = s.replace(link + '\n', '', 1) if (link + '\n') in s else s.replace(link, '', 1)
s = s.replace('"Source Sans 3",system-ui,sans-serif', STACK)
s = s.replace("'Source Sans 3',system-ui,sans-serif", STACK.replace('"', "'"))
s = s.replace('font-family="Source Sans 3, system-ui, sans-serif" font-size="15" font-weight="600"', 'font-family="Carlito, Calibri, sans-serif" font-size="16" font-weight="600"')
s = s.replace('font-family="Source Sans 3, system-ui, sans-serif"', 'font-family="Carlito, Calibri, sans-serif"')
s = s.replace("font:700 11.5px/1.2 'Source Sans 3'", "font:700 12px/1.2 'Carlito'")
for a, b in [
    ('#thVi .viTabs button[aria-pressed="true"]{font-weight:700;color:#222;background:#ffd400!important}',
     '#thVi .viTabs button[aria-pressed="true"]{font-weight:700;color:#222;background:#cdff3e!important}'),
    ('#thVi .viChip[aria-pressed="true"]{background:#ffd400;font-weight:700}',
     '#thVi .viChip[aria-pressed="true"]{background:#cdff3e;font-weight:700}'),
    ('#thVi .viChip[aria-pressed="true"]{background:#ffd400!important}',
     '#thVi .viChip[aria-pressed="true"]{background:#cdff3e!important}'),
]:
    assert s.count(a) == 1, a[:40]
    s = s.replace(a, b, 1)
assert 'Source Sans' not in s, 'Rest von Source Sans'
s = s.replace('</head>', '<meta id="schriftgelb-done" name="schriftgelb" content="1"></head>', 1)
if '--noversion' not in sys.argv:
    s = re.sub(r'(<meta name="app-version" content=")([^"]*)(")', lambda m: m.group(1) + '2026-11-25g' + m.group(3), s, count=1)
open('index.html', 'w', encoding='utf-8').write(s)
print('ok')
