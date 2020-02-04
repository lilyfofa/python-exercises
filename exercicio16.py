#from math import floor as f
#print('---'*15+'\nValor inteiro de um número\n'+'---'*15)
#n = float(input('Digite um número: '))
#print(f'A parte inteira do número {n} é {f(n)}.\n'+'---'*15)
from math import trunc as t
print('---'*15+'\nValor inteiro de um número\n'+'---'*15)
numero = float(input('Digite um número: ').replace(',','.'))
print(f'A parte inteira do número {numero} é {t(numero)}.\n'+'---'*15)