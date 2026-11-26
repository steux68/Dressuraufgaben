# PASSAGE 26.11.2026: Aushang-Kachel (Material): "PDF"-Pille durch das PDF-Symbol (dasein-design) ersetzt. Idempotent.
import re, sys
s = open('index.html', encoding='utf-8').read()
if 'id="pdfsym-css"' in s: sys.exit('schon angewendet')
svg = ('<svg viewBox="58 0 342 428" width="21" height="26" aria-hidden="true" focusable="false"><g fill="none" stroke="#4d4d4d" stroke-width="22" stroke-linejoin="round">'
       '<path d="M140 11H298L381 94V356Q381 384 353 384H140Q112 384 112 356V39Q112 11 140 11Z"/><path d="M298 11V70Q298 94 322 94H381"/></g>'
       '<rect x="68" y="80" width="202" height="84" fill="#e2401c"/><text x="169" y="148" fill="#fff" font-family="inherit" font-weight="700" font-size="74" text-anchor="middle" letter-spacing="2">PDF</text>'
       '<path d="M251 236H325V331H358L288 422L218 331H251Z" fill="#e2401c"/></svg>')
old = "b.className='tile pdf';\nb.innerHTML='<span class=\"code\"></span><span><div class=\"nm\"></div><div class=\"ds\"></div></span><span class=\"st ready\">PDF</span>';"
assert old in s
new = old.replace('<span class="st ready">PDF</span>', '<span class="pdfsym" aria-label="PDF">' + svg + '</span>')
s = s.replace(old, new, 1)
css = '<style id="pdfsym-css">.tile.pdf .pdfsym{display:inline-flex;align-items:center;justify-content:center;min-width:44px;height:32px;background:#ececea}</style>'
s = s.replace('</head>', css + '</head>', 1)
if '--noversion' not in sys.argv:
    s = re.sub(r'(<meta name="app-version" content=")([^"]*)(")', lambda m: m.group(1) + '2026-11-26n' + m.group(3), s, count=1)
open('index.html', 'w', encoding='utf-8').write(s); print('ok')
