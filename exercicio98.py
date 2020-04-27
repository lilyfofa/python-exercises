from time import sleep


def contagem(inicio, fim, passo):
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    print('---'*20)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}.')
    if fim > inicio:
        while fim >= inicio:
            print(inicio, end=' ')
            sleep(0.5)
            inicio += passo
    else:
        while inicio >= fim:
            print(inicio, end=' ')
            sleep(0.5)
            inicio -= passo
    print('FIM')


contagem(1, 10, 1)
contagem(10, 0, 2)
print('---'*20)
print('Agora é sua vez de criar a contagem!')
print('---'*20)
contagem(int(input('Início: ')), int(input('Fim: ')), int(input('Passo: ')))
