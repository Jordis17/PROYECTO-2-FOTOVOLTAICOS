"""Evaluación económica final. Caso base: medición neta sencilla (depósito y devolución, 49 % de la generación,
tarifa de acceso sobre la energía devuelta). Venta de excedentes como sensibilidad.
Sistema seleccionado: 76.5 kWp (170 módulos, 10 cadenas de 17, 2 inversores CPS de 25 kW).
Comparación de alternativas con el mismo modelo de costos y de factura."""
import json, math, numpy as np, matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
TC, EURUSD = 456.61, 1.1479
mes = ["Ene","Feb","Mar","Abr","May","Jun","Jul","Ago","Set","Oct","Nov","Dic"]
C = np.array([18482,17626,18238,18850,19339,18482,18972,19094,18238,18727,17993,18972.])
D = np.array([43.70,49.33,45.78,46.14,46.88,45.78,44.19,47.25,53.00,47.12,44.92,44.31])
pe, pd_, pa, iva, bomb = 59.67, 9861.68, 2.70, 0.13, 1827.40
p_exc, tder, t_acc = 27.40, 255.0, 25.0
v_kwh = pe*(1+iva) + pa
H = json.load(open("/home/claude/fv/datos/balance_horario_final.json"))

# ---------------- Costos (mismos precios unitarios para todas las alternativas) ----------------
P_MOD, P_INV, P_EST = 128.96*EURUSD, 8997.44, 19550/170
def costo(nmod, ninv, ncad, kwp, detalle=False):
    t = {}
    t["Módulos"] = nmod*P_MOD
    t["Inversores"] = ninv*P_INV
    t["Estructura"] = nmod*P_EST
    reels = math.ceil(ncad*80*3.281/500)          # 2 x 40 m de PV Wire por cadena
    I = 1.25*ninv*69.5
    if I <= 175:   feeder, gen_, sec = 148*6.98, 3120.00, 976.33          # 3/0, 175 A, 200 A
    elif I <= 300: feeder, gen_, sec = 148*10.0, 3600.00, 2320.00         # 350 kcmil (est.), 300 A (est.), 400 A (est.)
    elif I <= 400: feeder, gen_, sec = 2*148*6.5, 4100.00, 2320.00        # 2x4/0 (est.), 350 A (est.), 400 A (est.)
    else:          feeder, gen_, sec = 2*148*9.84, 5742.00, 3407.03       # 2x250 kcmil, 450 A (MAL36450), 600 A (HU366)
    t["Conductores"] = reels*259.99 + ninv*148*2.56 + feeder
    t["Protecciones"] = ninv*1174.50 + gen_ + sec
    t["Otros materiales eléctricos (15 %)"] = 0.15*(t["Conductores"] + t["Protecciones"])
    t = {k: round(v) for k, v in t.items()}
    equipo = sum(t.values())
    # Valor de la obra (equipos + instalación) para honorarios y cargos del CFIA
    inst = 100000*kwp                                   # supuesto declarado: ¢100 000 por kWp
    obra = equipo*TC + inst
    serv = {"Diseño: estudios preliminares y planos (4.5 %)": round(0.045*obra),   # Decreto 18636-MOPT, art. 4 C y CH b)
            "Registro ante el CFIA (0.25 %)": round(0.0025*obra),                 # derecho de asistencia 0.15 % + timbre 0.10 %
            "Interconexión ICE (etapas 1-4)": 382871,                             # ICE, RE-0031-IE-2026
            "Instalación (¢100 000/kWp)": round(inst)}
    servu = {k: round(v/TC) for k, v in serv.items()}
    c = equipo + sum(servu.values()); g = round(0.2*c); precio = c + g
    if detalle: return dict(tot=t, equipo=equipo, obra_crc=obra, serv=servu, serv_crc=serv, costo=c, ganancia=g, precio=precio, I0=precio*TC)
    return precio*TC

# ---------------- Factura y flujo ----------------
def factura(E, Dem, kwp=0.0, acc=0.0):
    en = E*pe; de = Dem*pd_; al = E*pa; t = tder*kwp
    return en + de + al + iva*(en + de + t + acc) + t + acc + bomb
def balance(gen, slf, kwp, modelo="neteo", red=0.0, acceso=False):
    """modelo: 'neteo' (medición neta sencilla, caso base), 'venta' (excedentes a ¢27.40 + TDER) o 'sin_exc'."""
    exp = gen - slf; need = C - slf; sin = factura(C, D)
    rec = np.minimum(exp, 0.49*gen); nr = exp - rec
    if modelo == "neteo":
        acc = 0.0; use = np.zeros(12)
        for i in range(12):                     # acumulado mensual dentro del año (neteo anual)
            acc += rec[i]; use[i] = min(acc, need[i]); acc -= use[i]
        buy = need - use
        if acceso:   # variante con tarifa de acceso sobre la energía devuelta (ejemplo de clase) y sin TDER
            con = factura(buy, D*(1-red), 0.0, acc=use*t_acc)
            s_gen = (slf*v_kwh).sum() + (use*(v_kwh - t_acc*(1+iva))).sum(); s_fijo = red*(D*pd_*(1+iva)).sum()
        else:        # caso base: tarifa de acceso solo aplica a tarifas monómicas (RE-0076-JD-2023); se cobra la TDER
            con = factura(buy, D*(1-red), kwp)
            s_gen = (slf*v_kwh).sum() + (use*v_kwh).sum(); s_fijo = -tder*kwp*12*(1+iva) + red*(D*pd_*(1+iva)).sum()
        extra = dict(rec=rec, nr=nr, use=use, buy=buy, perdido=acc)
    elif modelo == "venta":
        buy = need
        con = factura(buy, D*(1-red), kwp) - exp*p_exc
        s_gen = (slf*v_kwh).sum() + (exp*p_exc).sum(); s_fijo = -tder*kwp*12*(1+iva) + red*(D*pd_*(1+iva)).sum()
        extra = {}
    else:
        buy = need
        con = factura(buy, D*(1-red), 0.0)
        s_gen = (slf*v_kwh).sum(); s_fijo = red*(D*pd_*(1+iva)).sum(); extra = {}
    return dict(gen=gen, slf=slf, exp=exp, compra=buy, need=need, sin=sin, con=con, ah=sin-con, sg=s_gen, sf=s_fijo, **extra)
r_p, n_p, tasa, anos, om, d1, d2 = 0.09, 120, 0.07, 25, 0.01, 0.01, 0.0035
def flujo(I0, sg, sf, esc=0.0, fin=False):
    cuota = 0.8*I0*(r_p/12)/(1-(1+r_p/12)**-n_p)
    F = [-(0.2*I0 if fin else I0)]
    for k in range(1, anos+1):
        deg = (1-d1)*(1-d2)**(k-1)
        F.append((sg*deg + sf)*(1+esc)**(k-1) - om*I0*(1+esc)**(k-1) - (12*cuota if (fin and k <= 10) else 0))
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
def ind(F, I0): return dict(vpn=vpn(F), tir=tir(F), pri=pri(F), ir=1+vpn(F)/I0)

# ---------------- Sistema seleccionado ----------------
kWp = 168.3
CO = costo(374, 5, 22, kWp, detalle=True); I0 = CO["I0"]
gen = np.round(np.load("/home/claude/fv/datos/E_final.npy"))
def bal(k=0.75, **kw): return balance(gen, np.array(H[f"N22_{k}"]["self"], float), kWp, **kw)
B = bal()
res = {}
for nom, kw in [("Contado, 0 %", {}), ("Contado, 3 %", dict(esc=0.03)),
                ("Préstamo, 0 %", dict(fin=True)), ("Préstamo, 3 %", dict(esc=0.03, fin=True))]:
    F, cuota = flujo(I0, B["sg"], B["sf"], **kw); res[nom] = dict(ind(F, 0.2*I0 if "Préstamo" in nom else I0), F=F.tolist())
sens = {}
for nom, kw in {"Caso base": {}, "Demanda −10 %": dict(red=.1), "Demanda −20 %": dict(red=.2),
                "Neteo con tarifa de acceso": dict(acceso=True), "Venta de excedentes (¢27.40 y TDER)": dict(modelo="venta"), "Excedentes sin reconocimiento": dict(modelo="sin_exc"),
                "Carga 50 %": dict(k=0.5), "Carga 65 %": dict(k=0.65), "Carga 85 %": dict(k=0.85)}.items():
    b = bal(**kw); F, _ = flujo(I0, b["sg"], b["sf"]); sens[nom] = dict(ind(F, I0), ah=b["ah"].sum())
Fb0, _ = flujo(I0, B["sg"], B["sf"])
for t_ in (0.05, 0.09):
    sens[f"Tasa de descuento {round(t_*100)} %"] = dict(vpn=float(sum(f/(1+t_)**i for i, f in enumerate(Fb0))), tir=tir(Fb0), pri=pri(Fb0), ir=None, ah=B["ah"].sum())
Fp, _ = flujo(1.15*I0, B["sg"], B["sf"]); sens["Precio del sistema +15 %"] = dict(ind(Fp, 1.15*I0), ah=B["ah"].sum())

# ---------------- Alternativas (cadenas de 17 módulos) ----------------
ALT = [("N10_0.75", 10, 2), ("N14_0.75", 14, 3), ("N18_0.75", 18, 4), ("N20_0.75", 20, 4), ("N22_0.75", 22, 5)]
alts = []
for key, nc, ninv in ALT:
    p = round(nc*7.65, 2); nmod = nc*17
    g_ = np.array(H[key]["gen"], float); s_ = np.array(H[key]["self"], float)
    b = balance(g_, s_, p); Ia = costo(nmod, ninv, nc, p)
    F, _ = flujo(Ia, b["sg"], b["sf"])
    alts.append(dict(Pdc=p, ncad=nc, nmod=nmod, ninv=ninv, Pac=25*ninv, dcac=p/(25*ninv), I=Ia, gen=b["gen"].sum(),
                     cob=b["gen"].sum()/C.sum(), slf=b["slf"].sum(), dep=b["exp"].sum()/b["gen"].sum(), nr=b["nr"].sum(),
                     compra=b["compra"].sum(), ah=b["ah"].sum(), **ind(F, Ia)))
inc = {}

if __name__ == "__main__":
    print("COSTO", CO["tot"], CO["equipo"], CO["serv"], CO["costo"], CO["ganancia"], CO["precio"], round(I0/1e6, 3), round(CO["precio"]/168300, 3))
    print("gen", B["gen"].sum(), "self", B["slf"].sum(), "exp", B["exp"].sum(), "rec", B["rec"].sum(), "nr", B["nr"].sum(),
          "use", B["use"].sum(), "perdido fin de año", B["perdido"], "compra", B["compra"].sum(), "red", 1-B["compra"].sum()/C.sum())
    print("sin", B["sin"].sum(), "con", B["con"].sum(), "ah", B["ah"].sum(), B["ah"].sum()/B["sin"].sum(), "acceso", (B["use"]*t_acc).sum(),
          "año1", B["sg"]*(1-d1)+B["sf"], "cuota", cuota)
    for k, v in res.items(): print(k, round(v["vpn"]/1e6, 2), round(v["tir"]*100, 1), round(v["pri"], 1), round(v["ir"], 2))
    for k, v in sens.items(): print(k, round(v["ah"]/1e6, 2), round(v["vpn"]/1e6, 1), round(v["tir"]*100, 1), round(v["pri"], 1))
    print("obra", CO["obra_crc"], CO["serv_crc"])
    for a in alts: print(a["Pdc"], a["ninv"], round(a["dcac"], 2), round(a["I"]/1e6, 1), round(a["gen"]/1e3, 1), round(100*a["cob"], 1), round(a["slf"]/1e3, 1),
                         round(100*a["dep"], 1), round(a["nr"]), round(a["compra"]/1e3, 1), round(a["ah"]/1e6, 2), round(a["vpn"]/1e6, 1), round(a["tir"]*100, 1), round(a["pri"], 1))
    for i in range(12): print(mes[i], *[int(round(B[q][i])) for q in ("gen", "slf", "exp", "rec", "use", "compra")], round(B["ah"][i]/1000))
    json.dump(dict(CO=CO, I0=I0, cuota=cuota, B={k: (v.tolist() if hasattr(v, "tolist") else v) for k, v in B.items()},
                   res=res, sens=sens, alts=alts, inc=inc), open("/home/claude/fv/datos/economia_final.json", "w"), indent=1, default=float)
    plt.rcParams.update({"font.family": "STIXGeneral", "mathtext.fontset": "stix", "font.size": 8,
                         "axes.spines.top": False, "axes.spines.right": False})
    x = np.arange(12); w = 0.38
    fig, ax = plt.subplots(figsize=(3.45, 2.2))
    ax.bar(x-w/2, B["sin"]/1e6, w, color="#c4c9cf", label="Sin sistema FV")
    ax.bar(x+w/2, B["con"]/1e6, w, color="#2f5d8a", label="Costo neto con sistema FV")
    ax.set_xticks(x); ax.set_xticklabels(mes, fontsize=7); ax.set_ylabel("Monto mensual [millones de ¢]")
    ax.set_ylim(0, 2.3); ax.legend(fontsize=6.5, frameon=False, ncol=2, loc="upper center")
    ax.grid(axis="y", lw=0.4, color="#e3e3e3"); ax.set_axisbelow(True)
    fig.tight_layout(); fig.savefig("/home/claude/fv/informe/figuras/facturacion.pdf"); fig.savefig("/home/claude/fv/informe/figuras/facturacion.png", dpi=200)
    fig, ax = plt.subplots(figsize=(3.45, 2.3))
    for nom, c, mk, lab in [("Contado, 0 %", "#2f5d8a", "o", "De contado"), ("Préstamo, 0 %", "#9ab6cf", "s", "Con préstamo del 80 %")]:
        ax.plot(range(26), np.cumsum(res[nom]["F"])/1e6, color=c, marker=mk, ms=2.5, lw=1.2, label=lab)
    ax.axhline(0, color="#666", lw=0.8)
    ax.set_xlabel("Año"); ax.set_ylabel("Flujo acumulado [millones de ¢]"); ax.set_xlim(0, 25)
    ax.legend(fontsize=6.5, frameon=False, loc="upper left"); ax.grid(lw=0.4, color="#e3e3e3"); ax.set_axisbelow(True)
    fig.tight_layout(); fig.savefig("/home/claude/fv/informe/figuras/flujo_acumulado.pdf"); fig.savefig("/home/claude/fv/informe/figuras/flujo_acumulado.png", dpi=200)
