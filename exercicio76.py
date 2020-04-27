lista = ('Processador',650,'Placa-mãe',350,'Placa de vídeo',930,'Memória RAM', 250,'HD',230,'Fonte',210)
for c in range(0,len(lista), 2):
    print(f'{lista[c]:.<30} R${lista[c+1]:.2f}')