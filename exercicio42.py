print('---'*20+'\nCondição de existência do triângulo\n'+'---'*20)
a = float(input('Digite o primeiro segemento do triângulo: '))
b = float(input('Digite o segundo segemento do triângulo: '))
c = float(input('Digite o terceiro segemento do triângulo: '))
if (b-c) < a < (b+c) and (a-c) < b < (a+c) and (a-b) < c < (a+b):
    print(f'O triângulo com lados {a}, {b} e {c} pode existir. ', end='')
    if a == b == c:
        print('Os segmentos formam um triângulo equilátero!')
    elif a != b != c:
        print('Os segmentos formam um triângulo escaleno!')
    else:
        print('Os segmentos formam um triângulo isósceles!')
else:
    print(f'O triângulo com lados {a}, {b} e {c} \033[31mNÃO\033[m pode existir.')
