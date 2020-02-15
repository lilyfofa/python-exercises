casa = float(input('Qual o valor da casa? '))
salario = float(input('Qual o salário do comprador? '))
tempo = int(input('Quantos anos vai durar o financiamento? '))
if casa/(tempo * 12) > (salario * 0.3):
    print(f'O empréstimo foi NEGADO, já que a parcela será de R${casa/(tempo*12):.2f}, enquanto o salário é de R${salario}')
else:
    print(f'O empréstimo foi aprovado, com uma parcela mensal de R${casa/(tempo*12):.2f}')