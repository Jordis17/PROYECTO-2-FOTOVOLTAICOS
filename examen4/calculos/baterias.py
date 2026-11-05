"""Examen corto 4: matriz comparativa de baterías y dimensionamiento del banco.

Uso: python3 baterias.py
Cuando se tenga el consumo de la casa, se cambian E_CC y E_CA (Wh/día) y D
(días de autonomía) en la sección "Consumo real".
"""
import math

# ---------------------------------------------------------------------------
# 1. Matriz comparativa (datos consultados el 5 nov. 2026; ver modelos_preliminares.md)
# ---------------------------------------------------------------------------
EUR_USD = 1 / 0.8879  # Infobae, 5 nov. 2026 (1 USD = 0.8879 EUR)

modelos = [
    # id, nombre, V unidad, Ah (C20), unidades para 24 V, precio unitario USD, DOD de la tecnología, ciclos a esa DOD, kg por unidad
    dict(id="B1", nombre="Trojan T-105", V=6, Ah=225, n24=4, precio=225.00, dod=0.50, ciclos=1200, kg=28.0),
    dict(id="B2", nombre="Trojan SAGM 12 205", V=12, Ah=205, n24=2, precio=799.95, dod=0.50, ciclos=1700, kg=59.0),
    dict(id="B3", nombre="Ultracell UCG200-12", V=12, Ah=200, n24=2, precio=358.38 * EUR_USD, dod=0.50, ciclos=1200, kg=62.9),
    dict(id="B4", nombre="Power Queen 24V 100Ah", V=25.6, Ah=100, n24=1, precio=399.99, dod=0.80, ciclos=4000, kg=20.7),
    dict(id="B5", nombre="Victron 25.6V/200Ah Smart-a", V=25.6, Ah=200, n24=1, precio=2983.50, dod=0.80, ciclos=2500, kg=39.0),
]

print("Matriz comparativa (módulo de 24 V)")
print(f"{'':3} {'precio 24V':>10} {'E nom kWh':>9} {'E útil':>7} {'USD/kWh útil':>12} {'@70%':>7} {'USD/kWh vida':>12} {'kg':>6}")
for m in modelos:
    precio24 = m["precio"] * m["n24"]
    e_nom = m["V"] * m["n24"] * m["Ah"] / 1000          # kWh
    e_util = e_nom * m["dod"]
    c_util = precio24 / e_util                            # ecuación (1)
    c_70 = precio24 / (e_nom * 0.70)                      # misma base que el diseño
    c_vida = precio24 / (e_util * m["ciclos"])            # USD por kWh entregado en la vida en ciclos
    m.update(precio24=precio24, e_nom=e_nom, e_util=e_util, c_util=c_util, c_70=c_70, c_vida=c_vida, kg24=m["kg"] * m["n24"])
    print(f"{m['id']:3} {precio24:10.2f} {e_nom:9.2f} {e_util:7.2f} {c_util:12.1f} {c_70:7.1f} {c_vida:12.3f} {m['kg']*m['n24']:6.1f}")

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

print("\nTabla PROVISIONAL (todas las cargas en CA)")
consumos = [1000, 2000, 3000, 4000, 5000, 6000]   # Wh/día de las cargas
for D in (1, 2, 3):
    fila = []
    for E in consumos:
        E_T, Q = capacidad(0, E, D)
        fila.append(f"{E/1000:.0f} kWh: E_T={E_T:6.0f} Q={Q:6.0f} Ah ({math.ceil(Q/100)}xB4)")
    print(f"D={D}:", " | ".join(fila))

# ---------------------------------------------------------------------------
# 3. Consumo real (PENDIENTE: llenar con el levantamiento de cargas)
# ---------------------------------------------------------------------------
E_CC = None   # Wh/día de cargas en CC
E_CA = None   # Wh/día de cargas en CA
D = None      # días de autonomía
if None not in (E_CC, E_CA, D):
    E_T, Q = capacidad(E_CC, E_CA, D)
    print(f"\nConsumo real: E_T = {E_T:.0f} Wh/día, Q = {Q:.0f} Ah a 24 V")
    for m in modelos:
        Ah_24 = m["Ah"]  # capacidad de un módulo de 24 V
        n_par = math.ceil(Q / Ah_24)
        print(f"  {m['id']}: {n_par} en paralelo x {m['n24']} en serie = {n_par*m['n24']} unidades")
