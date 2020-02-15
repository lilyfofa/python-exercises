r = int(input('Digite a razão: '))
a1 = int(input('Digite o primeiro termo da PA: '))
inicio = 1
n = 1
opcao = 10
contador = 0
terminar = False
while not terminar:
    for c in range(inicio, opcao + 1):
        print(a1 + (c - 1) * r, end=' - ')
        contador += 1
    print('Pausa')
    inicio = opcao + 1
    opcao = int(input('Quantos termos mais você quer ver? '))
    if opcao == 0:
        terminar = True
    opcao += inicio - 1
print(f'PA finalizada com sucesso. {contador} termos foram exibidos.')

