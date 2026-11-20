// Presentación de 7 minutos del Proyecto 2. Uso: node generar.js  ->  Sistema_FV_aislado_Abner_Lopez.pptx
const path = require("path");
const fs = require("fs");
const pptxgen = require("pptxgenjs");
const { applyTheme } = require(process.env.PPTX_SKILL + "/scripts/apply_theme.js");

const RAIZ = path.resolve(__dirname, "..");
const FIG = (n) => path.join(RAIZ, "figuras", n);
const R = JSON.parse(fs.readFileSync(path.join(RAIZ, "calculos", "resultados.json"), "utf8"));
const OUT = path.join(__dirname, "Sistema_FV_aislado_Abner_Lopez.pptx");

const THEME = {
  name: "Sistema FV aislado", headFontFace: "Calibri", bodyFontFace: "Calibri",
  colors: { dk1: "0F2A44", lt1: "FFFFFF", dk2: "3E4F63", lt2: "F6F3EA", accent1: "C8821A", accent2: "2A78D6",
            accent3: "EB6834", accent4: "1BAF7A", accent5: "9A9890", accent6: "5E6A78", hlink: "2A78D6", folHlink: "6250D6" },
};
const NAVY = "0F2A44", GOLD = "C8821A", INK2 = "3E4F63", MUTED = "5E6A78", CREAM = "F6F3EA", CARD = "FFFFFF", LINE = "D5DAE0";
const BLUE = "2A78D6", ORANGE = "EB6834", GREY = "9A9890";

const pres = new pptxgen();
pres.layout = "LAYOUT_WIDE"; // 13.33 x 7.5
pres.theme = { headFontFace: THEME.headFontFace, bodyFontFace: THEME.bodyFontFace };
pres.title = "Sistema FV aislado de respaldo, casa de Abner López";
pres.author = "Abner López, Sebastián Rojas, Jordi Segura";
const C = pres.SchemeColor;

const SECC = ["Sitio", "Recurso", "Diseño", "Energía", "Instalación", "Economía", "Cierre"];
const N_TOT = 12;
let num = 0;

pres.defineSlideMaster({
  title: "CONTENIDO",
  background: { color: CREAM },
  objects: [
    { text: { text: "Casa de Abner López · Sistema FV aislado de 1.8 kWp", options: { x: 0.5, y: 0.22, w: 6, h: 0.3, fontSize: 11, bold: true, color: NAVY, margin: 0 } } },
    { placeholder: { options: { name: "kicker", type: "body", x: 0.5, y: 0.78, w: 9, h: 0.3, fontSize: 12, bold: true, color: GOLD, margin: 0, charSpacing: 1 }, text: "" } },
    { placeholder: { options: { name: "title", type: "title", x: 0.5, y: 1.05, w: 12.3, h: 0.65, fontSize: 30, bold: true, color: NAVY, margin: 0, valign: "top", align: "left" }, text: "" } },
    { line: { x: 0.5, y: 6.95, w: 12.33, h: 0, line: { color: LINE, width: 0.75 } } },
  ],
  slideNumber: { x: 12.0, y: 7.0, w: 0.83, h: 0.3, fontSize: 10, color: MUTED, align: "right" },
});

function nav(s, act, oscuro) {
  let x = 6.75;
  SECC.forEach((t) => {
    const w = 0.085 * t.length + 0.3;
    s.addText(t, { x, y: 0.2, w, h: 0.32, fontSize: 10, isTextBox: true, align: "center", margin: 0,
      color: t === act ? (oscuro ? "FFFFFF" : NAVY) : (oscuro ? "9FB0C2" : MUTED), bold: t === act, objectName: "nav " + t });
    if (t === act) s.addShape(pres.shapes.LINE, { x: x + 0.1, y: 0.53, w: w - 0.2, h: 0, line: { color: GOLD, width: 1.5 }, objectName: "nav activo" });
    x += w + 0.05;
  });
}
function nueva(sec, kicker, titulo, fuente) {
  num += 1;
  pres.addSection && null;
  const s = pres.addSlide({ masterName: "CONTENIDO" });
  nav(s, sec);
  s.addText(kicker, { placeholder: "kicker" });
  s.addText(titulo, { placeholder: "title" });
  if (fuente) s.addText(fuente, { x: 0.5, y: 7.0, w: 11.2, h: 0.3, fontSize: 10, color: MUTED, isTextBox: true, margin: 0, objectName: "fuente" });
  return s;
}
function tarjeta(s, x, y, w, h, fill) {
  s.addShape(pres.shapes.RECTANGLE, { x, y, w, h, fill: { color: fill || CARD }, line: { color: LINE, width: 0.75 },
    shadow: { type: "outer", color: "000000", opacity: 0.08, blur: 3, offset: 1, angle: 90 }, objectName: "tarjeta" });
}
function dato(s, x, y, w, valor, etiqueta, opts = {}) {
  s.addText(valor, { x, y, w, h: 0.55, fontSize: opts.big || 26, bold: true, color: opts.color || NAVY, margin: 0, isTextBox: true, valign: "bottom" });
  s.addText(etiqueta, { x, y: y + 0.58, w, h: opts.hl || 0.55, fontSize: 12, color: INK2, margin: 0, isTextBox: true, valign: "top" });
}
const fmt = (v, d = 0) => v.toLocaleString("es-CR", { minimumFractionDigits: d, maximumFractionDigits: d }).replace(/ /g, " ");
const M = ["Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Set", "Oct", "Nov", "Dic"];
const ejes = (extra) => Object.assign({
  catAxisLabelColor: MUTED, valAxisLabelColor: MUTED, catAxisLabelFontSize: 11, valAxisLabelFontSize: 11,
  catAxisLabelFontFace: "+mn-lt", valAxisLabelFontFace: "+mn-lt", legendFontFace: "+mn-lt", titleFontFace: "+mn-lt",
  valGridLine: { color: "E3E1DA", size: 0.5 }, catGridLine: { style: "none" }, legendFontSize: 11, legendColor: INK2,
  valAxisTitleColor: MUTED, valAxisTitleFontSize: 11, valAxisTitleFontFace: "+mn-lt",
}, extra);

const c = R.consumo, b = R.balance, m = R.modulo, rg = R.regulador, iv = R.inversor, e = R.energia, co = R.costos, f = R.finanzas;
const pv = R.recurso.pv;

// ------------------------------------------------------------------ 1. Portada
{
  num += 1;
  const s = pres.addSlide();
  s.background = { color: NAVY };
  s.addImage({ path: FIG("ubicacion_satelital.jpg"), x: 6.9, y: 0, w: 6.43, h: 7.5, sizing: { type: "cover", w: 6.43, h: 7.5 }, altText: "Vista satelital de la casa en Santa Rosa de Oreamuno, con el techo marcado", objectName: "imagen portada" });
  s.addText("EL-5854 SISTEMAS FOTOVOLTAICOS · TEC", { x: 0.6, y: 1.2, w: 6, h: 0.35, fontSize: 13, bold: true, color: GOLD, charSpacing: 1, isTextBox: true, margin: 0 });
  s.addText("Sistema fotovoltaico aislado de respaldo para cargas críticas", { x: 0.6, y: 1.7, w: 6.0, h: 1.9, fontSize: 36, bold: true, color: "FFFFFF", isTextBox: true, margin: 0, valign: "top" });
  s.addText("Casa de Abner López · Santa Rosa, Oreamuno, Cartago", { x: 0.6, y: 3.75, w: 6, h: 0.4, fontSize: 16, color: "CDD3DA", isTextBox: true, margin: 0 });
  s.addText("Abner López · Sebastián Rojas · Jordi Segura", { x: 0.6, y: 5.6, w: 6, h: 0.35, fontSize: 15, bold: true, color: "FFFFFF", isTextBox: true, margin: 0 });
  s.addText("Escuela de Ingeniería Electrónica · II Semestre 2026", { x: 0.6, y: 6.0, w: 6, h: 0.35, fontSize: 13, color: "CDD3DA", isTextBox: true, margin: 0 });
  s.addNotes("[0:00 – 0:20 · A. López] Buenas tardes. Presentamos el diseño de un sistema fotovoltaico aislado que respalda las cargas críticas de la casa de Abner López, en Santa Rosa de Oreamuno. La casa tiene servicio de JASEC; el sistema mantiene refrigeración, iluminación y comunicaciones durante dos días sin red ni sol, y el resto del tiempo esas cargas se alimentan con energía solar.");
}

// ------------------------------------------------------------------ 2. Sitio y consumo
{
  const s = nueva("Sitio", "01 · LUGAR Y CONSUMO", "Cargas críticas de la casa",
    "Placas de los equipos y lista del grupo (nov. 2026) · 9.9358° N, 83.8273° O; elevación de 2317 m según PVGIS · Imagen: Google Earth");
  s.addImage({ path: FIG("techo_medicion.jpg"), x: 0.5, y: 1.95, w: 4.2, h: 2.62, altText: "Medición del techo en Google Earth: 85 m² y 2313 a 2315 m de elevación", objectName: "techo" });
  s.addText("Techo de zinc ondulado a dos aguas, 12° hacia el este y el oeste, unos 85 m²", { x: 0.5, y: 4.62, w: 4.2, h: 0.5, fontSize: 12, color: INK2, isTextBox: true, margin: 0 });
  const cs = c.cargas.slice().sort((a, x) => x.E - a.E);
  const lab = cs.map((x) => x.eq.replace(/ \(grupo \d\)/, "").replace("Bombillos LED 15 W", `${x.N} bombillos LED`).replace("Bombillo LED 15 W", "1 bombillo LED")
    .replace(" Atlas AC12SSAAWA", "").replace(" Daytron MCHF90", "").replace(" Nexxt Nebula N300", ""));
  s.addChart(pres.charts.BAR, [{ name: "Energía", labels: lab, values: cs.map((x) => Math.round(x.E)) }], ejes({
    x: 4.95, y: 1.85, w: 4.6, h: 4.95, barDir: "bar", chartColors: [BLUE], showValue: true, dataLabelPosition: "outEnd",
    dataLabelColor: INK2, dataLabelFontSize: 11, dataLabelFontFace: "+mn-lt", showLegend: false, catAxisOrientation: "maxMin",
    valAxisHidden: true, valGridLine: { style: "none" }, barGapWidthPct: 45,
    showTitle: true, title: "Energía diaria de las cargas críticas [Wh/día]", titleFontSize: 12, titleColor: INK2,
    objectName: "grafico consumo por equipo",
  }));
  tarjeta(s, 9.85, 1.95, 3.0, 4.85);
  dato(s, 10.1, 2.05, 2.6, "4.33 kWh/día", "consumo de las cargas críticas (todas en CA, 120 V)");
  dato(s, 10.1, 3.25, 2.6, "783 W", "potencia con todo encendido a la vez");
  dato(s, 10.1, 4.45, 2.6, "3230 kWh", "consumo de la casa en 2026; 1 factura real y 11 estimadas", { hl: 0.8 });
  s.addNotes("[0:20 – 1:00 · A. López] La casa está a 2317 m de altura. El techo es de zinc ondulado a dos aguas, con 12° hacia el este y el oeste. Con el grupo definimos las cargas críticas: refrigerador, congelador, ocho bombillos LED, cargadores de celular y laptop, y el módem. Con los datos de placa suman 4.33 kWh al día; el refrigerador y el congelador son el 71 %. Si todo se enciende a la vez se piden 783 W. Para la factura teníamos una sola, la de octubre, y estimamos los otros meses con la tarifa residencial de JASEC: 3230 kWh al año.");
}

// ------------------------------------------------------------------ 3. Recurso solar
{
  const s = nueva("Recurso", "02 · RECURSO SOLAR", "Radiación sobre el techo y peor mes",
    "PVGIS 5.3 (ERA5, 2005–2023) · Diagrama cilíndrico con las ecuaciones del curso, tiempo solar");
  s.addImage({ path: FIG("diagrama_cilindrico.png"), x: 0.5, y: 1.9, w: 6.2, h: 2.92, altText: "Diagrama cilíndrico del recorrido solar del sitio para el día 21 de cada mes", objectName: "cilindrico" });
  s.addText("El Sol pasa al norte del cenit de abril a agosto; al mediodía del 21 de diciembre la altura es de 56.6°.", { x: 0.5, y: 4.9, w: 6.2, h: 0.55, fontSize: 12, color: INK2, isTextBox: true, margin: 0 });
  const ser = [["horizontal", "Horizontal", GREY], ["oeste", "12° oeste", ORANGE], ["este", "12° este (diseño)", BLUE]];
  s.addChart(pres.charts.LINE, ser.map(([k, n]) => ({ name: n, labels: M, values: pv[k].HSP.map((v) => +v.toFixed(2)) })), ejes({
    x: 6.95, y: 1.85, w: 5.9, h: 3.65, chartColors: ser.map((x) => x[2]), lineSize: 2, lineDataSymbol: "circle", lineDataSymbolSize: 6,
    valAxisMinVal: 3, valAxisMaxVal: 6.5, valAxisMajorUnit: 0.5, showLegend: true, legendPos: "t",
    showValAxisTitle: true, valAxisTitle: "HSP [kWh/(m²·día)]", objectName: "grafico radiacion",
  }));
  tarjeta(s, 0.5, 5.6, 12.35, 1.15);
  dato(s, 0.8, 5.65, 3.6, "3.73 HSP", "noviembre a 12° al este: mes de diseño", { big: 24 });
  dato(s, 4.9, 5.65, 3.6, "1721 kWh/m²", "al año en el plano de los módulos", { big: 24 });
  dato(s, 9.0, 5.65, 3.6, "14°, acimut −40°", "ángulo óptimo de PVGIS: solo 1.7 % más", { big: 24 });
  s.addNotes("[1:00 – 1:40 · A. López] Calculamos el recorrido del Sol para la latitud de 9.9°: pasa muy alto todo el año y de abril a agosto va por el norte. Para la radiación usamos PVGIS con las inclinaciones reales del techo. La cara este recibe 1721 kWh por metro cuadrado al año, 6 % más que la oeste, por eso los módulos van al este. El óptimo de PVGIS, 14° con acimut −40°, daría solo 1.7 % más y obligaría a una estructura inclinada, así que los módulos van paralelos al techo. El peor mes es noviembre, con 3.73 horas solares pico, y con ese valor se dimensiona.");
}

// ------------------------------------------------------------------ 4. Balance y baterías (oscura)
{
  num += 1;
  const s = pres.addSlide({ masterName: "CONTENIDO" });
  s.background = { color: NAVY };
  nav(s, "Diseño", true);
  s.addText("03 · BALANCE Y BATERÍAS", { placeholder: "kicker" });
  s.addText([{ text: "Banco para 2 días de autonomía", options: { color: "FFFFFF" } }], { placeholder: "title" });
  s.addText([
    { text: "E_T = E_CA / K_TCA = 4334 / 0.749 = 5786 Wh/día", options: { breakLine: true } },
    { text: "Q = 1.1 · E_T · D / (V · DOD) = 1.1 · 5786 · 2 / (24 · 0.7) = 758 Ah" },
  ], { x: 0.5, y: 2.0, w: 8.3, h: 0.95, fontSize: 16, color: "FFFFFF", isTextBox: true, margin: 0, paraSpaceAfter: 6 });
  s.addText("Pérdidas de clase: cables 2 %, dispersión 4 %, suciedad 5 %, MPPT 2 %, regulador 5 %, batería 1 %, inversor 5 % y autodescarga de 0.5 % diaria.", { x: 0.5, y: 3.25, w: 8.3, h: 0.7, fontSize: 13, color: "CDD3DA", isTextBox: true, margin: 0 });
  s.addText("Batería seleccionada en el examen 4: Power Queen 24 V 200 Ah (LiFePO₄). El fabricante admite hasta 4 en paralelo; ¢850 000 cada una en Kuat (nov. 2026).", { x: 0.5, y: 4.0, w: 8.3, h: 0.7, fontSize: 13, color: "CDD3DA", isTextBox: true, margin: 0 });
  const st = [["4 × 200 Ah", "en paralelo: 800 Ah ≥ 758 Ah"], ["20.48 kWh", "energía nominal del banco"], ["2.3 días", "de autonomía real al 70 % de descarga"], ["22 %", "de descarga en un día normal"]];
  st.forEach(([v, t], i) => {
    const x = 0.5 + i * 3.1;
    s.addShape(pres.shapes.RECTANGLE, { x, y: 5.15, w: 2.9, h: 1.5, fill: { color: "18395A" }, line: { color: "2C4D70", width: 0.75 }, objectName: "tarjeta oscura" });
    s.addText(v, { x: x + 0.2, y: 5.25, w: 2.6, h: 0.6, fontSize: 28, bold: true, color: GOLD, isTextBox: true, margin: 0 });
    s.addText(t, { x: x + 0.2, y: 5.9, w: 2.6, h: 0.65, fontSize: 12, color: "FFFFFF", isTextBox: true, margin: 0 });
  });
  s.addText("Ubicación: cuarto techado y ventilado junto al tablero principal, sin sol directo; la batería se carga de 0 a 50 °C y en el sitio la temperatura va de 7 a 29.5 °C.", { x: 9.1, y: 2.0, w: 3.75, h: 2.6, fontSize: 13, color: "CDD3DA", isTextBox: true, margin: 0, valign: "top" });
  s.addNotes("[1:40 – 2:20 · A. López] Con el método del curso, las cargas en alterna se dividen entre el factor de rendimiento, que con las pérdidas típicas da 0.749: la energía de diseño es 5786 Wh por día. Con 24 V, 70 % de descarga y dos días de autonomía, la capacidad es 758 Ah. Con la batería que elegimos en el examen 4, la Power Queen de 24 V y 200 Ah, se necesitan cuatro en paralelo, que es el máximo que permite el fabricante: 800 Ah y 20.5 kWh. En un día normal el banco se descarga cerca de 22 %, así que los ciclos no limitan su vida.");
}

// ------------------------------------------------------------------ 5. Módulo y arreglo
{
  const s = nueva("Diseño", "04 · MÓDULOS Y ARREGLO", "Cuatro módulos AIKO de 450 W en 2S2P",
    "Ficha AIKO-A450-MAH54Mb · NOCT estimado de 47 °C con los datos NOCT de la ficha · T ambiente de 7 a 29.5 °C (dato del grupo)");
  tarjeta(s, 0.5, 1.95, 4.0, 4.8);
  s.addText("P_campo = 5786 / 3.73 = 1551 W", { x: 0.75, y: 2.1, w: 3.6, h: 0.4, fontSize: 14, bold: true, color: NAVY, isTextBox: true, margin: 0 });
  s.addText("N = 1.1 · 1551 / 450 = 3.79 → 4 módulos", { x: 0.75, y: 2.55, w: 3.6, h: 0.4, fontSize: 14, bold: true, color: NAVY, isTextBox: true, margin: 0 });
  dato(s, 0.75, 3.15, 3.5, "1800 Wp", "4 × AIKO Neostar 2S, tipo N, 22.6 % de eficiencia");
  dato(s, 0.75, 4.35, 3.5, "8 m² · 86 kg", "en una fila de 4 en vertical, paralelos al techo, cara este", { hl: 0.8 });
  const hdr = ["T celda", "Voc [V]", "Vmp [V]", "Isc [A]", "P [W]"].map((t) => ({ text: t, options: { bold: true, color: "FFFFFF", fill: { color: NAVY } } }));
  const rows = m.tabla_T.map((t, i) => [["7 °C (mín.)", "25 °C (STC)", "63.2 °C (máx.)"][i], t.Voc.toFixed(2), t.Vmp.toFixed(2), t.Isc.toFixed(2), t.P.toFixed(1)]);
  s.addTable([hdr, ...rows], { x: 4.8, y: 1.95, w: 8.05, colW: [2.05, 1.5, 1.5, 1.5, 1.5], fontSize: 13, color: INK2, border: { type: "solid", color: LINE, pt: 0.75 }, fill: { color: CARD }, rowH: 0.4, align: "center", objectName: "tabla temperatura" });
  const hdr2 = ["Comprobación del arreglo 2S2P", "Arreglo", "Límite del regulador"].map((t) => ({ text: t, options: { bold: true, color: "FFFFFF", fill: { color: NAVY } } }));
  const ca = rg.cadenas;
  const rows2 = [["Voc con 7 °C (2 en serie)", ca.Voc_frio.toFixed(1) + " V", "≤ 145 V"],
    ["Vmp con 63.2 °C", ca.Vmp_cal.toFixed(1) + " V", "≥ 28.8 + 5 = 33.8 V"],
    ["Isc con 63.2 °C (2 en paralelo)", ca.Isc_cal.toFixed(1) + " A", "≤ 70 A"],
    ["Módulos en serie (curso: 145 / 33.7 = 4.3)", "2", "máx. 3 por Voc en frío"]];
  s.addTable([hdr2, ...rows2], { x: 4.8, y: 3.85, w: 8.05, colW: [3.85, 1.6, 2.6], fontSize: 13, color: INK2, border: { type: "solid", color: LINE, pt: 0.75 }, fill: { color: CARD }, rowH: 0.4, objectName: "tabla arreglo" });
  s.addText("Con 4 módulos solo caben 2S2P o 1S4P; con 1S4P la Vmp en calor (29.7 V) queda bajo el arranque del regulador.", { x: 4.8, y: 6.0, w: 8.05, h: 0.6, fontSize: 12, color: INK2, isTextBox: true, margin: 0 });
  s.addNotes("[2:20 – 3:05 · S. Rojas] Con el peor mes, 3.73 HSP, el campo debe ser de 1551 W; con el 10 % de margen del curso salen 3.79 módulos, es decir, cuatro AIKO de 450 W, el mismo módulo del proyecto 1: 1800 Wp. Corregimos sus parámetros entre 7 °C, la mínima del último año, y 63 °C en la celda con la máxima de 29.5 °C. En frío la tensión de circuito abierto sube a 42.3 V; en calor la potencia baja a 405 W. Con cuatro módulos el arreglo queda en dos cadenas de dos: 84.6 V en frío, debajo de los 145 V del regulador, y 59.4 V en calor, encima del mínimo de arranque.");
}

// ------------------------------------------------------------------ 6. Regulador
{
  const s = nueva("Diseño", "05 · REGULADOR DE CARGA", "Regulador MPPT de 85 A",
    "Especificaciones oficiales Victron SmartSolar MPPT 150/70 a 150/100 VE.Can · Curvas I-V del arreglo con los parámetros corregidos");
  s.addImage({ path: FIG("soa_regulador.png"), x: 0.5, y: 1.85, w: 6.1, h: 4.78, altText: "Zona de operación del regulador con las curvas I-V del arreglo 2S2P a 7, 25 y 63 °C", objectName: "SOA" });
  tarjeta(s, 6.9, 1.95, 5.95, 4.75);
  s.addText("i_reg = P_FV / V_bat = 1800 / 24 = 75 A", { x: 7.15, y: 2.1, w: 5.5, h: 0.45, fontSize: 18, bold: true, color: NAVY, isTextBox: true, margin: 0 });
  s.addText("Victron SmartSolar MPPT 150/85-Tr VE.Can", { x: 7.15, y: 2.6, w: 5.5, h: 0.4, fontSize: 15, bold: true, color: GOLD, isTextBox: true, margin: 0 });
  s.addText([
    { text: "85 A de salida ≥ 75 A; el de 70 A no cumple el criterio del curso", options: { bullet: true, breakLine: true } },
    { text: "2400 W nominales a 24 V para 1800 Wp", options: { bullet: true, breakLine: true } },
    { text: "Voc máx. 150 V; arranca con Vpv > Vbat + 5 V", options: { bullet: true, breakLine: true } },
    { text: "Isc máx. 70 A; el arreglo da 28.8 A", options: { bullet: true, breakLine: true } },
    { text: "Eficiencia 98 %, perfil de carga para litio, 28.8 V absorción", options: { bullet: true, breakLine: true } },
    { text: "Potencia plena hasta 2000 m; el sitio está a 2317 m, pero solo usa el 75 % de su potencia", options: { bullet: true } },
  ], { x: 7.15, y: 3.1, w: 5.5, h: 3.4, fontSize: 14, color: INK2, isTextBox: true, margin: 0, paraSpaceAfter: 6, valign: "top" });
  s.addNotes("[3:05 – 3:45 · S. Rojas] El regulador se dimensiona con la potencia del arreglo entre la tensión del banco: 75 A. Por eso no sirve el modelo de 70 A y elegimos el SmartSolar 150/85 de Victron. En el gráfico, la zona sombreada es donde el regulador puede trabajar, y los puntos de máxima potencia del arreglo, a 7, 25 y 63 °C, quedan adentro, con la tensión entre 59 y 71 V y la corriente cerca de 28 A, lejos de los 70 A permitidos. La ficha garantiza la potencia plena hasta 2000 m y el sitio está a 2317 m; como el regulador trabaja al 75 % de su potencia nominal, tiene margen.");
}

// ------------------------------------------------------------------ 7. Inversor-cargador
{
  const s = nueva("Diseño", "06 · INVERSOR-CARGADOR", "Inversor-cargador con transferencia automática",
    "Ficha Victron MultiPlus-II 120 V · Arranque de compresores supuesto en 4 veces su potencia nominal (cota alta de 3 a 4 veces vista en clase)");
  const hdr = ["Parámetro", "Cargas críticas", "MultiPlus-II 24/3000/70-50"].map((t) => ({ text: t, options: { bold: true, color: "FFFFFF", fill: { color: NAVY } } }));
  const rows = [["Potencia continua", "783 W", "2400 W a 25 °C · 2200 W a 40 °C"], ["Pico (arranque de compresores)", "1763 W", "5500 W"],
    ["Tensión DC", "24 V (banco)", "19 a 33 V"], ["Salida AC", "120 V, 60 Hz", "120 V ± 2 %, 60 Hz, onda senoidal"],
    ["Corriente de batería", "34 A (77 A en el pico)", "hasta 114 A a plena potencia"], ["Transferencia", "con red de JASEC", "50 A, menos de 20 ms"],
    ["Cargador desde la red", "", "70 A"], ["Eficiencia máxima", "", "94 %"]];
  s.addTable([hdr, ...rows.map((r) => r.map((t, j) => ({ text: t, options: { bold: j === 0 } })))], { x: 0.5, y: 1.95, w: 7.6, colW: [2.6, 2.1, 2.9], fontSize: 13, color: INK2, border: { type: "solid", color: LINE, pt: 0.75 }, fill: { color: CARD }, rowH: 0.42, objectName: "tabla inversor" });
  tarjeta(s, 8.4, 1.95, 4.45, 4.75);
  dato(s, 8.7, 2.1, 3.9, "33 %", "de la potencia continua con todo encendido");
  dato(s, 8.7, 3.3, 3.9, "32 %", "del pico admisible al arrancar refrigerador y congelador juntos", { hl: 0.8 });
  s.addText("Es el modelo de menor potencia de la serie MultiPlus-II de 24 V y 120 V. Si falla la red, pasa las cargas al inversor en menos de 20 ms; cuando vuelve, puede recargar el banco.", { x: 8.7, y: 4.75, w: 3.9, h: 1.8, fontSize: 13, color: INK2, isTextBox: true, margin: 0, valign: "top" });
  s.addNotes("[3:45 – 4:25 · S. Rojas] El inversor se elige por la potencia de las cargas que trabajan a la vez, no por la del arreglo. Con todo encendido son 783 W, y si el refrigerador y el congelador arrancan juntos, suponiendo cuatro veces su potencia, el pico es de 1763 W. Escogimos el MultiPlus-II de 24 V y 3000 VA, el más pequeño de la serie a 120 V: trabaja al 33 % de su potencia continua y al 32 % de su pico. Además trae el conmutador de transferencia: con red, las cargas siguen conectadas, y si la red falla pasan al inversor en menos de 20 ms. También tiene corte por baja tensión del banco, como pide el curso.");
}

// ------------------------------------------------------------------ 8. Estimación energética
{
  const s = nueva("Energía", "07 · ESTIMACIÓN ENERGÉTICA", "Energía disponible contra demanda",
    "Energía disponible = 1.8 kW · HSP (12° este, PVGIS) · K_TCA (0.749) · días del mes");
  s.addChart(pres.charts.BAR, [
    { name: "Disponible para las cargas", labels: M, values: e.mensual.map((x) => +x.E_util.toFixed(1)) },
    { name: "Demanda de las cargas críticas", labels: M, values: e.mensual.map((x) => +x.E_dem.toFixed(1)) },
  ], ejes({ x: 0.5, y: 1.85, w: 8.0, h: 4.95, barDir: "col", chartColors: [BLUE, GREY], barGapWidthPct: 60, showLegend: true, legendPos: "t",
    showValAxisTitle: true, valAxisTitle: "kWh/mes", valAxisMaxVal: 300, objectName: "grafico energia" }));
  tarjeta(s, 8.8, 1.95, 4.05, 4.75);
  dato(s, 9.1, 2.1, 3.5, "2320 kWh", "al año disponibles para las cargas");
  dato(s, 9.1, 3.3, 3.5, "1582 kWh", "al año que piden las cargas críticas");
  dato(s, 9.1, 4.5, 3.5, "116 %", "de cobertura en noviembre, el peor mes; el excedente se pierde", { hl: 0.8 });
  s.addNotes("[4:25 – 5:00 · J. Segura] Mes a mes multiplicamos la potencia del arreglo, las horas solares pico de la cara este, el factor de rendimiento y los días. Todos los meses la energía disponible supera la demanda: en noviembre, el peor, se cubre el 116 %, y en marzo casi el doble. En el año hay 2320 kWh disponibles y las cargas piden 1582. Lo que sobra no se puede usar porque el sistema no inyecta a la red; ese margen es el que permite recargar el banco después de días nublados.");
}

// ------------------------------------------------------------------ 9. Instalación
{
  const s = nueva("Instalación", "08 · ELEMENTOS DE INSTALACIÓN", "Montaje, cableado y protecciones",
    "Conductores según NEC 2014: i_w = 1.25 · 1.25 · Isc en el lado FV y 1.25 · I_máx en baterías y CA · Distancias supuestas: 10 m techo–equipos, 2 m banco–inversor, 5 m al tablero");
  const cols = [
    ["Estructura", ["2 rieles Unirac SM cortados a 4.7 m", "10 soportes L-Foot atornillados a las clavadoras, con sello", "6 grapas intermedias con unión a tierra y 4 de extremo", "Módulos paralelos al techo (12°), cara este"]],
    ["Cableado", ["T1 cadenas: 10 AWG PV Wire, 10 m, caída 1.82 %", "T3 regulador–barra: 2 AWG, 106 A", "T5 barra–inversor: 2/0 AWG, 143 A", "T6 y T7 en CA: 8 AWG THHN, 31 A, caída 0.52 %"]],
    ["Protecciones", ["Sin fusibles de cadena: solo 2 cadenas", "DPS DC MNSPD-115 en la caja combinadora", "Protector de falla a tierra GFP de 80 A en la entrada FV", "Interruptores DC: 125 A regulador, 100 A por batería, 175 A inversor; AC: 40 A"]],
  ];
  cols.forEach(([t, items], i) => {
    const x = 0.5 + i * 4.18;
    tarjeta(s, x, 1.95, 3.98, 4.15);
    s.addText(t, { x: x + 0.25, y: 2.08, w: 3.5, h: 0.4, fontSize: 18, bold: true, color: NAVY, isTextBox: true, margin: 0 });
    s.addText(items.map((it, k) => ({ text: it, options: { bullet: true, breakLine: k < items.length - 1 } })),
      { x: x + 0.25, y: 2.6, w: 3.55, h: 3.35, fontSize: 14, color: INK2, isTextBox: true, margin: 0, paraSpaceAfter: 8, valign: "top" });
  });
  s.addShape(pres.shapes.RECTANGLE, { x: 0.5, y: 6.25, w: 12.35, h: 0.55, fill: { color: "FBEFD9" }, line: { color: "E9C88E", width: 0.75 }, objectName: "aviso" });
  s.addText("Por verificar en sitio: las distancias reales, la separación de las clavadoras para los soportes y la capacidad del tablero principal.", { x: 0.7, y: 6.27, w: 12.0, h: 0.5, fontSize: 13, color: "8F5609", isTextBox: true, margin: 0, valign: "middle" });
  s.addNotes("[5:00 – 5:35 · J. Segura] Los cuatro módulos van en una fila sobre dos rieles, paralelos al techo, con soportes atornillados a las clavadoras. Los conductores se dimensionaron con el NEC 2014: en el lado fotovoltaico, 1.25 por 1.25 veces la corriente de cortocircuito, y en baterías y alterna 1.25 veces la corriente máxima. El tramo más largo, del techo a los equipos, tiene 1.8 % de caída. Como son solo dos cadenas no hacen falta fusibles por cadena; hay descargador de sobretensión, protector de falla a tierra e interruptores DC en el regulador, en cada batería y en el inversor.");
}

// ------------------------------------------------------------------ 10. Unifilar
{
  const s = nueva("Instalación", "09 · DIAGRAMA UNIFILAR", "Diagrama unifilar (IEC 60617)", "Diagrama completo en el informe");
  s.addImage({ path: path.join(__dirname, "unifilar.png"), x: 0.5, y: 1.8, w: 12.33, h: 5.05, sizing: { type: "contain", w: 12.33, h: 5.05 }, altText: "Diagrama unifilar del sistema aislado con simbología IEC 60617", objectName: "unifilar" });
  s.addNotes("[5:35 – 6:00 · J. Segura] En el unifilar, las dos cadenas llegan a la caja combinadora con su descargador, pasan por el protector de falla a tierra al regulador, y de ahí a la barra de 24 V, donde están las cuatro baterías, cada una con su interruptor. De la barra sale el inversor-cargador. Su entrada AC viene del tablero principal de JASEC y su salida alimenta el subtablero de cargas críticas, donde se reubican los circuitos del refrigerador, el congelador, las luces y los tomas.");
}

// ------------------------------------------------------------------ 11. Costos y proyección financiera
{
  const s = nueva("Economía", "10 · COSTOS Y PROYECCIÓN FINANCIERA", "Costo del sistema y flujo de caja",
    "Precios de nov. 2026 (Kuat, DRSA, PES Supply, Cambio Energético) · ¢447.54/USD (BCCR) · Tasa 7 %, O&M 1 %/año, 25 años · Reemplazos supuestos: equipos año 13, baterías año 15");
  const cc = co.crc;
  const rows = [["Baterías (4 × ¢850 000)", cc["Baterías Power Queen 24 V 200 Ah (4 x ¢850 000)"]],
    ["Inversor-cargador MultiPlus-II", cc["Inversor-cargador Victron MultiPlus-II 24/3000/70-50 120V"]],
    ["Protecciones, tableros y otros", cc["Protecciones y tableros"] + cc["Otros materiales eléctricos (15 %)"]],
    ["Conductores", cc["Conductores"]], ["Módulos (4)", cc["Módulos AIKO 450 W (4 x 128.96 EUR)"]],
    ["Regulador SmartSolar 150/85", cc["Regulador Victron SmartSolar 150/85-Tr VE.Can"]], ["Estructura", cc["Estructura de montaje"]],
    ["Diseño, CFIA e instalación", Object.values(co.serv).reduce((a, x) => a + x, 0)], ["Ganancia del instalador (20 %)", co.ganancia]];
  const hdr = [{ text: "Rubro", options: { bold: true, color: "FFFFFF", fill: { color: NAVY } } }, { text: "Monto [¢]", options: { bold: true, color: "FFFFFF", fill: { color: NAVY }, align: "right" } }];
  const body = rows.map(([a, v]) => [a, { text: fmt(v), options: { align: "right" } }]);
  body.push([{ text: "Precio del sistema", options: { bold: true } }, { text: fmt(co.I0), options: { bold: true, align: "right" } }]);
  s.addTable([hdr, ...body], { x: 0.5, y: 1.9, w: 5.2, colW: [3.5, 1.7], fontSize: 12, color: INK2, border: { type: "solid", color: LINE, pt: 0.75 }, fill: { color: CARD }, rowH: 0.38, objectName: "tabla costos" });
  s.addChart(pres.charts.LINE, [{ name: "Flujo acumulado", labels: f.acum.map((_, k) => String(k)), values: f.acum.map((v) => +(v / 1e6).toFixed(2)) }], ejes({
    x: 5.95, y: 1.85, w: 4.0, h: 4.95, chartColors: [ORANGE], lineSize: 2, lineDataSymbol: "none", showLegend: false,
    showTitle: true, title: "Flujo acumulado [millones de ¢]", titleFontSize: 12, titleColor: INK2, catAxisLabelFrequency: 5,
    valAxisMinVal: -12, valAxisMaxVal: 0, valAxisMajorUnit: 2, catAxisLabelPos: "low", catAxisLabelRotate: 0, objectName: "grafico flujo" }));
  tarjeta(s, 10.2, 1.95, 2.65, 4.85);
  dato(s, 10.4, 2.0, 2.3, "¢7.10 M", "precio del sistema", { big: 24, hl: 0.35 });
  dato(s, 10.4, 2.95, 2.3, "¢128 165", "ahorro del año 1 (54 % de la factura)", { big: 24, hl: 0.6 });
  dato(s, 10.4, 4.1, 2.3, "−¢8.0 M", "VAN; no se recupera en 25 años", { big: 24, hl: 0.6, color: ORANGE });
  dato(s, 10.4, 5.25, 2.3, "¢533/kWh", "costo de la energía respaldada", { big: 24, hl: 0.6 });
  s.addNotes("[6:00 – 6:40 · J. Segura] El sistema cuesta unos 7.1 millones de colones; casi la mitad son las baterías. Las cargas críticas son el 49 % del consumo de la casa, así que la factura baja de 237 000 a 109 000 colones al año: un ahorro de 128 000. Ese ahorro apenas supera el mantenimiento supuesto, y con los reemplazos del inversor y de las baterías la inversión no se recupera en 25 años: el VAN es de −8 millones y la energía respaldada cuesta 533 colones por kWh, frente a unos 90 de la red. Económicamente no se justifica por ahorro; su valor es mantener la comida refrigerada y las comunicaciones cuando falla la red.");
}

// ------------------------------------------------------------------ 12. Cierre
{
  num += 1;
  const s = pres.addSlide({ masterName: "CONTENIDO" });
  s.background = { color: NAVY };
  nav(s, "Cierre", true);
  s.addText("11 · CONCLUSIONES", { placeholder: "kicker" });
  s.addText([{ text: "Respaldo de 2 días para las cargas críticas", options: { color: "FFFFFF" } }], { placeholder: "title" });
  const pts = [
    ["1.8 kWp", "4 módulos AIKO en 2S2P, a 12° en la cara este; cubren la demanda aun en noviembre (116 %)."],
    ["800 Ah", "4 Power Queen de 24 V en paralelo, 20.5 kWh: 2.3 días de autonomía al 70 % de descarga."],
    ["85 A · 3000 VA", "Regulador SmartSolar 150/85 y MultiPlus-II con transferencia en menos de 20 ms."],
    ["¢7.10 M", "No se paga con el ahorro (VAN −¢8.0 M): es una inversión en continuidad del servicio."],
  ];
  pts.forEach(([v, t], i) => {
    const y = 2.0 + i * 1.05;
    s.addText(v, { x: 0.5, y, w: 3.0, h: 0.8, fontSize: 26, bold: true, color: GOLD, isTextBox: true, margin: 0, valign: "middle" });
    s.addText(t, { x: 3.6, y, w: 9.2, h: 0.8, fontSize: 17, color: "FFFFFF", isTextBox: true, margin: 0, valign: "middle" });
  });
  s.addText("Por confirmar antes de construir: cotizaciones locales, distancias y estado de la estructura del techo.", { x: 0.5, y: 6.35, w: 12.3, h: 0.45, fontSize: 14, color: "CDD3DA", isTextBox: true, margin: 0 });
  s.addNotes("[6:40 – 7:00 · J. Segura] En resumen: con 1.8 kWp y un banco de 800 Ah la casa mantiene sus cargas críticas por más de dos días sin red ni sol, y en un día normal esas cargas funcionan con energía solar. Los equipos cumplen los límites de tensión, corriente y potencia revisados. El sistema no se paga con el ahorro en la factura; su justificación es la continuidad del servicio. Muchas gracias; quedamos atentos a sus preguntas.");
}

(async () => {
  await pres.writeFile({ fileName: OUT });
  await applyTheme(OUT, THEME);
  console.log("ok", OUT, num);
})();
