import re
f='index.html'; s=open(f,encoding='utf8').read()
css='a.tile.oeps{padding-left:8px!important;padding-right:8px!important}\n'
s=re.sub(r'/\* oeps-row-css \*/.*?/\* /oeps-row-css \*/\n','',s,flags=re.S)
i=s.rfind('</style>'); s=s[:i]+'/* oeps-row-css */\n'+css+'/* /oeps-row-css */\n'+s[i:]
s=re.sub(r'(<meta name="app-version" content=")[^"]*"',r'\g<1>2026-11-01zzz4"',s,count=1)
open(f,'w',encoding='utf8').write(s)
