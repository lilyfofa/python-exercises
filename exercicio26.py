print('---'*20+'\nAchando os As\n'+'---'*20)
frase = str(input('Por favor, digite uma frase: ')).lower().strip()
print(f'A letra A aparece {frase.count("a")} vezes.\nA letra A aparece primeiramente na posição {frase.find("a")+1}.\nA última letra A  aparece na posição {frase.rfind("a")+1}.\n'+'---'*20)