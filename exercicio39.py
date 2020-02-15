import datetime
anoatual = datetime.datetime.today().year
ano = int(input('Digite o ano de seu nascimento: '))
if anoatual - ano == 18:
    print(f'Quem nasceu em {ano} tem {anoatual - ano} ano(s). Nesse ano você deverá se alistar!')
elif anoatual - ano < 18:
    print(f'Quem nasceu em {ano} tem {anoatual - ano} ano(s). Você deverá se alistar daqui a {(ano + 18) - anoatual} ano(s).')
else:
    print(f'Quem nasceu em {ano} tem {anoatual - ano} ano(s). Você deveria ter se alistado há {anoatual - (ano+18)} ano(s), ou seja, em {ano + 18}.')
