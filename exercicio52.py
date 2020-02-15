import math
from time import perf_counter
from tqdm import tqdm
#num = int(input('Digite um número: '))
inicio = perf_counter()
contador = 0
# for c in range (1, num + 1):
num = math.factorial(30) + 13
for c in tqdm(range(1, num + 1)):
    if num % c == 0:
        print(f'\033[30m{c}\033[m', end =' ')
        contador += 1
    else:
        print(f'\033[31m{c}\033[m', end=' ')
fim = perf_counter()
print(f'\nO número foi divisível {contador} vezes.')
if contador > 2:
    print('O número não é primo.')
else:
    print('O número é primo.')
print(f'A tarefa demorou {round(fim - inicio)} segundos.')



