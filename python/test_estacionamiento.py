import pytest
from estacionamiento import Estacionamiento


@pytest.fixture
def sistema():
    """Fixture que provee la instancia reutilizable del sistema."""
    return Estacionamiento()


# 1. Pruebas Parametrizadas: Casos Frontera y Gratuidad (R4, R5, R6, R7)
@pytest.mark.parametrize(
    "minutos, cliente, perdido, esperado",
    [
        (0, "normal", False, 0.0),       # R4: Límite inferior 0 min
        (15, "normal", False, 0.0),      # R5: Límite superior gratis (15 min)
        (16, "normal", False, 20.0),     # R6: Inicio cobro tarifa base
        (60, "normal", False, 20.0),     # R6: Fin de tarifa base 60 min
        (61, "normal", False, 35.0),     # R7: Hora adicional iniciada (minuto 61)
        (120, "normal", False, 35.0),    # R7: Exactamente 2 horas
        (121, "normal", False, 50.0),    # R7: Hora adicional iniciada (minuto 121)
    ],
)
def test_tarifas_frontera_normal(sistema, minutos, cliente, perdido, esperado):
    # Arrange & Act
    resultado = sistema.calcular_total(minutos, cliente, perdido)

    # Assert
    assert resultado == pytest.approx(esperado)


# 2. Casos Normales (R6, R7)
def test_caso_normal_30_minutos(sistema):
    # Arrange
    minutos, cliente, perdido = 30, "normal", False

    # Act
    resultado = sistema.calcular_total(minutos, cliente, perdido)

    # Assert (R6)
    assert resultado == pytest.approx(20.0)


def test_caso_normal_90_minutos(sistema):
    # Arrange
    minutos, cliente, perdido = 90, "normal", False

    # Act
    resultado = sistema.calcular_total(minutos, cliente, perdido)

    # Assert (R7)
    assert resultado == pytest.approx(35.0)


# 3. Prueba con Decimales y Descuento Frecuente (R7, R8)
def test_cliente_frecuente_con_decimales(sistema):
    # Arrange
    minutos, cliente, perdido = 61, "frecuente", False

    # Act
    resultado = sistema.calcular_total(minutos, cliente, perdido)

    # Assert (R7, R8: $35.00 con 10% desc = $31.50)
    assert resultado == pytest.approx(31.50)


# 4. Interacción de Reglas: Boleto Perdido vs Cliente Frecuente (R3, R8)
def test_boleto_perdido_prevalece_sobre_descuento(sistema):
    # Arrange
    minutos, cliente, perdido = 60, "frecuente", True

    # Act
    resultado = sistema.calcular_total(minutos, cliente, perdido)

    # Assert (R3: Debe ser $300 fijos sin aplicar descuento)
    assert resultado == pytest.approx(300.0)


def test_boleto_perdido_con_muchos_minutos(sistema):
    # Arrange
    minutos, cliente, perdido = 150, "normal", True

    # Act
    resultado = sistema.calcular_total(minutos, cliente, perdido)

    # Assert (R3: Se cobran $300 fijos)
    assert resultado == pytest.approx(300.0)


# 5. Entradas Inválidas / Excepciones (R10, R11)
def test_minutos_negativos_lanza_excepcion(sistema):
    # Arrange & Act & Assert (R10)
    with pytest.raises(ValueError):
        sistema.calcular_total(-5, "normal", False)


def test_cliente_invalido_lanza_excepcion(sistema):
    # Arrange & Act & Assert (R11)
    with pytest.raises(ValueError):
        sistema.calcular_total(30, "vip", False)
