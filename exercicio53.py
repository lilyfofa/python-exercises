frase = str(input('Digite uma frase: ')).replace(' ', '').upper()
# palindromo = frase[::-1]
# if palindromo == frase:
#     print(f'O inverso de {frase} é {palindromo}. Logo, a frase é um palíndromo.')
# else:
#     print(f'O inverso de {frase} é {palindromo}. Logo, a frase não é um palíndromo.')
inverso = ''
for c in range(len(frase) - 1, -1, -1):
    inverso+= frase[c]
if inverso == frase:
    print(f'O inverso de {frase} é {inverso}. Logo, a frase é um palíndromo.')
else:
    print(f'O inverso de {frase} é {inverso}. Logo, a frase não é um palíndromo.')