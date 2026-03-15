# Mais outro exercício sobre o laço for

n = int(input('Insira um número inteiro: '))

for i in range(1, 10 + 1):
    print('{} * {} = {}'.format(n, i, n*i))