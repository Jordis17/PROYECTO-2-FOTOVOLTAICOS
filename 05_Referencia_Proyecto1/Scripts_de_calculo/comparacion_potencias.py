"""Comparación de alternativas de potencia: energía, inversión, factura T-CO y flujo de caja.
Usa datos/autoconsumo_horario_v2.json (balance horario con NASA POWER 2015-2024)."""
import json, numpy as np

TC = 456.61; EURUSD = 1.1479
d = json.load(open('/home/claude/fv/datos/autoconsumo_horario_v2.json'))

# ---------------- Datos de facturas (mes calendario) ----------------
C = np.array([18482,17626,18238,18850,19339,18482,18972,19094,18238,18727,17993,18972.])
D = np.array([43.70,49.33,45.78,46.14,46.88,45.78,44.19,47.25,53.00,47.12,44.92,44.31])
Fact = np.array([1784895,1787605,1790965,1837895,1880430,1808075,1824720,1867375,2197090,2160335,2071120,2143700.])
# ---------------- Tarifas 2026 ----------------
pe, pd_, pa, iva, bomb = 59.67, 9861.68, 2.70, 0.13, 1827.40   # T-CO no horaria (ICE 2026)
p_exc = 27.40          # compra de excedentes ICE 2026 (punta y valle)
tder = 255.0           # ¢/kW-mes por kWp instalado, + IVA
def factura(Ecompra, Dem, kwp=0.0):
    en = Ecompra*pe; de = Dem*pd_; al = Ecompra*pa; t = tder*kwp
    return en + de + al + iva*(en + de + t) + t + bomb
conv = factura(C, D)

# ---------------- Costos (USD) por alternativa ----------------
def costo(Pdc, Pac):
    nmod = round(Pdc*1000/450); ninv = int(Pac/25); ncad = nmod//18
    eq = {}
    eq['Módulos'] = nmod*128.96*EURUSD
    eq['Inversores'] = ninv*8997.44
    eq['Estructura'] = nmod*16883/144              # BOM SolarMount por módulo
    eq['Cable DC'] = ncad*0.5*259.99                # 2x30 m PV Wire por cadena
    eq['Cable AC inversores'] = ninv*148*2.56       # 3x3 AWG + tierra, 15 m
    eq['Interruptores inversores'] = ninv*1174.50   # 3P 90 A
    I = 1.25*ninv*69.5
    # interruptor general, alimentador (15 m, 3 fases) y seccionador según la corriente
    if I <= 175:   g, cab, sec = 3120.00, 148*5.53, 976.33      # 175 A, 2/0, 200 A
    elif I <= 300: g, cab, sec = 3600.00, 148*10.0, 2320.00     # 300 A, 350 kcmil (est.), 400 A
    elif I <= 400: g, cab, sec = 4100.00, 2*148*6.5, 2320.00    # 350-400 A, 2x3/0 (est.), 400 A
    else:          g, cab, sec = 6500.00, 2*148*10.0, 4500.00   # 450-600 A (est.)
    eq['Interruptor general'] = g; eq['Alimentador AC'] = cab; eq['Seccionador'] = sec
    elec = sum(v for k, v in eq.items() if k not in ('Módulos','Inversores','Estructura'))
    eq['Otros eléctricos (15 %)'] = 0.15*elec
    equipo = sum(eq.values())
    serv = (300000 + 80000 + 200000 + 382871 + 100000*Pdc)/TC
    precio = 1.2*(equipo + serv)
    return dict(nmod=nmod, ninv=ninv, ncad=ncad, I=I, equipo=equipo, serv=serv, precio_usd=precio,
                precio_crc=precio*TC)

# ---------------- Flujo de caja (proyecto, sin financiamiento) ----------------
def indicadores(I0, ahorro1, esc, tasa=0.07, anos=25, om=0.01):
    F = [-I0]; deg = 1.0
    for k in range(1, anos+1):
        if k == 2: deg *= 0.99
        elif k > 2: deg *= 1 - 0.0035
        F.append(ahorro1*deg*(1+esc)**(k-1) - om*I0*(1+esc)**(k-1))
    F = np.array(F)
    vpn = sum(f/(1+tasa)**i for i, f in enumerate(F))
    lo, hi = -0.5, 1.0
    for _ in range(200):
        mid = (lo+hi)/2
        lo, hi = (mid, hi) if sum(f/(1+mid)**i for i, f in enumerate(F)) > 0 else (lo, mid)
    c = np.cumsum(F); k = int(np.argmax(c >= 0))
    pri = (k-1 + (-c[k-1])/F[k]) if c[-1] >= 0 else float('nan')
    return vpn, mid, pri

res = []
for k, info, alts in d['out']:
    for Pdc, Pac, M in alts:
        gen, slf, exp = (np.array(M[q], float) for q in ('gen', 'self', 'exp'))
        compra = C - slf
        c = costo(Pdc, Pac)
        for exc in (True, False):
            for red in (0.0, 0.10, 0.20):
                fv = factura(compra, D*(1-red), Pdc) - (exp*p_exc if exc else 0)
                ah = conv.sum() - fv.sum()
                for esc in (0.0, 0.03):
                    vpn, tir, pri = indicadores(c['precio_crc'], ah, esc)
                    res.append(dict(k=k, Pdc=Pdc, Pac=Pac, exc=exc, red=red, esc=esc, gen=gen.sum(), self=slf.sum(),
                                    exp=exp.sum(), compra=compra.sum(), fsc=slf.sum()/gen.sum(),
                                    ahorro=ah, fv=fv.sum(), vpn=vpn, tir=tir, pri=pri, **c))
json.dump(res, open('/home/claude/fv/datos/comparacion_potencias.json', 'w'), indent=1, default=float)

if __name__ == '__main__':
    print('Factura modelo sin FV: %.2f M  (facturado: %.2f M; ene-ago 2026 modelo %.2f vs real %.2f)' % (
        conv.sum()/1e6, Fact.sum()/1e6, conv[:8].sum()/1e6, Fact[:8].sum()/1e6))
    print('Cargo demanda anual con IVA: %.2f M' % ((D*pd_*1.13).sum()/1e6))
    for r in res:
        if r['red'] == 0 and r['esc'] == 0 and r['exc']:
            print(f"k{r['k']} {r['Pdc']:6.1f}/{r['Pac']:3.0f} mod{r['nmod']} inv{r['ninv']} I{r['I']:.0f} "
                  f"gen{r['gen']/1e3:6.1f} self{r['self']/1e3:6.1f} ({r['fsc']*100:4.1f}%) exp{r['exp']/1e3:5.1f} "
                  f"compra{r['compra']/1e3:6.1f} inv{r['precio_crc']/1e6:5.1f}M ({r['precio_usd']/r['Pdc']/1000:.2f}USD/W) "
                  f"ah{r['ahorro']/1e6:5.2f}M vpn{r['vpn']/1e6:6.1f} tir{r['tir']*100:5.1f} pri{r['pri']:5.1f}")
