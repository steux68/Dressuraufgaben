f='index.html'; s=open(f,encoding='utf8').read()
if 'img/pferde/p4.jpg' not in s:
    old="Rasse und Größe sind noch Vermutungen nach dem Foto.'}\n];"
    assert old in s
    add="""Rasse und Größe sind noch Vermutungen nach dem Foto.'},
 {n:'Name folgt',foto:'img/pferde/p4.jpg',m:'Dunkelbraun oder Rappe · Rasse noch offen · im Training',w:'folgt',e:'Trägt eine dunkle Ohrenhaube (Fliegenhaube) und ein Fliegennetz an der Trense.',t:'Fellfarbe und Rasse sind noch zu klären.'},
 {n:'Name folgt',foto:'img/pferde/p6.jpg',m:'Fuchs · Rasse und Größe noch offen',w:'folgt',e:'Heller Fleck auf der Stirn; legt den Kopf gern auf das Gatter des Auslaufs.',t:'Rasse und Größe sind noch zu klären.'},
 {n:'Name folgt',foto:'img/pferde/p7.jpg',m:'Fuchs mit breiter Blesse · Rasse noch offen',w:'folgt',e:'Breite weiße Blesse, die bis zur Nase reicht; trägt ein lila Halfter.',t:'Rasse und Größe sind noch zu klären.'}
];"""
    s=s.replace(old,add,1)
open(f,'w',encoding='utf8').write(s)
