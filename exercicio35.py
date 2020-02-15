print('---'*20+'\nCondição de existência do triângulo\n'+'---'*20)
a = float(input('Digite o valor do lado do triângulo: '))
b = float(input('Digite o valor de outro lado do triângulo: '))
c = float(input('Digite o valor do último lado do triângulo: '))
if (b-c) < a < (b+c) and (a-c) < b < (a+c) and (a-b) < c < (a+b):
    print(f'O triângulo com lados {a}, {b} e {c} pode existir.\n'+'---'*20)
else:
    print(f'O triângulo com lados {a}, {b} e {c} \033[31mNÃO\033[m pode existir.\n'+'---'*20)
