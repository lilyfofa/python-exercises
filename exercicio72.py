# lily = ('Rafa feia', 'Lily fofa', 'Blue feio')
# for p, i in enumerate(lily):
#      print(f'Palavra: {i}\nPosição: {p}')
numero = int(input('Digite qual número quer ver por extenso: '))
while numero > 20 or numero < 0:
    numero = int(input('Tente novamente. Digite qual número quer ver por extenso: '))
numeros = ('Zero','Um','Dois','Três','Quatro','Cinco','Seis','Sete','Oito','Nove',
            'Dez','Onze','Doze','Treze','Catorze','Quinze','Dezesseis','Dezessete','Dezoito','Dezenove','Vinte')
print(f'O número {numero} escrito por extenso é {numeros[numero]}')