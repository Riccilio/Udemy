"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista.
Não permita que o programa quebre com
erros de índices inexistentes na lista.
"""
import os

lista_de_compras = []

while True:
    user_input = input('Selecione uma opção\n'
                   '[i]nserir [a]pagar [l]istar:')

    if user_input.lower() == 'i':
        os.system('cls')
        item = input('Qual item deseja inserir na lista?')
        lista_de_compras.append(item)

    elif user_input.lower() == 'a':
        indice_str = input('Escolha o indice para apagar: ') #essa é a forma como o professor fez
                                                             #achei interessante pela forma como
                                                             #tratou os erros
        try:
            indice = int(indice_str)
            del lista_de_compras[indice]
        except ValueError:
            print('por favor, digite um indice. Deve ser um número int.')
        except IndexError:
            print('este índice não existe na lista.')



        # if len(lista_de_compras) == 0:    ###### ESTA FOI A FORMA COMO EU FIZ, SEM AJUDA EXTERNA.
        #     print('não há itens na lista para deletar.')
        # else:
        #     for index, item in enumerate(lista_de_compras):
        #         print(index, item)
        #     indice = int(input('qual o index do item que deseja retirar?'))
        #     print(f'o item {lista_de_compras[indice]} será retirado da lista de compras')
        #     lista_de_compras.pop(indice)

    elif user_input.lower() == 'l':
        if len(lista_de_compras) == 0:
            print('Sua lista está vazia.')
        else:
            for index, item in enumerate(lista_de_compras):
                print(index, item)

    else:
        print('opção inválida')