palavras = ('Jogar','Aprender','Grindar','Vencer','Perder','Overwatch')
for c in palavras:
    print(f'A palvra {c} tem as vogais: ', end='')
    for l in c:
        if l in 'aeiouAEIOU':
            print(l, end=' ')
    print()


