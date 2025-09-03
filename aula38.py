"""
repetições
While(enquanto)
Executa uma ação enquanto uma condição for verdadeira
loop infinito -> quando um codigo nao tem fim
continue 
"""

contador = 0

while contador <= 100:
    contador += 1

    if contador == 6:
        print("esconde o 6")
        continue

    if contador >=10 and contador <=27:
        print('esconde o', contador)
        continue

    print(contador)
    
    if contador == 40:
        break

print('acabou')
