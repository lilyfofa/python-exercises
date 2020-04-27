def área(l, c):
    area = l * c
    print('---'*20)
    print(f'A área de um terreno cujas dimensões são {l} m e {c} m é {area}m².')


área(float(input('Digite a larguta do terreno: ')), float(input('Digite o comprimento do terreno: ')))
