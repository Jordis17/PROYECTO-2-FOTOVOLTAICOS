import numpy as np
PHI=9.37695; L=-83.701886; LR=-90.0
def dbar_deg(d): return d*360/360.25
def eot_h(d):
    db=np.radians(dbar_deg(d))
    return -0.128*np.sin(db-np.radians(2.80))-0.165*np.sin(2*db+np.radians(19.7))
def decl(d):
    db=d*2*np.pi/365.25
    return np.degrees(np.arcsin(0.3978*np.sin(db-1.400+0.0355*np.sin(db-0.0489))))
def sunpos(d,ts):
    dl=np.radians(decl(d)); ph=np.radians(PHI); w=np.radians(15*(ts-12))
    sh=np.sin(ph)*np.sin(dl)+np.cos(ph)*np.cos(dl)*np.cos(w)
    h=np.arcsin(sh)
    # acimut medido desde el sur (positivo hacia el oeste), curso RS2 p27; cuadrante por cos(alpha)
    sa=np.cos(dl)*np.sin(w)/np.cos(h)
    ca=(np.sin(h)*np.sin(ph)-np.sin(dl))/(np.cos(h)*np.cos(ph))
    a_s=np.degrees(np.arctan2(sa,ca))
    a_n=(a_s+180)%360   # acimut desde el norte, sentido horario (convención de los diagramas del curso)
    return np.degrees(h),a_n
def ts_from_local(d,tl): return tl+(L-LR)/15+eot_h(d)
if __name__=="__main__":
    for name,d in [("21 mar",80),("21 jun",172),("23 set",266),("21 dic",355)]:
        h,a=sunpos(d,12.0)
        sunrise=12-np.degrees(np.arccos(-np.tan(np.radians(PHI))*np.tan(np.radians(decl(d)))))/15
        tl_noon=12-(L-LR)/15-eot_h(d)
        print(f"{name}: d={d} decl={decl(d):6.2f} eot={eot_h(d)*60:6.1f} min  h_noon={h:5.1f} az_noon={a:5.1f}  mediodia_solar_local={int(tl_noon)}:{(tl_noon%1)*60:04.1f}  salida_solar(ts)={sunrise:.2f}  duracion={2*(12-sunrise):.2f} h")
