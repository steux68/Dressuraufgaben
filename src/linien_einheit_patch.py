# PASSAGE 26.11.2026: Linienfarben vereinheitlicht (Punktlinie #8a8a8a -> #b8b8b8). Idempotent.
import re, sys
s = open('index.html', encoding='utf-8').read()
a = 'repeating-linear-gradient(to bottom,#8a8a8a 0 1px,transparent 1px 3px)'
b = 'repeating-linear-gradient(to right,#8a8a8a 0 1px,transparent 1px 3px)'
n = s.count(a) + s.count(b)
s = s.replace(a, a.replace('#8a8a8a', '#b8b8b8')).replace(b, b.replace('#8a8a8a', '#b8b8b8'))
if '--noversion' not in sys.argv and n:
    s = re.sub(r'(<meta name="app-version" content=")([^"]*)(")', lambda m: m.group(1) + '2026-11-26r' + m.group(3), s, count=1)
open('index.html', 'w', encoding='utf-8').write(s); print('ok', n)
