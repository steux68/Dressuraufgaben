# Koerpersprache + Gesundheit: Titel 16 px, Text 14 px wie in den Popups. 25.11.2026
import re,sys
s=open('index.html',encoding='utf-8').read()
if 'karten-einheit-css' in s: sys.exit('schon angewendet')
CSS='<style id="karten-einheit-css">\n#thBody .blt,#thGes .blt{font-size:16px;line-height:1.15;margin:0 0 6px}\n#thBody dd,#thGes dd,#thBody .bldl dd,#thGes .bldl dd{font-size:14px;line-height:1.4}\n#thBody dt,#thGes dt{font-size:14px}\n</style>\n'
i=s.rindex('</head>'); s=s[:i]+CSS+s[i:]
s=re.sub(r'(<meta name="app-version" content=")[^"]*"',r'\g<1>2026-11-25d"',s,count=1)
open('index.html','w',encoding='utf-8').write(s)
