"""
enumerate - enumera iteraveis (indices)
"""

lista = ['Maria', 'Robson', 'Luiz']
lista.append('joão')

# lista_enumerada= enumerate(lista)
# print(lista_enumerada)
#
# for item in lista_enumerada:
#     print(item)
#
# print(lista_enumerada)

for item in enumerate(lista):
    indice, nome = item
    print(indice, nome)

for indice, nome in enumerate(lista):
    print(indice, nome)

for item in enumerate(lista):
    print('FOR da tupla:')
    for valor in item:
        print(f'{valor}\t')


lista_enumerada_convertida = list(enumerate(lista))
print(lista_enumerada_convertida)