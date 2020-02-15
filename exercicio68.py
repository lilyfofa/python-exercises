from random import randint
vitorias = 0
print('---'*20)
print('Par ou ímpar')
print('---'*20)
while True:
    computador = randint(0, 10)
    usuario = int(input('Digite um número para competir com o computador: '))
    if usuario > 10 or usuario < 0:
        print('---' * 20)
        print('Digite um número entre 0 e 10!')
        break
    soma = computador + usuario
    pi = ''
    while pi not in 'PI':
        pi = str(input('Par ou ímpar [P/I]: ')).upper()
    if pi == 'P':
        if soma % 2 != 0:
            print(f'Você perdeu! Você jogou {usuario} e o computador {computador}. A soma deu {soma}, que é ímpar.')
            break
        if soma % 2 == 0:
            print(f'Você venceu! Você jogou {usuario} e o computador {computador}. A soma deu {soma}, que é par.')
            vitorias += 1
            print('---' * 20)
    if pi == 'I':
        if (computador + usuario) % 2 == 0:
            print(f'Você perdeu! Você jogou {usuario} e o computador {computador}. A soma deu {soma}, que é par.')
            break
        if (computador + usuario) % 2 != 0:
            print(f'Você venceu! Você jogou {usuario} e o computador {computador}. A soma deu {soma}, que é ímpar.')
            vitorias += 1
            print('---' * 20)
print('---'*20)
print(f'Tente novamente! Você venceu {vitorias} vez(es).')
