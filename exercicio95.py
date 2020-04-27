jogadores = list()
while True:
    jogador = dict()
    jogador['Nome'] = str(input('Digite o nome do jogador: '))
    jogador ['Gols'] = []
    for partida in range(0, int(input('Digite o número de partidas: '))):
        jogador['Gols'].append(int(input(f'   Quantos gols ele fez na partida {partida + 1}? ')))
    jogador['Total'] = sum(jogador['Gols'])
    jogadores.append(jogador)
    if str(input('Deseja continuar? (S/N) ')).title() in 'N':
        print('---'*20)
        break
    print('---'*20)
# for p, j in enumerate(jogadores):
#     print(f'Código = {p + 1}; ', end='')
#     for k, v in j.items():
#         print(f'{k} = {v}; ', end='')
#     print()
print('Cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
for k, v in enumerate(jogadores):
    print(f'{k + 1:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('---'*20)
while True:
    numero = int(input('Digite o código do jogador para ver seus dados: (-1 para terminar) '))
    if numero == -1:
        print('---'*20)
        break
    if numero > len(jogadores):
        print('Erro. Não existe esse código!')
    else:
        for p, v in enumerate(jogadores[numero - 1]['Gols']):
            print(f'   No jogo {p + 1}, o jogador {jogadores[numero - 1]["Nome"]} fez {v} gol(s).')
    print('---'*20)
