from random import randint
from time import sleep
from operator import itemgetter
valores = {}
ordem = []
for c in range (1,5):
    valores[f'J{c}'] = randint(1,6)
for k,v in valores.items():
    print(f'{k} tirou {v} no dado.')
    sleep(0.75)
print('---'*20)
ranking = sorted(valores.items(), key=itemgetter(1), reverse=True)
# c = 1
# for p in ranking:
#     print(f'{c}° lugar: {p[0]}, que tirou {p[1]}.')
for p, v in enumerate(ranking):
    print(f'{p + 1}° lugar: {v[0]}, que tirou {v[1]}.')