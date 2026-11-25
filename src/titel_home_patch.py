# PASSAGE 25.11.2026: Ein Tipp auf die freie Flaeche der Titelleiste (nicht nur auf den kleinen Titeltext rechts)
# fuehrt in allen Unteransichten (R1-R6, Pferdewissen, Galerie ...) wie "Start" nach Hause. Auf der Startseite aendert sich nichts. Idempotent.
import re, sys
s = open('index.html', encoding='utf-8').read()
if 'id="titel-home-js"' in s: sys.exit('schon angewendet')
css = '<style id="titel-home-css">.titlebar:has(#backBtn:not([hidden])){cursor:pointer;-webkit-tap-highlight-color:transparent}</style>'
js = ('<script id="titel-home-js">(function(){var bar=document.querySelector(".titlebar"),back=document.getElementById("backBtn");'
      'if(!bar||!back)return;bar.addEventListener("click",function(e){if(e.target!==bar&&e.target.id!=="title")return;'
      'if(back.hidden)return;back.click();});})();</script>')
assert s.count('</head>') >= 1
s = s.replace('</head>', css + '</head>', 1)
s = s.rstrip('\n') + '\n' + js + '\n'
if '--noversion' not in sys.argv:
    s = re.sub(r'(<meta name="app-version" content=")([^"]*)(")', lambda m: m.group(1) + '2026-11-26f' + m.group(3), s, count=1)
open('index.html', 'w', encoding='utf-8').write(s)
print('ok')
