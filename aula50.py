"""
Listas em python
Tipo list - Mutável
suporta varios valores de qualquer tipo
conhecimentos reutilizáveis - indices e fatiamento
métodos úteis: 
    append, insert, pop, del, clear, extend, +
create read update   delete
criar, ler, alterar, apagar = lista[i] (CRUD)

"""

lista = [10, 20, 30, 40, 50]
lista[2] = 300
del lista[2] # del deleta da lista o valor indicado no indice
print(lista)
print(lista[2])
lista.append(60) # append adiciona a lista
lista.pop() #remove o ultimo elemento. no caso o 60
lista.append(70) # append adiciona a lista
lista.append(80) # append adiciona a lista
ultimo_valor = lista.pop(1)
print(lista, 'removido,', ultimo_valor)
