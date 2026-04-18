# Mais outro exercício sobre o laço while

next = 's'

while next == 's':
    n1 = float(input('Insira um número: '))
    n2 = float(input('Insira outro número: '))

    choice = int(input('''
        Qual operação deseja realizar?
        [1] Somar
        [2] Multiplicar
        [3] Comparar
        [4] Novos números
        [5] Sair 
          '''))
    
    if choice == 1:
        print('{} + {} = {}'.format(n1, n2, n1+n2))
    elif choice == 2:
        print('{} * {} = {}'.format(n1, n2, n1*n2))
    elif choice == 3:
        if n1 > n2:
            print('{} é maior que {}.'.format(n1, n2))
        else:
            print('{} é maior que {}.'.format(n2, n1))
    elif choice == 5:
        next = 'n'
    else:
        continue
