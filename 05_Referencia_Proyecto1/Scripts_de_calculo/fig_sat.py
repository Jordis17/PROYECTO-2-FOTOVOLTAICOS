import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from PIL import Image
d="/home/claude/fv/datos/"
A=Image.open(d+"sat_z15.jpg").crop((150,100,650,500))   # 6.03 m/px
B=Image.open(d+"sat_z18_x2.jpg").crop((165,100,640,480)) # 0.377 m/px
plt.rcParams.update({"font.family":"STIXGeneral","mathtext.fontset":"stix","font.size":7})
fig,ax=plt.subplots(1,2,figsize=(3.45,1.65))
def deco(a,im,mpp,L,lab,txt):
    a.imshow(im); a.set_xticks([]); a.set_yticks([])
    w,h=im.size; px=L/mpp; x0=10; y0=h-14
    a.plot([x0,x0+px],[y0,y0],color="w",lw=2.5); a.text(x0+px/2,y0-8,lab,color="w",ha="center",fontsize=6.5,fontweight="bold")
    a.annotate("",xy=(w-18,32),xytext=(w-18,70),arrowprops=dict(arrowstyle="-|>",color="w",lw=1.2))
    a.text(w-18,30,"N",color="w",ha="center",va="bottom",fontsize=7,fontweight="bold")
    a.set_title(txt,fontsize=7,pad=2)
deco(ax[0],A,6.03,500,"500 m","(a) San Isidro de El General")
deco(ax[1],B,0.377,30,"30 m","(b) Edificio")
ax[0].plot(250,200,"o",ms=5,mfc="r",mec="w",mew=1)
fig.tight_layout(pad=0.4,w_pad=0.4)
fig.savefig("/home/claude/fv/informe/figuras/ubicacion_satelital.pdf",dpi=300)
fig.savefig("/home/claude/fv/informe/figuras/ubicacion_satelital.png",dpi=250)
