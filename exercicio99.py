from time import sleep


def maior(* n):
    cont = 0
    for c in n:
        print(c, end=' ')
        sleep(0.3)
        cont += 1
    print()
    print(f'Foram informados {cont} valores:')
    if len(n) == 0:
        print('O maior valor informado foi 0.')
    else:
        print(f'E o maior foi: {max(n)}')


maior(3,2,9,6,2)
maior()
