# Mais outro exercício sobre listas

ord_list = []

for n in range(5):
    number = int(input('Digite um valor: '))

    if number in ord_list:
        ord_list.append(number)
        ord_list.pop()
    else:
        ord_list.append(number)
        for i in range(len(ord_list)):
            if ord_list[-1] < ord_list[-1 + i]:
                ord_list.insert((-1 + i), number)
                ord_list.pop()
    
    if ord_list[ord_list.index(number)] != ord_list[-1]:
        print(f'Adicionado à posição {ord_list.index(number)} da lista')
    else:
        print('Adicionado ao fim da lista')

print('=' * 30)
print(f'Os números digitados em ordem crescente foram {ord_list}')