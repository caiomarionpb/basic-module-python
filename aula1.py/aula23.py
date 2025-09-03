"""
Operador lógico "not"
Usado para inverter expressões
not True = False
not False = True

"""

senha = input("Senha: ")

if senha != "123456":
    print("Acesso negado")
else:
    print("Acesso permitido")


if not senha:
    print("Você não digitou nada")