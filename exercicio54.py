import datetime
anoatual = datetime.date.today().year
maior = 0
menor = 0
for c in range(1, 8):
    idade = anoatual - int(input(f'Digite a data de nascimento da {c}ª pessoa: '))
    if idade >= 18:
        maior+= 1
    else:
        menor+= 1
print(f'Você digitou {maior} anos de nascimento que já estão na maioridade e {menor} que não estão.')

