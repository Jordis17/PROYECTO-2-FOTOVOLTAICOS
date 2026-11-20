// Ilustraciones de la presentación (SVG -> PNG). Uso: node ilustraciones.js  ->  img/*.png
const fs = require("fs");
const path = require("path");
const sharp = require("sharp");

const DIR = path.join(__dirname, "img");
fs.mkdirSync(DIR, { recursive: true });

// Casa a dos aguas con 4 módulos en la cara este (derecha). (x, y) = esquina inferior izquierda de la pared.
function casa(x, y, k, noche) {
  const w = 300 * k, h = 150 * k, alero = 25 * k, cum = 120 * k;
  const pared = noche ? "#3B4A5E" : "#F2E6D0", sombra = noche ? "#2E3B4D" : "#E3D3B6";
  const techoO = noche ? "#4A5466" : "#9AA3AE", techoE = noche ? "#5B6677" : "#B7BEC7";
  const vent = noche ? "#FFD27A" : "#7FB2D9";
  const cx = x + w / 2, ty = y - h;
  let s = "";
  s += `<rect x="${x}" y="${ty}" width="${w}" height="${h}" fill="${pared}"/>`;
  s += `<rect x="${cx}" y="${ty}" width="${w / 2}" height="${h}" fill="${sombra}"/>`;
  s += `<polygon points="${x - alero},${ty + 8 * k} ${cx},${ty - cum} ${cx},${ty}" fill="${techoO}"/>`;
  s += `<polygon points="${cx},${ty - cum} ${x + w + alero},${ty + 8 * k} ${cx},${ty}" fill="${techoE}"/>`;
  // módulos sobre la cara este, paralelos al techo
  const p0 = [cx + 18 * k, ty - cum + 22 * k], p1 = [x + w + alero - 22 * k, ty - 4 * k];
  const n = 4;
  for (let i = 0; i < n; i++) {
    const t0 = 0.04 + i * 0.24, t1 = t0 + 0.21;
    const a = [p0[0] + (p1[0] - p0[0]) * t0, p0[1] + (p1[1] - p0[1]) * t0];
    const b = [p0[0] + (p1[0] - p0[0]) * t1, p0[1] + (p1[1] - p0[1]) * t1];
    const d = 26 * k;
    s += `<polygon points="${a[0]},${a[1]} ${b[0]},${b[1]} ${b[0]},${b[1] - d} ${a[0]},${a[1] - d}" fill="#1D3F6E" stroke="#C9D6E6" stroke-width="${1.5 * k}"/>`;
    s += `<line x1="${(a[0] + b[0]) / 2}" y1="${(a[1] + b[1]) / 2}" x2="${(a[0] + b[0]) / 2}" y2="${(a[1] + b[1]) / 2 - d}" stroke="#5F86B8" stroke-width="${1 * k}"/>`;
    s += `<line x1="${a[0]}" y1="${a[1] - d / 2}" x2="${b[0]}" y2="${b[1] - d / 2}" stroke="#5F86B8" stroke-width="${1 * k}"/>`;
  }
  // puerta y ventanas
  s += `<rect x="${x + 40 * k}" y="${y - 85 * k}" width="${42 * k}" height="${85 * k}" fill="${noche ? "#6B4F35" : "#8A6542"}"/>`;
  s += `<rect x="${x + 105 * k}" y="${y - 110 * k}" width="${45 * k}" height="${40 * k}" fill="${vent}"/>`;
  s += `<rect x="${x + 195 * k}" y="${y - 110 * k}" width="${70 * k}" height="${40 * k}" fill="${vent}"/>`;
  s += `<line x1="${x + 230 * k}" y1="${y - 110 * k}" x2="${x + 230 * k}" y2="${y - 70 * k}" stroke="${pared}" stroke-width="${3 * k}"/>`;
  // cuarto de equipos con batería al costado
  const bx = x + w + 10 * k, bw = 70 * k, bh = 80 * k;
  s += `<rect x="${bx}" y="${y - bh}" width="${bw}" height="${bh}" fill="${noche ? "#33414F" : "#D9CCB2"}"/>`;
  s += `<polygon points="${bx - 6 * k},${y - bh} ${bx + bw + 6 * k},${y - bh + 10 * k} ${bx + bw + 6 * k},${y - bh + 2 * k} ${bx - 6 * k},${y - bh - 8 * k}" fill="${techoE}"/>`;
  s += `<rect x="${bx + 18 * k}" y="${y - 55 * k}" width="${34 * k}" height="${45 * k}" rx="${4 * k}" fill="#1BAF7A"/>`;
  s += `<rect x="${bx + 26 * k}" y="${y - 60 * k}" width="${7 * k}" height="${6 * k}" fill="#0F2A44"/><rect x="${bx + 38 * k}" y="${y - 60 * k}" width="${7 * k}" height="${6 * k}" fill="#0F2A44"/>`;
  s += `<path d="M${bx + 37 * k} ${y - 48 * k} l${-8 * k} ${16 * k} h${7 * k} l${-4 * k} ${14 * k} l${12 * k} ${-19 * k} h${-7 * k} z" fill="#FFFFFF"/>`;
  return s;
}

function montanas(W, H, noche) {
  const c1 = noche ? "#1E3A5C" : "#8FA9C4", c2 = noche ? "#17304D" : "#6F8FB0", c3 = noche ? "#12283F" : "#4E7397";
  return `
  <path d="M0 ${H * 0.58} L${W * 0.18} ${H * 0.44} L${W * 0.34} ${H * 0.36} L${W * 0.42} ${H * 0.33} L${W * 0.5} ${H * 0.35} L${W * 0.7} ${H * 0.45} L${W} ${H * 0.5} V${H} H0 Z" fill="${c1}"/>
  <path d="M0 ${H * 0.66} L${W * 0.25} ${H * 0.55} L${W * 0.45} ${H * 0.6} L${W * 0.68} ${H * 0.52} L${W} ${H * 0.6} V${H} H0 Z" fill="${c2}"/>
  <path d="M0 ${H * 0.74} Q${W * 0.3} ${H * 0.66} ${W * 0.55} ${H * 0.71} T${W} ${H * 0.69} V${H} H0 Z" fill="${c3}"/>`;
}

const svgs = {
  // Portada: amanecer sobre las faldas del Irazú
  portada: (() => {
    const W = 1286, H = 1500;
    let s = `<svg xmlns="http://www.w3.org/2000/svg" width="${W}" height="${H}">
    <defs><linearGradient id="cielo" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#2A5C8F"/><stop offset="0.45" stop-color="#7FA8CC"/><stop offset="0.75" stop-color="#F3C98B"/><stop offset="1" stop-color="#F6E3BF"/></linearGradient>
      <radialGradient id="halo"><stop offset="0" stop-color="#FFE7A8" stop-opacity="0.9"/><stop offset="1" stop-color="#FFE7A8" stop-opacity="0"/></radialGradient></defs>
    <rect width="${W}" height="${H}" fill="url(#cielo)"/>
    <circle cx="${W * 0.78}" cy="${H * 0.27}" r="260" fill="url(#halo)"/>
    <circle cx="${W * 0.78}" cy="${H * 0.27}" r="85" fill="#FFD36B"/>`;
    s += montanas(W, H, false);
    s += `<rect x="0" y="${H * 0.82}" width="${W}" height="${H * 0.18}" fill="#5E8C4F"/>
    <path d="M0 ${H * 0.82} Q${W * 0.5} ${H * 0.79} ${W} ${H * 0.82}" fill="#5E8C4F"/>`;
    // ciprés y arbustos
    for (const [x, hh] of [[110, 260], [190, 200], [1150, 230]]) s += `<path d="M${x} ${H * 0.83} q-38 ${-hh * 0.4} 0 ${-hh} q38 ${hh * 0.6} 0 ${hh} z" fill="#2F5A35"/>`;
    s += casa(320, H * 0.83, 1.85, false);
    s += `<rect x="0" y="${H * 0.83}" width="${W}" height="${H * 0.17}" fill="#4F7B43"/></svg>`;
    return [s, W, H];
  })(),

  // Cierre: la casa de noche con las cargas críticas encendidas
  noche: (() => {
    const W = 1000, H = 1100;
    let s = `<svg xmlns="http://www.w3.org/2000/svg" width="${W}" height="${H}">
    <defs><linearGradient id="n" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#0B1E33"/><stop offset="1" stop-color="#1F4268"/></linearGradient>
    <radialGradient id="luz"><stop offset="0" stop-color="#FFD27A" stop-opacity="0.55"/><stop offset="1" stop-color="#FFD27A" stop-opacity="0"/></radialGradient></defs>
    <rect width="${W}" height="${H}" fill="url(#n)"/>`;
    const est = [[80, 90], [210, 160], [330, 60], [470, 140], [560, 50], [690, 190], [120, 260], [400, 250], [880, 300], [620, 300], [260, 360]];
    est.forEach(([x, y], i) => { s += `<circle cx="${x}" cy="${y}" r="${i % 3 ? 2.5 : 4}" fill="#FFFFFF" opacity="0.85"/>`; });
    s += `<circle cx="800" cy="150" r="70" fill="#F4EBD0"/><circle cx="830" cy="130" r="64" fill="#11253D"/>`;
    s += montanas(W, H, true);
    s += `<circle cx="430" cy="790" r="330" fill="url(#luz)"/>`;
    s += casa(210, 930, 1.45, true);
    s += `<rect x="0" y="930" width="${W}" height="170" fill="#16283A"/></svg>`;
    return [s, W, H];
  })(),

  // Banco: 4 baterías de 24 V en paralelo sobre una barra común
  banco: (() => {
    const W = 1100, H = 760;
    let s = `<svg xmlns="http://www.w3.org/2000/svg" width="${W}" height="${H}" font-family="Calibri, Arial, sans-serif">`;
    s += `<rect x="60" y="70" width="980" height="22" rx="6" fill="#D9534F"/><text x="40" y="92" text-anchor="end" font-size="44" fill="#F3B9B6" font-weight="bold">+</text>`;
    s += `<rect x="60" y="680" width="980" height="22" rx="6" fill="#9FB0C2"/><text x="40" y="704" text-anchor="end" font-size="44" fill="#C9D3DE" font-weight="bold">−</text>`;
    for (let i = 0; i < 4; i++) {
      const x = 95 + i * 240;
      s += `<line x1="${x + 55}" y1="92" x2="${x + 55}" y2="215" stroke="#D9534F" stroke-width="10"/>`;
      s += `<line x1="${x + 145}" y1="215" x2="${x + 145}" y2="160" stroke="#9FB0C2" stroke-width="10"/>`;
      s += `<path d="M${x + 145} 160 H${x + 215} V690" stroke="#9FB0C2" stroke-width="10" fill="none"/>`;
      s += `<rect x="${x + 35}" y="205" width="40" height="24" rx="4" fill="#E6EBF0"/><rect x="${x + 125}" y="205" width="40" height="24" rx="4" fill="#E6EBF0"/>`;
      s += `<rect x="${x}" y="225" width="200" height="400" rx="18" fill="#1BAF7A"/>`;
      s += `<rect x="${x}" y="225" width="200" height="70" rx="18" fill="#14936A"/><rect x="${x}" y="265" width="200" height="30" fill="#14936A"/>`;
      s += `<rect x="${x + 30}" y="340" width="140" height="220" rx="10" fill="#0F2A44" opacity="0.25"/>`;
      s += `<path d="M${x + 112} 360 l-34 80 h28 l-14 78 l50 -100 h-30 l16 -58 z" fill="#FFFFFF"/>`;
      s += `<text x="${x + 100}" y="600" text-anchor="middle" font-size="30" font-weight="bold" fill="#FFFFFF">200 Ah</text>`;
    }
    s += `</svg>`;
    return [s, W, H];
  })(),
};

(async () => {
  for (const [n, [svg, W, H]] of Object.entries(svgs)) {
    await sharp(Buffer.from(svg)).resize(W, H).png().toFile(path.join(DIR, n + ".png"));
    console.log("img/" + n + ".png");
  }
})();

// Íconos (react-icons, Font Awesome 6) en dorado, para tarjetas y filas
const React = require("react");
const RDS = require("react-dom/server");
const fa = require("react-icons/fa6");
const ICONOS = ["FaSolarPanel", "FaBolt", "FaCarBattery", "FaTemperatureHalf", "FaMountain", "FaGaugeHigh", "FaShieldHalved", "FaPlug", "FaScrewdriverWrench", "FaSun"];
(async () => {
  for (const n of ICONOS) {
    const svg = RDS.renderToStaticMarkup(React.createElement(fa[n], { color: "#FFFFFF", size: 256 }));
    await sharp(Buffer.from(svg)).resize(256, 256, { fit: "contain", background: { r: 0, g: 0, b: 0, alpha: 0 } }).png().toFile(path.join(DIR, "ico_" + n + ".png"));
  }
  console.log("íconos", ICONOS.length);
})();
