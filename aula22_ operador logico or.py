"""
Operadores lógicos
and (e) // or (ou) // not (não)

or - Qualquer condição verdadeira avalia toda a expressão como verdadeira.

Se qualquer valor for considerado verdadeiro, a expressão inteira será avaliada naquele valor.

São considerados falsy(que vc já viu)
0 // 0.0 // '' // False

Também existe o tipo None que é usado para representar um não valor.
"""

#
# entrada = input('[E]ntrar [S]air: ')
# senha_digitada = input('Senha: ')
# senha_permitida = '123456'
#
#
# if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
# #nota do if:
# #   caso comece a ter muitas condições em um IF, separar as condições por parenteses pode ajudar.
#     print('entrar')
# else:
#     print('sair')
#


#avaliação de curto circuito
print(True or False)
print(True or False or 0)
print(True or False or 0 or 'abc')
print(False or 0 or 0.0 or '' or 'abc')
print(False or 0 or 0.0 or '' or 'abc' or True)


senha = input('Senha: ') or 'SEM SENHA'
print(senha)