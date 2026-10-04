import math


class Estacionamiento:
    TARIFA_BOLETO_PERDIDO = 300.0

    def calcular_total(self, minutos: int, tipo_cliente: str = "normal",
                       boleto_perdido: bool = False) -> float:
        """
        Calcula el total a pagar de acuerdo con el modelo de la práctica.
        """
        if minutos < 0:
            raise ValueError("Los minutos no pueden ser negativos")

        if tipo_cliente not in ("normal", "frecuente"):
            raise ValueError("Tipo de cliente no válido")

        # R3: Boleto perdido cobra cuota fija de $300 inmediatamente y sin descuento
        if boleto_perdido:
            return self.TARIFA_BOLETO_PERDIDO

        # R4 / R5: De 0 a 15 minutos es gratis (<= 15)
        if minutos <= 15:
            total = 0.0
        # R6: De 16 a 60 minutos es la tarifa base de $20
        elif minutos <= 60:
            total = 20.0
        # R7: Más de 60 minutos cobra $15 por cada hora adicional iniciada
        else:
            horas_adicionales = math.ceil((minutos - 60) / 60)
            total = 20.0 + (horas_adicionales * 15.0) 

        # R8: Descuento del 10% para clientes frecuentes (si no se perdió el boleto)
        if tipo_cliente == "frecuente":
            total *= 0.90

        return round(total, 2)
