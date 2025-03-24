"""
tipo tupla - uma lista imutavel
"""

nomes = 'Maria', 'Robson', 'Luiz'
nomes_list = list(nomes)
nomes_tuple = tuple(nomes)
_, _, nome, *resto = nomes
print(nomes[0])
print(nomes[-1])

print(type(nomes_list), type(nomes_tuple))