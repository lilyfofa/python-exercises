r = int(input('Digite a razão: '))
a1 = int(input('Digite o primeiro termo da PA: '))
an = 0
n = 1
while n <= 10:
    print(a1 + (n-1) * r, end=' - ')
    n += 1
print('Fim')