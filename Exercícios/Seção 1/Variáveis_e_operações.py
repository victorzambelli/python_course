"""
1) Inverter uma frase

2)
Criação de personagem de mundo de ficção, apresentando as seguintes opções:
    - Cor de cabelo (string)
    - Cor de pele (string)
    - Classes: Guerreiro, Mago, Arqueiro (string)
    - Idade (int)
    - Altura (float)
    - Habilidade específica (string)

Imprima para o usuário o personagem completo.
"""

# 1)
frase = "Hello world!"
print(frase[::-1])

# 2)
print("--------------Bem vindo a um novo universo--------------")
print("------------------Crie seu personagem-------------------")
hairColor = input("Informe a cor de cabelo: ")
skinColor = input("Informe a cor de pele: ")
classes = input("Informe a classe (Guerreiro, Mago, Arqueiro): ")
age = int(input("Informe a idade: "))
height = float(input("Informe a altura: "))
skill = input("Informe a habilidade específica: ")


print("------------------Personagem Criado-------------------")
print(f"O personagem tem a cor de cabelo: {hairColor} \nCor de pele: {skinColor} \nClasse: {classes} \nIdade: {age} \nAltura: {height} \nHabilidade: {skill}")
