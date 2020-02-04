from math import sqrt as r,pow as p,hypot as h
print('---'*20+'\nPitágoras Simulator\n'+'---'*20)
adjacente = float(input('Digite o comprimento do cateto adjacente: '))
oposto = float(input('Digite o comprimento do cateto oposto: '))
#print(f'Se os catetos medem {adjacente} e {oposto}, a hipotenusa mede {r(p(adjacente,2)+p(oposto,2)):.2f}.\n'+'---'*20)
#print(f'Se os catetos medem {adjacente} e {oposto}, a hipotenusa mede {(adjacente**2+oposto**2)**(1/2)}.\n'+'---'*20)
print(f'Se os catetos medem {adjacente} e {oposto}, a hipotenusa medirá {h(adjacente,oposto):.2f}.\n'+'---'*20)