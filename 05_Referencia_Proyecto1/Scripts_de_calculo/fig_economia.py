import json, numpy as np, matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
J=json.load(open("/home/claude/fv/datos/economia.json"))
plt.rcParams.update({"font.family":"STIXGeneral","mathtext.fontset":"stix","font.size":8,"axes.spines.top":False,"axes.spines.right":False})
mes=["Ene","Feb","Mar","Abr","May","Jun","Jul","Ago","Set","Oct","Nov","Dic"]
x=np.arange(12); w=0.38
fig,ax=plt.subplots(figsize=(3.45,2.3))
ax.bar(x-w/2,np.array(J["conv"])/1e6,w,color="#b9c7d3",label="Factura actual")
ax.bar(x+w/2,np.array(J["fv"])/1e6,w,color="#2f6f9f",label="Factura con sistema FV")
ax.set_xticks(x); ax.set_xticklabels(mes,fontsize=7); ax.set_ylabel("Monto mensual [millones de ¢]"); ax.set_ylim(0,2.3)
ax.legend(fontsize=6.5,frameon=False,ncol=2,loc="upper center")
ax.grid(axis="y",lw=0.4,color="#ddd"); ax.set_axisbelow(True)
fig.tight_layout(); fig.savefig("/home/claude/fv/informe/figuras/facturacion.pdf"); fig.savefig("/home/claude/fv/informe/figuras/facturacion.png",dpi=200)
fig,ax=plt.subplots(figsize=(3.45,2.4))
for k,lab,c,m in [("F","Con financiamiento (80 %)","#2f6f9f","o"),("Fc","De contado","#d08a2e","s")]:
    cum=np.cumsum(J[k])/1e6
    ax.plot(range(26),cum,color=c,marker=m,ms=2.8,lw=1.3,label=lab)
ax.axhline(0,color="#555",lw=0.8)
ax.set_xlabel("Año"); ax.set_ylabel("Flujo acumulado [millones de ¢]"); ax.set_xlim(0,25)
ax.legend(fontsize=6.5,frameon=False,loc="upper left")
ax.grid(lw=0.4,color="#ddd"); ax.set_axisbelow(True)
fig.tight_layout(); fig.savefig("/home/claude/fv/informe/figuras/flujo_acumulado.pdf"); fig.savefig("/home/claude/fv/informe/figuras/flujo_acumulado.png",dpi=200)
