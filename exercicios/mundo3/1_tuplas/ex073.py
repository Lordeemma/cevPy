# Outro exercício sobre tuplas

brasileirao_2026 = ('São Paulo', 'Palmeiras', 'Fluminense', 'Bahia', 'Flamengo',
               'Coritiba', 'Grêmio', 'Corinthians', 'Bragantino', 'Athletico-PR',
               'EC Vitória', 'Chapecoense', 'Mirassol', 'Santos', 'Vasco da Gama',
               'Atlético-MG', 'Botafogo', 'Remo', 'Cruzeiro', 'Internacional')

print(f'Top 5 do Brasileirão 2026: {brasileirao_2026[0:5]}')
print(f'Últimos 4 colocados: {brasileirao_2026[-1:-4]}')
print(f'Times em ordem alfabética: {sorted(brasileirao_2026)}')

for i, time in enumerate(brasileirao_2026):
    if time == 'Chapecoense':
        print(f'A Chapecoense está na {i + 1}ª posição.')

