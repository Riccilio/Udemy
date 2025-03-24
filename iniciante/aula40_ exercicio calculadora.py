"""
calculadora com while
"""

while True:

    operadores_permitidos = '+-*/'

    primeiro_numero_str = input('insira o primeiro número: ')
    try:
        primeiro_numero_float = float(primeiro_numero_str)
    except:
        print('insira um número válido.')
        continue

    operador = input('insira a operação a ser realizada(+-*/) ')
    if operador not in operadores_permitidos or len(operador) > 1:
        print('insira um operador válido')
        continue

    segundo_numero_str = input('insira o número que operará o primeiro número: ')
    try:
        segundo_numero_float = float(segundo_numero_str)
    except:
        print('insira um número válido.')
        continue

    if operador =='+':
        resultado = primeiro_numero_float + segundo_numero_float

    elif operador =='-':
        resultado = primeiro_numero_float - segundo_numero_float

    elif operador =='*':
        resultado = primeiro_numero_float * segundo_numero_float

    elif operador =='/':
        resultado = primeiro_numero_float / segundo_numero_float
    else:
        print('não era pra isso acontecer')


    print(resultado)

    sair = input('Quer sair? [s]im: ').lower().startswith('s')
    if sair:
        break
