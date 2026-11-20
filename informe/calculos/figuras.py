"""Figuras del Proyecto 2 (lee resultados.json de sistema.py). Uso: python3 figuras.py"""
import json
from pathlib import Path
import numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

AQ = Path(__file__).resolve().parent
FIG = AQ.parent / "figuras"
R = json.load(open(AQ / "resultados.json"))
plt.rcParams.update({"font.family": "STIXGeneral", "mathtext.fontset": "stix", "font.size": 8,
                     "axes.spines.top": False, "axes.spines.right": False})
C1, C2, C3, C4, C5 = "#2a78d6", "#eb6834", "#1baf7a", "#eda100", "#6250d6"
GRIS = "#9a9890"
mes = ["Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Set", "Oct", "Nov", "Dic"]

def guardar(fig, n):
    fig.tight_layout()
    fig.savefig(FIG / f"{n}.pdf"); fig.savefig(FIG / f"{n}.png", dpi=200); plt.close(fig)

def rejilla(ax, eje="y"):
    ax.grid(axis=eje, lw=0.4, color="#ddd"); ax.set_axisbelow(True)

# 1. Consumo diario por equipo crítico
c = sorted(R["consumo"]["cargas"], key=lambda x: x["E"])
fig, ax = plt.subplots(figsize=(3.45, 2.4))
y = np.arange(len(c))
ax.barh(y, [x["E"] for x in c], color=C1, height=0.6)
ax.set_yticks(y); ax.set_yticklabels([x["eq"].replace("Bombillos LED 15 W", "3 bombillos LED" if "1)" in x["eq"] else "4 bombillos LED").replace("Bombillo LED 15 W", "1 bombillo LED").replace(" (grupo 1)", "").replace(" (grupo 2)", "").replace(" (grupo 3)", "") for x in c], fontsize=6.5)
for i, x in enumerate(c): ax.text(x["E"] + 25, i, f"{x['E']:.0f}", va="center", fontsize=6.5)
ax.set_xlabel("Energía [Wh/día]"); ax.set_xlim(0, 2050); rejilla(ax, "x")
guardar(fig, "consumo_equipos")

# 2. Consumo y factura mensual con y sin sistema
f = R["finanzas"]; x = np.arange(12); w = 0.38
fig, axs = plt.subplots(2, 1, figsize=(3.45, 3.6), sharex=True)
ax = axs[0]
ax.bar(x - w / 2, f["kWh"], w, color=GRIS, label="Consumo de la casa")
ax.bar(x + w / 2, f["E_crit_m"], w, color=C1, label="Cargas críticas")
ax.set_ylabel("Energía [kWh]"); ax.set_ylim(0, 340); rejilla(ax)
ax.legend(fontsize=6.5, frameon=False, ncol=2, loc="upper center")
ax = axs[1]
ax.bar(x - w / 2, np.array(f["sin"]) / 1000, w, color=GRIS, label="Sin sistema")
ax.bar(x + w / 2, np.array(f["con"]) / 1000, w, color=C2, label="Con sistema")
ax.set_ylabel("Factura [miles de ¢]"); ax.set_ylim(0, 27); rejilla(ax)
ax.set_xticks(x); ax.set_xticklabels(mes)
ax.legend(fontsize=6.5, frameon=False, ncol=2, loc="upper center")
guardar(fig, "consumo_facturas")

# 3. Diagrama cilíndrico (latitud del sitio, tiempo solar; ecuaciones del curso)
PHI = 9.935845
def decl(d):
    db = d * 2 * np.pi / 365.25
    return np.degrees(np.arcsin(0.3978 * np.sin(db - 1.400 + 0.0355 * np.sin(db - 0.0489))))
def sunpos(d, ts):
    dl = np.radians(decl(d)); ph = np.radians(PHI); w_ = np.radians(15 * (np.asarray(ts) - 12))
    h = np.arcsin(np.sin(ph) * np.sin(dl) + np.cos(ph) * np.cos(dl) * np.cos(w_))
    sa = np.cos(dl) * np.sin(w_) / np.cos(h)
    ca = (np.sin(h) * np.sin(ph) - np.sin(dl)) / (np.cos(h) * np.cos(ph))
    return np.degrees(h), (np.degrees(np.arctan2(sa, ca)) + 180) % 360
dias = {"21 dic": 355, "21 ene": 21, "21 nov": 325, "21 feb": 52, "21 oct": 294, "21 mar": 80, "21 set": 264,
        "21 abr": 111, "21 ago": 233, "21 may": 141, "21 jul": 202, "21 jun": 172}
grupos = [("21 dic", ["21 dic"]), ("21 ene / 21 nov", ["21 ene", "21 nov"]), ("21 feb / 21 oct", ["21 feb", "21 oct"]),
          ("21 mar / 21 set", ["21 mar", "21 set"]), ("21 abr / 21 ago", ["21 abr", "21 ago"]),
          ("21 may / 21 jul", ["21 may", "21 jul"]), ("21 jun", ["21 jun"])]
cols = plt.cm.viridis(np.linspace(0.05, 0.9, len(grupos)))
fig, ax = plt.subplots(figsize=(7.0, 3.3))
ts = np.linspace(5.5, 18.5, 600)
for (lab, ms), col in zip(grupos, cols):
    for k, m in enumerate(ms):
        h, a = sunpos(dias[m], ts)
        cortes = np.where(np.abs(np.diff(a)) > 180)[0] + 1
        primero = True
        for sa_, sh_ in zip(np.split(a, cortes), np.split(h, cortes)):
            mk = sh_ > 0
            if mk.sum() < 2: continue
            ax.plot(sa_[mk], sh_[mk], color=col, lw=1.3, ls="-" if k == 0 else (0, (4, 2)),
                    label=lab if (k == 0 and primero) else None)
            primero = False
dd = np.arange(1, 366, 2); od = np.argsort(decl(dd))
for t in range(6, 19):
    H, A = sunpos(dd, t); H, A = H[od], A[od]; mk = H > 0
    if mk.sum() < 2 or t == 12: continue
    ax.plot(A[mk], H[mk], color="#888", lw=0.6, ls=":")
    i = np.argmin(decl(dd)[od]); ax.text(A[i] + (3 if A[i] > 180 else -3), H[i] - 1.5, f"{t}:00", fontsize=6.5,
                                        ha="left" if A[i] > 180 else "right", va="top", color="#444")
ax.set_xlim(0, 360); ax.set_ylim(0, 90); ax.set_xticks(range(0, 361, 30)); ax.set_yticks(range(0, 91, 15))
ax.set_xlabel(r"Acimut solar [°]  (0° = N, 90° = E, 180° = S, 270° = O)"); ax.set_ylabel(r"Altura solar $h$ [°]")
rejilla(ax, "both")
ax.legend(fontsize=6.5, ncol=4, loc="upper center", bbox_to_anchor=(0.5, 1.17), frameon=False)
guardar(fig, "diagrama_cilindrico")
cil = {}
for m in ("21 dic", "21 jun", "21 mar"):
    h, a = sunpos(dias[m], 12.0); cil[m] = float(h)
sal = {m: 12 - np.degrees(np.arccos(-np.tan(np.radians(PHI)) * np.tan(np.radians(decl(d))))) / 15 for m, d in dias.items()}
json.dump(dict(h_mediodia=cil, duracion={m: 2 * (12 - v) for m, v in sal.items()}), open(AQ / "cilindrico.json", "w"), indent=1)

# 4. Irradiación diaria (HSP) por mes y orientación
pv = R["recurso"]["pv"]
fig, ax = plt.subplots(figsize=(3.45, 2.5))
for k, lab, col, ls in [("horizontal", "Horizontal", GRIS, "-"), ("oeste", "12° al oeste", C2, "-"),
                        ("sur", "12° al sur", C3, "-"),
                        ("optimo", f"Óptimo ({pv['optimo']['slope']}°, acimut {pv['optimo']['azimuth']}°)", C5, "--"),
                        ("este", "12° al este (diseño)", C1, "-")]:
    ax.plot(x, pv[k]["HSP"], color=col, lw=2 if k == "este" else 1.2, ls=ls, marker="o", ms=3, label=lab)
i = int(np.argmin(pv["este"]["HSP"]))
ax.annotate(f"{pv['este']['HSP'][i]:.2f} HSP", xy=(i, pv["este"]["HSP"][i]), xytext=(i - 2.6, 3.35), fontsize=6.5,
            arrowprops=dict(arrowstyle="-", lw=0.6, color="#555"))
ax.set_xticks(x); ax.set_xticklabels(mes); ax.set_ylabel("Irradiación [kWh/m²·día]"); ax.set_ylim(3, 6.5)
ax.legend(fontsize=6, frameon=False, ncol=2, loc="upper right"); rejilla(ax)
guardar(fig, "radiacion_mensual")

# 5. SOA del regulador con las curvas I-V del arreglo 2S2P
def iv(Voc, Vmp, Isc, Imp, Vv):
    C2_ = (Vmp / Voc - 1) / np.log(1 - Imp / Isc); C1_ = (1 - Imp / Isc) * np.exp(-Vmp / (C2_ * Voc))
    return np.clip(Isc * (1 - C1_ * (np.exp(Vv / (C2_ * Voc)) - 1)), 0, None)
tt = R["modulo"]["tabla_T"]; reg = R["regulador"]["reg"]
fig, ax = plt.subplots(figsize=(3.45, 2.7))
Vmin, Vop, Vabs_, Imax, Pm = 28.8 + 5, reg["Voc_op"], reg["Voc_abs"], reg["Isc_max"], reg["P_nom24"]
Vh = np.linspace(Vmin, Vop, 200)
ax.fill_between(Vh, 0, np.minimum(Pm * 0 + Imax, Imax), color="#e8eef4", zorder=0, label="Zona de operación del regulador")
ax.plot([Vmin, Vmin, Vop, Vop], [0, Imax, Imax, 0], color="#555", lw=0.9)
ax.axvline(Vabs_, color="#a33", lw=1, ls="--"); ax.text(Vabs_ + 1.5, 40, "$V_{oc}$ máx. = 150 V", ha="left", rotation=90, fontsize=6.5, color="#a33")
ax.text(Vmin + 2, Imax + 1.5, "$I_{sc}$ máx. = 70 A", fontsize=6.5, color="#a33")
ax.text(Vmin + 1, 2, "$V_{bat}$+5 V", fontsize=6.5, color="#555", rotation=90, va="bottom")
for t, col, lab in zip(tt, [C1, C3, C2], ["7 °C", "25 °C (STC)", "63.2 °C"]):
    Vv = np.linspace(0, 2 * t["Voc"], 300); I = 2 * iv(t["Voc"], t["Vmp"], t["Isc"], t["Imp"], Vv / 2)
    ax.plot(Vv, I, color=col, lw=1.3, label=f"Arreglo 2S2P a {lab}")
    ax.plot(2 * t["Vmp"], 2 * t["Imp"], "o", color=col, ms=4, mec="w", mew=0.6)
ax.set_xlim(0, 160); ax.set_ylim(0, 105); ax.set_xlabel("Tensión FV [V]"); ax.set_ylabel("Corriente FV [A]")
ax.legend(fontsize=6.2, frameon=False, loc="upper center", ncol=2); rejilla(ax, "both")
guardar(fig, "soa_regulador")

# 6. Energía mensual: disponible para las cargas y demanda
e = R["energia"]["mensual"]
fig, ax = plt.subplots(figsize=(3.45, 2.3))
ax.bar(x - w / 2, [m["E_util"] for m in e], w, color=C1, label="Disponible para las cargas")
ax.bar(x + w / 2, [m["E_dem"] for m in e], w, color=GRIS, label="Demanda de las cargas críticas")
ax.set_xticks(x); ax.set_xticklabels(mes); ax.set_ylabel("Energía [kWh/mes]"); ax.set_ylim(0, 300)
ax.legend(fontsize=6.5, frameon=False, ncol=1, loc="upper right"); rejilla(ax)
guardar(fig, "energia_mensual")

# 7. Flujo de caja acumulado
fig, ax = plt.subplots(figsize=(3.45, 2.3))
ac = np.array(f["acum"]) / 1e6
ax.plot(range(len(ac)), ac, color=C2, lw=2, marker="o", ms=3)
ax.axhline(0, color="#555", lw=0.8)
for k, lab in ((13, "Reemplazo de\ninversor y regulador"), (15, "Reemplazo de\nbaterías")):
    ax.annotate(lab, xy=(k, ac[k]), xytext=(k - 10 if k == 13 else k + 2, ac[k] + (-1.6 if k == 13 else 1.2)), fontsize=6,
                arrowprops=dict(arrowstyle="-", lw=0.6, color="#555"))
ax.set_xlabel("Año"); ax.set_ylabel("Flujo acumulado [millones de ¢]"); ax.set_xlim(0, 25); rejilla(ax)
guardar(fig, "flujo_acumulado")
print("figuras listas")

# 8. Componentes de la radiación (PVGIS-ERA5 y NASA POWER)
RAIZ = AQ.parents[1]
mr = json.load(open(RAIZ / "recurso" / "pvgis_MRcalc_mensual.json"))["outputs"]["monthly"]
ns = json.load(open(RAIZ / "recurso" / "nasa_power_climatologia_2001-2025.json"))["properties"]["parameter"]
dm = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
MK = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]
G, Dh, B = [], [], []
for m in range(1, 13):
    r = [q for q in mr if q["month"] == m]; n = len(r)
    G.append(sum(q["H(h)_m"] for q in r) / n / dm[m - 1])
    Dh.append(sum(q["Kd"] * q["H(h)_m"] for q in r) / n / dm[m - 1])
    B.append(sum(q["Hb(n)_m"] for q in r) / n / dm[m - 1])
comp = dict(GHI=G, DHI=Dh, DNI=B, nasa_GHI=[ns["ALLSKY_SFC_SW_DWN"][k] for k in MK],
            nasa_DHI=[ns["ALLSKY_SFC_SW_DIFF"][k] for k in MK], nasa_DNI=[ns["ALLSKY_SFC_SW_DNI"][k] for k in MK])
json.dump(comp, open(AQ / "componentes.json", "w"), indent=1)
fig, ax = plt.subplots(figsize=(3.45, 2.6))
for k, lab, col in [("GHI", "Global horizontal (GHI)", C1), ("DNI", "Directa normal (DNI)", C2), ("DHI", "Difusa horizontal (DHI)", C3)]:
    ax.plot(x, comp[k], color=col, lw=1.8, marker="o", ms=3, label=f"{lab}, PVGIS")
    ax.plot(x, comp["nasa_" + k], color=col, lw=1.0, ls="--")
ax.plot([], [], color="#555", lw=1.0, ls="--", label="NASA POWER (mismo color)")
ax.set_xticks(x); ax.set_xticklabels(mes); ax.set_ylabel("Irradiación [kWh/m²·día]"); ax.set_ylim(0, 7.5)
ax.legend(fontsize=6, frameon=False, ncol=2, loc="upper center"); rejilla(ax)
guardar(fig, "radiacion_componentes")
print("componentes listos")
