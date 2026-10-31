
(function(){
 const I=document.getElementById('intro'),svg=I&&I.querySelector('.vier');if(!svg)return;
 const ns='http://www.w3.org/2000/svg',T=[...svg.querySelectorAll('text')];
 const order=['A','K','E','H','C','M','B','F','X'],pos=order.map(l=>{const t=T.find(x=>x.textContent===l);return[+t.getAttribute('x'),+t.getAttribute('y')];});
 const c=document.createElementNS(ns,'circle');c.setAttribute('id','lhi');c.setAttribute('r','14');c.setAttribute('class','lhi');svg.insertBefore(c,T[0]);
 const iab=I.querySelector('.iabc');
 const cols=['#ffe14d','#cdff3e','#ffe14d','#ffd0d6','#cdff3e','#d6e4ff','#ffe14d','#cdff3e','#ffe14d'];
 let k=0,t0=0;
 function step(){
  if(I.hidden||document.hidden){t0=0;c.style.opacity=0;return;}
  if(!t0)t0=Date.now();if(Date.now()-t0<3700){c.style.opacity=0;return;}
  const p=pos[k%order.length];c.setAttribute('cx',p[0]);c.setAttribute('cy',p[1]);c.setAttribute('r',order[k%order.length]==='X'?'17':'14');
  c.style.fill=cols[k%cols.length];c.style.opacity=1;c.classList.remove('lhp');void c.getBoundingClientRect();c.classList.add('lhp');
  k++;}
 setInterval(step,1000);
 I.addEventListener('click',()=>{c.style.opacity=0;t0=Date.now()+1e9;},true);
})();
