"""
Tipos de Dados

? Temos 8 tipos de dados no python:
    - String: que seria um texto, exemplo: "texto"
    - Integer: que seria um número inteiro, exemplo: 10
    - Float: que seria um número real, exemplo: 10.5
    - Boolean: que seria um booleano, exemplo: True
    - Complex: que seria um número complexo, exemplo: 1+2j
    - List: que seria uma lista, exemplo: [1, 2, 3]
    - Dictionary: que seria um dicionário, exemplo: {"nome": "Amanda", "idade": 25}
    - Tuple: que seria um tipo que agrupa um conjunto de elementos, exemplo: (1, 2, 3)
"""
game = "God of war"
print(game[4:10])

name = "João"
age = 25
height = 1.75
is_male = True
print(type(name), type(age), type(height), type(is_male))

fruits = ["banana", "apple", "orange"]
print(type(fruits))

person = {"name": "Amanda", "age": 25}
print(type(person))

points = (100, 25, 20)
print(type(points))
