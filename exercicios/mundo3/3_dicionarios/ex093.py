jogador = dict()

jogador['nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {jogador['nome']} jogou? '))
jogador['gols'] = list()
jogador['total'] = 0

for i in range(0, partidas):
    qtd_gols = int(input(f'Quantos gols na partida {i + 1}? '))
    jogador['gols'].append(qtd_gols)
    jogador['total'] += qtd_gols

print('-=' * 30)
print(jogador)
print('-=' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')
print('-=' * 30)

print(f'O jogador {jogador['nome']} jogou {partidas} partidas.')

for i, v in enumerate(jogador['gols']):
    print(f'Na partida {i + 1}, fez {v} gols.')
    
print(f'Foi um total de {jogador['total']} gols.')