import re
f='index.html'; s=open(f,encoding='utf8').read()
new="""const P=[
 {n:'Name folgt',foto:'img/pferde/p1.jpg',m:'Fuchsschecke · vermutlich Shetlandpony · klein',w:'folgt',e:'Breite weiße Blesse, lange rotbraune Mähne (hier zum Zopf geflochten).',t:'Rasse und Größe sind noch Vermutungen nach dem Foto.'},
 {n:'Name folgt',foto:'img/pferde/p2.jpg',m:'Flohschimmel (grau mit dunklen Sprenkeln) · Rasse noch offen',w:'folgt',e:'Dunkle Sprenkel im ganzen Fell; trägt ein grünes Halfter mit Fellpolster.',t:'Rasse und Größe sind noch zu klären.'},
 {n:'Name folgt',foto:'img/pferde/p3.jpg',m:'Schimmel · vermutlich Araber-Typ · Größe noch offen',w:'folgt',e:'Feiner Kopf mit dunklen, ausdrucksvollen Augen; die Mähne ist grau.',t:'Rasse und Größe sind noch Vermutungen nach dem Foto.'}
];"""
a=s.index('const P=[\n {'); b=s.index('];',a)+2
s=s[:a]+new+s[b:]
css='''/* pferde-css */
#theo .hp,.hp{display:block}
#theo .hp .ph,.hp .ph{width:100%;height:auto;aspect-ratio:4/3;margin-bottom:8px;border-style:solid}
#theo .hp .nm{font-size:1.1rem;font-weight:700}
/* /pferde-css */
'''
s=re.sub(r'/\* pferde-css \*/.*?/\* /pferde-css \*/\n','',s,flags=re.S)
i=s.rfind('</style>'); s=s[:i]+css+s[i:]
s=re.sub(r'(<meta name="app-version" content=")[^"]*"',r'\g<1>2026-11-01zzz2"',s,count=1)
open(f,'w',encoding='utf8').write(s)
