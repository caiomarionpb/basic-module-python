"""
Faça uma lista de comrpar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar os valores de sua lista
não permita que o programa quebre com erros de indices inexistentes na lista
"""

def menu():
    print('\n=== Lista de comrpas ===')
    print('1 - adiconar itens')
    print('2 - remover itens')
    print('3 - mostrar lista')
    print('4 - sair')

def main():
    lista = []

    while True:
        menu()
        opcao = input('Escolha uma opção: ')

        if opcao == '1':
            item = input('digite o item que deseja adicionar: ')
            lista.append(item)
            print(f'{item} foi adicionado a lista!')

        elif opcao == '2':
            if not lista:
                print('a lista esta vazia, nada a remover')
            else:
                for i, item in enumerate(lista):
                    print(f'{i} - {item}')
                try:
                    indice = int(input('Digite o indice do item que deseja remover'))
                    if 0 <= indice < len(lista):
                        removido = lista.pop(indice)
                        print(f'{removido} foi removido da lista')
                    else:
                        print('Índice inválido.')
                except ValueError:
                    print('digite um número válido')

        elif opcao == '3':
            if not lista:
                print('sua lista está vazia')
            else:
                print('\n sua lista de compras: ')
                for i, item in enumerate(lista):
                    print(f'{i} - {item}')
        
        elif opcao == '4':
            print('saindo do programa')
            break
        else:
            print('opção invalida')

main()