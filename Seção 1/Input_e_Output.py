"""
Input e Output

? O que são:
    Input - input(): Recebe dados do usuário
    Output - print(): Imprime dados do usuário

*Observação: Os dados recebidos são do tipo String.
"""

print("Digite seu nome: ")
name = input()

print(f"Olá, {name}!")

print("Digite um número: ")
num1 = input()
print("Digite um segundo número: ")
num2 = input()

# ? Se recebemos dados do tipo string, precisamos converter para um número.
print(f"A soma entre {num1} e {num2} é: {int(num1) + int(num2)}") # ? Neste caso escolhemos o tipo int = integer (inteiro)
