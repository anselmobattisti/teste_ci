"""Código de produção usado nos exemplos de teste da aula 15."""


class Calculadora:
    def somar(self, a, b):
        return a + b

    def dividir(self, a, b):
        # Em Python, 10 / 0 já lança ZeroDivisionError.
        return a / b
