# contador = 0
lista = []
maior = menor = 0
while True:
    usuario = []
    nome = str(input('Digite o nome da pessoa: '))
    peso = float(input('Digite seu peso: '))
    usuario.append(nome)
    usuario.append(peso)
    lista.append(usuario[:])
    if len(lista) == 0:
        maior = menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso
    usuario.clear()
    # contador += 1
    if input('Deseja continuar? (S/N) ') in 'Nn':
        break
print(f'{len(lista)} pessoas foram cadastradas:')
print(f'O menor peso foi {menor} kg. Peso de: ', end='')
for c in lista:
    if c[1] == menor:
        print(f'[{c[0]}]', end=' ')
print(f'\nO maior peso foi {maior} kg. Peso de: ', end='')
for c in lista:
    if c[1] == maior:
        print(f'[{c[0]}]', end=' ')