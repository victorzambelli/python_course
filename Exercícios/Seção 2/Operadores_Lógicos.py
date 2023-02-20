"""
Exercício
    - Crie um sistema de cadastro e login de um site, utilizando um username e senha informados pelo usuário.
"""

print("------------Sistema de Cadastro------------")
username = input("Crie seu nome de usuário: ")
password = input("Crie sua senha: ")

print("\n--------------Sistema de Login--------------")
if input("Usuário: ") == username and input("Senha: ") == password:
    print(f"Login efetuado com sucesso! \nSeja bem vindo(a) {username}")
else:
    print("Login incorreto!")
