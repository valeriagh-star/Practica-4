package mx.edu.practica4;

public class Estacionamiento {

    public static final double TARIFA_BOLETO_PERDIDO = 300.0;

    public double calcularTotal(int minutos, String tipoCliente, boolean boletoPerdido) {
        if (minutos < 0) {
            throw new IllegalArgumentException("Los minutos no pueden ser negativos");
        }

        if (!"normal".equals(tipoCliente) && !"frecuente".equals(tipoCliente)) {
            throw new IllegalArgumentException("Tipo de cliente no válido");
        }

        // R3: Boleto perdido cobra cuota fija inmediatamente y sin descuentos
        if (boletoPerdido) {
            return TARIFA_BOLETO_PERDIDO;
        }

        double total;

        // R4 / R5: De 0 a 15 minutos es gratis
        if (minutos <= 15) {
            total = 0.0;
        } else if (minutos <= 60) {
            total = 20.0;
        } else {
            // R7: Redondeo hacia arriba para horas adicionales iniciadas
            int horasAdicionales = (int) Math.ceil((minutos - 60) / 60.0);
            total = 20.0 + (horasAdicionales * 15.0);
        }

        // R8: Descuento del 10% 
        if ("frecuente".equals(tipoCliente)) {
            total *= 0.90;
        }

        return Math.round(total * 100.0) / 100.0;
    }
}
