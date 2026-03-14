# Exercício de condições

import random

random_number = random.randint(0, 5)

print('DESCUBRA O NÚMERO SORTEADO')
print('Um número de 0 a 5 foi sorteado. Adivinhe qual foi!')
answer = int(input('Insira o número: '))

if answer == random_number:
    print('O número sorteado foi {}. Parabéns, você venceu!'.format(random_number))
else:
    print('O número sorteado foi {}. Que pena, você errou!'.format(random_number))