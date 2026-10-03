import json, os, sys
from PIL import Image, ImageDraw, ImageFont, ImageOps, ImageFilter
W,H=1080,1350
NAVY=(15,27,45); BLUE=(53,182,243); WHITE=(255,255,255); GREY=(190,200,215)
FONT='brand/Montserrat.ttf'
def font(size, var='ExtraBold'):
    f=ImageFont.truetype(FONT,size)
    try: f.set_variation_by_name(var)
    except Exception as e: pass
    return f
def fit_text(draw,text,maxw,size,var,minsize=30):
    while size>minsize:
        f=font(size,var)
        if draw.textlength(text,font=f)<=maxw: return f
        size-=2
    return font(minsize,var)
def tracked(draw,xy,text,f,fill,spacing,anchor='l'):
    # letterspaced text; anchor l/r/m by x
    widths=[draw.textlength(ch,font=f) for ch in text]
    total=sum(widths)+spacing*(len(text)-1)
    x,y=xy
    if anchor=='r': x-=total
    elif anchor=='m': x-=total/2
    for ch,w in zip(text,widths):
        draw.text((x,y),ch,font=f,fill=fill); x+=w+spacing
    return total
def load_photo(idx, focus=(0.5,0.5), zoom=1.0, blur=None):
    im=Image.open(f'drive/full/{idx:04d}.jpg'); im=ImageOps.exif_transpose(im).convert('RGB')
    if im.width>2400: im=im.resize((2400,int(im.height*2400/im.width)),Image.LANCZOS)
    for b in (blur or []):
        x0,y0,x1,y1=[int(v*s) for v,s in zip(b,(im.width,im.height,im.width,im.height))]
        reg=im.crop((x0,y0,x1,y1)).filter(ImageFilter.GaussianBlur(max(8,(x1-x0)//6)))
        im.paste(reg,(x0,y0))
    return im, focus, zoom
def crop_to(im,box_w,box_h,focus=(0.5,0.5),zoom=1.0):
    iw,ih=im.size; scale=max(box_w/iw,box_h/ih)*zoom
    nw,nh=int(iw*scale)+1,int(ih*scale)+1
    im=im.resize((nw,nh),Image.LANCZOS)
    cx,cy=focus[0]*nw,focus[1]*nh
    x0=int(min(max(cx-box_w/2,0),nw-box_w)); y0=int(min(max(cy-box_h/2,0),nh-box_h))
    return im.crop((x0,y0,x0+box_w,y0+box_h))
def panel_blur(panel,boxes):
    for b in (boxes or []):
        x0,y0,x1,y1=[int(v*s) for v,s in zip(b,(panel.width,panel.height,panel.width,panel.height))]
        x0,y0=max(0,x0),max(0,y0); x1,y1=min(panel.width,x1),min(panel.height,y1)
        if x1<=x0 or y1<=y0: continue
        reg=panel.crop((x0,y0,x1,y1)).resize((max(1,(x1-x0)//28),max(1,(y1-y0)//28)),Image.BILINEAR).resize((x1-x0,y1-y0),Image.BILINEAR).filter(ImageFilter.GaussianBlur(6))
        panel.paste(reg,(x0,y0))
    return panel
def rounded(draw,box,r,fill,outline=None,width=0):
    draw.rounded_rectangle(box,radius=r,fill=fill,outline=outline,width=width)
def render(ad,out,code=None):
    img=Image.new('RGB',(W,H),NAVY); d=ImageDraw.Draw(img)
    # logo
    logo=Image.open('brand/logo_rgba.png').convert('RGBA'); lh=118; logo=logo.resize((int(logo.width*lh/logo.height),lh),Image.LANCZOS)
    img.paste(logo,(48,34),logo)
    tracked(d,(W-48,74),ad.get('tag','MOBILE  •  WARWICKSHIRE'),font(24,'Medium'),GREY,5,anchor='r')
    # headline
    base=ad.get('h1size',84)
    while True:
        y=168
        f1=fit_text(d,ad['h1'],W-96,base,'ExtraBold'); y+=int(f1.size*1.06)
        f2=fit_text(d,ad['h2'],W-96,min(base,f1.size),'ExtraBold') if ad.get('h2') else None
        if f2: y+=int(f2.size*1.06)
        fs=fit_text(d,ad['sub'],W-96,min(44,base//2+2),'SemiBold') if ad.get('sub') else None
        if fs: y+=int(fs.size*1.25)+8
        if y+14<=430 or base<=60: break
        base-=2
    y=168
    d.text((48,y),ad['h1'],font=f1,fill=WHITE); y+=int(f1.size*1.06)
    if f2: d.text((48,y),ad['h2'],font=f2,fill=BLUE); y+=int(f2.size*1.06)
    if fs: d.text((W/2,y+4),ad['sub'],font=fs,fill=WHITE,anchor='ma'); y+=int(fs.size*1.25)+8
    # photo panel
    top=430; bottom=975
    ph=bottom-top
    inset=ad.get('inset')
    if inset:
        main_w=int(W*0.70); im,fo,zo=load_photo(ad['img'],tuple(ad.get('focus',(0.5,0.5))),ad.get('zoom',1.0),ad.get('blur'))
        pan=crop_to(im,main_w,ph,fo,zo)
        if code and os.path.exists(f'ads2/panelblur_{code}.png'):
            pb=Image.open(f'ads2/panelblur_{code}.png').convert('RGB'); assert pb.size==pan.size,(code,pb.size,pan.size); pan=pb
        img.paste(pan,(0,top))
        ix0=main_w+14; iw=W-ix0-20; ih=ph-28
        im2,fo2,zo2=load_photo(inset['img'],tuple(inset.get('focus',(0.5,0.5))),inset.get('zoom',1.0),inset.get('blur'))
        ins=crop_to(im2,iw-8,ih-8,fo2,zo2)
        rounded(d,(ix0,top+14,ix0+iw,top+14+ih),10,fill=WHITE)
        img.paste(ins,(ix0+4,top+18))
        d=ImageDraw.Draw(img)
        # caption
        cap=inset.get('caption','REAL RESULT'); fc=font(20,'Bold')
        cw=d.textlength(cap,font=fc)+36
        rounded(d,(ix0+iw/2-cw/2,top+14+ih-58,ix0+iw/2+cw/2,top+14+ih-14),8,fill=(20,30,48))
        d.text((ix0+iw/2,top+14+ih-36),cap,font=fc,fill=WHITE,anchor='mm')
    else:
        im,fo,zo=load_photo(ad['img'],tuple(ad.get('focus',(0.5,0.5))),ad.get('zoom',1.0),ad.get('blur'))
        pan=crop_to(im,W,ph,fo,zo)
        if code and os.path.exists(f'ads2/panelblur_{code}.png'):
            pb=Image.open(f'ads2/panelblur_{code}.png').convert('RGB'); assert pb.size==pan.size,(code,pb.size,pan.size); pan=pb
        img.paste(pan,(0,top)); d=ImageDraw.Draw(img)
    # badge
    if ad.get('badge'):
        b1,b2=ad['badge']
        fb1=font(60,'ExtraBold'); fb2=font(24,'Bold')
        bw=int(max(d.textlength(b1,font=fb1),d.textlength(b2,font=fb2)))+56
        bx,by=28,top+22
        rounded(d,(bx,by,bx+bw,by+124),14,fill=(15,27,45,230),outline=WHITE,width=3)
        d.text((bx+bw/2,by+44),b1,font=fb1,fill=BLUE,anchor='mm')
        d.text((bx+bw/2,by+98),b2,font=fb2,fill=WHITE,anchor='mm')
    # footer
    fy=bottom+34
    if ad.get('kicker'):
        tracked(d,(W/2,fy),ad['kicker'],font(26,'SemiBold'),WHITE,6,anchor='m'); fy+=52
    pm=ad.get('price')  # dict
    if pm:
        if pm['mode']=='wasnow':
            fw=font(50,'SemiBold'); fn=font(50,'SemiBold'); fp=font(92,'ExtraBold')
            was=f"Was from "; wasp=pm['was']; now="Now from "; nowp=pm['now']
            w1=d.textlength(was,font=fw); w2=d.textlength(wasp,font=fw); w3=d.textlength(now,font=fn); w4=d.textlength(nowp,font=fp)
            gap=70; total=w1+w2+gap+w3+w4; x=(W-total)/2; cy=fy+48
            d.text((x,cy),was,font=fw,fill=WHITE,anchor='lm'); x+=w1
            d.text((x,cy),wasp,font=fw,fill=WHITE,anchor='lm'); d.line((x-2,cy-2,x+w2+2,cy-10),fill=(235,70,70),width=6); x+=w2+gap/2
            d.line((x,cy-34,x,cy+34),fill=(90,105,130),width=2); x+=gap/2
            d.text((x,cy),now,font=fn,fill=WHITE,anchor='lm'); x+=w3
            d.text((x,cy),nowp,font=fp,fill=WHITE,anchor='lm'); fy+=104
        elif pm['mode']=='from':
            fn=font(50,'SemiBold'); fp=font(92,'ExtraBold'); lab=pm.get('label','From ')
            w3=d.textlength(lab,font=fn); w4=d.textlength(pm['now'],font=fp); x=(W-w3-w4)/2; cy=fy+48
            d.text((x,cy),lab,font=fn,fill=WHITE,anchor='lm'); d.text((x+w3,cy),pm['now'],font=fp,fill=WHITE,anchor='lm'); fy+=104
        elif pm['mode']=='text':
            ft=fit_text(d,pm['now'],W-120,64,'ExtraBold'); d.text((W/2,fy+48),pm['now'],font=ft,fill=WHITE,anchor='mm'); fy+=104
    # CTA
    cta=ad.get('cta','GET MY QUOTE'); fcta=font(46,'ExtraBold')
    rounded(d,(40,fy+6,W-40,fy+96),16,fill=BLUE); d.text((W/2,fy+51),cta,font=fcta,fill=WHITE,anchor='mm'); fy+=112
    fine=ad.get('fine','Price varies by vehicle size and condition.')
    ff=font(21,'Medium')
    lines=[]
    for para in fine.split('\n'):
        cur=''
        for w in para.split():
            t=(cur+' '+w).strip()
            if d.textlength(t,font=ff)>W-120 and cur: lines.append(cur); cur=w
            else: cur=t
        if cur: lines.append(cur)
    for i,line in enumerate(lines[:2]): d.text((W/2,fy+4+i*28),line,font=ff,fill=GREY,anchor='ma')
    img.save(out,quality=92)
if __name__=='__main__':
    spec=json.load(open(sys.argv[1])); os.makedirs('ads2/out',exist_ok=True)
    only=sys.argv[2:] 
    for c in spec['campaigns']:
        for a in c['ads']:
            if only and a['code'] not in only: continue
            render(a['design'],f"ads2/out/{a['code']}.jpg",a['code']); print('rendered',a['code'])
