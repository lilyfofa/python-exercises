pessoas = []
while True:
    usuario = {}
    usuario['Nome'] = str(input('Nome: ')).title()
    while True:
        usuario['Sexo'] = str(input('Sexo: (M/F) ')).title()
        if usuario['Sexo'] in 'MF':
            break
        print('Erro. Responda com M ou F!')
    usuario['Idade'] = int(input('Idade: '))
    pessoas.append(usuario)
    while True:
        continuar = str(input('Deseja continuar? (S/N) ')).title()
        if continuar in 'SN':
            break
        else:
            print('Erro. Responda com S ou N!')
    if continuar in 'N':
        print('---' * 20)
        break
    print('---'*20)
# Quantas pessoas foram cadastradas
print(f'Ao todo, {len(pessoas)} pessoas foram cadastradas.')
# A média de idade
soma = 0
for p in pessoas:
    soma += p['Idade']
print(f'A média de idade é de {soma / len(pessoas):.2f}.')
# Mulheres cadastradas
print('As mulheres cadastradas foram: ', end='')
for i in pessoas:
    if i['Sexo'] in 'Ff':
        print(f"[{i['Nome']}]", end=' ')
print()
# Pessoas acima da média de idade
print('Pessoas acima da média de idade: ')
for lily in pessoas:
    if lily['Idade'] > (soma / len(pessoas)):
        print('   ', end='')
        for k, v in lily.items():
            print(f'{k} = {v}; ', end='')
        print()




