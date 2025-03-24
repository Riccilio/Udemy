"""
Interpolação básica de strings
s - string
d e i - int
f = float
x e X = Hexadecimal (ABCDEF0123456789)
"""

nome = 'pedro'
preco = 100.95897643
variavel = '%s, o preço é R$%f' % (nome, preco)
print(variavel)
print('O hexadecimal de %d é %04X' %(1500, 1500))

#não sei pra que server interpolação de strings.