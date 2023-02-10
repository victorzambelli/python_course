"""
Operações matemáticas

? Temos x operações matemáticas no python:
    - Adição ( Utiliza o operador + )
    - Subtração ( Utiliza o operador - )
    - Multiplicação ( Utiliza o operador * )
    - Divisão ( Utiliza o operador / )
    - Potência ( Utiliza o operador ** )
    - Resto da divisão ( Utiliza o operador % )
    - Porcentagem ( Utiliza o operador // )

* Exemplo abaixo:
"""

num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))

print(f"Adição: {num1 + num2}")
print(f"Subtração: {num1 - num2}")
print(f"Multiplicação: {num1 * num2}")
print(f"Divisão: {num1 / num2}")
print(f"Potência: {num1 ** num2}")
print(f"Resto da divisão: {num1 % num2}")
print(f"Porcentagem: {num1 // num2}")

# Operação com string
name = "João "
print(name * 3)

surname = "Santos"
print(name + surname)

# Operação com boolean
# *Obs: True = 1 / False = 0
print(True * False) # = 0
print(True * True) # = 1
print(True + True) # = 2
print(True - False) # = 1
