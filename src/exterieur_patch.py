import re
f='index.html'; s=open(f,encoding='utf8').read()
js=open('src/anatomie.js',encoding='utf8').read()
a=s.index('<script id="ana-js">'); b=s.index('</script>',a)
s=s[:a]+'<script id="ana-js">\n'+js+'\n'+s[b:]
css='''
#aBr,#aBl{position:absolute;inset:0;width:100%;height:100%;pointer-events:none;z-index:1}
#aBr[hidden],#aBl[hidden]{display:none}
#aBr path{fill:none;stroke:#e30613;stroke-width:1.6;vector-effect:non-scaling-stroke;stroke-linejoin:round}
.abl{position:absolute;transform:translate(-50%,-100%);margin-top:-3px;font-size:11px;font-weight:700;color:#e30613;white-space:nowrap;background:#ffffffd9;padding:0 3px}
.anaBar+.anaBar{margin-top:-2px}
.aSwRow{display:flex;justify-content:space-between;gap:8px;margin-top:6px}
.aSw{display:flex;align-items:center;gap:6px;min-height:0;padding:2px 12px 2px 4px;border:1.5px solid #22281f;border-radius:30px;background:var(--surface);color:#111;font-size:.9rem;font-weight:700;-webkit-tap-highlight-color:transparent}
.aSw.e{padding:2px 4px 2px 12px}
.aSw[aria-pressed="false"]{border:1.5px dotted var(--muted);font-weight:500;color:var(--muted)}
.aSw[aria-pressed="true"]{border-color:transparent}
.aSw .ar{overflow:visible;flex:none}.aSw .rg{fill:none;stroke:#3a3c37;stroke-width:1px}.aSw .dt{fill:#4d4f4a;stroke:#1a1a1a;stroke-width:1px;stroke-linejoin:round}
.aSw text{fill:#3a3c37;font:700 6.4px Calibri,Carlito,sans-serif;text-anchor:middle;dominant-baseline:central}
.aSw .tr{display:none}.aSw[aria-pressed="false"] .tr{display:block;fill:none;stroke:#3a3c37;stroke-width:.7;transform-box:fill-box;transform-origin:center;animation:aring 2.2s ease-out infinite}
@keyframes aring{0%{transform:scale(1);opacity:.7}100%{transform:scale(1.6);opacity:0}}
@media (prefers-reduced-motion:reduce){.aSw .tr{animation:none}}
#thAna.full .aSwRow{display:none}
'''
s=re.sub(r'/\* ext-css \*/.*?/\* /ext-css \*/\n','',s,flags=re.S)
i=s.rfind('</style>'); s=s[:i]+'/* ext-css */\n'+css+'/* /ext-css */\n'+s[i:]
s=re.sub(r'(<meta name="app-version" content=")[^"]*"',r'\g<1>2026-11-01zzu"',s,count=1)
open(f,'w',encoding='utf8').write(s)
