def votar(nascimento):
    from datetime import date
    idade = date.today().year - nascimento
    if idade < 16:
        return f'Com {idade}, o voto é negado.'
    elif 16 <= idade < 18 or idade >= 70:
        return f'Com {idade} anos, o voto é facultativo.'
    elif 18 <= idade < 70:
        return f'Com {idade} anos, o voto é obrigatório.'


nascimento = int(input('Ano de nascimento: '))
print(votar(nascimento))