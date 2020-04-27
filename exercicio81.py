contador = 0
lista = []
while True:
    numero = int(input('Digite um valor: '))
    contador += 1
    lista.append(numero)
    if input('Deseja continuar? (S/N) ') in 'Nn':
        break
print(f'Você digitou {contador} valor(es).')
print(f'Você digitou a lista {sorted(lista,reverse=True)}')
if 5 in lista:
    print('O número 5 aparece na lista!')
else:
    print('O número 5 não aparece na lista!')