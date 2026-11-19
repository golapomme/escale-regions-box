import json, base64, os
s=open('src/template.html').read()
paths=json.load(open('src/map-paths.json'))
def uri(p,mime): return f"data:{mime};base64,"+base64.b64encode(open(p,'rb').read()).decode()
pics={os.path.splitext(f)[0]:uri('src/img/'+f,'image/webp') for f in sorted(os.listdir('src/img')) if f.endswith('.webp')}
s=s.replace('__PICS__',json.dumps(pics,separators=(',',':')))
s=s.replace('__MAPDATA__',json.dumps({'w':620,'h':598,'regions':paths},separators=(',',':')))
s=s.replace('__LOGO__',uri('src/logo.png','image/png')).replace('__HERO__',uri('src/hero.jpg','image/jpeg')).replace('__BOX__',uri('src/box.jpg','image/jpeg'))
open('index.html','w').write(s); print(len(s)//1024,'KB')
