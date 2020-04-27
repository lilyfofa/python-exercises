jogador = dict()
jogador['Nome'] = str(input('Digite o nome do jogador: '))
jogador ['Gols'] = []
for partida in range(0, int(input('Digite o número de partidas: '))):
    jogador['Gols'].append(int(input(f'Quantos gols ele fez na partida {partida + 1}? ')))
jogador['Total de gols'] = sum(jogador['Gols'])
print('---'*20)
# Primeira forma
print(jogador)
print('---'*20)
# Segunda forma
for k,v in jogador.items():
    print(f'{k}: {v}')
print('---'*20)
# Terceira forma
print(f'O jogador {jogador["Nome"]} jogou {len(jogador["Gols"])} partidas.')
for p, g in enumerate(jogador['Gols']):
    print(f'Na partida {p + 1}, o jogador fez {g} gols.')
print(f'Foi um total de {jogador["Total de gols"]} gols.')