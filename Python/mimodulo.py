"""
Ejemplo de un módulo Python. Contiene una variable llamada mi_variable,
una función llamada mifact que implementa de forma simple el cálculo del factorial de un número (entero positivo).
"""

mi_variable = -8.90234

def mifact(n):
    factorial = 1
    x = 1
    while x <= n:
        factorial = factorial*x
        x = x+1
    return factorial
