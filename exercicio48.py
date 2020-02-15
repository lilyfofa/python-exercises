soma = 0
quant = 0
for i in range (1, 500):
    if i % 3 == 0 and i % 2 != 0:
        quant += 1
        soma += i
print(f'A soma dos  {quant} múltiplos de 3 ímpares de 1 a 500 é {soma}.')

