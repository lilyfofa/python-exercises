idadetotal = 0
# maisvelhos = []
idademaior = 0
maisvelho = ''
contador = 0
for c in range(1,5):
    print(f'--- {c}ª pessoa ---')
    nome = str(input('Nome: ')).title().strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo (M/F): ')).upper().strip()
    idadetotal += idade
    if sexo == 'M' and c == 1:
        idademaior = idade
        maisvelho = nome
    if sexo == 'M' and idade > idademaior:
        idademaior = idade
        maisvelho = nome
    #if sexo == 'M':
        #maisvelhos.append(nome)
    if sexo == 'F' and idade < 20:
        contador += 1
#maisvelhos.sort()
#print(f'A idade média é de {idadetotal / 4}. O homem mais velho é {maisvelhos[0]}. ', end='')
print(f'A idade média é de {idadetotal / 4}. O homem mais velho é {maisvelho}. ', end='')
if contador == 1:
    print(f'{contador} mulher tem menos de 20 anos.')
elif contador == 0:
    print('Nenhuma mulher tem menos de 20 anos.')
else:
    print(f'{contador} mulheres têm menos de 20 anos.')


