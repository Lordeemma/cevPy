# Outro exercício sobre o laço while

from random import randint

player_choice = -1
cpu_choice = randint(0, 10)
attempt_counter = 0

print('''
\033[1;35;47m===================
      JOGO DA      
    ADIVINHAÇÃO    
===================
Um número de 0 a 10
   será sorteado.  
  Tente adivinhar  
     qual foi!     
\033[m''')

while player_choice != cpu_choice:
    player_choice = int(input('\033[1;35;47mQual número foi sorteado?\033[m'))

    if player_choice != cpu_choice:
        print('\033[1;35;47mTente novamente.\033[m')
        attempt_counter += 1
    
    if player_choice == cpu_choice:
        print('\033[1;35;47mVOCÊ VENCEU!\033[m', '\033[1;35;47mNúmero de tentativas: {}\033[m'.format(attempt_counter))
        

