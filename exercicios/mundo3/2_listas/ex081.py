# Mais outro exercício sobre listas

numlist = []

while True:
    number = int(input('Digite um valor: '))
    numlist.append(number)

    for i in range(0, len(numlist)):
        if numlist[-1] > numlist[-1 + i]:
            numlist.insert(-1 + i, number)
            numlist.pop()

    choice = str(input('Deseja continuar [S/N]? ')).lower().strip()
    
    if choice != 's':
        break

print(f'Você digitou {len(numlist)} elementos')
print(f'Os valores em ordem decrescente são {numlist}')

if 5 in numlist == False:
    print(f'O valor 5 não foi encontrado da lista')
else:
    print(f'O valor 5 faz parte da lista!')