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

print('')
print('-=' * 30)

for i in range(0, 3):
    print('')
    for v in range(0, 3):
        print(f'[{matriz[i][v]:^5}]', end=' ')
        y += 1

