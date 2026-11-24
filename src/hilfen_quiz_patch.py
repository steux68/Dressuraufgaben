# Hilfen: Quiz (10 Fragen: Zeichen erkennen, Zeichen finden, Symbol deuten). Nur Zeichen mit eindeutigem Bild werden gefragt. Idempotent. 24.11.2026
import re,sys
s=open('index.html',encoding='utf-8').read()
if 'function hlQStart' in s: sys.exit('schon angewendet')
def rep(old,new):
    global s
    assert s.count(old)==1,old[:80]
    s=s.replace(old,new,1)
rep("[['l','Lernen'],['u','Übersicht'],['z','Zeichen']]","[['l','Lernen'],['u','Übersicht'],['z','Zeichen'],['q','Quiz']]")
rep("   if(a==='m')hls.m=v;","   if(a==='m'){hls.m=v;if(v==='q'&&!hq.l.length)hlQStart();}")
rep("   if(a==='p')hls.i=(hls.i-1+n)%n;\n","   if(a==='p')hls.i=(hls.i-1+n)%n;\n   if(a==='qa'&&!hq.done){hq.pick=+v;hq.done=true;if(hq.pick===hq.l[hq.i].c)hq.ok++;}\n   if(a==='qn'){hq.i++;hq.done=false;hq.pick=-1;}\n   if(a==='qr')hlQStart();\n")
rep(" o+='<p class=\"tline hiSrc\">"," if(hls.m==='q')o+='<div class=\"hiCard hiQ\"></div>';\n o+='<p class=\"tline hiSrc\">")
rep(" if(hls.m==='l')hlLock();\n}"," if(hls.m==='l')hlLock();\n if(hls.m==='q')hlQDraw();\n}")
JS=r"""
const HLX={hT:'Die Hand nimmt an oder hält durch und verändert so die Verbindung zum Pferdemaul.',hN:'Die Hand gibt nach, die Zügel werden weicher.',sF:'Der Gesäßknochen wird belastet, das Gewicht wirkt auf das Pferd.',sH:'Der Gesäßknochen wird weniger belastet.',sO:'Der Reiter entlastet das Gesäß, zum Beispiel beim Erheben aus dem Sattel.',lD:'Der Schenkel treibt das Pferd an.',lH:'Der Schenkel liegt hinter dem Gurt und verwahrt: er hält die Hinterhand auf der Linie.',lX:'Der Schenkel liegt ruhig am Pferd und treibt nicht.'};
const hq={l:[],i:0,ok:0,done:false,pick:-1,h:0};
function hlSig(p){return p.h+p.s+p.l+(p.b?1:0);}
function hlShuf(a){a=a.slice();for(let i=a.length-1;i>0;i--){const j=Math.floor(Math.random()*(i+1));[a[i],a[j]]=[a[j],a[i]];}return a;}
function hlQStart(){
 const uq=HL.filter(p=>HL.filter(x=>hlSig(x)===hlSig(p)).length===1),sh=hlShuf(uq),A=sh.slice(0,4),B=sh.slice(4,7),C=hlShuf(HLK).slice(0,3);
 const wr=(p)=>{const o=HL.filter(x=>hlSig(x)!==hlSig(p));return hlShuf(o.filter(x=>x.g===p.g)).concat(hlShuf(o.filter(x=>x.g!==p.g)));};
 const qs=[];
 A.forEach(p=>{const w=wr(p).slice(0,2),o=hlShuf([p].concat(w));qs.push({k:'a',p:p,o:o.map(x=>x.n),c:o.indexOf(p),e:p.t});});
 B.forEach(p=>{const L2=wr(p),sm=L2.filter(x=>x.g===p.g),ot=L2.filter(x=>x.g!==p.g),w=[...new Set([sm[0],ot[0]].concat(L2).filter(Boolean))].slice(0,2),o=hlShuf([p].concat(w));qs.push({k:'b',p:p,o:o,c:o.indexOf(p),e:p.t});});
 C.forEach(q=>{const same=HLK.filter(x=>x[0]!==q[0]&&x[0][0]===q[0][0]),oth=HLK.filter(x=>x[0]!==q[0]&&x[0][0]!==q[0][0]),w=hlShuf(same).concat(hlShuf(oth)).slice(0,2),o=hlShuf([q].concat(w));
  qs.push({k:'c',g:q[0],o:o.map(x=>x[1]),c:o.findIndex(x=>x[0]===q[0]),e:HLX[q[0]]});});
 hq.l=hlShuf(qs);hq.i=0;hq.ok=0;hq.done=false;hq.pick=-1;hq.h=0;
}
function hlQInner(q,done,pick){
 const n=hq.l.length,two=x=>String(x).padStart(2,'0');
 const T={a:'Zeichen erkennen',b:'Zeichen finden',c:'Symbol deuten'}[q.k];
 let h='<p class="hiN">'+T+'</p>';
 if(q.k==='a')h+='<p class="hiQq">Welche Hilfe zeigt dieses Zeichen?</p><div class="hiQf">'+hlPic(q.p,90,159)+'</div>';
 if(q.k==='b')h+='<p class="hiQq">Welches Zeichen gehört zu „'+q.p.n+'“?</p>';
 if(q.k==='c')h+='<p class="hiQq">Was bedeutet dieses Symbol?</p><div class="hiQf hiQg">'+hlMini(q.g)+'</div>';
 h+='<div class="hiQo'+(q.k==='b'?' row':'')+'">';
 q.o.forEach((t,i)=>{let c='hiQb'+(q.k==='b'?' pic':'');if(done){if(i===q.c)c+=' ok';else if(i===pick)c+=' bad';}
  h+='<button type="button" class="'+c+'" data-a="qa" data-v="'+i+'"'+(done?' disabled':'')+(q.k==='b'?' aria-label="Zeichen '+(i+1)+'"':'')+'>'+(q.k==='b'?hlPic(t,56,99):t+(done&&i===q.c?' ✓':''))+'</button>';});
 h+='</div><p class="hiQr">'+(done?(pick===q.c?'<b class="g">Richtig.</b> ':'<b class="r">Leider falsch.</b> ')+q.e:'')+'</p>';
 h+='<div class="hiDl hiQd"><span>'+two(hq.i+1)+' / '+two(n)+' · '+hq.ok+' richtig</span>'+(done?'<button type="button" class="hiAr" data-a="qn" aria-label="Weiter"><svg width="20" height="20" viewBox="0 0 20 20" aria-hidden="true"><path d="M7.5 4.5 13 10l-5.5 5.5" fill="none" stroke="#222" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg></button>':'<span></span>')+'</div>';
 return h;
}
function hlQDraw(){
 const root=g('thHi'),card=root.querySelector('.hiQ');if(!card)return;
 const n=hq.l.length;
 if(hq.i>=n){card.style.minHeight=hq.h?hq.h+'px':'';card.innerHTML='<p class="hiN">Ergebnis</p><p class="hiQq">'+hq.ok+' von '+n+' richtig.</p><div class="hiDl hiQd"><span>Hilfen</span><button type="button" class="hiQb" data-a="qr" style="width:auto;min-height:0;padding:6px 12px">Neu starten</button></div>';return;}
 if(!hq.h&&root.offsetParent){card.style.minHeight='';let m=0;hq.l.forEach(z=>{card.innerHTML=hlQInner(z,true,z.c);m=Math.max(m,card.offsetHeight);});hq.h=m;}
 if(hq.h)card.style.minHeight=hq.h+'px';
 card.innerHTML=hlQInner(hq.l[hq.i],hq.done,hq.pick);
}
"""
rep("function hilfen(){",JS+"function hilfen(){")
CSS="""#thHi .hiQq{margin:10px 0 8px;padding:0 4px;font-weight:700;font-size:1.05rem;color:#111;line-height:1.3}
#thHi .hiQf{display:flex;justify-content:center;margin:4px 0 10px}#thHi .hiQg svg{width:96px;height:77px}
#thHi .hiQo{display:flex;flex-direction:column;gap:6px}#thHi .hiQo.row{flex-direction:row}
#thHi .hiQb{text-align:left;padding:10px 12px;font-size:.95rem;line-height:1.35;color:#222;background:#fff;border:0;border-radius:0;outline:1px dotted #9a9a96;outline-offset:-1px;min-height:44px}
#thHi .hiQb.pic{flex:1;display:flex;justify-content:center;padding:6px 2px}
#thHi .hiQb:disabled{opacity:1;color:#222}
#thHi .hiQb.ok{background:#cdff3e;outline:1px solid #22281f;font-weight:700}
#thHi .hiQb.bad{background:#fbe3e1;outline:1px dotted #e30613;color:#e30613}
#thHi .hiQr{margin:10px 4px 8px;font-size:.98rem;line-height:1.4;color:#222}#thHi .hiQr .g{color:#1a7f37}#thHi .hiQr .r{color:#e30613}
#thHi .hiQd{align-items:center;min-height:50px;margin-top:8px}
#thHi .hiQ{display:flex;flex-direction:column}#thHi .hiQ .hiQd{margin-top:auto}
"""
i=s.rindex("</style>");s=s[:i]+CSS+s[i:]
if '--noversion' not in sys.argv:
    s=re.sub(r'(<meta name="app-version" content=")([^"]*)(")',lambda m:m.group(1)+'2026-11-24c'+m.group(3),s,count=1)
open('index.html','w',encoding='utf-8').write(s)
