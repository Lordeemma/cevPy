# Mais outro exercício sobre interrupção do laço while

from random import randint
from time import sleep

print('''
================
      
    PAR  OU
     ÍMPAR
      
================     
      ''')

player_choice = 0
victory_counter = 0

while True:
    while player_choice < 1 or player_choice > 5:
        player_choice = int(input('Escolha um número par ou impar de 1 a 5: '))
        
        if player_choice < 1 or player_choice > 5:
            print('Faça uma escolha válida!')
            print('')

    print('')

    if player_choice % 2 == 0:
        print(f'VOCÊ ESCOLHEU PAR ({player_choice})')
    else:
        print(f'VOCÊ ESCOLHEU ÍMPAR ({player_choice})')

    print('')
    
    cpu_choice = randint(1, 5)

    if cpu_choice % 2 == 0:
        print(f'O COMPUTADOR ESCOLHEU PAR ({cpu_choice})')
    else:
        print(f'O COMPUTADOR ESCOLHEU ÍMPAR ({cpu_choice})')

    print('=========================================')

    result = player_choice + cpu_choice

    if player_choice % 2 == result % 2:
        print(f'VOCÊ VENCEU! (Resultado: {result})')
        victory_counter += 1
    else:
        print(f'VOCÊ PERDEU! (Resultado: {result})')
        break


    player_choice = 0
    cpu_choice = 0
    print('INICIANDO NOVO JOGO', end='')
    for i in range(1, 3 + 1):
        print('.', end='')
        sleep(0.3)
    print('')

print(f'VITÓRIAS CONSECUTIVAS: {victory_counter}')
