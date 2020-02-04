from math import sin,cos,tan,radians
print('---'*30+'\nSeno, cosseno e tangente\n'+'---'*30)
angulo = float(input('Digite um ângulo: '))
print(f'O ãngulo {angulo} tem seno de valor {sin(radians(angulo)):.2f}, cosseno de valor {cos(radians(angulo)):.2f} e tangente de valor {tan(radians(angulo)):.2f}.\n'+'---'*30)
