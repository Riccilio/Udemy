"""
Exercício
Exiba os índices da lista

_ == concordancia entre programadores sobre a variavel usada para armazenar dados desnecessários.
"""
lista = ['Maria','Helena', 'Luiz']

indices = range(len(lista))
for indice in indices:
    print(indice, lista[indice], type(lista[indice]))