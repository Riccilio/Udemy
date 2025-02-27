"""
introdução ao try/except
try -> tentar executar o código
except - > ocorreu algum erro ao tentar executar
"""

numero_str = input("vou dobrar o número que for inserido: ")

try:
    print('STR: ', numero_str)
    numero_float = float(numero_str)
    print('FLOAT: ', numero_float)
    print(f"o dobro de {numero_str} é {numero_float*2:.2f}")
except:
    print('isso não é um número')

# if numero_str.isdigit(): #função isdigit verifica se o valor é um numero INTEIRO
#     numero_float = float(numero_str)
#     print(f"o dobro de {numero_str} é {numero_float*2:.2f}")
# else:
#     print("valor inserido não é um número inteiro")