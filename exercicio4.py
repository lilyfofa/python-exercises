msg = input('Digite uma palavra: ')
print('A palavra tem classe ', type(msg))
print('A palavra tem espaços? ', msg.isspace())
print('É um número? ', msg.isnumeric())
print('É alfabético? ', msg.isalpha())
print('É alfanumérico? ', msg.isalnum())
print('Está em maiúsculas?' , msg.isupper())
print('Está em minúsculas? ', msg.islower())
print('Está capitalizada? ', msg.istitle())
