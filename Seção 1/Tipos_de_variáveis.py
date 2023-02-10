"""
Tipos de Variáveis

? O que são:
    - São um modo de rotular ou nomear todos os dados pertencentes ao seu programa.

? O que são Dados:
    - São todas informações que serão utilizadas ao longo do seu código. Podendo ser números, palavras, frases, textos, dentre outros.

? Temos apenas 2 tipos de variáveis no python:
    - Variável Global: Pode ser utilizada dentro do código inteiro.
    - Variável Local: Pode ser utilizada dentro de um bloco de código.
"""

def hello_name():
    name = "João"
    print(f"Olá, {name}!")

# print(name) Isso não será permitido, pois a variável name está dentro de um bloco de código, logo ela é uma variável local.

hello_name()
