alunos = []
alunos.append({'Nome':input('Nome: '), 'Nota': float(input('Nota: '))})
if alunos[0]['Nota'] > 6:
    alunos[0]['Situação'] = 'aprovado'
else:
    alunos[0]['Situação'] = 'reprovado'
# print(f'Seu nome é {alunos[0]["nome"]}. Sua nota é {alunos[0]["nota"]}. Sua situação é {alunos[0]["situação"]}.')
print('---'*15)
for k, v in alunos[0].items():
    print(f'{k}: {v}')
