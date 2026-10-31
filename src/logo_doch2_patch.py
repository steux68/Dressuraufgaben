# DOCH!-Kopflogo, Fassung 2 (kleiner): "Deutsche" in einer Zeile mit weissem D im "!", "Grammatik" darunter, beginnend unter dem "u".
import re
P="deutsch/index.html"
s=open(P,encoding="utf-8").read()
svg=('<h1 class="logo" role="img" aria-label="DOCH! Deutsche Grammatik">'
'<svg viewBox="0 0 276 62" aria-hidden="true">'
'<text class="lb" x="0" y="53" font-size="54">DOCH</text>'
'<g transform="translate(8 0)"><path class="lx" d="M129 2h21.5a3.2 3.2 0 0 1 3.2 3.7l-2.7 29a3.2 3.2 0 0 1-3.2 2.9h-9a3.2 3.2 0 0 1-3.2-2.9l-2.7-29A3.2 3.2 0 0 1 129 2z"/>'
'<circle class="lx" cx="139.7" cy="48" r="8.8"/>'
'<text class="ld" x="139.7" y="24" font-size="21" text-anchor="middle">D</text>'
'<text class="ls" x="157" y="24" font-size="21">eutsche</text>'
'<text class="ls" x="@GX@" y="47" font-size="21">Grammatik</text></g>'
'</svg></h1>')
GX=165.3   # x des "u" in "Deutsche", per Messung (getStartPositionOfChar)
svg=svg.replace('@GX@',('%.1f'%GX))
s=re.sub(r'<h1 class="logo".*?</h1>(?=<button class="markb on")',lambda m:svg,s,count=1,flags=re.S)
css=('<style id="logo-doch">'
'.home .brand{align-items:center}'
'.home h1.logo{display:flex;align-items:center;justify-content:center;flex:1;min-width:0;line-height:1;cursor:pointer;margin:0}'
'.home h1.logo svg{display:block;width:100%;max-width:220px;height:auto;overflow:visible}'
'.home .mark{width:calc(12vw - 1px);max-width:50px;height:auto;aspect-ratio:306/106}.home .markb{padding:0;margin:0;flex:none}'
'.home h1.logo .lb{font-family:DdBar,Carlito,sans-serif;font-weight:600;fill:var(--red);stroke:var(--red);stroke-width:2.6;stroke-linejoin:round;letter-spacing:.8px}'
'.home h1.logo .lx{fill:var(--red)}'
'.home h1.logo .ld{font-family:DdCor,Georgia,serif;font-weight:500;fill:#fff;stroke:#fff;stroke-width:.6}'
'.home h1.logo .ls{font-family:DdCor,Georgia,serif;font-weight:500;fill:var(--red);stroke:var(--red);stroke-width:.35}'
'</style>')
s=re.sub(r'<style id="logo-doch">.*?</style>',lambda m:css,s,count=1,flags=re.S)
open(P,"w",encoding="utf-8").write(s)
