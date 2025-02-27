"""
Operadores lógicos
and (e) // or (ou) // not (não)

and - todas as condições precisam ser verdadeiras.
Se qualquer valor for considerado falso, a expressão inteira será avaliada naquele valor.

São considerados falsy (já estudados)
0 // 0.0 // '' // False

Também existe o tipo None que é usado para representar um não valor.
"""


entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')
senha_permitida = '123456'


if entrada == 'E' and senha_digitada == senha_permitida:
    print('entrar')
else:
    print('sair')


#avaliação de curto circuito
print(True and True and True)
print(True and False and True)
print(True and 0 and True)
print(True and 0.0 and True)
print(True and '' and True)
