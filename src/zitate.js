(function(){
 const $=id=>document.getElementById(id),esc=s=>String(s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
 const WIKI={'Xenophon':['de:Xenophon','en:Xenophon'],'Gustav Steinbrecht':['de:Gustav_Steinbrecht','en:Gustav_Steinbrecht'],'Seneca':['de:Lucius_Annaeus_Seneca','de:Seneca','en:Seneca_the_Younger'],'William Shakespeare':['de:William_Shakespeare','en:William_Shakespeare'],
  'Friedrich von Bodenstedt':['de:Friedrich_von_Bodenstedt','en:Friedrich_von_Bodenstedt'],'Karl V. (zugeschrieben)':['de:Karl_V._(HRR)','en:Charles_V,_Holy_Roman_Emperor'],'Winston Churchill':['de:Winston_Churchill','en:Winston_Churchill']};
 let cache={};try{cache=JSON.parse(localStorage.getItem('zl_pics')||'{}')}catch(e){}
 const saveC=()=>{try{localStorage.setItem('zl_pics',JSON.stringify(cache))}catch(e){}};
 function loadPics(root){root.querySelectorAll('img[data-w]').forEach(im=>{const list=im.dataset.w.split('|'),key=list.join('|'),show=u=>{im.onload=()=>im.parentNode.classList.add('has');im.src=u;};
  if(cache[key]){show(cache[key]);return;}if(cache[key]===0)return;
  const next=i=>{if(i>=list.length){cache[key]=0;saveC();return;}const p=list[i].indexOf(':'),lg=list[i].slice(0,p),t=list[i].slice(p+1);
   fetch('https://'+lg+'.wikipedia.org/api/rest_v1/page/summary/'+encodeURIComponent(t)).then(r=>r.ok?r.json():null).then(j=>{const u=j&&(j.thumbnail&&j.thumbnail.source||j.originalimage&&j.originalimage.source);if(u){cache[key]=u;saveC();show(u);}else next(i+1);}).catch(()=>next(i+1));};
  next(0);});}
 const PLUS='<svg class="pl" viewBox="-12 -12 24 24" aria-hidden="true"><circle r="10.5"/><path d="M-5.5 0H5.5M0 -5.5V5.5"/></svg>';
 function build(){const src=$('thZl');if(!src||!src.children.length||$('zqsec'))return false;
  const heads=[...document.querySelectorAll('#theo2 .wsec')],zh=heads.find(h=>h.textContent.trim()==='Zitate');if(!zh)return false;
  const items=[];let sec='';[...src.children].forEach(el=>{if(el.classList.contains('wsec')){sec=el.textContent;return;}
   const q=el.querySelector('q'),b=el.querySelector('b');if(!q||!b)return;
   items.push({sec,ini:(el.querySelector('.pic')||{}).textContent||'',who:b.textContent,when:(el.querySelector('small')||{}).textContent||'',q:q.textContent,o:(el.querySelector('.o')||{}).textContent||'',n:(el.querySelector('.n')||{}).textContent||'',u:el.getAttribute('href')});});
  const secs=[...new Set(items.map(x=>x.sec))];let F='Alle',MORE=false;const CAP=6,PERSEC=2;
  const c=document.createElement('div');c.className='tc zqs';c.id='zqsec';
  function render(){let sec='',qi=0;const rows=[],cnt={};let total=0,shown=0;
   items.forEach(x=>{if(F!=='Alle'&&x.sec!==F)return;total++;cnt[x.sec]=(cnt[x.sec]||0)+1;if(!MORE&&(F==='Alle'?cnt[x.sec]>PERSEC:cnt[x.sec]>CAP))return;shown++;if(qi===0||x.sec!==sec){if(F==='Alle')rows.push('<h4 class="zqh">'+esc(x.sec)+'</h4>');if(x.sec!==sec){sec=x.sec;qi=0;}}
    const w=WIKI[x.who];
    rows.push('<a class="zqt'+(qi++%2?' alt':'')+'" href="'+esc(x.u)+'" target="_blank" rel="noopener"><span class="zpic" aria-hidden="true"><i>'+esc(x.ini)+'</i>'+(w?'<img alt="" loading="lazy" data-w="'+w.join('|')+'">':'')+'</span><span class="zqb"><b class="who">'+esc(x.who)+'</b><small>'+esc(x.when)+'</small><q>'+esc(x.q)+'</q>'+(x.o?'<span class="zen o">'+esc(x.o)+'</span>':'')+(x.n?'<span class="zen">'+esc(x.n)+'</span>':'')+'</span></a>');});
   c.innerHTML='<div class="wchips zch">'+['Alle'].concat(secs).map(f=>'<button type="button" data-f="'+esc(f)+'" aria-pressed="'+(F===f)+'">'+esc(f==='Wer hat das wirklich gesagt?'?'Wer sagte das?':f)+'</button>').join('')+'</div><div class="zql">'+rows.join('')+'</div>'+(total>shown||(MORE&&total>(F==='Alle'?PERSEC*secs.length:CAP))?'<button type="button" class="zmore" aria-expanded="'+MORE+'" aria-label="'+(MORE?'Weniger Zitate':'Mehr Zitate')+'"><svg class="zcx" viewBox="-12 -12 24 24" aria-hidden="true"><circle class="r1" r="8"/><circle class="r2" r="8"/><circle class="c" r="8"/><path class="v" d="M0 -4.2V4.2"/><path d="M-4.2 0H4.2"/></svg><span class="cvt"><span class="op">mehr</span><span class="cl">weniger</span></span><b>Zitate</b></button>':'')+'<p class="tline">Antippen öffnet die Quelle. Bilder: Wikipedia / Wikimedia Commons.</p>';
   c.querySelectorAll('.zch button').forEach(b=>b.onclick=()=>{F=b.dataset.f;MORE=false;render();});
   const zm=c.querySelector('.zmore');if(zm)zm.onclick=()=>{MORE=!MORE;render();if(!MORE)c.scrollIntoView({block:'nearest'});};loadPics(c);}
  render();src.style.display='none';zh.after(c);return true;}
 if(!build()){let n=0;const iv=setInterval(()=>{if(build()||++n>40)clearInterval(iv);},250);}
})();
