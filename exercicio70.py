soma = caros = contador = precob = 0
barato = ' '
print('Loja da Lily\n'+'---'*20)
while True:
    contador += 1
    nome = str(input('Digite o nome do produto: ')).title()
    preco = float(input('Digite o preço do produto: '))
    soma += preco
    if preco > 1000:
        caros += 1
    if contador == 1:
        barato = nome
        precob = preco
    else:
        if preco < precob:
            barato = nome
            precob = preco
    a = ' '
    while a not in 'SN':
        a = str(input('Deseja continuar? [S/N] ')).upper()
    if a == 'N':
        break
    print('---'*20)
print(f'O total dos preços digitados é R${soma:.2f}. Há {caros} produto(s) cujo valor é maior que R$1000,00. O produto mais barato é {barato}, que custa R${precob:.2f}.')




