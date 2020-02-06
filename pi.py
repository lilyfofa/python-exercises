from decimal import *
print('\033[1:31m---'*30+'\nFilósofo Pithon\n'+'---'*30+'\033[m')
casas = int(input('\033[1:30mPor favor, digite a quantidade de casas decimais para números irracionais: '))
getcontext().prec= casas + 1
numero = int(input('Digite um número inteiro (quanto maior o número, maior será a precisão: '))
positivos = 0
negativos = 0
for c in range(1, numero, 4):
     positivos = positivos + (Decimal(1)/Decimal(c))
for c in range(3, numero, 4):
     negativos = negativos - (Decimal(1)/Decimal(c))
print(f'O valor de π calculado é {(positivos + negativos)*4}.\033[m\n'+'\033[1:31m---'*30)
