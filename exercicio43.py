massa = float(input('Por favor, digite a sua massa (kg): ').replace(',','.'))
altura = float(input('Por favor, digite a sua altura (m): ').replace(',','.'))
imc = massa/(altura**2)
if imc < 18.5:
    print(f'Você está na categoria ABAIXO DO PESO, já que seu IMC é igual a {imc:.2F}')
elif 18.5 <= imc < 25:
    print(f'Você está na categoria PESO IDEAL, já que seu IMC é igual a {imc:.2F}')
elif 25 <= imc < 30:
    print(f'Você está na categoria SOBREPESO, já que seu IMC é igual a {imc:.2F}')
elif 30 <= imc <= 40:
    print(f'Você está na categoria OBESIDADE, já que seu IMC é igual a {imc:.2F}')
else:
    print(f'Você está na categoria OBESIDADE MÓBIDA, já que seu IMC é igual a {imc:.2F}')
