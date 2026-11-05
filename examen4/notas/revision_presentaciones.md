# Revisión de presentaciones y transcripciones (baterías)

## Tecnologías estudiadas (Aislado 3, diapositivas 31–47; clase del 23 oct.)
- **Plomo-ácido**: de electrolito inundado y selladas o reguladas por válvula (VRLA). Las VRLA pueden ser de gel o AGM (separador de vidrio absorbente). En Aislado 2 (diap. 16) aparece la OPzS (placa tubular inundada) en el ejemplo de dimensionamiento.
- **Ion-litio**: de fosfato (LiFePO₄) y de níquel, cobalto y magnesio [sic] (NCM). En la tabla de costos aparece también LTO.
- **Níquel-cadmio**, **sodio-azufre** y **de flujo** (vanadio redox y zinc-bromo).
- Tabla resumen de May et al. (2018): vida en años, ciclos, eficiencia y costo instalado, junto con PHS y CAES.

## Parámetros que usa el profesor
| Parámetro | Dónde |
|---|---|
| Capacidad nominal en Ah o Wh, con la tasa C20, C100 o C10 y su dependencia de la temperatura y de la corriente | Aislado 3, diap. 7–12; clase del 23 oct. |
| Tensión nominal y armado en serie y paralelo (solo baterías iguales) | Aislado 1, diap. 19; Aislado 4, diap. 5–7; clase del 30 oct. |
| Corriente máx. de carga (define el regulador) y de descarga (define las baterías en paralelo según el inversor) | Aislado 3, diap. 13–19 |
| SOC y DOD (DOD < 75 % para plomo-ácido; 70 % en el proyecto) | Aislado 1, diap. 19; Aislado 3, diap. 20–24; Aislado 4, diap. 28 |
| Días de autonomía (1 a 10; 2 en el ejemplo) | Aislado 1, diap. 19; Aislado 3, diap. 26–27 |
| Ciclos de vida a una DOD dada | Aislado 3, diap. 41 y 47; ficha de la diap. 9 de Aislado 4 |
| Eficiencia (ida y vuelta) y pérdida por rendimiento de la batería p_b = 0.01 | Aislado 1, diap. 9–11; Aislado 3, diap. 43, 45 y 47 |
| Autodescarga K_a = 0.005, término (1 − K_a·D/DOD) | Aislado 1, diap. 10; Aislado 4, diap. 12–13 |
| Temperatura de operación (alta y baja) | Aislado 3, diap. 9 y 41; ficha de la diap. 9 de Aislado 4 |
| Mantenimiento (agua, ecualización, instalación) | Aislado 3, diap. 35–37; Aislado 4, diap. 27 |
| Costo ($/kWh) | Aislado 3, diap. 34, 39, 41 y 47 |
| Densidad de energía y peso | Aislado 3, diap. 41; clase del 30 oct. (estante de plomo-ácido frente a batería de litio en el TEC) |
| Garantía y BMS (ficha de ejemplo) | Aislado 4, diap. 8–9 |

## Fórmula de capacidad (Aislado 1, diap. 20; Aislado 2, diap. 15; Aislado 3, diap. 27)
Q = 1.1 · E_T · D / (V · DOD), en Ah. E_T es la energía diaria ya corregida por pérdidas, D los días de autonomía, V = 24 V y DOD = 0.7. El 1.1 es un margen de seguridad. En el ejemplo de clase: Q = 1.1 · 2115.8 · 2 / (12 · 0.7) = 554.1 Ah, con C100.

## Indicación del examen (clase del 23 oct.)
"Similar al examen corto 2": investigar y evaluar tecnologías para el proyecto. En Aislado 4 (diap. 41) se pide terminar de definir la tecnología y el fabricante, elegir el regulador y redefinir el arreglo de baterías.
