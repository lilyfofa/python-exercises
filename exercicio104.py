def leiaInt(msg):
    while True:
        n = str(input(msg))
        if n.isnumeric():
            return f'Você digitou o número {n}.'
            break
        else:
            print('\033[1:31mErro! Digite um número válido.\033[m')


print(leiaInt('Digite um número: '))