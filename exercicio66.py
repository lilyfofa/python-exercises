soma = contador = 0
while True:
    numero = int(input('Digite um número inteiro: [999 para terminar] '))
    if numero == 999:
        break
    soma += numero
    contador += 1
print(f'A soma do(s) {contador} valor(es) é {soma}.')


