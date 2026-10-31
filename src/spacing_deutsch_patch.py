"""Deutsch-App: Abstände und Linien (31.10. spät).
1) Kapitel sind nur noch so hoch wie ihr Inhalt (außer dem letzten): keine grauen/weißen Leerflächen mehr unter „mehr“-Leisten und unter kurzen Kapiteln.
2) Gekürzte Kapitel strecken ihre „mehr“-Zeile nicht mehr auf Bildschirmhöhe.
3) Hinweis, was sich hinter „mehr“ verbirgt, ist wieder sichtbar (einzeilig, kleiner, grau), z. B. „Verben & Formen · Aussprache …“ oder „+15 weitere“.
4) Doppellinien: Endet der Inhalt schon mit einer gepunkteten Linie (Listenzeilen), entfällt die obere Linie der „mehr“-Leiste (Klasse .nl).
Aufruf im Repo-Hauptordner: python3 src/spacing_deutsch_patch.py  (idempotent)"""
import re,sys
f='deutsch/index.html'; s=open(f,encoding='utf8').read()
if 'function dedupLine' in s: sys.exit('schon angewendet')
def rep(a,b):
    global s
    assert s.count(a)==1,a[:80]; s=s.replace(a,b,1)
# 1) Kapitelhöhe
rep('p.style.minHeight=Math.max(0,next===null?H-ROWS*HB+1:H-(ROWS-next)*HB-40-(r+1)*HB)+"px";',
    'p.style.minHeight=(next===null?Math.max(0,H-ROWS*HB+1):0)+"px";')
# 2) kein Strecken
rep('m.style.minHeight=(44+Math.max(0,av-y))+"px";','m.style.minHeight="";')
# 3) Hinweise
rep("""const hint=hid.length?hid.slice(0,3).join(" · ")+(hid.length>3?" …":""):rows?"+"+rows:"";m.setAttribute("aria-label","Mehr "+name+(hint?": "+hint:""));m.innerHTML=PLUS+'<span class="cvt">mehr</span><b>'+esc(name)+'</b>';}""",
    """const hint=hid.length?hid.slice(0,3).join(" · ")+(hid.length>3?" …":""):rows?"+"+rows+" weitere":"";m.setAttribute("aria-label","Mehr "+name+(hint?": "+hint:""));m.innerHTML=PLUS+'<span class="cvt">mehr</span><b>'+esc(name)+'</b>'+(hint?'<small>'+esc(hint)+'</small>':'');dedupLine(m);}""")
rep("""m.innerHTML=MINUS+'<span class="cvt">weniger</span><b>'+esc(name)+'</b>';return;""",
    """m.innerHTML=MINUS+'<span class="cvt">weniger</span><b>'+esc(name)+'</b>';dedupLine(m);return;""")
rep("""<span class=\\"cvt\\">mehr</span><b>Zitate</b></button>""" if False else """<span class="cvt">mehr</span><b>Zitate</b></button>""",
    """<span class="cvt">mehr</span><b>Zitate</b><small>+'+hid+' weitere</small></button>""")
# 4) Doppellinien
rep("let capT=0;function capAll(){clearTimeout(capT);capT=setTimeout(()=>{PAGES.forEach((P,i)=>capOne(P,i));},60);}",
    """/* endet der Inhalt schon mit einer gepunkteten Linie, braucht die Leiste oben keine eigene (keine Doppellinie) */
function dedupLine(m){m.classList.remove("nl");const pv=m.previousElementSibling;if(!pv||m.hidden)return;const T=m.getBoundingClientRect().top;
  for(const e of pv.querySelectorAll("*")){const r=e.getBoundingClientRect();if(!r.height||r.bottom>T+1||r.bottom<T-9)continue;const cs=getComputedStyle(e);
    if(/gradient/.test(cs.backgroundImage)||(cs.borderBottomStyle!=="none"&&parseFloat(cs.borderBottomWidth)>0)){m.classList.add("nl");return;}}}
let capT=0;function capAll(){clearTimeout(capT);capT=setTimeout(()=>{PAGES.forEach((P,i)=>capOne(P,i));document.querySelectorAll(".mrow:not([hidden])").forEach(dedupLine);},60);}""")
# CSS
css=('.mrow small{flex:1 1 0;min-width:0;margin-left:4px;overflow:hidden;white-space:nowrap;text-overflow:ellipsis;font-size:12px;font-weight:400;letter-spacing:0;color:var(--muted)}'
 '.mrow>span,.mrow>b{flex:none}.mrow.nl{margin-top:0;background:var(--df) left bottom/100% 1px no-repeat}'
 '.mrow.capm.nl{background:var(--df) left 29px/100% 1px no-repeat,#fff}.mrow.capm.nl:is(.p-links,.p-hist,.p-home){background:var(--df) left 29px/100% 1px no-repeat,#f4f4f2}')
rep('@keyframes mrp{',css+'@keyframes mrp{')
mm=re.search(r'(<meta name="app-version" content=")(\d{4}-\d{2}-\d{2})([a-z]+)(">)',s); nv=mm.group(3)[:-1]+chr(ord(mm.group(3)[-1])+1)
s=s.replace(mm.group(0),mm.group(1)+mm.group(2)+nv+mm.group(4),1)
open(f,'w',encoding='utf8').write(s); print('ok ->',mm.group(2)+nv)
