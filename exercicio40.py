nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
if media < 5:
    print(f'Sua média é {media:.1f} e, portanto, você foi REPROVADO.')
elif 5 <= media < 7:
    print(f'Sua média é {media:.1f} e, portanto, você está de RECUPERAÇÃO.')
else:
    print(f'Parabéns! Sua média é {media:.1f} e, portanto, você foi APROVADO!')
