from random import randint
from time import sleep
from operator import itemgetter

jogadores = dict()
for k in range(0, 4):
    jogadores[f'jogador{k + 1}'] = randint(1, 6)

print('Valores sorteados:')
for k, v in jogadores.items():
    print(f'O {k} tirou {v}')
    sleep(1)

print('Ranking dos jogadores:')

ordem = dict(sorted(jogadores.items(), key=itemgetter(1), reverse=True))

n = 0
for k, v in ordem.items():
    n += 1
    print(f'{n}º lugar:', end=' ')
    print(f'{k} com {v}')
    sleep(1)
