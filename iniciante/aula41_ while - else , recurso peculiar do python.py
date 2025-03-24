"""while / else
o else é executado toda vez que o while termina de iterar o codigo.

ao encontrar um break, o codigo pula o else.
"""
string = 'valor qualquer'

i = 0

while i < len(string):
    letra = string[i]
    print(letra)
    i += 1
    if letra == '':
        break
else:
    print('print dentro do while')



print('fora do while.')
