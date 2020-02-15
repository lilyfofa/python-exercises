r = int(input('Digite a razão: '))
a1 = int(input('Digite o primeiro termo da PA: '))
for c in range(1,11):
    print(a1 + (c - 1) * r, end=' - ')
print('Fim')