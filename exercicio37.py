numero = int(input('Digite um número inteiro: '))
base = int(input('Digite a base para a qual ele será convertido:\n1 - Binária\n2 - Octal\n3 - Hexadecimal\nSua resposta: '))
if base == 1:
    print(f'O número {numero} na base binária é {bin(numero)[2:]}.')
elif base == 2:
    print(f'O número {numero} na base octal é {oct(numero)[2:]}.')
elif base == 3:
    print(f'O número {numero} na base hexadecimal é {hex(numero)[2:]}.')
else:
    print('Por favor, digite somente algum desses números: 1, 2 e 3!')