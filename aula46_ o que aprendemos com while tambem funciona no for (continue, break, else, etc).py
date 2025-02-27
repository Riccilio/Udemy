

for i in range(10):
    if i == 2:
        print('i é 2, pulando...')
        continue #retorna para o inicio do laço, linha 3

    if i == 8:
        print('i é 8, seu else não executará')
        break #termina o for loop. o else não será executado pois não terminou naturalmente.

    for j in range(1, 3):
        print(i,j)

else:
    print('For completo com sucesso!')