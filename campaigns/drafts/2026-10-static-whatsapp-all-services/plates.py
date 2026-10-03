import cv2, numpy as np
from PIL import Image
def find_plate(panel, box, only=None):
    """panel: PIL RGB; box: fractional approx region. Returns 4-point polygon (pixels) or None."""
    W,H=panel.size
    x0,y0,x1,y1=[int(v*s) for v,s in zip(box,(W,H,W,H))]
    x0,y0=max(0,x0),max(0,y0); x1,y1=min(W,x1),min(H,y1)
    roi=np.array(panel.crop((x0,y0,x1,y1)))[:,:,::-1]
    hsv=cv2.cvtColor(roi,cv2.COLOR_BGR2HSV)
    yellow=cv2.inRange(hsv,(12,70,110),(40,255,255))
    white=cv2.inRange(hsv,(0,0,165),(180,70,255))
    white2=cv2.inRange(hsv,(0,0,115),(180,95,255))
    yellow2=cv2.inRange(hsv,(10,50,80),(45,255,255))
    best=None
    for name,m in (('yellow',yellow),('white',white),('white2',white2),('yellow2',yellow2)):
        if only and not name.startswith(only): continue
        if best is not None and name.endswith('2'): break
        m=cv2.morphologyEx(m,cv2.MORPH_CLOSE,np.ones((7,7),np.uint8))
        m=cv2.morphologyEx(m,cv2.MORPH_OPEN,np.ones((3,3),np.uint8))
        cnts,_=cv2.findContours(m,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        for c in cnts:
            a=cv2.contourArea(c)
            if a<0.025*roi.shape[0]*roi.shape[1]: continue
            r=cv2.minAreaRect(c); (cx,cy),(rw,rh),ang=r
            if rw==0 or rh==0: continue
            ar=max(rw,rh)/min(rw,rh)
            if ar<1.4 or ar>8: continue
            fill=a/(rw*rh)
            if fill<0.6: continue
            score=a*fill
            if best is None or score>best[0]: best=(score,r,name)
    if best is None: return None
    (cx,cy),(rw,rh),ang=best[1]
    rw*=1.10; rh*=1.18
    pts=cv2.boxPoints(((cx,cy),(rw,rh),ang))
    pts[:,0]+=x0; pts[:,1]+=y0
    return pts.astype(np.int32), best[2]
def apply(panel, polys):
    arr=np.array(panel)[:,:,::-1].copy()
    for pts in polys:
        mask=np.zeros(arr.shape[:2],np.uint8); cv2.fillConvexPoly(mask,pts,255)
        x,y,w,h=cv2.boundingRect(pts)
        x=max(0,x); y=max(0,y); w=min(w,arr.shape[1]-x); h=min(h,arr.shape[0]-y)
        if w<2 or h<2: continue
        reg=arr[y:y+h,x:x+w]
        small=cv2.resize(reg,(max(2,w//18),max(2,h//18)),interpolation=cv2.INTER_AREA)
        pix=cv2.resize(small,(w,h),interpolation=cv2.INTER_LINEAR)
        pix=cv2.GaussianBlur(pix,(0,0),max(2,w/40))
        m=mask[y:y+h,x:x+w].astype(np.float32)/255.0
        m=cv2.GaussianBlur(m,(0,0),1.5)[:,:,None]
        arr[y:y+h,x:x+w]=(pix*m+reg*(1-m)).astype(np.uint8)
    return Image.fromarray(arr[:,:,::-1])

def find_plate_text(panel, box):
    """Locate a plate by its characters: dark glyph blobs on a light background inside a loose region. Returns quad or None."""
    W,H=panel.size
    x0,y0,x1,y1=[int(v*s) for v,s in zip(box,(W,H,W,H))]
    roi=np.array(panel.crop((x0,y0,x1,y1)))[:,:,::-1]
    g=cv2.cvtColor(roi,cv2.COLOR_BGR2GRAY)
    th=cv2.adaptiveThreshold(g,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,21,10)
    n,lab,stats,_=cv2.connectedComponentsWithStats(th)
    glyphs=[]
    for s in stats[1:]:
        x,y,w,h,a=s
        if 8<=h<=70 and 2<=w<=50 and 0.15<=w/h<=1.1 and a>20:
            # light background around?
            glyphs.append((x,y,w,h))
    if len(glyphs)<4: return None
    # cluster glyphs by similar height and y
    best=None
    for gy in glyphs:
        x,y,w,h=gy
        grp=[g2 for g2 in glyphs if abs(g2[1]+g2[3]/2-(y+h/2))<h*0.6 and 0.6<g2[3]/h<1.6]
        if len(grp)>=4:
            xs=[g2[0] for g2 in grp]+[g2[0]+g2[2] for g2 in grp]; ys=[g2[1] for g2 in grp]+[g2[1]+g2[3] for g2 in grp]
            width=max(xs)-min(xs); height=max(ys)-min(ys)
            if 2.0<width/max(height,1)<9 and (best is None or len(grp)>best[0]): best=(len(grp),min(xs),min(ys),max(xs),max(ys))
    if best is None: return None
    _,bx0,by0,bx1,by1=best
    padx=int((bx1-bx0)*0.12)+6; pady=int((by1-by0)*0.35)+6
    pts=np.array([[bx0-padx,by0-pady],[bx1+padx,by0-pady],[bx1+padx,by1+pady],[bx0-padx,by1+pady]],dtype=np.int32)
    pts[:,0]+=x0; pts[:,1]+=y0
    return pts
