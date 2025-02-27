#ORDEM DE IMPORTANCIA DE NUMERADORES (PRECEDENCIA MAIS FORTE)
# 1. (n+n) parenteses
# 2. ** potenciação
# 3. * / // % multiplicação, divisão, divisão verdadeira e módulo
# 4. + - adição e  subtração

conta_1 = 1 + 1 ** 5 + 5
conta_2 = (1 + (0.5 + 0.5)) ** (5 + 5)
print(conta_1)
print(int(conta_2))