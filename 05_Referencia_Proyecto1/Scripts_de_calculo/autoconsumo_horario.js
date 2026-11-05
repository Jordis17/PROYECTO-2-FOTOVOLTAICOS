// Balance horario generación-carga del sistema de 168.3 kWp (22 cadenas, 5 inversores) y de las alternativas (versión final, 11 oct 2026).
// Se ejecuta en la consola del navegador en https://power.larc.nasa.gov (el contenedor no accede a la API de NASA POWER).
// Resultado: datos/balance_horario_final.json. Procedimiento equivalente en Python: scripts/simulacion_horaria.py.
window.D = window.D || {};
for (let y = 2015; y <= 2024; y++) {
  if (window.D[y]) continue;
  const u = `https://power.larc.nasa.gov/api/temporal/hourly/point?parameters=ALLSKY_SFC_SW_DWN,T2M&community=RE&longitude=-83.7019&latitude=9.3769&start=${y}0101&end=${y}1231&format=JSON&time-standard=LST`;
  window.D[y] = (await fetch(u).then(r => r.json())).properties.parameter;
}
// Energía mensual por kWp sin recorte: HSP(10°, factores K) · PR mensual · días (diseno_final.py; pérdida térmica de cada mes).
const ykWp = [119.552,119.396,133.251,113.613,102.708,97.453,98.85,104.945,108.918,104.475,94.172,108.863];
const C = [18482,17626,18238,18850,19339,18482,18972,19094,18238,18727,17993,18972];
const Dm = [43.70,49.33,45.78,46.14,46.88,45.78,44.19,47.25,53.00,47.12,44.92,44.31];
const H = [];
for (let y = 2015; y <= 2024; y++) { const P = window.D[y]; for (const k of Object.keys(P.ALLSKY_SFC_SW_DWN)) {
  const m = +k.slice(4,6)-1, d = +k.slice(6,8), h = +k.slice(8,10);
  H.push({ y, m, h, dow: new Date(y, m, d).getDay(), G: Math.max(0, P.ALLSKY_SFC_SW_DWN[k]), T: P.T2M[k] }); } }
const S = Array(12).fill(0); for (const r of H) S[r.m] += r.G/10;
for (const r of H) r.g = r.G*ykWp[r.m]/S[r.m];                    // generación horaria por kWp
const open = r => (r.dow != 0 && r.h >= 6 && r.h <= 20);           // lunes a sábado, 6:00 a 21:00
const cnt = {}; for (const r of H) { const key = r.y+'-'+r.m; cnt[key] = cnt[key] || {o:0, c:0}; open(r) ? cnt[key].o++ : cnt[key].c++; }
function sim(inv, k) {   // inv: kWp por inversor de 25 kW; k: carga en horario de atención como fracción de la demanda
  const M = { gen: Array(12).fill(0), self: Array(12).fill(0), clip: 0 };
  for (const r of H) { const key = r.y+'-'+r.m;
    const L = open(r) ? k*Dm[r.m] : (C[r.m]-k*Dm[r.m]*cnt[key].o)/cnt[key].c;
    let g = 0; for (const p of inv) { let gi = r.g*p; if (gi > 25) { M.clip += (gi-25)/10; gi = 25; } g += gi; }
    M.gen[r.m] += g/10; M.self[r.m] += Math.min(g, L)/10; }
  M.gen = M.gen.map(Math.round); M.self = M.self.map(Math.round); M.clip = Math.round(M.clip); return M; }
const out = {};
// Cadenas de 17 módulos de 0.45 kW: 5 cadenas = 38.25 kWp y 4 cadenas = 30.6 kWp por inversor de 25 kW.
const A = 38.25, B = 30.6;
const alts = { N10: [A,A], N14: [A,A,B], N18: [A,A,B,B], N20: [A,A,A,A], N22: [A,A,B,B,B] };
for (const n in alts) out[n+'_0.75'] = sim(alts[n], 0.75);
for (const k of [0.5, 0.65, 0.85]) out['N22_'+k] = sim(alts.N22, k);
// Pérdida térmica de referencia ponderada con la irradiancia (≈ 4.3 %) y horas con Vmp(17 módulos) < 480 V (0):
let num = 0, den = 0, low = 0;
for (const r of H) if (r.G > 0) { const Tc = r.T + 27/800*r.G; num += r.G*0.0026*(Tc-25); den += r.G; if (17*33.70*(1-0.0031*(Tc-25)) < 480) low++; }
out.perdida_termica_referencia_horaria = num/den; out.horas_Vmp17_bajo_480 = low/10;
JSON.stringify(out);
