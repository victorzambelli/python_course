"""
1 - Realizar a média das notas de 4 alunos.

2 - Converter uma temperatura de graus °C para °F e C° para K.
Dados: °F = °C * 1.8 + 32, K = °C + 273.15

"""

# 1)
nota_Pedro = int(input("Digite a nota do Pedro: "))
nota_Paula = int(input("Digite a nota do Paula: "))
nota_Patricia = int(input("Digite a nota do Patricia: "))
nota_Pablo = int(input("Digite a nota do Pablo: "))

media = (nota_Pedro + nota_Paula + nota_Patricia + nota_Pablo) / 4
print(f"A média das notas é: {media}")

# 2)
temperatura = float(input("Digite a temperatura em °C: "))
fahrenheit = temperatura * 1.8 + 32
kelvin = temperatura + 273.15
print(f"A temperatura em °F é: {fahrenheit} \nA temperatura em K é: {kelvin}")
