"""Evaluación económica final: 76.5 kWp (170 módulos, 10 cadenas de 17, 2 inversores CPS de 25 kW).
La degradación se aplica solo a la parte del ahorro que depende de la generación."""
import json, numpy as np, matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
TC, EURUSD = 456.61, 1.1479
mes = ["Ene","Feb","Mar","Abr","May","Jun","Jul","Ago","Set","Oct","Nov","Dic"]
C = np.array([18482,17626,18238,18850,19339,18482,18972,19094,18238,18727,17993,18972.])
D = np.array([43.70,49.33,45.78,46.14,46.88,45.78,44.19,47.25,53.00,47.12,44.92,44.31])
pe, pd_, pa, iva, bomb = 59.67, 9861.68, 2.70, 0.13, 1827.40
p_exc, tder = 27.40, 255.0
v_kwh = pe*(1+iva) + pa            # valor de cada kWh autoconsumido [¢]

# ---------------- Presupuesto del sistema seleccionado ----------------
kWp = 76.5
eq = [
 ("Módulos", "AIKO-A450-MAH54Mb", 170, 128.96*EURUSD),
 ("Inversores", "CPS SCA25KTL-DO/US-208 con caja de conexiones", 2, 8997.44),
 ("Estructura", "Riel SM 240 in", 60, 101.10),
 ("Estructura", "Riel SM 132 in (precio estimado proporcional)", 20, 101.10*132/240),
 ("Estructura", "Empalme", 60, 10.81),
 ("Estructura", "Grapa intermedia BND", 320, 4.15),
 ("Estructura", "Grapa de extremo", 40, 3.55),
 ("Estructura", "Soporte L-Foot", 360, 4.35),
 ("Estructura", "Pata de inclinación 307107M", 180, 32.01),
 ("Estructura", "Fijación a lámina S-5-U Mini", 360, 7.66),
 ("Estructura", "Terminal de tierra", 20, 8.40),
 ("Conductores", "PV Wire 10 AWG, carrete 500 ft", 4, 259.99),
 ("Conductores", "THHN 3 AWG [ft]", 296, 2.56),
 ("Conductores", "THHN 3/0 AWG [ft]", 148, 6.98),
 ("Protecciones", "Interruptor 3P 90 A", 2, 1174.50),
 ("Protecciones", "Interruptor 3P 175 A", 1, 3120.00),
 ("Protecciones", "Seccionador 200 A", 1, 976.33),
]
tot = {}
for r, d_, q, p in eq: tot[r] = tot.get(r, 0) + q*p
tot["Otros materiales eléctricos (15 %)"] = 0.15*(tot["Conductores"] + tot["Protecciones"])
tot = {k: round(v) for k, v in tot.items()}
equipo = sum(tot.values())
serv_crc = {"Estudios de factibilidad": 300000, "Viabilidad ante el ICE": 80000, "Visado de planos (CFIA)": 200000,
            "Interconexión ICE (etapas 1-4)": 382871, "Instalación (¢100 000/kWp)": round(100000*kWp)}
serv = {k: round(v/TC) for k, v in serv_crc.items()}
costo = equipo + sum(serv.values()); ganancia = round(0.2*costo); precio = costo + ganancia; I0 = precio*TC

# ---------------- Factura y flujo ----------------
def factura(E, Dem, kwp=0.0):
    en = E*pe; de = Dem*pd_; al = E*pa; t = tder*kwp
    return en + de + al + iva*(en + de + t) + t + bomb
def partes(slf, exp, kwp, exc=True, red=0.0):
    """Ahorro anual separado: dependiente de la generación y fijo (TDER, demanda)."""
    s_gen = (slf*v_kwh).sum() + (exp*p_exc).sum()*(1 if exc else 0)
    s_fijo = -tder*kwp*12*(1+iva) + red*(D*pd_*(1+iva)).sum()
    return s_gen, s_fijo
r_p, n_p, tasa, anos, om, d1, d2 = 0.09, 120, 0.07, 25, 0.01, 0.01, 0.0035
def flujo(I0_, s_gen, s_fijo, esc=0.0, fin=False):
    cuota = 0.8*I0_*(r_p/12)/(1-(1+r_p/12)**-n_p)
    F = [-(0.2*I0_ if fin else I0_)]
    for k in range(1, anos+1):
        deg = (1-d1)*(1-d2)**(k-1)
        F.append((s_gen*deg + s_fijo)*(1+esc)**(k-1) - om*I0_*(1+esc)**(k-1) - (12*cuota if (fin and k <= 10) else 0))
    return np.array(F), cuota
def vpn(F): return float(sum(f/(1+tasa)**i for i, f in enumerate(F)))
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
def ind(F): return dict(vpn=vpn(F), tir=tir(F), pri=pri(F))

# ---------------- Sistema seleccionado ----------------
cfg = json.load(open("/home/claude/fv/datos/configuracion_76kWp.json"))
gen = np.round(np.load("/home/claude/fv/datos/E76.npy"))
def balance(k=0.75, exc=True, red=0.0):
    slf = np.array(cfg[f"C_{k}"]["self"], float); exp = gen - slf; compra = C - slf
    sin = factura(C, D); con = factura(compra, D*(1-red), kWp) - (exp*p_exc if exc else 0)
    sg, sf = partes(slf, exp, kWp, exc, red)
    return dict(gen=gen, slf=slf, exp=exp, compra=compra, sin=sin, con=con, ah=sin-con, sg=sg, sf=sf)
B = balance()
res = {}
for nom, kw in [("Contado, 0 %", {}), ("Contado, 3 %", dict(esc=0.03)),
                ("Préstamo, 0 %", dict(fin=True)), ("Préstamo, 3 %", dict(esc=0.03, fin=True))]:
    F, cuota = flujo(I0, B["sg"], B["sf"], **kw); res[nom] = dict(ind(F), F=F.tolist())
sens = {}
for nom, (k, exc, red) in {"Caso base": (0.75, True, 0), "Demanda −10 %": (0.75, True, .1),
                           "Demanda −20 %": (0.75, True, .2), "Excedentes sin pago": (0.75, False, 0),
                           "Carga 65 %": (0.65, True, 0), "Carga 85 %": (0.85, True, 0)}.items():
    b = balance(k, exc, red); F, _ = flujo(I0, b["sg"], b["sf"])
    sens[nom] = dict(ind(F), ah=b["ah"].sum())

# ---------------- Comparación de alternativas (mismo modelo) ----------------
v2 = json.load(open("/home/claude/fv/datos/autoconsumo_horario_v2.json"))
def costo_aprox(Pdc, Pac):   # misma estimación usada en la comparación inicial
    nmod = round(Pdc*1000/450); ninv = int(Pac/25); ncad = nmod//18
    e = nmod*128.96*EURUSD + ninv*8997.44 + nmod*16883/144
    el = ncad*0.5*259.99 + ninv*148*2.56 + ninv*1174.50
    I = 1.25*ninv*69.5
    el += (3120+148*5.53+976.33) if I <= 175 else ((3600+1480+2320) if I <= 300 else (4100+2*148*6.5+2320))
    e += el*1.15
    return 1.2*(e + (300000+80000+200000+382871+100000*Pdc)/TC)*TC
alts = []
for Pdc, Pac, M in [a for a in v2["out"][1][2] if a[0] in (97.2, 105.3, 113.4) and a[1] == 75]:
    g_, s_ = np.array(M["gen"], float), np.array(M["self"], float); e_ = g_ - s_
    Ia = costo_aprox(Pdc, Pac); sg, sf = partes(s_, e_, Pdc)
    ah = (factura(C, D) - (factura(C - s_, D, Pdc) - e_*p_exc)).sum()
    F, _ = flujo(Ia, sg, sf); alts.append(dict(Pdc=Pdc, I=Ia, gen=g_.sum(), slf=s_.sum(), compra=(C-s_).sum(), ah=ah, **ind(F)))
F0, _ = flujo(I0, B["sg"], B["sf"])
alts.insert(0, dict(Pdc=kWp, I=I0, gen=B["gen"].sum(), slf=B["slf"].sum(), compra=B["compra"].sum(), ah=B["ah"].sum(), **ind(F0)))
# inversión incremental frente a la mayor alternativa
last = alts[-1]; Fi = flujo(last["I"], *partes(np.array(v2["out"][1][2][4][2]["self"], float),
        np.array(v2["out"][1][2][4][2]["gen"], float)-np.array(v2["out"][1][2][4][2]["self"], float), 113.4))[0] - F0
inc = dict(dI=last["I"]-I0, dA=last["ah"]-B["ah"].sum(), tir=tir(Fi))

if __name__ == "__main__":
    print("tot", tot, "equipo", equipo, "serv", serv, "costo", costo, "ganancia", ganancia, "precio", precio, "CRC", I0, "USD/W", precio/kWp/1000)
    print("gen", B["gen"].sum(), "self", B["slf"].sum(), "exp", B["exp"].sum(), "compra", B["compra"].sum(), "red compra", 1-B["compra"].sum()/C.sum())
    print("sin", B["sin"].sum(), "con", B["con"].sum(), "ah", B["ah"].sum(), B["ah"].sum()/B["sin"].sum(), "sg", B["sg"], "sf", B["sf"])
    print("cuota", cuota)
    for k, v in res.items(): print(k, round(v["vpn"]/1e6, 2), round(v["tir"]*100, 1), round(v["pri"], 1))
    for k, v in sens.items(): print(k, round(v["ah"]/1e6, 2), round(v["vpn"]/1e6, 1), round(v["tir"]*100, 1), round(v["pri"], 1))
    for a in alts: print({k: round(v, 3) if isinstance(v, float) else v for k, v in a.items()})
    print("incremental", inc)
    for i in range(12): print(mes[i], *[int(round(B[q][i])) for q in ("gen", "slf", "exp", "compra")], round(B["ah"][i]))
    json.dump(dict(tot=tot, equipo=equipo, serv=serv, serv_crc=serv_crc, costo=costo, ganancia=ganancia, precio=precio, I0=I0,
                   cuota=cuota, B={k: (v.tolist() if hasattr(v, "tolist") else v) for k, v in B.items()}, res=res, sens=sens,
                   alts=alts, inc=inc), open("/home/claude/fv/datos/economia76.json", "w"), indent=1, default=float)
    plt.rcParams.update({"font.family": "STIXGeneral", "mathtext.fontset": "stix", "font.size": 8,
                         "axes.spines.top": False, "axes.spines.right": False})
    x = np.arange(12); w = 0.38
    fig, ax = plt.subplots(figsize=(3.45, 2.2))
    ax.bar(x-w/2, B["sin"]/1e6, w, color="#c4c9cf", label="Sin sistema FV")
    ax.bar(x+w/2, B["con"]/1e6, w, color="#2f5d8a", label="Costo neto con sistema FV")
    ax.set_xticks(x); ax.set_xticklabels(mes, fontsize=7); ax.set_ylabel("Monto mensual [millones de ¢]")
    ax.set_ylim(0, 2.3); ax.legend(fontsize=6.5, frameon=False, ncol=2, loc="upper center")
    ax.grid(axis="y", lw=0.4, color="#e3e3e3"); ax.set_axisbelow(True)
    fig.tight_layout(); fig.savefig("/home/claude/fv/informe/figuras/facturacion.pdf")
    fig.savefig("/home/claude/fv/informe/figuras/facturacion.png", dpi=200)
    fig, ax = plt.subplots(figsize=(3.45, 2.3))
    for nom, c, mk, lab in [("Contado, 0 %", "#2f5d8a", "o", "De contado"), ("Préstamo, 0 %", "#9ab6cf", "s", "Con préstamo del 80 %")]:
        ax.plot(range(26), np.cumsum(res[nom]["F"])/1e6, color=c, marker=mk, ms=2.5, lw=1.2, label=lab)
    ax.axhline(0, color="#666", lw=0.8)
    ax.set_xlabel("Año"); ax.set_ylabel("Flujo acumulado [millones de ¢]"); ax.set_xlim(0, 25)
    ax.legend(fontsize=6.5, frameon=False, loc="upper left")
    ax.grid(lw=0.4, color="#e3e3e3"); ax.set_axisbelow(True)
    fig.tight_layout(); fig.savefig("/home/claude/fv/informe/figuras/flujo_acumulado.pdf")
    fig.savefig("/home/claude/fv/informe/figuras/flujo_acumulado.png", dpi=200)
