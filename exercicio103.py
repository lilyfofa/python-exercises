# def jogador(nome, gols):
#     if nome == '':
#         nome = '<desconhecido>'
#     if gols == '':
#         gols = 0
#     else:
#         int(gols)
#     return f'O jogador {nome} fez {gols} gols no campeonato.'
#
#
# player = str(input('Jogador: '))
# goals = str(input('Númro de gols: '))
# print(jogador(player, goals))


def jogador(nome='<desconhcido>', gol=0):
    return f'O jogador {nome} fez {gol} gols.'



name = input('Nome: ')
goals = str(input('Número de gols: '))
if goals.isnumeric():
    goals = int(goals)
else:
    goals = 0
if name == '':
    print(jogador(gol=goals))
else:
    print(jogador(name, goals))