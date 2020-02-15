print('---'*30+'\nMaior e menor valor\n'+'---'*30)
primeiro = int(input('Por favor, digite um número: '))
segundo = int(input('Por favor, digite outro número: '))
terceiro = int(input('Por favor, digite outro número: '))
if primeiro > segundo > terceiro:
    print(f'O número {primeiro} é o maior e o número {terceiro} é o menor.\n'+'---'*30)
elif primeiro > terceiro > segundo:
    print(f'O número {primeiro} é o maior e o número {segundo} é o menor.\n'+'---'*30)
elif segundo > primeiro > terceiro:
    print(f'O número {segundo} é o maior e o número {terceiro} é o menor.\n'+'---'*30)
elif segundo > terceiro > primeiro:
    print(f'O número {segundo} é o maior e o número {primeiro} é o menor.\n'+'---'*30)
elif terceiro > primeiro > segundo:
    print(f'O número {terceiro} é o maior e o número {segundo}.\n'+'---'*30)
else:
    print(f'O número {terceiro} é o maior e o número {primeiro} é o menor.\n'+'---'*30)
