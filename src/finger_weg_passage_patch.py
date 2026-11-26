# PASSAGE 26.11.2026: Erstes Mal "Finger-Weg" wie in DOCH!: roter Punkt mit Welle + gelbes Etikett.
# Schritt 1 (Titelseite): Punkt neben M, Etikett "Tippe einen Buchstaben."  Schritt 2 (Aufgabenliste): Punkt unter "Üben" bei R1, Etikett "Tippe eine Aufgabe."
# Ersetzt die Tipp-Leiste "Als App aufs Handy legen" (steht weiter in Info). Zaehler localStorage "passage-fw" (0/1/2). Wiederholen: Info -> "Einfuehrung". Idempotent.
import re, sys
s = open('index.html', encoding='utf-8').read()
if 'id="fw-css"' in s: sys.exit('schon angewendet')
RED = '#a30b17'
css = ('<style id="fw-css">#tip{display:none!important}'
 '.fw{position:fixed;z-index:99990;pointer-events:none;opacity:0;transition:opacity .35s}.fw.on{opacity:1}'
 '.fw-d{width:0;height:0}'
 '.fw-d i{position:absolute;left:-12px;top:-12px;width:24px;height:24px;border-radius:50%;border:2px solid @R@;opacity:0;animation:fwrip 3.6s linear infinite}'
 '.fw-d i+i{animation-delay:.45s}'
 '.fw-d u{position:absolute;left:-5px;top:-5px;width:10px;height:10px;border-radius:50%;background:@R@;text-decoration:none;animation:fwcore 3.6s linear infinite}'
 '@keyframes fwrip{0%,6%{transform:scale(.3);opacity:0}10%{opacity:.9}34%{transform:scale(1);opacity:0}100%{opacity:0}}'
 '@keyframes fwcore{0%,4%{transform:scale(0)}9%{transform:scale(1)}30%{transform:none}34%{transform:translate(var(--kx),var(--ky))}38%{transform:none}42%{transform:translate(var(--kx),var(--ky))}46%,100%{transform:none}}'
 '.fw-l{background:#cdff3e;color:#222;border-radius:10px;font-weight:700;font-size:14px;padding:3px 10px;line-height:1.15;white-space:nowrap}'
 '.fw-l span{display:block;overflow:hidden;width:0;animation:fwty 1s steps(var(--n),end) .35s forwards}'
 '@keyframes fwty{to{width:var(--w)}}'
 '@media (prefers-reduced-motion:reduce){.fw-d i{display:none}.fw-d u{animation:none}.fw-l span{animation:none;width:auto}}'
 '#info button[data-fwr]{border:0;border-radius:0;background:#ececea;color:#1a1a1a;font:inherit;font-size:14px;padding:6px 12px;cursor:pointer}'
 '</style>').replace('@R@', RED)
js = r'''<script id="fw-js">(function(){
var K="passage-fw",els=[],tm=0,mode=0;
function get(){try{return +localStorage.getItem(K)||0}catch(e){return 0}}
function put(n){try{if(get()<n)localStorage.setItem(K,n)}catch(e){}}
function $(i){return document.getElementById(i)}
function clear(){clearTimeout(tm);els.forEach(function(e){e.remove()});els=[];mode=0;}
function dot(x,y,kx,ky){var d=document.createElement("div");d.className="fw fw-d";d.style.left=x+"px";d.style.top=y+"px";d.style.setProperty("--kx",kx+"px");d.style.setProperty("--ky",ky+"px");d.innerHTML="<i></i><i></i><u></u>";document.body.appendChild(d);els.push(d);setTimeout(function(){d.classList.add("on")},20);}
function lab(txt,x,y,align){var l=document.createElement("div");l.className="fw fw-l";l.innerHTML="<span>"+txt+"</span>";l.style.left="0px";l.style.top=y+"px";document.body.appendChild(l);var sp=l.firstChild;sp.style.setProperty("--w",sp.scrollWidth+"px");sp.style.setProperty("--n",txt.length);var w=sp.scrollWidth+22;var left=align==="r"?x-w:x;l.style.left=Math.max(4,Math.min(left,window.innerWidth-w-8))+"px";els.push(l);setTimeout(function(){l.classList.add("on")},20);}
function arm(){tm=setTimeout(clear,14000);}
function busy(){var i=$("info");return i&&!i.hidden;}
function show1(){clear();if(get()>=1||busy())return;var hs=$("hscroll");if(hs&&hs.scrollTop>4)return;var it=$("intro");if(!it||it.getBoundingClientRect().height<50)return;
 var m=[].slice.call(document.querySelectorAll("#intro .pin")).filter(function(g){return g.textContent.trim()==="C"})[0];if(!m)return;var r=m.getBoundingClientRect();if(!r.width)return;
 var y=r.top+r.height/2;dot(r.right+20,y,5,0);lab("Tippe hier.",r.right+38,y-13,"l");mode=1;arm();}
function showTile(){clear();if(get()>=2||get()<1||busy())return;var t=document.querySelector("#tiles .tile");if(!t)return;var st=t.querySelector(".st")||t;var r=st.getBoundingClientRect(),tr=t.getBoundingClientRect();if(r.width<10||tr.top<110||tr.bottom>window.innerHeight-60)return;
 var cx=r.left+r.width/2;dot(cx,r.top-13,0,5);lab("Tippe hier.",r.right,r.bottom+3,"r");mode=2;arm();}
document.addEventListener("pointerdown",function(e){if(!els.length)return;var t=e.target,m=mode;clear();
 if(m===1){if(t.closest&&t.closest("#intro")){put(1);setTimeout(showTile,1500);}return;}
 if(m===2)put(2);},true);
var hs=$("hscroll");if(hs)hs.addEventListener("scroll",function(){if(els.length)clear();},{passive:true});
window.addEventListener("resize",function(){if(els.length)clear();});
document.addEventListener("click",function(e){var b=e.target.closest&&e.target.closest("[data-fwr]");if(!b)return;try{localStorage.setItem(K,"0")}catch(x){}var h=$("homebtn");if(h)h.click();else location.reload();});
setTimeout(show1,2200);
})();</script>'''
assert '</head>' in s
s = s.replace('</head>', css + '</head>', 1)
a = '<p><b>Android (Chrome):</b> Menü ⋮ → „Zum Startbildschirm hinzufügen“</p></div>'
assert s.count(a) == 1
s = s.replace(a, a.replace('</div>', '') + '</div>\n<div><p><b>Einführung:</b> <button type="button" data-fwr="1">Hinweise noch einmal zeigen</button></p></div>')
s = s.rstrip('\n') + '\n' + js + '\n'
if '--noversion' not in sys.argv:
    s = re.sub(r'(<meta name="app-version" content=")([^"]*)(")', lambda m: m.group(1) + '2026-11-26h' + m.group(3), s, count=1)
open('index.html', 'w', encoding='utf-8').write(s)
print('ok')
