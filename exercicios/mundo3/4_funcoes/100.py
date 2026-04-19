from random import randint
from time import sleep

numeros = list()

def sorteio():
    print('Sorteando 5 valores da lista:', end=' ')
    for i in range(0, 5):
        aleatorio = randint(1, 10)
        print(f'{aleatorio}', end=' ', flush=True)
        numeros.append(aleatorio)
        sleep(0.5)
    print('PRONTO!')

def somaPar(lst):
    soma = 0

    for i, v in enumerate(lst):
        if v % 2 == 0:
            soma += v

    print(f'Somando os valores pares de {numeros}, temos {soma}')

sorteio()
somaPar(numeros)
