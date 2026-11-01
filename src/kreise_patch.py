import re
f='index.html'; s=open(f,encoding='utf8').read()
blk="b.querySelector('.code').textContent=c;{const KB={thsV:'img/kreis_auge.svg',thsA:'img/kreis_anatomie.jpg',thsP:'img/kreis_pferde.jpg'}[id];if(KB){const cd=b.querySelector('.code');cd.textContent='';cd.setAttribute('role','img');cd.setAttribute('aria-label',n);cd.style.setProperty('background','#fff url('+KB+') center/'+(KB.slice(-4)==='.svg'?'118%':'cover')+' no-repeat','important');}}/* kreisbild */"
if '/* kreisbild */' in s:
    s=re.sub(r"b\.querySelector\('\.code'\)\.textContent=c;\{const KB=.*?/\* kreisbild \*/",lambda m:blk,s,count=1,flags=re.S)
else:
    a="b.querySelector('.code').textContent=c;"
    assert s.count(a)==1; s=s.replace(a,blk)
s=re.sub(r'/\* kreise-css \*/.*?/\* /kreise-css \*/\n','',s,flags=re.S)
sq='#p-w .tile .code{border-radius:0!important;width:52px;height:52px}\n'
z=sq+'.ad.on,.ad.ok,.ad.bad{z-index:8}\n.alab{z-index:9}\n'
s=re.sub(r'/\* ad-z-css \*/.*?/\* /ad-z-css \*/\n','',s,flags=re.S)
i=s.rfind('</style>'); s=s[:i]+'/* ad-z-css */\n'+z+'/* /ad-z-css */\n'+s[i:]
s=re.sub(r'(<meta name="app-version" content=")[^"]*"',r'\g<1>2026-11-01zzw"',s,count=1)
open(f,'w',encoding='utf8').write(s)
