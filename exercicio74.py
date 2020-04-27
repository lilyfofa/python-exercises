import random
numeros = (1,2,3,4,5,6,7,8,9,10)
contador = 0
menor = 0
maior = 0
print('Os números sorteados foram: ',end='')
for c in range(0,5):
    numero = numeros[random.randint(0,9)]
    print(numero, end=' ')
    if contador == 0:
        menor = maior = numero
    else:
        if numero > maior:
            maior = numero
        elif numero < menor:
            menor = numero
    contador += 1
print(f'\nO maior número foi {maior} e o menor foi {menor}.')