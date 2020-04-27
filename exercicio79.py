lista = []
while True:
    numero = int(input('Digite um número: '))
    if numero not in lista:
        lista.append(numero)
    else:
        print('Esse valor já existe, logo não vou adicionar!')
    continuar = input('Deseja continuar (S/N): ')
    if continuar in 'Nn':
        break
print(f'Você digitou os valores: {sorted(lista)}')