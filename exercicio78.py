numeros = []
for c in range(0,5):
    numero = int(input(f'Digite um número para a posição {c}: '))
    numeros.append(numero)
print(f'Você digitou os valores: {numeros}')
print(f'O maior número é {max(numeros)}, digitado nas posições: ',end='')
for p, c in enumerate(numeros):
    if c == max(numeros):
        print(p,end=' ')
print()
print(f'O menor número é {min(numeros)}, digitado nas posições: ',end='')
for p, c in enumerate(numeros):
    if c == min(numeros):
        print(p,end=' ')
