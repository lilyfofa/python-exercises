km = int(input('Digite o número de quilômetros rodados: '))
print(f'Você deverá pagar R${km*0.5:.2f}.' if km <= 200 else f'Você deverá pagar R${km*0.45:.2f}')