"""
1°) Exercício
    - Faça um programa que calcule a soma dos divisores de um número inteiro definido pelo usuário.
    ? Exemplo: Se o usuário escolheu 10, temos 1 + 2 + 5 + 10 = 18

2°) Exercício
    - Faça um programa que imprima os n primeiros múltiplos de 5, sendo n definido pelo usuário.
    ? Exemplo: Se o usuário escolheu n = 3, será impresso: 5, 10, 15.
"""

# Exercício 1)
numero_inteiro = int(input("Digite um número inteiro: "))
soma = 0

for i in range(1, numero_inteiro + 1):
    if numero_inteiro % i == 0:
        soma += i

print(f"A soma dos divisores de {numero_inteiro} é {soma}.")
