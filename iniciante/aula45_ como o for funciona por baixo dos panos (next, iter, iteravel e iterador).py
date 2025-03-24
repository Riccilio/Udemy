"""
iterável -> str, range, etc (__iter__)
iterador -> quem sabe entregar um valor por vez
next -> me entregue o proximo valor
iter -> me entregue seu iterador

__iter__() <- os "__" são chamados de dunder. nesse caso, esse método é o dunder iter
__next__() <- dunder next
"""

#texto = 'Pedro'.__iter__()
# texto = iter('Pedro') # .__iter__()
#
# print(texto.__next__())
# print(texto.__next__())
# print(texto.__next__())
# print(texto.__next__())
# print(texto.__next__())
# print(next(texto)) # mesma coisa que o dunder next, mas aqui nesse caso vai apresentar um erro, porque acabaram as iterações em "texto"

#for letra in texto
texto = 'Pedro' # iteravel
iterador = iter(texto) # iterador

while True:
    try:
        letra = next(iterador)
        print(letra)
    except StopIteration:
        break
