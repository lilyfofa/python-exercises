lista = []
for c in range(0,5):
    numero = int(input('Digite um valor: '))
    if c == 0 or numero > lista[-1]:
        lista.append(numero)
    else:
        p = 0
        while p < len(lista):
            if numero <= lista[p]:
                lista.insert(p, numero)
                break
            p += 1
print(f'Os valores digitados em ordem foram: {lista}')