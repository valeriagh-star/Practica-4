# Práctica 4

## Casos-Prueba y Análisis

> ### Integrantes del Equipo:
> * García Herrera Valeria
> * Grajeda Palacios Dulce Abril
> * Pérez Megchun Pablo de Jesús

> ### Breve descripción de la práctica:
> <p align="justify">
> Esta práctica consiste en diseñar, implementar y analizar una suite de pruebas unitarias para un sistema de cobro de estacionamiento que evalúa los minutos de permanencia, el tipo de cliente y si perdió el boleto. A partir del flujo de trabajo <b>Problema → Modelo → Casos → Pruebas ↔ Implementación</b> y el patrón <i>Arrange–Act–Assert</i>, las pruebas se estructuran desde la especificación formal y no solo desde el código. Esto permite identificar casos normales, fronteras y entradas inválidas, verificar excepciones y analizar los resultados para diferenciar objetivamente entre la aprobación de una prueba y la validez integral del programa.
> </p>

---

## Reglas del Sistema y Cobertura

1. **Valores Válidos y Excepciones (R1, R2, R10, R11)**
   - **Propósito:** Validar que los minutos no sean negativos y que el tipo de cliente sea un valor permitido.
   - **Beneficio:** Garantiza el manejo correcto ante datos de entrada no válidos o fuera del modelo mediante el lanzamiento de excepciones.

2. **Tiempo Libre y Tarifa Base (R4, R5, R6)**
   - **Propósito:** Comprobar el costo de $0.00 en el rango de 0 a 15 minutos y la tarifa base de $20.00 en el rango de 16 a 60 minutos.
   - **Beneficio:** Verifica el cumplimiento exacto de los límites del periodo sin costo y la transición a la tarifa inicial de la primera hora.

3. **Horas Adicionales y Fracciones (R7)**
   - **Propósito:** Aplicar la función techo (`math.ceil` / `Math.ceil`) a partir del minuto 61 para cobrar $15.00 por cada hora adicional o fracción iniciada.
   - **Beneficio:** Asegura el cobro de la fracción de hora iniciada desde el primer minuto excedente conforme a la regla del modelo.

4. **Descuentos y Boleto Perdido (R3, R8, R9)**
   - **Propósito:** Aplicar un 10% de descuento a clientes frecuentes y asignar el cobro fijo de $300.00 cuando el boleto fue perdido.
   - **Beneficio:** Confirma que el cobro por boleto perdido anula cualquier descuento por cliente frecuente y evita costos negativos.

---

## Estrategia de Trabajo

- **Análisis del Modelo Formal:** Identificación de las 11 reglas del modelo del sistema y diseño de la matriz de 15 casos de prueba priorizando valores frontera (15–16 min, 60–61 min).

- **Inclusión de Redondeo Superior:** Incorporación de `math.ceil` tanto en Python como en Java para garantizar el cobro de la fracción de hora iniciada a partir del minuto 61.

- **Ejecución y Verificación:** Validación del 100% de éxito de las pruebas unitarias tanto en Python como en Java.

---

## Requisitos

- **Python:** Versión 3.10 o superior con la biblioteca `pytest`.
- **Java:** JDK 17 o superior con Apache Maven 3.5.0+.

---

## Instrucciones para ejecutar las pruebas:

- **Ejecución de pruebas en Python (`pytest`):**

  `cd python`

  `pytest -v`

- **Ejecución de pruebas en Java (`Maven` / `JUnit 5`):**

  `cd ../java`

  `mvn test`
