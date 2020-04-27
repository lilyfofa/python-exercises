lista = [[], [], []]
pares = terceira = maior = 0
for c in range(0, 3):
    for i in range(0,3):
        valor = int(input(f'Digite o valor para [{c},{i}]: '))
        lista[c].append(valor)
        if valor % 2 == 0:
            pares += valor
        if i == 2:
            terceira += valor
        if c == 1:
            if i == 0:
                maior = valor
            else:
                if valor > maior:
                    maior = valor
for a in range(0,3):
    for b in range(0,3):
        print(f'[{lista[a][b]:^5}]',end=' ')
    print()
print(f'A soma de todos os valores pares é {pares}.')
print(f'A soma dos valores da terceira coluna é {terceira}')
print(f'E o maior valor da segunda linha é {maior}.')
