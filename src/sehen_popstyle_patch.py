# Sehen im Look der grossen Popups: W/E-Pfeile auf dem Diagramm statt "Zurueck/Weiter", Lernen|Quiz-Schalter oben,
# roter Grossbuchstaben-Titel + Text + gepunktete Angabenzeile statt grauem Kasten; Quiz im gleichen Stil. Idempotent. 02.11.2026
import re,sys
s=open('index.html',encoding='utf-8').read()
m=re.search(r"const WSVG='([^']*)';\s*const ESVG='([^']*)';",s)
WSVG,ESVG=m.group(1),m.group(2)
if 'id="thVseg"' not in s:
    # 1) Schalter und Hinweis ueber dem Diagramm
    a='<div id="thStage">'
    assert s.count(a)==1
    s=s.replace(a,'<div class="anaSeg" id="thVseg" hidden><button type="button" id="thVsL" aria-pressed="true">Lernen</button><button type="button" id="thVsQ" aria-pressed="false">Quiz</button></div>\n<p class="vhint" id="thVhint" hidden>Wo bist du? Kann dich das Pferd sehen?</p>\n'+a,1)
    # 2) Pfeile im Diagramm
    b='<g id="thEy"></g></svg>'
    assert s.count(b)==1
    s=s.replace(b,b+'\n<button type="button" class="tlar pw" id="thVa" aria-label="Zurück" hidden>'+WSVG+'</button><button type="button" class="tlar pe" id="thVe" aria-label="Weiter" hidden>'+ESVG+'</button>',1)
    # 3) Lernkarte: Titel, Text, Angabenzeile
    old='<div class="top"><span class="badge">Sehen</span><span class="count" id="thVct"></span></div>\n<p class="nm" id="thVnm"></p><p class="ds" id="thVds"></p>'
    assert old in s
    s=s.replace(old,'<p class="nm" id="thVnm"></p><p class="ds" id="thVds"></p><dl class="anaDl"><dt>Karte</dt><dd id="thVct"></dd><dt>Thema</dt><dd>Sehen</dd></dl>',1)
    # 4) CSS
    css='''
/* Sehen im Popup-Look */
#thStage{position:relative}
#thVa,#thVe{position:absolute;top:50%;margin-top:-21px;width:42px;height:42px;min-height:0;border:0!important;padding:0;border-radius:50%!important;background:rgba(255,255,255,.82)!important;display:flex;align-items:center;justify-content:center;z-index:20;-webkit-tap-highlight-color:transparent}
#thVa{left:6px}#thVe{right:6px}
#thVa[hidden],#thVe[hidden]{display:none!important}
#thVa:disabled,#thVe:disabled{opacity:.28}
#thVseg{display:flex;margin:6px 0 2px}#thVseg[hidden]{display:none}
#thVhint{margin:2px 0;text-align:center;font-size:.95rem;color:#222}#thVhint[hidden]{display:none}
#thSee .btns{display:none}
#thVlearn .card{background:none;border:0;box-shadow:none;padding:2px 4px;gap:0}
#thVnm{margin:0;color:#e30613;text-transform:uppercase;font-weight:700;font-size:1.35rem;line-height:1.15;letter-spacing:.01em}
#thVds{margin:6px 0 0;font-size:.98rem;line-height:1.45;color:#222}
#thSee .anaDl{margin:10px 0 0;padding-top:6px;border-top:1px dotted #b8b8b8;display:grid;grid-template-columns:auto 1fr;gap:2px 10px;font-size:12px;line-height:1.3}
#thSee .anaDl dt{color:#888}#thSee .anaDl dd{margin:0;color:#111}
#thVquiz{display:flex;flex-direction:column;gap:6px}
#thVquiz .qrow{display:none}
#thVquiz .opts{order:1;display:flex;flex-direction:column;gap:4px}
#thVquiz .opt{width:100%;text-align:left;min-height:0;padding:7px 10px;font-size:.95rem}
#thVquiz .fb{order:2;display:block!important;margin:2px 0 0;color:#e30613;text-transform:uppercase;font-weight:700;font-size:1.15rem;line-height:1.15;letter-spacing:.01em}
#thVquiz .why{order:3;display:block!important;margin:0;font-size:.92rem;line-height:1.35;color:#222}
#thVquiz .why b{color:#222;font-weight:700}
#thVquiz .score{order:4;margin-top:6px;padding-top:6px;border-top:1px dotted #b8b8b8;font-size:12px;color:#888}
#thVquiz .score strong{color:#111;font-weight:400}
#thVquiz .score button{display:none}
'''
    k='</style>'
    i=s.index(k,s.index('#thEye .zb{fill:'))
    s=s[:i]+css+s[i:]
    # 5) JS
    js='''/* Sehen: Popup-Look, Schalter und Pfeile steuern die vorhandenen Knoepfe */
function seeUi(){const on=!g('thSee').hidden,q=vMode==='q';
 g('thVseg').hidden=!on;g('thVhint').hidden=!(on&&q);g('thVa').hidden=!(on&&!q);g('thVe').hidden=!on;
 g('thVsL').setAttribute('aria-pressed',!q);g('thVsQ').setAttribute('aria-pressed',q);
 g('thVa').disabled=g('thVpv').disabled;g('thVe').disabled=q?g('thVnext').disabled:false;
 g('thVe').setAttribute('aria-label',q?g('thVnext').textContent.replace(/\\s*→/,''):'Weiter');}
g('thVsL').onclick=()=>{if(vMode==='q')g('thVback').click();};
g('thVsQ').onclick=()=>{if(vMode!=='q')g('thVgo').click();};
g('thVa').onclick=()=>g('thVpv').click();
g('thVe').onclick=()=>{if(vMode==='q')g('thVnext').click();else g('thVnx').click();};
['thVnext','thVpv'].forEach(id=>new MutationObserver(seeUi).observe(g(id),{attributes:true,childList:true,characterData:true,subtree:true}));
function lockQuiz(){const f=g('thVfb'),w=g('thVwhy');f.style.minHeight='';w.style.minHeight='';const kf=f.textContent,kw=w.innerHTML;let mf=0,mw=0;
 ['Richtig.','Leider falsch.','Fertig: '+VR+' von '+VR+' richtig.'].forEach(t=>{f.textContent=t;mf=Math.max(mf,f.offsetHeight);});
 Object.values(VW).forEach(t=>{why('thVwhy',t);mw=Math.max(mw,w.offsetHeight);});
 f.textContent=kf;w.innerHTML=kw;f.style.minHeight=mf+'px';w.style.minHeight=mw+'px';}
'''
    anchor="let lockT=0;"
    assert anchor in s
    s=s.replace(anchor,js+anchor,1)
    old="lockWhy('thVfb','thVwhy',Object.values(VW))"
    assert old in s
    s=s.replace(old,"lockQuiz()",1)
    old=" lockSoon();\n}\nSUBS.forEach"
    assert old in s
    s=s.replace(old," lockSoon();seeUi();\n}\nSUBS.forEach",1)
    old="function seeMode(m){vMode=m;lockSoon();"
    assert old in s
    s=s.replace(old,old+"seeUi();",1)
    old="g('thVfb').textContent='Richtig wäre: '+VA[vk]+'.';"
    assert old in s
    s=s.replace(old,"g('thVfb').textContent='Leider falsch.';",1)
    # 6) Beschriftungen "ein Auge" nach innen, damit die Pfeile sie nicht verdecken
    s=s.replace("['ein Auge',44,150],['ein Auge',276,150]","['ein Auge',72,150],['ein Auge',248,150]")
if '--noversion' not in sys.argv:
    s=re.sub(r'(<meta name="app-version" content=")([^"]*)(")',lambda mm:mm.group(1)+'2026-11-02zzz43'+mm.group(3),s,count=1)
open('index.html','w',encoding='utf-8').write(s)
