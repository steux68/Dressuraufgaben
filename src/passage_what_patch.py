#!/usr/bin/env python3
"""Titelseite: kleiner Link "Was heisst Passage?" unter dem Untertitel, oeffnet eine Karte mit Erklaerung
und Beispiel-Link (idempotent). Aufruf im Repo-Ordner: python3 -I src/passage_what_patch.py"""
import re
s=open('index.html',encoding='utf8').read()
if 'id="pwhat-css"' not in s:
    css=('<style id="pwhat-css">#intro .iwhat{margin:10px 0 0;text-align:center}'
         '#pwhatBtn{font:inherit;font-size:.95rem;color:#e30613;background:none;border:0;padding:8px 10px;text-decoration:underline;cursor:pointer}'
         '#pwhat{position:fixed;inset:0;z-index:100000;display:flex;align-items:center;justify-content:center;padding:18px;background:rgba(0,0,0,.45)}'
         '#pwhat[hidden]{display:none}'
         '#pwhat .pwcard{background:#fff!important;box-shadow:none!important;opacity:1!important;color:#111;border-radius:14px;max-width:420px;width:100%;max-height:86vh;overflow:auto;padding:18px 18px 14px;box-sizing:border-box;border:1px solid #bbb}'
         '#pwhat h2{margin:0 0 10px;font-size:1.15rem}#pwhat p{margin:0 0 10px;line-height:1.45;font-size:.98rem}'
         '#pwhat .row{display:flex;gap:10px;flex-wrap:wrap;margin-top:14px}'
         '#pwhat a.ex,#pwhat button{font:inherit;font-size:.95rem;border-radius:8px;padding:10px 14px;cursor:pointer;text-decoration:none;text-align:center}'
         '#pwhat a.ex{border:1px solid #e30613;color:#e30613;background:#fff}#pwhat button{border:0;background:#ececec;color:#111}</style>')
    html=('<div id="pwhat" role="dialog" aria-modal="true" aria-labelledby="pwhatH" hidden><div class="pwcard">'
          '<h2 id="pwhatH">Was heißt „Passage“?</h2>'
          '<p>Die Passage ist ein sehr erhabener, langsamer Trab mit einer langen Schwebephase: Das Pferd hebt die Beine hoch und scheint bei jedem Schritt kurz in der Luft zu stehen, fast wie beim Tanzen. Sie gehört zur Hohen Schule und kommt in den Aufgaben R1–R6 noch nicht vor.</p>'
          '<p>Der Name steht für das Schöne und Hohe in der Dressur. „a–x“ ist der Weg von A nach X, den man in jeder Aufgabe reitet, und „Pax“ ist lateinisch für Frieden.</p>'
          '<div class="row"><a class="ex" href="https://en.wikipedia.org/wiki/Passage_(dressage)" target="_blank" rel="noopener">Beispiel ansehen ›</a>'
          '<button type="button" id="pwhatX">Schließen</button></div></div></div>')
    js=('<script id="pwhat-js">(function(){var d=document.getElementById("pwhat"),b=document.getElementById("pwhatBtn");if(!d||!b)return;'
        'function o(){d.hidden=false;}function c(){d.hidden=true;}b.addEventListener("click",o);'
        'document.getElementById("pwhatX").addEventListener("click",c);d.addEventListener("click",function(e){if(e.target===d)c();});'
        'document.addEventListener("keydown",function(e){if(e.key==="Escape")c();});})();</script>')
    s=s.replace('</head>',css+'</head>',1)
    s=s.replace('Lernen, Spiel, Theorie · Pferdewissen</p>','Lernen, Spiel, Theorie · Pferdewissen</p><p class="iwhat"><button type="button" id="pwhatBtn">Was heißt „Passage“? ›</button></p>',1)
    s=s.replace('</body>',html+js+'</body>',1)
s=re.sub(r'(<meta name="app-version" content=")[^"]*',r'\g<1>2026-11-01zzj',s,count=1)
open('index.html','w',encoding='utf8').write(s)
