print('-' * 30)

jogadores = list()

while True:
    jogador = dict()
    jogador['nome'] = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantas partidas {jogador['nome']} jogou? '))
    jogador['gols'] = list()
    jogador['total'] = 0

    for i in range(0, partidas):
        qtd_gols = int(input(f'Quantos gols na partida {i + 1}? '))
        jogador['gols'].append(qtd_gols)
        jogador['total'] += qtd_gols
    jogadores.append(jogador)

    escolha = str(input('Deseja continuar [S/N]? ')).strip().upper()
    if escolha == 'S':
        print('-' * 30)
    else:
        break

print('-=' * 40)
print(f'{'Cód':<6}', f'{'NOME':<32}', f'{'GOLS':<20}', f'{'TOTAL':<12}')
print('-' * 80)

for i in range(0, len(jogadores)):
    print(f'{i:>6}', f'{jogadores[i]['nome']:<32}', f'{jogadores[i]['gols']}', f'{jogadores[i]['total']:>20}')
print('-' * 80)

while True:
    id = int(input('Mostrar dados de qual jogador? '))

    if id > len(jogadores) - 1 and id != 999:
        print(f'ERRO! Não existe jogador com Código {id}! Tente novamente.')
    else:
        print(f'—— LEVANTAMENTO DO JOGADOR {jogadores[id]['nome']}:')
        for i, v in enumerate(jogadores[id]['gols']):
            print(f'Na partida {i + 1}, fez {v} gols.')
    
    if id == 999:
        print('<< VOLTE SEMPRE >>')
        break
    print('-' * 30)

