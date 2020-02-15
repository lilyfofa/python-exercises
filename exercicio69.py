maior = menor = homens = 0
while True:
    print('---'*20+'\nCadastre uma pessoa\n'+'---'*20)
    idade = int(input('Digite a idade dessa pessoa: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Qual é o sexo dessa pessoa: ')).upper()
    if idade >= 18:
        maior += 1
    if sexo == 'F' and idade < 20:
        menor += 1
    if sexo == 'M':
        homens += 1
    a = ' '
    while a not in 'SN':
        a = str(input('Deseja continuar? [S/N] ')).upper()
    if a == 'N':
        break
print(f'Total de pessoas com 18 anos ou mais: {maior}.\nTotal de mulheres com menos de 20 anos: {menor}.\nTotal de homens cadastrados: {homens}.')
