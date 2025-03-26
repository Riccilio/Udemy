"""
argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
argumento não nomeado recebe apenas o argumento (valor):
"""

#definião da função
def soma(x,y,z):
    print(f'{x=} y={y} {z=}', '|', 'x + y + z =',x + y + z)

soma(1, 2, 3)
soma(2, 1, 0)
soma(y=4,z=5 ,x=3)
soma(1, 2, z=5) #apos um argumento nomeado ('z='5) todos os proximos devem ser nomeados!