"""
introdução ao desempacotamento + tuples (tuplas)
"""

nome1, nome2, nome3 = ['maria', 'helena', 'luiz']
print(nome2)

nome1, *resto = ['maria', 'helena', 'luiz']
print(nome1, resto)

_, _, nome, *resto = ['maria', 'helena', 'luiz']
print(nome) # o underline é uma variavel mas indica que nao usarei aquele valor, mas o python entende como variavel e considera como se fosse nome1, nome2, nome3 e assim em diante.