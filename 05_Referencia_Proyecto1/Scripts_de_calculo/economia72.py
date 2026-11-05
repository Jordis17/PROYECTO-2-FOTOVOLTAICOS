"""Evaluación económica final: 72 kWp (160 módulos, 10 cadenas de 16, 2 inversores CPS de 25 kW).
Balance mensual de datos/configuracion_72kWp.json (escenario B, carga k = 0.75 como referencia)."""
import json, numpy as np, matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
TC, EURUSD = 456.61, 1.1479
mes = ["Ene","Feb","Mar","Abr","May","Jun","Jul","Ago","Set","Oct","Nov","Dic"]
cfg = json.load(open("/home/claude/fv/datos/configuracion_72kWp.json"))
C = np.array([18482,17626,18238,18850,19339,18482,18972,19094,18238,18727,17993,18972.])
D = np.array([43.70,49.33,45.78,46.14,46.88,45.78,44.19,47.25,53.00,47.12,44.92,44.31])
pe, pd_, pa, iva, bomb = 59.67, 9861.68, 2.70, 0.13, 1827.40
p_exc, tder, kWp = 27.40, 255.0, 72.0

# ---------------- Presupuesto ----------------
eq = [  # (rubro, descripción, cantidad, precio unitario USD)
 ("Módulos", "AIKO-A450-MAH54Mb", 160, 128.96*EURUSD),
 ("Inversores", "CPS SCA25KTL-DO/US-208 con caja de conexiones", 2, 8997.44),
 ("Estructura", "Riel SM 240 in", 80, 101.10),
 ("Estructura", "Empalme", 60, 10.81),
 ("Estructura", "Grapa intermedia BND", 300, 4.15),
 ("Estructura", "Grapa de extremo", 40, 3.55),
 ("Estructura", "Soporte L-Foot", 340, 4.35),
 ("Estructura", "Pata de inclinación 307107M", 170, 32.01),
 ("Estructura", "Fijación a lámina S-5-U Mini", 340, 7.66),
 ("Estructura", "Terminal de tierra", 20, 8.40),
 ("Conductores", "PV Wire 10 AWG, carrete 500 ft", 4, 259.99),
 ("Conductores", "THHN 3 AWG [ft]", 296, 2.56),
 ("Conductores", "THHN 2/0 AWG [ft]", 148, 5.53),
 ("Protecciones", "Interruptor 3P 90 A", 2, 1174.50),
 ("Protecciones", "Interruptor 3P 175 A", 1, 3120.00),
 ("Protecciones", "Seccionador 200 A", 1, 976.33),
]
tot = {}
for r, d_, q, p in eq: tot[r] = tot.get(r, 0) + q*p
tot["Otros materiales eléctricos (15 %)"] = 0.15*(tot["Conductores"] + tot["Protecciones"])
equipo = sum(tot.values())
serv_crc = {"Estudios de factibilidad": 300000, "Viabilidad ante el ICE": 80000, "Visado de planos (CFIA)": 200000,
            "Interconexión ICE (etapas 1-4)": 18591.89+142355.14+131746.70+90177.39,
            "Instalación (¢100 000/kWp)": 100000*kWp}
serv = sum(serv_crc.values())/TC
costo = equipo + serv; precio = 1.2*costo; I0 = precio*TC
print({k: round(v) for k, v in tot.items()}, "equipo", round(equipo), "serv", round(serv), "costo", round(costo),
      "precio USD", round(precio), "CRC M", round(I0/1e6, 2), "USD/W", round(precio/72000, 3))

# ---------------- Factura ----------------
def factura(E, Dem, kwp=0.0):
    en = E*pe; de = Dem*pd_; al = E*pa; t = tder*kwp
    return en + de + al + iva*(en + de + t) + t + bomb
def balance(key, exc=True, red=0.0):
    m = cfg[key]; slf = np.array(m["self"], float)
    gen = np.load("/home/claude/fv/datos/E72.npy")   # generación mensual con HSP·P·PR (Sección V)
    exp = gen - slf
    compra = C - slf
    sin = factura(C, D); con = factura(compra, D*(1-red), kWp) - (exp*p_exc if exc else 0)
    return dict(gen=gen, slf=slf, exp=exp, compra=compra, sin=sin, con=con, ah=sin-con)
B = balance("B_0.75")

# ---------------- Flujo de caja ----------------
r_p, n_p, tasa, anos, om = 0.09, 120, 0.07, 25, 0.01
prest = 0.8*I0; im = r_p/12; cuota = prest*im/(1-(1+im)**-n_p)
def flujo(ah1, esc=0.0, fin=False):
    F = [-(0.2*I0 if fin else I0)]; deg = 1.0
    for k in range(1, anos+1):
        if k == 2: deg *= 0.99
        elif k > 2: deg *= 1-0.0035
        F.append(ah1*deg*(1+esc)**(k-1) - om*I0*(1+esc)**(k-1) - (12*cuota if (fin and k <= 10) else 0))
    return np.array(F)
def vpn(F): return sum(f/(1+tasa)**i for i, f in enumerate(F))
def tir(F):
    lo, hi = -0.5, 1.0
    for _ in range(200):
        m = (lo+hi)/2
        lo, hi = (m, hi) if sum(f/(1+m)**i for i, f in enumerate(F)) > 0 else (lo, m)
    return m
def pri(F):
    c = np.cumsum(F)
    if c[-1] < 0: return float("nan")
    k = int(np.argmax(c >= 0)); return k-1 + (-c[k-1])/F[k]
esc_list = {"sin aumento": 0.0, "+3 % anual": 0.03}
ind = {}
for nom, kw in [("Contado, sin aumento", dict()), ("Contado, +3 %", dict(esc=0.03)),
                ("Préstamo 80 %, sin aumento", dict(fin=True)), ("Préstamo 80 %, +3 %", dict(esc=0.03, fin=True))]:
    F = flujo(B["ah"].sum(), **kw); ind[nom] = dict(vpn=vpn(F), tir=tir(F), pri=pri(F), F=F.tolist())
sens = {}
for nom, (key, exc, red) in {"Base": ("B_0.75", True, 0), "Demanda −10 %": ("B_0.75", True, .1),
                             "Demanda −20 %": ("B_0.75", True, .2), "Excedentes no pagados": ("B_0.75", False, 0),
                             "Carga baja (k = 0.65)": ("B_0.65", True, 0), "Carga alta (k = 0.85)": ("B_0.85", True, 0)}.items():
    b = balance(key, exc, red); F = flujo(b["ah"].sum())
    sens[nom] = dict(ah=b["ah"].sum(), vpn=vpn(F), tir=tir(F), pri=pri(F))

if __name__ == "__main__":
    print("Gen", B["gen"].sum(), "self", B["slf"].sum(), "exp", B["exp"].sum(), "compra", B["compra"].sum())
    print("Factura sin", B["sin"].sum()/1e6, "con", B["con"].sum()/1e6, "ahorro", B["ah"].sum()/1e6, B["ah"].sum()/B["sin"].sum())
    en0 = (C*pe*(1+iva)+C*pa).sum(); de0 = (D*pd_*(1+iva)).sum()
    print("energia+alumbrado+IVA sin", en0/1e6, "demanda+IVA", de0/1e6)
    print("TDER anual", tder*kWp*12*1.13/1e6, "excedentes", (B["exp"]*p_exc).sum()/1e6)
    print("cuota", cuota, "anual", 12*cuota, "prest", prest)
    for k, v in ind.items(): print(k, round(v["vpn"]/1e6, 2), round(v["tir"]*100, 1), round(v["pri"], 1))
    for k, v in sens.items(): print(k, round(v["ah"]/1e6, 2), round(v["vpn"]/1e6, 2), round(v["tir"]*100, 1), round(v["pri"], 1))
    for i in range(12): print(mes[i], *[round(B[q][i]) for q in ("gen", "slf", "exp", "compra", "sin", "con", "ah")])
    json.dump(dict(tot=tot, equipo=equipo, serv_crc=serv_crc, costo=costo, precio=precio, I0=I0, cuota=cuota,
                   B={k: v.tolist() for k, v in B.items()}, ind=ind, sens=sens),
              open("/home/claude/fv/datos/economia72.json", "w"), indent=1, default=float)
    # Figuras
    plt.rcParams.update({"font.family": "STIXGeneral", "mathtext.fontset": "stix", "font.size": 8,
                         "axes.spines.top": False, "axes.spines.right": False})
    x = np.arange(12); w = 0.38
    fig, ax = plt.subplots(figsize=(3.45, 2.2))
    ax.bar(x-w/2, B["sin"]/1e6, w, color="#c4c9cf", label="Sin sistema FV")
    ax.bar(x+w/2, B["con"]/1e6, w, color="#2f5d8a", label="Con sistema FV")
    ax.set_xticks(x); ax.set_xticklabels(mes, fontsize=7); ax.set_ylabel("Factura mensual [millones de ¢]")
    ax.set_ylim(0, 2.3); ax.legend(fontsize=6.5, frameon=False, ncol=2, loc="upper center")
    ax.grid(axis="y", lw=0.4, color="#e3e3e3"); ax.set_axisbelow(True)
    fig.tight_layout(); fig.savefig("/home/claude/fv/informe/figuras/facturacion.pdf")
    fig.savefig("/home/claude/fv/informe/figuras/facturacion.png", dpi=200)
    fig, ax = plt.subplots(figsize=(3.45, 2.3))
    for nom, c, mk in [("Contado, sin aumento", "#2f5d8a", "o"), ("Préstamo 80 %, sin aumento", "#9ab6cf", "s")]:
        ax.plot(range(26), np.cumsum(ind[nom]["F"])/1e6, color=c, marker=mk, ms=2.5, lw=1.2, label=nom)
    ax.axhline(0, color="#666", lw=0.8)
    ax.set_xlabel("Año"); ax.set_ylabel("Flujo acumulado [millones de ¢]"); ax.set_xlim(0, 25)
    ax.legend(fontsize=6.5, frameon=False, loc="upper left")
    ax.grid(lw=0.4, color="#e3e3e3"); ax.set_axisbelow(True)
    fig.tight_layout(); fig.savefig("/home/claude/fv/informe/figuras/flujo_acumulado.pdf")
    fig.savefig("/home/claude/fv/informe/figuras/flujo_acumulado.png", dpi=200)
