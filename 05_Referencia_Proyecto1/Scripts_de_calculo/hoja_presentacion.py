import re, glob, os
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.comments import Comment
D="/tmp/claude-0/-home-claude/ff53d67a-765a-5ceb-99fe-aaffd7d17607/scratchpad/deck/project/slides/"
rows=[
("cover","Portada","Título, integrantes, curso y semestre","Inicio","A. López",20),
("sitio","Lugar de estudio","Vista satelital, gráfico de consumo y cuatro cifras clave","Sitio y recurso solar","A. López",50),
("recorrido","Recorrido solar","Diagrama cilíndrico y los tres ángulos importantes","Sitio y recurso solar","A. López",40),
("radiacion","Recurso solar","Componentes de radiación y comparación NASA–PVGIS","Sitio y recurso solar","A. López",45),
("inclinacion","Inclinación","Curva de energía según la inclinación y la decisión de 10°","Sitio y recurso solar","A. López",45),
("modulo","Módulo","Datos de la ficha y tabla de efecto de la temperatura","Módulo y dimensionamiento","S. Rojas",45),
("criterio","Criterio de tamaño","Por qué se limitó a 50 kW, con las cifras del sistema","Módulo y dimensionamiento","S. Rojas",60),
("configuracion","Inversor y configuración","Tabla de comprobación y gráfico SOA","Módulo y dimensionamiento","S. Rojas",60),
("produccion","Producción","Generación frente a consumo y factor de rendimiento","Módulo y dimensionamiento","S. Rojas",45),
("instalacion","Instalación","Montaje, conductores y protecciones","Instalación y economía","J. Segura",50),
("unifilar","Diagrama unifilar","El diagrama a tamaño completo","Instalación y economía","J. Segura",40),
("economia","Economía","Costo, ahorro, escenarios y flujo acumulado","Instalación y economía","J. Segura",60),
("conclusiones","Conclusiones","Resultados y lo que falta confirmar","Cierre","J. Segura",40)]
def notes(i):
    s=open(D+i+".html").read(); m=re.search(r"<aside>(.*?)</aside>",s,re.S); return m.group(1).strip() if m else ""
wb=Workbook(); ws=wb.active; ws.title="Plan de presentación"
A="Arial"; bold=Font(name=A,bold=True); base=Font(name=A); blue=Font(name=A,color="0000FF")
hdrfill=PatternFill("solid",fgColor="1F3A5F"); yel=PatternFill("solid",fgColor="FFFF00")
thin=Side(style="thin",color="BFBFBF"); bd=Border(left=thin,right=thin,top=thin,bottom=thin)
ws["A1"]="Plan de la presentación — Sistema FV conectado a red, CoopeAgri (EL5854)"; ws["A1"].font=Font(name=A,bold=True,size=14)
ws["A2"]="Duración objetivo [s]"; ws["A2"].font=bold
ws["C2"]=600; ws["C2"].font=blue; ws["C2"].fill=yel; ws["C2"].comment=Comment("Exposición de 10 minutos solicitada por el profesor (instructivo del proyecto).","Claude")
ws["D2"]="Duración total [s]"; ws["D2"].font=bold
ws["E2"]="=SUM(F6:F18)"; ws["E2"].font=base
ws["F2"]="Diferencia [s]"; ws["F2"].font=bold
ws["G2"]="=E2-C2"; ws["G2"].font=base
ws["A3"]="Leyenda: celdas con texto azul y fondo amarillo = editables (expositor, tiempo, duración objetivo). Los tiempos y la asignación de expositores son una propuesta inicial."
ws["A3"].font=Font(name=A,italic=True,size=9)
hdr=["#","Id","Diapositiva","Qué muestra","Sección","Tiempo [s]","Inicio [mm:ss]","Fin [mm:ss]","Expositor","Notas del orador"]
for c,h in enumerate(hdr,1):
    x=ws.cell(row=5,column=c,value=h); x.font=Font(name=A,bold=True,color="FFFFFF"); x.fill=hdrfill; x.alignment=Alignment(horizontal="center",vertical="center",wrap_text=True); x.border=bd
for k,(i,t,q,sec,who,sec_t) in enumerate(rows):
    r=6+k
    vals=[k+1,i,t,q,sec,sec_t,None,None,who,notes(i)]
    for c,v in enumerate(vals,1):
        x=ws.cell(row=r,column=c,value=v); x.font=base; x.border=bd; x.alignment=Alignment(vertical="top",wrap_text=True)
    for c in (6,9): ws.cell(row=r,column=c).font=blue; ws.cell(row=r,column=c).fill=yel
    ws.cell(row=r,column=7,value=("=0" if k==0 else f"=H{r-1}"))
    ws.cell(row=r,column=8,value=f"=G{r}+F{r}/86400")
    ws.cell(row=r,column=6).value=sec_t
    # start/end as time: convert seconds
    ws.cell(row=r,column=7).number_format="mm:ss"; ws.cell(row=r,column=8).number_format="mm:ss"
    for c in (7,8): ws.cell(row=r,column=c).font=base; ws.cell(row=r,column=c).border=bd; ws.cell(row=r,column=c).alignment=Alignment(vertical="top")
ws["E2"].number_format="0"; ws["G2"].number_format='0;-0;0'
r=20; ws.cell(row=r,column=1,value="Tiempo por expositor").font=bold
for j,n in enumerate(["A. López","S. Rojas","J. Segura"]):
    ws.cell(row=r+1+j,column=1,value=n).font=base
    ws.cell(row=r+1+j,column=3,value=f'=SUMIF($I$6:$I$18,A{r+1+j},$F$6:$F$18)').font=base
    ws.cell(row=r+1+j,column=4,value=f'=C{r+1+j}/$E$2').font=base; ws.cell(row=r+1+j,column=4).number_format="0.0%"
ws.cell(row=r,column=3,value="Segundos").font=bold; ws.cell(row=r,column=4,value="% del total").font=bold
widths=[5,14,24,44,24,11,11,11,13,90]
for c,w in enumerate(widths,1): ws.column_dimensions[chr(64+c)].width=w
for k in range(13): ws.row_dimensions[6+k].height=105
ws.freeze_panes="C6"
wb.save("/home/claude/fv/presentacion/plan_presentacion.xlsx")
