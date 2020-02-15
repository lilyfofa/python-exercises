# lista = []
maior = 0
menor = 0
for c in range(1,6):
    peso = float(input(f'Digite o peso da {c}ª pessoa: '))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            peso = menor
print(f'O maior peso foi de {maior} e o menor foi de {menor}')
#     lista.append(peso)
# lista.sort()
# print(f'O maior peso foi de {lista[-1]} e o menor foi de {lista[0]}')