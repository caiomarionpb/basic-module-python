"""
Exercicio
exiba os indices da lista
Maria
Helena
Luiz
"""

lista = ['Caio', 'marion', 'garcia']
lista.append('joao')


indices = range(len(lista))

for indice in indices:
    print(indice, lista[indice], type(lista[indice]))
    