"""
iterável -> str, range, etc (.__iter__)
iterador -> quem sabe entregar um valor por vez
next -> me entregue o proximo valor (.__next__)
iter -> me entregue seu iterador 
"""
#for letra in texto
# o código abaixo faz exatamente o que o for faz "por baixo dos panos"
texto = 'caio' # iterável
# iterador = iter(texto) # iterator

# while True:
#     try:
#         letra = next(iterador)
#         print(letra)
#     except StopIteration:
#        break

for letra in texto:
    print(letra) # basicamente 8 linhas de código resumidas em 3