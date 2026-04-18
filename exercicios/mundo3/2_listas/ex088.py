from random import randint
from time import sleep

print('=' * 30)
print(f'{'JOGA NA MEGA SENA':^30}')
print('=' * 30)

qtd_jogos = int(input('Quantos jogos você quer que eu sorteie? '))
jogo = list()

print('-=-=-=', f'{f'SORTEANDO {qtd_jogos} JOGOS':^20}', '-=-=-=')

for i in range(0, qtd_jogos):
    jogo.clear()
    while len(jogo) < 6:
        rand = randint(1, 60)

        if rand not in jogo:
            jogo.append(rand)
    print(f'Jogo {i + 1}: {jogo}')
    sleep(0.7)

print('-=-=-=', f'{'< BOA SORTE! >':^20}', '-=-=-=')