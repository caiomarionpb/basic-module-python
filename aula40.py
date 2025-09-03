# iterando strings com while

#   0123456789
nome = 'caio marion' # iteráveis

tamanho_nome = len(nome)

indice = 0
novo_nome = ''
while indice < len(nome):
    letra = nome[indice]
    novo_nome += f'*{letra}'
    indice += 1

novo_nome += '*'
print(novo_nome)
# print(tamanho_nome)

# print(nome[5])

# nova_string = ''
# nova_string += '*C*a*i*o* *M*a*r*i*o*n*'