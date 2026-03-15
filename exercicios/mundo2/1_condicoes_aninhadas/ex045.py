# Último exercício sobre condições aninhadas

import random

choices = ['PEDRA', 'PAPEL', 'TESOURA']
result = ['O JOGADOR VENCEU', 'O COMPUTADOR VENCEU']

print('JOKENPO VS CPU')

player_choice = int(input("""
    Qual é sua escolha?
    [1] PEDRA
    [2] PAPEL                     
    [3] TESOURA                     
    """))

cpu_choice = random.randint(1, 3)

if player_choice == 1 and cpu_choice == 3:
    print('{} vence {}. {}!'.format(choices[0], choices[2], result[0]))
elif player_choice == 2 and cpu_choice == 1:
    print('{} vence {}. {}!'.format(choices[1], choices[0], result[0]))
elif player_choice == 3 and cpu_choice == 2:
    print('{} vence {}. {}!'.format(choices[2], choices[1], result[0]))

if cpu_choice == 1 and player_choice == 3:
    print('{} vence {}. {}!'.format(choices[0], choices[2], result[1]))
elif cpu_choice == 2 and player_choice == 1:
    print('{} vence {}. {}!'.format(choices[1], choices[0], result[1]))
elif cpu_choice == 3 and player_choice == 2:
    print('{} vence {}. {}!'.format(choices[2], choices[1], result[1]))

if player_choice == cpu_choice:
    print('EMPATE!')

