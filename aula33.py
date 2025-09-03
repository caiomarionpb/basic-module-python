"""
Faça um programa que peça ao usuário digitar um número inteiro,
informe se este número é par ou impar. Caso o usuário não digite um número inteiro, informe que não é um número inteiro.
"""
num = input("Digite um número: ")
try:
    num_int = int(num)
    if num_int % 2 == 0:
        print("O número é par.")
    else:
        print("O número é ímpar.")
except ValueError:
    print("Isso não é um número inteiro.")

"""
faça um programa que pergunte a hora ao usuário e, baseando-se no horário
descrito, exiba a saudação apropriada. Ex.:
bom dia 0-11, boa tarde 12-17 e boa noite 18-23
"""
horario = input('digite o horário: ')
try:
    hora = int(horario)
    if 0 <= hora <= 11:
        print('Bom dia')
    elif 12 <= hora <= 17:
        print('Boa tarde')
    else:
        ('boa noite')
except ValueError:
    print('Digite um número inteiro')

"""
Faça um programa que peça ao usuário. Se o nome tiver 4 letras ou
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva
"Seu nome é normal"; maior que 6 letras escreva "Seu nome é muito grande"
"""

nome = input('digite seu nome: ')
tamanho = len(nome)
if tamanho <= 4:
    print('Seu nome é curto')
elif 5<= tamanho <= 6:
    print('seu nome é normal')
else:
    print('nome muito grande')
