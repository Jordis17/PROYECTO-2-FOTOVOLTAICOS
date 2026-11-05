import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
meses=["Set\n2025","Oct","Nov","Dic","Ene\n2026","Feb","Mar","Abr","May","Jun","Jul","Ago"]
E=[18238,18727,17993,18972,18482,17626,18238,18850,19339,18482,18972,19094]
D=[53,47.12,44.92,44.31,43.7,49.33,45.78,46.14,46.88,45.78,44.19,47.25]
prom=sum(E)/12
plt.rcParams.update({"font.family":"STIXGeneral","mathtext.fontset":"stix","font.size":8,"axes.spines.top":False,"axes.spines.right":False})
fig,(a1,a2)=plt.subplots(2,1,figsize=(3.45,3.6),sharex=True,gridspec_kw={"height_ratios":[1.6,1]})
x=range(12)
a1.bar(x,[e/1000 for e in E],width=0.7,color="#2f6f9f")
a1.axhline(prom/1000,color="#555",lw=0.8,ls="--")
a1.text(-0.4,21.3,f"- - promedio: {prom/1000:.1f} MWh/mes",ha="left",va="bottom",fontsize=7,color="#333")
a1.set_ylim(0,23); a1.set_ylabel("Energía [MWh]")
a1.grid(axis="y",lw=0.4,color="#ddd"); a1.set_axisbelow(True)
a2.plot(x,D,color="#2f6f9f",lw=1.5,marker="o",ms=3.5)
a2.set_ylim(40,55); a2.set_ylabel("Demanda [kW]")
a2.grid(axis="y",lw=0.4,color="#ddd"); a2.set_axisbelow(True)
a2.set_xticks(list(x)); a2.set_xticklabels(meses,fontsize=7)
fig.tight_layout(h_pad=0.6)
fig.savefig("/home/claude/fv/informe/figuras/consumo_mensual.pdf")
fig.savefig("/home/claude/fv/informe/figuras/consumo_mensual.png",dpi=200)
