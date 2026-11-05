import numpy as np, json
TC=456.61          # ¢/USD BCCR venta 9-oct-2026
EURUSD=1.1479
# ---------- Costos ----------
eq=[ # (rubro, desc, cant, precio unitario USD, fuente)
("Módulos","AIKO-A450-MAH54Mb",144,128.96*EURUSD,"cambioenergetico"),
("Inversores","CPS SCA25KTL-DO/US-208",2,8997.44,"solarcellzusa"),
("Estructura","Riel SM 240 in",64,101.10,"hoja"),
("Estructura","Empalme 303019M",48,10.81,"portlandia"),
("Estructura","Grapa intermedia BND",272,4.15,"hoja"),
("Estructura","Grapa extremo",32,3.55,"hoja"),
("Estructura","L-Foot",304,4.35,"hoja"),
("Estructura","Pata inclinación 307107M",152,32.01,"portlandia"),
("Estructura","S-5-U Mini",304,7.66,"portlandia"),
("Estructura","Terminal tierra ILSCO",16,8.40,"hoja"),
("Cableado","PV Wire 10 AWG, carrete 500 ft",4,259.99,"portlandia"),
("Cableado","THHN 3 AWG [ft]",296,2.56,"elliott"),
("Cableado","THHN 2/0 AWG [ft]",148,5.53,"elliott"),
("Protecciones","TM 3P 90 A QDL32090",2,1174.50,"superbreakers"),
("Protecciones","TM 3P 175 A LAL36175",1,3120.00,"superbreakers"),
("Protecciones","Seccionador 200 A D324N",1,976.33,"supplyhouse"),
]
tot={}
for r,d,q,p,s in eq: tot[r]=tot.get(r,0)+q*p
tot["Otros eléctricos"]=0.15*(tot["Cableado"]+tot["Protecciones"])
equipo=sum(tot.values())
serv_crc={"Estudios de factibilidad":300000,"Viabilidad ante el ICE":80000,"Visado de planos (CFIA)":200000,
          "Interconexión ICE (etapas 1-4, con IVA)":18591.89+142355.14+131746.70+90177.39,"Instalación (¢100 000/kW)":100000*64.8}
serv=sum(serv_crc.values())/TC
costo=equipo+serv; precio=costo*1.2
print({k:round(v) for k,v in tot.items()}, "equipo",round(equipo),"serv USD",round(serv),"costo",round(costo),"precio",round(precio),"precio CRC",round(precio*TC), "USD/W",precio/64800)
# ---------- Energía y facturación (año 1, tarifas 2026) ----------
mes=["Ene","Feb","Mar","Abr","May","Jun","Jul","Ago","Set","Oct","Nov","Dic"]
E=np.load("/home/claude/fv/datos/E_mensual.npy")
C=np.array([18482,17626,18238,18850,19339,18482,18972,19094,18238,18727,17993,18972],float)
D=np.array([43.70,49.33,45.78,46.14,46.88,45.78,44.19,47.25,53.00,47.12,44.92,44.31])
pe,pd,pa,iva,bomb=59.67,9861.68,2.70,0.13,1827.40
tac=25.0; tder=255.0; kWinst=64.8
fac=0.60   # autoconsumo inmediato (ejemplo del curso, Normativa p49)
def factura(Ered,Dem,acc=0,der=0):
    en=Ered*pe; de=Dem*pd; al=Ered*pa
    return en+de+al+iva*(en+de+acc+der)+acc+der+bomb
conv=np.array([factura(C[i],D[i]) for i in range(12)])
inm=fac*E; dep=E-inm; lim=0.49*E; recon=np.minimum(dep,lim); nore=dep-recon
EN=C-inm               # energía retirada de la red
neta=C-E+nore          # energía facturada a tarifa completa
fv=np.array([factura(neta[i],D[i],acc=recon[i]*tac,der=tder*kWinst) for i in range(12)])
ahorro=conv-fv
res=dict(conv=conv.sum(),fv=fv.sum(),ahorro=ahorro.sum())
print({k:round(v) for k,v in res.items()}, "pct",ahorro.sum()/conv.sum())
for i in range(12): print(mes[i],round(E[i]),round(inm[i]),round(dep[i]),round(EN[i]),round(conv[i]),round(fv[i]),round(ahorro[i]))
# ---------- Flujo de caja (como la hoja) ----------
r_esc=0.05; i_an=0.09; n=120; tasa=0.07; anos=25
P=precio*TC; prest=0.8*P; ini=0.2*P
im=i_an/12; cuota=prest*im/(1-(1+im)**-n); pago_an=12*cuota
mant0=0.01*precio*TC
def flujo(esc=r_esc,fin=True,fac_deg=True):
    F=[-(ini if fin else P)]; ah=ahorro.sum()
    deg=1.0
    for y in range(1,anos+1):
        if y==2: deg*=0.99
        elif y>2: deg*=(1-0.0035)
        a=ah*deg*(1+esc)**(y-1)
        m=mant0*(1+esc)**(y-1)
        d=pago_an if (fin and y<=10) else 0
        F.append(a-m-d)
    return np.array(F)
def npv(r,F): return sum(f/(1+r)**k for k,f in enumerate(F))
def irr(F):
    lo,hi=-0.9,1.0
    for _ in range(200):
        mid=(lo+hi)/2
        if npv(mid,F)>0: lo=mid
        else: hi=mid
    return mid
def pri(F):
    c=np.cumsum(F); k=np.argmax(c>=0)
    return k-1+(-c[k-1])/F[k] if c[-1]>=0 else None
out={}
for lab,kw in [("base",{}),("sin_esc",{"esc":0.0}),("contado",{"fin":False}),("contado_sin_esc",{"esc":0.0,"fin":False})]:
    F=flujo(**kw); out[lab]=dict(VPN=npv(tasa,F),TIR=irr(F),PRI=pri(F),IR=1+npv(tasa,F)/abs(F[0]),F0=F[0],F1=F[1],F11=F[11])
    print(lab,{k:(round(v,3) if v is not None else None) for k,v in out[lab].items()})
print("cuota mensual",round(cuota),"pago anual",round(pago_an),"inicial",round(ini),"prestamo",round(prest),"mant0",round(mant0))
json.dump(dict(tot=tot,equipo=equipo,serv_crc=serv_crc,costo=costo,precio=precio,ahorro=ahorro.tolist(),conv=conv.tolist(),fv=fv.tolist(),E=E.tolist(),inm=inm.tolist(),dep=dep.tolist(),EN=EN.tolist(),out=out,cuota=cuota,ini=ini,prest=prest,mant0=mant0,F=flujo().tolist(),Fc=flujo(fin=False).tolist()),open("/home/claude/fv/datos/economia.json","w"),default=float,indent=1)
