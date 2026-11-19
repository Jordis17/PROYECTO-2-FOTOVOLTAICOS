"""Facturas mensuales estimadas de 2026 (casa de Abner López, JASEC, tarifa T-RE).

Dato real: la factura de octubre de 2026 es de 19 175 colones, que con la tarifa
de JASEC equivale a 275 kWh. El grupo indica que las facturas han estado entre
16 000 y 22 000 colones. Los otros 11 meses siguen el patrón mes a mes del
ejemplo de JASEC de la hoja de escenarios del curso (fila "EC Energía consumida
por el cliente", Mes 1 = enero, supuesto):
- meses con consumo del ejemplo mayor o igual al de octubre: misma proporción
  que en el ejemplo (275 kWh x consumo del mes / consumo de octubre);
- meses por debajo de octubre: la diferencia con octubre se reduce en la misma
  proporción para que el mes más bajo dé 235.3 kWh, es decir, unos 16 000 colones.

Uso: python3 generar_facturas_estimadas.py  ->  facturas_estimadas_2026.xlsx
(después recalcular el archivo para que las fórmulas tengan valores guardados).
"""
from pathlib import Path
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side

OUT = Path(__file__).with_name("facturas_estimadas_2026.xlsx")
F = "Arial"
f_b = Font(name=F, size=10, bold=True)
f_t = Font(name=F, size=13, bold=True)
f_n = Font(name=F, size=10)
f_in = Font(name=F, size=10, color="0000FF")
fill_in = PatternFill("solid", fgColor="FFFF99")
fill_hd = PatternFill("solid", fgColor="D9E1F2")
fill_real = PatternFill("solid", fgColor="E2EFDA")
thin = Side(style="thin", color="BFBFBF")
box = Border(left=thin, right=thin, top=thin, bottom=thin)
wrap = Alignment(wrap_text=True, vertical="top")
center = Alignment(horizontal="center", vertical="center", wrap_text=True)

wb = Workbook()

# ------------------------------------------------------------------ Tarifa
wt = wb.active
wt.title = "Tarifa"
wt.column_dimensions["A"].width = 46
wt.column_dimensions["B"].width = 14
wt.column_dimensions["C"].width = 12
wt.column_dimensions["D"].width = 80
wt["A1"] = "Tarifa residencial JASEC (T-RE) y cargos de la factura, 2026"; wt["A1"].font = f_t
hdr = ["Concepto", "Valor", "Unidad", "Fuente"]
for j, h in enumerate(hdr, 1):
    c = wt.cell(3, j, h); c.font = f_b; c.fill = fill_hd; c.border = box
SRC_T = ("ARESEP, datos abiertos, tarifas de distribución, JASEC T-RE, ene.-dic. 2026; "
         "RE-0072-IE-2025 (ET-94-2025), La Gaceta 236, Alcance 161, 16 dic. 2025. Consultado 19 nov. 2026.")
SRC_AP = ("ARESEP, datos abiertos, tarifas de alumbrado público, JASEC T-AP, 2026; "
          "RE-0072-IE-2025. Consultado 19 nov. 2026.")
rows = [
    ("Cargo fijo primeros 30 kWh", 1863.30, "₡/mes", SRC_T),
    ("Energía de 31 a 200 kWh", 62.11, "₡/kWh", SRC_T),
    ("Energía de más de 200 kWh", 76.02, "₡/kWh", SRC_T),
    ("Alumbrado público, primeros 30 kWh", 80.10, "₡/mes", SRC_AP),
    ("Alumbrado público, de 31 a 50 000 kWh", 2.67, "₡/kWh", SRC_AP),
    ("Tributo de bomberos (sobre el cargo de energía)", 0.0175, "", "Ley 8992: 1.75 % de la facturación por consumo eléctrico; no aplica con consumo de 100 kWh o menos."),
    ("Consumo mínimo para cobrar bomberos", 100, "kWh", "Ley 8992 (exentos los abonados con 100 kWh o menos)."),
    ("IVA (sobre el cargo de energía)", 0.13, "", "Ley 9635: el consumo residencial de 280 kWh o menos está exento; si se supera, se cobra sobre todo el consumo."),
    ("Límite de consumo exento de IVA", 280, "kWh", "Ley 9635."),
]
names = ["fijo", "b1", "b2", "ap0", "ap1", "bomb", "bmin", "iva", "ivamin"]
ref = {}
for i, (lbl, v, u, s) in enumerate(rows):
    r = 4 + i
    wt.cell(r, 1, lbl).font = f_n
    c = wt.cell(r, 2, v); c.font = f_in; c.fill = fill_in
    c.number_format = "0.00%" if u == "" else ("#,##0.00" if v < 1000 else "#,##0.00")
    if names[i] in ("bmin", "ivamin"): c.number_format = "0"
    wt.cell(r, 3, u).font = f_n
    d = wt.cell(r, 4, s); d.font = f_n; d.alignment = wrap
    for j in range(1, 5): wt.cell(r, j).border = box
    ref[names[i]] = f"Tarifa!$B${r}"
wt.cell(15, 1, "Comprobación: la factura de octubre (₡19 175) se reproduce con 275 kWh.").font = f_n
wt.cell(16, 1, "Criterio de IVA igual al del Proyecto 1: se aplica al cargo de energía, no al alumbrado ni al tributo de bomberos.").font = f_n

# ------------------------------------------------------------------ Facturas
wf = wb.create_sheet("Facturas")
wf["A1"] = "Facturas mensuales de 2026: octubre real, demás meses estimados"; wf["A1"].font = f_t
wf["A2"] = ("Patrón: ejemplo de JASEC de la hoja de escenarios del curso (Mes 1 = enero, supuesto). Meses por encima de octubre: "
            "misma proporción que el ejemplo. Meses por debajo: diferencia con octubre reducida para que el mínimo dé unos ₡16 000.")
wf["A2"].font = f_n
wf["A3"] = "Factura real de octubre:"; wf["A3"].font = f_b
wf["C3"] = 19175; wf["C3"].font = f_in; wf["C3"].fill = fill_in; wf["C3"].number_format = "#,##0"
wf["D3"] = "₡ (dato del grupo)"; wf["D3"].font = f_n
wf["E3"] = "kWh de octubre:"; wf["E3"].font = f_b
wf["F3"] = 275; wf["F3"].font = f_in; wf["F3"].fill = fill_in
wf["G3"] = "obtenido de la tarifa (ver comprobación en la columna K)"; wf["G3"].font = f_n
wf["A4"] = "Consumo del mes más bajo:"; wf["A4"].font = f_b
wf["C4"] = 235.3; wf["C4"].font = f_in; wf["C4"].fill = fill_in
wf["D4"] = "kWh (≈ ₡16 000, mínimo indicado por el grupo)"; wf["D4"].font = f_n

H = ["Mes", "Origen", "Consumo del ejemplo del curso [kWh]", "Factor respecto a octubre",
     "Consumo [kWh]", "Energía [₡]", "Alumbrado público [₡]", "Bomberos [₡]", "IVA [₡]", "Total [₡]", "Comprobación"]
W = [8, 11, 14, 11, 11, 12, 12, 11, 11, 12, 30]
for j, (h, w) in enumerate(zip(H, W), 1):
    c = wf.cell(5, j, h); c.font = f_b; c.fill = fill_hd; c.alignment = center; c.border = box
    wf.column_dimensions[chr(64 + j)].width = w
wf.row_dimensions[5].height = 42
EC = [350, 415.3, 490.5, 421.3, 482.3, 495.1, 365.2, 498.7, 492.1, 480, 458.2, 326.1]
MES = ["ene", "feb", "mar", "abr", "may", "jun", "jul", "ago", "set", "oct", "nov", "dic"]
R0 = 6
OCT = R0 + 9
for i in range(12):
    r = R0 + i
    real = MES[i] == "oct"
    wf.cell(r, 1, MES[i])
    wf.cell(r, 2, "Real" if real else "Estimado")
    c = wf.cell(r, 3, EC[i]); c.font = f_in; c.fill = fill_in; c.number_format = "0.0"
    wf.cell(r, 4, f"=C{r}/$C${OCT}").number_format = "0.000"
    wf.cell(r, 5, f"=ROUND(IF(C{r}>=$C${OCT},$F$3*D{r},$F$3-($F$3-$C$4)*($C${OCT}-C{r})/($C${OCT}-MIN($C${R0}:$C${R0+11}))),1)").number_format = "0.0"
    e = f"E{r}"
    wf.cell(r, 6, f"={ref['fijo']}+{ref['b1']}*MAX(0,MIN({e},200)-30)+{ref['b2']}*MAX(0,{e}-200)").number_format = "#,##0"
    wf.cell(r, 7, f"={ref['ap0']}+{ref['ap1']}*MAX(0,{e}-30)").number_format = "#,##0"
    wf.cell(r, 8, f"=IF({e}>{ref['bmin']},{ref['bomb']}*F{r},0)").number_format = "#,##0"
    wf.cell(r, 9, f"=IF({e}>{ref['ivamin']},{ref['iva']}*F{r},0)").number_format = "#,##0;-#,##0;\"-\""
    wf.cell(r, 10, f"=F{r}+G{r}+H{r}+I{r}").number_format = "#,##0"
    if real:
        wf.cell(r, 11, f'=IF(ABS(J{r}-$C$3)<1,"Coincide con la factura","Revisar")')
    for j in range(1, 12):
        c = wf.cell(r, j); c.border = box
        if j != 3: c.font = f_n
        if real and j != 3: c.fill = fill_real
RT = R0 + 12
wf.cell(RT, 1, "Total").font = f_b
for col in "EFGHIJ":
    c = wf[f"{col}{RT}"]; c.value = f"=SUM({col}{R0}:{col}{RT-1})"; c.font = f_b
    c.number_format = "0.0" if col == "E" else "#,##0"
wf.cell(RT + 1, 1, "Promedio").font = f_b
for col in "EJ":
    c = wf[f"{col}{RT+1}"]; c.value = f"=AVERAGE({col}{R0}:{col}{RT-1})"; c.font = f_b
    c.number_format = "0.0" if col == "E" else "#,##0"
wf.cell(RT + 3, 1, "Meses con IVA (consumo mayor a 280 kWh):").font = f_n
wf.cell(RT + 3, 5, f'=COUNTIF(E{R0}:E{RT-1},">"&{ref["ivamin"]})').font = f_b
wf.cell(RT + 3, 7, "Factura mínima y máxima:").font = f_n
wf.cell(RT + 3, 9, f"=MIN(J{R0}:J{RT-1})").number_format = "#,##0"
wf.cell(RT + 3, 10, f"=MAX(J{R0}:J{RT-1})").number_format = "#,##0"
wf.cell(RT + 4, 1, "Leyenda: amarillo con texto azul = dato de entrada; verde = mes con factura real.").font = f_n
wf.freeze_panes = "A6"

wb.save(OUT)
print("ok", OUT)
