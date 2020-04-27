import random
import time
jogos = int(input('Quantos jogos quer que eu sorteie? '))
lista = []
for c in range(0, jogos):
    lista.append(list())
    for _ in range(0, 6):
        valor = random.randint(1,60)
        while valor in lista[c]:
            valor = random.randint(1,61)
        lista[c].append(valor)
    print(f'Jogo {c + 1}: {sorted(lista[c])}')
    time.sleep(1)
