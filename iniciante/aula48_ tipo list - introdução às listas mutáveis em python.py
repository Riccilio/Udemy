"""
Listas em Python
tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizaveis - índices e fatiamento

========================Métodos Úteis===========================

*append - Adiciona um item ao final
*insert - Adiciona um item no índice escolhido
*pop - remove do final da lista se não for declarado um indice escolhido e retorna o elemento
*del - apaga um índice
*clear - limpa a lista
*extend - estende a lista
*+ - concatena listas


Create Read Update Delete (CRUD)
"""


#          +01234
#          -54321
# string = 'ABCDE' # 5 caracteres (len)
# lista1 = list()
#indices   0    1          2        3    4
# lista2 = [123, True, 'Pedro Leme', 1.2, []]
#print(lista1, lista2, type(lista1))
#print(bool(lista1), bool(lista2))
# lista2[2] = 'Maria'
# print(lista2)
# print(lista2[2], type(lista2[2]))


########### PARTE 2 ########### = APPEND, POP, DEL

# lista = [10, 20, 30, 40]
# lista[2] = 300
# del lista[2]
# numero = lista[2]
# print(lista, numero)
# lista.append(50)
# lista.pop()
# lista.append(60)
# lista.append(70)
#removido = lista.pop()
# removido = lista.pop(2)
# print(lista, type(removido), removido)

########### PARTE 3 ###############
# lista = ['a', 'b', 'c', 'd']
# lista.insert(0, 'e')
#metodo insert : pode-se passar um index maior que a lista, que o metodo leva em consideração.
# se o index for maior que o range da lista, o metodo funciona como um append.
# print(lista)

########### PARTE 4 ###############
# lista_a = [1, 2, 3]
# lista_b = [4, 5, 6]
# lista_c = lista_a + lista_b
# lista_a.extend(lista_b) #não retorna o valor, no caso aqui alterou o conteúdo da lista_a
# print(lista_c)
# print(lista_a)

########### PARTE 5 ###############
"""
Cuidados com dados mutáveis
= - copiando o valor (imutaveis)
= - aponta para o mesmo valor da memória (mutável)
"""

# nome = 'Pedro'
# noutra_variavel = nome
# nome = 'Carlos'
# print(nome)
# print(noutra_variavel)

lista_a = ['pedro','maria']
lista_b = lista_a
lista_c = lista_a.copy()

lista_a[1] = 'jose'
print(f"lista A: {lista_a},\n"
      f"lista B: {lista_b},\n"
      f"lista C: {lista_c}.")