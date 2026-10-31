# Neues DOCH!-Kopflogo: dickes DOCH + dickes "!", weisses D im Ausrufezeichen, Rest rot. Idempotent.
import re
P="deutsch/index.html"
s=open(P,encoding="utf-8").read()
svg=('<h1 class="logo" role="img" aria-label="DOCH! Deutsche Grammatik">'
'<svg viewBox="0 0 330 74" aria-hidden="true">'
'<text class="lb" x="0" y="66" font-size="68">DOCH</text>'
'<path class="lx" d="M176 2h26a4 4 0 0 1 4 4.6l-3.4 36a4 4 0 0 1-4 3.6h-11.2a4 4 0 0 1-4-3.6L172 6.6A4 4 0 0 1 176 2z"/>'
'<circle class="lx" cx="189" cy="60" r="11"/>'
'<text class="ld" x="189" y="29" font-size="26" text-anchor="middle">D</text>'
'<text class="ls" x="211" y="29" font-size="26">eutsche Grammatik</text>'
'</svg></h1>')
s=re.sub(r'<h1 class="logo">.*?</h1>(?=<button class="markb on")',svg,s,count=1,flags=re.S) if '<h1 class="logo">' in s else s
css=('<style id="logo-doch">'
'.home h1.logo{display:flex;align-items:center;justify-content:center;flex:1;min-width:0;line-height:1;cursor:pointer;margin:0}'
'.home h1.logo svg{display:block;width:100%;max-width:330px;height:auto;overflow:visible}'
'.home h1.logo .lb{font-family:DdBar,Carlito,sans-serif;font-weight:600;fill:var(--red);stroke:var(--red);stroke-width:3.2;stroke-linejoin:round;letter-spacing:1px}'
'.home h1.logo .lx{fill:var(--red)}'
'.home h1.logo .ld{font-family:DdCor,Georgia,serif;font-weight:500;fill:#fff;stroke:#fff;stroke-width:.7}'
'.home h1.logo .ls{font-family:DdCor,Georgia,serif;font-weight:500;fill:var(--red);stroke:var(--red);stroke-width:.4}'
'</style>')
if 'id="logo-doch"' not in s:
    s=s.replace('</head>',css+'</head>',1)
else:
    s=re.sub(r'<style id="logo-doch">.*?</style>',css,s,count=1,flags=re.S)
s=s.replace('content="2026-10-31m"','content="2026-10-31n"')
open(P,"w",encoding="utf-8").write(s)
