def ajuda():
    from time import sleep

    def visual(frase, codigo):
        print(f'\033[{codigo}m', end='')
        print('-' * (len(frase) + 20))
        print(' ' * 10 + frase)
        print('-' * (len(frase) + 20))
        print('\033[m', end='')

    while True:
        visual('Ajuda com o Python', '1;30;44')
        msg = input('Função ou biblioteca: ')
        if msg.upper() == 'FIM':
            titulo = 'Até mais'
            visual(titulo, '1;30;45')
            break
        sleep(0.5)
        titulo = f'Procurando sobre {msg}'
        sleep(1)
        visual(titulo, '1;30;41')
        sleep(1)
        print(f'\033[7:30m{msg.__doc__}')
        print('\033[m', end='')
        sleep(1)

ajuda()
