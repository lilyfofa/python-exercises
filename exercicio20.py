print('---'*15+'\nOrdenador de alunos\n'+'---'*15)
primeiro = input('Digite o nome do primeiro aluno: ')
segundo = input('Digite o nome do segundo aluno: ')
terceiro = input('Digite o nome do terceiro aluno: ')
quarto = input('Digite o nome do quarto aluno: ')
lista = [primeiro,segundo,terceiro,quarto]
from random import shuffle
shuffle(lista)
print(f'A ordem dos alunos será {lista}.')

