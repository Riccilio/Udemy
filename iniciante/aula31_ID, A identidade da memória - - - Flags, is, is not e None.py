'''
Flag (Bandeira) - Marcar um local
None = Não valor
is e is not = é ou não é (tipo, valor, identidade)
id = Identidade
'''


# v1 = 'a'
# v2 = 'a'
# v3 = 'b'
#
# print(id(v1))
# print(id(v2))
# print(id(v3))


condicao = True
passou_no_if = None

if condicao:
    passou_no_if = True
    print('Faça algo')
else:
    print('não faça algo')

if passou_no_if is None:
    print('Não passou no if')
else:
    print('passou no if')



print(passou_no_if, passou_no_if is None)
print(passou_no_if, passou_no_if is not None)