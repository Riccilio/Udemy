"""
Operadores in e not in
Strings são iteráveis

 0 1 2 3 4
 P e d r o
 -5-4-3-2-1
"""
#
# nome = 'Pedro'
# print(nome[2]) # acessa a letra 'd'
# print(nome[3]) # acessa a letra 'r'
# print(nome[-1]) # acessa a letra 'o'
# print('e' in nome)# checa letras e silabas no 'nome'
# print('a' in nome)
# print('dro' in nome)
# print(100 * '-')
#
# print('' not in nome) # GRANDE OBSERVAÇÃO:
# # Uma string vazia ('') sempre estará presente em qualquer string, por isso retorna True

nome = input('Qual seu nome? ')
procurar = input('O que você deseja procurar? ')

if procurar in nome:
    print(f'{procurar} está em {nome}')
elif procurar not in nome:
    print(f'{procurar} não está em {nome}')






