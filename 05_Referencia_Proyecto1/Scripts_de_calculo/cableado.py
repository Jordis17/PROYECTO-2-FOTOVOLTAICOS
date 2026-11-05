"""Dimensionamiento de conductores (5 inversores CPS de 25 kW, 22 cadenas de 17 módulos)."""
import math
# Resistencias DC NEC Cap. 9 Tabla 8 (cobre trenzado sin recubrir, 75 °C) [ohm/km]
R = {"12": 6.34, "10": 3.97, "8": 2.51, "6": 1.61, "4": 1.01, "3": 0.802, "2": 0.634,
     "1/0": 0.399, "2/0": 0.317, "3/0": 0.251, "250": 0.169}
Isc_c, Imp_c, Vmp_c = 14.40, 13.62, 503.0          # cadena de 17 módulos a 64.3 °C
# Tramo 2: cadena - inversor (longitud supuesta de la cadena más lejana)
L_dc = 40
iw = 1.25*1.25*Isc_c
dv = 2*L_dc*Imp_c*R["10"]/1000
print(f"Tramo 2: iw = {iw:.1f} A, 10 AWG corregido = {40*0.8*0.82:.1f} A, dV = {100*dv/Vmp_c:.2f} %")
# Tramo 3: inversor - tablero FV
Iac, L3, V = 69.5, 15, 208
dv3 = math.sqrt(3)*L3*Iac*R["3"]/1000
print(f"Tramo 3: iw = {1.25*Iac:.1f} A, 3 AWG corregido = {100*0.94:.0f} A, dV = {100*dv3/V:.2f} %")
# Tramo 4: tablero FV - tablero principal (5 inversores, 2 conductores de 250 kcmil por fase)
n_inv, L4 = 5, 15
I4 = n_inv*Iac
dv4 = math.sqrt(3)*L4*I4*(R["250"]/2)/1000
print(f"Tramo 4: I = {I4:.1f} A, iw = {1.25*I4:.1f} A, 2x250 kcmil corregido = {2*255*0.94:.0f} A, dV = {100*dv4/V:.2f} %")
print(f"Caída AC total = {100*(dv3+dv4)/V:.2f} %")
print("Fusible de cadena >= 1.56*Isc_STC =", round(1.5625*14.12, 1), "A")
