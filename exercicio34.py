print('---'*20+'\nCálculo do reajuste salarial\n'+'---'*20)
salario = float(input('Digite o salário do funcionário: '))
if salario <= 1250:
    print(f'O salário com reajuste será de R${salario * 1.15:.2f}.\n'+'---'*20)
else:
    print(f'O sálario com reajuste será de R${salario * 1.1:.2f}.\n'+'---'*20)
