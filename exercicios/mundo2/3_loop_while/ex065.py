# Último exercício sobre o laço while

answer = 's'
sum = 0
c = 0
great = 0
less = 2147483647

while answer == 's':
    add = int(input('Digite um número: '))
    sum += add
    c += 1

    if add > great:
        great = add

    if add < less:
        less = add

    choice = str(input('Deseja continuar [S/N]? '))
    if choice.lower().strip() == answer:
        continue
    else:
        answer = 'n'

print('Média entre os números: {}'.format(sum / c))
print('Menor número: {}'.format(less))
print('Maior número: {}'.format(great))
    
