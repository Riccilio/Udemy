"""
Exercício
peça ao usuário para digitar seu nome
peça ao usuário para digitar sua idade
se nome e idade forem digitados:
    exiba:
        seu nome é {nome}
        seu nome invertido é {nome invertido}
        se nome contem (ou não) espaços
        seu nome tem {n} letras
        a primeira letra do seu nome é {letra}
        a ultima letra do seu nome é {letra}
se nada for digitado em nome ou idade:
    exiba:
        "desculpe, você deixou campos vazios"
"""


nome = input("Digite seu nome: ")
idade = str(input("Digite sua idade: "))

if nome and idade:
    print(f"seu nome é {nome}")
    print(f"seu nome invertido é: {nome[::-1]}")
    if " " in nome:
        print("seu nome contem espaços")
    elif " " not in nome:
        print("seu nome NÃO contem espaços")
    print(f"seu nome contem {len(nome)} letras")
    print(f"a primeira letra do seu nome é {nome[0]}")
    print(f"a ultima letra do seu nome é {nome[-1]}")
else:
    print("você deixou campos vazios")