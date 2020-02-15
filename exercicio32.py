import datetime as dt
print('---'*30+'\nAnos bissextos\n'+'---'*30)
ano = int(input('Por favor, digite um ano para saber se ele é bissexto: (0 para o ano atual) '))
if ano == 0 and dt.datetime.now().year % 4 == 0 and dt.datetime.now().year % 100 != 0 or dt.datetime.now().year % 400 == 0:
    print(f'0 ano de {dt.datetime.now().year} é bissexto.\n'+'---'*30)
elif ano != 0 and ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano de {ano} é bissexto.\n'+'---'*30)
else:
    print(f'O ano de {ano} não é bissexto.\n'+'---'*30)