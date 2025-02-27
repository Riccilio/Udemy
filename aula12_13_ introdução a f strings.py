nome = 'Ledro Peme'
altura = 1.85
peso = 100
imc = peso / (altura * altura)

# Ledro Peme tem 1.85 de altura,
# pesa 100 quilos e seu IMC é
# 29.2
# IMC = peso / (altura x altura)
mensagem = (f"Ledro Peme tem {altura} m de altura, pesa {str(peso)} quilos.\n"
            f"Por isso, seu IMC é: {str(imc)}")
print(mensagem)