# Unsere Pferde: Quadrate (2 Spalten) -> Popup wie in der Anatomie, mit W/E-Pfeilen auf dem Bild
import re
f='index.html'; s=open(f,encoding='utf8').read()
a=s.index('function horses(){'); b=s.index('\nlet current=',a)
new=r"""function horses(){
 const box=g('thHlist');if(box.childElementCount)return;
 const WS='<svg class="ar" width="28" height="28" viewBox="-12 -12 24 24" aria-hidden="true"><circle class="tr" r="9.5"/><path class="rg" d="M-7.88 -5.31A9.5 9.5 0 1 1 -7.88 5.31"/><path class="dt" transform="rotate(180)" d="M5.4 0L-4.6 -4.9L-2.2 0L-4.6 4.9Z"/><text x="-9.50" y="0">W</text></svg>';
 const ES='<svg class="ar" width="28" height="28" viewBox="-12 -12 24 24" aria-hidden="true"><circle class="tr" r="9.5"/><path class="rg" d="M7.88 5.31A9.5 9.5 0 1 1 7.88 -5.31"/><path class="dt" transform="rotate(0)" d="M5.4 0L-4.6 -4.9L-2.2 0L-4.6 4.9Z"/><text x="9.50" y="0">E</text></svg>';
 const XS='<svg viewBox="-12 -12 24 24" aria-hidden="true"><circle class="rg" r="9.5"/><path class="xx" d="M-3.6 -3.6L3.6 3.6M3.6 -3.6L-3.6 3.6"/></svg>';
 const grid=document.createElement('div');grid.className='agal';
 let pi=0,pop=null;
 const $=id=>document.getElementById(id);
 function build(){
  pop=document.createElement('div');pop.className='tlpop anapop pferpop';pop.hidden=true;pop.setAttribute('role','dialog');pop.setAttribute('aria-modal','true');
  pop.innerHTML='<div class="tlcard"><div class="tltop"><span class="tlk" id="pfTk"></span><button type="button" class="tlx" id="pfX" aria-label="Schließen">'+XS+'</button></div><div class="tlbody"><figure class="gfig has" id="pfFig"><img id="pfImg" alt="" draggable="false"><button type="button" class="tlar pw" id="pfPv" aria-label="Vorheriges Pferd">'+WS+'</button><button type="button" class="tlar pe" id="pfNx" aria-label="Nächstes Pferd">'+ES+'</button></figure><h4 id="pfT"></h4><p id="pfM"></p><dl class="anaDl" id="pfDl"></dl></div></div>';
  document.body.appendChild(pop);
  $('pfX').onclick=close;pop.addEventListener('click',e=>{if(e.target===pop)close();});
  $('pfPv').onclick=()=>go(-1);$('pfNx').onclick=()=>go(1);
  addEventListener('keydown',e=>{if(pop.hidden)return;if(e.key==='Escape')close();else if(e.key==='ArrowLeft')go(-1);else if(e.key==='ArrowRight')go(1);});
  let tx=0,ty=0;pop.addEventListener('touchstart',e=>{tx=e.touches[0].clientX;ty=e.touches[0].clientY;},{passive:true});
  pop.addEventListener('touchend',e=>{const dx=e.changedTouches[0].clientX-tx,dy=e.changedTouches[0].clientY-ty;if(Math.abs(dx)>60&&Math.abs(dx)>Math.abs(dy)*1.6)go(dx<0?1:-1);},{passive:true});
 }
 function paint(){
  const p=P[pi];$('pfTk').innerHTML='<b></b> · '+(pi+1)+' / '+P.length;$('pfTk').firstChild.textContent='Pferd';
  $('pfImg').src=p.foto||'';$('pfImg').alt=p.n;$('pfT').textContent=p.n;$('pfM').textContent=p.m||'';
  const dl=$('pfDl');dl.textContent='';
  [['Wesen',p.w],['Eigenheiten',p.e],['Gut zu wissen',p.t],['Bild',(pi+1)+' von '+P.length]].forEach(([k,v])=>{if(!v)return;const dt=document.createElement('dt'),dd=document.createElement('dd');dt.textContent=k;dd.textContent=v;dl.append(dt,dd);});
 }
 function open(i){if(!pop)build();pi=i;paint();pop.hidden=false;pop.querySelector('.tlbody').scrollTop=0;}
 function close(){if(pop)pop.hidden=true;}
 function go(d){pi=(pi+P.length+d)%P.length;paint();}
 P.forEach((p,i)=>{
  const b=document.createElement('button');b.type='button';b.className='agc';
  const im=document.createElement('span');im.className='agi';if(p.foto)im.style.backgroundImage='url('+p.foto+')';
  const n=document.createElement('span');n.className='agn';n.textContent=p.n;
  const k=document.createElement('span');k.className='agk';k.textContent=(p.m||'').split(' · ')[0];
  b.append(im,n,k);b.onclick=()=>open(i);grid.appendChild(b);
 });
 box.appendChild(grid);
 window.pferdeClose=close;
}
"""
s=s[:a]+new+s[b:]
if 'pferdeClose' not in s.split("g('thHorse').hidden=which!=='thsP'")[1][:600]:
    s=s.replace("if(which!=='thsA'&&window.anaClose)anaClose();","if(which!=='thsA'&&window.anaClose)anaClose();if(which!=='thsP'&&window.pferdeClose)pferdeClose();",1)
css='''/* pferde-pop */
#thHlist .agi{aspect-ratio:1/1;background-position:center;background-size:cover}
#thHlist .agn{font-size:1rem}
/* /pferde-pop */'''
s=re.sub(r'/\* pferde-pop \*/.*?/\* /pferde-pop \*/\n?','',s,flags=re.S)
i=s.rfind('</style>'); s=s[:i]+css+'\n'+s[i:]
open(f,'w',encoding='utf8').write(s)
