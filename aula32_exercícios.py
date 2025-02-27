"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
# entrada = input('insira um número inteiro: ')
# if entrada.isdigit():
#     par_ou_impar = entrada % 2
#     if par_ou_impar == 0:
#         print('é par')
#     else:
#         print('é impar')
# else:
#     print('digite um numero inteiro')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
# entrada = input('digite a hora em números inteiros: ')
#
# try:
#     hora = int(entrada)
#     if hora == 0 and hora <=11:
#         print('bom dia')
#     elif hora >=12 and hora <=17:
#         print('boa tarde')
#     elif hora >=18 and hora <=23:
#         print('boa noite')
#     else:
#         print('digite uma hora válida')
# except:
#     print('digite um numero')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
nome = input('qual o seu primeiro nome? ')
tamanho_nome = len(nome)
if tamanho_nome > 1:
    if tamanho_nome <= 4:
        print('pequeno')
    elif tamanho_nome >= 5 and tamanho_nome <= 6:
        print('normal')
    elif tamanho_nome > 6:
        print('grandao')
else:
    print('digite um nome valido')

