print("---"*15+'\nAluguel de Carros\n'+"---"*15)
d = int(input('Por quantos dias você utilizou o carro? '))
k = int(input('Quantos quilômetros foram rodados? '))
print(f'Você deverá pagar R${60*d+0.15*k:.2f}.\n'+'---'*15)
