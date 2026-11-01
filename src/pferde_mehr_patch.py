f='index.html'; s=open(f,encoding='utf8').read()
if 'img/pferde/p4.jpg' not in s:
    old="Rasse und Größe sind noch Vermutungen nach dem Foto.'}\n];"
    assert old in s
    add="""Rasse und Größe sind noch Vermutungen nach dem Foto.'},
 {n:'Name folgt',foto:'img/pferde/p4.jpg',m:'Dunkelbraun oder Rappe · Rasse noch offen · im Training',w:'folgt',e:'Trägt eine dunkle Ohrenhaube (Fliegenhaube) und ein Fliegennetz an der Trense.',t:'Fellfarbe und Rasse sind noch zu klären.'},
 {n:'Name folgt',foto:'img/pferde/p5.jpg',m:'Fuchs · Rasse noch offen',w:'folgt',e:'Heller Fleck auf der Stirn, große aufmerksame Ohren und ein neugieriger Blick über die Boxentür.',t:'Rasse und Größe sind noch zu klären.'},
 {n:'Name folgt',foto:'img/pferde/p6.jpg',m:'Fuchs · Rasse und Größe noch offen',w:'folgt',e:'Heller Fleck auf der Stirn; legt den Kopf gern auf das Gatter des Auslaufs.',t:'Es könnte dasselbe Pferd wie auf dem vorigen Foto sein – bitte bestätigen.'}
];"""
    s=s.replace(old,add,1)
open(f,'w',encoding='utf8').write(s)
