
"""
Cuidados com dados mutáveis
= - copiando o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""

# nome = 'caio'
# outra_variavel = nome
# nome = 'enzzo'
# print(nome)
# print(outra_variavel)

lista_a = ['caio', 'marion', 1 , True, 1.2]
lista_b = lista_a.copy()

lista_a[0] = 'qualquer coisa'
print(lista_a)
print(lista_b)