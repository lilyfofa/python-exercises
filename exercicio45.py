import random
from time import sleep
# Poderia ter usado o randint para escolher um item de uma lista com range [0,1,2]
# lista = ['Papel', 'Pedra', 'Tesoura']
computador = random.randint(1,3)
# Pedra - 1
# Papel - 2
# Tesoura - 3
print('Digite o número referente a sua jogada:\n[1] Pedra\n[2] Papel\n[3] Tesoura')
usuario = int(input('Digite o número: '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!')
if usuario < 1 or usuario > 3:
    print('Jogada inválida. Tente novamente.')
elif computador == usuario:
    print('Vocês empataram!', end=' ')
    if computador == 1:
        print('Vocês dois jogaram PEDRA!')
    elif computador == 2:
        print('Vocês dois jogaram PAPEL!')
    elif computador == 3:
        print('Vocês doi jogaram TESOURA')
elif computador == 1 and usuario == 3 or computador == 2 and usuario == 1 or computador == 3 and usuario == 2:
    print('O computador VENCEU. ', end='')
    if computador == 1:
        print('O computador jogou PEDRA. ', end='')
    elif computador == 2:
        print('O computador jogou PAPEL. ', end='')
    elif computador == 3:
        print('O computador jogou TESOURA. ', end='')
    if usuario == 1:
        print('Você jogou PEDRA.')
    elif usuario == 2:
        print('Você jogou PAPEL.')
    elif usuario == 3:
        print('Você jogou TESOURA.')
else:
    print('Você VENCEU! ', end= '')
    if computador == 1:
        print('O computador jogou PEDRA. ', end='')
    elif computador == 2:
        print('O computador jogou PAPEL. ', end='')
    elif computador == 3:
        print('O computador jogou TESOURA. ', end='')
    if usuario == 1:
        print('Você jogou PEDRA.')
    elif usuario == 2:
        print('Você jogou PAPEL.')
    elif usuario == 3:
        print('Você jogou TESOURA.')
