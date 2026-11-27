p='index.html';s=open(p,encoding='utf-8').read()
if 'links-testseiten' in s: print('already'); raise SystemExit
a="b.onclick=()=>{openWissen();setTimeout(()=>$(id).click(),0);};PW.appendChild(b);});\n"
assert s.count(a)==1
add=a+""" /*links-testseiten*/
 [['Gg','Gangarten','Schritt, Trab, Galopp: Fußfolge als Animation von oben','gangarten.html'],['Sk','Skala der Ausbildung','Die sechs Punkte als Treppe mit Phasen und Detailkarte','skala.html']].forEach(([c,n,d,u])=>{
  const b=document.createElement('button');b.className='tile ready wrow';
  b.innerHTML='<span class="code"></span><span><div class="nm"></div><div class="ds"></div></span><span class="st ready">Öffnen</span>';
  b.querySelector('.code').textContent=c;b.querySelector('.nm').textContent=n;b.querySelector('.ds').textContent=d;
  b.onclick=()=>{location.href=u;};PW.appendChild(b);});
"""
s=s.replace(a,add)
s=s.replace('2026-11-27-theorie','2026-11-27-testseiten')
open(p,'w',encoding='utf-8').write(s);open('version.txt','w').write('2026-11-27-testseiten');print('ok')
