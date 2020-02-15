num1 = int(input('Digite o primeiro valor inteiro: '))
num2 = int(input('Digite o segundo valor inteiro: '))
parar = False
while not parar:
    print('---' * 20 + '\nEscolha uma dessas opções:\n[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Novos números\n[5] Sair do programa\n' + '---' * 20)
    opcao = int(input('Digite sua opção: '))
    if opcao == 1:
        print(f'O resultado da soma é {num1 + num2}.')
    elif opcao == 2:
        print(f'O resultado da multiplicação é {num1 * num2}.')
    elif opcao == 3:
        if num1 > num2:
            print(f'{num1} é maior.')
        else:
            print(f'{num2} é maior.')
    elif opcao == 4:
        num1 = int(input('Digite o primeiro valor inteiro: '))
        num2 = int(input('Digite o segundo valor inteiro: '))
    elif opcao == 5:
        parar = True
    else:
        print('Opção inválida. Digite uma opção entre 1 e 5.')
print('---'*20+'\nFim\n'+'---'*20)

