(function(ZL,ERAS,HEAD,MODE,PRE){
 const $=id=>document.getElementById(id),esc=s=>String(s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
 const reduceM=matchMedia('(prefers-reduced-motion: reduce)').matches;
 const eraOf=y=>ERAS.find(e=>y>=e[0]&&y<e[1])||ERAS[4],tlCol=e=>e.h?"#3a3c37":eraOf(e.y)[4];
 const WK=t=>"https://de.wikipedia.org/wiki/"+encodeURIComponent(t.replace(/ /g,"_"));
 const TXW=62,th=64,cw=th+6+TXW,xo=th+6,H=2*(24+2*th+6+7),S=Math.max(46,Math.ceil((th/2+6+TXW+4)/2)),X0=Math.ceil(th/2)+10;
 const G={H,th,cw,x:xo,S,X0,W:Math.ceil(X0+(ZL.length-1)*S+cw-th/2+14)};
 const tlX=y=>{const P=ZL.map((e,i)=>[e.y,X0+i*S]);if(y<=P[0][0])return Math.max(2,P[0][1]-(P[0][0]-y)*.2);for(let i=1;i<P.length;i++)if(y<=P[i][0]){const a=P[i-1],b=P[i];return a[1]+(b[1]-a[1])*(y-a[0])/(b[0]-a[0]);}const L=P[P.length-1];return Math.min(G.W-2,L[1]+(y-L[0])*3);};
 /* Bilder: Wikipedia-Zusammenfassung (erster Treffer mit Bild), Ergebnis wird gemerkt */
 let cache={};try{cache=JSON.parse(localStorage.getItem('zl_pics')||'{}')}catch(e){}
 const saveC=()=>{try{localStorage.setItem('zl_pics',JSON.stringify(cache))}catch(e){}};
 function loadPics(root){root.querySelectorAll('img[data-w]').forEach(im=>{const list=im.dataset.w.split('|'),key=list.join('|'),show=u=>{im.onload=()=>im.parentNode.classList.add('has');im.src=u;};
  if(cache[key]){show(cache[key]);return;}if(cache[key]===0)return;
  const next=i=>{if(i>=list.length){cache[key]=0;saveC();return;}const p=list[i].indexOf(':'),lg=list[i].slice(0,p),t=list[i].slice(p+1);
   fetch('https://'+lg+'.wikipedia.org/api/rest_v1/page/summary/'+encodeURIComponent(t)).then(r=>r.ok?r.json():null).then(j=>{const u=j&&(j.thumbnail&&j.thumbnail.source||j.originalimage&&j.originalimage.source);if(u){cache[key]=u;saveC();show(u);}else next(i+1);}).catch(()=>next(i+1));};
  next(0);});}
 const ARW=k=>'<svg class="ar" width="34" height="34" viewBox="-12 -12 24 24" aria-hidden="true"><path class="rg" d="'+(k<0?'M-7.88 -5.31A9.5 9.5 0 1 1 -7.88 5.31':'M7.88 5.31A9.5 9.5 0 1 1 7.88 -5.31')+'"/><path class="dt" transform="rotate('+(k<0?180:0)+')" d="M5.4 0L-4.6 -4.9L-2.2 0L-4.6 4.9Z"/><text x="'+(k<0?-9.5:9.5)+'" y="0">'+(k<0?'W':'E')+'</text></svg>';
 const lab=e=>e.lab||String(e.y);
 const thumb=e=>'<i>'+esc(e.ini)+'</i>'+(e.w?'<img alt="" loading="lazy" data-w="'+e.w.join('|')+'">':'');
 function html(){let sp='';const lanes={a:[],b:[]};
  ZL.forEach((e,i)=>{if(!e.e)return;const s=i%2?'b':'a',x1=tlX(e.y),x2=tlX(e.e),L=lanes[s];let k=0;while(L[k]!=null&&L[k]>x1-2&&k<2)k++;L[k]=x2;sp+='<i class="tlsp '+s+'" style="left:'+x1+'px;width:'+Math.max(6,x2-x1)+'px;--k:'+k+';background:'+tlCol(e)+'" title="'+esc(e.d)+'"></i>';});
  return '<div class="tlw"><div class="tl" id="@@" style="height:'+G.H+'px;--th:'+th+'px;--cw:'+cw+'px;--tw:'+TXW+'px;--x:'+xo+'px;--d:0px;--g:0px"><div class="tlc" style="width:'+G.W+'px">'+
   ERAS.map(r=>{const a=Math.max(0,tlX(r[0])),b=tlX(r[1]);return '<i class="tlwash" style="left:'+a+'px;width:'+(b-a)+'px;background:'+r[3]+'"></i><i class="tlera" style="left:'+a+'px;width:'+(b-a)+'px;background:'+r[3]+';color:'+r[4]+'">'+r[2]+'</i>';}).join('')+sp+
   ZL.map((e,i)=>{const ln=['a1','b1','a2','b2'][i%4],x=X0+i*S;return '<span class="tltk'+(e.h?' h':'')+'" data-i="'+i+'" style="left:'+x+'px;--ec:'+tlCol(e)+'">'+esc(lab(e))+'</span><i class="tlln '+ln+'" style="left:'+x+'px;background:'+tlCol(e)+'"></i>'+
    '<button type="button" class="tlcd '+ln+(e.h?' h':'')+'" data-i="'+i+'" style="left:'+(x-th/2)+'px" aria-label="'+esc(e.d)+': '+esc(e.t)+(e.h?' (Zeitgeschehen)':'')+'"><span class="tlth">'+thumb(e)+'</span><span class="tltx"><small>'+esc(e.d)+'</small><b>'+esc(e.t)+'</b>'+(e.h?'<em>Zeitgeschehen</em>':'')+'</span></button>';}).join('')+
   '</div></div><button type="button" class="tlar pw" aria-label="zurück">'+ARW(-1)+'</button><button type="button" class="tlar pe" aria-label="weiter">'+ARW(1)+'</button></div>'+
   '<div class="tls tlsm" id="@@sm" aria-label="Zeitleiste – Jahre">'+ZL.map((e,i)=>'<button type="button" data-i="'+i+'" class="'+(e.h?'h':'')+'" style="--ec:'+tlCol(e)+'" aria-label="'+esc(e.d)+': '+esc(e.t)+'">'+esc(lab(e))+'</button>').join('')+'</div>';}
 const TLO={i:0,open:false};
 function open(i){const n=ZL.length;i=(i+n)%n;TLO.i=i;const e=ZL[i],r=eraOf(e.y);TLO.open=true;$('@@pop').hidden=false;
  $('@@k').innerHTML='Geschichte <b>'+String(i+1).padStart(2,'0')+'</b> / '+n;
  $('@@b').innerHTML='<div class="gfig tlfig'+(e.h?' h':'')+'"><i>'+esc(e.ini)+'</i><img alt="'+esc(e.t)+'" data-w="'+e.w.join('|')+'"><button type="button" class="tlar pw" aria-label="früher">'+ARW(-1)+'</button><button type="button" class="tlar pe" aria-label="später">'+ARW(1)+'</button></div>'+
   '<p class="gs">'+esc(e.d)+' · '+(e.h?'Zeitgeschehen':r[2])+'</p><h4>'+esc(e.t)+'</h4><p>'+esc(e.x)+'</p><p class="tline">Bild: Wikipedia / Wikimedia Commons · Quelle: '+esc(e.l[1])+' · <a class="wk" href="'+esc(e.l[0])+'" target="_blank" rel="noopener" title="'+esc(e.l[1])+'" aria-label="Mehr bei '+esc(e.l[1])+'">mehr ↗</a></p>';
  $('@@b').scrollTop=0;$('@@b').querySelector('.pw').onclick=()=>open(TLO.i-1);$('@@b').querySelector('.pe').onclick=()=>open(TLO.i+1);
  loadPics($('@@b'));$('@@b').querySelectorAll('.gfig img[data-w]').forEach(im=>{const u=cache[im.dataset.w];if(u&&/\/\d+px-/.test(u)){im.onerror=()=>{im.onerror=null;im.src=u;};im.src=u.replace(/\/\d+px-/,'/800px-');}});
  $('@@s').querySelectorAll('button').forEach((b,k)=>{b.classList.toggle('on',k===i);b.setAttribute('aria-current',k===i?'true':'false');});
  const on=$('@@s').children[i];if(on){const Z=$('@@s');Z.scrollTo({left:on.offsetLeft-Z.clientWidth/2+on.offsetWidth/2,behavior:reduceM?'auto':'smooth'});}
  const T=$('@@');if(T)T.scrollLeft=X0+i*S-T.clientWidth/2;}
 const close=()=>{TLO.open=false;$('@@pop').hidden=true;};
 function mkPop(){const p=document.createElement('div');p.className='tlpop';p.id='@@pop';p.hidden=true;p.setAttribute('role','dialog');p.setAttribute('aria-modal','true');p.setAttribute('aria-labelledby','@@k');
  p.innerHTML='<div class="tlcard"><div class="tltop"><span class="tlk" id="@@k"></span><button type="button" class="tlx" id="@@x" aria-label="Schließen"><svg viewBox="-12 -12 24 24" aria-hidden="true"><circle class="rg" r="9.5"/><path class="xx" d="M-3.6 -3.6L3.6 3.6M3.6 -3.6L-3.6 3.6"/></svg></button></div><div class="tlbody" id="@@b"></div><div class="tls" id="@@s" aria-label="Zeitleiste">'+ZL.map((e,i)=>'<button type="button" data-i="'+i+'" class="'+(e.h?'h':'')+'" style="--ec:'+tlCol(e)+'" aria-label="'+esc(e.d)+': '+esc(e.t)+'">'+esc(lab(e))+'</button>').join('')+'</div></div>';
  document.body.appendChild(p);p.addEventListener('click',e=>{if(e.target===p)close();});$('@@x').onclick=close;
  $('@@s').querySelectorAll('button').forEach(b=>b.onclick=()=>open(+b.dataset.i));
  document.addEventListener('keydown',e=>{if(!TLO.open)return;if(e.key==='Escape')close();if(e.key==='ArrowRight')open(TLO.i+1);if(e.key==='ArrowLeft')open(TLO.i-1);});
  let x0=null,y0=0;const tb=$('@@b');tb.addEventListener('touchstart',e=>{x0=e.touches[0].clientX;y0=e.touches[0].clientY;},{passive:true});
  tb.addEventListener('touchend',e=>{if(x0==null)return;const dx=e.changedTouches[0].clientX-x0,dy=e.changedTouches[0].clientY-y0;x0=null;if(Math.abs(dx)>60&&Math.abs(dx)>Math.abs(dy)*1.5)open(TLO.i+(dx<0?1:-1));},{passive:true});}
 function bind(P){P.querySelectorAll('.tlcd').forEach(b=>b.onclick=()=>open(+b.dataset.i));loadPics(P);
  const T=$('@@'),M=$('@@sm');let who=null,t0=0;const now=()=>performance.now(),frac=e=>e.scrollLeft/Math.max(1,e.scrollWidth-e.clientWidth);
  const cur=()=>Math.max(0,Math.min(ZL.length-1,Math.round((T.scrollLeft+T.clientWidth/2-X0)/S)));let last=-1;
  const mark=()=>{const i=cur();if(i===last)return;last=i;M.querySelectorAll('button').forEach((b,k)=>b.classList.toggle('on',k===i));T.querySelectorAll('.tltk').forEach((b,k)=>b.classList.toggle('on',k===i));};
  const pw=P.querySelector('.tlw>.pw'),pe=P.querySelector('.tlw>.pe'),ends=()=>{pw.toggleAttribute('data-off',T.scrollLeft<4);pe.toggleAttribute('data-off',T.scrollLeft>T.scrollWidth-T.clientWidth-4);};
  pw.onclick=()=>T.scrollBy({left:-T.clientWidth*.6,behavior:reduceM?'auto':'smooth'});pe.onclick=()=>T.scrollBy({left:T.clientWidth*.6,behavior:reduceM?'auto':'smooth'});T.addEventListener('scroll',ends,{passive:true});ends();
  T.addEventListener('scroll',()=>{mark();if(who==='M'&&now()-t0<150)return;who='T';t0=now();M.scrollLeft=frac(T)*(M.scrollWidth-M.clientWidth);},{passive:true});
  M.addEventListener('scroll',()=>{if(who==='T'&&now()-t0<150)return;who='M';t0=now();T.scrollLeft=frac(M)*(T.scrollWidth-T.clientWidth);},{passive:true});
  M.querySelectorAll('button').forEach(b=>b.onclick=()=>{who='T';t0=now()+400;const i=+b.dataset.i;T.scrollTo({left:X0+i*S-T.clientWidth/2,behavior:reduceM?'auto':'smooth'});setTimeout(()=>{M.scrollTo({left:b.offsetLeft-M.clientWidth/2+b.offsetWidth/2,behavior:reduceM?'auto':'smooth'});},50);});
  mark();}
 function insert(){const box=$('theo2');if(!box||$('@@sec'))return false;
  const c=document.createElement('div');c.className='tc tlsec';c.id='@@sec';c.innerHTML=html()+'<p class="tline">Seitlich wischen · antippen für Bild und Text. Dunkle Felder: Zeitgeschehen. Bilder: Wikipedia / Wikimedia Commons.</p>';
  if(MODE==='A'){const h=document.createElement('p');h.className='wsec';h.textContent=HEAD;box.prepend(h,c);}
  else{const w=[...box.querySelectorAll('.wsec')].find(x=>/Kleine Geschichte/.test(x.textContent));if(!w)return false;w.textContent=HEAD;w.after(c);const l=$('thHl');if(l)l.style.display='none';}
  mkPop();bind(c);return true;}
 if(!insert()){let n=0;const iv=setInterval(()=>{if(insert()||++n>40)clearInterval(iv);},250);}
});
