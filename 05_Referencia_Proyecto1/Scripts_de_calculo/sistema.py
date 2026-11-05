import sys; sys.path.insert(0,"/home/claude/fv/scripts")
import numpy as np, math
from radiacion import G, K, dias, mes
# Módulo (Sección IV)
Voc_min,Vmp_min,Isc_min,Imp_min=41.67,34.51,14.04,13.29
Voc_max,Vmp_max,Isc_max,Imp_max=37.18,30.79,14.40,13.62
Voc,Vmp,Isc,Imp,P=40.69,33.70,14.12,13.36,450
# Inversor CPS SCA25KTL-DO/US-208
Pac=25e3; Vdcmax=1000; Vmppt=(480,850); Vstart=330; IscMPPT=36; PmpptMax=17e3; PpvMax=45e3; nMPPT=3
print("Rango P_STC por inversor:",1.2*Pac,1.5*Pac)
print("Nmax serie inversor:",Vdcmax/Voc_min, " módulo:",1500/Voc_min)
print("Nmin MPPT:",Vmppt[0]/Vmp_max," Nmax MPPT:",Vmppt[1]/Vmp_min," Nmin arranque:",Vstart/Voc_max)
print("Cadenas por MPPT:",IscMPPT/Isc_max)
n=18; ns=4; inv=2
N=n*ns*inv; Pfv=N*P/1000
print("Total módulos",N,"Pfv kWp",Pfv,"relación DC/AC",Pfv/(2*Pac/1000))
for lab,(v1,v2) in {"Voc_min":(Voc_min,0),"Vmp_min":(Vmp_min,0),"Vmp_max":(Vmp_max,0),"Voc_max":(Voc_max,0),"Voc_STC":(Voc,0),"Vmp_STC":(Vmp,0)}.items(): print(lab,"cadena",round(n*v1,1))
print("Isc 2 cadenas hot",2*Isc_max,"Imp 2 cad hot",2*Imp_max," Imp2 STC",2*Imp)
print("P MPPT (2 cad) STC",2*n*P,"Tmin",2*n*462.8)
# PR
f={"Temperatura":0.07,"Cableado":0.02,"Dispersión":0.02,"Suciedad":0.03,"Seguimiento MPP":0.01,"Reflectancia":0.02}
PR=np.prod([1-v for v in f.values()])*0.965
print("PR",PR)
H=G*np.array(K[10])
E=H*Pfv*PR*dias
cons=np.array([18482,17626,18238,18850,19339,18482,18972,19094,18238,18727,17993,18972]) # ene..dic (ene-ago 2026, set-dic 2025)
for i in range(12): print(mes[i],round(H[i],2),round(E[i]),round(100*E[i]/cons[i],1))
print("Anual",round(E.sum()),"yield",round(E.sum()/Pfv),"cobertura",round(100*E.sum()/cons.sum(),1), "cons",cons.sum())
np.save("/home/claude/fv/datos/E_mensual.npy",E)
