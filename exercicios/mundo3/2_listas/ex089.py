alunos = list()
temp_alunos = list()

while True:
    nome = str(input('Nome: ')).strip()
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))

    temp_alunos.append(nome)
    temp_alunos.append(n1)
    temp_alunos.append(n2)
    alunos.append(temp_alunos[:])
    temp_alunos.clear()

    escolha = str(input('Deseja continuar [S/N]? ')).strip().upper()

    if escolha == 'S':
        continue
    else:
        break

print('-=' * 40)
print(f'{'No.':<3}', f'{'NOME':<16}', f'{'MÉDIA':^5}')
print('-' * 30)

for i in range(0, len(alunos)):
    media = (alunos[i][1] + alunos[i][2]) / 2
    print(f'{i:<3}', f'{alunos[i][0]:<16}', f'{media:^.1f}')

print('-' * 30)

while True:
    notas = int(input('Deseja ver as notas de qual aluno? (999 interrompe): '))

    if notas == 999:
        print('FINALIZANDO...')
        print('<<< VOLTE SEMPRE >>>')
        break
    else:
        print(f'As notas de {alunos[notas][0]} são [{alunos[notas][1]}, {alunos[notas][2]}]')
        print('-' * 20)