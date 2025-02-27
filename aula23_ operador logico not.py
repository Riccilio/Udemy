"""
Operadores lógicos
and (e) // or (ou) // not (não)

not - usado para inverter expressões

not True = False
not False = True
"""

senha = input('senha: ')

if not senha:
    print('sem senha')
elif senha == '123456':
    print('entrou')
else:
    print('Senha incorreta.')

print(not 0) # False
print(not 1) # True


