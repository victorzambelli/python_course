"""
Estruturas Lógicas

and (e):
    ? Retorna True apenas se todas condições forem verdadeiras.

or (ou):
    ? Retorna True apenas se pelo menos uma condição for verdadeira.

is (é):
    ? Comparação entre valores, similar ao ==

not (não):
    ? Inversão do valor booleano (True -> False, False -> True)
"""

# Exemplo com and
numero = 68

if numero >= 60 and numero <= 70:
    print("Tudo ok!")
else:
    print("Erro!")
    
# Exemplo com or
pizza = True
hamburguer = False

if pizza or hamburguer:
    print("Achei comida!")
else:
    print("Estou sem comida!")

# Exemplo com is
login = False

if login is True:
    print("Você está logado!")
else:
    print("Você não está logado!")

# Exemplo com not
agua = True

if not agua:
    print("Preciso comprar água.")
else:
    print("Tenho água, preciso tomar.")
