# Examen corto 4: lista de modelos (aprobada por el grupo)

> **Actualización 5 nov. 2026:** los datos se verificaron contra las fuentes oficiales. Ver `verificacion_fichas.md`. B2 cambió a Trojan SAES 12 205 (la SAGM 12 205 está descontinuada). Esta tabla queda como registro de la búsqueda inicial.

Precios usados en la matriz (`calculos/baterias.py`): B1 225.00 USD (RES Supply), B2 799.95 USD (Air One Solar), B3 358.38 EUR = 403.63 USD (1 USD = 0.8879 EUR, Infobae, 5 nov. 2026), B4 399.99 USD (Walmart), B5 2983.50 USD (solar-electric.com).

Consulta: 5 nov. 2026. Los datos técnicos vienen de los buscadores (fichas o tiendas que reproducen la ficha). **No se pudieron descargar las fichas oficiales** porque la red de esta sesión bloquea los sitios de los fabricantes y de las tiendas de Costa Rica. Antes de pasarlos al informe hay que revisar cada dato contra el PDF oficial.

| # | Modelo | Tecnología | Unidad | Para 24 V | Datos técnicos encontrados | Precio encontrado (fuente, moneda) |
|---|---|---|---|---|---|---|
| B1 | Trojan T-105 | Plomo-ácido inundado (placa gruesa, ciclo profundo) | 6 V, 225 Ah C20 (250 Ah C100) | 4 en serie | 1200 ciclos al 50 % DOD (tabla Trojan Signature Line), ~28 kg | Sin precio en CR. Referencia: Mercado Libre Colombia, COP 1 550 000. **Falta un precio de EE. UU. o CR** |
| B2 | Trojan SAGM 12 205 | Plomo-ácido VRLA AGM | 12 V, 205 Ah C20 (174 Ah C100) | 2 en serie | 1700 ciclos al 50 % DOD, 59 kg, 380×176×357 mm, garantía 2 años (según tienda) | Sin precio en CR. baterias.com (España): 1185.39 EUR, agotado. **Falta un precio vigente** |
| B3 | Ultracell UCG200-12 | Plomo-ácido VRLA gel | 12 V, 200 Ah | 2 en serie | ~1200 ciclos al 50 % DOD, ~2400 al 30 %; vida de diseño 10 o 15 años según el documento (hay que confirmarla) | wattuneed (UE): 358.38 EUR con IVA; otra tienda UE: 417.45 EUR |
| B4 | Power Queen 24 V 100 Ah | LiFePO₄ | 25.6 V, 100 Ah, 2.56 kWh, BMS de 100 A | 1 | >4000 ciclos (la DOD no aparece en lo encontrado), peso y garantía sin confirmar | Walmart EE. UU.: 399.99 USD. Kuat CR (distribuidor oficial Power Queen): "litio 24 V desde ₡400 000" (página de hace ~1 año, sin modelo exacto) |
| B5 | Victron LiFePO4 25.6V/200Ah Smart-a (BAT524120610) | LiFePO₄ | 25.6 V, 200 Ah, 5.12 kWh | 1 | 2500 ciclos al 80 % DOD, 3000 al 70 %, 5000 al 50 %; 39 kg (según tienda) | solar-electric.com (EE. UU.): 2983.50 USD |

Cobertura: plomo-ácido (inundado, AGM y gel) e ion-litio LiFePO₄. Son 5 modelos de 2 tecnologías del curso, más de lo que pide el examen (4 modelos y 2 tecnologías).

## Opción local descartada por ahora
- LEDXPRES (CR), "Batería Gel Tubular de Ciclo Profundo", SKU LXBATGELTUB, ₡405 000, agotada. No se encontró su capacidad ni su marca, así que no se puede comparar. Si el grupo consigue la ficha, podría reemplazar a B3 como opción local.
- Purasol (CR) vende LiFePO₄ de 12.8 V y 24 V, pero los buscadores no muestran precios.

## Qué hace falta para cerrar la lista
1. Fichas oficiales (PDF) de B1 a B5: trojanbattery.com, ultracell.co.uk, ipowerqueen.com, victronenergy.com.
2. Precios en Costa Rica: kuatcr.com, purasol.cr, ledxpres.com o una cotización por correo o WhatsApp. En otro caso, precios de EE. UU. de la misma tienda para todos.
3. Tipo de cambio del día (BCCR) para pasar todo a USD.

Para que la sesión pueda abrir esos sitios, hay que agregarlos en *Allowed domains* de la configuración de red del entorno. Otra opción es que el grupo descargue los PDF y los suba al repositorio.
