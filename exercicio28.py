from random import randint
print('---'*20+'\nAdivinhe o número do computador\n'+'---'*20)
maquina = randint(0,5)
player = int(input('Por favor, digite um número entre 0 e 5: '))
if maquina == player:
    print(f'Parabéns! Você venceu! O número era {maquina}.\n'+'---'*20)
elif player > 5 or player < 0:
    print('Por favor, escolhe um número maior que 0 e menor que 5!\n'+'---'*20)

else:
    print(f'Ah! Você perdeu! Tente novamente. O número era {maquina}.\n'+'---'*20)
