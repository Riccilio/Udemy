"""
exercicios com funções

crie uma função que multiplica todos os argumentos
não nomeados recebidos
retorne o total para uma variavel e mostre o valor da variavel

crie uma função fala se um numero é par ou impar.
retorne se o numero é par ou impar
"""

def multiplicacao(*args):
    total = 0
    for multiplicador in args:
        if total == 0 or total == 1:
            total = multiplicador
            continue
        total *= multiplicador
    return total

def par_ou_impar(numero):
    #return numero % 2 == 0
    multiplo_de_dois = numero % 2 == 0
    if multiplo_de_dois:
        return 'É Par'
    return 'É Impar'


print(par_ou_impar(2834756146514635136514))



numeros = 0,1,2,3,4,5,6,7,8
print(multiplicacao(*numeros))
print(2*3*4*5*6*7*8)
