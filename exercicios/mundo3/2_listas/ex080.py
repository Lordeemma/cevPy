# Mais outro exercício sobre listas

import random

ord_list = []

for n in range(5):
    number = int(input('Digite um valor: '))
    
    if number not in ord_list:
        ord_list.append(number)

    for pos, value in enumerate(ord_list):
        if ord_list[-1] < ord_list[-1 + pos]:
                ord_list.insert(-1 + pos, number)
                ord_list.pop()
                break
    
    if ord_list[ord_list.index(number)] != ord_list[-1]:
        print(f'{ord_list[ord_list.index(number)]} adicionado à posição {ord_list.index(number)} da lista')
    else:
        print(f'{ord_list[ord_list.index(number)]} adicionado ao fim da lista')

print('=' * 30)
print(f'Os números digitados em ordem crescente foram {ord_list}')