expressão = input('Digite a expressão: ')
# contador = 0
# contador2 = 0
# for c in expressão:
#     if c == '(':
#         contador +=1
#     elif c == ')':
#         contador2 += 1
# if contador == contador2:
#     print('A expressão está correta!')
# else:
#     print('A expressão não é válida!')
lista = []
for c in expressão:
    if c == '(':
        lista.append(c)
    elif c == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(c)
if len(lista) > 0:
    print('Sua expressão não é válida!')
else:
    print('Sua expressão é válida!')