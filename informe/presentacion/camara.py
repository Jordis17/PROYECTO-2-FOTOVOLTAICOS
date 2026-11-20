"""Agrega un cuadro de cámara (cameo de PowerPoint) a cada diapositiva.

Uso: python3 camara.py Sistema_FV_aislado_Abner_Lopez.pptx
El cameo es una imagen con la extensión liveFeedProps, igual a la que escribe
PowerPoint con Insertar > Cameo; al grabar o presentar muestra la cámara.
"""
import re
import sys
import zipfile
from pathlib import Path

EMU = 914400
# Posición (x, y, diámetro) en pulgadas: arriba a la derecha, bajo las pestañas.
POS_CONTENIDO = (11.68, 0.62, 1.17)
POS_PORTADA = (7.25, 0.45, 1.6)  # en el cielo de la ilustración de la portada

SVG = """<svg xmlns="http://www.w3.org/2000/svg" width="256" height="256" viewBox="0 0 256 256">
<rect width="256" height="256" fill="#3E4F63"/>
<circle cx="128" cy="100" r="44" fill="#C9D3DE"/>
<path d="M44 256c6-58 40-92 84-92s78 34 84 92z" fill="#C9D3DE"/>
</svg>"""

PIC = (
    '<p:pic><p:nvPicPr><p:cNvPr id="{id}" name="Cámara"/>'
    '<p:cNvPicPr><a:picLocks noChangeAspect="1"/><a:extLst>'
    '<a:ext uri="{{51228E76-BA90-4043-B771-695A4F85340A}}">'
    '<alf:liveFeedProps xmlns:alf="http://schemas.microsoft.com/office/drawing/2021/livefeed"/>'
    '</a:ext></a:extLst></p:cNvPicPr><p:nvPr/></p:nvPicPr>'
    '<p:blipFill><a:blip><a:extLst><a:ext uri="{{96DAC541-7B7A-43D3-8B79-37D633B846F1}}">'
    '<asvg:svgBlip xmlns:asvg="http://schemas.microsoft.com/office/drawing/2016/SVG/main" r:embed="{rid}"/>'
    '</a:ext></a:extLst></a:blip><a:stretch><a:fillRect/></a:stretch></p:blipFill>'
    '<p:spPr><a:xfrm><a:off x="{x}" y="{y}"/><a:ext cx="{d}" cy="{d}"/></a:xfrm>'
    '<a:prstGeom prst="ellipse"><a:avLst/></a:prstGeom>'
    '<a:ln w="19050"><a:solidFill><a:srgbClr val="C8821A"/></a:solidFill></a:ln></p:spPr></p:pic>'
)


def main(ruta):
    ruta = Path(ruta)
    zin = zipfile.ZipFile(ruta)
    archivos = {n: zin.read(n) for n in zin.namelist()}
    zin.close()

    archivos["ppt/media/camara.svg"] = SVG.encode()
    ct = archivos["[Content_Types].xml"].decode()
    if 'Extension="svg"' not in ct:
        ct = ct.replace("<Default ", '<Default Extension="svg" ContentType="image/svg+xml"/><Default ', 1)
    archivos["[Content_Types].xml"] = ct.encode()

    slides = sorted((n for n in archivos if re.fullmatch(r"ppt/slides/slide\d+\.xml", n)),
                    key=lambda n: int(re.search(r"\d+", n).group()))
    for n in slides:
        num = int(re.search(r"\d+", n).group())
        xml = archivos[n].decode()
        if "liveFeedProps" in xml:
            continue
        rels_n = n.replace("slides/", "slides/_rels/") + ".rels"
        rels = archivos[rels_n].decode()
        ids = [int(i) for i in re.findall(r'Id="rId(\d+)"', rels)]
        rid = f"rId{max(ids) + 1}"
        rels = rels.replace("</Relationships>",
                            f'<Relationship Id="{rid}" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/image" Target="../media/camara.svg"/></Relationships>')
        archivos[rels_n] = rels.encode()
        sid = max(int(i) for i in re.findall(r'<p:cNvPr id="(\d+)"', xml)) + 1
        x, y, d = POS_PORTADA if num == 1 else POS_CONTENIDO
        pic = PIC.format(id=sid, rid=rid, x=round(x * EMU), y=round(y * EMU), d=round(d * EMU))
        archivos[n] = xml.replace("</p:spTree>", pic + "</p:spTree>", 1).encode()

    with zipfile.ZipFile(ruta, "w", zipfile.ZIP_DEFLATED) as zout:
        # [Content_Types].xml primero, como lo espera el formato
        zout.writestr("[Content_Types].xml", archivos.pop("[Content_Types].xml"))
        for n, b in archivos.items():
            zout.writestr(n, b)
    print(f"cámara agregada en {len(slides)} diapositivas")


if __name__ == "__main__":
    main(sys.argv[1])
