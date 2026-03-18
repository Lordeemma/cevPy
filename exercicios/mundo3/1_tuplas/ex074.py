# Mais outro exercício sobre tuplas

from random import randint

random_list = (randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9), randint(0,9))
great = 0
least = 10

for i in random_list:

    if i > great:
        great = i

    if i < least:
        least = i

print (f'Os números sorteados foram {random_list}')
print(f'O maior número sorteado foi {great}')
print(f'O menor número sorteado foi {least}')