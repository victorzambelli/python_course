"""
Loop While

    - Como declarar?
    while condição: # Enquanto a condição for True faça:
        # Processoo
"""

contador = 0

while contador < 9:
    print(contador, end = ' ')
    contador += 1
    if contador == 5:
        continue # Prosseguir com o loop imediatamente / break # Para o loop imediatamente