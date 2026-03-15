# Exercício sobre o laço for

from time import sleep

for c in reversed(range(10 + 1)):
    if c == 0:
        print('{}!! FELIZ ANO NOVO!'.format(c))
        break

    print(c)
    sleep(1)          
    