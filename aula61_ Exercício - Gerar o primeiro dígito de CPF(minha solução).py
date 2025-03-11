"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados:
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""

lista_resultados = []
cpf = input('Insira o CPF com pontuação: ')
cpf_sem_ponto = cpf.replace('.', '')
cpf_split = cpf_sem_ponto.split('-')
cpf_primeira_parte = cpf_split[0]
cpf_segunda_parte = cpf_split[1]
print(cpf, cpf_sem_ponto, cpf_split, cpf_primeira_parte, cpf_segunda_parte )

multiplicador = 10
for iterador, numero in enumerate(cpf_primeira_parte):
    numero_int = int(numero)
    resultado = numero_int * multiplicador
    lista_resultados.append(resultado)
    multiplicador -= 1
    if iterador + 1 == len(cpf_primeira_parte):
        break

soma_resultados = sum(lista_resultados)
soma_resultados_multiplicados_por_10 = soma_resultados * 10
resto_divisão_soma_resultados_multiplicados = soma_resultados_multiplicados_por_10 % 11
if resto_divisão_soma_resultados_multiplicados > 9:
    print(f'Resultado final do primeiro dígito confirmador do CPF: 0')
else:
    print(f'Resultado final do primeiro dígito confirmador do CPF: {resto_divisão_soma_resultados_multiplicados}')





