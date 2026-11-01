import re
f='index.html'; s=open(f,encoding='utf8').read()
s=re.sub(r'<g id="vgrid">.*?</g>','',s,count=1,flags=re.S)
s=re.sub(r'<circle class="an vdot"[^>]*/>','',s)
grid='<g id="vgrid">'+''.join('<line x1="%d" y1="30" x2="%d" y2="270" stroke="#dcdcdc" stroke-width="1"/>'%(x,x) for x in (70,100,130))+''.join('<line x1="40" y1="%d" x2="160" y2="%d" stroke="#dcdcdc" stroke-width="1"/>'%(y,y) for y in range(60,270,30) if y!=150)+'</g>'
dots=''.join('<circle class="an vdot" cx="%d" cy="%d" r="3.6" fill="#111"/>'%(x,y) for x in (40,160) for y in (90,210))
i=s.index('<svg class="vier"'); j=s.index('<line class="an"',i)
s=s[:j]+grid+s[j:]
k=s.index('<g class="an pin"',i)
s=s[:k]+dots+s[k:]
# Viereck-Bereich (vier.js) ebenfalls
v=open('src/vier.js',encoding='utf8').read()
if 'viGit' not in v:
    v=v.replace("let h='<rect","let h='<g class=\"viGit\">';for(let x=X0+30;x<X1;x+=30)h+='<line x1=\"'+x+'\" y1=\"'+Y0+'\" x2=\"'+x+'\" y2=\"'+Y1+'\" stroke=\"#dcdcdc\"/>';for(let y=Y0+30;y<Y1;y+=30)if(y!==(Y0+Y1)/2)h+='<line x1=\"'+X0+'\" y1=\"'+y+'\" x2=\"'+X1+'\" y2=\"'+y+'\" stroke=\"#dcdcdc\"/>';h+='</g><rect")
    v=v.replace(" s.innerHTML=h;"," [Y0+60,Y1-60].forEach(y=>[X0,X1].forEach(x=>{h+='<circle cx=\"'+x+'\" cy=\"'+y+'\" r=\"4\" fill=\"#111\"/>'}));\n s.innerHTML=h;")
    open('src/vier.js','w',encoding='utf8').write(v)
open(f,'w',encoding='utf8').write(s)
