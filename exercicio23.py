print('---'*15+'\nAnálise de números\n'+'---'*15)
numero = int(input('Digite um número: '))
print(f'Unidade: {numero//1%10}\nDezena: {numero//10%10}\nCentena: {numero//100%10}\nMilhar: {numero//1000%10}\n'+'---'*15)

