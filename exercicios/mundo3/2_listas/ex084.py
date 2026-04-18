import math

cadastro = list()
dados = list()
pesomai = 0
pesomen = math.inf

while True:
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Peso: ')))

    if dados[1] > pesomai:
        pesomai = dados[1]
    elif dados[1] < pesomen:
        pesomen = dados[1]

    cadastro.append(dados[:])
    dados.clear()

    escolha = str(input('Deseja continuar [S/N]? ')).strip().upper()

    if escolha == 'S':
        continue
    else:
        break
    
print('-=' * 30)
    
print(f'Ao todo, você cadastrou {len(cadastro)} pessoas.')

print(f'O maior peso foi {float(pesomai):.2f}kg, peso de ', end='')
for p in cadastro:
    
    if p[1] == pesomai:
        print(f'[{p[0]}]', end=' ')

print('')

print(f'O menor peso foi {float(pesomen):.2f}kg, peso de ', end='')
for p in cadastro:
    
    if p[1] == pesomen:
        print(f'[{p[0]}]', end=' ')