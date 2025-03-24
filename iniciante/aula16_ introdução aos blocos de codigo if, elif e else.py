# if /    elif   / else
# se / se não se / se não

entrada = input('você quer entrar ou sair?')

if entrada == 'entrar':
    print('entrou')
elif entrada == 'sair':
    print('saiu')
else :
    print('você não digitou nem entrar e nem sair')

print('este print é fora de qualquer if/elif/else')