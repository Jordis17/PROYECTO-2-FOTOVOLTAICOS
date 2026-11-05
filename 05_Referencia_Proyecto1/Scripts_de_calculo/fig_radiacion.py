import sys; sys.path.insert(0,"/home/claude/fv/scripts")
import numpy as np, matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from radiacion import *
plt.rcParams.update({"font.family":"STIXGeneral","mathtext.fontset":"stix","font.size":8,"axes.spines.top":False,"axes.spines.right":False})
C1,C2,C3="#2f6f9f","#d08a2e","#6a9a3a"
x=np.arange(12)
# Fig componentes + comparación
fig,(a1,a2)=plt.subplots(2,1,figsize=(3.45,3.9),sharex=True)
a1.plot(x,G,color=C1,marker="o",ms=3.5,lw=1.4,label="Global horizontal (GHI)")
a1.plot(x,B,color=C2,marker="s",ms=3.5,lw=1.4,label="Directa normal (DNI)")
a1.plot(x,D,color=C3,marker="^",ms=3.5,lw=1.4,label="Difusa horizontal (DHI)")
a1.set_ylim(0,7.6); a1.set_ylabel("Irradiación [kWh/(m$^2$·día)]")
a1.legend(fontsize=6.5,frameon=False,loc="upper center",ncol=2,columnspacing=0.8,handlelength=1.6)
a1.set_title("(a) Componentes de radiación, NASA POWER",fontsize=8,pad=3)
w=0.38
a2.bar(x-w/2,G,w,color=C1,label="NASA POWER (2001–2025)")
a2.bar(x+w/2,Gp,w,color="#9cc0dc",label="PVGIS-ERA5 (2005–2023)")
a2.set_ylim(0,7.6); a2.set_ylabel("GHI [kWh/(m$^2$·día)]")
a2.legend(fontsize=6.5,frameon=False,loc="upper center",ncol=2,columnspacing=0.8)
a2.set_title("(b) Irradiación global horizontal por base de datos",fontsize=8,pad=3)
for a in (a1,a2): a.grid(axis="y",lw=0.4,color="#ddd"); a.set_axisbelow(True)
a2.set_xticks(x); a2.set_xticklabels(mes,fontsize=7)
fig.tight_layout(h_pad=0.8)
fig.savefig("/home/claude/fv/informe/figuras/radiacion_componentes.pdf"); fig.savefig("/home/claude/fv/informe/figuras/radiacion_componentes.png",dpi=200)
# Fig inclinación
betas=sorted(K); Hn=[(G*np.array(K[b])*dias).sum() for b in betas]; Hp=[(Gp*np.array(K[b])*dias).sum() for b in betas]
fig,ax=plt.subplots(figsize=(3.45,2.2))
ax.plot(betas,Hn,color=C1,marker="o",ms=3.5,lw=1.4,label="NASA POWER × K")
ax.plot(betas,Hp,color=C2,marker="s",ms=3.5,lw=1.4,label="PVGIS × K")
ax.plot([14],[(Gopt*dias).sum()],marker="*",ms=9,color="#333",ls="none",label="PVGIS, óptimo propio (14°)")
ax.set_xlabel(r"Inclinación $\beta$ [°] (orientación sur)"); ax.set_ylabel("Irradiación anual [kWh/m$^2$]")
ax.set_xticks(betas); ax.set_ylim(1350,1750)
ax.grid(lw=0.4,color="#ddd"); ax.set_axisbelow(True)
ax.legend(fontsize=6.5,frameon=False,loc="lower left")
fig.tight_layout()
fig.savefig("/home/claude/fv/informe/figuras/inclinacion_anual.pdf"); fig.savefig("/home/claude/fv/informe/figuras/inclinacion_anual.png",dpi=200)
