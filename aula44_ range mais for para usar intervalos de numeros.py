"""
for + range
range -> range (start, stop, step)
start = de onde começa a contar
stop = onde para de contar (este valor não é incluido)
step = de quantos em quantos ele conta
"""

# numeros = range(10)
# numeros = range(5, 10)
# numeros = range(5, 10, 2)
numeros = range(0, -10, -1)
# print(numeros[2])

for numero in numeros:
    print(numero)