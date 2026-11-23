#!/usr/bin/env python3
"""Anatomie-Galerie: nur der Titel im Band (keine Punktzahl, kein 'Originalseite'). python3 src/anatomie_titel_patch.py <version> index.html"""
import sys, re
ver, path = sys.argv[1], sys.argv[2]
s = open(path, encoding='utf8').read()
if 'id="ana-titel-css"' in s:
    print('schon angewendet'); sys.exit(0)
CSS = '<style id="ana-titel-css">.agc .agk{display:none!important}.agc .agb{padding:5px 6px}</style>'
j = s.rindex('</style>') + len('</style>')
s = s[:j] + '\n' + CSS + s[j:]
m = re.search(r'(<meta name="app-version" content=")([^"]*)(")', s)
s = s[:m.start(2)] + ver + s[m.end(2):]
open(path, 'w', encoding='utf8').write(s)
print('ok', m.group(2), '->', ver)
