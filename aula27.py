"""
fatiamento de strings
012345678
Olá mundo
-987654321
fatiamento [i: f: p] [::] inicio, fim, passo
Obs.: a função len retorna a quantidade de caracteres da str
"""

variavel = 'testando o fatiamento'
print(variavel[4:9]) # do 4 ao 8
print(variavel[-10:-0]) # -0 é o mesmo que 0
print(len(variavel)) # quantidade de caracteres na string
print(variavel[0: len(variavel): 1]) # percorre a string toda
print(variavel[0: 21: 2]) # pula de 2 em 2
print(variavel[::-1]) # inverte a string
