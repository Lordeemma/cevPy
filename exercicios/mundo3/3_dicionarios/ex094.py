pessoas = list()

while True:
    pessoa = dict()
    pessoa['nome'] = str(input('Nome: ')).strip()
    pessoa['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()
    pessoa['idade'] = int(input('Idade: '))
    pessoas.append(pessoa)

    escolha = str(input('Deseja continuar [S/N]? ')).strip().upper()
    if escolha == 'S':
        print('=' * 30)
        continue
    else:
        break

print('-=' * 30)
print(f'— O grupo tem {len(pessoas)} pessoas.')


idade = 0
for pessoa in pessoas:
    idade += pessoa['idade']
media = idade / len(pessoas)
print(f'— A média de idade é de {media:.2f} anos')

tem_mulheres = 0
for pessoa in pessoas:
    if pessoa['sexo'] == 'F':
        tem_mulheres += 1

if tem_mulheres > 0:
    print('— As mulheres cadastradas foram:', end=' ')    
    for pessoa in pessoas:
        if pessoa['sexo'] == 'F':
            print(pessoa['nome'], end=' ')
else:
    print('— Nenhuma mulher foi cadastrada.', end='')
print('')

print('— Lista de pessoas que estão acima da média: ')
for pessoa in pessoas:
    if pessoa['idade'] > media:
        print(f'nome = {pessoa['nome']}; sexo = {pessoa['sexo']}; idade = {pessoa['idade']};')
print('<< ENCERRADO >>')
