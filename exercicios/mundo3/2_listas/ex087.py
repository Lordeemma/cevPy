print('=' * 30)
print(f'{'MATRIZ':^30}')
print('=' * 30)

matriz = list()
tempmatriz = list()

for y in range(0, 3):
    tempmatriz.clear()
    for x in range (0, 3):
        n = int(input(f'Insira um número na posição ({y}, {x}): '))

        tempmatriz.append(n)

    matriz.append(tempmatriz[:])

print('-=' * 30)

for i in range(0, 3):
    print('')
    for v in range(0, 3):
        print(f'[{matriz[i][v]:^5}]', end=' ')
        y += 1

print('')
print('-=' * 30)
print('')

soma = maior_valor = soma_terceira_coluna = 0

for y in range(0, 3):
    for x in range(0, 3):
        if matriz[y][x] % 2 == 0:
            soma += matriz[y][x]

        if y == 1:
            if matriz[y][x] > maior_valor:
                maior_valor = matriz[y][x]

        if x == 2:
            soma_terceira_coluna += matriz[y][x]

print(f'A soma dos valores pares é {soma}')
print(f'A soma dos valores da terceira coluna é {soma_terceira_coluna}')
print(f'O maior valor da segunda linha é {maior_valor}')