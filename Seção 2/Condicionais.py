"""
Estrutura condicionais

* if (se)
* elif (senão se)
"""

# Exemplo: Altura para poder ir no brinquedo de parque.
altura = float(input("Digite a altura: "))

if altura <= 1.6:
    print("Você não tem a altura necessária para este brinquedo!")
elif altura >= 1.9:
    print("Você é muito alto para este brinquedo!")
else:
    print("Divirta-se!")

# Exemplo 2: Consultar média final para aprovação
nota = float(input("Digite sua nota: "))

if nota > 6:
    print("Pode curtir suas férias, você passou! 🎉")
elif nota == 6:
    print("Ufa, essa foi por pouco! 😣")
else:
    print("Você não conseguiu dessa vez! 😥")

# Exemplo 3: Impar ou par
numero = int(input("Digite um numero: "))

if numero % 2 == 0:
    print(f"{numero} é par!")
else:
    print(f"{numero} é impar!")

# Exemplo com String
pais = input("Digite o nome de um pais: ")

if pais == "Noruega":
    print("Ah não, muito frio!")
elif pais == "China":
    print("Muito longe!")
elif pais == "Brasil":
    print("Já estamos aqui!")
else:
    print("Vamos!")
