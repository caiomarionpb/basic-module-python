"""
Listas em python
Tipo list - Mutável
suporta varios valores de qualquer tipo
conhecimentos reutilizáveis - indices e fatiamento
métodos úteis: append, insert, pop, del, clear, extend, +
"""

#     +01234
#     -54321

string = 'ABCDE' # 5 caracteres (len)
# print(lista, type(lista))
#         0    1         2         3    4 - indices
#        -5   -4        -3        -2   -1 - indices
lista = [123,True, 'caio marion', 1.2, []] # [] lista vazia com chaves sem nada!!
lista[-3] = 'Maria'
print(lista)
print(lista[2], type(lista[2]))
