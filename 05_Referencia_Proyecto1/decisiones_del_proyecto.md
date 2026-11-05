# Decisiones y supuestos vigentes — 11 oct 2026

## Datos del sitio
- NISE 2471778, tarifa T-CO, acometida 120/208 V 3Φ. Coordenadas 9.376950° N, −83.701886°; 704 m s. n. m.
- Consumo 09/2025–08/2026: 223 013 kWh; demanda máxima facturada 53 kW. Cargos 2026: ¢59.67/kWh, ¢9 861.68/kW, alumbrado ¢2.70/kWh, IVA 13 %, bomberos ¢1 827.40.
- Techo plano de lámina, estimado 21.5 × 92.5 m (sin planos; verificar). Eje largo de la nave girado ≈7° respecto al N–S (imagen satelital); módulos con acimut ≈173° (efecto < 0.1 %; cálculos con orientación sur).

## Recurso y módulo
- NASA POWER (diseño) y PVGIS (comparación). Inclinación 10° sur (máximo en 5°, 10° es 0.2 % menor). 1625 kWh/m²·año, 4.45 HSP.
- Temperaturas: NASA POWER horario 2005–2025, 14.1 °C y 30.5 °C (celda NASA a 1018 m). Celda 14.1 / 64.3 °C. γVmp ≈ −0.31 %/°C (aproximación).

## Dimensionamiento
- Criterio del profesor (clase ConectadoRed1): cubrir el consumo anual sin superarlo; neteo simple como modelo base. Decidido por el grupo el 11 oct 2026 (reemplaza la selección por mayor VPN de 76.5 kWp).
- N_mes = E_cons/(HSP·P_mód·PR·días) → 306–428 módulos; 381 módulos para el 100 % anual; con cadenas de 17 se eligen 22 cadenas = 374 módulos (168.3 kWp), 98.4 % del consumo.
- PR mensual 0.801–0.804: temperatura 7.6–8.1 % (T2M mensual NASA POWER, NOCT 47 °C, G = 1000 W/m²), cableado 2 %, mismatch 2 %, suciedad 3 %, MPP 1 %, reflectancia 2 %, recorte 0.14 %, inversor 3.5 %.
- 5 × CPS 25 kW (límite 5 cadenas por inversor); criterio P_AC = P_STC/1.5…/1.2 = 112.2–140.3 kW → 125 kW (DC/AC 1.35).
- Alternativas como complemento (Tabla VIII): 76.5, 107.1, 137.7, 153.0 y 168.3 kWp; 153 kWp tiene VPN algo mayor (¢34.4 M), diferencia pequeña.
- Transformador y circuito del ICE: no limitan el diseño; se mencionan en conclusiones como verificación que corresponde al ICE.

## Instalación
- 22 filas, arreglo 19.8 × 54.2 m (≈54 % del techo); Unirac SolarMount + patas + S-5!.
- Cables: 10 AWG PV; tramo 2 de 40 m (0.86 %); tramo 3 en 3 AWG THHN (0.70 %); tramo 4 en 2×(3×250 kcmil THHN) + 2×2 AWG T, I = 347.5 A (0.37 %); ΔV AC total 1.06 %.
- Protecciones: fusible gPV 25 A; TM 90 A y diferencial 100 A/300 mA por inversor; DPS AC; seccionador 600 A (HU366); interconexión 450 A (MAL36450) en tablero principal (regla del 120 %).

## Economía
- La hoja 2026Oct9_EscenariosAFSFV.xlsx es solo guía de la estructura del análisis; no se usan sus datos.
- Medición neta sencilla (43879-MINAE): depósito reconocido = mín(depositado, 49 % de la generación) por mes, devolución dentro del año. Caso base sin tarifa de acceso (solo monómicas, RE-0076-JD-2023) y con TDER ¢255/kWp·mes + IVA sobre 168.3 kWp. Demanda sin reducción en el caso base.
- Costos: igual criterio (CFIA 4.5 % + 0.25 %, ICE ¢382 871, instalación ¢100 000/kWp y ganancia 20 % como supuestos). Precio USD 260 717 = ¢119.05 M; valor de la obra ¢94.34 M.
- Flujo 25 años; tasa 7 %; préstamo 80 % a 9 % en 120 meses (cuota ¢1 206 419); degradación 1 % + 0.35 %/año; O&M 1 %.
- Resultados: contado 0 % VPN ¢29.5 M, TIR 9.7 %, IR 1.25, PRI 9.2; contado 3 % VPN ¢75.6 M; préstamo 0 % VPN ¢23.0 M, TIR 10.7 %, PRI 13.1. Sensibilidad: tarifa de acceso VPN ¢3.7 M; venta de excedentes −¢18.6 M; sin reconocimiento −¢44.6 M; carga 50 % ¢14.6 M; tasa 9 % ¢6.5 M; precio +15 % ¢9.5 M.
- Sección «Herramientas de apoyo» (uso de IA) antes de las referencias, con la redacción del grupo.
