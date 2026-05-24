def ficha(nome='<desconhecido>', gols=0):
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')

print('-' * 30)
nome = str(input('Nome do jogador: ')).strip()
gols = str(input('Número de gols: '))

if gols.isnumeric():
    gols = int(gols)
else:
    g = 0

if nome == '':
    ficha(gols = g)
else:
    ficha(nome, gols)