# Mais um exercício sobre o laço for

sum = 0

for i in range(1, 500 + 1):
    if i % 2 != 0 and i % 3 == 0:
        sum += i

    if i == 500:
        print('A soma dos números ímpares foi de {}'.format(sum))

