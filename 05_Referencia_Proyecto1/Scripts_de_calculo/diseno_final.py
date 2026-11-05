"""Diseño eléctrico del arreglo seleccionado (criterio: generar el consumo anual): 374 módulos, 22 cadenas de 17, 5 inversores CPS de 25 kW."""
import sys, json, os; sys.path.insert(0, "/home/claude/fv/scripts"); os.chdir("/home/claude/fv/scripts")
import numpy as np, matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from radiacion import G, K, dias, mes

# Módulo AIKO 450 W corregido por temperatura (Tabla de la Sección IV)
Voc_f, Vmp_f, Isc_f, Imp_f = 41.67, 34.84, 14.04, 13.29     # 14.1 °C (gVmp = gP - gIsc = -0.31 %/°C)
Voc_c, Vmp_c, Isc_c, Imp_c = 37.18, 29.59, 14.40, 13.62     # 64.3 °C
Voc, Vmp, Isc, Imp, P = 40.69, 33.70, 14.12, 13.36, 450
# Inversor CPS SCA25KTL-DO/US-208
Pac, Vdcmax, Vmin, Vmax, Vop, Vstart = 25e3, 1000, 480, 850, (200, 950), 330
IscMPPT, PmpptMax, PpvMax = 36, 17e3, 45e3

n, cad, inv = 17, 22, 5
N = n*cad; Pfv = N*P/1000
r = {}
r["N"], r["Pfv"], r["DCAC_total"], r["DCAC_inv5"], r["DCAC_inv4"] = N, Pfv, Pfv*1000/(inv*Pac), (5*n*P)/Pac, (4*n*P)/Pac
r["Ns_max"] = Vdcmax/Voc_f; r["Ns_min"] = Vmin/Vmp_c; r["Ns_maxMPPT"] = Vmax/Vmp_f
r["cad_MPPT"] = IscMPPT/Isc_c
r["Voc_frio"] = n*Voc_f; r["Vmp_frio"] = n*Vmp_f; r["Vmp_cal"] = n*Vmp_c; r["Voc_cal"] = n*Voc_c
r["Isc_MPPT"] = 2*Isc_c; r["P_MPPT"] = 2*n*P; r["P_MPPT_frio"] = 2*n*462.8; r["P_inv"] = 5*n*P
for k, v in r.items(): print(k, round(v, 2))

# Factor de rendimiento: pérdida por temperatura calculada para cada mes (curso: Tc = Ta + (NOCT-20)/800*G)
Nc = json.load(open("/home/claude/fv/datos/nasa_power_climatologia.json"))
Tm = np.array([Nc["T2M"][m] for m in ["JAN","FEB","MAR","APR","MAY","JUN","JUL","AUG","SEP","OCT","NOV","DEC"]])
NOCT, gP = 47.0, 0.26/100
Tc_mes = Tm + (NOCT-20)/800*1000
L_temp = gP*(Tc_mes-25)                       # pérdida térmica mensual
perd = {"Cableado": 0.02, "Dispersión": 0.02, "Suciedad": 0.03,
        "Seguimiento MPP": 0.01, "Reflectancia": 0.02, "Recorte del inversor": 0.0014}
PR_otros = np.prod([1-v for v in perd.values()])*0.965
PR_mes = PR_otros*(1-L_temp)
for i in range(12): print(mes[i], round(Tm[i], 2), round(Tc_mes[i], 1), round(100*L_temp[i], 2), round(PR_mes[i], 3))
HSP = G*np.array(K[10])
E = HSP*Pfv*PR_mes*dias
PR = E.sum()/(HSP*Pfv*dias).sum()
print("PR anual equivalente", round(PR, 4), "pérdida térmica anual equivalente", round(100*(1-PR/PR_otros), 2))
cons = np.array([18482,17626,18238,18850,19339,18482,18972,19094,18238,18727,17993,18972.])
for i in range(12): print(mes[i], round(HSP[i], 2), round(E[i]), round(100*E[i]/cons[i], 1))
print("Anual", round(E.sum()), "yield", round(E.sum()/Pfv), "cobertura", round(100*E.sum()/cons.sum(), 1))
np.save("/home/claude/fv/datos/E_final.npy", E)
json.dump(dict(r, PR=PR, PR_mes=PR_mes.tolist(), L_temp=L_temp.tolist(), Tm=Tm.tolist(), Tc_mes=Tc_mes.tolist(), PR_otros=PR_otros, E=E.tolist(), HSP=HSP.tolist(), perd=perd), open("/home/claude/fv/datos/diseno_final.json", "w"), indent=1)

# ---------- Figuras ----------
plt.rcParams.update({"font.family": "STIXGeneral", "mathtext.fontset": "stix", "font.size": 8,
                     "axes.spines.top": False, "axes.spines.right": False})
cases = [("14.1 °C", Voc_f, Vmp_f, Isc_f, Imp_f, "#9ab6cf"), ("25 °C (STC)", Voc, Vmp, Isc, Imp, "#4f7ea8"),
         ("64.3 °C", Voc_c, Vmp_c, Isc_c, Imp_c, "#1f3f66")]
def iv(Voc, Vmp, Isc, Imp, V):
    C2 = (Vmp/Voc-1)/np.log(1-Imp/Isc); C1 = (1-Imp/Isc)*np.exp(-Vmp/(C2*Voc))
    return np.clip(Isc*(1-C1*(np.exp(V/(C2*Voc))-1)), 0, None)
fig, ax = plt.subplots(figsize=(3.45, 2.6))
Vh = np.linspace(Vmin, Vmax, 200); Ih = np.minimum(PmpptMax/Vh, IscMPPT)
ax.fill_between(Vh, 0, Ih, color="#e9ecef", zorder=0, label="Zona MPPT a plena potencia")
ax.plot(Vh, Ih, color="#666", lw=0.8); ax.plot([Vmin, Vmin], [0, IscMPPT], color="#666", lw=0.8)
ax.plot([Vmax, Vmax], [0, PmpptMax/Vmax], color="#666", lw=0.8)
ax.axvline(Vdcmax, color="#666", lw=0.8, ls="--"); ax.text(Vdcmax-10, 38.5, "1000 V", ha="right", fontsize=6.5, color="#444")
ax.axhline(IscMPPT, color="#666", lw=0.8, ls="--"); ax.text(20, IscMPPT+0.6, "36 A", fontsize=6.5, color="#444")
ax.text(700, 26, "17 kW", fontsize=6.5, color="#444")
for lab, a, b, c, d, col in cases:
    V = np.linspace(0, n*a, 300); I = 2*iv(a, b, c, d, V/n)
    ax.plot(V, I, color=col, lw=1.2, label=f"Celda a {lab}")
    ax.plot(n*b, 2*d, "o", color=col, ms=3.5, mec="w", mew=0.5)
ax.set_xlim(0, 1050); ax.set_ylim(0, 42)
ax.set_xlabel("Tensión DC [V]"); ax.set_ylabel("Corriente DC [A]")
ax.legend(fontsize=6.2, frameon=False, loc="lower left")
ax.grid(lw=0.4, color="#e3e3e3"); ax.set_axisbelow(True)
fig.tight_layout()
fig.savefig("/home/claude/fv/informe/figuras/soa.pdf"); fig.savefig("/home/claude/fv/informe/figuras/soa.png", dpi=200)

fig, ax = plt.subplots(figsize=(3.45, 2.2)); x = np.arange(12); w = 0.38
ax.bar(x-w/2, cons/1000, w, color="#c4c9cf", label="Consumo (set. 2025 – ago. 2026)")
ax.bar(x+w/2, E/1000, w, color="#2f5d8a", label="Generación estimada")
ax.set_ylim(0, 27)
ax.set_xticks(x); ax.set_xticklabels(mes, fontsize=7); ax.set_ylabel("Energía [MWh]")
ax.legend(fontsize=6.3, frameon=False, ncol=2, loc="upper center")
ax.grid(axis="y", lw=0.4, color="#e3e3e3"); ax.set_axisbelow(True)
fig.tight_layout()
fig.savefig("/home/claude/fv/informe/figuras/produccion.pdf"); fig.savefig("/home/claude/fv/informe/figuras/produccion.png", dpi=200)
