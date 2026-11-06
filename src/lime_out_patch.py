# Restliches Limettengruen (Reiter-Staffel, Schalter) durch das einheitliche Aktiv-Gelb ersetzen. 06.11.2026.
import re, sys
s = open('index.html', encoding='utf-8').read()
if '/* lime-out */' in s:
    print('schon angewendet'); sys.exit(0)
n = 0
for a in ('#cdff3e', '#eaffae', '#e1ffb0', '#d7ff4a'):
    n += len(re.findall(re.escape(a), s, re.I)); s = re.sub(re.escape(a), '#ffec99', s, flags=re.I)
i = s.rindex('</style>'); s = s[:i] + '\n/* lime-out */\n' + s[i:]
s = re.sub(r'(<meta name="app-version" content=")([^"]*)(")', lambda m: m.group(1)+'2026-11-06zzz91'+m.group(3), s, count=1)
open('index.html','w',encoding='utf-8').write(s); print('ok', n)
