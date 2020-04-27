c = 1
lista = []
while True:
    nome = str(input('Nome: ')).title()
    nota1 = int(input('Nota 1: '))
    nota2 = int(input('Nota 2 : '))
    aluno = [c, nome, nota1, nota2]
    lista.append(aluno[:])
    if input('Deseja continuar? (S/N) ') in 'Nn':
        break
    c += 1
print('---'*30)
print(f'N | Nome       | Média')
for c in lista:
    print(f'{c[0]:} | {c[1]:10} | {(c[2] + c[3]) / 2}')
print('---'*30)

while True:
    numero = int(input('Digite o número do aluno para ver suas notas: (-1 para encerrar) ')) - 1
    if numero == -2:
        break
    print(f'As notas de {lista[numero][1]} foram {lista[numero][2]} e {lista[numero][3]}.')
    print('---' * 30)

