import math
n = int(input('Digite um número: '))
#print('O dobro do número {} é igual a {}. Seu triplo equivale a {}. Sua raiz quadrada vale {}.'.format(n,(n*2),(n*3),math.sqrt(n)))
print(f'O dobro do número {n} é {n*2}, o triplo vale {n*3} e sua raiz quadrada equivale a {pow(n,1/2)}')



