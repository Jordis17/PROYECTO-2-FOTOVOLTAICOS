# CLAUDE.md – Proyecto 2 (Sistema Aislado FV)

En este repositorio se trabaja el **Proyecto 2 (Sistema Aislado FV)** del curso EL-5854 Sistemas Fotovoltaicos del TEC. Somos estudiantes de Ingeniería Electrónica que llevan el curso por primera vez. Todo el material está en este repositorio; el índice está en `00_LEEME.md`.

El informe se escribe en LaTeX. Proponé una carpeta `informe/` con la misma organización del Proyecto 1 (`05_Referencia_Proyecto1/Informe_final_LaTeX/`) y compilá con `pdflatex` para verificar.

## Materiales y prioridad
1. `01_Instrucciones/Instrucciones_proyecto2_sistema_aislado.txt`: define qué debe tener el informe. Es el criterio principal.
2. `02_Presentaciones_curso/`: referencia principal para conceptos, fórmulas y procedimientos, en especial `Sistemas_aislados/` (Aislado 1–4: baterías, regulador, inversor aislado). Abrí cada presentación antes de usarla; no supongas su contenido por el título.
3. `03_Transcripciones_y_clase_asincrona/`: lo que el profesor explicó en clase.
4. `05_Referencia_Proyecto1/`: el Proyecto 1 (conectado a red, nota 95 en la defensa) como ejemplo del nivel, la estructura, el formato LaTeX y el tipo de cálculos esperados. Reutilizá métodos y scripts, pero **no copies datos ni resultados**: el Proyecto 2 es un sitio nuevo.
5. `04_Plantillas_y_herramientas/`: plantilla IEEE y hoja de escenarios del profesor.

## Primera tarea: Examen corto 4 (entrega miércoles 11 de noviembre, 23:59, por Teams)
Indicación del profesor: seleccionar las baterías del Proyecto 2 con la **misma metodología del examen 2** (Tecnología fotovoltaica; ver `05_Referencia_Proyecto1/Examenes_cortos/` y la diapositiva "Trabajo en grupos. Tarea Examen 2" de `TecnologiaFV4`). Requisitos:
- Revisar **al menos 4 modelos distintos** de baterías que abarquen **al menos 2 de las tecnologías estudiadas** (Aislado 3 y 4).
- Explicar en qué consiste cada tecnología, con referencias bibliográficas.
- Buscar opciones en el mercado con su costo (fuente, moneda y fecha de consulta).
- Hacer una matriz comparativa y seleccionar la batería para el proyecto, justificando la elección.
- Informe corto en la plantilla IEEE, formato y bibliografía IEEE.
- Para el dimensionamiento usar lo indicado en clase: banco de **24 V y 70 % de profundidad de descarga**.

## Sitio del proyecto
- **Casa de Abner López**, en Santa Rosa, distrito del cantón de Oreamuno, provincia de Cartago, Costa Rica.
- Coordenadas (dadas por el grupo en el informe del examen 4): **9.938834° N, 83.831893° O**.
- Características del techo: **pendientes**, el grupo las aporta. No las inventes; pedilas. La lista de equipos ya está en `examen4/calculos/levantamiento_cargas_casa.xlsx`.
- Como la casa tiene servicio eléctrico, el proyecto puede plantearse como el segundo caso del instructivo (sistema de respaldo) o como un conjunto de cargas que se alimentan solo con el sistema aislado. Esa decisión la toma el grupo.
- **Decidido por el grupo (5 nov. 2026):** sistema de **respaldo de cargas críticas** con **2 días de autonomía**.
- **Actualizado (11 nov. 2026):** cargas críticas = refrigerador, congelador, 8 bombillos LED, cargadores de celular y laptop, módem (4.33 kWh/día; ver `examen4/calculos/levantamiento_cargas_casa.xlsx`). La cámara de refrigeración queda excluida y se usa **1 día de autonomía**: con 2 días harían falta 8 B4 y el fabricante admite 4 en paralelo. Banco: 4 Power Queen 24 V 100 Ah en paralelo (400 Ah).

Como la selección de baterías depende del consumo, antes de compararlas hace falta la **lista de equipos** (tensión, potencia nominal y pico, corriente nominal y máxima, y horas de uso al día). Si todavía no la tenemos, prepará una plantilla de tabla para llenarla y una lista de los equipos típicos de una casa para revisarlos con el grupo.

## Después: Proyecto 2 completo
Trabajá por etapas y pedí aprobación al final de cada una:
1. Revisión de materiales y plan del informe (secciones del instructivo ↔ presentaciones ↔ cálculos, tablas y figuras).
2. Desarrollo sección por sección, en LaTeX, con la misma organización del informe del Proyecto 1.
3. Revisión final: requisitos cumplidos, cálculos verificados, consistencia de cifras, compilación sin errores.
4. Presentación de **7 minutos**.

## Reglas de trabajo
- Usá los procedimientos del curso. Si necesitás un método externo, explicá por qué y consultá antes.
- No inventes datos, características de equipos, precios, citas ni requisitos normativos. Si falta un dato, decilo y preguntá; si hay que suponer algo, márcalo como supuesto.
- Usá fichas técnicas oficiales. No cites en la bibliografía las presentaciones del curso ni la hoja del profesor.
- El diagrama unifilar debe usar **simbología estándar (IEC 60617)**, no bloques: fue la corrección del profesor en el Proyecto 1 (ver `figuras/unifilar_tikz.tex`).
- Ante decisiones importantes (sitio, carga, tecnología, equipos), preguntá antes de seguir.

## Redacción
- Natural y clara, propia de estudiantes, en tercera persona; sin lenguaje rebuscado ni teoría que no se use en el diseño.
- Cada apartado: qué se busca, cómo se calcula, qué resultado da y qué significa para el diseño.
- Sin expresiones vagas como «influye menos», «ligeramente», «algo mayor», «reduce el margen»: dar la cifra.
- No repetir datos que ya están en tablas; no listas en negrita con fórmulas; evitar cadenas de datos con punto y coma.
- Cambios solo si corrigen algo real (error, ambigüedad, repetición); no agregar texto para que parezca más completo.
