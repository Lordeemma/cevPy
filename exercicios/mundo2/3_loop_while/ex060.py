# Mais outro exercício sobre o laço while

from math import factorial

n = 0

while n <= 0:
    n = int(input('Insira um número inteiro: '))
    c = n
    if n < 0:
        print('Não insira números negativos!')

print('WHILE')
while c >= 1:
    if c > 2:
        print(c, '*', end=' ')
        c -= 1
        if c == 2:
            print(c, '*', end=' ')
            c -= 1
            continue
    else:
        print('{} = {}'.format(c, factorial(n)))
        c = 0

print('')
print('FOR')
c = n
for i in range(n, 1 - 1, -1):
    if i == 1:
        print('{} = {}'.format(i, c))
    else:
        print('{} * '.format(i), end='')
        c *= i - 1

