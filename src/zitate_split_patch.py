#!/usr/bin/env python3
"""Geschichte und Zitate werden zwei Abschnitte (Steuart, 13 Nov 2026): 01 Dressuraufgaben, 02 Pferdewissen,
03 Geschichte, 04 Zitate, 05 Materialien, 06 Links. Dazu: kein gepunkteter Strich mehr links vom senkrechten
Urheberhinweis (kam von der allgemeinen .copy-Regel: border-top + gepunkteter Hintergrund, gedreht = links).
Aufruf im Repo-Hauptordner: python3 src/zitate_split_patch.py"""
import re, sys
p = "index.html"
s = open(p, encoding="utf-8").read()
if "/* zitate-split */" in s:
    sys.exit("already patched")

def rep(old, new, count=1):
    global s
    if s.count(old) < 1:
        sys.exit("Anker nicht gefunden: " + old[:70])
    s = s.replace(old, new) if count == 0 else s.replace(old, new, count)

# 1. Abschnittsliste
rep("const SECS=[['a','Dressuraufgaben'],['w','Pferdewissen'],['g','Geschichte & Zitate'],['m','Materialien'],['x','Links']];",
    "const SECS=[['a','Dressuraufgaben'],['w','Pferdewissen'],['g','Geschichte'],['z','Zitate'],['m','Materialien'],['x','Links']];")

# 2. Inhalt: zwei Seiten statt einer
old = re.search(r" /\* 03 Geschichte & Zitate \*/.*?PG\.appendChild\(pg\);\n", s, re.S)
if not old:
    sys.exit("PG-Block nicht gefunden")
new = (" /* 03 Geschichte, 04 Zitate */\n"
 " const PG=mk('p-g','hsec');if(window.THEO_LISTS)THEO_LISTS();\n"
 " const h1=document.createElement('p');h1.className='wsec';h1.textContent='Kleine Geschichte des Pferdes';\n"
 " const pg=document.createElement('div');pg.id='theo2';pg.append(h1,$('thHl'));PG.appendChild(pg);\n"
 " const PZ=mk('p-z','hsec');const pz=document.createElement('div');pz.id='theo3';pz.append($('thZl'));PZ.appendChild(pz);\n")
s = s[:old.start()] + new + s[old.end():]
rep("const PAGES=[PA,PW,PG,PM,PX];", "const PAGES=[PA,PW,PG,PZ,PM,PX];")

# 3. Nummern der Sprungziele
rep("const IDX={mat:3,gesch:2,xyz:4};", "const IDX={mat:4,gesch:2,zit:3,xyz:5};")
rep("window.openMat=()=>toHome(3);window.openGesch=()=>toHome(2);window.openXyz=()=>toHome(4);",
    "window.openMat=()=>toHome(4);window.openGesch=()=>toHome(2);window.openZit=()=>toHome(3);window.openXyz=()=>toHome(5);")
rep("window.xyzRaw=()=>{_show('home');goSec(4);};", "window.xyzRaw=()=>{_show('home');goSec(5);};")
rep("const m={'#material':3,'#geschichte':2,'#xyz':4,'#links':4};", "const m={'#material':4,'#geschichte':2,'#zitate':3,'#xyz':5,'#links':5};")
rep("const ANCH={'#material':3,'#geschichte':2,'#xyz':4,'#links':4}", "const ANCH={'#material':4,'#geschichte':2,'#zitate':3,'#xyz':5,'#links':5}")
rep("v==='gesch'?'Geschichte & Zitate'", "v==='gesch'?'Geschichte'")

# 4. CSS: #theo2-Regeln auch für #theo3 (Zitate-Seite), kein Strich am Urheberhinweis
a = s.index("#theo2 .wsec{margin:12px 0 4px")
b = s.index("</style>", a)
blk = re.sub(r"#theo2 ([^,{]+)", lambda m: "#theo2 " + m.group(1) + ",#theo3 " + m.group(1), s[a:b])
s = s[:a] + blk + s[b:]
CSS = ("\n/* zitate-split */\n"
       "footer.copy.cv{background-image:none!important;border-top:0!important;padding-top:0!important}\n")
i = s.rindex("</style>"); s = s[:i] + CSS + s[i:]

# 5. Farbwechsel der Leisten: sechs Farben
rep("b.setAttribute('data-pc',i%5)", "b.setAttribute('data-pc',i%6)")
rep('body.introOn .hb[data-pc="4"]{--pc:#ece2f8;animation-delay:-2.8s}',
    'body.introOn .hb[data-pc="4"]{--pc:#ece2f8;animation-delay:-2.8s} body.introOn .hb[data-pc="5"]{--pc:#dff3ea;animation-delay:-3.5s}')

m = re.search(r'(name="app-version" content="(\d{4}-\d\d-\d\d))([a-z]*)(")', s)
if m:
    nxt = chr(ord(m.group(3)[-1]) + 1) if m.group(3) else "a"
    s = s.replace(m.group(0), m.group(1) + (m.group(3)[:-1] + nxt if m.group(3) else nxt) + m.group(4), 1)
open(p, "w", encoding="utf-8").write(s)
print("OK – Geschichte und Zitate getrennt, app-version erhöht")
