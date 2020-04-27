from random import randint
from time import sleep
lista = []


def sorteio():
    print('Sorteando 5 valores: ')
    for _ in range(0,5):
        numero = randint(1, 10)
        print(numero, end=' ')
        lista.append(numero)
        sleep(0.5)
    print()

def par():
    par = 0
    print('Os números pares são:')
    for v in lista:
        if v % 2 == 0:
            par += v
            print(v, end=' ')
            sleep(0.5)
    print(f'\nA soma dos pares equivale a {par}.')

sorteio()
par()