lista = [[], [], []]
for c in range(0, 3):
    for i in range(0,3):
        lista[c].append(int(input(f'Digite o valor para [{c},{i}]: ')))
for a in range(0,3):
    for b in range(0,3):
        print(f'[{lista[a][b]:^5}]',end=' ')
    print()
