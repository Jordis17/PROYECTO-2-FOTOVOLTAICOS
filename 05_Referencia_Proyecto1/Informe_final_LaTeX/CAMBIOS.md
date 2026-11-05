# Cambios aplicados a ACTUALIZADO (27 oct. 2026)

Las secciones se reconstruyeron a partir de `Informe_Proyecto/informe/secciones` y de la redacción de ACTUALIZADO.pdf. Sin las correcciones, el texto compilado coincide palabra por palabra con ACTUALIZADO.pdf. Si el grupo trabaja en Overleaf, se pueden reemplazar los archivos completos.

| Archivo | Cambio |
|---|---|
| ACTUALIZADO.tex | Pie de página `Pág.\ \thepage`. Antes aparecía "Pág.~24" en las referencias. |
| ACTUALIZADO.tex | Figuras y cuadros con `[!htbp]` en lugar de `[H]`, y paquete `placeins`. Antes quedaban en blanco el 44 % de la pág. 6 y el 61 % de la pág. 17; ahora el informe tiene 25 páginas. |
| ACTUALIZADO.tex | Nueva referencia [9]: manual de instalación del módulo AIKO (rev. 1.9, abr. 2024). Las demás referencias se renumeran solas. |
| 00_resumen.tex | 98 % → 98.4 %. |
| 03_recurso.tex | Redacción de la elección de NASA POWER. |
| 03_recurso.tex | Se quitó el óptimo de 14° de PVGIS (texto, lista de bases de datos y pie de la Fig. 7). En su lugar se indica que con PVGIS × K el máximo también está en 5°. |
| 03_recurso.tex | Justificación de los 10° frente a 5°: el manual del módulo pide evitar que se acumulen agua y polvo y dice que con inclinación suficiente la lluvia limpia la superficie; se pierde solo 0.2 % de energía y la separación de 2.5 m entre filas supera la mínima con los dos ángulos (2.03 m y 1.90 m). |
| figuras/inclinacion_anual.pdf/.png | Fig. 7 sin la estrella del óptimo de PVGIS (14°). Se generó con el mismo código de `Informe_Proyecto/scripts/fig_radiacion.py`, sin esa línea. |
| 04_modulo.tex | Coeficiente de Isc: ahora se imprime "+0.05 %/°C". Antes se perdía el signo. |
| 05_red.tex | 306 → 305 módulos en marzo; 381 módulos (171.5 kWp) → 380 (171.0 kWp). |
| 06_instalacion.tex | Rieles: con patas de 8 in (0.20 m), la separación es de ≈ 1.17 m. Antes decía 0.9 m y 0.16 m, que es menos que la pata más corta. |
| 06_instalacion.tex | `\FloatBarrier` antes de la Sección 6, para que la Fig. 9 quede en la Sección 5. |
| 07_economia.tex | "un 9 % más de generación" → "un 10 %". |

## Revisión por secciones (segunda vuelta)

| Archivo | Cambio |
|---|---|
| ACTUALIZADO.tex y secciones 02–07 | Se quitaron los comentarios `% ====` de encabezado y el comentario del preámbulo. No cambian el PDF. |
| 00_resumen.tex | Se aclara que la recuperación en 9.2 años es pagando de contado (con préstamo son 13.1 años). |
| 03_recurso.tex | La inclinación favorece de setiembre a marzo y reduce de abril a agosto (antes decía noviembre–febrero y mayo–agosto; así lo muestran los factores K). |
| 04_modulo.tex | Se dividió una oración larga en 4.2. |
| 05_red.tex | 5.2: se quitó la afirmación de que el inversor cumple los requisitos de factor de potencia y distorsión de la red, que no se comprobó; ahora solo dice que la tensión y la frecuencia coinciden con las del servicio. |
| 05_red.tex | 5.3: se aclaró el reparto de cadenas por MPPT en los inversores 3 a 5. |
| 06_instalacion.tex | 6.3: el fusible se compara con 1.56 · Isc en STC (22.1 A); antes lo llamaba «corriente de diseño del tramo», que en 6.2 es 22.5 A. |
| 07_economia.tex | 7.4: las tres viñetas con oraciones en negrita se pasaron a un párrafo. |

## Respaldo de los costos de instalación y margen

| Archivo | Cambio |
|---|---|
| 07_economia.tex | 7.1: la instalación (¢100 000/kWp) y el margen (20 %) se comparan con el estudio de costos de NREL para techos comerciales: con sus horas, salarios, gastos generales, contingencia y utilidad aplicados a los mismos equipos se obtienen 0.47 USD/W, frente a 0.48 USD/W con los supuestos usados. |
| ACTUALIZADO.tex | Nueva referencia: Ramasamy et al., NREL/TP-7A40-83586 (Q1 2022). |

## Diagrama unifilar con simbología normalizada (30 oct. 2026)

Corrección pedida en la defensa: el diagrama anterior era de bloques.

| Archivo | Cambio |
|---|---|
| figuras/unifilar.pdf | Diagrama rehecho con símbolos IEC 60617, los mismos de las presentaciones del curso: módulos en serie por cadena, fusible gPV por cadena, seccionador DC multipolar, DPS DC y AC, inversor (DC/AC), interruptor termomagnético, interruptor diferencial, barra, seccionador visible, interruptor de interconexión, medidor bidireccional, transformador del ICE y puestas a tierra. Los tramos T1–T4 llevan su designación de conductores y se agregaron cuadros de simbología, conductores, notas y especificaciones. |
| figuras/unifilar_tikz.tex | Fuente TikZ del diagrama (se compila sola con pdflatex y genera unifilar.pdf). |
| 06_instalacion.tex | 6.4: el texto y el pie de la Fig. 10 indican la simbología IEC 60617 y lo que incluye el diagrama. |

## Revisión de redacción por secciones (30 oct. 2026)

Carpeta: `ACTUALIZADO_revisado_30oct`. La versión anterior queda sin cambios en `ACTUALIZADO_corregido`. No cambian el diseño ni los resultados; solo se corrigen ambigüedades, datos mal descritos y repeticiones.

| Archivo | Cambio |
|---|---|
| 00_resumen.tex | "con la tarifa T-CO"; "la potencia se dimensionó… con medición neta sencilla"; el diseño (no el sistema) incluye estructura, cableado, protecciones y unifilar; se agrega el 66.4 % de reducción de la factura. |
| 01_introduccion.tex | Sin cambios. |
| 02_lugar.tex | 2.1: se indica para qué se usan los extremos de temperatura. 2.4: la variación del consumo se separa de la nota del medidor y se explica su efecto; se agrega el 3 % de alumbrado y bomberos; se explica por qué el cargo por demanda se mantiene en el caso base. |
| 03_recurso.tex | 3.1: se define el ángulo diario (2πd/365.25); se aclara que las líneas de hora de la Fig. 4 están en hora estándar. 3.2: DNI mayor de diciembre a marzo y GHI de enero a abril (antes decía diciembre a abril para ambas); la causa de la diferencia NASA–PVGIS se presenta como posible. |
| 04_modulo.tex | 4.1: degradación garantizada con valores (1 % y 0.35 %/año). 4.2: se quitó una frase repetida en 4.3. 4.3: cálculo del NOCT explicado paso a paso; por qué la temperatura mínima de la celda es la del aire; las corrientes a 64.3 °C se usan para el inversor y los conductores (no para las protecciones). |
| 05_red.tex | 5.1: "celda de NASA POWER" → "zona que representan los datos"; párrafo dividido; 51 % → 51.2 %; aclaración del límite mensual del 49 %; "plantas" → "potencias". 5.3: el intervalo P/1.5–P/1.2 se relaciona con la relación DC/AC. 5.4: se indica entre qué altitudes es la diferencia de 314 m. 5.5: se quitó una frase repetida. |
| 06_instalacion.tex | 6.1: hora solar. 6.2: redacción del tramo 2. 6.3: el TM de 90 A también es menor que la capacidad del conductor de 3 AWG (94 A); la puesta a tierra pasa a un párrafo propio. 6.4: "leyenda de símbolos". |
| 07_economia.tex | 7.1: comparación con NREL sin la lista de parámetros. 7.2: 51.2 %. 7.3: se explica la TDER y la tarifa binómica. 7.4: tasas de comercio (6.6 %) y servicios (11.7 %); el efecto del perfil de carga con cifras (el VPN baja a la mitad). 7.5: "sistemas de menor potencia"; la diferencia con 153 kWp en cifras. |
| 08_conclusiones.tex | Párrafo de los inversores reescrito con los VPN; "tarifa TDER" (antes "tarifa por disponibilidad de la red"); recuperación, TIR y déficit anual del préstamo con valores. |
| 05_red.tex (5.3, segunda pasada) | Se explica qué fija cada límite de módulos en serie y cómo se redondea (17 a 23 módulos); el límite superior del MPPT "permitiría 24"; dos cadenas por MPPT coinciden con sus dos entradas. Las cadenas de 17 se justifican porque cada fila es una cadena: 17 módulos (19.8 m) caben en los 21.5 m del techo con 0.85 m por lado, y con 18 quedarían 0.27 m. Cinco inversores porque 125 kW es el único múltiplo de 25 kW entre 112.2 y 140.3 kW. "Algo sobre 1.5" → relación de 1.53 con 38.25 kWp bajo los 45 kW. |
| 05_red.tex (5.4) | Se quitó la oración del caso con 2 °C más de temperatura (499 V). |
| 06_instalacion.tex (6.1) | Párrafo de la estructura SOLARMOUNT reescrito en dos párrafos, en el orden de armado y sin cambiar los datos. |
| 06_instalacion.tex (6.2 y 6.3) | Tramos en párrafos en lugar de viñetas con negrita; oraciones más cortas, sin cadenas de datos con punto y coma; se define $I$ en la caída de tensión; «del lado de la alimentación» se explica como antes del interruptor principal. Mismos datos y referencias. |
| 06_instalacion.tex | `\FloatBarrier` antes de 6.4 para que la Tabla 13 quede en 6.3. |
| 07_economia.tex (Tabla 16) | Se quitaron las citas dentro de la tabla: el 7 % y el 9 % son supuestos (se justifican con el BCCR en el texto) y la degradación ya está citada en 4.1. |
| 05_red.tex, 07_economia.tex (revisión final) | Se quitaron expresiones vagas: «algo menores», «algo por debajo», «algo mayor… levemente negativo» (ahora ¢1.3 millones por año) y «apenas positivo» (ahora ¢3.7 millones). |
| 08_conclusiones.tex | Último párrafo: la rentabilidad depende de que se mantengan las condiciones actuales de la medición neta sencilla (antes decía «de cómo se reconozca», como si la regla no estuviera definida). |
| 03, 05, 06, 07, 08 (ajustes finales) | 3.2: elección de NASA POWER en una sola oración clara. 5.1: se quitó «cada kWp produce 1304 kWh», que se repetía en 5.5. 7.1: partidas no incluidas en el costo, sin lista con punto y coma. 7.4: «el factor decisivo» y «reducen el margen» reescritos. Seis «por lo que» cambiados para no repetirlos (6.1, 7.1 ×3, 7.4, conclusiones). |
| ACTUALIZADO.pdf | Recompilado: 26 páginas, sin errores ni advertencias. |

