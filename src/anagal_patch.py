import re
f='index.html'; s=open(f,encoding='utf8').read()
js=open('src/anatomie.js',encoding='utf8').read()
a=s.index('<script id="ana-js">'); b=s.index('</script>',a)
s=s[:a]+'<script id="ana-js">\n'+js+'\n'+s[b:]
old=open('src/anatomie.css',encoding='utf8').read()
s=s.replace(old,'',1)
s=re.sub(r'/\* ext-css \*/.*?/\* /ext-css \*/\n','',s,flags=re.S)
s=re.sub(r'/\* anagal-css \*/.*?/\* /anagal-css \*/\n','',s,flags=re.S)
css=open('src/anatomie2.css',encoding='utf8').read()
i=s.rfind('</style>'); s=s[:i]+'/* anagal-css */\n'+css+'\n/* /anagal-css */\n'+s[i:]
s=re.sub(r'(<meta name="app-version" content=")[^"]*"',r'\g<1>2026-11-01zzv"',s,count=1)
open(f,'w',encoding='utf8').write(s)
