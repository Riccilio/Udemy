"""
Fatiamento de strings
 012345678
 olá mundo
-987654321
fatiamento [i:f:p] [::]

obs.: a função len retorna a qtd de caracteres na string
"""

variavel = 'olá mundo'
print(variavel[5]) #printa u de olá mundo
print(variavel[-4]) #printa u de olá mundo
print(variavel[4:]) #printa os caracteres do 4 ao final
print(variavel[4:7]) #printa os caracteres do indice 4 a 7
print(variavel[0:5]) #printa os caracteres do indice 0 a 5
print(variavel[-2:-8])
print(len(variavel[-9:8]))

print(variavel[0:len(variavel):1]) #o numero 1 representa o passo. passo é como ele vai pegar os caracteres da string. nesse caso, é de 1 em 1.
print(variavel[0:len(variavel):2]) #o numero 2 representa o passo. passo é como ele vai pegar os caracteres da string. nesse caso, ele pega 1 caracter, e pula outro.
print(variavel[0:len(variavel):3]) #o numero 3 representa o passo. passo é como ele vai pegar os caracteres da string. nesse caso, ele pega 1 caracter, e pula outros 2.
print(variavel[::-1]) #no caso do passo negativo, ele retorna o valor de trás pra frente
print(variavel[::-2]) #no caso do passo negativo, ele retorna o valor de trás pra frente

#observação sobre o fatiamento 4:X ==> o X não é incluso. O fatiamento irá parar no caracter anterior ao indice final.