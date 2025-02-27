"""

Faça um jogo para o usuário adivinhar qual
a palavra secreta.

- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.

- Quando o usuário digitar uma letra, você
vai conferir se a letra digitada está
na palavra secreta.

    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;

    - Se a letra digitada não estiver
    na palavra secreta; exiba *.

Faça a contagem de tentativas do seu
usuário.

"""


print('jogo da palavra secreta!\n'
      'nesse jogo você deve adivinhar a palavra secreta.\n'
      'as regras são: \n'
      '\n'
      '1* você só pode tentar pela mesma quantidade de letras que a palavra secreta tem!\n'
      '2* todas as letras são minusculas\n')

palavra_secreta = 'runescape'
tamanho_palavra_secreta = len(palavra_secreta)
j = 0
print(f'a palavra secreta tem um tamanho de {tamanho_palavra_secreta} letras')
for i in palavra_secreta:
    tentativa_usuario = input('tente adivinhar alguma letra da palavra: ')
    if tentativa_usuario in palavra_secreta:
        print(f'a palavra secreta contem a letra: "{tentativa_usuario}"\n'
              f'a palavra secreta tem a letra "{tentativa_usuario}" {palavra_secreta.count(tentativa_usuario)} vezes')
        while j < tamanho_palavra_secreta:
            letra = palavra_secreta[j]
            if letra == tentativa_usuario:
                print(f'a sua letra aparece na posição da palavra: {j+1}')
            j += 1
    if tentativa_usuario not in palavra_secreta:
        print(f'a palavra secreta não contem a letra: {tentativa_usuario}')
else:
    print('suas chances acabaram!!! pronto para adivinha a palavra secreta?')

tentativa_final = input('Qual a Palavra secreta?')
if tentativa_final == palavra_secreta:
    print('parabens, voce ganhou!')
elif tentativa_final != palavra_secreta:
    print('voce não acertou.')
else:
    print('este print não deveria ocorrer.')










