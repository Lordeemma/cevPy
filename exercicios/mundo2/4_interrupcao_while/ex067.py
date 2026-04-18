# Outro exercício sobre interrupção do laço while

print('''
===============      

    TABUADA    
     
===============      
      ''')

while True:
    n = int(input('Digite um número e veja sua tabuada: '))

    if n < 0:
        break

    for i in range(1, 10 + 1):
        print(f'{n} x {i} = {n*i}')

    