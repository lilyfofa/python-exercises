print('---'*20+'\nNomes e sobrenomes\n'+'---'*20)
nome = input('Por favor, digite seu nome completo: ').title().strip()
print(f'Seu primeiro nome é {nome.split()[0]} e seu último nome é {nome.split()[-1]}.\n'+'---'*20)
