# introdução a f-strings
#o que estiver dentro das chaves é a variável que será mostrada em string no print

nome = 'Caio Marion'
altura = 1.85
peso = 110
imc = peso / altura ** 2

linha_1 = f'{nome} tem {altura: .2f} de altura'
linha_2 = f'pesa {peso} kg e seu IMC é {imc: .2f}'
linha_3 = f'{imc: .2f}'
print(linha_1)
print(linha_2)
print(linha_3)