"""
Listas em python
Tipo list - Mutável
suporta varios valores de qualquer tipo
conhecimentos reutilizáveis - indices e fatiamento
métodos úteis: 
    append: adiciona um item ao final
    insert: adiciona um item no indice escolhido
    pop: remove do final ou do indice escolhido
    del: apaga um indice
    clear: limpa a lista
    extend: extende a lista 
    + : concatena as listas

create read update   delete
criar, ler, alterar, apagar = lista[i] (CRUD)
"""

lista_a = [1, 2, 3]
lista_b = [4, 5 ,6]
lista_c = lista_a + lista_b
lista_a.extend(lista_b)
print(lista_c)