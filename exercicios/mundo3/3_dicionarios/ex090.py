aluno = dict()

aluno['nome'] = str(input('Nome do aluno: '))
aluno['media'] = float(input(f'Média de {aluno['nome']}: '))

if aluno['media'] < 7:
    aluno['situacao'] = 'REPROVADO'
else:
    aluno['situacao'] = 'APROVADO'

print('')

print(f'Nome do aluno: {aluno['nome']}')
print(f'Média: {aluno['media']}')
print(f'Situação: {aluno['situacao']}')