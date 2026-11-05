import sys; sys.path.insert(0,"/home/claude/fv/scripts")
import numpy as np, matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from radiacion import mes
plt.rcParams.update({"font.family":"STIXGeneral","mathtext.fontset":"stix","font.size":8,"axes.spines.top":False,"axes.spines.right":False})
n,m=18,2
cases=[("14.1 °C",41.67,34.51,14.04,13.29,"#2f6f9f"),("25 °C (STC)",40.69,33.70,14.12,13.36,"#6a9a3a"),("64.3 °C",37.18,30.79,14.40,13.62,"#d08a2e")]
def iv(Voc,Vmp,Isc,Imp,V):
    C2=(Vmp/Voc-1)/np.log(1-Imp/Isc); C1=(1-Imp/Isc)*np.exp(-Vmp/(C2*Voc))
    return np.clip(Isc*(1-C1*(np.exp(V/(C2*Voc))-1)),0,None)
fig,ax=plt.subplots(figsize=(3.45,2.7))
# SOA
Vmin,Vmax,Vdc,Imax,Pm=480,850,1000,36,17000
Vh=np.linspace(Vmin,Vmax,200); Ih=np.minimum(Pm/Vh,Imax)
ax.fill_between(Vh,0,Ih,color="#e8eef4",zorder=0,label="SOA (rango MPPT)")
ax.plot(Vh,Ih,color="#555",lw=0.9)
ax.plot([Vmin,Vmin],[0,Imax],color="#555",lw=0.9); ax.plot([Vmax,Vmax],[0,Pm/Vmax],color="#555",lw=0.9)
ax.axvline(Vdc,color="#a33",lw=1,ls="--"); ax.text(Vdc-8,37.5,"$V_{dc,\\max}$ = 1000 V",ha="right",va="bottom",fontsize=6.5,color="#a33")
ax.axhline(Imax,color="#a33",lw=1,ls="--"); ax.text(30,Imax+0.6,"$I_{sc,\\max}$ = 36 A por MPPT",fontsize=6.5,color="#a33")
ax.annotate("$P_{\\max}$ = 17 kW por MPPT",xy=(790,17000/790),xytext=(830,28),fontsize=6.5,color="#333",ha="center",arrowprops=dict(arrowstyle="-",color="#555",lw=0.6))
for lab,Voc,Vmp,Isc,Imp,c in cases:
    V=np.linspace(0,n*Voc,300); I=m*iv(Voc,Vmp,Isc,Imp,V/n)
    ax.plot(V,I,color=c,lw=1.3,label=f"Arreglo a {lab}")
    ax.plot(n*Vmp,m*Imp,"o",color=c,ms=4,mec="w",mew=0.6)
ax.set_xlim(0,1050); ax.set_ylim(0,42)
ax.set_xlabel("Tensión DC [V]"); ax.set_ylabel("Corriente DC [A]")
ax.legend(fontsize=6.3,frameon=False,loc="lower left",bbox_to_anchor=(0.0,0.02))
ax.grid(lw=0.4,color="#ddd"); ax.set_axisbelow(True)
fig.tight_layout()
fig.savefig("/home/claude/fv/informe/figuras/soa.pdf"); fig.savefig("/home/claude/fv/informe/figuras/soa.png",dpi=200)
# Producción vs consumo
E=np.load("/home/claude/fv/datos/E_mensual.npy")
cons=np.array([18482,17626,18238,18850,19339,18482,18972,19094,18238,18727,17993,18972])
fig,ax=plt.subplots(figsize=(3.45,2.3)); x=np.arange(12); w=0.38
ax.bar(x-w/2,cons/1000,w,color="#b9c7d3",label="Consumo")
ax.bar(x+w/2,E/1000,w,color="#d08a2e",label="Generación estimada")
ax.set_xticks(x); ax.set_xticklabels(mes,fontsize=7); ax.set_ylabel("Energía [MWh]"); ax.set_ylim(0,24)
ax.legend(fontsize=6.5,frameon=False,ncol=2,loc="upper center")
ax.grid(axis="y",lw=0.4,color="#ddd"); ax.set_axisbelow(True)
fig.tight_layout()
fig.savefig("/home/claude/fv/informe/figuras/produccion.pdf"); fig.savefig("/home/claude/fv/informe/figuras/produccion.png",dpi=200)
