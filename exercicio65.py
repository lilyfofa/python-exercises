contador = soma = maior = menor = 0
resposta = 'S'
while resposta == 'S':
    numero = int(input('Digite um número: '))
    contador += 1
    soma += numero
    if contador == 1:
        maior = numero
        menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    resposta = str(input('Deseja continuar (S/N): ')).upper()
print(f'Você digitou {contador} números e a média entre eles é {soma / contador}. O maior foi {maior} e o menor foi {menor}.')

