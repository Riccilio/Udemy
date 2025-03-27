"""
args - Argumentos não nomeados
* - *args (empacotamento e desempacotamento)
"""
# lembrete de desempacotamento
# x, y, *resto = 1, 2, 3, 4
# print(x, y, resto)


# def soma(*args):
#     total = 0
#     for numero in args:
#         total += numero
#         print(numero, total)
#
# print(soma(1, 2,3,4,5,6))


def soma(*args):
    total = 0
    for numero in args:
        total += numero
    return total

# soma_1 = soma(1,2,3)
# print(soma_1)
# soma_2 = soma(4,5,6)
# print(soma_2)
# outra_soma= soma(1,2,3,4,5,6,7)
# print(outra_soma)

numeros = 1,2,3,4,5,6,7
print('ultimo print',sum(numeros))

print(*numeros)
