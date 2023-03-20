"""
1) Faça um programa que calcule o maior palindromo resultado do produto de dois números de 3 dígitos.
    - Palindromo são numeros que lendo da esquerda para a direita resulta no mesmo número caso leia da direita para esquerda.

    Ex: 52625
    - O maior palindromo resultado do produto de dois números é 91+99 = 9009
"""

n1 = 999
res = 0

while n1 != 0:
    n2 = n1
    while n2 != 0:
        numero = n1 * n2
        numero_invertido = str(numero)[::-1]
        if numero_invertido == str(numero):
            num = int(numero)
            if res < num:
                res=num
                n2 -= 1
            else:
                n2 -= 1
        else:
            n2 -= 1
    n1 -= 1

print(res)
