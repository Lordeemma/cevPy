# Outro exercício sobre o laço for

sum = 0

for i in range (1, 6 + 1):
    n = int(input('Insira o {}º número: '.format(i)))
    
    if n % 2 == 0:
        sum += n

    if i == 6:
        print('A soma dos números pares resultou em {}'.format(sum))
