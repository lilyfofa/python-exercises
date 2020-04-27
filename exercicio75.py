primeiro = int(input('Digite o primeiro valor: '))
segundo = int(input('Digite o segundo valor: '))
terceiro = int(input('Digite o terceiro valor: '))
quarto = int(input('Digite o quarto valor: '))
numeros = (primeiro, segundo, terceiro, quarto)
print(f'O número 9 apareceu {numeros.count(9)} vez(es).')
if numeros.count(3) == 0:
    print('O número três não foi digitado.')
else:
    print(f'O três foi digitado primeiro na posição {numeros.index(3) + 1}.')
contador = 0
for c in numeros:
    if c % 2 == 0:
        contador += 1
print(f'Há {contador} número(s) pares.')
