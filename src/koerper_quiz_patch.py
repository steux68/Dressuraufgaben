# Koerpersprache: Lernen/Quiz-Umschalter und kleines Quiz (10 Fragen: Zeichen -> Bedeutung). Idempotent. 02.11.2026
import re,sys
s=open('index.html',encoding='utf-8').read()
if 'function bodyQuiz' in s: sys.exit('schon angewendet')
def rep(old,new):
    global s
    assert s.count(old)==1,old[:70]
    s=s.replace(old,new,1)
ESVG='<svg class="ar" width="28" height="28" viewBox="-12 -12 24 24" aria-hidden="true"><circle class="tr" r="9.5"/><path class="rg" d="M7.88 5.31A9.5 9.5 0 1 1 7.88 -5.31"/><path class="dt" transform="rotate(0)" d="M5.4 0L-4.6 -4.9L-2.2 0L-4.6 4.9Z"/><text x="9.50" y="0">E</text></svg>'
rep("function bodyLang(){\n const root=g('thBody');root.innerHTML='';","function bodyLang(){\n const root=g('thBody');root.innerHTML='';\n root.appendChild(bodyModeSeg());if(bqz){bodyQuiz(root);return;}")
JS=r"""
let bqz=false,BQ={l:[],i:0,ok:0,done:false,pick:-1};
function bodyModeSeg(){const seg=document.createElement('div');seg.className='anaSeg bqseg';
 [['Lernen',false],['Quiz',true]].forEach(a=>{const x=document.createElement('button');x.type='button';x.textContent=a[0];x.setAttribute('aria-pressed',bqz===a[1]);x.onclick=()=>{bqz=a[1];if(bqz)bqStart();bodyLang();};seg.appendChild(x);});return seg;}
function bqStart(){const all=[];BL.forEach((b,gi)=>b.rows.forEach((r,ri)=>all.push({g:gi,k:b.k,t:b.t,q:r[0],a:r[1]})));
 const sh=a=>{a=a.slice();for(let i=a.length-1;i>0;i--){const j=Math.floor(Math.random()*(i+1));[a[i],a[j]]=[a[j],a[i]];}return a;};
 BQ.l=sh(all).slice(0,10).map(q=>{const same=sh(all.filter(x=>x.a!==q.a&&x.g===q.g)),oth=sh(all.filter(x=>x.a!==q.a&&x.g!==q.g));
  const w=same.concat(oth).slice(0,2).map(x=>x.a);const o=sh([q.a].concat(w));q.o=o;q.c=o.indexOf(q.a);return q;});
 BQ.i=0;BQ.ok=0;BQ.done=false;BQ.pick=-1;BQ.h=0;}
function bodyQuiz(root){
 const card=document.createElement('div');card.className='card blcard bqcard';root.appendChild(card);
 const n=BQ.l.length,two=x=>String(x).padStart(2,'0');
 if(BQ.i>=n){card.innerHTML='<p class="blt">Ergebnis</p><p class="bqq">'+BQ.ok+' von '+n+' richtig.</p><div class="bqbar"><span>Körpersprache</span><span><button type="button" class="bqe" id="bqr" aria-label="Neu starten" style="width:auto;padding:0 10px">Neu starten</button></span></div>';
  card.querySelector('#bqr').onclick=()=>{bqStart();bodyLang();};return;}
 const q=BQ.l[BQ.i];
 if(!BQ.h){let m=0;BQ.l.forEach(z=>{card.innerHTML=bqHTML(z,true,z.c,two,n);m=Math.max(m,card.offsetHeight);});BQ.h=m;}
 card.style.minHeight=BQ.h+'px';card.innerHTML=bqHTML(q,BQ.done,BQ.pick,two,n);
 card.querySelectorAll('.bqb').forEach(b=>b.onclick=()=>{if(BQ.done)return;BQ.pick=+b.dataset.i;BQ.done=true;if(BQ.pick===q.c)BQ.ok++;bodyLang();});
 const nx=card.querySelector('#bqn');if(nx)nx.onclick=()=>{BQ.i++;BQ.done=false;BQ.pick=-1;bodyLang();};
}
function bqHTML(q,done,pick,two,n){
 let h='<p class="blt">'+q.t+'</p><p class="bqq">'+q.q+'</p><div class="bqo">';
 q.o.forEach((t,i)=>{let c='bqb';if(done){if(i===q.c)c+=' ok';else if(i===pick)c+=' bad';}h+='<button type="button" class="'+c+'" data-i="'+i+'"'+(done?' disabled':'')+'>'+t+(done&&i===q.c?' ✓':'')+'</button>';});
 h+='</div><p class="bqf">'+(done?(pick===q.c?'<b class="g">Richtig.</b>':'<b class="r">Leider falsch.</b>'):'')+'</p>';
 h+='<div class="bqbar"><span>'+two(BQ.i+1)+' / '+two(n)+' · '+BQ.ok+' richtig</span>'+(done?'<button type="button" class="bqe" id="bqn" aria-label="Weiter">__E__</button>':'<span></span>')+'</div>';
 return h;
}
""".replace('__E__',ESVG.replace("'","\\'"))
rep("function hist(){",JS+"function hist(){")
CSS="""#thBody .bqseg{margin:8px 0 4px}
#thBody .bqcard{display:flex;flex-direction:column}#thBody .bqcard .bqbar{margin-top:auto}#thBody .bqcard .bqf{margin-bottom:8px}
#thBody .bqq{margin:10px 0 8px;font-weight:700;font-size:1.05rem;color:#111;line-height:1.3}
#thBody .bqo{display:flex;flex-direction:column;gap:6px}
#thBody .bqb{text-align:left;padding:10px 12px;font-size:.95rem;line-height:1.35;color:#222;background:#fff;border:0;outline:1px dotted #9a9a96;outline-offset:-1px;min-height:44px}
#thBody .bqb:disabled{opacity:1;color:#222}
#thBody .bqb.ok{background:#d4ff3a;outline:1px solid #7a9a00;font-weight:700}
#thBody .bqb.bad{background:#fbe3e1;outline:1px dotted #e30613;color:#e30613}
#thBody .bqf{margin:8px 0 0;min-height:1.4em;font-size:.98rem}#thBody .bqf .g{color:#1a7f37}#thBody .bqf .r{color:#e30613}
#thBody .bqbar{display:flex;align-items:center;justify-content:space-between;margin-top:8px;padding-top:6px;border-top:1px dotted #b8b8b8;font-size:12px;color:#888;min-height:46px}
#thBody .bqe{position:static;width:42px;height:42px;padding:0;border:0!important;border-radius:50%!important;background:rgba(255,255,255,.82)!important;display:flex;align-items:center;justify-content:center;color:#666}
"""
i=s.rindex("</style>");s=s[:i]+CSS+s[i:]
if '--noversion' not in sys.argv:
    s=re.sub(r'(<meta name="app-version" content=")([^"]*)(")',lambda m:m.group(1)+'2026-11-02zzz61'+m.group(3),s,count=1)
open('index.html','w',encoding='utf-8').write(s)
