# Outro exercício sobre listas

from random import randint

numlist = []

while True:
    number = int(input('Insira um número: '))

    if number in numlist:
        print('Valor duplicado! Não vou adicionar.')
        numlist.append(number)
        numlist.pop()
        
    else:
        numlist.append(number)
        print('Valor adicionado com sucesso!')

    choice = str(input('Deseja continuar [S/N]? ')).lower()
    
    if choice != 's':
        break

numlist.sort()

print(f'Lista de números digitados em ordem crescente: {numlist}')