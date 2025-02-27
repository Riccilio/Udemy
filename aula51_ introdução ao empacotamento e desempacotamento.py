"""
introdução ao desempacotamento
_ == concordancia entre programadores sobre a variavel usada para armazenar dados desnecessários.
"""
lista = ['Maria','Helena', 'Luiz']

nome1, nome2, nome3 = lista
_, nome4, *_=lista
print(nome2)
print(nome4)
