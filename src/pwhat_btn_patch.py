# "Was heißt PASSAGE?": Link wird Karten-Button mit rotem P-Logo (wie die Materialien-Zeilen), Ende der Links-Seite. Idempotent. 09.11.2026
import re,sys
s=open('index.html',encoding='utf-8').read()
if 'id="pwbtn-css"' in s: sys.exit('schon angewendet')
old="bt.className='pwlink';bt.textContent='Was heißt PASSAGE? ↗';"
assert s.count(old)==1
new=("bt.className='tile pwtile';bt.innerHTML='<span class=\"code\"><svg viewBox=\"0 0 48 48\" width=\"46\" height=\"46\" aria-hidden=\"true\"><circle cx=\"24\" cy=\"24\" r=\"24\" fill=\"#e30613\"/>"
 "<text x=\"11\" y=\"33\" font-size=\"30\" font-weight=\"700\" fill=\"#fff\" font-family=\"Lato,sans-serif\">P</text><text x=\"21\" y=\"38\" font-size=\"9.5\" font-weight=\"700\" fill=\"#fff\" font-family=\"Lato,sans-serif\">a–x</text></svg></span>"
 "<span><div class=\"nm\">Was heißt PASSAGE?</div><div class=\"ds\">Der Name, die Lektion und wie sie entstand</div></span><span class=\"st soon\">↗</span>';")
s=s.replace(old,new,1)
CSS='''<style id="pwbtn-css">
#xyz .pwtile{width:100%;margin:18px 0 0;font:inherit;color:inherit;cursor:pointer;text-align:left}
#xyz .pwtile .code{background:none!important;width:46px;height:46px;overflow:hidden;display:block!important}
#xyz .pwtile .code svg{display:block}
</style>
'''
i=s.rindex('</style>')+len('</style>')
s=s[:i]+'\n'+CSS+s[i:]
if '--noversion' not in sys.argv:
    s=re.sub(r'(<meta name="app-version" content=")([^"]*)(")',lambda m:m.group(1)+'2026-11-09zzz118'+m.group(3),s,count=1)
open('index.html','w',encoding='utf-8').write(s)
