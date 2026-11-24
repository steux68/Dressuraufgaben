import re,sys
f='index.html'; s=open(f,encoding='utf8').read()
css=('#tiles .tile.ready.hasl .code{width:31px!important;height:31px!important;min-width:31px!important;font-size:14px!important;padding:0!important;line-height:1!important}\n'
     '#tiles .tile.lkrow .code{width:26px!important;height:26px!important;min-width:26px!important;font-size:11px!important}\n')
s=re.sub(r'/\* kreise2-css \*/.*?/\* /kreise2-css \*/\n','',s,flags=re.S)
i=s.rfind('</style>'); s=s[:i]+'/* kreise2-css */\n'+css+'/* /kreise2-css */\n'+s[i:]
if '--noversion' not in sys.argv:
    s=re.sub(r'(<meta name="app-version" content=")[^"]*"',r'\g<1>2026-11-24a"',s,count=1)
open(f,'w',encoding='utf8').write(s)
