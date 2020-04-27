times = ('Athletico-PR','Atlético-GO','Atlético-MG','Bahia','Botafogo','Bragantino','Ceará','Corinthians',
         'Coritiba','Flamengo','Fluminense','Fortaleza','Goiás','Grêmio','Internacional',
         'Palmeiras','Santos','São Paulo','Vasco','Sport')
print(f'Os cinco primeiros times são: {times[:5]}')
print(f'Os últimos quatro colocados são {times[-4:]}')
# print(f'A ordem alfabética dos times é {sorted(times)}')
print(f'A ordem alfabética dos times é:')
for c in sorted(times):
    print(c)
print(f'O Corinthians está na posição {times.index("Corinthians") + 1}.')