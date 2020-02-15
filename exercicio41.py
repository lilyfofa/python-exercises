from datetime import datetime
ano = datetime.today().year
nascimento = int(input('Qual o ano de nascimento do atleta? '))
idade = ano - nascimento
if idade <= 9:
    print(f'O atleta tem {idade} anos e está na categoria MIRIM.')
elif 9 < idade <= 14:
    print(f'O atleta tem {idade} anos e está na categoria INFANTIL.')
elif 14 < idade <= 19:
    print(f'O atleta tem {idade} anos e está na categoria JÚNIOR.')
elif 19 < idade <= 25:
    print(f'O atleta tem {idade} anos e está na categoria SÊNIOR.')
else:
    print(f'O atleta tem {idade} anos e está na categoria MASTER.')