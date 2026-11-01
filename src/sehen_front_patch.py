# Sehen: neue Karte "Der Kopf von vorn" (eigene Zeichnung: Kopf von vorn, Sehfeld in der Draufsicht darum gelegt)
import re
f='index.html'; s=open(f,encoding='utf8').read()
if 'id="thEf"' not in s:
    head=('<g id="thEf" style="display:none">'
     '<path class="hz" d="M141,104C134,84 138,66 146,58C152,70 154,90 152,106Z"/>'
     '<path class="hz" d="M179,104C186,84 182,66 174,58C168,70 166,90 168,106Z"/>'
     '<path class="hz" d="M140,104C150,98 170,98 180,104C190,112 190,128 187,142C184,160 180,176 178,190C176,204 170,210 160,210C150,210 144,204 142,190C140,176 136,160 133,142C130,128 130,112 140,104Z"/>'
     '<path d="M160,108L160,172" fill="none" stroke="var(--muted)" stroke-width="1.4" stroke-dasharray="1.5 4" stroke-linecap="round"/>'
     '<ellipse class="hz" cx="150" cy="198" rx="3" ry="5" transform="rotate(-15 150 198)"/><ellipse class="hz" cx="170" cy="198" rx="3" ry="5" transform="rotate(15 170 198)"/>'
     '<circle cx="136" cy="126" r="3.2" fill="var(--fg)"/><circle cx="184" cy="126" r="3.2" fill="var(--fg)"/></g>')
    s=s.replace('<g id="thEh"></g>','<g id="thEh"></g>'+head,1)
# Karte einfügen
if "n:'Der Kopf von vorn'" not in s:
    old="{n:'Mit beiden Augen',z:'b'"
    new="{n:'Der Kopf von vorn',z:'f',d:'Hier schaust du dem Pferd ins Gesicht. Die Augen sitzen weit außen am Kopf. Darum sieht jedes Auge zur Seite, und nur ein schmaler Streifen vor der Nase wird von beiden Augen gesehen. Hinter dem Kopf ist der tote Winkel.'},\n "+old
    assert old in s; s=s.replace(old,new,1)
# seeShow: Frontansicht schalten
old="const v=V[vi];seeMark(v.z);g('thEy').textContent='';"
new="const v=V[vi];seeFront(v.z==='f');seeMark(v.z==='f'?'':v.z);g('thEy').textContent='';"
if 'seeFront(v.z' not in s:
    assert old in s; s=s.replace(old,new,1)
    fn="""function seeFront(on){
 g('thEz').setAttribute('transform',on?'rotate(180 160 150)':'');
 g('thEh').style.display=on?'none':'';g('thEf').style.display=on?'':'none';
 const l=g('thEl');l.textContent='';
 (on?[['beide Augen',160,266],['ein Auge',44,150],['ein Auge',276,150],['toter Winkel',160,24]]:[['beide Augen',160,82],['ein Auge',44,150],['ein Auge',276,150],['toter Winkel',160,312]]).forEach(([t,x,y])=>{el('text',{class:'lbl',x,y},l).textContent=t;});
 g('thEye').setAttribute('aria-label',on?'Gesichtsfeld des Pferdes, Kopf von vorn':'Gesichtsfeld des Pferdes von oben');
}
"""
    s=s.replace("function seeShow(){",fn+"function seeShow(){",1)
# Quiz: Frontansicht aus
old="function seeMode(m){vMode=m;"
if 'seeFront(false)' not in s:
    assert old in s; s=s.replace(old,old+"if(m==='q')seeFront(false);",1)
sstr=re.sub(r'(<meta name="app-version" content=")[^"]*"',r'\g<1>2026-11-01zzz28"',s,count=1)
open(f,'w',encoding='utf8').write(sstr)
