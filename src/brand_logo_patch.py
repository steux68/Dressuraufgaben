# P a–x: Mittellinie (.rule.m) aus, Kopf-Logo als dichtes Wortzeichen: PASSAGE dick rot, "a–x" blau darunter rechtsbündig. Idempotent.
import re
P="index.html";s=open(P,encoding="utf-8").read()
svg=('<svg class="bmark" viewBox="0 0 200 52" aria-hidden="true">'
'<rect class="bx" x="0" y="1" width="42" height="42" fill="#e30613"/>'
'<text class="bp" x="5" y="33" font-size="34">P</text><text class="ba" x="14.5" y="37.6" font-size="14">a–x</text>'
'<text class="pw" x="49" y="35" font-size="39">PASSAGE</text>'
'<text class="pax" x="195.8" y="50" font-size="15.5" text-anchor="end">a–x</text></svg>')
s=re.sub(r'(<a class="brand" id="brand"[^>]*>).*?(</a>)',lambda m:m.group(1)+svg+m.group(2),s,count=1,flags=re.S)
css=('<style id="brand-logo">'
'.rule.m{display:none!important}'
'#brand{gap:0!important;height:auto!important}'
'#brand .bmark{width:min(calc(44vw - 2px),200px)!important;height:auto!important;display:block}'
'#brand .bp,#brand .ba{font-family:inherit;font-weight:700;fill:#fff}#brand .ba{letter-spacing:1.6px}'
'#brand .pw{font-family:inherit;font-weight:700;fill:#e30613;stroke:#e30613;stroke-width:1.6;stroke-linejoin:round;letter-spacing:.2px}'
'#brand .pax{font-family:inherit;font-weight:700;fill:#0057d8;stroke:#0057d8;stroke-width:.5;letter-spacing:.5px}'
'</style>')
s=re.sub(r'<style id="brand-logo">.*?</style>','',s,flags=re.S)
s=s.replace('</head>',css+'</head>',1)
s=re.sub(r'(<meta name="app-version" content=")[^"]*(")',lambda m:m.group(1)+'2026-11-01zw'+m.group(2),s,count=1)
open(P,"w",encoding="utf-8").write(s)
