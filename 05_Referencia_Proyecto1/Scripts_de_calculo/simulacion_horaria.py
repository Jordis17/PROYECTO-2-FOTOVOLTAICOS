"""Balance horario generación–carga del sistema de 168.3 kWp (22 cadenas, 5 inversores) y de las alternativas (reproducible).

Uso (requiere internet para la primera descarga):
    python simulacion_horaria.py            # descarga NASA POWER 2015-2024 y calcula
    python simulacion_horaria.py --sin-descarga   # usa datos/nasa_power_horario_2015_2024.csv

Procedimiento (el mismo de scripts/autoconsumo_horario.js):
 1. Datos horarios de NASA POWER (ALLSKY_SFC_SW_DWN = GHI [Wh/m2] y T2M [°C]), 2015-2024, en hora
    estándar local (LST, UTC-6). La marca HH corresponde a la hora que inicia en HH:00.
 2. Pérdida por temperatura de referencia (solo informativa): Tc = T2M + (NOCT-20)/800*G con NOCT = 47 °C;
    pérdida = Σ G·0.26 %·(Tc-25) / Σ G  (≈ 4.3 %). El diseño usa la pérdida mensual con G = 1000 W/m2 (7.6–8.1 %).
 3. Energía mensual de diseño por kWp: HSP(10°, factores K)·PR_mes_sin_recorte·días, con la pérdida
    térmica de cada mes (diseno_final.py). La generación de cada hora se reparte con la forma horaria de la GHI:
    g_h = GHI_h · E_mes / promedio_anual(Σ GHI del mes)   [kWh por kWp].
    (Con 10° de inclinación la forma horaria de la GHI se usa como aproximación de la del plano inclinado.)
 4. Potencia de cada inversor = g_h · kWp_inversor, recortada a 25 kW (recorte del inversor).
 5. Carga supuesta (no medida): lunes a sábado de 6:00 a 21:00 = k·D_mes (D_mes = demanda facturada);
    resto de horas = carga constante que completa el consumo facturado del mes. k = 0.75 en el caso base.
 6. Para cada hora: autoconsumo = min(generación, carga); exportación = generación - autoconsumo.
    Se suman los 10 años y se dividen entre 10 (año promedio).
"""
import sys, json, csv, datetime, os
import numpy as np

LAT, LON = 9.3769, -83.7019
DATA = os.path.join(os.path.dirname(__file__), "..", "datos", "nasa_power_horario_2015_2024.csv")
# Energía mensual por kWp sin recorte, con PR mensual (pérdida térmica de cada mes, Sección V, factores K a 10°)
YKWP_811 = [119.552,119.396,133.251,113.613,102.708,97.453,98.85,104.945,108.918,104.475,94.172,108.863]  # PR mensual (diseno_final.py)
C = [18482,17626,18238,18850,19339,18482,18972,19094,18238,18727,17993,18972]
D = [43.70,49.33,45.78,46.14,46.88,45.78,44.19,47.25,53.00,47.12,44.92,44.31]

def descargar(path=DATA):
    import requests
    rows = []
    for y in range(2015, 2025):
        u = ("https://power.larc.nasa.gov/api/temporal/hourly/point?parameters=ALLSKY_SFC_SW_DWN,T2M"
             f"&community=RE&longitude={LON}&latitude={LAT}&start={y}0101&end={y}1231&format=JSON&time-standard=LST")
        p = requests.get(u, timeout=120).json()["properties"]["parameter"]
        for k in p["ALLSKY_SFC_SW_DWN"]:
            rows.append((k, max(0.0, p["ALLSKY_SFC_SW_DWN"][k]), p["T2M"][k]))
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", newline="") as f:
        w = csv.writer(f); w.writerow(["YYYYMMDDHH_LST", "GHI_Wh_m2", "T2M_C"]); w.writerows(rows)
    return path

def leer(path=DATA):
    t, G, T = [], [], []
    with open(path) as f:
        r = csv.reader(f); next(r)
        for k, g, tt in r: t.append(k); G.append(float(g)); T.append(float(tt))
    return t, np.array(G), np.array(T)

def simular(t, G, T, kwp_inv=(38.25, 38.25, 30.6, 30.6, 30.6), pac=25.0, k=0.75, noct=47.0, gp=0.26):
    y = np.array([int(s[:4]) for s in t]); m = np.array([int(s[4:6])-1 for s in t])
    d = np.array([int(s[6:8]) for s in t]); h = np.array([int(s[8:10]) for s in t])
    dow = np.array([datetime.date(a, b+1, c).isoweekday() % 7 for a, b, c in zip(y, m, d)])  # 0 = domingo
    nyears = len(set(y))
    # 2. pérdida por temperatura ponderada con la irradiancia
    Tc = T + (noct-20)/800*G; mask = G > 0
    perd = float((G[mask]*gp/100*(Tc[mask]-25)).sum()/G[mask].sum())
    # 3. generación horaria por kWp
    ykwp = np.array(YKWP_811)       # PR mensual (pérdida térmica de cada mes)
    S = np.array([G[m == i].sum()/nyears for i in range(12)])
    g = G*ykwp[m]/S[m]
    # 4. potencia por inversor con recorte
    gen = np.zeros_like(g); clip = 0.0
    for p in kwp_inv:
        gi = g*p; clip += np.clip(gi-pac, 0, None).sum(); gen += np.minimum(gi, pac)
    # 5. carga supuesta
    abierto = (dow != 0) & (h >= 6) & (h <= 20)
    carga = np.zeros_like(g)
    for yy in set(y):
        for i in range(12):
            sel = (y == yy) & (m == i)
            n_o = (sel & abierto).sum(); n_c = (sel & ~abierto).sum()
            Pc = (C[i]-k*D[i]*n_o)/n_c
            carga[sel & abierto] = k*D[i]; carga[sel & ~abierto] = Pc
    # 6. balance
    auto = np.minimum(gen, carga); exp = gen-auto
    mens = lambda v: [float(v[m == i].sum()/nyears) for i in range(12)]
    return dict(perdida_temperatura=perd, gen=mens(gen), self=mens(auto), exp=mens(exp),
                clip=clip/nyears, horas_Vmp17_bajo_480=float(((17*33.70*(1-0.0031*(Tc-25))) < 480)[mask].sum()/nyears))

if __name__ == "__main__":
    path = DATA if "--sin-descarga" in sys.argv else descargar()
    t, G, T = leer(path)
    res = {}
    # Cadenas de 17 módulos de 0.45 kW: 5 cadenas = 38.25 kWp y 4 cadenas = 30.6 kWp por inversor
    A, B = 38.25, 30.6
    alts = {"N10": (A, A), "N14": (A, A, B), "N18": (A, A, B, B), "N20": (A, A, A, A), "N22": (A, A, B, B, B)}
    for n, inv in alts.items():
        r = simular(t, G, T, kwp_inv=inv); res[n + "_0.75"] = r
        print(f"{n}: generación {sum(r['gen']):.0f} kWh, autoconsumo {sum(r['self']):.0f} kWh, recorte {r['clip']:.0f} kWh")
    for k in (0.5, 0.65, 0.85):
        r = simular(t, G, T, kwp_inv=alts["N22"], k=k); res[f"N22_{k}"] = r
        print(f"N22, k={k}: autoconsumo {sum(r['self']):.0f} kWh, horas con Vmp(17) < 480 V: {r['horas_Vmp17_bajo_480']:.1f}")
    json.dump(res, open(os.path.join(os.path.dirname(__file__), "..", "datos", "simulacion_horaria_final.json"), "w"), indent=1)
