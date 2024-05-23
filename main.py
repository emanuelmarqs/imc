nome = input('Digite seu nome:')
peso = str(input('Digite seu peso')).replace(',','.')
peso = float(peso)
altura = str(input("Digite sua altura: ")).replace(',','.')
altura = float(altura)
imc = str(peso/(altura**2)).replace(',','.')
imc = float(imc)

print(f'{imc:,.2f}') #exibe o imc com apenas 2 casas decimais.

if imc < 17:
    print(f"{nome} você está muito abaixo do peso.")
elif imc <= 18.5:
    print(f"{nome} você está abaixo do peso.")
elif imc <= 25:
    print(f"{nome} você está no peso ideal.")
elif imc <= 30:
    print(f"{nome} você está acima do peso.")
elif imc <= 35:
    print(f"{nome} você é obeso Grau I")
elif imc < 40:
    print(f"{nome} você é obeso Grau II")
else:
    print(f'{nome} você tem obesidade grau III.')




