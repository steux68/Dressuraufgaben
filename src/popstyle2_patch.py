# Figuren (Lernen + Quiz) und Fragen/Situationen im Look der grossen Popups. Idempotent. 02.11.2026
import re,sys
s=open('index.html',encoding='utf-8').read()
m=re.search(r"const WSVG='([^']*)';\s*const ESVG='([^']*)';",s)
WSVG,ESVG=m.group(1),m.group(2)
if 'id="thFa"' not in s:
    b='<button type="button" class="tlar pw" id="thVa"'
    assert s.count(b)==1
    s=s.replace(b,'<button type="button" class="tlar pw" id="thFa" aria-label="Zurück" hidden>'+WSVG+'</button><button type="button" class="tlar pe" id="thFe" aria-label="Weiter" hidden>'+ESVG+'</button>\n'+b,1)
    old='<div class="top"><span class="tests" id="thTg"></span><span class="count" id="thCt"></span></div>\n<p class="nm" id="thNm"></p><p class="ds" id="thDs"></p><p class="de" id="thDe"></p>'
    assert old in s
    s=s.replace(old,'<p class="nm" id="thNm"></p><p class="ds" id="thDs"></p><p class="de" id="thDe"></p><dl class="anaDl"><dt>Karte</dt><dd id="thCt"></dd><dt>Aufgaben</dt><dd><span class="tests" id="thTg"></span></dd></dl>',1)
    # Fragen: runder E-Pfeil statt Knopf
    old='<button id="thQn" class="primary" disabled>Nächste Frage →</button>'
    assert old in s
    s=s.replace(old,old+'\n<button type="button" class="tlar pe" id="thQe" aria-label="Nächste Frage" disabled>'+ESVG+'</button>',1)
    css='''
/* Figuren und Fragen im Popup-Look */
#thFa,#thFe{position:absolute;top:50%;margin-top:-21px;width:42px;height:42px;min-height:0;border:0!important;padding:0;border-radius:50%!important;background:rgba(255,255,255,.82)!important;display:flex;align-items:center;justify-content:center;z-index:20;-webkit-tap-highlight-color:transparent}
#thFa{left:6px}#thFe{right:6px}
#thFa[hidden],#thFe[hidden]{display:none!important}
#thFa:disabled,#thFe:disabled{opacity:.28}
#thLearn .btns{display:none}
#thLearn .card,#thQuest .card{background:none;border:0;box-shadow:none;padding:2px 4px;gap:0}
#thNm{margin:0;color:#e30613;text-transform:uppercase;font-weight:700;font-size:1.35rem;line-height:1.15;letter-spacing:.01em}
#thDs{margin:6px 0 0;font-size:.98rem;line-height:1.45;color:#222}
#thDe{margin:6px 0 0;font-size:.9rem;color:#555}
#thLearn .anaDl,#thGame .score,#thQuest>.score{margin:10px 0 0;padding-top:6px;border-top:1px dotted #b8b8b8;font-size:12px;color:#888}
#thLearn .anaDl{display:grid;grid-template-columns:auto 1fr;gap:2px 10px;line-height:1.3}
#thLearn .anaDl dt{color:#888}#thLearn .anaDl dd{margin:0;color:#111}
#thGame{display:flex;flex-direction:column;gap:6px}
#thGame .qrow{display:none}
#thGame .opts,#thQuest .opts{display:flex;flex-direction:column;gap:4px}
#thGame .opts{order:1}#thGame .fb{order:2}#thGame .why{order:3}#thGame .score{order:4}
#thGame .opt,#thQuest .opt{width:100%;text-align:left;min-height:0;padding:7px 10px;font-size:.95rem}
#thGame .fb,#thQuest .fb{display:block!important;margin:2px 0 0;color:#e30613;text-transform:uppercase;font-weight:700;font-size:1.15rem;line-height:1.15;letter-spacing:.01em}
#thGame .why,#thQuest .why{display:block!important;margin:0;font-size:.92rem;line-height:1.35;color:#222}
#thGame .score strong,#thQuest .score strong{color:#111;font-weight:400}
#thQuest .q{margin:4px 0 6px;font-size:1.05rem;font-weight:700;color:#111}
#thQuest .card{justify-content:flex-start!important}
#theo #thQuest #thQch{background:transparent!important;border:0!important;box-shadow:none!important}
#thQuest .badge{color:#e30613;background:none!important;padding:0;text-transform:uppercase;font-weight:700;font-size:.8rem;letter-spacing:.04em}
#thQuest{position:relative}
#thQn{display:none}
#thQe{position:static;width:42px;height:42px;min-height:0;border:0!important;padding:0;border-radius:50%!important;background:rgba(255,255,255,.82)!important;display:flex;align-items:center;justify-content:center;margin:6px 0 0 auto}
#thQe:disabled{opacity:.28}
'''
    i=s.index('</style>',s.index('/* Sehen im Popup-Look */'))
    s=s[:i]+css+s[i:]
    js='''/* Figuren/Fragen: Pfeile steuern die vorhandenen Knoepfe */
function figUi(){const l=!g('thLearn').hidden,q=!g('thGame').hidden;
 g('thFa').hidden=!l;g('thFe').hidden=!(l||q);g('thFa').disabled=g('thPv').disabled;g('thFe').disabled=q?g('thGn').disabled:false;
 g('thQe').disabled=g('thQn').disabled;}
g('thFa').onclick=()=>g('thPv').click();
g('thFe').onclick=()=>{if(!g('thGame').hidden)g('thGn').click();else g('thNx').click();};
g('thQe').onclick=()=>g('thQn').click();
['thPv','thGn','thQn'].forEach(id=>new MutationObserver(figUi).observe(g(id),{attributes:true}));
'''
    a="let lockT=0;"
    s=s.replace(a,js+a,1)
    old=" lockSoon();seeUi();\n}\nSUBS.forEach"
    assert old in s
    s=s.replace(old," lockSoon();seeUi();figUi();\n}\nSUBS.forEach",1)
    s=s.replace("g('thFb').textContent=right?'Richtig.':'Richtig wäre: '+F[cur].n+'.';","g('thFb').textContent=right?'Richtig.':'Leider falsch.';",1)
    s=s.replace("g('thQfb').textContent='Richtig wäre: '+qcur.a+'.';","g('thQfb').textContent='Leider falsch.';",1)
if '--noversion' not in sys.argv:
    s=re.sub(r'(<meta name="app-version" content=")([^"]*)(")',lambda mm:mm.group(1)+'2026-11-02zzz57'+mm.group(3),s,count=1)
open('index.html','w',encoding='utf-8').write(s)
