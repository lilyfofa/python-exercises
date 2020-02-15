numero = int(input('Digite um número (999 para finalizar): '))
contador = soma = 0
while numero != 999:
    contador += 1
    soma += numero
    numero = int(input('Digite um número (999 para finalizar): '))
print(f'Programa finalizado com sucesso. {contador} números foram digitados e sua soma é {soma}.')
