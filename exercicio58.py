from random import randint
computador = randint(0,10)
print('O computador acaba de escolher um número entre 0 e 10. Você consegue adivinhá-lo?')
usuario = int(input('Qual é seu palpite: '))
contador = 1
while usuario != computador:
    contador += 1
    if usuario > computador:
        print('Menos... Tente novamente.')
    if usuario < computador:
        print('Mais... Tente novamente.')
    usuario = int(input('Seu palpite: '))
if usuario == computador:
    print(f'Parabéns! Você acertou após {contador} tentativa(s).')