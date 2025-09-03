# solução do exercicio da aula59.py

import os

lista = []
while True:
    print('selecione uma opção: ')
    opcao = input('[i]nserir, [a]pagar, [l]istar: ')

    if opcao == 'i':
        os.system('cls')
        valor = input('Valor: ')
        lista.append(valor)
    elif opcao == 'a':
        indice_str = input('Escolha seu índice para apagar: ')

        try:
            indice = int(indice_str)
            del lista[indice]
        except ValueError:
            print('não foi possível apagar este índice')
        except IndexError:
            print('índice não existe')
    elif opcao == 'l':
        os.system('cls')

        if len(lista) == 0:
            print('nada a listar')

        for i, valor in enumerate(lista):
            print(i, valor)


    else:
        print('Por favor, escolha i, a ou l.')