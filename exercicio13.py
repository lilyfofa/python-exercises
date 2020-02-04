print("---"*30+'\nCálculo de reajuste salarial\n'+"---"*30)
s = float(input('Digite o valor do salário atual: ').replace(",","."))
p = float(input('Digite a porcentagem do aumento: ').replace(",","."))
print(f'Seu salário de {s} será de {s+s*(p/100):.2f} dado o aumento de {p}%.\nIsso representa um aumento de {s*(p/100):.2f}, com um ganho real de {s*(p/100-0.0448):.2f}. (INPC-2020)\n'+"---"*30)

