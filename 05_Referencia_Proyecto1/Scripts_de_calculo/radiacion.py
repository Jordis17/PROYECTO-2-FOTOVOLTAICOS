import json, numpy as np
N=json.load(open("/home/claude/fv/datos/nasa_power_climatologia.json"))
P=json.load(open("/home/claude/fv/datos/pvgis_y_nasa_resumen.json"))
M=["JAN","FEB","MAR","APR","MAY","JUN","JUL","AUG","SEP","OCT","NOV","DEC"]
mes=["Ene","Feb","Mar","Abr","May","Jun","Jul","Ago","Set","Oct","Nov","Dic"]
dias=np.array([31,28,31,30,31,30,31,31,30,31,30,31])
G=np.array([N["ALLSKY_SFC_SW_DWN"][m] for m in M]); B=np.array([N["ALLSKY_SFC_SW_DNI"][m] for m in M]); D=np.array([N["ALLSKY_SFC_SW_DIFF"][m] for m in M])
Gp=np.array(P["PVGIS_MRcalc"]["H_h_kWh_m2_mo"])/dias
Gopt=np.array(P["PVGIS_MRcalc"]["H_iopt_kWh_m2_mo"])/dias
K={0:[1]*12,
5:[1.03,1.02,1.01,.99,.98,.98,.98,.99,1.01,1.03,1.04,1.04],
10:[1.05,1.04,1.01,.98,.95,.94,.95,.98,1.01,1.04,1.06,1.07],
15:[1.07,1.04,1,.96,.92,.91,.92,.96,1.01,1.05,1.09,1.09],
20:[1.08,1.04,.99,.94,.88,.86,.88,.93,.99,1.06,1.1,1.11],
25:[1.09,1.04,.97,.9,.84,.81,.83,.89,.98,1.06,1.11,1.11],
30:[1.08,1.03,.95,.87,.79,.76,.78,.85,.95,1.05,1.11,1.12],
35:[1.08,1.01,.92,.82,.73,.7,.73,.81,.92,1.03,1.1,1.11],
40:[1.06,.99,.88,.77,.67,.63,.66,.76,.88,1,1.09,1.1]}
if __name__=="__main__":
    print("mes  GHI_N  DNI_N  DHI_N  DHI/GHI  GHI_P  dif%")
    for i in range(12): print(mes[i],G[i],B[i],D[i],round(D[i]/G[i],2),round(Gp[i],3),round(100*(Gp[i]/G[i]-1),1))
    print("anual NASA kWh/m2",round((G*dias).sum(),1)," prom",round((G*dias).sum()/365,3),"| PVGIS",round((Gp*dias).sum(),1),round((Gp*dias).sum()/365,3))
    print("DHI/GHI anual", round((D*dias).sum()/(G*dias).sum(),3))
    for b,k in K.items():
        k=np.array(k); Hn=(G*k*dias).sum(); Hp=(Gp*k*dias).sum()
        print(f"beta={b:2d}  NASA {Hn:7.1f} ({100*(Hn/(G*dias).sum()-1):+.1f}%)  PVGIS {Hp:7.1f} ({100*(Hp/(Gp*dias).sum()-1):+.1f}%)  minmes NASA {min(G*k):.2f}")
    print("PVGIS opt 14 anual", round((Gopt*dias).sum(),1), 100*((Gopt*dias).sum()/(Gp*dias).sum()-1))
