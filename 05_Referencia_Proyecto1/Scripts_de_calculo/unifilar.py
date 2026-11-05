"""Diagrama unifilar del sistema de 168.3 kWp (22 cadenas de 17 módulos, 5 inversores CPS de 25 kW).
Genera el archivo editable de draw.io (unifilar/unifilar.drawio) y el PDF para el informe con matplotlib,
usando las mismas coordenadas (y hacia abajo)."""
import html, re
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyBboxPatch

W, Hc = 1320, 1520
cells = []; nid = [10]; draw = []
def _id(): nid[0] += 1; return f"c{nid[0]}"
def _plain(t):
    t = t.replace("<br>", "\n")
    t = re.sub(r"(\w+)<sub>(\w+)</sub>", lambda m: f"${m.group(1)}_{{{m.group(2)}}}$", t)
    return re.sub(r"<[^>]+>", "", t)
def box(x, y, w, h, txt, style, fill="#FFFFFF", edge="#000000", fs=16, bold=False, rounded=False, dashed=False, align="center", valign="center"):
    i = _id(); cells.append(f'<mxCell id="{i}" value="{html.escape(txt)}" style="{style}" vertex="1" parent="1"><mxGeometry x="{x}" y="{y}" width="{w}" height="{h}" as="geometry"/></mxCell>')
    draw.append(("box", x, y, w, h, _plain(txt), fill, edge, fs, bold or "<b>" in txt, rounded, dashed, align, valign))
def text(x, y, w, h, txt, size=16, align="left", bold=False, color="#000000"):
    st = f"text;html=1;align={align};verticalAlign=middle;whiteSpace=wrap;fontSize={size};fontColor={color};" + ("fontStyle=1;" if bold else "")
    i = _id(); cells.append(f'<mxCell id="{i}" value="{html.escape(txt)}" style="{st}" vertex="1" parent="1"><mxGeometry x="{x}" y="{y}" width="{w}" height="{h}" as="geometry"/></mxCell>')
    draw.append(("text", x, y, w, h, _plain(txt), size, align, bold, color))
def line(pts, color="#000000", w=1.6, dash=False):
    i = _id(); (x0, y0), (x1, y1) = pts[0], pts[-1]
    mid = "".join(f'<mxPoint x="{x}" y="{y}"/>' for x, y in pts[1:-1])
    st = f"endArrow=none;html=1;rounded=0;strokeColor={color};strokeWidth={w};" + ("dashed=1;" if dash else "")
    cells.append(f'<mxCell id="{i}" style="{st}" edge="1" parent="1"><mxGeometry relative="1" as="geometry"><mxPoint x="{x0}" y="{y0}" as="sourcePoint"/><mxPoint x="{x1}" y="{y1}" as="targetPoint"/>' + (f'<Array as="points">{mid}</Array>' if mid else "") + '</mxGeometry></mxCell>')
    draw.append(("line", pts, color, w, dash))
def slash(x, y, n, color):
    for k in range(n): line([(x-5+8*k, y+7), (x+5+8*k, y-7)], color, 1.2)
DC = "#B22222"; AC = "#1F4E79"; GND = "#2E7D32"
F = "fontFamily=Helvetica;"
PV = (F + "rounded=0;whiteSpace=wrap;html=1;fontSize=14;fillColor=#DCE6F2;strokeColor=#1F4E79;", dict(fill="#DCE6F2", edge="#1F4E79", fs=14))
PROT = (F + "rounded=0;whiteSpace=wrap;html=1;fontSize=14;fillColor=#FFF2CC;strokeColor=#7F6000;", dict(fill="#FFF2CC", edge="#7F6000", fs=14))
INV = (F + "rounded=1;whiteSpace=wrap;html=1;fontSize=15;fillColor=#E2EFDA;strokeColor=#375623;", dict(fill="#E2EFDA", edge="#375623", fs=15, rounded=True))
PAN = (F + "rounded=0;whiteSpace=wrap;html=1;fontSize=16;fillColor=#F2F2F2;strokeColor=#404040;verticalAlign=top;fontStyle=1;", dict(fill="#F2F2F2", edge="#404040", fs=16, bold=True, valign="top"))
INFO = (F + "rounded=0;whiteSpace=wrap;html=1;fontSize=15;align=left;verticalAlign=top;spacingLeft=6;spacingTop=4;", dict(fill="#FFFFFF", edge="#000000", fs=15, align="left", valign="top"))
def B(x, y, w, h, t, S, **kw): st, d = S; d = {**d, **kw}; box(x, y, w, h, t, st, **d)

text(20, 6, 1300, 30, "Diagrama unifilar — Sistema FV de 168.3 kWp / 125 kW AC — CoopeAgri R.L., Servicios Complementarios (NISE 2471778)", 19, bold=True)

# ---- Tablero FV ----
B(760, 42, 280, 1210, "TABLERO FV<br>208 V 3Φ, 3H + T", PAN)
nstr = [5, 5, 4, 4, 4]; s0 = 0; y0 = 50; yac_list = []
for b, n in enumerate(nstr):
    ys = [y0 + 8 + 42*k for k in range(n)]
    hb = 42*n + 8
    B(205, y0, 250, hb, "", (F + "rounded=0;whiteSpace=wrap;html=1;dashed=1;fillColor=none;strokeColor=#7F6000;", dict(fill="none", edge="#7F6000", dashed=True)))
    for k, yy in enumerate(ys):
        B(20, yy, 140, 34, f"Cadena {s0+k+1}<br>17 × AIKO 450 W", PV, fs=13)
        line([(160, yy+17), (230, yy+17)], DC); slash(185, yy+17, 2, DC)
        B(230, yy+4, 70, 26, "F 25 A", PROT, fs=13)
    groups = [(0, 1, "MPPT 1"), (2, 3, "MPPT 2"), (4, 4, "MPPT 3")] if n == 5 else [(0, 1, "MPPT 1"), (2, 2, "MPPT 2"), (3, 3, "MPPT 3")]
    for a, c, lab in groups:
        ya, yc = ys[a]+17, ys[c]+17; ym = (ya+yc)/2
        line([(300, ya), (320, ya), (320, yc), (300, yc)] if a != c else [(300, ya), (335, ya)], DC)
        if a != c: line([(320, ym), (335, ym)], DC)
        B(335, ym-16, 105, 32, f"Entrada {lab}", PROT, fs=12)
        line([(440, ym), (500, ym)], DC)
    text(205, y0+hb+1, 300, 18, "Caja de conexiones del inversor", 12, bold=True, color="#7F6000")
    kwp = n*7.65
    B(500, y0+4, 160, hb-8, f"INVERSOR {b+1}<br>CPS SCA25KTL-DO/US-208<br>25 kW · 3 MPPT · 208 V 3Φ<br>{n} cadenas · {kwp:.2f} kWp<br>Secc. DC y DPS DC/AC integrados", INV, fs=13)
    yac = y0 + hb/2
    line([(660, yac), (770, yac)], AC, 2.2); slash(685, yac, 3, AC)
    text(662, yac+6, 108, 40, "3×3 AWG THHN<br>+ 8 AWG T, 15 m", 12)
    B(770, yac-20, 90, 40, "TM 3P<br>90 A", PROT, fs=13)
    line([(860, yac), (880, yac)], AC, 2.2)
    B(880, yac-22, 110, 44, "ID 3P 100 A<br>300 mA", PROT, fs=13)
    line([(990, yac), (1010, yac)], AC, 2.2)
    yac_list.append(yac); s0 += n; y0 += hb + 34

# ---- Barra del tablero FV y salida ----
ybot = 1200
line([(1010, yac_list[0]), (1010, ybot)], AC, 4)
B(880, 1130, 110, 40, "DPS AC tipo 2", PROT, fs=13); line([(990, 1150), (1010, 1150)], AC, 1.5)
line([(1010, ybot), (1010, 1290), (1060, 1290)], AC, 2.5); slash(1030, 1290, 3, AC)
text(700, 1262, 300, 44, "2×(3×250 kcmil THHN) + 2×2 AWG T, 15 m", 13, align="right")
B(1060, 1258, 120, 64, "Seccionador<br>visible 3P 600 A<br>con bloqueo", PROT, fs=12)
line([(1180, 1290), (1215, 1290), (1215, 860)], AC, 2.5)
B(1105, 620, 210, 240, "TABLERO PRINCIPAL EXISTENTE<br>120/208 V 3Φ 4H<br>Cargas del edificio", PAN, fs=15)
B(1150, 780, 130, 64, "Interruptor de<br>interconexión<br>3P 450 A", PROT, fs=12)
line([(1215, 620), (1215, 590)], AC, 2.5)
B(1150, 500, 130, 90, "Medidor<br>bidireccional ICE", PROT, fs=14)
line([(1215, 500), (1215, 430)], AC, 2.5)
B(1150, 350, 130, 80, "Red ICE", PAN)

# ---- Tierra ----
B(560, 1340, 740, 34, "Barra de puesta a tierra — sistema de electrodos del edificio", (F + f"rounded=0;whiteSpace=wrap;html=1;fontSize=15;fillColor=#E2EFDA;strokeColor={GND};", dict(fill="#E2EFDA", edge=GND, fs=15)))
line([(90, 1230), (90, 1357), (560, 1357)], GND, 1.3, True)
text(100, 1310, 440, 26, "Marcos y rieles unidos con grapas BND y Cu desnudo 10 AWG", 13, color=GND)
line([(880, 1252), (880, 1340)], GND, 1.3, True); line([(1210, 860), (1300, 860), (1300, 1340)], GND, 1.3, True)

# ---- Cuadros de información ----
B(20, 1392, 420, 120, "Resumen<br>374 módulos AIKO-A450-MAH54Mb (450 W), 168.3 kWp<br>22 cadenas de 17 módulos; 5 inversores de 25 kW<br>Inversores 1–2: 5 cadenas · 3–5: 4 cadenas<br>Inclinación 10°, orientación sur", INFO, fs=14)
B(450, 1392, 420, 120, "Valores por cadena<br>V<sub>oc</sub> a 14.1 °C: 708 V (máx. 1000 V)<br>V<sub>mp</sub>: 503 V (64.3 °C) y 592 V (14.1 °C)<br>I<sub>sc</sub> a 64.3 °C: 14.4 A<br>DC: 10 AWG PV Wire, ≤ 40 m · fusible gPV 25 A", INFO, fs=14)
B(880, 1392, 420, 120, "Notas<br>Rojo: DC · azul: AC · verde discontinuo: tierra<br>Marcas oblicuas: conductores activos<br>Longitudes estimadas · TM: termomagnético<br>ID: interruptor diferencial · DPS: protección contra sobretensiones", INFO, fs=14)

xml = (f'<mxfile host="drawio"><diagram name="Unifilar"><mxGraphModel dx="1400" dy="1500" grid="0" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="{W}" pageHeight="{Hc}" math="0" shadow="0">'
       '<root><mxCell id="0"/><mxCell id="1" parent="0"/>' + "".join(cells) + '</root></mxGraphModel></diagram></mxfile>')
open("/home/claude/fv/unifilar/unifilar.drawio", "w").write(xml)

# ---- PDF con matplotlib ----
plt.rcParams.update({"font.family": "DejaVu Sans", "mathtext.fontset": "dejavusans"})
sc = 7.0/W
fig = plt.figure(figsize=(W*sc, Hc*sc)); ax = fig.add_axes([0, 0, 1, 1]); ax.set_xlim(0, W); ax.set_ylim(Hc, 0); ax.axis("off")
pt = 0.72*sc*72      # 1 px de draw.io en puntos tipográficos
for d in draw:
    if d[0] == "box":
        _, x, y, w, h, t, fill, edge, fs, bold, rounded, dashed, align, valign = d
        if rounded:
            p = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0,rounding_size=14", fc=fill, ec=edge, lw=0.8)
        else:
            p = Rectangle((x, y), w, h, fc=(fill if fill != "none" else "none"), ec=edge, lw=0.8, ls="--" if dashed else "-")
        ax.add_patch(p)
        if t:
            lines = t.split("\n"); fsz = fs*pt
            if align == "left":
                tx, ha = x+8, "left"
            else:
                tx, ha = x+w/2, "center"
            ty, va = (y+6, "top") if valign == "top" else (y+h/2, "center")
            if bold and lines and "<b>" not in t and align == "left":
                pass
            ax.text(tx, ty, t, ha=ha, va=va, fontsize=fsz, linespacing=1.25, fontweight="bold" if (bold and align != "left") else "normal", wrap=False)
    elif d[0] == "text":
        _, x, y, w, h, t, size, align, bold, color = d
        tx, ha = (x, "left") if align == "left" else ((x+w, "right") if align == "right" else (x+w/2, "center"))
        ax.text(tx, y+h/2, t, ha=ha, va="center", fontsize=size*pt, fontweight="bold" if bold else "normal", color=color, linespacing=1.2)
    else:
        _, pts, color, w, dash = d
        xs, ys = zip(*pts); ax.plot(xs, ys, color=color, lw=w*0.55, ls=(0, (4, 3)) if dash else "-", solid_capstyle="butt")
fig.savefig("/home/claude/fv/unifilar/unifilar.pdf"); fig.savefig("/home/claude/fv/informe/figuras/unifilar.pdf")
fig.savefig("/home/claude/fv/unifilar/unifilar.png", dpi=250)
print("ok", len(cells))
