numeros = []
pares = []
impares = []
while True:
    numero = int(input('Digite um valor: '))
    numeros.append(numero)
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)
    if input('Deseja continuar? (S/N) ') in 'Nn':
        break
print(f'Você digitou os valores: {numeros}')
print(f'Os números pares são: {pares}')
print(f'E os números ímpares são {impares}')