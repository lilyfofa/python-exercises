from datetime import datetime
ano = datetime.today().year
trab = dict()
trab['Nome'] = input('Digite seu nome: ')
trab['Idade'] = ano - int(input('Digite seu ano de nascimento: '))
trab['Carteira de trabalho'] = int(input('Digite sua carteira de trabalho:  (0 não tem) '))
if trab['Carteira de trabalho'] != 0:
    trab['Ano de contratação'] = int(input('Digite o ano de contratação: '))
    trab['Sálario'] = 'R$' + input('Digite seu sálario: R$')
    trab['Idade de aposentadoria'] = trab['Idade'] + (35 - (ano - trab['Ano de contratação']))
print('---'*20)
for k, v in trab.items():
    print(f'{k}: {v}')
print('---'*20)