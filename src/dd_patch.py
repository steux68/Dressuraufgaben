#!/usr/bin/env python3
"""Kopfzeile, Schalter, Seitenlinien und Randmarken 1:1 aus dem Code von dasein-design (phone/index.html) übernommen;
Dock-Balken pulsieren auf der Titelseite als ganze Fläche in blassen Farben.  Aufruf: python3 src/dd_patch.py <version> index.html"""
import sys, re
ver, path = sys.argv[1], sys.argv[2]
s = open(path, encoding='utf8').read()
if 'id="dd-js"' in s: sys.exit('schon angewendet')
def rep(old, new, cnt=1):
    global s
    assert s.count(old) == cnt, f'{s.count(old)}x: {old[:70]}'
    s = s.replace(old, new)
# Markup: Schalter wie dasein-design
s, n = re.subn(r'<div class="mode" id="mode">.*?</div>', '<button type="button" class="wsw" id="wsw" aria-pressed="false" aria-label="Zwischen Work und Wonder (Galerie) wechseln"><span class="wk" id="mlL">work</span><i class="tg"><b></b></i><span class="wo" id="mlR">wonder</span></button>', s, count=1, flags=re.S)
assert n == 1
# Skript des Schalters
rep("$('msw').setAttribute('aria-checked',on?'true':'false');$('mlL').classList.toggle('on',!on);$('mlR').classList.toggle('on',on);}", "$('wsw').setAttribute('aria-pressed',on?'true':'false');}")
rep("$('msw').onclick=()=>{if(view==='gal')$('backBtn').click();else window.openGal();};", "$('wsw').onclick=()=>{if(view==='gal')$('backBtn').click();else window.openGal();};")
rep(" $('mlL').onclick=()=>{if(view==='gal')$('backBtn').click();};\n $('mlR').onclick=()=>{if(view!=='gal')window.openGal();};\n", "")
# alte Randmarken der Titelseite entfernen
s, n = re.subn(r'body\.introOn::before\{content:"";[^\n]*\}\n', '', s, count=1); assert n == 1
# Dock-Linien (Unterstrich) ersetzen: ganze Balken pulsieren, jeder in anderer blasser Farbe
s, n = re.subn(r'@keyframes pxl\{.*?\}\}\nbody\.introOn \.hb::after\{[^\n]*\}\n(body\.introOn \.hb:nth-of-type[^\n]*\n)+@media \(prefers-reduced-motion:reduce\)\{body\.introOn \.hb::after\{[^\n]*\}\}\n', '', s, count=1, flags=re.S); assert n == 1
CSS = '''
/* ---- 1:1 aus dasein-design (phone/index.html): Kopfzeile, Schalter, Seitenlinien, Randmarken ---- */
:root{--head:56px;--red:#e30613}
.app{background:none!important}
.titlebar{border-top:0!important;border-bottom:1px dashed var(--line)!important;padding:8px 0!important;margin-top:0!important}
.titlebar .wsw{display:none}
body.bv .titlebar .wsw{display:flex}
#brand{height:34px;gap:calc(2.139vw - .62px)}
#brand .bmark{width:calc(11.76vw - 3.42px);height:calc(8.02vw - 2.33px)}
#brand .bw{font-size:calc(7.219vw - 2.09px);line-height:1;letter-spacing:-.01em;font-weight:400}
.wsw{align-items:center;gap:5px;margin-left:auto;margin-right:6px;border:0;background:none;padding:4px 0;font:inherit;font-size:12px;letter-spacing:.04em;color:#666;cursor:pointer;-webkit-tap-highlight-color:transparent;min-height:0}
.wsw .tg{position:relative;width:28px;height:15px;border-radius:8px;border:1px solid #3a3c37;background:#fff;transition:background .25s;display:block}
.wsw .tg b{position:absolute;left:2px;top:2px;width:9px;height:9px;border-radius:50%;background:#cdff3e;box-shadow:0 0 0 1px #3a3c37;transition:transform .25s}
.wsw .tg b::after{content:"";position:absolute;inset:-1px;border-radius:50%;border:1px solid var(--red);opacity:0;animation:pdr 3.2s ease-out infinite}
.wsw[aria-pressed=true] .tg b::after{animation:none}
.wsw[aria-pressed=true] .tg{background:#eaffae} .wsw[aria-pressed=true] .tg b{transform:translateX(13px);background:var(--red)}
.wsw .wk{color:#000;font-weight:700} .wsw[aria-pressed=true] .wk{color:#666;font-weight:400} .wsw[aria-pressed=true] .wo{color:var(--red);font-weight:700}
@keyframes pdr{0%{transform:scale(1);opacity:.8}100%{transform:scale(4.2);opacity:0}}
.rule{position:fixed;top:0;bottom:0;width:1px;z-index:45;pointer-events:none;background:repeating-linear-gradient(to bottom,var(--line) 0 4px,transparent 4px 7px)}
.rule.l{left:7px} .rule.r{right:7px} .rule.m{left:calc(50% - .5px)}
.tk{position:fixed;left:8px;right:8px;height:11px;z-index:45;pointer-events:none;--t:repeating-linear-gradient(to right,#b8b8b8 0 4px,transparent 4px 6px);
 background:var(--t) left top/10px 1px no-repeat,var(--t) left bottom/10px 1px no-repeat,var(--t) right top/10px 1px no-repeat,var(--t) right bottom/10px 1px no-repeat}
.tk.t{top:calc(var(--head) + 10px)} .tk.b{bottom:calc(env(safe-area-inset-bottom,0px) + 9px)}
.tk.m{top:calc(50% + var(--head) / 2 - env(safe-area-inset-bottom,0px) / 2 - 5px)}
/* Dock-Balken pulsieren auf der Titelseite als ganze Fläche, jeder in einer anderen, extrem blassen Farbe */
@keyframes hbp{0%,100%{background-color:#fff}50%{background-color:var(--pc)}}
body.introOn .hb{animation:hbp 3.4s ease-in-out infinite}
body.introOn .hb[data-i="0"]{--pc:#fbe0e3} body.introOn .hb[data-i="1"]{--pc:#e6f4c8;animation-delay:-.7s}
body.introOn .hb[data-i="2"]{--pc:#dfe9fb;animation-delay:-1.4s} body.introOn .hb[data-i="3"]{--pc:#fdf0c2;animation-delay:-2.1s}
body.introOn .hb[data-i="4"]{--pc:#ece2f8;animation-delay:-2.8s}
@media (prefers-reduced-motion:reduce){body.introOn .hb{animation:none}.wsw .tg b::after{animation:none}}
'''
i = s.rfind('</style>'); s = s[:i] + CSS + s[i:]
JS = '''
<i class="rule l" aria-hidden="true"></i><i class="rule m" aria-hidden="true"></i><i class="rule r" aria-hidden="true"></i><i class="tk t" aria-hidden="true"></i><i class="tk m" aria-hidden="true"></i><i class="tk b" aria-hidden="true"></i>
<script id="dd-js">
(function(){const T=document.querySelector('.titlebar');if(!T)return;const set=()=>document.documentElement.style.setProperty('--head',Math.round(T.getBoundingClientRect().bottom)+'px');
 set();addEventListener('resize',set);addEventListener('load',set);setTimeout(set,400);if(window.ResizeObserver)new ResizeObserver(set).observe(T);})();
</script>
'''
rep('</body></html>', JS + '</body></html>')
s = re.sub(r'(<meta name="app-version" content=")[^"]*"', r'\g<1>' + ver + '"', s, count=1)
open(path, 'w', encoding='utf8').write(s); print('ok')
