"""
Dir e Help

? O que são:
    Dir - Apresenta uma lista de funções e métodos que podem ser utilizados em algum tipo de dado.
    Sintaxe: dir(valor/tipo de dado)

    Help - Apresenta as instruções de utilização das funções e métodos disponíveis para determinado tipo de dado.
    Sintaxe: help(função) ou help(valor/ tipo de dado.método / função)
"""
exemplo_dir = dir("dog") # ? Se o tipo de dado for Int por exemplo, a lista irá mudar.
print(exemplo_dir)

exemplo_help = help("dog".title)
print(exemplo_help)
