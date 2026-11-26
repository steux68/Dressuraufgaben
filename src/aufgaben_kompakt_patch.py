# PASSAGE 26.11.2026: Aufgabenliste von 12 auf 6 Zeilen. Die Zeile "Lernkarten Rx zum Ausdrucken" (.lkrow) wird ausgeblendet (bleibt im DOM, ihr Klick laedt das PDF),
# stattdessen sitzt das PDF-Symbol von dasein-design (img/pdf.svg, inline) als kleiner Knopf neben "Ueben". Beschreibung gekuerzt ("ca. 3½ Min. · 17 Lektionen"). Idempotent.
import re, sys
s = open('index.html', encoding='utf-8').read()
if 'id="akomp-css"' in s: sys.exit('schon angewendet')
SVG = ('<svg viewBox="58 0 342 428" width="21" height="26" aria-hidden="true" focusable="false"><g fill="none" stroke="#4d4d4d" stroke-width="22" stroke-linejoin="round">'
       '<path d="M140 11H298L381 94V356Q381 384 353 384H140Q112 384 112 356V39Q112 11 140 11Z"/><path d="M298 11V70Q298 94 322 94H381"/></g>'
       '<rect x="68" y="80" width="202" height="84" fill="#e2401c"/><text x="169" y="148" fill="#fff" font-family="inherit" font-weight="700" font-size="74" text-anchor="middle" letter-spacing="2">PDF</text>'
       '<path d="M251 236H325V331H358L288 422L218 331H251Z" fill="#e2401c"/></svg>')
css = ('<style id="akomp-css">#tiles>.tile.lkrow{display:none!important}#tiles>.tile.hasl::after{display:none!important}#tiles>.tile.hasl{padding:8px 8px!important}'
       '#tiles .tgrp{display:flex;align-items:center;gap:6px}'
       '#tiles .pdfb{display:inline-flex;align-items:center;justify-content:center;min-width:44px;height:32px;background:#ececea;cursor:pointer;-webkit-tap-highlight-color:transparent}'
       '#tiles .pdfb:active{background:#cdff3e}#tiles .pdfb.busy{opacity:.45}</style>')
js = ('<script id="akomp-js">(function(){var T=document.getElementById("tiles");if(!T)return;var SV=' + repr(SVG).replace('\\', '\\\\') + ';'
      'function fix(){[].slice.call(T.querySelectorAll(":scope>.tile.hasl")).forEach(function(t){if(t.getAttribute("data-ak"))return;var l=t.nextElementSibling;if(!l||!l.classList.contains("lkrow"))return;t.setAttribute("data-ak","1");'
      'var d=t.querySelector(".ds");if(d){var x=d.textContent,i=x.indexOf("ca. ");if(i>0)d.textContent=x.slice(i);}'
      'var st=t.querySelector(".st");if(!st)return;var g=document.createElement("span");g.className="tgrp";st.parentNode.insertBefore(g,st);g.appendChild(st);'
      'var p=document.createElement("span");p.className="pdfb";p.setAttribute("role","button");p.setAttribute("tabindex","0");p.setAttribute("aria-label",l.getAttribute("aria-label")||"Lernkarten als PDF laden");p.innerHTML=SV;'
      'function go(e){e.preventDefault();e.stopPropagation();l.click();}p.addEventListener("click",go);p.addEventListener("keydown",function(e){if(e.key==="Enter"||e.key===" ")go(e);});g.appendChild(p);var ls=l.querySelector(".st");if(ls)new MutationObserver(function(){p.classList.toggle("busy",ls.textContent==="\u2026");}).observe(ls,{childList:true,characterData:true,subtree:true});});}'
      'fix();new MutationObserver(fix).observe(T,{childList:true});})();</script>')
s = s.replace('</head>', css + '</head>', 1)
s = s.rstrip('\n') + '\n' + js + '\n'
if '--noversion' not in sys.argv:
    s = re.sub(r'(<meta name="app-version" content=")([^"]*)(")', lambda m: m.group(1) + '2026-11-26l' + m.group(3), s, count=1)
open('index.html', 'w', encoding='utf-8').write(s); print('ok')
