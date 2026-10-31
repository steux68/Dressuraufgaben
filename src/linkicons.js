/* Links: kleine Symbole der Webseiten, direkt von dort geladen (apple-touch-icon, sonst favicon.ico). Fehlt eines, bleibt der Textkasten. */
(function(){
 const X=document.getElementById('xyz');if(!X)return;
 function load(a){
  if(a.dataset.ico)return;a.dataset.ico='1';
  let u;try{u=new URL(a.href);}catch(e){return;}
  if(/steinbach/.test(u.hostname))return;
  const box=a.querySelector('.lkw');if(!box)return;
  const cand=[u.origin+'/apple-touch-icon.png',u.origin+'/favicon.ico'];
  (function tryNext(i){
   if(i>=cand.length)return;
   const im=new Image();im.referrerPolicy='no-referrer';im.decoding='async';im.alt='';im.className='lkic';
   im.onload=()=>{if(im.naturalWidth>=16){box.classList.add('hasic');box.insertBefore(im,box.firstChild);}else tryNext(i+1);};
   im.onerror=()=>tryNext(i+1);im.src=cand[i];
  })(0);
 }
 function all(){X.querySelectorAll('a.lk').forEach(load);}
 if('IntersectionObserver' in window){const io=new IntersectionObserver(es=>{if(es.some(e=>e.isIntersecting)){all();io.disconnect();}},{rootMargin:'400px'});io.observe(X);}else all();
})();
