"""Generate the illustrated README walkthrough. Requires Pillow."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import math
ROOT = Path(__file__).resolve().parents[1]
FONT = '/System/Library/Fonts/Supplemental/Arial.ttf'
def font(n): return ImageFont.truetype(FONT, n)
frames = []
for i in range(80):
    stage = i // 20
    im = Image.new('RGB', (1000, 600), '#0b1020')
    d = ImageDraw.Draw(im)
    def label(x,y,s,size=18,color='#cbd5e1'): d.text((x,y),s,font=font(size),fill=color)
    label(30,22,'Code Dot',32,'#ffffff')
    label(30,64,'One press. Understand the file. Review with repository context.',18)
    label(730,33,'ILLUSTRATED DEMO',15,'#94a3b8')
    d.rounded_rectangle((25,110,605,440),14,fill='#141d30')
    label(45,126,'CURSOR / VS CODE',14,'#94a3b8')
    d.line((210,160,210,425),fill='#334155',width=1)
    label(42,175,'shop/',18,'#ffffff')
    for j,name in enumerate(['checkout.js','formatPrice.js','checkout.test.js']):
        y=213+j*45
        if j==0 or (stage==2 and j==1):
            d.rounded_rectangle((35,y-6,200,y+27),5,fill='#274969')
        label(45,y,name,16)
    label(232,175,'checkout.js',19,'#7dd3fc')
    for j,line in enumerate(['import { formatPrice }','  from "./formatPrice";','','export function checkout(cart) {','  return formatPrice(','    cart.totalDollars','  );','}']):
        color='#fbbf24' if j==5 and stage>=2 else '#dbeafe'
        label(230,215+j*24,line,16,color)
    d.rounded_rectangle((625,110,975,440),14,fill='#141d30')
    label(647,128,'CODE DOT REVIEW',14,'#7dd3fc')
    if stage==0:
        label(648,184,'1. Open the file',25,'#ffffff')
        label(648,231,'Choose the file you want to',18)
        label(648,260,'understand or debug.',18)
        label(648,317,'Unsaved edits are included.',17,'#a7f3d0')
    elif stage==1:
        label(648,184,'2. Press Code Dot',25,'#ffffff')
        label(648,235,'The active file is captured.',18)
        label(648,279,'Reviewing'+'.'*(1+i%3),20,'#7dd3fc')
    elif stage==2:
        label(648,184,'3. Follow the context',24,'#ffffff')
        label(648,235,'Reads relevant imports,',18)
        label(648,262,'callers, types, and tests.',18)
        label(648,317,'formatPrice expects cents.',18,'#fbbf24')
        label(648,351,'checkout passes dollars.',18,'#fbbf24')
    else:
        label(648,174,'4. Read + listen',25,'#ffffff')
        label(648,219,'Purpose: display a cart total.',17)
        label(648,253,'Bug: inconsistent money units.',17,'#fbbf24')
        label(648,287,'Fix: agree on cents or dollars.',17,'#a7f3d0')
        label(648,321,'Test: $12.34 displays correctly.',17)
        for k in range(30):
            h=5+abs(math.sin(i*.5+k*.7))*22
            d.line((650+k*9,393-h,650+k*9,393+h),fill='#7dd3fc',width=4)
    d.rounded_rectangle((25,457,975,578),15,fill='#10192b')
    d.rounded_rectangle((48,470,138,564),12,fill='#050810',outline='#60a5fa' if stage==1 else '#334155',width=3)
    sprite=Image.open(ROOT/'icon.gif')
    sprite.seek(i % sprite.n_frames)
    icon=sprite.convert('RGB').resize((78,78))
    im.paste(icon,(54,476))
    if stage==1:
        r=40+int(5*math.sin(i*.4))
        d.ellipse((93-r,517-r,93+r,517+r),outline='#7dd3fc',width=3)
    labels=['Select file','Press dot','Read repo context','Explain + speak']
    for k,s in enumerate(labels):
        x=173+k*197
        d.ellipse((x,483,x+23,506),fill='#38bdf8' if k==stage else '#334155')
        label(x+7,486,str(k+1),13,'#ffffff')
        label(x,524,s,16,'#ffffff' if k==stage else '#94a3b8')
    frames.append(im)
ROOT.joinpath('assets').mkdir(exist_ok=True)
frames[0].save(ROOT/'assets/code-dot-walkthrough.gif',save_all=True,append_images=frames[1:],duration=130,loop=0,optimize=True)

