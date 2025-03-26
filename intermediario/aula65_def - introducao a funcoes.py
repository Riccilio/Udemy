"""
introdução às funções (def) em Python
funções são trechos de código usados para
replicar determinada ação ao longo do seu código.
Elas podem receber valores para parametros (argumentos)
e retornar um valor específico.
Por padrão, funções Python retornam None (nada).
"""
# def imprimir(a, b, c):
#     print(a)
#     print(b)
#     print(c)
#
# imprimir(1, 2, 3)
# imprimir(4, 5, 6)


def saudacao(nome='Sem nome'):
    print(f'Olá, {nome}')

saudacao('Pedro Leme')
saudacao('Gabriela')
saudacao()

