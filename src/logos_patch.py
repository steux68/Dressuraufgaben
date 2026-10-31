#!/usr/bin/env python3
"""OEPS- und Steinbach-Logo aus der Kopfzeile in die Links-Seite (erste und zweite Karte),
Links kompakter, neue Icons (P a-x) mit Cache-Marke.
Aufruf: python3 src/logos_patch.py <version> index.html   (Icons vorher: python3 -I src/mk_icon.py)
Bricht ab, wenn schon angewendet."""
import sys, re, json

ver, path = sys.argv[1], sys.argv[2]
s = open(path, encoding='utf8').read()
if 'id="logos-js"' in s:
    sys.exit('schon angewendet')


def rep(old, new):
    global s
    assert s.count(old) == 1, f'{s.count(old)}x: {old[:60]}'
    s = s.replace(old, new)


CSS = '''
/* ---- Kopfzeile ohne Logos; Logos stehen auf der Links-Seite ---- */
#lockup,#toprow{display:none!important}
.lkw.logo{padding:0 8px}
.lkw.logo svg{height:44px;width:auto;max-width:100%;display:block}
/* ---- Links kompakter ---- */
.lkhead{padding:8px 10px 9px;margin-top:4px}
.lkhead h3{margin:0 0 3px;font-size:.74rem}
.lkhead p{font-size:.88rem;line-height:1.3}
.lk{padding:8px 10px 10px;gap:1px}
.lkw{height:56px;margin-bottom:5px}
.lkw b{font-size:1.08rem}
.lkw small{font-size:.62rem;margin-top:2px}
.lkn{font-size:.98rem;line-height:1.15}
.lkd{font-size:.8rem;line-height:1.25}
'''
JS = '''
<script id="logos-js">
(function(){
 const L=document.getElementById('lockup');if(!L)return;
 const sv=L.querySelectorAll('.cell svg');
 const put=(sel,svg)=>{const el=document.querySelector(sel);if(el&&svg){el.textContent='';el.appendChild(svg);el.classList.add('logo');}};
 put('#xyz a[href*="oeps.at"] .lkw',sv[0]);
 put('#xyz a[href*="reitstall-steinbach"] .lkw',sv[1]);
})();
</script>
'''
i = s.rfind('</style>')
assert i > 0
s = s[:i] + CSS + s[i:]
rep('</body></html>', JS + '</body></html>')
rep('<link rel="apple-touch-icon" href="apple-touch-icon.png">', '<link rel="apple-touch-icon" href="apple-touch-icon.png?v=2">')
rep('<link rel="icon" href="icon-192.png">', '<link rel="icon" type="image/png" href="icon-192.png?v=2">')
s = re.sub(r'(<meta name="app-version" content=")[^"]*"', r'\g<1>' + ver + '"', s, count=1)
open(path, 'w', encoding='utf8').write(s)

m = json.load(open('manifest.webmanifest', encoding='utf8'))
m['icons'] = [
    {'src': 'icon-192.png?v=2', 'sizes': '192x192', 'type': 'image/png', 'purpose': 'any'},
    {'src': 'icon-512.png?v=2', 'sizes': '512x512', 'type': 'image/png', 'purpose': 'any'},
    {'src': 'icon-512.png?v=2', 'sizes': '512x512', 'type': 'image/png', 'purpose': 'maskable'},
]
open('manifest.webmanifest', 'w', encoding='utf8').write(json.dumps(m, ensure_ascii=False, indent=1) + '\n')
print('ok')
