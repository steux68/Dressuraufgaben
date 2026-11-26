# PASSAGE 26.11.2026: Lernen-Ansicht: Selbsttest / Zeichnen / Ansage als drei Schalter mit Kreis (gepunktet = aus, Neon = an), "Ganze Aufgabe" als eigener breiter Knopf mit Pfeil.
# Die Original-Knoepfe (#qz, #dz, #cl, #al) bleiben bestehen (Text ": aus/an" wird per Skript in data-on uebersetzt, per CSS nur das Wort gezeigt). Idempotent.
import re, sys
s = open('index.html', encoding='utf-8').read()
if 'id="lsw-css"' in s: sys.exit('schon angewendet')
OFF = "url(\"data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='14' height='14'%3E%3Ccircle cx='7' cy='7' r='6.5' fill='%23f4f4f2' stroke='%231a1a1a' stroke-dasharray='1 2'/%3E%3C/svg%3E\")"
ON = "url(\"data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='14' height='14'%3E%3Ccircle cx='7' cy='7' r='6.5' fill='%23cdff3e' stroke='%231a1a1a'/%3E%3C/svg%3E\")"
css = ('<style id="lsw-css">.btns:has(#qz){grid-template-columns:repeat(3,minmax(0,1fr))}'
       '.btns #qz[data-l],.btns #dz[data-l],.btns #cl[data-l]{display:flex!important;align-items:center;justify-content:flex-start!important;gap:0!important;font-size:0!important;height:44px;padding:0 0 0 30px!important;border:0;border-radius:0;'
       'background-color:#ececea!important;background-repeat:no-repeat!important;background-position:10px center!important;background-size:14px 14px!important;background-image:@OFF@;color:#1a1a1a;font-weight:400!important}'
       '.btns #qz svg,.btns #dz svg,.btns #cl svg{display:none!important}'
       '.btns #qz::before,.btns #dz::before,.btns #cl::before{content:attr(data-l);font-size:14px;line-height:1;flex:none;width:auto;height:auto;opacity:1;background:none;-webkit-mask:none;mask:none}'
       '.btns #qz[data-on="1"],.btns #dz[data-on="1"],.btns #cl[data-on="1"]{background-image:@ON@;background-color:#ececea!important;font-weight:400!important}'
       '.btns #qz[data-on="1"]::before,.btns #dz[data-on="1"]::before,.btns #cl[data-on="1"]::before{font-weight:700}'
       '.btns #al{grid-column:1/4;display:flex!important;align-items:center;justify-content:space-between;padding:0 14px!important;height:44px;font-weight:700!important}'
       '.btns #al::after{content:"\\2192";font-weight:400;position:static;transform:none;height:auto;left:auto;right:auto;top:auto}'
       '@media(max-width:340px){.btns #qz::before,.btns #dz::before,.btns #cl::before{font-size:13px}.btns #qz,.btns #dz,.btns #cl{padding-left:28px!important}}'
       '</style>').replace('@OFF@', OFF).replace('@ON@', ON)
js = ('<script id="lsw-js">(function(){var L={qz:"Selbsttest",dz:"Zeichnen",cl:"Ansage"};function upd(b){var t=(b.textContent||"").trim();b.setAttribute("data-l",L[b.id]);'
      'var on=!/:\\s*aus\\s*$/i.test(t);b.setAttribute("data-on",on?"1":"0");}'
      'Object.keys(L).forEach(function(i){var b=document.getElementById(i);if(!b)return;upd(b);new MutationObserver(function(){upd(b)}).observe(b,{childList:true,characterData:true,subtree:true,attributes:true,attributeFilter:["aria-pressed"]});});})();</script>')
s = s.replace('</head>', css + '</head>', 1)
s = s.rstrip('\n') + '\n' + js + '\n'
if '--noversion' not in sys.argv:
    s = re.sub(r'(<meta name="app-version" content=")([^"]*)(")', lambda m: m.group(1) + '2026-11-26m' + m.group(3), s, count=1)
open('index.html', 'w', encoding='utf-8').write(s); print('ok')
