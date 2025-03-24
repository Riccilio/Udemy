"""
Formatação básica de strings
s - string
d - int
f - float
.<número de dígitos>f


x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - esquerda
< - direita
^ - centro
= - força o numero a aparecer antes dos zeros

Sinal - + ou -
ex.: 0>-100,.1f

conversion flags - !r !s !a
"""

variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel:@>10}')
print(f'{variavel:@<10}')
print(f'{variavel:@^10}')
print(f'|{variavel: ^10}|')
print(f'{1000.48736:,.1f}')
print(f'{1000.48736:+,.1f}')
print(f'{1000.48736:0=+10,.1f}')
print(f'O hexadecimal de 1500 é {1500:08X}')

print(f'{variavel!r}')# chama o metodo __repr__
print(f'{variavel!s}')# chama o metodo __str__
print(f'{variavel!a}')# chama o metodo __ask__



