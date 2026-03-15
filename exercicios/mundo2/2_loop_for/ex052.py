# Mais outro exercício sobre o laço for

from math import sqrt

n = int(input('Digite um número: '))

if n == 2:
    print('{} é primo.'.format(n))
elif n <= 1:
    print('{} não é primo'.format(n))
elif n % 2 == 0:
    print ('{} não é primo.'.format(n))
else:
    for i in range(2, int(sqrt(n)) + 1, 2):
        if n % i == 0:
            print('{} não é primo.'.format(n))
            break

        print('{} é primo.'.format(n, r))

