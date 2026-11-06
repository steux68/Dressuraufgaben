# Anatomie: Tippen aufs Bild = echtes Vollbild (ohne Kopfzeile/Leiste, Beschreibung als Blatt unten), nochmal tippen = zurueck in den Kasten. Idempotent. 06.11.2026
import re, sys
s = open('index.html', encoding='utf-8').read()
if '/* fullscreen-tap */' in s:
    print('schon angewendet'); sys.exit(0)

def rep(old, new):
    global s
    assert s.count(old) == 1, f'{s.count(old)}x: {old[:80]}'
    s = s.replace(old, new)

rep("sc.addEventListener('click',e=>{if(full||e.target.closest('.ad'))return;if(mode==='quiz'&&qtype==='where'&&!answered)return;setFull(true);});",
    "sc.addEventListener('click',e=>{if(e.target.closest('.ad'))return;if(mode==='quiz'&&qtype==='where'&&!answered)return;setFull(!full);});")
rep("zoom=v&&innerWidth<innerHeight?(W/H>1.2?2.2:1.2):1", "zoom=v&&innerWidth<innerHeight&&W/H>1.2?1.8:1")
rep("const base=Math.min(innerWidth-20,(innerHeight-170)*W/H);", "const base=Math.min(innerWidth,innerHeight*W/H);")
rep("{const h=$('aHint'),o=$('aOv'),", "pop.classList.toggle('noSel',mode==='lern'&&sel<0);{const h=$('aHint'),o=$('aOv'),")
rep("if(full)x=mode==='lern'&&P.length?D:'';", "if(full)x=(mode==='lern'&&P.length?D+' · ':'')+(en?'tap picture: back':'Bild tippen: zurück');")

CSS = '''
/* fullscreen-tap */
.anapop.full{inset:0!important;padding:0!important;--ph:100dvh;background:#111!important;-webkit-backdrop-filter:none;backdrop-filter:none;z-index:6000}
.anapop.full .tlcard{background:#111;border-radius:0;max-width:none;width:100%;height:100%}
.anapop.full .tltop,.anapop.full .anaBar{display:none}
.anapop.full .anaBody{padding:0;gap:0;position:relative}
.anapop.full .anaStage{background:#111;outline:0}
.anapop.full .anaScroll{display:flex;background:#111;cursor:zoom-out}
.anapop.full .anaFig{margin:auto;flex:none}
.anapop.full .anaPanel{position:absolute;left:0;right:0;bottom:0;z-index:7;min-height:0;max-height:40vh;overflow-y:auto;background:#fff;border-top:1px dotted #b8b8b8;padding:8px 14px calc(env(safe-area-inset-bottom,0px) + 10px);box-shadow:0 -6px 16px rgba(0,0,0,.3)}
.anapop.full.noSel .anaPanel{display:none}
.anapop.full .anaZoom{top:64px}
.anapop.full .aOv{top:env(safe-area-inset-top,0px)}
'''
i = s.index('</style>', s.index('.anapop:not(.full) .anaScroll{cursor:zoom-in}'))
s = s[:i] + CSS + s[i:]
if '--noversion' not in sys.argv:
    s = re.sub(r'(<meta name="app-version" content=")([^"]*)(")', lambda m: m.group(1) + '2026-11-06zzz80' + m.group(3), s, count=1)
open('index.html', 'w', encoding='utf-8').write(s)
print('ok')
