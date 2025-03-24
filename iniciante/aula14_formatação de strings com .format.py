a = 'A'
b = 'B'
c = 1.1
string ='a={nome1} b={nome2} c={nome3:.1f}' #:.1f define quantas casa decimais, no caso, 1.
formato = string.format(
    nome1=a,
    nome2=b,
    nome3=c) #parametro nomeado. tudo que vem apos um parametro nomeado deve ser tambem nomeado.
print(formato)
