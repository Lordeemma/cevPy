# Penúltimo exercício sobre interrupção do laço while

print('{:^}'.format('=' * 30))
print('')
print('{:^30}'.format('MERCADO DA'))
print('{:^30}'.format('SÉ'))
print('')
print('{:^}'.format('=' * 30))

greater_thousand = 0
total = 0
cheap_name = 0
cheap_price = 2655923012

while True:

    name = str(input('Insira o nome do produto: '))
    price = float(input('Insira o preço do produto: R$'))

    total += price

    if price > 1000:
        greater_thousand += 1

    if price < cheap_price:
        cheap_name = name
        cheap_price = price

    choice = str(input('Deseja continuar [S/N]? ')).lower().strip()

    print('{:^}'.format('=' * 30))

    if choice != 's':
        break

print(f'Preço total das compras: R${total:.2f}')
print(f'Produtos com preço maior que R$1000: {greater_thousand}')
print(f'O produto com menor preço é {cheap_name}, com um preço de R${cheap_price:.2f}')

    
