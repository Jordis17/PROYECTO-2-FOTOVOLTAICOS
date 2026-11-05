# Examen corto 4: verificación de datos contra fuentes oficiales

Consulta: 5 nov. 2026. Los archivos de respaldo están en `examen4/fichas/`. Hay PDF oficiales y extractos de texto (`.txt`) de las páginas oficiales y de las tiendas, cada uno con su URL.

Decisiones del grupo (5 nov. 2026):
- B2 pasa de Trojan SAGM 12 205 (ya no aparece en el sitio de Trojan) a **Trojan SAES 12 205** (AES AGM), que es el modelo vigente.
- Los ciclos de B3 se toman de la ficha Ultracell que aloja un distribuidor, aclarando que no es el sitio oficial. Ultracell solo entrega sus fichas PDF por un portal con registro.
- Se habilitan `assets.ctfassets.net` (PDF de Trojan) y `bccr.fi.cr` (tipo de cambio).

## Datos verificados

| Modelo | Dato | Antes | Fuente oficial | Archivo |
|---|---|---|---|---|
| B1 T-105 | Capacidad | 225 Ah C20, 250 Ah C100 | Igual (185 Ah C5, 207 Ah C10) | `Trojan_T105_pagina_oficial.txt` |
| B1 T-105 | Masa | ≈28 kg | 28 kg (62 lb) | idem |
| B1 T-105 | Autodescarga | 5–15 %/mes | Igual | idem |
| B1 T-105 | Temperatura de operación | — | −20 a 45 °C | idem |
| B1 T-105 | Ciclos por DOD, garantía | 1200 al 50 %; garantía 1 o 5 años | **Pendiente**: solo están en el PDF (assets.ctfassets.net) | — |
| B2 SAES 12 205 | Capacidad | (SAGM) 205 Ah C20 | 175 Ah C20; 159 Ah C10; 216 Ah C100 | `Trojan_SAES_12_205_pagina_oficial.txt` |
| B2 SAES 12 205 | Ciclos | (SAGM) 1700 al 50 % | 1200 al 100 % DOD (página oficial). Ciclos al 50 %: **pendiente** del PDF | idem |
| B2 SAES 12 205 | Masa, dimensiones | 59 kg, 380×176×357 mm | Igual | idem |
| B2 SAES 12 205 | Garantía | 2 años (distribuidor) | 3 años | idem |
| B2 SAES 12 205 | Precio | 799.95 USD (SAGM) | **Pendiente**: hace falta una tienda de EE. UU. | — |
| B3 UCG200-12 | Tecnología | Gel | VRLA híbrida: separador AGM con electrolito en gel ("Hybrid VRLA") | `Ultracell_UCG_pagina_oficial.txt` |
| B3 UCG200-12 | Capacidad | 200 Ah (tratada como C20) | **206 Ah a C20**, 200 Ah a C10 | idem |
| B3 UCG200-12 | Masa | 62.9 kg | **62.2 kg** | idem |
| B3 UCG200-12 | Vida de diseño | 10 o 15 años | **10 años** | idem |
| B3 UCG200-12 | Ciclos, garantía | 1200 al 50 %, 2400 al 30 % | No los publica el sitio oficial. Ciclos según la ficha del distribuidor. Garantía no declarada | — |
| B4 Power Queen | Ciclos | >4000, DOD n.d. | **4000 al 100 %, 6000 al 80 %, 15 000 al 60 %** | `PowerQueen_24V100Ah_pagina_oficial.txt` |
| B4 Power Queen | Máx. serie/paralelo | n.d. | **4 en paralelo y 2 en serie (4P2S)**, hasta 8 unidades iguales | idem y manual p. 08 |
| B4 Power Queen | Temperatura de carga | <0 °C no | 0 a 50 °C; descarga −20 a 60 °C; almacenamiento −10 a 50 °C | idem y manual p. 02 |
| B4 Power Queen | Protección de carga a baja temperatura | ? | **No incluida** (la ficha marca "/" en "Low-Temperature Protection" y en la auto-recuperación) | idem |
| B4 Power Queen | Masa | 20.7 kg | 20.68 kg | idem |
| B4 Power Queen | Garantía | 5 años | 5 años | idem |
| B4 Power Queen | Corriente continua | 100 A | 100 A en carga y en descarga | idem |
| B4 Power Queen | Corriente pico | 280 A durante 5 s (distribuidor) | **300 A durante 1 s** | manual p. 01 |
| B4 Power Queen | Autodescarga, eficiencia | — | No declaradas. El manual pide recargar cada 3 meses en almacenamiento, al 50 % de SOC y entre 10 y 35 °C | manual p. 03 |
| B4 Power Queen | Precio | 399.99 USD (Walmart) | Tienda oficial EE. UU.: 413.99 USD. **Kuat CR: ₡400 000, mismo modelo, en stock** | `Kuat_CR_PowerQueen_24V100Ah.txt` |
| B5 Victron | Ciclos | 2500/3000/5000 al 80/70/50 % | Igual (fin de vida con capacidad ≥80 %) | `Victron_LiFePO4_Smart_12.8_25.6V_datasheet.pdf` |
| B5 Victron | Eficiencia | 92 % | 92 % | idem |
| B5 Victron | Autodescarga | — | No declarada. Almacenamiento máximo de 1 año a 25 °C con carga completa | idem |
| B5 Victron | Temperatura de carga | — | **5 a 50 °C**; descarga −20 a 50 °C | idem y manual |
| B5 Victron | BMS externo | "confirmar" | **Sí**. Debe conectarse a un BMS de Victron, que se compra aparte (manual, "Use only with a Victron Energy-approved BMS") | `Victron_Lithium_Smart_manual.pdf` |
| B5 Victron | Garantía | 5 años (distribuidores) | **3 años** para baterías de litio (ampliable a 10 años pagando el 10 % del precio) | `Victron_garantia_pagina_oficial.txt` |
| B5 Victron | Masa | 39 kg | 39 kg | ficha |
| B5 Victron | Máximo de unidades | — | 20 baterías por sistema | ficha y manual |

## Opciones locales encontradas (precios en colones, 5 nov. 2026)
- Kuat CR, Power Queen 24 V 100 Ah: ₡400 000, en stock. Es el modelo B4.
- Kuat CR, Power Queen 24 V 200 Ah: ₡850 000.
- LEDXPRES, "Batería de Gel Solar" 12 V 200 Ah: ₡395 000, en stock. Marca no declarada; vida "500 a 5000 ciclos" sin DOD; garantía de 1 año.
- LEDXPRES, gel tubular EM200PT 12 V 200 Ah C20: ₡405 000, en stock. 1500 ciclos al 80 % de DOD y autodescarga <2 %/mes según la tienda. Marca no declarada.
- Purasol: no publica precios, solo cotización.

## Resultado con los PDF de Trojan y el BCCR (5 nov. 2026)
- T-105: la ficha oficial (`Trojan_T105_datasheet.pdf`, T-105.DS_020819) y la guía de especificaciones 2026 **no declaran ciclos**. Los 1200 ciclos al 50 % se mantienen desde el folleto Signature Line alojado por un distribuidor, con el mismo criterio que B3.
- T-105, garantía: la garantía de Trojan para América Latina (`Trojan_garantia_LATAM_2020.pdf`) es de **12 meses** para toda batería Trojan vendida en la región, y excluye aplicaciones que superan el 50 % de DOD. Antes figuraba como "1 o 5 años".
- SAES 12 205: la ficha oficial (`Trojan_SAES_12_205_datasheet.pdf`) y la guía 2026 dan **179 Ah a C20 y 57 kg**. La página web da 175 Ah y 59 kg; se usa la ficha. Autodescarga <3 %/mes; vida IEC 61427 de 8 años o más. La gráfica de ciclos contra DOD no se puede leer en el PDF, así que se usan los 1200 ciclos al 100 % de la página oficial.
- SAES 12 205, garantía: 3 años con DOD máxima de 80 % (`Trojan_garantia_AES_2023.pdf`). Hay que confirmarla en CR, porque la garantía LATAM es de 12 meses.
- BCCR, 5 nov. 2026: compra ₡449.63 y venta ₡454.41 por dólar. Se usa la venta (`BCCR_tipo_cambio_2026-11-05.txt`). ₡400 000 = 880.26 USD.

## Pendiente
1. Precio de EE. UU. de la SAES 12 205. RES Supply no la vende y solar-electric.com responde con una verificación anti-bots.
