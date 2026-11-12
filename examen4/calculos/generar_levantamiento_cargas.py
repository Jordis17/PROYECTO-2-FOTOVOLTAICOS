import sys
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.utils import get_column_letter as L
from openpyxl.comments import Comment

out = sys.argv[1]
F = "Arial"
f_base = Font(name=F, size=10)
f_b = Font(name=F, size=10, bold=True)
f_t = Font(name=F, size=13, bold=True)
f_in = Font(name=F, size=10, color="0000FF")
f_ex = Font(name=F, size=10, italic=True, color="808080")
f_link = Font(name=F, size=10, color="008000")
fill_in = PatternFill("solid", fgColor="FFFF99")
fill_hd = PatternFill("solid", fgColor="D9E1F2")
fill_tot = PatternFill("solid", fgColor="EDEDED")
thin = Side(style="thin", color="BFBFBF")
box = Border(left=thin, right=thin, top=thin, bottom=thin)
wrap = Alignment(wrap_text=True, vertical="top")
center = Alignment(horizontal="center", vertical="center", wrap_text=True)

R0, R1 = 6, 45          # filas de datos (40 equipos)
REX = 5                 # fila de ejemplo (no se suma)
RNG = lambda c: f"{c}${R0}:{c}${R1}"

wb = Workbook()

# ---------------------------------------------------------------- Instrucciones
ws = wb.active
ws.title = "Instrucciones"
ws.column_dimensions["A"].width = 110
lines = [
    ("Levantamiento de cargas: casa de Abner López (Santa Rosa, Oreamuno, Cartago)", f_t),
    ("Proyecto 2, sistema FV aislado, EL-5854. Hoja para llenar en la visita a la casa.", f_base),
    ("", f_base),
    ("Cómo usarla", f_b),
    ("1. En la hoja «Cargas», llenar una fila por tipo de equipo. Solo se editan las celdas amarillas con texto azul; las demás se calculan solas.", f_base),
    ("2. Tomar los datos de la placa o etiqueta del equipo y fotografiarla. Anotar en «Fuente del dato» de dónde salió cada valor (placa, manual o ficha, medición o supuesto).", f_base),
    ("3. Si un dato no aparece en la placa, dejar la celda vacía o marcar la fuente como «Supuesto» y explicarlo en «Observaciones». No estimar sin indicarlo.", f_base),
    ("4. En «¿Carga crítica?» poner «Sí» solo para las cargas que el sistema debe respaldar. Las de «No» quedan registradas pero no se suman.", f_base),
    ("5. En «Perfil horario», para cada equipo, anotar qué fracción de cada hora está encendido (1 = toda la hora, 0.5 = media hora, vacío = apagado). La suma debe coincidir con las horas/día de «Cargas»; la columna de verificación lo indica.", f_base),
    ("6. «Resumen» usa 2 días de autonomía, definidos por el grupo. El resto sale de las fórmulas del curso (Aislado 1 y 2) con las pérdidas típicas de clase.", f_base),
    ("La fila 5 de «Cargas» y de «Perfil horario» es un EJEMPLO (televisor de 100 W, 3 h/día, del ejemplo de clase de Aislado 2). No se suma: se puede dejar o borrar.", f_base),
    ("", f_base),
    ("Datos que pide el instructivo para cada equipo", f_b),
    ("Tensión de operación, potencia nominal, potencia pico, corriente nominal, corriente máxima y horas de uso en un día.", f_base),
    ("La potencia pico o de arranque importa en motores y compresores (refrigeradora, bomba de agua, lavadora): define la sobrecarga que debe soportar el inversor.", f_base),
    ("", f_base),
    ("Decisiones del grupo (5 nov. 2026)", f_b),
    ("• El sistema es de respaldo para un grupo de cargas críticas de la casa (la casa tiene servicio eléctrico).", f_base),
    ("• Días de autonomía: 2.", f_base),
    ("", f_base),
    ("Equipos típicos para revisar en la casa (lista de control, sin datos)", f_b),
]
typ = [
    "Iluminación: bombillos o tubos LED por cuarto, luces exteriores",
    "Refrigeradora o congelador (anotar la potencia de arranque del compresor)",
    "Ducha eléctrica o calentador de agua (si es eléctrica, conviene excluirla del sistema aislado y justificarlo)",
    "Cocina o plantilla eléctrica, horno, microondas, olla arrocera, cafetera, tostadora, licuadora",
    "Lavadora y secadora; plancha",
    "Televisores, decodificador o streaming, equipo de sonido",
    "Router y módem de internet",
    "Computadoras, monitores, impresora, cargadores de celulares",
    "Ventiladores",
    "Bomba de agua o hidroneumático (alta corriente de arranque)",
    "Portón eléctrico, cámaras, alarma",
    "Cargas en espera (standby): equipos que consumen apagados",
]
for t, f in lines:
    ws.append([t]); c = ws.cell(ws.max_row, 1); c.font = f; c.alignment = Alignment(wrap_text=True, vertical="top")
for t in typ:
    ws.append(["☐ " + t]); ws.cell(ws.max_row, 1).font = f_base
ws.append([""])
ws.append(["Leyenda"]); ws.cell(ws.max_row, 1).font = f_b
ws.append(["Celda amarilla con texto azul: dato que llena el grupo."]); c = ws.cell(ws.max_row, 1); c.fill = fill_in; c.font = f_in
ws.append(["Texto negro: fórmula, no editar."]); ws.cell(ws.max_row, 1).font = f_base
ws.append(["Texto verde: valor tomado de otra hoja, no editar."]); ws.cell(ws.max_row, 1).font = f_link
ws.append(["Texto gris en cursiva: fila de ejemplo, no se suma."]); ws.cell(ws.max_row, 1).font = f_ex

# ---------------------------------------------------------------- Cargas
wc = wb.create_sheet("Cargas")
hdr = ["#", "Zona o cuarto", "Equipo", "Marca y modelo", "Cant. N", "Tipo (CA/CC)", "Tensión [V]",
       "P nominal [W]", "P pico o arranque [W]", "I nominal [A]", "I máx. [A]", "Horas/día H [h]",
       "¿Carga crítica? (Sí/No)", "Energía N·P·H [Wh/día]", "Fuente del dato",
       "Foto (archivo)", "Observaciones"]
widths = [5, 14, 22, 20, 8, 9, 9, 10, 11, 9, 9, 10, 13, 12, 15, 14, 30]
wc["A1"] = "Levantamiento de cargas: casa de Abner López"; wc["A1"].font = f_t
wc["A2"] = "Llenar solo las celdas amarillas. Energía = N·P·H (Aislado 1), sumada solo si la carga es crítica."; wc["A2"].font = f_base
for j, (h, w) in enumerate(zip(hdr, widths), 1):
    c = wc.cell(4, j, h); c.font = f_b; c.fill = fill_hd; c.alignment = center; c.border = box
    wc.column_dimensions[L(j)].width = w
wc.row_dimensions[4].height = 42

def energy(r):
    return f'=IF(AND(M{r}="Sí",C{r}<>""),E{r}*H{r}*L{r},0)'

ex = [ "Ej.", "Sala", "Televisor (EJEMPLO)", "", 1, "CA", 120, 100, None, None, None, 3, "No", None,
       "Ejemplo de clase", "", "Fila de ejemplo con valores del ejemplo de Aislado 2; no se suma." ]
for j, v in enumerate(ex, 1):
    c = wc.cell(REX, j, v); c.font = f_ex; c.border = box; c.alignment = wrap
wc.cell(REX, 14, f"=E{REX}*H{REX}*L{REX}").font = f_ex

inputs = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 16, 17]
for r in range(R0, R1 + 1):
    wc.cell(r, 1, r - R0 + 1).font = f_base
    wc.cell(r, 1).border = box
    for j in inputs:
        c = wc.cell(r, j); c.fill = fill_in; c.font = f_in; c.border = box
        if j == 17 or j in (2, 3, 4): c.alignment = wrap
    c = wc.cell(r, 14, energy(r)); c.font = f_base; c.border = box; c.number_format = '#,##0;-#,##0;"-"'
for j in (8, 9):
    for r in range(REX, R1 + 1): wc.cell(r, j).number_format = '#,##0.0;-#,##0.0;""'
for r in range(REX, R1 + 1):
    for j in (10, 11, 12): wc.cell(r, j).number_format = '0.00;-0.00;""'

RT = R1 + 2
wc.cell(RT, 3, "Total de cargas críticas").font = f_b
for (lbl, crit, row) in [("Total de cargas críticas", None, RT),
                         ("   en CA", "CA", RT + 1), ("   en CC", "CC", RT + 2)]:
    wc.cell(row, 3, lbl).font = f_b
    if crit:
        fml = f'=SUMIFS({RNG("N")},{RNG("F")},"{crit}")'
    else:
        fml = f'=SUM({RNG("N")})'
    c = wc.cell(row, 14, fml); c.font = f_b; c.fill = fill_tot; c.number_format = '#,##0'
    wc.cell(row, 15, "Wh/día").font = f_base

dv_tipo = DataValidation(type="list", formula1='"CA,CC"', allow_blank=True)
dv_si = DataValidation(type="list", formula1='"Sí,No"', allow_blank=True)
dv_src = DataValidation(type="list", formula1='"Placa,Manual o ficha,Medición,Supuesto"', allow_blank=True)
dv_num = DataValidation(type="decimal", operator="greaterThanOrEqual", formula1="0", allow_blank=True)
dv_h = DataValidation(type="decimal", operator="between", formula1="0", formula2="24", allow_blank=True)
for dv, col in [(dv_tipo, "F"), (dv_si, "M"), (dv_src, "O")]:
    wc.add_data_validation(dv); dv.add(f"{col}{R0}:{col}{R1}")
wc.add_data_validation(dv_num); dv_num.add(f"E{R0}:K{R1}")
wc.add_data_validation(dv_h); dv_h.add(f"L{R0}:L{R1}")
wc.freeze_panes = "D5"
wc["I4"].comment = Comment("Potencia de arranque de motores y compresores. Si la placa no la indica, dejar vacío y anotarlo en Observaciones.", "Grupo")
wc["M4"].comment = Comment("Sí: carga crítica, se respalda con el sistema y se suma. No: queda registrada pero no se suma.", "Grupo")

# ---------------------------------------------------------------- Perfil horario
wp = wb.create_sheet("Perfil horario")
wp["A1"] = "Perfil horario de uso"; wp["A1"].font = f_t
wp["A2"] = "Fracción de cada hora en que el equipo está encendido (1 = toda la hora; 0.5 = media hora; vacío = apagado). Sirve para el gráfico de consumo y para la potencia simultánea del inversor."; wp["A2"].font = f_base
ph = ["#", "Equipo", "Tipo", "N", "P nominal [W]", "¿Crítica?", "H en «Cargas» [h]"] + [f"{h:02d}–{h+1:02d}" for h in range(24)] + ["Suma [h]", "Verificación"]
for j, h in enumerate(ph, 1):
    c = wp.cell(4, j, h); c.font = f_b; c.fill = fill_hd; c.alignment = center; c.border = box
    wp.column_dimensions[L(j)].width = 6.5 if 8 <= j <= 31 else 10
wp.column_dimensions["B"].width = 24
wp.row_dimensions[4].height = 30
H0, H1 = 8, 31  # columnas H..AE
for r in range(REX, R1 + 1):
    links = [f"=Cargas!A{r}", f'=Cargas!C{r}&""', f'=Cargas!F{r}&""', f"=Cargas!E{r}", f"=Cargas!H{r}", f'=Cargas!M{r}&""', f"=Cargas!L{r}"]
    for j, fml in enumerate(links, 1):
        c = wp.cell(r, j, fml); c.font = f_ex if r == REX else f_link; c.border = box
        if j in (4, 5, 7): c.number_format = '0.##;-0.##;""'
    for j in range(H0, H1 + 1):
        c = wp.cell(r, j); c.border = box; c.number_format = '0.##;-0.##;""'
        if r == REX:
            c.font = f_ex
        else:
            c.fill = fill_in; c.font = f_in
    c = wp.cell(r, 32, f"=SUM({L(H0)}{r}:{L(H1)}{r})"); c.number_format = '0.##;-0.##;""'; c.border = box
    c.font = f_ex if r == REX else f_base
    c = wp.cell(r, 33, f'=IF(OR(B{r}="",F{r}<>"Sí"),"",IF(ABS(AF{r}-G{r})<0.01,"OK","Revisar"))'); c.border = box
    c.font = f_ex if r == REX else f_base
for j in (H0 + 19, H0 + 20, H0 + 21):   # ejemplo: TV 19-22 h
    wp.cell(REX, j, 1)
dvf = DataValidation(type="decimal", operator="between", formula1="0", formula2="1", allow_blank=True)
wp.add_data_validation(dvf); dvf.add(f"{L(H0)}{R0}:{L(H1)}{R1}")

rows = [
    ("Energía de las cargas críticas [Wh]", None, "frac"),
    ("   en CA [Wh]", "CA", "frac"),
    ("   en CC [Wh]", "CC", "frac"),
    ("Potencia CA conectada [W]", "CA", "on"),
    ("Potencia total conectada [W]", None, "on"),
]
RP = R1 + 2
for k, (lbl, tipo, kind) in enumerate(rows):
    r = RP + k
    wp.cell(r, 2, lbl).font = f_b
    for j in range(H0, H1 + 1):
        col = L(j)
        cond = f'(${"F"}${R0}:$F${R1}="Sí")'
        if tipo: cond += f'*($C${R0}:$C${R1}="{tipo}")'
        term = f"{col}${R0}:{col}${R1}" if kind == "frac" else f"({col}${R0}:{col}${R1}>0)"
        c = wp.cell(r, j, f"=SUMPRODUCT({cond}*$D${R0}:$D${R1}*$E${R0}:$E${R1}*{term})")
        c.font = f_base; c.fill = fill_tot; c.number_format = '#,##0'
    if kind == "frac":
        c = wp.cell(r, 32, f"=SUM({L(H0)}{r}:{L(H1)}{r})"); c.font = f_b; c.number_format = '#,##0'
    else:
        c = wp.cell(r, 32, f"=MAX({L(H0)}{r}:{L(H1)}{r})"); c.font = f_b; c.number_format = '#,##0'
wp.cell(RP, 33, "Wh/día (suma)").font = f_base
wp.cell(RP + 3, 33, "W (máximo)").font = f_base
wp.cell(RP + 4, 33, "W (máximo)").font = f_base
wp.cell(RP + 6, 2, "La potencia conectada suma la potencia nominal de todo equipo encendido en algún momento de esa hora. Es una cota superior de la potencia simultánea.").font = f_base
wp.freeze_panes = "H5"
RP_CA_ON = RP + 3
RP_TOT = RP

# ---------------------------------------------------------------- Resumen
wr = wb.create_sheet("Resumen")
wr.column_dimensions["A"].width = 52; wr.column_dimensions["B"].width = 14
wr.column_dimensions["C"].width = 10; wr.column_dimensions["D"].width = 70
wr["A1"] = "Resumen del consumo y capacidad del banco"; wr["A1"].font = f_t
wr["A2"] = "Procedimiento del curso (Aislado 1 y 2). Banco de 24 V, DOD de 70 % y batería B4 (Power Queen 25.6 V 200 Ah)."; wr["A2"].font = f_base
r = 4
cells = {}
def head(t):
    global r
    wr.cell(r, 1, t).font = f_b; wr.cell(r, 1).fill = fill_hd
    for j in (2, 3, 4): wr.cell(r, j).fill = fill_hd
    r += 1
def row(key, label, val, unit, note, kind="calc", fmt="0.000"):
    global r
    wr.cell(r, 1, label).font = f_base
    c = wr.cell(r, 2, val); c.number_format = fmt
    c.font = {"in": f_in, "link": f_link, "calc": f_base}[kind]
    if kind == "in": c.fill = fill_in
    wr.cell(r, 3, unit).font = f_base
    wr.cell(r, 4, note).font = f_base; wr.cell(r, 4).alignment = Alignment(wrap_text=True, vertical="top")
    cells[key] = f"$B${r}"; r += 1

head("Datos de diseño")
row("D", "Días de autonomía D", 2, "días", "Decisión del grupo (12 nov. 2026): 2 días, con la Power Queen 24 V 200 Ah.", "in", "0")
row("V", "Tensión del banco V", 24, "V", "Indicado en clase.", "in", "0")
row("DOD", "Profundidad de descarga de diseño DOD", 0.7, "", "Indicado en clase (70 %).", "in", "0%")
row("M", "Margen de seguridad", 1.1, "", "Factor 1.1 de la fórmula del curso.", "in", "0.0")
head("Pérdidas (valores típicos de clase, Aislado 2; se reemplazan con las fichas)")
for k, lbl, v in [("pc", "Caída de tensión en cables p_c", 0.02), ("pd", "Dispersión de la radiación p_d", 0.04),
                  ("ps", "Suciedad p_s", 0.05), ("pmppt", "Seguimiento del MPP p_mppt", 0.02),
                  ("pR", "Regulador p_R", 0.05), ("pb", "Rendimiento de la batería p_b", 0.01),
                  ("pi", "Inversor p_i (solo CA)", 0.05), ("Ka", "Autodescarga diaria K_a", 0.005)]:
    row(k, lbl, v, "", "Valor típico de clase.", "in", "0.000")
head("Batería seleccionada (B4)")
row("C24", "Capacidad de un módulo de 24 V, C_24", 200, "Ah", "Power Queen 25.6 V 200 Ah (manual del fabricante).", "in", "0")
row("Imax", "Corriente continua máxima de descarga por módulo", 200, "A", "Manual del fabricante.", "in", "0")
row("Npmax", "Máximo de módulos en paralelo", 4, "", "Manual del fabricante: 4 en paralelo (800 Ah).", "in", "0")
row("Vmod", "Tensión nominal del módulo", 25.6, "V", "Ficha del fabricante.", "in", "0.0")
head("Consumo (de la hoja «Cargas» y «Perfil horario»)")
row("ECC", "Energía diaria de las cargas en CC, E_CC", f'=SUMIFS(Cargas!{RNG("N")},Cargas!{RNG("F")},"CC")', "Wh/día", "Σ N·P·H de las cargas críticas en CC.", "link", "#,##0")
row("ECA", "Energía diaria de las cargas en CA, E_CA", f'=SUMIFS(Cargas!{RNG("N")},Cargas!{RNG("F")},"CA")', "Wh/día", "Σ N·P·H de las cargas críticas en CA.", "link", "#,##0")
row("E", "Energía diaria de las cargas, E_CC + E_CA", f"={cells['ECC']}+{cells['ECA']}", "Wh/día", "", "calc", "#,##0")
row("Eperf", "Energía según el perfil horario", f"='Perfil horario'!AF{RP_TOT}", "Wh/día", "Debe coincidir con la fila anterior si el perfil está completo.", "link", "#,##0")
row("nrev", "Equipos con perfil horario por revisar", f"=COUNTIF('Perfil horario'!AG{R0}:AG{R1},\"Revisar\")", "", "Debe ser 0.", "link", "0")
row("PCA", "Potencia CA conectada máxima, P_CA", f"='Perfil horario'!AF{RP_CA_ON}", "W", "Base para la potencia del inversor (consumos simultáneos en CA).", "link", "#,##0")
row("Ppico", "Mayor potencia de arranque individual en CA", f'=_xlfn.MAXIFS(Cargas!{RNG("I")},Cargas!{RNG("F")},"CA",Cargas!{RNG("M")},"Sí")', "W", "Para revisar la sobrecarga admisible del inversor.", "link", "#,##0")
head("Factores de rendimiento y energía corregida")
p = cells
sump = f"({p['pc']}+{p['pd']}+{p['ps']}+{p['pmppt']}+{p['pR']}+{p['pb']})"
auto = f"(1-{p['Ka']}*{p['D']}/{p['DOD']})"
row("KTCC", "K_TCC", f"=(1-{sump})*{auto}", "", "K_TCC = (1 − Σp)(1 − K_a·D/DOD)")
row("KTCA", "K_TCA", f"=(1-{sump}-{p['pi']})*{auto}", "", "K_TCA = (1 − Σp − p_i)(1 − K_a·D/DOD)")
row("ET", "Energía total corregida, E_T", f"={p['ECC']}/{cells['KTCC']}+{p['ECA']}/{cells['KTCA']}", "Wh/día", "E_T = E_CC/K_TCC + E_CA/K_TCA", "calc", "#,##0")
head("Capacidad del banco")
row("Q", "Capacidad necesaria Q", f"={p['M']}*{cells['ET']}*{p['D']}/({p['V']}*{p['DOD']})", "Ah", "Q = 1.1·E_T·D/(V·DOD)", "calc", "#,##0")
row("NpE", "Módulos en paralelo por energía", f"=ROUNDUP({cells['Q']}/{p['C24']},0)", "", "⌈Q/C_24⌉", "calc", "0")
row("Ibat", "Corriente de descarga del banco I_bat", f"={cells['PCA']}/({p['V']}*(1-{p['pi']}))", "A", "I_bat = P_CA/(V·η_i), con η_i = 1 − p_i", "calc", "0.0")
row("NpI", "Módulos en paralelo por corriente", f"=ROUNDUP({cells['Ibat']}/{p['Imax']},0)", "", "⌈I_bat/I_máx⌉", "calc", "0")
row("Np", "Módulos en paralelo N_p", f"=MAX({cells['NpE']},{cells['NpI']})", "", "El mayor de los dos.", "calc", "0")
row("chk", "Verificación del máximo en paralelo", f'=IF({cells["Np"]}<={p["Npmax"]},"Cumple","Excede: revisar alternativa B5 o B3")', "", "El fabricante admite hasta 4 en paralelo.", "calc", "@")
row("Ebank", "Energía nominal del banco", f"={cells['Np']}*{p['Vmod']}*{p['C24']}/1000", "kWh", "", "calc", "0.00")
for rr in range(4, r):
    for j in (1, 2, 3, 4): wr.cell(rr, j).border = box

wb.move_sheet("Resumen", offset=-1)
wb.save(out)
print("ok", out)
