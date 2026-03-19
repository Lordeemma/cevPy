# Exercício sobre listas

from math import inf

number_list = []
great = 0
least = inf

for n in range(0, 5):
    number = int(input('Insira um número: '))
    number_list.append(number)

    if number > great:
        great = number

    if number < least:
        least = number

print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
print(f'Você digitou os valores {number_list}')


print(f'O maior valor foi {great} nas posições', end=' ')
for i, v in enumerate(number_list):

    if v == great:
        
        print(f'{i}...', end=' ')

print('')

print(f'O menor valor foi {least} nas posições', end=' ')
for i, v in enumerate(number_list):

    if v == least:
        print(f'{i}...', end=' ')
