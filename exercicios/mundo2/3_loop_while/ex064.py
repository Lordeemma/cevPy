# Penúltimo exercício sobre o laço while

sum = 0
c = 0

while c != 999:
    add = int(input('Digite um número inteiro: '))
    if add != 999:
        sum += add
    
    c = add

print('Soma total: {}'.format(sum))