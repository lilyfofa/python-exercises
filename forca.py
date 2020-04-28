```python
def main(*msg):
    temp = []
    from random import randint
    def linha():
        print('~~~'*15)
    linha()
    print('        Forca')
    linha()
    if type(msg) == str:
        palavra = msg
    else:
        palavra = (msg[randint(0, len(msg)) - 1]).upper()
    contador = 0
    lista = []
    erros = []
    for _ in palavra:
        lista.append(' _ ')
    while lista.count(' _ ') > 0:
        for item in lista:
            print(item, end='')
        print('\n'+'~~~'*15)
        while True:
            chute = input('Qual o seu chute? ').upper()
            if len(chute) == 1 and chute.isalpha():
                break
        if chute in palavra:
            print(f'Você acertou a letra {chute}!')
            for p, v in enumerate(palavra):
                if chute == v:
                    lista[p] = chute
        else:
            print(f'A letra {chute} não está na palavra!')
            erros.append(chute)
            contador += 1
        if len(erros) > 0:
            linha()
            print('Letras erradas')
            print(erros)
            linha()

    print(f'PARABÉNS! A palavra era {palavra}. Você teve {contador} erro(s).')
    linha()
```

