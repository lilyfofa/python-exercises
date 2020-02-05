print('---'*20+'\nAnálise de nomes\n'+'---'*20)
nome = str(input('Por favor, digite seu nome completo: ')).strip()
print(f'Seu nome em maiúsuclas é {nome.upper()}.\nSeu nome em minúsuclas é {nome.lower()}.\nSeu nome tem {len(nome.replace(" ",""))} letras.\nSeu primeiro nome é {nome.split()[0]} e ele tem {len(nome.split()[0])} letras.\n'+'---'*20)
