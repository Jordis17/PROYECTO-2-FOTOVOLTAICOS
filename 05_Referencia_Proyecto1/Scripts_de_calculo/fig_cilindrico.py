import sys; sys.path.insert(0,"/home/claude/fv/scripts")
import numpy as np, matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from geometria import sunpos, decl
plt.rcParams.update({"font.family":"STIXGeneral","mathtext.fontset":"stix","font.size":8,"axes.spines.top":False,"axes.spines.right":False})
# días 21 de cada mes
dias={"21 ene":21,"21 feb":52,"21 mar":80,"21 abr":111,"21 may":141,"21 jun":172,"21 jul":202,"21 ago":233,"21 set":264,"21 oct":294,"21 nov":325,"21 dic":355}
# pares con declinación similar comparten curva aprox.; se dibujan las 12 pero se rotulan 7
grupos=[("21 dic",["21 dic"]),("21 ene / 21 nov",["21 ene","21 nov"]),("21 feb / 21 oct",["21 feb","21 oct"]),("21 mar / 21 set",["21 mar","21 set"]),("21 abr / 21 ago",["21 abr","21 ago"]),("21 may / 21 jul",["21 may","21 jul"]),("21 jun",["21 jun"])]
cols=plt.cm.viridis(np.linspace(0.05,0.9,len(grupos)))
fig,ax=plt.subplots(figsize=(7.0,3.3))
ts=np.linspace(5.5,18.5,400)
for (lab,ms),c in zip(grupos,cols):
    for k,m in enumerate(ms):
        h,a=sunpos(dias[m],ts); ok=h>0
        aa=a.copy(); 
        # cortar saltos 0/360
        seg=np.where(np.abs(np.diff(aa))>180)[0]+1
        for s_a,s_h in zip(np.split(aa[ok] if False else aa,seg),np.split(h,seg)):
            mk=s_h>0
            ax.plot(s_a[mk],s_h[mk],color=c,lw=1.3,ls="-" if k==0 else (0,(4,2)),label=lab if k==0 and s_a is not None and (s_a==np.split(aa,seg)[0]).all() else None)
# líneas horarias (tiempo solar)
for t in range(6,19):
    pts=[sunpos(d,t) for d in range(1,366,3)]
    H=np.array([p[0] for p in pts]); A=np.array([p[1] for p in pts]); o=np.argsort(np.array([decl(d) for d in range(1,366,3)]))
    H,A=H[o],A[o]; mk=H>0
    if mk.sum()<2: continue
    A2,H2=A[mk],H[mk]; cut=np.where(np.abs(np.diff(A2))>90)[0]+1
    for sa,sh in zip(np.split(A2,cut),np.split(H2,cut)):
        if len(sa)>1: ax.plot(sa,sh,color="#888",lw=0.6,ls=":")
        if len(sa)>1 and t==12 and sa[0]<90: ax.plot([0,0],[sh.min(),90],color="#888",lw=0.6,ls=":"); ax.plot([360,360],[sh.min(),90],color="#888",lw=0.6,ls=":")
    i=np.argmin(np.abs(np.array([decl(d) for d in range(1,366,3)])[o]+23.44))
    if H[i]>2: ax.text(A[i]+(4 if A[i]>180 else -4 if A[i]<180 else 0),H[i]-1,f"{t}:00",fontsize=6.5,ha="left" if A[i]>180 else ("right" if A[i]<180 else "center"),va="top",color="#444")
ax.set_xlim(0,360); ax.set_ylim(0,90)
ax.set_xticks(range(0,361,30)); ax.set_yticks(range(0,91,15))
ax.set_xlabel(r"Acimut solar $\alpha$ [°]  (0° = N, 90° = E, 180° = S, 270° = O)")
ax.set_ylabel(r"Altura solar $h$ [°]")
ax.grid(lw=0.4,color="#ddd"); ax.set_axisbelow(True)
ax.legend(fontsize=6.5,ncol=4,loc="upper center",bbox_to_anchor=(0.5,1.17),frameon=False)
fig.tight_layout()
fig.savefig("/home/claude/fv/informe/figuras/diagrama_cilindrico.pdf"); fig.savefig("/home/claude/fv/informe/figuras/diagrama_cilindrico.png",dpi=200)
