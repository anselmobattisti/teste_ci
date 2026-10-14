import pytest

from src.calculadora import Calculadora


def test_deve_somar_dois_numeros():
    calc = Calculadora()          # Arrange
    resultado = calc.somar(2, 3)  # Act
    assert resultado == 5         # Assert


def test_deve_lancar_erro_ao_dividir_por_zero():
    calc = Calculadora()
    # verifica que a operacao lanca a excecao correta:
    with pytest.raises(ZeroDivisionError):
        calc.dividir(10, 0)
