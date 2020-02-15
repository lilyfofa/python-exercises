sexo = str(input('Digite o seu sexo (M/F): ')).strip().upper()
# while sexo != 'M' and sexo != 'F':
while sexo not in 'MF':
    sexo = str(input('Dado inválido. Por favor, digite seu sexo: ')).strip().upper()
print(f'Sexo {sexo} registrado com sucesso.')