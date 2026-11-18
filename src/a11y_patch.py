# 18.11.2026: Zugaenglichkeit, unsichtbar: Seitensprache (lang="de"), groessere Beruehrungsflaeche fuer Wissen-Schalter, INFO, OK, Info-Link.
# Aussehen unveraendert. Idempotent. Zurueck: git revert dieses Commit.
import re, sys
s = open('index.html', encoding='utf-8').read()
if 'id="a11y-css"' in s:
    print('schon vorhanden'); sys.exit(0)
def rep(a, b, n=1):
    global s
    assert s.count(a) == n, (a, s.count(a)); s = s.replace(a, b)
rep('<html data-theme="light">', '<html lang="de" data-theme="light">')
rep('</head>', '<style id="a11y-css">#wsw.hitx,#tipInfo.hitx,#tipx.hitx,#infoLink.hitx{--hh:44px!important}#tipInfo.hitx::after,#infoLink.hitx::after,#tipx.hitx::after{left:-10px!important;right:-10px!important}</style>\n</head>')
s = re.sub(r'(<meta name="app-version" content=")([^"]*)(")', lambda m: m.group(1) + '2026-11-18a' + m.group(3), s, count=1)
open('index.html', 'w', encoding='utf-8').write(s)
print('ok')
