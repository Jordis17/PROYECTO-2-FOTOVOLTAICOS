"""Examen corto 4: matriz comparativa de baterías y dimensionamiento del banco.

Uso: python3 baterias.py
Cuando se tenga el consumo de la casa, se cambian E_CC y E_CA (Wh/día) y D
(días de autonomía) en la sección "Consumo real".
"""
import math

# ---------------------------------------------------------------------------
# 1. Matriz comparativa (datos verificados el 5 nov. 2026; ver notas/verificacion_fichas.md)
# ---------------------------------------------------------------------------
EUR_USD = 1 / 0.8879  # Infobae, 5 nov. 2026 (1 USD = 0.8879 EUR)
CRC_USD = 454.41      # BCCR, tipo de cambio de referencia de venta, 5 nov. 2026 (CRC por USD)

modelos = [
    # id, nombre, V unidad, Ah (C20 para plomo-ácido), unidades para 24 V, precio unitario USD,
    # DOD a la que el fabricante declara los ciclos, ciclos a esa DOD, kg por unidad
    dict(id="B1", nombre="Trojan T-105", V=6, Ah=225, n24=4, precio=225.00, dod=0.50, ciclos=1200, kg=28.0),
    # B2: precio pendiente (None); ciclos declarados al 100 % de DOD
    dict(id="B2", nombre="Trojan SAES 12 205", V=12, Ah=179, n24=2, precio=None, dod=1.00, ciclos=1200, kg=57.0),
    dict(id="B3", nombre="Ultracell UCG200-12", V=12, Ah=206, n24=2, precio=358.38 * EUR_USD, dod=0.50, ciclos=1200, kg=62.2),
    dict(id="B4", nombre="Power Queen 24V 100Ah", V=25.6, Ah=100, n24=1, precio=399.99, dod=0.80, ciclos=6000, kg=20.68),
    dict(id="B5", nombre="Victron 25.6V/200Ah Smart-a", V=25.6, Ah=200, n24=1, precio=2983.50, dod=0.80, ciclos=2500, kg=39.0),
]

print("Matriz comparativa (módulo de 24 V)")
print(f"{'':3} {'precio 24V':>10} {'E nom kWh':>9} {'E útil':>7} {'USD/kWh útil':>12} {'@70%':>7} {'USD/kWh vida':>12} {'kg':>6}")
for m in modelos:
    e_nom = m["V"] * m["n24"] * m["Ah"] / 1000          # kWh
    e_util = e_nom * m["dod"]
    m.update(e_nom=e_nom, e_util=e_util, kg24=m["kg"] * m["n24"])
    if m["precio"] is None:
        print(f"{m['id']:3} {'n.d.':>10} {e_nom:9.2f} {e_util:7.2f} {'n.d.':>12} {'n.d.':>7} {'n.d.':>12} {m['kg24']:6.1f}")
        continue
    precio24 = m["precio"] * m["n24"]
    c_util = precio24 / e_util                            # ecuación (1)
    c_70 = precio24 / (e_nom * 0.70)                      # misma base que el diseño
    c_vida = precio24 / (e_util * m["ciclos"])            # USD por kWh entregado en la vida en ciclos
    m.update(precio24=precio24, c_util=c_util, c_70=c_70, c_vida=c_vida)
    print(f"{m['id']:3} {precio24:10.2f} {e_nom:9.2f} {e_util:7.2f} {c_util:12.1f} {c_70:7.1f} {c_vida:12.3f} {m['kg24']:6.1f}")

# Precios en Costa Rica (5 nov. 2026), en colones, como referencia
print("\nReferencia con precios de Costa Rica (CRC)")
cr = [
    # nombre, precio por unidad CRC, unidades para 24 V, kWh nominales del módulo de 24 V, DOD de los ciclos
    ("B4 Power Queen 24V 100Ah (Kuat)", 400000, 1, 2.56, 0.80),
    ("Gel 12V 200Ah C20, marca n.d. (LEDXPRES)", 395000, 2, 4.80, 0.50),
]
for nombre, crc, n, e_nom, dod in cr:
    total = crc * n
    print(f"  {nombre}: {total:,.0f} CRC = {total/CRC_USD:8.2f} USD; "
          f"{total/(e_nom*dod):,.0f} CRC/kWh útil = {total/(e_nom*dod)/CRC_USD:6.1f} USD/kWh útil")

# ---------------------------------------------------------------------------
# 2. Dimensionamiento (procedimiento del curso, Aislado 1 y 2)
# ---------------------------------------------------------------------------
V_SIS = 24.0     # V
DOD = 0.70       # profundidad de descarga de diseño
MARGEN = 1.1     # margen de seguridad de la fórmula del curso

# Pérdidas típicas del curso (deben reemplazarse por las de las fichas del regulador e inversor)
p = dict(pc=0.02, pd=0.04, ps=0.05, pmppt=0.02, pR=0.05, pb=0.01, pi=0.05)
Ka = 0.005


def K_T(D, ca=True):
    """Factor de rendimiento K_TCA (ca=True) o K_TCC (ca=False)."""
    suma = p["pc"] + p["pd"] + p["ps"] + p["pmppt"] + p["pR"] + p["pb"] + (p["pi"] if ca else 0)
    return (1 - suma) * (1 - Ka * D / DOD)


def capacidad(E_CC, E_CA, D):
    """Devuelve (E_T corregida en Wh/día, Q en Ah) para el banco de 24 V."""
    E_T = E_CC / K_T(D, ca=False) + E_CA / K_T(D, ca=True)
    Q = MARGEN * E_T * D / (V_SIS * DOD)
    return E_T, Q


print("\nK_TCC, K_TCA:", {D: (round(K_T(D, False), 4), round(K_T(D, True), 4)) for D in (1, 2, 3)})

# Power Queen 24V 100Ah: máximo 4 en paralelo (4P2S, manual p. 08) -> 400 Ah a 24 V
Q_MAX_B4 = 4 * 100
for D in (1, 2, 3):
    E_max = Q_MAX_B4 * V_SIS * DOD / (MARGEN * D) * K_T(D, ca=True)   # Wh/día de cargas en CA
    print(f"B4, 4 en paralelo, D={D}: consumo máximo de las cargas = {E_max:.0f} Wh/día")

print("\nTabla PROVISIONAL (todas las cargas en CA)")
consumos = [1000, 2000, 3000, 4000, 5000, 6000]   # Wh/día de las cargas
for D in (1, 2, 3):
    fila = []
    for E in consumos:
        E_T, Q = capacidad(0, E, D)
        n4 = math.ceil(Q/100)
        fila.append(f"{E/1000:.0f} kWh: E_T={E_T:6.0f} Q={Q:6.0f} Ah ({n4}xB4{'' if n4 <= 4 else ' >4P'})")
    print(f"D={D}:", " | ".join(fila))

# ---------------------------------------------------------------------------
# 3. Consumo real (levantamiento de cargas del 11 nov. 2026; ver levantamiento_cargas_casa.xlsx)
# ---------------------------------------------------------------------------
# Cargas críticas (todas en CA): N, P [W], H [h/día]
cargas = {
    "Refrigerador Atlas AC12SSAAWA (115 V x 1.71 A)": (1, 115 * 1.71, 9),
    "Congelador Daytron MCHF90": (1, 130, 10),
    "Bombillos LED Sylvania 15 W, grupo 1": (3, 15, 5),
    "Bombillos LED Sylvania 15 W, grupo 2": (4, 15, 2),
    "Bombillo LED Sylvania 15 W, grupo 3": (1, 15, 3),
    "Cargadores de laptop (promedio de 45.1, 65.0 y 45.0 W)": (1, (45.1 + 65.0 + 45.0) / 3, 6),
    "Cargadores de celular (promedio de 40, 35, 35, 45 y 20 W)": (1, 35, 12),
    "Módem (aproximación: adaptador 12 V, 0.5 A)": (1, 6, 24),
}
camara = 115 * 4.5 * 14   # Wh/día, aproximación con Fogel VR-12-US; excluida del respaldo
E_CC = 0.0
E_CA = sum(N * P * H for N, P, H in cargas.values())
print("\nCargas críticas:")
for k, (N, P, H) in cargas.items():
    print(f"  {k}: {N} x {P:.1f} W x {H} h = {N*P*H:.0f} Wh/día")
print(f"  E_CA = {E_CA:.0f} Wh/día; cámara de refrigeración (excluida) = {camara:.0f} Wh/día")
for D in (1, 2):
    E_T, Q = capacidad(E_CC, E_CA, D)
    print(f"  D={D}: E_T = {E_T:.0f} Wh/día, Q = {Q:.0f} Ah -> {math.ceil(Q/100)} B4 (máx. 4), {math.ceil(Q/200)} B5")
E_T, Q = capacidad(E_CC, E_CA + camara, 1)
print(f"  Con la cámara y D=1: E_T = {E_T:.0f} Wh/día, Q = {Q:.0f} Ah -> {math.ceil(Q/100)} B4")
D = 1   # días de autonomía definidos el 11 nov. 2026
E_T, Q = capacidad(E_CC, E_CA, D)
Np = math.ceil(Q / 100)
P_CA = sum(N * P for N, P, H in cargas.values()) - 51.7 - 35 + (45.1 + 65.0 + 45.0) + (40 + 35 + 35 + 45 + 20)
I_bat = P_CA * (1 + p["pi"]) / V_SIS
print(f"\nDiseño: D = {D}, Q = {Q:.0f} Ah, {Np} B4 en paralelo = {Np*100} Ah, {Np*2.56:.2f} kWh nominales")
print(f"  P_CA con todas las cargas críticas encendidas = {P_CA:.0f} W, I_bat = {I_bat:.1f} A (límite {Np*100} A)")
print(f"  Costo: {Np} x 400000 CRC = {Np*400000:,} CRC = {Np*400000/CRC_USD:.2f} USD (Kuat); {Np} x 399.99 = {Np*399.99:.2f} USD (EE. UU.)")
