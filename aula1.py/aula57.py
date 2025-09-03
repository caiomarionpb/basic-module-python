"""
tipo tupla = uma lista imutável
"""
nomes = 'maria', 'helena', 'luiz'
print(nomes[0])
print(nomes)

nomes = ['maria', 'helena', 'luiz']
nome = tuple(nomes)
nomes = list(nomes)

print(nomes[-1])
print(nomes)