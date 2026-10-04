package mx.edu.practica4;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertThrows;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;

class EstacionamientoTest {

    private Estacionamiento sistema;

    @BeforeEach
    void setup() {
        sistema = new Estacionamiento();
    }

    // 1. Pruebas Parametrizadas: Casos Frontera y Periodo Libre (7 subcasos) (R4, R5, R6, R7)
    @ParameterizedTest
    @CsvSource({
        "0, normal, false, 0.0",      // Caso 4: Límite inferior 0 min
        "15, normal, false, 0.0",     // Caso 5: Límite periodo libre 15 min
        "16, normal, false, 20.0",    // Caso 6: Inicio cobro tarifa base
        "60, normal, false, 20.0",    // Caso 7: Fin de tarifa base 60 min
        "61, normal, false, 35.0",    // Caso 8: Hora adicional iniciada (61 min)
        "120, normal, false, 35.0",   // Caso 9: Exactamente 2 horas
        "121, normal, false, 50.0"    // Hora adicional iniciada (121 min)
    })
    void testTarifasFronteraNormal(int minutos, String cliente, boolean perdido, double esperado) {
        double resultado = sistema.calcularTotal(minutos, cliente, perdido);
        assertEquals(esperado, resultado, 0.001);
    }

    // 2. Casos Normales (R6, R7)
    @Test
    void testCaso01Normal30Min() {
        assertEquals(20.00, sistema.calcularTotal(30, "normal", false), 0.001);
    }

    @Test
    void testCaso02Normal90Min() {
        assertEquals(35.00, sistema.calcularTotal(90, "normal", false), 0.001);
    }

    @Test
    void testCaso03Frecuente45Min() {
        assertEquals(18.00, sistema.calcularTotal(45, "frecuente", false), 0.001);
    }

    // 3. Entradas Inválidas / Excepciones (R10, R11)
    @Test
    void testCaso10MinutosNegativos() {
        assertThrows(IllegalArgumentException.class, () -> {
            sistema.calcularTotal(-5, "normal", false);
        });
    }

    @Test
    void testCaso11ClienteInvalido() {
        assertThrows(IllegalArgumentException.class, () -> {
            sistema.calcularTotal(30, "VIP", false);
        });
    }

    // 4. Interacción Boleto Perdido vs Descuento (R3, R8)
    @Test
    void testCaso12FrecuenteBoletoPerdido60Min() {
        assertEquals(300.00, sistema.calcularTotal(60, "frecuente", true), 0.001);
    }

    @Test
    void testCaso13FrecuenteBoletoPerdido150Min() {
        assertEquals(300.00, sistema.calcularTotal(150, "frecuente", true), 0.001);
    }

    // 5. Clientes Frecuentes y Decimales (R7, R8)
    @Test
    void testCaso14FrecuenteDecimales61Min() {
        assertEquals(31.50, sistema.calcularTotal(61, "frecuente", false), 0.001);
    }
}
