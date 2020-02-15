soma = 0
quant = 0
for c in range(0, 6):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        quant += 1
        soma += num
print(f'A soma do(s)  {quant} número(s) par(es) digitado(s) é {soma}.')