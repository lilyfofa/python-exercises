# numero = int(input('Por favor, digite um número natural: '))
# fator = numero - 1
# print(f'{numero} x ', end='')
# while fator > 1:
#     print(f'{fator} x ', end='')
#     numero *= fator
#     fator -= 1
# print(f'1 = {numero}.')
numero = int(input('Por favor, digite um número natural: '))
fator = numero
resultado = 1
while fator > 0:
    print(f'{fator}', end='')
    print(' x ' if fator > 1 else ' = ', end='')
    resultado *= fator
    fator -= 1
print(resultado)


