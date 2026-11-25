# Hilfen "Lernen" im Stil des Anatomie-Popups: Kopfzeile Gruppe · Zaehler, Pfeile (W/E-Kreis), Hinweiszeile, Titel/Text/Datenliste. 25.11.2026
import re,sys
s=open('index.html',encoding='utf-8').read()
if 'hilfen-ana-css' in s: sys.exit('schon angewendet')
a=s.index("const WSVG='<svg class=\"ar\"")
WS=s[a:s.index('\n',a)]; ES=s[s.index("const ESVG=",a):s.index('\n',s.index("const ESVG=",a))]
WS=WS.replace('const WSVG=','const HLAW='); ES=ES.replace('const ESVG=','const HLAE=')
# 1) Lernen-Markup
i=s.index("o+='<div class=\"hiCard\"><p class=\"hiN\">'+p.n+'</p>"); j=s.index("</div></div>';",i)+len("</div></div>';")
NEW="""o+='<div class="hiCard hiAna"><div class="tltop"><span class="tlk"><b>'+p.g+'</b> · '+(hls.i+1)+' / '+L.length+'</span></div><div class="hiStage"><button type="button" class="tlar pw" data-a="p" aria-label="Zurück">'+HLAW+'</button>'+hlPic(p,150,265)+'<button type="button" class="tlar pe" data-a="n" aria-label="Weiter">'+HLAE+'</button></div><p class="aTip">Pfeile tippen oder seitlich wischen</p><div class="hiPanel anaPanel">'+hlPanel(p,hls.i,L.length)+'</div></div>';"""
s=s[:i]+NEW+s[j:]
# 2) Panel + Konstanten vor hlRender
FN=WS+"\n"+ES+"""
function hlPanel(p,k,n){return '<p class="nm">'+p.n+'</p><p class="ds">'+p.t+'</p><p class="ds"><b>Gut zu wissen:</b> '+p.w+'</p><dl class="anaDl"><dt>Zügel</dt><dd>'+HLZ[p.h]+'</dd><dt>Sitz</dt><dd>'+HLS[p.s]+'</dd><dt>Schenkel</dt><dd>'+HLL[p.l]+'</dd><dt>Gruppe</dt><dd>'+p.g+'</dd><dt>Zeichen</dt><dd>'+(k+1)+' / '+n+'</dd></dl>';}
"""
s=s.replace("function hlRender(){",FN+"function hlRender(){",1)
# 3) hlLock neu
i=s.index("function hlLock(){"); j=s.index("\n}\n",i)+3
LOCK="""function hlLock(){
 const root=g('thHi'),pn=root.querySelector('.hiPanel');if(!pn||!root.offsetParent)return;
 const keep=pn.innerHTML;pn.style.minHeight='';let m=0;
 HL.forEach(x=>{pn.innerHTML=hlPanel(x,0,HL.length);m=Math.max(m,pn.offsetHeight);});
 pn.innerHTML=keep;pn.style.minHeight=m+'px';
}
"""
s=s[:i]+LOCK+s[j:]
CSS='''<style id="hilfen-ana-css">
#thHi .hiAna{background:#fff;padding:0 4px 10px}
#thHi .hiAna .tltop{display:grid;grid-template-columns:1fr auto 1fr;padding:4px 4px 3px;min-height:0}
#thHi .hiAna .tlk{grid-column:2;font-size:12px;letter-spacing:.06em;color:#555}
#thHi .hiAna .tlk b{color:#e30613;font-weight:400}
#thHi .hiStage{position:relative;display:flex;justify-content:center;align-items:center;padding:14px 0 8px}
#thHi .hiStage .tlar{width:26px;height:26px;margin-top:-13px;background:rgba(255,255,255,.6);border-radius:50%!important}
#thHi .hiStage .tlar svg{width:22px;height:22px}
#thHi .hiAna .aTip{margin:0;text-align:center;font-size:12px;line-height:18px;color:#8a8a86;letter-spacing:.02em}
#thHi .hiAna .hiPanel{padding:8px 4px 0;min-height:0}
#thHi .hiAna .nm{margin:0;color:#e30613;text-transform:uppercase;font-weight:700;font-size:16px;line-height:1.15;letter-spacing:.01em}
#thHi .hiAna .ds{margin:5px 0 0;font-size:14px;line-height:1.4;color:#222}
#thHi .hiAna .anaDl{margin-top:10px}
</style>
'''
i=s.rindex('</head>'); s=s[:i]+CSS+s[i:]
s=re.sub(r'(<meta name="app-version" content=")[^"]*"',r'\g<1>2026-11-25b"',s,count=1)
open('index.html','w',encoding='utf-8').write(s)
