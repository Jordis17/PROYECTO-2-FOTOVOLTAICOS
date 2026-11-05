# Material para el Proyecto 2 – Sistema aislado (EL-5854)

## Qué hay en cada carpeta

| Carpeta | Contenido |
|---|---|
| 01_Instrucciones | **Instructivo del Proyecto 2 (sistema aislado)**, transcrito del Loop "Cronograma de clase", y el instructivo del Proyecto 1 como referencia. |
| 02_Presentaciones_curso | Todas las presentaciones del curso: introducción, recurso solar (1–4), tecnología FV (1–4), conectado a red (1–4), normativa nacional y **sistemas aislados (1–4)**. |
| 03_Transcripciones_y_clase_asincrona | Transcripciones de las clases y la clase asincrónica de PVLib (video transcrito, asignación y script). |
| 04_Plantillas_y_herramientas | Plantilla IEEE en LaTeX y la hoja de escenarios del profesor (2026Oct9_EscenariosAFSFV.xlsx). |
| 05_Referencia_Proyecto1 | Lo que se entregó en el Proyecto 1: informe final en LaTeX y PDF (versión revisada del 30 oct., con CAMBIOS.md), la presentación de la defensa (nota 95), el guion y los scripts de cálculo en Python. |

## Tareas del Proyecto 2 según las presentaciones

**Aislado 1 (14 oct.), diapositiva "Trabajo en grupos":**
- Seleccionar un **nuevo sitio** para el proyecto aislado y obtener la caracterización del consumo.
- Revisar o realizar el cálculo de la cantidad de paneles para el sistema aislado.
- Seleccionar el inversor aislado necesario.
- Determinar la capacidad necesaria de las baterías (**suponer 24 V y 70 % de DOD**).

**Aislado 4 (30 oct.), diapositiva "Trabajo en grupos":**
- Terminar de definir la tecnología y el fabricante de las baterías.
- Seleccionar un regulador de carga compatible con el acondicionamiento de potencia elegido.
- (Re)definir la forma del arreglo de baterías.

El instructivo completo está en `01_Instrucciones/Instrucciones_proyecto2_sistema_aislado.txt`. La presentación es de **7 minutos** (en el Proyecto 1 eran 10). El Loop no indica la fecha de entrega.

## Lo que se puede reutilizar del Proyecto 1
- Estructura del informe y plantilla LaTeX (`Informe_final_LaTeX/ACTUALIZADO.tex` y `secciones/`).
- Métodos de recurso solar, inclinación con factores K, corrección por temperatura del módulo y cableado (secciones 3, 4 y 6 del informe y los scripts).
- Comentario del profesor en la defensa: el diagrama unifilar debe usar **simbología estándar** (IEC), no bloques. El unifilar corregido está en `figuras/unifilar_tikz.tex`.
