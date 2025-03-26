"""
Escopo de funções em Python
Escopo significa o local onde aquele código pode atingir.
Existem os escopos global e local.
O escopo global é o escopo onde todo o código é alcançavel
O escopo local é o escopo onde apenas nomes do mesmo local podem ser alcançados
"""

x = 1

def escopo():
    x= 10
    def outra_funcao():
        y = 2
        print(x , y)

    outra_funcao()
    print(x)


escopo()