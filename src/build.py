import json, base64, os
D=''
s=open('src/template.html').read()
paths=json.load(open('src/map-paths.json'))
def uri(p,mime): return f"data:{mime};base64,"+base64.b64encode(open(D+p,'rb').read()).decode()
pics={os.path.splitext(f)[0]:uri('src/img/'+f,'image/webp') for f in sorted(os.listdir('src/img')) if f.endswith('.webp')}
faces=[('Poppins',400,'normal','poppins-latin-400-normal'),('Poppins',400,'italic','poppins-latin-400-italic'),('Poppins',500,'normal','poppins-latin-500-normal'),('Poppins',500,'italic','poppins-latin-500-italic'),('Poppins',600,'normal','poppins-latin-600-normal'),('Poppins',700,'normal','poppins-latin-700-normal'),('Caveat',500,'normal','caveat-latin-500-normal'),('Caveat',700,'normal','caveat-latin-700-normal'),('Playfair Display',700,'normal','playfair-display-latin-700-normal'),('Playfair Display',400,'italic','playfair-display-latin-400-italic'),('Playfair Display',700,'italic','playfair-display-latin-700-italic')]
ff=''.join(f"@font-face{{font-family:'{n}';font-weight:{w};font-style:{st};font-display:swap;src:url({uri('src/fonts/'+f+'.woff2','font/woff2')}) format('woff2')}}\n" for n,w,st,f in faces)
s=s.replace('__FONTFACES__',ff)
s=s.replace('__PICS__',json.dumps(pics,separators=(',',':')))
s=s.replace('__MAPDATA__',json.dumps({'w':620,'h':598,'regions':paths},separators=(',',':')))
s=s.replace('__LOGO__',uri('src/logo.png','image/png')).replace('__HERO__',uri('src/hero.jpg','image/jpeg')).replace('__BOX__',uri('src/box.jpg','image/jpeg'))
open('index.html','w').write(s); print(len(s)//1024,'KB')
