"""
https://docs.python.org/pt-br/3/library/stdtypes.html
Imutáveis que vimos: str, int, float, bool
"""
string = 'Pedro Leme'
outra_string = f'{string[:3]}ABC{string[4:]}'
#.zfill
#.capitalize
#etcetera

# string[3] = 'abc' #não é possivel mudar o valor de uma string, pois é IMUTAVEL
print(outra_string)
