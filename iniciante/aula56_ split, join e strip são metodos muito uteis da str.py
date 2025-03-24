"""
split e join com list e str
split - divide uma string
join - une uma string
"""

frase = '           olha só que, coisa interessante              '
lista_frases_crua = frase.split(',')# caracter escolhido não será incluído na seleção
lista_frases = []
for i, frase in enumerate(lista_frases_crua):
    lista_frases.append(lista_frases_crua[i].strip())

print(lista_frases_crua)
print(lista_frases)
frases_unidas = '-'.join(lista_frases)

print(frases_unidas)

#print(lista_frases_crua[i].rstrip())
#print(lista_frases_crua[i].lstrip())
#print(lista_frases_crua)
