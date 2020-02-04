from random import choice
print('---'*15+'\nSorteador\n'+'---'*15)
primeiro = input('Qual o nome do primeiro aluno? ')
segundo = input('Qual o nome do segundo aluno? ')
terceiro = input('Qual o nome do terceiro aluno? ')
print(f'O aluno sorteado foi {choice([primeiro,segundo,terceiro])}\n'+'---'*15)
