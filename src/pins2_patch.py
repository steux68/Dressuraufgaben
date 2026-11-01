import re
f='index.html'; s=open(f,encoding='utf8').read()
s=s.replace("const w=Math.max(1.2,M.a*.9);","const w=Math.max(.9,M.a*.62);")
s=s.replace("@keyframes pinlit{0%{fill:#bfbfbf}8%{fill:#cdff3e}70%{fill:#cdff3e}100%{fill:#bfbfbf}}","@keyframes pinlit{0%{fill:#fff}8%{fill:#cdff3e}70%{fill:#cdff3e}100%{fill:#fff}}")
s=re.sub(r'/\* pins2 \*/.*?/\* /pins2 \*/\n','',s,flags=re.S)
css='''/* pins2 */
.vier .pin .pb{fill:#fff;stroke:#e30613;stroke-width:.55}
.vier .pin circle{r:8.4px}
.vier .pin text{font-size:12px}
#vgrid line{stroke-width:.55}
@keyframes pinlit{0%{fill:#fff;transform:scale(1)}8%{fill:#ffd400}35%{transform:scale(1.18)}70%{fill:#ffd400;transform:scale(1)}100%{fill:#fff}}
.vier .pin .pb{transform-box:fill-box;transform-origin:center}
.vier .pin .r1,.vier .pin .r2{stroke:#ffd400!important;stroke-width:1.6}
/* /pins2 */
'''
i=s.rfind('</style>'); s=s[:i]+css+s[i:]
open(f,'w',encoding='utf8').write(s)
t=open('src/trails.js',encoding='utf8').read().replace("const w=Math.max(1.2,M.a*.9);","const w=Math.max(.9,M.a*.62);")
open('src/trails.js','w',encoding='utf8').write(t)
v=open('src/vier_gross_patch.py',encoding='utf8').read().replace('100vh - 350px','100vh - 305px')
open('src/vier_gross_patch.py','w',encoding='utf8').write(v)
