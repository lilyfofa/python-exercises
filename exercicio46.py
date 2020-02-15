from time import sleep
for i in range(10, 0, -1): #O exercício pedia até 0, mas não faz muito sentido. Nesse caso, seria range(10, -1, -1)
    print(i)
    sleep(1)
print('Feliz Ano Novo!')
