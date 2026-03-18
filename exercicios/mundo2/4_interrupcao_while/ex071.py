# Último exercício sobre interrupção do laço while

print('{:^}'.format('=' * 30))
print('')
print('{:^30}'.format('BANCO VSF S.A.'))
print('')
print('{:^}'.format('=' * 30))

total_bill = 0

value = int(input('Insira o valor a ser retirado do caixa eletrônico: R$'))

while True:
    for val_bill in [50, 20, 10, 5, 1]:
        if value // val_bill != 0:
            total_bill += value // val_bill
            value -= total_bill * val_bill
            print(f'Notas de R${val_bill}: {total_bill}')
            total_bill = 0
            bill = val_bill
    break

