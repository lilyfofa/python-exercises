c100 = c50 = c20 = c10 = c5 = c2 = m1 = 0
print('Banco Lily Fofa\n'+'---'*20)
valor = int(input('Digite o valor que você quer sacar: R$'))
print('---'*20)
while valor >= 100:
    valor -= 100
    c100 += 1
while valor >= 50:
    valor -= 50
    c50 += 1
while valor >= 20:
    valor -= 20
    c20 += 1
while valor >= 10:
    valor -= 10
    c10 += 1
while valor >= 5:
    valor -= 5
    c5 += 1
while valor >= 2:
    valor -= 2
    c2 += 1
while valor >= 1:
    valor -= 1
    m1 += 1
if c100 > 0:
    print(f'Total de {c100} cédula(s) de R$100.')
if c50 > 0:
    print(f'Total de {c50} cédula(s) de R$50.')
if c20 > 0:
    print(f'Total de {c20} cédula(s) de R$20.')
if c10 > 0:
    print(f'Total de {c10} cédula(s) de R$10.')
if c5 > 0:
    print(f'Total de {c5} cédula(s) de R$5.')
if c2 > 0:
    print(f'Total de {c2} cédula(s) de R$2.')
if m1 > 0:
    print(f'Total de {m1} moeda(s) de R$1.')
print('---'*20)
# print('Banco da Lily')
# print('---' * 20)
# valor = int(input('Que valor você quer sacar? R$ '))
# cedula = 100
# total = 0
# while True:
#     if valor >= cedula:
#         valor -= cedula
#         total += 1
#     else:
#         if total > 0:
#             print(f'Total de {total} cédulas de R$ {cedula}')
#         if cedula == 100:
#             cedula = 50
#         elif cedula == 50:
#             cedula = 20
#         elif cedula == 20:
#             cedula = 10
#         elif cedula == 10:
#             cedula = 1
#         total = 0
#         if valor == 0:
#             break
# print('---' * 20)