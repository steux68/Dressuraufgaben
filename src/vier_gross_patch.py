import re
f='index.html'; s=open(f,encoding='utf8').read()
s=re.sub(r'/\* viergross \*/.*?/\* /viergross \*/\n','',s,flags=re.S)
css='/* viergross */\n#intro .ipic{height:clamp(190px,min(66vh,calc(100vh - 330px)),600px)!important}\n#hscroll #intro{gap:8px}\n/* /viergross */\n'
i=s.rfind('</style>'); s=s[:i]+css+s[i:]
open(f,'w',encoding='utf8').write(s)
