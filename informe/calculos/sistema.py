"""Proyecto 2: diseño del sistema FV aislado de respaldo (casa de Abner López, Santa Rosa de Oreamuno).

Procedimiento del curso (Aislado 1 a 4). Todos los datos de equipos salen de las fichas en
equipos/fichas/ y examen4/fichas/; los supuestos están marcados con "SUPUESTO".
Uso: python3 sistema.py  ->  imprime el diseño y guarda resultados.json
"""
import json, math
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
OUT = Path(__file__).with_name("resultados.json")
R = {}

# ----------------------------------------------------------------------------- 1. Consumo
# Cargas críticas (examen4/calculos/levantamiento_cargas_casa.xlsx, datos del grupo y placas)
cargas = [  # (equipo, N, P [W], H [h/día])
    ("Refrigerador Atlas AC12SSAAWA", 1, 196.7, 9),
    ("Congelador Daytron MCHF90", 1, 130.0, 10),
    ("Bombillos LED 15 W (grupo 1)", 3, 15.0, 5),
    ("Bombillos LED 15 W (grupo 2)", 4, 15.0, 2),
    ("Bombillo LED 15 W (grupo 3)", 1, 15.0, 3),
    ("Cargadores de celular (5)", 1, 35.0, 12),
    ("Cargadores de laptop (3)", 1, 51.7, 6),
    ("Módem Nexxt Nebula N300", 1, 6.0, 24),
]
E_CA = sum(n * p * h for _, n, p, h in cargas)
E_CC = 0.0
# Potencia simultánea, peor caso: todo encendido y los 5 cargadores de celular y las 3 laptops a la vez
P_cel = 40 + 35 + 35 + 45 + 20          # placas de los cargadores (dato del grupo)
P_lap = 45.1 + 65.0 + 45.0              # placas Delta, Lenovo y HP
P_sim = 196.7 + 130 + 8 * 15 + P_cel + P_lap + 6
P_comp = 196.7 + 130                    # compresores
k_arr = 4                               # SUPUESTO: arranque de compresor = 4 veces la nominal (cota alta de 3-4x de clase)
P_pico = P_sim - P_comp + k_arr * P_comp
R["consumo"] = dict(E_CA=E_CA, E_CC=E_CC, P_sim=P_sim, P_pico=P_pico,
                    cargas=[dict(eq=e, N=n, P=p, H=h, E=n * p * h) for e, n, p, h in cargas])

# ----------------------------------------------------------------------------- 2. Balance (Aislado 2)
pc, pd, ps, pmppt, pR, pb, pi, Ka = 0.02, 0.04, 0.05, 0.02, 0.05, 0.01, 0.05, 0.005
V, DOD, D = 24, 0.7, 2
K_TCC = (1 - (pc + pd + ps + pmppt + pR + pb)) * (1 - Ka * D / DOD)
K_TCA = (1 - (pc + pd + ps + pmppt + pR + pb + pi)) * (1 - Ka * D / DOD)
E_T = E_CC / K_TCC + E_CA / K_TCA
Q = 1.1 * E_T * D / (V * DOD)
C_bat, n_par = 200, 4
R["balance"] = dict(K_TCC=K_TCC, K_TCA=K_TCA, E_T=E_T, Q=Q, Q_inst=C_bat * n_par,
                    E_banco=25.6 * C_bat * n_par / 1000,
                    autonomia_real=V * C_bat * n_par * DOD / E_T)

# ----------------------------------------------------------------------------- 3. Recurso (PVGIS)
mes = ["Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Set", "Oct", "Nov", "Dic"]
dias = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
pv = {}
for k, f in [("este", "pvgis_PVcalc_12grados_aspect-90.json"), ("oeste", "pvgis_PVcalc_12grados_aspect90.json"),
             ("sur", "pvgis_PVcalc_12grados_sur.json"), ("optimo", "pvgis_PVcalc_optimo.json")]:
    d = json.load(open(RAIZ / "recurso" / f))
    pv[k] = dict(HSP=[m["H(i)_d"] for m in d["outputs"]["monthly"]["fixed"]],
                 E_m=[m["E_m"] for m in d["outputs"]["monthly"]["fixed"]],
                 H_y=d["outputs"]["totals"]["fixed"]["H(i)_y"], E_y=d["outputs"]["totals"]["fixed"]["E_y"],
                 slope=d["inputs"]["mounting_system"]["fixed"]["slope"]["value"],
                 azimuth=d["inputs"]["mounting_system"]["fixed"]["azimuth"]["value"])
mr = json.load(open(RAIZ / "recurso" / "pvgis_MRcalc_mensual.json"))["outputs"]["monthly"]
Hh = [sum(r["H(h)_m"] for r in mr if r["month"] == m + 1) / len([r for r in mr if r["month"] == m + 1]) / dias[m] for m in range(12)]
Hopt = [sum(r["H(i_opt)_m"] for r in mr if r["month"] == m + 1) / len([r for r in mr if r["month"] == m + 1]) / dias[m] for m in range(12)]
pv["horizontal"] = dict(HSP=Hh)
HSP = pv["este"]["HSP"]
m_peor = min(range(12), key=lambda i: HSP[i])
HSP_min = HSP[m_peor]
R["recurso"] = dict(pv=pv, Hopt_MR=Hopt, mes_peor=mes[m_peor], HSP_min=HSP_min)

# ----------------------------------------------------------------------------- 4. Módulo y campo FV (Aislado 1)
mod = dict(P=450, Vmp=33.70, Imp=13.36, Voc=40.69, Isc=14.12, P_noct=339, I_noct=11.42,
           gP=-0.26, gVoc=-0.22, gIsc=0.05)              # ficha AIKO-A450-MAH54Mb
P_campo = E_T / HSP_min                                   # W
N_mod_calc = 1.1 * P_campo / mod["P"]
N_mod = 4
P_inst = N_mod * mod["P"]
# NOCT estimado con la ficha (como en el P1): potencia y corriente a NOCT
T_noct_P = 25 + (mod["P_noct"] / (0.8 * mod["P"]) - 1) / (mod["gP"] / 100)
T_noct_I = 25 + (mod["I_noct"] / (0.8 * mod["Isc"]) - 1) / (mod["gIsc"] / 100)
NOCT = 47.0
gVmp = mod["gP"] - mod["gIsc"]                            # aproximación (no es dato del fabricante)
T_amb_min, T_amb_max = 7.0, 29.5                          # dato del grupo (últimos 12 meses)
T_min = T_amb_min                                         # al amanecer la celda está a la temperatura del aire
T_max = T_amb_max + (NOCT - 20) / 800 * 1000
def corr(x, g, T): return x * (1 + g / 100 * (T - 25))
tabla_T = []
for T in (T_min, 25.0, T_max):
    tabla_T.append(dict(T=T, Voc=corr(mod["Voc"], mod["gVoc"], T), Vmp=corr(mod["Vmp"], gVmp, T),
                        Isc=corr(mod["Isc"], mod["gIsc"], T), Imp=corr(mod["Imp"], mod["gIsc"], T),
                        P=corr(mod["P"], mod["gP"], T)))
R["modulo"] = dict(P_campo=P_campo, N_mod_calc=N_mod_calc, N_mod=N_mod, P_inst=P_inst,
                   T_noct_P=T_noct_P, T_noct_I=T_noct_I, NOCT=NOCT, gVmp=gVmp,
                   T_min=T_min, T_max=T_max, tabla_T=tabla_T)

# ----------------------------------------------------------------------------- 5. Regulador (Aislado 1, 2 y 4)
reg = dict(nombre="Victron SmartSolar MPPT 150/85-Tr VE.Can", I_max=85, P_nom24=2400, Voc_abs=150, Voc_op=145,
           Isc_max=70, eta=0.98)
i_reg = P_inst / V
N_s_max_curso = reg["Voc_op"] / mod["Vmp"]                 # Nserie = Vmax_reg / Vmp (Aislado 2)
Voc_frio = tabla_T[0]["Voc"]; Vmp_cal = tabla_T[2]["Vmp"]
N_s_max = math.floor(reg["Voc_op"] / Voc_frio)
V_abs = 28.8                                               # absorción a 24 V (ficha)
N_s_min = math.ceil((V_abs + 5) / Vmp_cal)                 # el MPPT arranca con Vpv > Vbat + 5 V
Ns, Np = 2, 2
cad = dict(Ns=Ns, Np=Np, Voc_frio=Ns * Voc_frio, Vmp_frio=Ns * tabla_T[0]["Vmp"], Vmp_cal=Ns * Vmp_cal,
           Isc_cal=Np * tabla_T[2]["Isc"], Imp_cal=Np * tabla_T[2]["Imp"], Isc_STC=Np * mod["Isc"],
           P_max=Ns * Np * tabla_T[0]["P"])
I_out_real = P_inst * reg["eta"] / V_abs                   # corriente máxima real hacia el banco (STC)
R["regulador"] = dict(reg=reg, i_reg=i_reg, N_s_max_curso=N_s_max_curso, N_s_max=N_s_max, N_s_min=N_s_min,
                      cadenas=cad, I_out_real=I_out_real, sobredim_P=reg["P_nom24"] / P_inst)

# ----------------------------------------------------------------------------- 6. Inversor-cargador (Aislado 1)
inv = dict(nombre="Victron MultiPlus-II 24/3000/70-50 120V", S=3000, P25=2400, P40=2200, P65=1700, P_pico=5500,
           eta=0.94, Vdc_min=19, Vdc_max=33, I_carga=70, I_transf=50)
I_bat_sim = P_sim / (V * (1 - pi))
I_bat_pico = P_pico / (V * (1 - pi))
I_bat_max_inv = inv["P25"] / (inv["eta"] * 22.4)           # SUPUESTO: 22.4 V = 2.8 V por celda, batería casi descargada
I_bat_carga_total = reg["I_max"] + inv["I_carga"]
R["inversor"] = dict(inv=inv, I_bat_sim=I_bat_sim, I_bat_pico=I_bat_pico, I_bat_max_inv=I_bat_max_inv,
                     uso_cont=P_sim / inv["P25"], uso_pico=P_pico / inv["P_pico"],
                     I_carga_total=I_bat_carga_total, I_bat_lim=200 * n_par)

# ----------------------------------------------------------------------------- 7. Estimación energética
E_gen_d = [P_inst / 1000 * h for h in HSP]                  # kWh/día a la entrada (P·HSP)
E_util_d = [e * K_TCA for e in E_gen_d]                     # kWh/día disponibles para las cargas CA
E_dem_d = E_CA / 1000
mensual = []
for i in range(12):
    mensual.append(dict(mes=mes[i], HSP=HSP[i], E_gen=E_gen_d[i] * dias[i], E_util=E_util_d[i] * dias[i],
                        E_dem=E_dem_d * dias[i], cobertura=min(1, E_util_d[i] / E_dem_d),
                        excedente=max(0, E_util_d[i] - E_dem_d) * dias[i],
                        E_pvgis=pv["este"]["E_m"][i] * P_inst / 1000))
R["energia"] = dict(mensual=mensual, E_gen_y=sum(m["E_gen"] for m in mensual), E_util_y=sum(m["E_util"] for m in mensual),
                    E_dem_y=sum(m["E_dem"] for m in mensual), E_pvgis_y=pv["este"]["E_y"] * P_inst / 1000)

# ----------------------------------------------------------------------------- 8. Cableado (NEC 2014)
# Resistencia DC, NEC Cap. 9 Tabla 8 (cobre trenzado, 75 °C) [ohm/km]; ampacidad Tabla 310.15(B)(16)
Rk = {"10": 3.97, "8": 2.51, "2": 0.634, "1/0": 0.399, "2/0": 0.317}
amp75 = {"10": 35, "8": 50, "2": 115, "1/0": 150, "2/0": 175}
amp90 = {"10": 40, "8": 55, "2": 130, "1/0": 170, "2/0": 195}
L_pv, L_reg, L_bat, L_inv, L_ac = 10.0, 1.5, 1.0, 2.0, 5.0   # SUPUESTOS de distancia (aceptados por el grupo)
tramos = []
def caida_dc(L, I, cal, Vn): return 100 * 2 * L * I * Rk[cal] / 1000 / Vn
# T1: cadena -> caja combinadora junto al regulador (PV Wire 10 AWG, 4 conductores en tubo, techo a 50 °C)
iw1 = 1.25 * 1.25 * tabla_T[2]["Isc"]
cap1 = amp90["10"] * 0.82 * 0.80
tramos.append(dict(t="1", desc="Cadena - caja combinadora", L=L_pv, iw=iw1, cal="10 AWG PV Wire", cap=cap1,
                   dV=caida_dc(L_pv, tabla_T[2]["Imp"], "10", Ns * Vmp_cal)))
# T2: caja combinadora -> regulador (2 cadenas en paralelo, interior)
iw2 = 1.25 * 1.25 * Np * tabla_T[2]["Isc"]
tramos.append(dict(t="2", desc="Combinadora - regulador", L=L_reg, iw=iw2, cal="8 AWG THHN", cap=amp75["8"],
                   dV=caida_dc(L_reg, Np * tabla_T[2]["Imp"], "8", Ns * Vmp_cal)))
# T3: regulador -> barra del banco
iw3 = 1.25 * reg["I_max"]
tramos.append(dict(t="3", desc="Regulador - barra DC", L=L_reg, iw=iw3, cal="2 AWG", cap=amp75["2"],
                   dV=caida_dc(L_reg, reg["I_max"], "2", V)))
# T4: cada batería -> barra DC (los 4 cables de igual longitud). Corriente máxima del banco: la mayor entre la
# descarga del inversor y la carga simultánea del regulador y el cargador; cada batería lleva un cuarto.
I_banco_max = max(I_bat_max_inv, reg["I_max"] + inv["I_carga"])
iw4 = 1.25 * 2 * I_banco_max / n_par                         # SUPUESTO: factor 2 por reparto desigual entre baterías
tramos.append(dict(t="4", desc="Batería - barra DC (x4)", L=L_bat, iw=iw4, cal="2 AWG", cap=amp75["2"],
                   dV=caida_dc(L_bat, 2 * I_banco_max / n_par, "2", V)))
# T5: barra DC -> inversor (NEC 690.8(A)(4): potencia continua / (eficiencia · tensión mínima))
iw5 = 1.25 * I_bat_max_inv
tramos.append(dict(t="5", desc="Barra DC - inversor", L=L_inv, iw=iw5, cal="2/0 AWG", cap=amp75["2/0"],
                   dV=caida_dc(L_inv, I_bat_max_inv, "2/0", V)))
# T6 y T7: lado CA, 120 V
I_ac = inv["S"] / 120
iw6 = 1.25 * I_ac
for t, desc in (("6", "Tablero principal - inversor (entrada CA)"), ("7", "Inversor - subtablero crítico")):
    tramos.append(dict(t=t, desc=desc, L=L_ac, iw=iw6, cal="8 AWG THHN", cap=amp75["8"] * 0.94 / 0.94,
                       dV=100 * 2 * L_ac * I_ac * Rk["8"] / 1000 / 120))
for tr in tramos: tr["ok"] = tr["cap"] >= tr["iw"]
R["cableado"] = tramos

# ----------------------------------------------------------------------------- 9. Protecciones
prot = [
    dict(lugar="Caja combinadora FV", eq="Sin fusibles de cadena (2 cadenas: NEC 690.9(A))", cant=0, usd=0),
    dict(lugar="Caja combinadora FV", eq="Caja MidNite MNPV3 con barra MNPV3-BUSBAR", cant=1, usd=90.78 + 32.99),
    dict(lugar="Caja combinadora FV", eq="Descargador DC MidNite MNSPD-115 (115 V)", cant=1, usd=97.95),
    dict(lugar="Entrada FV del regulador", eq="Protector de falla a tierra con interruptor MidNite MNDC-GFP80 (80 A, 150 V)", cant=1, usd=242.93),
    dict(lugar="Salida del regulador", eq="Interruptor DC MidNite MNEDC125RT (125 A)", cant=1, usd=50.99),
    dict(lugar="Cada batería", eq="Interruptor DC MidNite MNEDC100 (100 A, 150 V)", cant=4, usd=20.99),
    dict(lugar="Entrada DC del inversor", eq="Interruptor DC MidNite MNEDC175 (175 A, 125 V)", cant=1, usd=141.99),
    dict(lugar="Gabinetes DC", eq="Gabinete MidNite MNEDCQUAD (4 interruptores)", cant=2, usd=70.15),
    dict(lugar="Barras DC", eq="Barra MidNite MNBIGBUSBAR (+ y -)", cant=2, usd=66.65),
    dict(lugar="Tablero principal", eq="Interruptor 1P 40 A Square D QO140 (entrada CA)", cant=1, usd=19.62),
    dict(lugar="Subtablero crítico", eq="Centro de carga Square D QO816L100F (8 espacios)", cant=1, usd=76.19),
    dict(lugar="Subtablero crítico", eq="Interruptor 1P 40 A Square D QO140 (principal)", cant=1, usd=19.62),
]
iw_pv_out = 1.25 * Np * 1.25 * mod["Isc"]
R["protecciones"] = dict(lista=prot, I_pv_circ=Np * 1.25 * mod["Isc"], iw_pv_out=iw_pv_out,
                         I_rev_cadena=1.25 * mod["Isc"])

# ----------------------------------------------------------------------------- 10. Estructura
est = [  # (elemento, cantidad, USD unitario) precios PES Supply, oct. 2026 (los mismos del P1)
    ("Riel Unirac SM 240 in (6.1 m), cortado a 4.7 m", 2, 101.10),
    ("Grapa intermedia con unión a tierra Unirac SM BND", 6, 4.15),
    ("Grapa de extremo Unirac SM", 4, 3.55),
    ("Soporte L-Foot Unirac (atornillado a la clavadora, con sello)", 10, 4.35),
    ("Terminal de tierra para riel", 2, 8.40),
]
R["estructura"] = dict(lista=[dict(eq=e, cant=c, usd=u) for e, c, u in est],
                       masa_mod=N_mod * 21.5, area=N_mod * 1.757 * 1.134)

# ----------------------------------------------------------------------------- 11. Costos
TC = 447.54; EURUSD = 1.0997                                  # BCCR, venta, 19 nov. 2026
ft = 3.281
L_cable = {"10 AWG PV Wire": 4 * L_pv * 1.1, "8 AWG THHN": 2 * L_reg * 1.1 + 4 * L_ac * 1.1,
           "2 AWG": (2 * L_reg + 8 * L_bat) * 1.1, "2/0 AWG": 2 * L_inv * 1.1}
p_cable = {"10 AWG PV Wire": 259.99 / 500, "8 AWG THHN": 2.56, "2 AWG": 6.27, "2/0 AWG": 6.07}  # USD/ft
# SUPUESTO: 8 AWG con el precio del THHN 3 AWG del P1 y 2 AWG con el del cable 1/0 (cotas altas)
costos_usd = {
    "Módulos AIKO 450 W (4 x 128.96 EUR)": N_mod * 128.96 * EURUSD,
    "Regulador Victron SmartSolar 150/85-Tr VE.Can": 476.00,
    "Inversor-cargador Victron MultiPlus-II 24/3000/70-50 120V": 997.05,
    "Estructura de montaje": sum(c * u for _, c, u in est),
    "Conductores": sum(L_cable[k] * ft * p_cable[k] for k in L_cable),
    "Protecciones y tableros": sum(p["cant"] * p["usd"] for p in prot),
}
costos_usd["Otros materiales eléctricos (15 %)"] = 0.15 * (costos_usd["Conductores"] + costos_usd["Protecciones y tableros"])
costos_crc = {k: v * TC for k, v in costos_usd.items()}
costos_crc["Baterías Power Queen 24 V 200 Ah (4 x ¢850 000)"] = 4 * 850000
equipo = sum(costos_crc.values())
inst = 300000                                                 # SUPUESTO: mano de obra de instalación, ¢300 000
obra = equipo + inst
serv = {"Diseño, honorarios CFIA (4.5 %)": 0.045 * obra, "Registro ante el CFIA (0.25 %)": 0.0025 * obra,
        "Instalación (supuesto)": inst}
costo = equipo + sum(serv.values())
ganancia = 0.2 * costo
I0 = costo + ganancia
R["costos"] = dict(TC=TC, EURUSD=EURUSD, usd=costos_usd, crc=costos_crc, L_cable=L_cable, equipo=equipo,
                   serv=serv, costo=costo, ganancia=ganancia, I0=I0, por_Wp=I0 / P_inst)

# ----------------------------------------------------------------------------- 12. Proyección financiera
# Factura JASEC T-RE 2026 (consumo/facturas_estimadas_2026.xlsx)
kWh = [237.0, 256.1, 281.0, 257.8, 276.3, 283.7, 241.4, 285.7, 281.9, 275.0, 268.6, 285.7]
def factura(E):
    en = 1863.30 + 62.11 * max(0, min(E, 200) - 30) + 76.02 * max(0, E - 200)
    ap = 80.10 + 2.67 * max(0, E - 30)
    bo = 0.0175 * en if E > 100 else 0
    iv = 0.13 * en if E > 280 else 0
    return round((en + ap + bo + iv) / 5) * 5
E_crit_m = [E_dem_d * d * c["cobertura"] for d, c in zip(dias, mensual)]
sin = [factura(e) for e in kWh]
con = [factura(e - ec) for e, ec in zip(kWh, E_crit_m)]
ahorro1 = sum(sin) - sum(con)
tasa, anos, om, esc = 0.07, 25, 0.01, 0.0                    # mismos supuestos del P1 (tasa 7 %, O&M 1 %/año)
# SUPUESTO: inversor y regulador se reemplazan en el año 13 (vida típica 12-15 años, no declarada en ficha);
# baterías: 6000 ciclos al 80 % (ficha) con ~22 % de descarga diaria -> no limitan por ciclos en 25 años;
# como la ficha no da vida calendario, se supone un reemplazo de baterías en el año 15.
rep = {13: (costos_crc["Regulador Victron SmartSolar 150/85-Tr VE.Can"] + costos_crc["Inversor-cargador Victron MultiPlus-II 24/3000/70-50 120V"]),
       15: 4 * 850000}
F = [-I0]
for k in range(1, anos + 1):
    a = ahorro1 * (1 - 0.01 - 0.0035 * (k - 1)) * (1 + esc) ** (k - 1)  # degradación del módulo (ficha AIKO)
    a = min(a, ahorro1 * (1 + esc) ** (k - 1))
    F.append(a - om * I0 - rep.get(k, 0))
VAN = sum(f / (1 + tasa) ** k for k, f in enumerate(F))
acum = []; s = 0
for f in F: s += f; acum.append(s)
pri = next((k for k, a in enumerate(acum) if a >= 0), None)
def tir(F):
    lo, hi = -0.99, 1.0
    def npv(r): return sum(f / (1 + r) ** k for k, f in enumerate(F))
    if npv(lo) * npv(hi) > 0: return None
    for _ in range(200):
        mid = (lo + hi) / 2
        if npv(lo) * npv(mid) <= 0: hi = mid
        else: lo = mid
    return mid
VP_E = sum(sum(E_crit_m) * (1 - 0.01 - 0.0035 * (k - 1)) / (1 + tasa) ** k for k in range(1, anos + 1))
VP_C = I0 + sum((om * I0 + rep.get(k, 0)) / (1 + tasa) ** k for k in range(1, anos + 1))
R["finanzas"] = dict(LCOE=VP_C / VP_E, DOD_diaria=E_CA / (1 - pi) / (R["balance"]["E_banco"] * 1000), kWh=kWh, E_crit_m=E_crit_m, sin=sin, con=con, ahorro1=ahorro1,
                     ahorro_pct=ahorro1 / sum(sin), F=F, acum=acum, VAN=VAN, TIR=tir(F), PRI=pri,
                     rep=rep, tasa=tasa, om=om, anos=anos,
                     simple=I0 / (ahorro1 - om * I0) if ahorro1 > om * I0 else None)

json.dump(R, open(OUT, "w"), indent=1, ensure_ascii=False, default=float)

# ----------------------------------------------------------------------------- impresión
c = R["consumo"]; b = R["balance"]; m = R["modulo"]; r = R["regulador"]; iv = R["inversor"]
print(f"E_CA = {c['E_CA']:.1f} Wh/día   P_sim = {c['P_sim']:.1f} W   P_pico = {c['P_pico']:.0f} W")
print(f"K_TCA = {b['K_TCA']:.4f}  E_T = {b['E_T']:.0f} Wh/día  Q = {b['Q']:.0f} Ah -> 800 Ah, {b['E_banco']:.2f} kWh, autonomía real {b['autonomia_real']:.2f} d")
print(f"Peor mes {R['recurso']['mes_peor']} HSP = {HSP_min}  P_campo = {m['P_campo']:.0f} W  N = {m['N_mod_calc']:.2f} -> {N_mod} ({P_inst} Wp)")
print(f"NOCT estimado: {m['T_noct_P']:.1f} (P) / {m['T_noct_I']:.1f} (I) -> 47 °C;  T celda {m['T_min']} a {m['T_max']:.1f} °C")
for t in m["tabla_T"]: print("   T={T:5.1f}  Voc={Voc:.2f}  Vmp={Vmp:.2f}  Isc={Isc:.2f}  Imp={Imp:.2f}  P={P:.1f}".format(**t))
print(f"i_reg = {r['i_reg']:.1f} A (<= 85 A)  Nserie curso = {r['N_s_max_curso']:.2f}; por Voc frío máx {r['N_s_max']}, mín {r['N_s_min']}")
print("Arreglo 2S2P:", {k: round(v, 2) for k, v in r["cadenas"].items()}, f"I_out real = {r['I_out_real']:.1f} A, P_nom/P_inst = {r['sobredim_P']:.2f}")
print(f"Inversor: P_sim/P25 = {iv['uso_cont']:.0%}  P_pico/5500 = {iv['uso_pico']:.0%}  I_bat sim {iv['I_bat_sim']:.1f} A, pico {iv['I_bat_pico']:.1f} A, máx inv {iv['I_bat_max_inv']:.1f} A; carga total {iv['I_carga_total']} A")
e = R["energia"]
print(f"Energía: gen {e['E_gen_y']:.0f} kWh/año, útil {e['E_util_y']:.0f}, demanda {e['E_dem_y']:.0f}, PVGIS {e['E_pvgis_y']:.0f}")
for x in e["mensual"]: print("   {mes} HSP {HSP:.2f} gen {E_gen:6.1f} util {E_util:6.1f} dem {E_dem:6.1f} cob {cobertura:.0%} exc {excedente:5.1f} pvgis {E_pvgis:6.1f}".format(**x))
for t in tramos: print("   T{t} {desc:42s} L={L:4.1f} iw={iw:6.1f} {cal:15s} cap={cap:6.1f} dV={dV:4.2f}% {ok}".format(**t))
print("Protecciones: I_pv_circ = {I_pv_circ:.1f} A, iw salida FV = {iw_pv_out:.1f} A, I inversa cadena = {I_rev_cadena:.1f} A".format(**R["protecciones"]))
co = R["costos"]
for k, v in co["crc"].items(): print(f"   {k:60s} ¢{v:12,.0f}")
for k, v in co["serv"].items(): print(f"   {k:60s} ¢{v:12,.0f}")
print(f"Equipo ¢{co['equipo']:,.0f}  costo ¢{co['costo']:,.0f}  ganancia ¢{co['ganancia']:,.0f}  PRECIO ¢{co['I0']:,.0f} ({co['I0']/TC:,.0f} USD, {co['por_Wp']:.0f} ¢/Wp)")
f = R["finanzas"]
print("Facturas sin:", f["sin"], sum(f["sin"]))
print("Facturas con:", f["con"], sum(f["con"]))
print(f"LCOE ¢{f['LCOE']:.0f}/kWh  DOD diaria {f['DOD_diaria']:.1%}")
print(f"Ahorro año 1 ¢{f['ahorro1']:,.0f} ({f['ahorro_pct']:.0%})  O&M ¢{om*I0:,.0f}  VAN ¢{f['VAN']:,.0f}  TIR {f['TIR']}  PRI {f['PRI']}  simple {f['simple']}")
