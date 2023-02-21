"""
Loop for

    - O que é?
        ? Loop é algo que se repete diversas vezes.
        ? Na programação utilizamos para repetir uma determinada tarefa.

    - For (para):
        ? é uma das ferramentas que realizam este loop.

    - Como declarar em python?
        ? for item in sequencia:
            #Processo

    - Traduzindo:
        ? Para cada item na sequência, faça:
            #Processo

    - A sequência deve ser iterável, mas o que é isso?
        ? São um conjunto de dados que podem ser desmembrados.

    Exemplos:
        ? a) Strings (Podem ser desmembradas por cada caracter)
            "Filmes" -> 'F', 'i', 'l', ...

            ? Podemos pegar caracteres pelos índices da string:
            nome = "Samantha"
            print(nome[2]) # Imprimir o m

            ? Curiosidade:
            S a m a n t h a
            0 1 2 3 4 5 6 7

        ? b) Listas, Tuplas, dicionários e sets(conjuntos):
            ? Como declarar listas:
            frutas = ["banana", "morango", "laranja"]

        ? c) Função range():
            - O que ela faz?
            ? Cria um intervalo de números escolhidos pelo usuário.

            - Declaração:
            ? range(numero_de_inicio, numero_de_final)
            
            Exemplo:
            ? range(1,10) - Cria um intervalo de 1 a 10.
"""

# Exemplo com string
filme = "Avatar 2"

for letra in filme:
    print(letra)

# Exemplo com lista
frutas = ["banana", "morango", "laranja"]

for fruta in frutas:
    print(fruta)

# Exemplo com range
numeros = range(1, 11)
for numero in numeros:
    print(numero, end=",")

# Break
string = 'abcdefghijkl'

for letra in string:
    print(letra)
    if letra == 'g':
        break

# Continue
string2 = 'abcdefghijkl'

for letra in string2:
    if letra == 'g':
        continue
    print(letra)

# Enumerate
pessoa = 'Sherlock'

for valor in enumerate(pessoa):
    print(valor)

for contador, letra in enumerate(pessoa):
    print(f"Número: {contador} é a letra: {letra}")
