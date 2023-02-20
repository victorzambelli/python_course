"""
Exercício
    - Fazer uma calculadora de 4 operações (soma, subtração, multiplicação, divisão e potência).
    ? Peça a operação desejada ao usuário e depois numeros ao usuário.
"""

print("-----------------Calculadora------------------")
print("Soma (+), Subtração (-), Multiplicação (-), Divisão (/), Potência (^)")
operator = input("Digite um operador: ")
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
print("----------------------------------------------")

if operator == "+":
    print(f"A soma de {num1} + {num2} é: \n{num1 + num2}")
elif operator == "-":
    print(f"A subtração de {num1} + {num2} é: \n{num1 - num2}")
elif operator == "*":
    print(f"A multiplicação de {num1} + {num2} é: \n{num1 * num2}")
elif operator == "/":
    print(f"A divisão de {num1} + {num2} é: \n{num1 / num2}")
elif operator == "^":
    print(f"A potência de {num1} + {num2} é: \n{num1 ** num2}")
else:
    print("Operador inválido!")
