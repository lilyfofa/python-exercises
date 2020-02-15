contador = 3
a = 0
b = 1
numero = int(input('Quantos termos quer que o programa mostre? '))
print(f'{a} - {b} ', end=' - ')
while numero >= contador:
    c = a + b
    print(c, end=' - ')
    contador += 1
    a = b
    b = c
print('FIM')