"""Hoja de cálculo económica (T-CO) del sistema de 168.3 kWp con medición neta sencilla, con fórmulas."""
import json, numpy as np
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter as L

J = json.load(open("/home/claude/fv/datos/economia_final.json"))
B = J["B"]
mes = ["Ene","Feb","Mar","Abr","May","Jun","Jul","Ago","Set","Oct","Nov","Dic"]
C = [18482,17626,18238,18850,19339,18482,18972,19094,18238,18727,17993,18972]
D = [43.70,49.33,45.78,46.14,46.88,45.78,44.19,47.25,53.00,47.12,44.92,44.31]

wb = Workbook()
F = "Arial"
blue = Font(name=F, color="0000FF"); black = Font(name=F); bold = Font(name=F, bold=True)
green = Font(name=F, color="008000"); hdr = Font(name=F, bold=True, color="FFFFFF")
hfill = PatternFill("solid", fgColor="1F3F66"); yel = PatternFill("solid", fgColor="FFFF00")
thin = Side(style="thin", color="BBBBBB")
def header(ws, row, vals):
    for j, v in enumerate(vals, 1):
        c = ws.cell(row, j, v); c.font = hdr; c.fill = hfill; c.alignment = Alignment(horizontal="center", wrap_text=True, vertical="center")

# ---------- Supuestos ----------
S = wb.active; S.title = "Supuestos"
rows = [
 ("Potencia instalada [kWp]", 168.3, "Diseño (374 módulos de 450 W, 22 cadenas de 17); se usa para la TDER"),
 ("Precio del sistema [¢]", round(J["I0"]), f"Tabla de costos del informe (USD {J['CO']['precio']:,} × 456.61)"),
 ("Cargo por energía [¢/kWh]", 59.67, "Tarifa T-CO 2026, facturas ICE"),
 ("Cargo por demanda [¢/kW]", 9861.68, "Tarifa T-CO 2026, facturas ICE"),
 ("Alumbrado público [¢/kWh]", 2.70, "Facturas ICE"),
 ("IVA sobre energía, demanda y TDER", 0.13, "Facturas ICE"),
 ("Tributo de bomberos [¢/mes]", 1827.40, "Facturas ICE"),
 ("Energía depositada reconocida [fracción de la generación]", 0.49, "Medición neta sencilla, Reglamento 43879-MINAE"),
 ("Tarifa TDER [¢/kW-mes]", 255, "ICE: ¢255 por kW instalado al mes; se aplica a los kWp del arreglo (conservador)"),
 ("Reducción de demanda facturada", 0.0, "Caso base 0 %; sensibilidad 10 % y 20 %"),
 ("Aumento anual de tarifas y gastos", 0.0, "Caso base 0 %; escenario 3 %"),
 ("Tasa de descuento", 0.07, "Supuesto: mayor que la TBP (3.59 %, set. 2026) y similar a la TAN de comercio (6.63 %), BCCR"),
 ("Degradación año 1", 0.01, "Garantía del módulo; se aplica solo al ahorro por energía"),
 ("Degradación anual posterior", 0.0035, "Garantía del módulo"),
 ("Mantenimiento y reposición [fracción del precio/año]", 0.01, "Supuesto"),
 ("Fracción financiada", 0.8, "Supuesto; arrendadoras financian 80–100 % (Avolta Energy, 2026)"),
 ("Interés anual del préstamo", 0.09, "Dentro de la TAN en colones del BCCR: comercio 6.63 %, servicios 11.69 % (may.–jun. 2026)"),
 ("Plazo del préstamo [meses]", 120, "Supuesto; Banco Popular financia paneles hasta 144 meses"),
]
header(S, 1, ["Parámetro", "Valor", "Fuente / nota"])
for i, (a, v, n) in enumerate(rows, 2):
    S.cell(i, 1, a).font = black; c = S.cell(i, 2, v); c.font = blue; S.cell(i, 3, n).font = black
    if isinstance(v, float) and v < 1 and "kWh" not in a: c.number_format = "0.0%"
    elif v >= 1000: c.number_format = "#,##0"
for r in (11, 12): S.cell(r, 2).fill = yel
S["A22"] = "Celdas en azul: datos de entrada. Celdas amarillas: palancas de escenario."
S["A23"] = "Este libro corresponde al sistema seleccionado de 168.3 kWp (374 módulos, 22 cadenas de 17). La generación y el autoconsumo mensuales son datos de entrada (balance horario) y no se recalculan al cambiar B2."
S["A23"].font = Font(name=F, italic=True); S["A22"].font = Font(name=F, italic=True)
S.column_dimensions["A"].width = 46; S.column_dimensions["B"].width = 16; S.column_dimensions["C"].width = 46
N = {a: f"Supuestos!$B${i}" for i, (a, _, _) in enumerate(rows, 2)}
kwp, I0, pe, pdm, pa, iva, bomb, lim, tder, red, esc, tasa, d1, d2, om, ffin, rint, nper = [N[r[0]] for r in rows]

# ---------- Balance y factura (medición neta sencilla) ----------
M = wb.create_sheet("Balance mensual")
cols = ["Mes", "Consumo [kWh]", "Demanda [kW]", "Generación [kWh]", "Autoconsumo [kWh]", "Depositada [kWh]",
        "Depositada reconocida [kWh]", "No reconocida [kWh]", "Necesidad de la red [kWh]", "Devuelta [kWh]", "Saldo acumulado [kWh]",
        "Comprada [kWh]", "Factura sin FV [¢]", "Factura con FV [¢]", "Ahorro [¢]"]
header(M, 1, cols)
for i in range(12):
    r = i + 2
    M.cell(r, 1, mes[i]).font = black
    M.cell(r, 2, C[i]).font = blue; M.cell(r, 3, D[i]).font = blue
    M.cell(r, 4, round(B["gen"][i])).font = blue; M.cell(r, 5, round(B["slf"][i])).font = blue
    M.cell(r, 6, f"=D{r}-E{r}"); M.cell(r, 7, f"=MIN(F{r},{lim}*D{r})"); M.cell(r, 8, f"=F{r}-G{r}")
    M.cell(r, 9, f"=B{r}-E{r}")
    prev = "0" if r == 2 else f"K{r-1}"
    M.cell(r, 10, f"=MIN({prev}+G{r},I{r})"); M.cell(r, 11, f"={prev}+G{r}-J{r}"); M.cell(r, 12, f"=I{r}-J{r}")
    M.cell(r, 13, f"=B{r}*{pe}+C{r}*{pdm}+B{r}*{pa}+{iva}*(B{r}*{pe}+C{r}*{pdm})+{bomb}")
    M.cell(r, 14, f"=L{r}*{pe}+C{r}*(1-{red})*{pdm}+L{r}*{pa}+{iva}*(L{r}*{pe}+C{r}*(1-{red})*{pdm}+{tder}*{kwp})+{tder}*{kwp}+{bomb}")
    M.cell(r, 15, f"=M{r}-N{r}")
M.cell(14, 1, "Total").font = bold
for j in range(2, 16):
    col = L(j)
    if j == 11: M.cell(14, j, "=K13").font = bold
    else: M.cell(14, j, f"=SUM({col}2:{col}13)" if j != 3 else "=AVERAGE(C2:C13)").font = bold
for r in range(2, 15):
    for j in range(2, 16): M.cell(r, j).number_format = "#,##0" if j != 3 else "0.00"
M["A16"] = "Generación (HSP·P·PR mensual) y autoconsumo (balance horario NASA POWER 2015-2024, carga supuesta 75 % de la demanda en horario de atención): valores de entrada para 168.3 kWp. La energía depositada se reconoce hasta el 49 % de la generación de cada mes y se devuelve en el mismo mes o en los siguientes del año."
M["A18"] = "Ahorro anual que depende de la generación [¢]"; M["O18"] = f"=(E14+J14)*({pe}*(1+{iva})+{pa})"
M["A19"] = "Ahorro anual fijo (TDER y demanda) [¢]"; M["O19"] = "=O14-O18"
for rr in (18, 19): M[f"O{rr}"].number_format = "#,##0;(#,##0)"; M[f"A{rr}"].font = bold
M["A16"].font = Font(name=F, italic=True)
for j, w in enumerate([8, 12, 11, 13, 13, 13, 14, 13, 13, 12, 12, 12, 15, 15, 13], 1): M.column_dimensions[L(j)].width = w
M.row_dimensions[1].height = 45

# ---------- Resultados del balance horario ----------
Hh = wb.create_sheet("Balance horario")
cfg = json.load(open("/home/claude/fv/datos/balance_horario_final.json"))
header(Hh, 1, ["Mes", "Gen. horaria [kWh]", "Autoc. k=0.65 [kWh]", "Autoc. k=0.75 [kWh]", "Autoc. k=0.85 [kWh]"])
for i in range(12):
    Hh.cell(i+2, 1, mes[i])
    for j, key in enumerate(["N22_0.75", "N22_0.65", "N22_0.75", "N22_0.85"], 2):
        Hh.cell(i+2, j, cfg[key]["gen"][i] if j == 2 else cfg[key]["self"][i]).font = blue
Hh.cell(14, 1, "Total").font = bold
for j in range(2, 6): Hh.cell(14, j, f"=SUM({L(j)}2:{L(j)}13)").font = bold
Hh["A16"] = "Balance horario con NASA POWER 2015-2024 (hora estándar local) y pérdida térmica mensual. k: carga en horario de atención como fracción de la demanda facturada del mes."
Hh["A17"] = "La generación horaria incluye el recorte de cada inversor (303 kWh/año); la del informe usa HSP·P·PR con 0.3 % de recorte. Los totales mensuales difieren en menos de 1 %."
Hh["A18"] = "Para reproducir estos valores: python scripts/simulacion_horaria.py (descarga NASA POWER 2015-2024 y repite el cálculo)."
for j, w in enumerate([8, 18, 18, 18, 18], 1): Hh.column_dimensions[L(j)].width = w
Hh.row_dimensions[1].height = 32

# ---------- Flujo de caja ----------
Fl = wb.create_sheet("Flujo de caja")
header(Fl, 1, ["Año", "Factor de degradación", "Ahorro [¢]", "Mantenimiento [¢]", "Flujo de contado [¢]",
               "Cuota del préstamo [¢]", "Flujo con préstamo [¢]", "Acumulado contado [¢]", "Acumulado con préstamo [¢]"])
Fl["K1"] = "Cuota mensual [¢]"; Fl["K1"].font = bold
Fl["L1"] = f"=PMT({rint}/12,{nper},-{ffin}*{I0})"; Fl["L1"].number_format = "#,##0"
for k in range(0, 26):
    r = k + 2
    Fl.cell(r, 1, k)
    if k == 0:
        Fl.cell(r, 2, None); Fl.cell(r, 3, 0); Fl.cell(r, 4, 0)
        Fl.cell(r, 5, f"=-{I0}"); Fl.cell(r, 6, 0); Fl.cell(r, 7, f"=-(1-{ffin})*{I0}")
        Fl.cell(r, 8, f"=E{r}"); Fl.cell(r, 9, f"=G{r}")
    else:
        Fl.cell(r, 2, f"=1-{d1}" if k == 1 else f"=B{r-1}*(1-{d2})")
        Fl.cell(r, 3, f"=('Balance mensual'!$O$18*B{r}+'Balance mensual'!$O$19)*(1+{esc})^(A{r}-1)")
        Fl.cell(r, 4, f"={om}*{I0}*(1+{esc})^(A{r}-1)")
        Fl.cell(r, 5, f"=C{r}-D{r}")
        Fl.cell(r, 6, f"=IF(A{r}*12<={nper},12*$L$1,0)")
        Fl.cell(r, 7, f"=E{r}-F{r}")
        Fl.cell(r, 8, f"=H{r-1}+E{r}"); Fl.cell(r, 9, f"=I{r-1}+G{r}")
    for j in range(3, 10): Fl.cell(r, j).number_format = "#,##0;(#,##0);-"
    Fl.cell(r, 2).number_format = "0.0000"
for j, w in enumerate([6, 12, 15, 15, 16, 15, 16, 17, 18], 1): Fl.column_dimensions[L(j)].width = w
Fl.column_dimensions["K"].width = 18; Fl.column_dimensions["L"].width = 14
Fl.row_dimensions[1].height = 32

# ---------- Indicadores ----------
I = wb.create_sheet("Indicadores")
header(I, 1, ["Indicador", "Contado (proyecto)", "Con préstamo (aporte propio)"])
I["A2"] = "VPN [¢]"; I["B2"] = f"='Flujo de caja'!E2+NPV({tasa},'Flujo de caja'!E3:E27)"; I["C2"] = f"='Flujo de caja'!G2+NPV({tasa},'Flujo de caja'!G3:G27)"
I["A3"] = "TIR"; I["B3"] = "=IRR('Flujo de caja'!E2:E27)"; I["C3"] = "=IRR('Flujo de caja'!G2:G27)"
I["A4"] = "Recuperación simple [años]"
I["A7"] = "Índice de rentabilidad, IR"; I["B7"] = "=1+B2/-'Flujo de caja'!E2"; I["C7"] = "=1+C2/-'Flujo de caja'!G2"
I["B7"].number_format = I["C7"].number_format = "0.00"
for col, src in (("B", "H"), ("C", "I")):
    rng = f"'Flujo de caja'!{src}2:{src}27"
    k = f"MATCH(TRUE,INDEX({rng}>=0,0),0)"
    I[f"{col}4"] = (f"=INDEX('Flujo de caja'!A2:A27,{k}-1)+(-INDEX({rng},{k}-1))/(INDEX({rng},{k})-INDEX({rng},{k}-1))")
I["A5"] = "Ahorro anual nominal, sin degradación [¢]"; I["B5"] = "='Balance mensual'!O14"; I["C5"] = "='Balance mensual'!O14"
I["A6"] = "Ahorro anual nominal [% de la factura]"; I["B6"] = "='Balance mensual'!O14/'Balance mensual'!M14"; I["C6"] = "=B6"
for r in (2, 5): I[f"B{r}"].number_format = I[f"C{r}"].number_format = "#,##0"
for r in (3, 6): I[f"B{r}"].number_format = I[f"C{r}"].number_format = "0.0%"
I["B4"].number_format = I["C4"].number_format = "0.0"
I["A9"] = "Cambie las celdas amarillas de 'Supuestos' (reducción de demanda, aumento de tarifas) para ver los escenarios."
I["A9"].font = Font(name=F, italic=True)
I.column_dimensions["A"].width = 36; I.column_dimensions["B"].width = 20; I.column_dimensions["C"].width = 28
for ws in wb:
    for row in ws.iter_rows():
        for c in row:
            if c.font.name != F: c.font = Font(name=F, bold=c.font.bold, color=c.font.color, italic=c.font.italic)
out = "/home/claude/fv/economia/evaluacion_economica_168kWp.xlsx"
import os; os.makedirs(os.path.dirname(out), exist_ok=True)
wb.save(out); print(out)
