import re
f='index.html'; s=open(f,encoding='utf8').read()
s=re.sub(r'/\* viergross \*/.*?/\* /viergross \*/\n','',s,flags=re.S)
css='/* viergross */\n#hscroll #intro{justify-content:flex-start;gap:6px}\n#intro .ipic{flex:1 1 0!important;height:auto!important;min-height:200px;max-height:620px}\n/* /viergross */\n'
i=s.rfind('</style>'); s=s[:i]+css+s[i:]
open(f,'w',encoding='utf8').write(s)
