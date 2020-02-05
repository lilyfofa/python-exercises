print('---'*20+'\nPardal do Python\n'+'---'*20)
velocidade = int(input('Qual era a sua velocidade em km/h? '))
if velocidade <= 80:
    print('Ufa! Vocẽ não terá de pagar multa alguma!\n'+'---'*20)
else:
    print(f'Ah! Você foi multado. Terá que pagar R${(velocidade - 80)*7}.\n'+'---'*20)




